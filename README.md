# Face/Object Recognition

# Docker

Build image

    $ docker build -t opencv:v1.0 .

Run image and share some volume to make possible to store changes in your local machine

    $ docker run -d --name elbarto -p 8888:8888 -v ~/Node/dilan/elbarto/face-recognition:/home elbarto:v1.0

Fetch Jupyter's token

    $ docker logs elbarto

... it will be something like this:

    The Jupyter Notebook is running at:
    http://0.0.0.0:8888/?token=679cd547537772e8f7723999db152bdb7c30169d71c1e159


# In case you want to jump inside container:

    $ docker exec -it elbarto bash