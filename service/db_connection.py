import os
from util.db.dynamo_table import DynamoTable
from util.db.sql_table import SqlTable
from util.db.mongo_table import MongoTable
from util.db.neo4j_table import Neo4Table
from util.db.lite_table import LiteTable

# ----------------------------------------------
OOTZ_DB_TYPE = os.environ.get(
    'OOTZ_DB_TYPE',
    '''
        <** Escolha um dos tipos de BD **>
        - MySql
        - Postgres
        - MongoDB
        - SqlServer
        - DynamoDB
        - Neo4J
        - Sqlite
    '''
    # Exemplo:
    # OOTZ_DB_TYPE = 'Postgres'
)
OOTZ_USER = os.environ.get(
    'OOTZ_USER',
    '<<** Coloque aqui seu usuário **>>'
)
OOTZ_PASSWORD = os.environ.get(
    'OOTZ_PASSWORD',
    '<<** Coloque aqui sua senha **>>'
)
OOTZ_HOST = os.environ.get(
    'OOTZ_HOST',
    'localhost'
)
# ----------------------------------------------

def get_table(schema):
    db_types = {
        'DynamoDB': lambda: DynamoTable(schema, {
            "service_name": "dynamodb",
            "region_name": "us-west-2",
            "endpoint_url": f"http://{OOTZ_HOST}:8000",
            "aws_access_key_id": OOTZ_USER,
            "aws_secret_access_key": OOTZ_PASSWORD,
        }),
        'SqlServer': lambda: SqlTable(schema, {
            "dialect": "mssql",
            "driver": "pyodbc",
            "username": OOTZ_USER,
            "password": OOTZ_PASSWORD,
            "host": OOTZ_HOST,
            "port": "1433",
            "database": "ootz"
        }),
        'MongoDB': lambda: MongoTable(schema, {
            # "server": "mongodb+srv://",
            "server": "",
            "host_or_user": OOTZ_USER,
            "port_or_password": OOTZ_PASSWORD,
            "database": "Ootz"
        }),
        'Postgres': lambda: SqlTable(schema, {
            "dialect": "postgresql",
            "driver": "psycopg2",
            "username": OOTZ_USER,
            "password": OOTZ_PASSWORD,
            "host": OOTZ_HOST,
            "port": "5432",
            "database": "ootz"
        }),
        'Neo4J': lambda: Neo4Table(schema, {
            "host": OOTZ_HOST,
            "port": 7687,
            "user": OOTZ_USER,
            "password": OOTZ_PASSWORD
        }),
        'Sqlite': lambda: LiteTable(schema, {
            "timeout": 5,
            "cached_statements": 100,
            "uri": True,
            "check_same_thread": True
        }),
        'MySql': lambda: LiteTable(schema, {
            "host": OOTZ_HOST,
            "user": OOTZ_USER,
            "password": OOTZ_PASSWORD,
            "database": "ootz"
        }),
    }
    func = db_types[OOTZ_DB_TYPE]
    return func()
