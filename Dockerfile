FROM tensorflow/tensorflow
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
COPY . .
RUN pip3 install -r requirements.txt --no-cache-dir
