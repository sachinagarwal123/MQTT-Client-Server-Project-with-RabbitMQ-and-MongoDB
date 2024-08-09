import pika
import json
import threading

class RabbitMQHandler:
    def __init__(self, connection_params='localhost', queue_name='mqtt_messages'):
        try:
            self.connection_params = pika.ConnectionParameters(connection_params)
            self.queue_name = queue_name
            self.connection = None
            self.channel = None
        except Exception as e:
            raise e

    def connect(self):
        try:
            self.connection = pika.BlockingConnection(self.connection_params)
            self.channel = self.connection.channel()
            self.channel.queue_declare(queue=self.queue_name)
        except Exception as e:
            raise e
        
    def publish_message(self, message):
        try:
            self.channel.basic_publish(
                exchange='',
                routing_key=self.queue_name,
                body=message
            )
        except Exception as e:
            raise e

    def start_consuming(self, callback):
        try:
            def on_message(ch, method, properties, body):
                message = json.loads(body)
                callback(message)

            self.channel.basic_consume(
                queue=self.queue_name, 
                on_message_callback=on_message, 
                auto_ack=True
            )
            
            threading.Thread(target=self.channel.start_consuming, daemon=True).start()
        except Exception as e:
            raise e

    def close(self):
        try:
            if self.connection:
                self.connection.close()
        except Exception as e:
            raise e