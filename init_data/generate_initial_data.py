import json
import datetime
import random


def generate_seats():
    result = []
    i = 0
    for col in range(12):
        for row in range(10):
            result.append(
                {'id': i,
                 'row': row,
                 'column': col
                 }
            )
            i += 1
    with open('seats.json', 'w') as f:
        json.dump(result, f)


def generate_film():
    result = []
    start_date = datetime.datetime.today()
    for idx, title in enumerate(["Piorun",
                                 "Cruella",
                                 "Nasze magiczne Encanto",
                                 "Kraina lodu",
                                 "Hamilton",
                                 "Gwiazdka Hollywood",
                                 "Lilo i Stitch",
                                 "Czarownica",
                                 "Vaiana: skarb oceanu",
                                 "Muppety",
                                 "Samoloty",
                                 "Raya i ostatni smok",
                                 "Zaplątani",
                                 "Zwierzogród",
                                 "Wyprawa do dżungli",
                                 "Sneakerella",
                                 "Ralph Demolka",
                                 "Mary Poppins powraca",
                                 "Niedźwiedzica polarna"]):
        date = str(start_date + datetime.timedelta(days=random.randint(0, 30))).replace(' ', 'T')
        result.append(
            {'id': idx,
             'title': f"'{title}'",
             'date': f"'{date}'"
             }
        )
    with open('film.json', 'w') as f:
        json.dump(result, f)


def generate_room():
    result = []
    for i in range(1, 10):
        result.append(
            {'id': i,
             'number_of_room': i,
             }
        )
    with open('cinema_room.json', 'w') as f:
        json.dump(result, f)


if __name__ == '__main__':
    generate_seats()
    generate_film()
    generate_room()
