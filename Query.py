from Connector import Connector


class Query:
    def __init__(self, connector: Connector):
        self._connector = connector

    def get_object_by_arg(self, table_name: str, arg_name: str, arg_value):
        query = f"SELECT * FROM {table_name} WHERE {arg_name} = {arg_value};"
        result = self._connector.execute_command(query)
        return result

    def delete(self, table_name: str, id: int):
        query = f"DELETE FROM {table_name} WHERE id = '{id}' IF EXISTS;"
        self._connector.execute_command(query)
