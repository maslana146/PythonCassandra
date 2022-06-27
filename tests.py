import multiprocessing
import os
import random
import time
from multiprocessing import Pool

from Connector import Connector
from Query import Query
from System import System

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


system_1 = get_system()
system_2 = get_system()


def perform_random_actions(i):
    system = get_system()
    for _ in range(50):
        film = random.choice(films)
        seat_col = random.randint(0, 4)
        seat_row = random.randint(0, 4)

        query = system.buy_ticket(film, seat_row, seat_col, str(multiprocessing.current_process().pid))
        print(multiprocessing.current_process().pid, film, seat_row, seat_col, query)


def reserve_all_seats(film: str):
    system = get_system()
    seats = []
    for seat_col in range(5):
        for seat_row in range(5):
            seats.append((seat_col, seat_row))
    random.shuffle(seats)
    for seat in seats:
        # time.sleep(random.random() / 2)
        query = system.buy_ticket(film, seat[0], seat[1], str(multiprocessing.current_process().pid))
        print(multiprocessing.current_process().pid, film, seat[0], seat[1], query)


def test_1():
    t = time.time()
    for i in range(1000):
        system_1.buy_ticket('Hamilton', 2, 3, 'test_1')
    print(time.time() - t)


def test_2():
    t = time.time()
    with Pool(2) as p:
        p.map(perform_random_actions, [1, 2])
    print(time.time() - t)


def test_3():
    t = time.time()
    with Pool(2) as p:
        p.map(reserve_all_seats, ["Lilo i Stitch", "Lilo i Stitch"])
    print(time.time() - t)
