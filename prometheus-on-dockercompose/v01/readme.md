# Prometheus on Docker Compose Ver 1

+ ファイルモードを変更する

```
chmod 0777 -R svr/prometheus
```

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


## イメージ

![](https://docs.google.com/drawings/d/e/2PACX-1vRg7a78VqSl9cPP7OfUyEoS75M0mfncgP71qLVe-pytVQFIFGIiR2P0vU3Y6H0ffN-7QBAbph4Bg4Zw/pub?w=152&h=105)
