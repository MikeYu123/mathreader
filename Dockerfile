FROM tensorflow/tensorflow
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . .
ENTRYPOINT [ "python" ]
CMD [ "server.py" ]
