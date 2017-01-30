#!/usr/bin/env python3

import pika
import time
from termcolor import cprint
import random

connection = pika.BlockingConnection(
            pika.URLParameters("amqp://admin:admin@192.168.77.151/admin")
            )

channel = connection.channel()
channel.queue_declare('lesson2', durable=True)

def sending():
    x = random.randint(1,6)
    channel.basic_publish(exchange='',                                                                 
                       routing_key='lesson2',
                       body='{}'.format(x),
                       properties=pika.BasicProperties(
                                    delivery_mode = 2)
                       )
    return x

while True:
    time.sleep(1)
    cprint("[#]",'red', attrs=['bold'],end='')
    print(" - sending {} ".format(sending()))
    
     
