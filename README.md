# How to start?

**Run cassandra in docker**

```shell
docker run -p 9042:9042 --rm --name cassandra -d cassandra:latest
```

**Get into container**

```shell
docker exec -it cassandra bash            
```

**Get into cassandra**

```shell
cqlsh
```

**Show all tables**

```cassandraql
USE main;
DESC tables;
```


