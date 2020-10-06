@echo off
REM set OOTZ_DB_TYPE=Neo4J
set OOTZ_DB_TYPE=MySql
REM set OOTZ_DB_TYPE=Postgres
REM set OOTZ_DB_TYPE=MongoDB
REM set OOTZ_DB_TYPE=DynamoDB
REM set OOTZ_DB_TYPE=SqlServer
REM set OOTZ_DB_TYPE=Sqlite

REM set OOTZ_USER=<***usuário***>
REM set OOTZ_PASSWORD=<***senha***>

pip install -r requirements.txt
start python app.py
