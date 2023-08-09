import pika
import time

# NOTE: In real world you should get your username and password from a setting file
# That could be a toml file or something like that
# We don't public credentials data in git
credentials = pika.PlainCredentials('mohammad', 'mohammad')

connection_params = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=credentials
)

connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.queue_declare(queue='third-test')
channel.basic_ack


def callback(ch, method, properties, body):
    print(f"Received message: {body}")
    time.sleep(5)
    print("Done!...")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(
    queue='third-test',
    on_message_callback=callback,
)

print("Waiting for messages ...")

channel.start_consuming()
