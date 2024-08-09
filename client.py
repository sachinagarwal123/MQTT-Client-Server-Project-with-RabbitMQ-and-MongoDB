import json
import time
import random
from rabbitmq_handler import RabbitMQHandler

class Client:
    def __init__(self):
        try:
            self.rabbitmq_handler = RabbitMQHandler()
            self.rabbitmq_handler.connect()
        except Exception as e:
            raise e

    def generate_message(self):
        try:
            return {
                'timestamp': int(time.time()),
                'status': random.randint(0, 6)
            }
        except Exception as e:
            raise e

    def run(self):
        try:
            while True:
                message = self.generate_message()
                message_json = json.dumps(message)
                
                self.rabbitmq_handler.publish_message(message_json)
                
                print(f"Sent message: {message_json}")
                time.sleep(1)
        except Exception as e:
            raise e

    def close(self):
        self.rabbitmq_handler.close()

if __name__ == '__main__':
    client = Client()
    try:
        client.run()
    except KeyboardInterrupt:
        print("Shutting down client...")
    finally:
        client.close()