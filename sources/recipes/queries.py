
from adapters.mysql_adapter import MysqlAdapter


class RecipeQueries:

    def __init__(self):
        print("RecipeQueries")
        self.db = MysqlAdapter()

    def get_all_generic_ingredient(self):
        return self.db.get('SELECT * FROM generic_ingredient LIMIT 100')