import pika


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

channel.queue_declare(queue='second-test')


def callback(ch, method, properties, body):
    print(f"Received message: {body}")

channel.basic_consume(
    queue='second-test',
    on_message_callback=callback,
    auto_ack=True
)

print("Waiting for messages ...")

channel.start_consuming()
