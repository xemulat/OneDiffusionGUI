# OneDiffusionGUI
Basically a project that I made for school.
It takes the input from the client and sends it to the OneDiffusion server.

# Screenshots
## Normal mode
![image](https://github.com/xemulat/OneDiffusionGUI/assets/98595166/6e046983-004a-4147-942e-88aafacdb51c)

## Translation enabled
![image](https://github.com/xemulat/OneDiffusionGUI/assets/98595166/ab817ef7-f31d-48d0-bffd-dcb69fdae80b)

## Logs
![image](https://github.com/xemulat/OneDiffusionGUI/assets/98595166/4649a60e-c5a2-4514-9443-2c03fd0dc4ac)

# Running
## Server
1. You need python 3.10.xx installed.
2. Depending on your hardware you can choose:

a) Nvidia GPUs.
```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```
b) Older Nvidia GPUs.
```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
c) CPU.
```
pip3 install torch torchvision torchaudio
```
3. Install the rest of the packages.
```
pip install bentoml onediffusion
```
4. Start the OneDiffusion server, replace YOUR/MODEL with a huggingface model. Example: Lykon/DreamShaper.
```
onediffusion start stable-diffusion --model-id YOUR/MODEL
```
5. [OPTIONAL] Set up port forwarding on your router for the port 3000 to connect to the server from other networks.

## Client
1. Clone this repo.
```
git clone https://github.com/xemulat/OneDiffusionGUI
```
2. Install requirements.
```
pip install PyQt5 requests easygoogletranslate
```
3. Edit the line 21 to reflect your setup. Example:
```
r = post('http://127.0.0.1:3000/text2img', headers=self.headers, json=self.payload)
```
4. Run it
```
python main.py
```
