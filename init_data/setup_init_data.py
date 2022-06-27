import json
import time

from Connector import Connector
from Query import Query

KEYSPACE = 'main'

seats_table = {
    'id': 'int',
    'row': 'int',
    'column': 'int',
    'free': 'boolean',
    'cinema_room': 'int'

}
room_table = {
    'id': 'int',
    'number_of_room': 'int',
}
film_table = {
    'id': 'int',
    'title': 'text',
    'date': 'timestamp',
    'cinema_room': 'int',

}
tickets_table = {
    'id': 'int',
    'seat_id': 'int',
    'film_id': 'int',
    'price': 'int',
    'data': 'timestamp',
    'user': 'text',
}


def setup_init_config():
    connector = Connector()
    connector.connect("127.0.0.1", 9042)
    connector.create_keyspace(KEYSPACE)
    connector.set_keyspace(KEYSPACE)
    connector.create_table('tickets', tickets_table, 'id')
    query = Query(connector)
    for table in [(seats_table, 'seats'), (room_table, 'cinema_room'), (film_table, 'film')]:
        connector.create_table(table[1], table[0], 'id')
        time.sleep(3)
        with open(f'{table[1]}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for idx, i in enumerate(data):
                query.add_data(i, table[1])
    connector.disconnect()


if __name__ == '__main__':
    setup_init_config()
