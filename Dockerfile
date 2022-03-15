FROM python:3.8
LABEL Maintainer="Hassan_Ahmed"
WORKDIR /app
COPY requirements.txt .
COPY cv_api/ /app
RUN pip install --upgrade pip
RUN apt-get update 
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install cmake==3.22.3
RUN pip3 install -r requirements.txt
CMD  ["python3" , "/app/manage.py" , "runserver" , "0.0.0.0:8000"]
