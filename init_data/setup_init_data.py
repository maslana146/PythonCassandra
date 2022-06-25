import json

from Connector import Connector

KEYSPACE = 'main'

seats_table = {
    'id': 'int',
    'row': 'int',
    'column': 'int',
}
room_table = {
    'id': 'int',
    'number_of_room': 'int',
}
film_table = {
    'id': 'int',
    'title': 'text',
    'date': 'timestamp'
}
tickets_table = {
    'id': 'int',
    'seat_id': 'int',
    'film_id': 'int',
    'price': 'int',
    'data': 'timestamp'
}
if __name__ == '__main__':
    connector = Connector()
    connector.connect("127.0.0.1", 9042)
    connector.create_keyspace(KEYSPACE)
    connector.set_keyspace(KEYSPACE)

    connector.create_table('tickets', tickets_table, 'id')
    for table in [(seats_table, 'seats'), (room_table, 'cinema_room'), (film_table, 'film')]:
        connector.create_table(table[1], table[0], 'id')
        with open(f'{table[1]}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for idx, i in enumerate(data):
                connector.add_data(i, table[1])
