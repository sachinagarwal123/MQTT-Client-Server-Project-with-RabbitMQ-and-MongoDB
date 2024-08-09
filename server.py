from flask import Flask, request, jsonify
from db_handler import DatabaseHandler
from rabbitmq_handler import RabbitMQHandler

app = Flask(__name__)
db_handler = DatabaseHandler()
rabbitmq_handler = RabbitMQHandler()
rabbitmq_handler.connect()

def process_message(message):
    try:
        db_handler.insert_message(message)
        print(f"Saved Message: {message}")
    except Exception as e:
        raise e

rabbitmq_handler.start_consuming(process_message)

@app.route('/status_counts', methods=['GET'])
def get_status_counts():
    try:
        start_time = int(request.args.get('start_time'))
        end_time = int(request.args.get('end_time'))
        
        status_counts = db_handler.get_status_counts(start_time, end_time)
        
        return jsonify(status_counts)
    except Exception as e:
        raise e

if __name__ == '__main__':
    app.run(debug=True)
