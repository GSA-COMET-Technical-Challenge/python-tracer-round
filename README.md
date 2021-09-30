# python-tracer-round
Description:

RIVA deploy's a Flask API server due to the fact that it is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. Flask offers suggestions, but doesn’t enforce any dependencies or project layout. It is up to the developer to choose the tools and libraries they want to use. There are many extensions provided by the community that make adding new functionality easy.

Install python packages in requirements.txt

Run python app.py

Local Docker Image Build:
docker build --no-cache -t vault-server .

Run Docker Container Locally:

docker run -p 5000:5000 vault-server
