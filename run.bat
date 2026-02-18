@echo off
REM Activate virtual environment
call venv\Scripts\activate

REM Run FastAPI server
call uvicorn app:app --reload --host 0.0.0.0 --port 8000

pause

@REM Run below command to run ngrok
@REM ngrok http 8000