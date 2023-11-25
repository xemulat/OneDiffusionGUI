from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap
from requests import post
from timeit import default_timer

from easygoogletranslate import EasyGoogleTranslate

class GenerationThread(QThread):
    finished = pyqtSignal(bytes)

    def __init__(self, payload, headers):
        super(GenerationThread, self).__init__()
        self.payload = payload
        self.headers = headers

    def run(self):
        print('[i] Generation started...')
        f = default_timer()
        r = post('http://127.0.0.1:3000/text2img', headers=self.headers, json=self.payload)
        self.finished.emit(r.content)
        t = default_timer()
        print(f'[i] Finished. Took {round(t-f, 1)}s')

class Ui_Form(object):
    def updateImage(self, content):
        pixmap = QPixmap()
        pixmap.loadFromData(content)
        scene = QGraphicsScene()
        item = QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        self.imageViewer.setScene(scene)
        self.pushButton.setEnabled(True)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(794, 584)
        self.imageViewer = QtWidgets.QGraphicsView(Form)
        self.imageViewer.setGeometry(QtCore.QRect(212, 2, 580, 580))
        self.imageViewer.setObjectName("imageViewer")
        self.ItemFrame = QtWidgets.QFrame(Form)
        self.ItemFrame.setGeometry(QtCore.QRect(2, 2, 206, 576))
        self.ItemFrame.setObjectName("ItemFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ItemFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stepsLabel = QtWidgets.QLabel(self.ItemFrame)
        self.stepsLabel.setMaximumSize(QtCore.QSize(16777215, 36))
        self.stepsLabel.setObjectName("stepsLabel")
        self.verticalLayout_2.addWidget(self.stepsLabel)
        self.stepsSlider = QtWidgets.QSlider(self.ItemFrame)
        self.stepsSlider.setMinimum(1)
        self.stepsSlider.setMaximum(150)
        self.stepsSlider.setProperty("value", 35)
        self.stepsSlider.setOrientation(QtCore.Qt.Horizontal)
        self.stepsSlider.setObjectName("stepsSlider")
        self.verticalLayout_2.addWidget(self.stepsSlider)
        self.stepCounter = QtWidgets.QLabel(self.ItemFrame)
        self.stepCounter.setText("")
        self.stepCounter.setObjectName("stepCounter")
        self.verticalLayout_2.addWidget(self.stepCounter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.guidanceLabel = QtWidgets.QLabel(self.ItemFrame)
        self.guidanceLabel.setMaximumSize(QtCore.QSize(16777215, 36))
        self.guidanceLabel.setObjectName("guidanceLabel")
        self.verticalLayout_2.addWidget(self.guidanceLabel)
        self.guidanceSlider = QtWidgets.QSlider(self.ItemFrame)
        self.guidanceSlider.setMinimum(1)
        self.guidanceSlider.setMaximum(30)
        self.guidanceSlider.setSingleStep(1)
        self.guidanceSlider.setProperty("value", 7)
        self.guidanceSlider.setOrientation(QtCore.Qt.Horizontal)
        self.guidanceSlider.setInvertedAppearance(False)
        self.guidanceSlider.setObjectName("guidanceSlider")
        self.verticalLayout_2.addWidget(self.guidanceSlider)
        self.guidnaceCounter = QtWidgets.QLabel(self.ItemFrame)
        self.guidnaceCounter.setMaximumSize(QtCore.QSize(16777215, 10))
        self.guidnaceCounter.setText("")
        self.guidnaceCounter.setObjectName("guidnaceCounter")
        self.verticalLayout_2.addWidget(self.guidnaceCounter)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.promptLabel = QtWidgets.QLabel(self.ItemFrame)
        self.promptLabel.setMaximumSize(QtCore.QSize(16777215, 36))
        self.promptLabel.setObjectName("promptLabel")
        self.verticalLayout_2.addWidget(self.promptLabel)
        self.promptTextBox = QtWidgets.QTextEdit(self.ItemFrame)
        self.promptTextBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.promptTextBox.setObjectName("promptTextBox")
        self.verticalLayout_2.addWidget(self.promptTextBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.negativeLabel = QtWidgets.QLabel(self.ItemFrame)
        self.negativeLabel.setMaximumSize(QtCore.QSize(16777215, 36))
        self.negativeLabel.setObjectName("negativeLabel")
        self.verticalLayout_2.addWidget(self.negativeLabel)
        self.negativeTextbox = QtWidgets.QTextEdit(self.ItemFrame)
        self.negativeTextbox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.negativeTextbox.setObjectName("negativeTextbox")
        self.verticalLayout_2.addWidget(self.negativeTextbox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)

        self.pushButton = QtWidgets.QPushButton(self.ItemFrame)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 120))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)

        self.checkBox = QtWidgets.QCheckBox(self.ItemFrame)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setMinimumSize(QtCore.QSize(0, 30))
        self.verticalLayout_2.addWidget(self.checkBox)


        self.pushButton.clicked.connect(self.generationHandler)

        self.stepsSlider.valueChanged.connect(self.updateStepCounter)

        # Connect guidanceSlider to guidnaceCounter
        self.guidanceSlider.valueChanged.connect(self.updateGuidanceCounter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def updateStepCounter(self, value):
        self.stepCounter.setText(str(value))

    def updateGuidanceCounter(self, value):
        self.guidnaceCounter.setText(str(value))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "OneDiffusion GUI"))
        self.stepsLabel.setText(_translate("Form", "Steps"))
        self.guidanceLabel.setText(_translate("Form", "Guidance"))
        self.promptLabel.setText(_translate("Form", "Prompt"))
        self.negativeLabel.setText(_translate("Form", "Negative"))
        self.pushButton.setText(_translate("Form", "Generate"))
        self.checkBox.setText(_translate("Form", "Translate"))
        
        self.stepCounter.setText(_translate("Form", "40"))
        self.guidnaceCounter.setText(_translate("Form", "7"))

    def generationHandler(self):
        self.pushButton.setEnabled(False)
        stepsVar = self.stepsSlider.value()
        guidanceVar = self.guidanceSlider.value()
        promptVar = self.promptTextBox.toPlainText()
        negVar = self.negativeTextbox.toPlainText()
        
        translateBool = self.checkBox.checkState()
        
        if translateBool == 2:
            translator = EasyGoogleTranslate(
                target_language='en',
                timeout=10
            )
            promptVar = translator.translate(promptVar)
        print(f'[d] Prompt: {promptVar}\n[d] Steps: {stepsVar}\n[d] Guidance: {guidanceVar}')


        payload = {
            "prompt": promptVar,
            "negative_prompt": negVar,
            "height": 576,
            "width": 576,
            "num_inference_steps": stepsVar,
            "guidance_scale": guidanceVar,
            "eta": 0,
            "lora_weights": None
        }

        headers = {'accept': 'image/jpeg', 'Content-Type': 'application/json'}

        self.generation_thread = GenerationThread(payload, headers)
        self.generation_thread.finished.connect(self.updateImage)
        self.generation_thread.start()

    def closeEvent(self, event):
        if hasattr(self, 'generation_thread') and self.generation_thread.isRunning():
            self.generation_thread.terminate()
            self.generation_thread.wait()

app = QtWidgets.QApplication([])
MainWindow = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(MainWindow)
MainWindow.show()
app.exec_()
