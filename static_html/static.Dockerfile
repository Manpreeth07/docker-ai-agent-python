#declare what image to use
FROM python:latest
#docker build -f Dockerfile -t pyapp .
#docker run -it pyapp



#docker build -f Dockerfile -t manpreeth006/ai-py-app-test:latest .
#docker push manpreeth006/ai-py-app-test:latest
WORKDIR /app
#copy local_folder to container_folder
# RUN mkdir -p /static_folder
# COPY ./static_html /static_folder
#RUN echo "hello" > index.html

#docker build -f Dockerfile -t manpreeth006/ai-py-app-test:v1 .
#docker push manpreeth006/ai-py-app-test:v1
COPY ./src /app 
CMD ["python", "-m", "http.server", "8000"]

#python -m http.server 8000
#docker run -it -p 8000:8000 pyapp