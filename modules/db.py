import pandas as pd

class DB:
    
    # TODO: check parameters and how to pass it to query
    def query(self, query_str: str, parameters):
        return pd.read_csv('data/hw_health_daily.csv')
