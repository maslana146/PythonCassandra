from Connector import Connector
from Query import Query


class System:
    def __init__(self, query: Query):
        self._query = query
        self._id = 0

    def buy_ticket(self, title: str, row_seat: int, col_seat: int, user: str):
        film = self._query.select_query(['*'], 'film', [("title", '=', f"'{title}'")]).one()
        if not film:
            return "Film not found."
        seat = self._query.select_query(['*'], 'seats', [('column', '=', f'{col_seat}'),
                                                         ('row', '=', f'{row_seat}'),
                                                         ('free', '=', True),
                                                         ('cinema_room', '=', f'{film["cinema_room"]}')]).one()
        if not seat:
            return "Seat is already reserved"
        seat['free'] = False
        # time.sleep(1)
        self._query.add_data(seat, 'seats')
        tickets = self._query.select_query(['*'], 'tickets', []).all()
        if tickets:
            max_id = max(tickets, key=lambda x: x['id'])['id']
        else:
            max_id = 0
        ticket = {
            'id': max_id + 1,
            'seat_id': seat['id'],
            'film_id': film['id'],
            'price': 666,
            'data': f"'{film['date']}'",
            'user': f"'{user}'"
        }

        self._query.add_data(ticket, 'tickets')
        return ticket

    def get_all_tickets(self, title: str):
        film = self._query.select_query(['*'], 'film', [("title", '=', f"'{title}'")]).one()
        if not film:
            return "Film not found."
        results = self._query.select_query(['*'], 'tickets', [('film_id', '=', film['id'])]).all()
        return results


if __name__ == '__main__':
    connector = Connector()
    connector.connect("127.0.0.1", 9042)
    connector.set_keyspace('main')
    system = System(Query(connector))
    # res = system.buy_ticket('Piorun', 2, 1)
    res = system.get_all_tickets('Piorun')
    print(res)
