# Face/Object Recognition

Steps:

    $ git clone https://github.com/Dilan/elbarto.git ~/projects/elbarto
    $ cd ~/projects/elbarto
    $ docker pull hackerloft/opencv:v1.0
    $ docker run -d --name elbarto -p 8888:8888 -v ~/projects/elbarto/face-recognition:/home hackerloft/opencv:v1.0
    $ docker exec -it elbarto python /home/get_faces.py /home/test-data/test_Diana_Vera.jpg /home/output/


# Docker

Build image

    $ docker build -t opencv:v1.0 .

... or just pull it from hub.docker.com

    docker pull hackerloft/opencv:v1.0

Run image and share some volume to make possible to store changes in your local machine

    $ docker run -d --name elbarto -p 8888:8888 -v ~/projects/elbarto/face-recognition:/home hackerloft/opencv:v1.0

Fetch Jupyter's token

    $ docker logs elbarto

... it will be something like this:

    The Jupyter Notebook is running at:
    http://0.0.0.0:8888/?token=679cd547537772e8f7723999db152bdb7c30169d71c1e159


# In case you want to jump inside container:

    $ docker exec -it elbarto bash

# Convert notebook to script

    # (inside container)
    $ jupyter nbconvert --to script /home/DetectFace.ipynb --stdout > /home/DetectFace.py
    # (outside container)
    $ docker exec -it elbarto jupyter nbconvert --to script /home/DetectFace.ipynb

# Find faces and save to "output" folder

    $ docker exec -it elbarto python /home/get_faces.py /home/test-data/test_Diana_Vera.jpg /home/output/

Useful Links

    https://github.com/caesar0301/awesome-public-datasets

    https://www.pyimagesearch.com/

    https://github.com/informramiz/Fully-Convolutional-Networks/blob/master/CarND-Object-Detection-Lab.ipynb

    https://blog.openai.com/universe/

    # pandas
    https://bitbucket.org/hrojas/learn-pandas
