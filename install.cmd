@echo off

:: Nombre del directorio del entorno virtual
set VIRTUAL_ENV_NAME=myenv

:: Verificar si el entorno virtual ya existe
if exist %VIRTUAL_ENV_NAME% (
    echo El entorno virtual "%VIRTUAL_ENV_NAME%" ya existe.
) else (
    :: Crear un nuevo entorno virtual
    echo Creando un nuevo entorno virtual "%VIRTUAL_ENV_NAME%"...
    python -m venv %VIRTUAL_ENV_NAME%
)

:: activar entorno
call myenv\Scripts\activate

:: Instalar las dependencias desde requirements.txt
if exist requirements.txt (
    echo Instalando las dependencias desde requirements.txt...
    pip install -r requirements.txt
) else (
    echo El archivo requirements.txt no se encontró en el directorio actual.
)
