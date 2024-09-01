@echo off
if "%1"=="run" (
    shift
    python D:\WTF\lazy.py %1
) else (
    echo Usage: lazy run ^<filename^>.lazy
)
