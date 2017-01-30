#!/usr/bin/env python3

from threading import Thread
import time
import pika
from termcolor import cprint

class Worker(Thread):
    def __init__(self,worker_id):
        cprint("[x]", 'green', end='')
        cprint(' - worker started with id {}'.format(worker_id))
        Thread.__init__(self)
        self.worker_id = worker_id
        self.connection = pika.BlockingConnection(
            pika.URLParameters("amqp://admin:admin@192.168.77.151/admin")
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare('lesson2', durable=True)
        self.channel.basic_qos(prefetch_count=2)
        self.channel.basic_consume(
                      Worker.handler,
                      queue='lesson2',
                      )
        self.channel.worker_id = self.worker_id
        

    @staticmethod
    def handler(ch, method, properties, body):
        cprint("[x]", 'green', end='')
        print(" - received {} in worker {} ".format(int(body.decode('utf8')), ch.worker_id))
        time.sleep(int(body.decode('utf8')))
        ch.basic_ack(delivery_tag = method.delivery_tag)
    
    def run(self):
        self.channel.start_consuming()
        
        
if __name__ == '__main__':
    workers = []
    for i in range(5):
        workers.append(Worker(i))
    for worker in workers:
        worker.start()
            
