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

def callback(ch, method, properties, body):
    """
    Callback function to handle received messages.

    Args:
        ch: Channel object.
        method: AMQP method.
        properties: Message properties.
        body: Message body.
    """
    print(f"Received message: {body}")

# Set up a consumer to process messages from the 'first-test' queue
channel.basic_consume(queue='first-test', on_message_callback=callback, auto_ack=True)

print("Waiting for messages ...")

# Start consuming messages indefinitely
channel.start_consuming()