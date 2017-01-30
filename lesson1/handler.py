#!/usr/bin/env python3

import pika
import time
from termcolor import cprint

connection = pika.BlockingConnection(
            pika.URLParameters("amqp://admin:admin@192.168.77.151/admin")
            )

channel = connection.channel()
channel.queue_declare('test')

def handler(ch, method, properties, body):
    cprint("[#] - received {}".format(body), 'green')

channel.basic_consume(handler,
                      queue='test',
                      no_ack=True)

channel.start_consuming()
