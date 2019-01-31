@echo off
if exist .setupcomplete (python main.py) else (setup && python main.py && echo. > .setupcomplete)