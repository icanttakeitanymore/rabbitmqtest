#!/usr/bin/env python3

import pika
import time
from termcolor import cprint

connection = pika.BlockingConnection(
            pika.URLParameters("amqp://admin:admin@192.168.77.151/admin")
            )

channel = connection.channel()
channel.queue_declare('test')

def sending():
    channel.basic_publish(exchange='',                                                                 
                       routing_key='test',
                       body='test rabbit mq')

while True:
    time.sleep(3)
    cprint("[#] - sending ", 'red', attrs=['bold'])
    sending()
    
