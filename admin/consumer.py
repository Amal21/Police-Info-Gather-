import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from recherches.models import Recherche

params = pika.URLParameters('amqps://dumytatf:swqlCqfIC71HaotdI8N9m8fSzbR0Qy2Z@toad.rmq.cloudamqp.com/dumytatf')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    id = json.loads(body)
    print(id)
    recherche = Recherche.objects.get(id=id)
    #product.likes = product.likes + 1
    recherche.save()
    print('recherche likes increased!')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
