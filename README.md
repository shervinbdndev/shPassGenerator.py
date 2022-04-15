<h1 align='center' style="font-size:5rem"><b>shPassGenerator</b></h1>
<p align='center'><b>Version 1.0.4</b></p>
<div align="center">
    <div align="center">
        <img src="https://img.shields.io/github/license/shervinbdndev/shPassGenerator.svg"></img>
    </div>
    <img src="https://img.shields.io/github/forks/shervinbdndev/shPassGenerator.svg"></img>
    <img src="https://img.shields.io/github/stars/shervinbdndev/shPassGenerator.svg"></img>
    <img src="https://img.shields.io/github/watchers/shervinbdndev/shPassGenerator.svg"></img>
    <img src="https://img.shields.io/github/issues-pr/shervinbdndev/shPassGenerator.svg"></img>
    <img src="https://img.shields.io/github/issues-pr-closed/shervinbdndev/shPassGenerator.svg"></img>
    <img src="https://img.shields.io/github/downloads/shervinbdndev/shPassGenerator/total.svg"></img>
</div>
<br>
<div align="center">
    <img style="display:block;margin-left:auto;margin-right:auto;width:70%;" src="https://github-readme-stats.vercel.app/api/pin/?username=shervinbdndev&repo=shPassGenerator&theme=dracula"></img>
</div>
<br>
<h3 align='center'>Under construction! Not ready for use yet! Currently experimenting and planning!</h3>
<h3 align='center'>Developed by Shervin Badanara (shervinbdndev) on Github</h3>
<div align="center">
    <img src="https://forthebadge.com/images/badges/made-with-python.svg"></img>
</div>
<br>
<hr>
<br>
<h2 align='center'><b>Language and technologies used in This Project</h2>
<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"></img>
<img src="https://img.shields.io/badge/Google_chrome-4285F4?style=for-the-badge&logo=Google-chrome&logoColor=white"></img>
<img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white"></img>
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"></img>
<img src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white"></img>
<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></img>
<img src="https://img.shields.io/badge/Stack_Overflow-FE7A16?style=for-the-badge&logo=stack-overflow&logoColor=white"></img>
<img src="https://img.shields.io/badge/Reddit-FF4500?style=for-the-badge&logo=reddit&logoColor=white"></img>

<br>
<h2 align='center'><b>WorkSpace</h2>
<img src="https://img.shields.io/badge/Intel-Core_i5_10700K-0071C5?style=for-the-badge&logo=intel&logoColor=white"></img>
<img src="https://img.shields.io/badge/NVIDIA-RTX2060 OC-76B900?style=for-the-badge&logo=nvidia&logoColor=white"></img>
<img src="https://img.shields.io/badge/Windows11-0078D6?style=for-the-badge&logo=windows&logoColor=white"></img>


<hr>

<br><br><br>
<h1 align='left'><b>Update Your Interpreter</b></h1>

# Windows / CMD

```python
py -m pip install --upgrade pip
```

# Linux / Terminal

```python
python -m pip install --upgrade pip
```
<br>

<hr>
<br><br><br>
<h1 align='left'><b>Installation</b></h1>
 
# Windows / CMD , Linux / Terminal
```python
pip install shPassGenerator
```
<h2 align='left'>or</h2>

```python
py -m pip install shPassGenerator
```

<br><br><br>
<h1 align='left'><b>Update Library</b></h1>
 
# Windows / CMD , Linux / Terminal
```python
pip install -U shPassGenerator
```

<h2 align='left'>or</h2>

```python
py -m pip install --upgrade shPassGenerator
```

<br>

<hr>
<br><br><br>
<h1 align='left'><b>Usage</b></h1>

Args  |  Type   |  Efficiency
------------- | ------------- | -------------
length  | Integer | Set The Length of your Password (Max Length is Unlimited)
chars  |  Boolean  | Use Lowercase & Uppercase Characters in Your Password
lowercase  |  Boolean  |  Use Lowercase Characters in Your Password
uppercase  |  Boolean  |  Use Uppercase Characters in Your Password
numbers  |  Boolean  |  Use Numbers in Your Password
symbols  |  Boolean  |  Use Symbols in Your Password
octal  |  Boolean  |  Use Octal Characters in Your Password
hexa  |  Boolean  |  Use Hexa Characters in Your Password

<br>

<b>Generate Strong Passwords</b>

```python
from shPassGenerator import GeneratePass


print(f"This Password is Strong : {GeneratePass(length=16 , lowercase=True)}")
print(f"This Password is Strong too : {GeneratePass(length=50 , chars=True , symbols=True)}")
```
<b>Output</b>

```md
This Password is Strong : umvgfarzfirmuesc
This Password is Strong too : aU;/k.ofD-d@ZoCeLgaOui/=zdr)n#o@KKi%e[D'`I>$vpHNzT
```

<br><br><br>
<hr>
<h1 align='left'>Enjoy :)</h1>

<br>
<h3><b>Package Uploaded in PYPI :<a href="https://pypi.org/project/shPassGenerator/">Here</a></b></h3>