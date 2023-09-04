@echo off
setlocal

set "INPUT_UI_FILE=%~1"

set "OUTPUT_PY_FILE=%~2"

pyuic5 -x "%INPUT_UI_FILE%" -o "%OUTPUT_PY_FILE%"

endlocal
