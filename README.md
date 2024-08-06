# Sample Code App

This is a simple PyQt5 application that opens a window with the title "Sample App."

## Setup

To set up the project, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Install the package to create the executable
```bash
pip install pyinstaller
```

## Building the Executable

```bash
pyinstaller --onefile main.py    
```
This will create the executable file as you need but when you run the .exe file, you will see a console which will show the standard output on executing the file. To avoid it, use:
```bash
pyinstaller --onefile --noconsole main.py
```
Your final app window will be displayed. 


### Customizing the .exe file.
To set a custom icon for your executable, you need an .ico file. You can create one using an online converter or an image editing tool that supports the .ico format.
Once you have your icon file, use the --icon option in the PyInstaller command to specify the icon:
```
pyinstaller --onefile --noconsole --icon=path/to/your/icon.ico your_script.py
```
Replace path/to/your/icon.ico with the path to your .ico file and your_script.py with your Python script's name.

To change the name of the executable, use the --name option:
```
pyinstaller --onefile --noconsole --name=CustomAppName main.py
```
Change 'CustomAppName' with the name you wish to use.

#### Full Example Command
```
pyinstaller --onefile --noconsole --icon=path/to/your/icon.ico --name=CustomAppName main.py
```
