FROM python:latest
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
RUN pip install -r requirements.txt
RUN pip install --upgrade google-cloud-storage
RUN apt-get update
RUN apt install -y libgl1-mesa-glx
# RUN apt-get install ffmpeg libsm6 libxext6  -y
# ENV GOOGLE_APPLICATION_CREDENTIALS="/Users/lolaliu/Desktop/extreme-lore-330419-3cf85f977ccf.json"
CMD ["python3","gui.py"]
