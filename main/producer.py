import pika, json

params = pika.URLParameters('amqps://dumytatf:swqlCqfIC71HaotdI8N9m8fSzbR0Qy2Z@toad.rmq.cloudamqp.com/dumytatf')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
