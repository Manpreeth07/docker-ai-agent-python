#declare what image to use
FROM python:latest

#host.docker.internal ->localhost
#curl -X POST -d '{"message":"Hello world"}' -H "Content-Type: application/json" http://host.docker.internal:8080/api/chats/
RUN apt-get update && apt-get install -y curl
#create a python virtual environment
#isolate python dependencies from the system python
RUN python -m venv /opt/venv/
ENV PATH=/opt/venv/bin:$PATH

WORKDIR /app
#copy local_folder to container_folder
COPY requirements.txt /tmp/requirements.txt
#run pip install to install dependencies
RUN pip install -r /tmp/requirements.txt
COPY ./src /app 
CMD ["python", "-m", "http.server", "8000"]
