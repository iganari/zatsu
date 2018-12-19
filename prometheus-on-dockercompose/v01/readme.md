# Prometheus on Docker Compose Ver 1

+ 起動

```
docker-compose up -d
```

```
$ docker ps
CONTAINER ID        IMAGE                    COMMAND             CREATED             STATUS              PORTS                
    NAMES
541244a0e2e3        prom/prometheus:v2.6.0   "/bin/prometheus"   6 minutes ago       Up About a minute   0.0.0.0:9090->9090/tcp   prometheus_on_dockercompose
```
```
$ docker-compose ps
           Name                   Command       State           Ports         
------------------------------------------------------------------------------
prometheus_on_dockercompose   /bin/prometheus   Up      0.0.0.0:9090->9090/tcp      
```

+ 停止

```
docker-compose stop
```

+ 削除

```
docker-compose rm (-f)
```
