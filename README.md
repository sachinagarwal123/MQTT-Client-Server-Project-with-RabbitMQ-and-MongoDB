# MQTT-Client-Server-Project-with-RabbitMQ-and-MongoDB

This project implements a client-server system using MQTT messaging via RabbitMQ, with data storage in MongoDB and a Flask endpoint for data retrieval.

## Project Overview

The system consists of two main components:

- **Client Script**: Emits MQTT messages every second with a random "status" value (0-6).
- **Server Script**: Processes incoming MQTT messages, stores them in MongoDB, and provides an HTTP endpoint to retrieve status counts within a specified time range.

## Prerequisites

1. **Python**: Version 3.12
2. **Virtual Environment**: `venv`
3. **RabbitMQ Server**
4. **MongoDB Server**

## Configuration

Ensure that your RabbitMQ and MongoDB servers are running. By default, the scripts connect to:

- RabbitMQ: `localhost:5672`
- MongoDB: `localhost:27017`

If your servers are running on different hosts or ports, you will need to update the connection settings in the scripts accordingly.

## Setup Steps

1. **Clone the Repository**

    ```bash
    git clone {repo_url}
    cd {repo_directory}
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv {environment_name}
    ```

3. **Activate the Virtual Environment**

    - **For Windows Users:**

      ```bash
      {environment_name}\Scripts\activate
      ```

    - **For Linux and Mac Users:**

      ```bash
      source {environment_name}/bin/activate
      ```

4. **Install Dependencies**


    Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. **Set Up RabbitMQ**

    **Download RabbitMQ:**

    - **Windows**: Download the RabbitMQ installer from [RabbitMQ's website](https://www.rabbitmq.com/install-windows.html) and follow the installation instructions.

    - **Linux**: Use the package manager to install RabbitMQ. For example, on Ubuntu:

      ```bash
      sudo apt-get update
      sudo apt-get install rabbitmq-server
      ```

    - **macOS**: Use Homebrew:

      ```bash
      brew install rabbitmq
      ```

    **Start RabbitMQ Server:**

    - **Windows**: RabbitMQ should start automatically. If not, you can start it via the command line:

      ```bash
      rabbitmq-server
      ```

    - **Linux**: Start the RabbitMQ server:

      ```bash
      sudo service rabbitmq-server start
      ```

    - **macOS**: Start RabbitMQ using Homebrew services:

      ```bash
      brew services start rabbitmq
      ```

6. **Set Up MongoDB**

    **Download MongoDB:**

    - **Windows and macOS**: Download the MongoDB installer from the [MongoDB download page](https://www.mongodb.com/try/download/community).

    - **Linux**: Use the package manager to install MongoDB. For example, on Ubuntu:

      ```bash
      sudo apt-get update
      sudo apt-get install -y mongodb
      ```

    **Start MongoDB Server:**

    - **Windows**: MongoDB should start automatically after installation. If not, you can start it via the command line:

      ```bash
      mongod
      ```

    - **Linux**: Start the MongoDB server:

      ```bash
      sudo service mongodb start
      ```

    - **macOS**: Start MongoDB using Homebrew services:

      ```bash
      brew services start mongodb-community
      ```

7. **Run the Server Script**

    In one terminal, start the server script:

    ```bash
    python server.py
    ```

8. **Run the Client Script**

    In a separate terminal, start the client script:

    ```bash
    python client.py
    ```

The client will start sending messages every second, and the server will process and store these messages.
