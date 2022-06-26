import json
import datetime
import random

FILMS = ["Piorun",
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
         "Niedźwiedzica polarna"]


def generate_seats():
    result = []
    j = 0
    for i in range(len(FILMS)):
        for col in range(5):
            for row in range(5):
                result.append(
                    {'id': j,
                     'row': row,
                     'column': col,
                     'free': True,
                     'cinema_room': i
                     }
                )
                j += 1
    with open('seats.json', 'w') as f:
        json.dump(result, f)


def generate_film():
    result = []
    date = str(datetime.datetime.today()).replace(' ', 'T')
    for idx, title in enumerate(FILMS):

        result.append(
            {'id': idx,
             'title': f"'{title}'",
             'date': f"'{date}'",
             'cinema_room': idx
             }
        )
    with open('film.json', 'w') as f:
        json.dump(result, f)


def generate_room():
    result = []
    for i in range(len(FILMS)):
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
