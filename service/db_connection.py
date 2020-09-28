from util.db.neo4j_table import Neo4Table

def get_table(schema):
    return Neo4Table(schema, {
                "host": "localhost",
                "port": 7687,
                "user": "neo4j",
                "password": "1234"
            })