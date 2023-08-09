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

channel.queue_declare(queue='third-test')

message_body = 'Hello, world!...'

channel.basic_publish(exchange='', routing_key='third-test', body=message_body)

print(f"Message sent to 'third-test' queue: {message_body}")

connection.close()
