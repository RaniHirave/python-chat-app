# Python Chat Application

This is a simple chat application built using Python and Flask. The application allows users to send and receive messages in real-time.

## Project Structure

```
python-chat-app
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   └── templates
│       └── index.html
├── tests
│   ├── __init__.py
│   └── test_app.py
├── Dockerfile
├── Jenkinsfile
├── .github
│   └── workflows
│       └── ci-cd.yml
├── requirements.txt
└── README.md
```

## Requirements

To run this application, you need to have Python 3.x installed along with the following dependencies:

- Flask
- Flask-SocketIO
- Flask-SQLAlchemy

You can install the required packages using pip:

```
pip install -r requirements.txt
```

## Running the Application

To start the application, run the following command:

```
python app/main.py
```

The application will be available at `http://localhost:5000`.

## Testing

To run the tests, use the following command:

```
pytest
```

## Docker

To build the Docker image, run:

```
docker build -t python-chat-app .
```

To run the Docker container, use:

```
docker run -p 5000:5000 python-chat-app
```

## CI/CD

This project includes a Jenkinsfile for CI/CD integration and a GitHub Actions workflow for automated testing and deployment.

## License

This project is licensed under the MIT License.