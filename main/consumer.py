import pika, json

from main import Recherche,db

params = pika.URLParameters('amqps://dumytatf:swqlCqfIC71HaotdI8N9m8fSzbR0Qy2Z@toad.rmq.cloudamqp.com/dumytatf')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in main')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'recherche_created':
        recherche = Recherche(id=data['id'], cin=data['cin'], description=data['description'])
        db.session.add(recherche)
        db.session.commit()
        print('recherche Created')

    elif properties.content_type == 'recherche_updated':
        recherche = Recherche.query.get(data['id'])
        recherche.cin = data['cin']
        recherche.description = data['description']
        db.session.commit()
        print('recherche Updated')

    elif properties.content_type == 'recherche_deleted':
        recherche = Recherche.query.get(data)
        db.session.delete(recherche)
        db.session.commit()
        print('recherche Deleted')


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
