@ECHO OFF
@echo Iniciando Entorno virtual e instalando dependencias...
@echo Starting virual environment and Installing dependecies...
powershell env/Scripts/activate.ps1; pip install -r requirements.txt