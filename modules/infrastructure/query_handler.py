from pandas import DataFrame
from modules.db import DB


class QueryHandler:
    def __init__(self):
        self.db_connection = DB()
    
    
    def query(self, query: str, parameters) -> DataFrame:
        return self.db_connection.query(query, parameters)
