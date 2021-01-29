# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# export x11 window
RUN export QT_GRAPHICSSYSTEM="native"

# install apt packages
RUN apt-get update && apt-get install -y \
    libgl1-mesa-dev

# copy the dependecies file to the working directory
COPY requirements.txt .

# install dependecies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY app/ .

# command to run on container start
CMD [ "python", "./cxiata.py"]