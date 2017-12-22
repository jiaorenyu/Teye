#!/bin/bash

if [ $# != 1 ]; then
    echo "usage: bash $(basename $0) type(start|stop|restart)"
    exit
fi

pidfile=run/server.pid

type=$1

if [ "$type" == "start" ]; then
    nohup python3 server.py --configfile=conf/server.conf &
    ps -ef | grep server
elif [ "$type" == "stop" ]; then
    kill -9 `cat $pidfile`
    ps -ef | grep server
elif [ "$type" == "restart" ]; then
    kill -9 `cat $pidfile`
    nohup python3 server.py --configfile=conf/server.conf &
    ps -ef | grep server
fi
