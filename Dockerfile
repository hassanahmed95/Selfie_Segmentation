FROM python:3.8
LABEL Maintainer="Hassan_Ahmed"
WORKDIR /app
COPY requirements.txt .
COPY cv_api/ /app
RUN apt-get update && apt-get install -y
RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get install -y \
        build-essential \
        cmake \
        git \
        wget \
        unzip \
        yasm \
        pkg-config \
        libswscale-dev \
        libtbb2 \
        libtbb-dev \
        libjpeg-dev \
        libpng-dev \
        libtiff-dev \
        libavformat-dev \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*
RUN pip install -U opencv-python dlib
RUN pip3 install -r requirements.txt
#CMD  ["python3" , "/app/manage.py" , "runserver" , "0.0.0.0:8000"]
CMD  ["python3" , "/app/main.py"]
