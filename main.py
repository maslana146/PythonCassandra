# from Connector import Connector
# from Query import Query
#
# connector = Connector()
# KEYSPACE = 'main'
# connector.connect("127.0.0.1", 9042)
# connector.set_keyspace(KEYSPACE)
# query = Query(connector)
# z = query.select_query(['*'], 'film', [
#     ('title', '=', "'Piorun'")
# ])
# a = 1
import multiprocessing
import random
from multiprocessing import Pool

from Connector import Connector
from Query import Query
from System import System
import os

from tests import test_1

os.environ['PYTHONUNBUFFERED'] = '1'
films = ["Zwierzogród",
         "Wyprawa do dżungli",
         "Sneakerella",
         "Ralph Demolka",
         "Mary Poppins powraca",
         "Niedźwiedzica polarna"]


def get_system():
    connector = Connector()
    connector.connect("127.0.0.1", 9042)
    connector.set_keyspace('main')
    return System(Query(connector))


# system_1 = get_system()
# system_2 = get_system()


def perform_random_action(i):
    system = get_system()
    for _ in range(50):
        film = random.choice(films)
        seat_col = random.randint(0, 4)
        seat_row = random.randint(0, 4)

        query = system.buy_ticket(film, seat_row, seat_col)
        print(multiprocessing.current_process().pid, film, seat_row, seat_col, query)
    # return query


# def test_1():
#     for i in range(100):
#         query = system_1.buy_ticket('Hamilton', 2, 2)
#         print(query)
#     print(system_1.get_all_tickets('Hamilton'))


def dupa():
    # p = Pool(2)
    # for i in range(2):
    with Pool(2) as p:
        p.map(perform_random_action, [1, 2])
        # p.apply_async(perform_random_action, [])

if __name__ == '__main__':
    system = get_system()
    print(system.get_all_tickets("Cruella"))
