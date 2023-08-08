import pika


credentials = pika.PlainCredentials('mohammad', 'mohammad')

connection_params = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=credentials
)

connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.queue_declare(queue='second-test')

message_body = 'Hello, world!!..'

channel.basic_publish(exchange='', routing_key='second-test', body=message_body)

print(f"Message sent to 'second-test' queue: {message_body}")

connection.close()