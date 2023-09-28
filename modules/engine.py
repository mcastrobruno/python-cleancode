from modules.query_handler import QueryHandler


class Engine:

    def __init__(self):
        self.query_handler = QueryHandler()

    def run(self):
        df = self.query_handler.query("Select * From tbl_health_daily", None)
        print(df)
