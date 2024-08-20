@echo off

REM Download and install Python 3
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.9.9/python-3.9.9-amd64.exe', 'python-installer.exe')"
python-installer.exe /quiet InstallAllUsers=1 PrependPath=1

REM Install PyQt5, PIL, pytesseract, and other modules using pip
python -m pip install pyqt5 pillow pytesseract pyqt5-tools

REM Download and install Tesseract
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://github.com/UB-Mannheim/tesseract/wiki/tesseract-ocr-w64-setup-v5.0.0-alpha.20210811.exe', 'tesseract-installer.exe')"
tesseract-installer.exe /S

REM Clean up downloaded installers
del python-installer.exe
del tesseract-installer.exe