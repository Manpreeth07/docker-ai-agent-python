#declare what image to use
FROM python:latest

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
