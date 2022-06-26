from typing import List, Tuple

from Connector import Connector


class Query:
    def __init__(self, connector: Connector):
        self._connector = connector

    def select_query(self, columns: List[str], table_name: str, conditions: List[Tuple]):
        qury_conditions = []
        for condition in conditions:
            qury_conditions.append(f"{condition[0]} {condition[1]} {condition[2]}")
        qury_conditions = ' AND '.join(qury_conditions)
        if conditions:
            query = f"SELECT {', '.join(columns)} FROM {table_name} WHERE {qury_conditions} ALLOW FILTERING;"
        else:
            query = f"SELECT {', '.join(columns)} FROM {table_name} ALLOW FILTERING;"
        try:
            result = self._connector.execute_command(query)
            return result
        except Exception as e:
            raise ValueError(f'Invalid query: {query} raise error: {e}')

    def delete_by_id(self, table_name: str, id: int):
        query = f"DELETE FROM {table_name} WHERE id = '{id}' IF EXISTS;"
        self._connector.execute_command(query)

    def add_data(self, data: dict, table_name: str):
        query = f"INSERT INTO {table_name} (" + ', '.join(
            data.keys()) + ")" + f" VALUES (" + ', '.join([str(i) for i in data.values()]) + ");"
        try:
            self._connector.execute_command(query)
        except Exception as e:
            raise ValueError(f'Invalid query: {query} raise error: {e}')
