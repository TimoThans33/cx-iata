# CX-IATA

Graphical User Interface build with Qt for data analysis of the IATA system from Prime Vision.

## Getting started

```
pip install requirements.txt
```
On linux instead of exporting python path you can
```
python3 setup.py install
```
```
python3 cx-iata.py
```

## Creating a windows exe

For creating a windows exe I used pyinstaller. Pyinstaller is a python Distutils extension which converts Python scripts into executable Windows programs, able to run without requiring a python installation.
```
pip install pyinstaller
```
```
pyinstaller cxiata.py --onefile --clean
```
This will create an .exe file in the dist folder.

## Docker container

Not working yet.