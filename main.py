from Connector import Connector

connector = Connector()

connector.connect("127.0.0.1", 9042)
keyspace = 'test'
test_table = {'name': 'text',
              'age': 'int',
              'id': 'int'}

connector.create_keyspace(keyspace)
connector.set_keyspace(keyspace)
connector.create_table('test_tabela', test_table, 'id')
z = 1

t = 1
