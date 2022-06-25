from Connector import Connector
from Query import Query

connector = Connector()
KEYSPACE = 'main'
connector.connect("127.0.0.1", 9042)
connector.set_keyspace(KEYSPACE)
query = Query(connector)
z = query.get_object_by_arg('film','title','Samoloty')
a = 1