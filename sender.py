
import pika


# Create the connection parameters
connection_params = pika.ConnectionParameters(
    host="localhost",  # Replace with appropriate host if needed
    port=5672          # Default AMQP port
)

# Establish a connection to the RabbitMQ server
connection = pika.BlockingConnection(connection_params)

# Create a channel for communication
channel = connection.channel()

# Declare a queue named 'first-test'
channel.queue_declare(queue='first-test')

# Publish a message to the 'first-test' queue
message_body = 'Hello, world!!..'

channel.basic_publish(exchange='', routing_key='first-test', body=message_body)

print(f"Message sent to 'first-test' queue: {message_body}")

# Close the connection
connection.close()