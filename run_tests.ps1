Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv\Scripts\python.exe -m pytest -v

exit $LASTEXITCODE