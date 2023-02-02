# Python is the name of the image we are using, after : is the tag you can find in the docker hub website
FROM python:3.9.2

# Set the working directory to /app, you can find the path when you type 'pwd' in the terminal
WORKDIR /python-docker

ADD server2.py .

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "server2.py" ]