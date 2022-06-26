from cassandra.cluster import Session, Cluster, NoHostAvailable
from cassandra.query import dict_factory

class Connector:
    def __init__(self, default_time_out: int = 60):
        self._session: Session = None
        self._default_time_out = default_time_out

    def set_keyspace(self, name: str, set_global: bool = True) -> None:
        self._session.execute(f"USE {name}")
        if set_global:
            self._session.set_keyspace(name)

    def create_keyspace(self, name: str, replication_factor: int = 3, strategy: str = 'SimpleStrategy') -> None:
        exec_command: str = f"CREATE KEYSPACE IF NOT EXISTS {name}   WITH REPLICATION = " + \
                            "{" + f"'class' : '{strategy}', 'replication_factor' : {replication_factor} " + "};"
        self.execute_command(exec_command)
        # self._session.row_factory

    def create_table(self, name: str, table: dict, pk: str) -> None:
        if pk not in table.keys():
            raise KeyError(f"Give PK {pk} not in column names.")
        exec_command: str = f"CREATE TABLE IF NOT EXISTS {name} ("
        for name, col_type in table.items():
            exec_command += f'{name} {col_type},'
        exec_command += f"PRIMARY KEY({pk}));"
        self.execute_command(exec_command)

    def drop_table(self, name: str):
        exec_command: str = f"DROP TABLE IF EXISTS {name};"
        self.execute_command(exec_command)

    def execute_command(self, command: str):
        if self._session:
            result = self._session.execute(command)
            return result
        raise KeyError(f"Session is not setup.")

    def connect(self, ip_address: str, port: int) -> None:
        cluster: Cluster = Cluster([ip_address], port)

        try:
            self._session = cluster.connect()
            self._session.default_timeout = self._default_time_out
            self._session.row_factory = dict_factory
        except (NoHostAvailable) as error:
            raise ConnectionError(f"DB is unreachable: {error}")

    def disconnect(self):
        if self._session:
            self._session.shutdown()
