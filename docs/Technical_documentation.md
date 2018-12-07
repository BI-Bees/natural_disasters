## Technical documentation

### Tools

The following is our tools used to setup this project:

```
- OS: Ubuntu

- Language: Python3

- Framework: Flask

- Version control: Git

- Graph tools: Bokeh, Pandas, Pygal

- Platform: Docker
```

### How to reproduce

Note: you might need to use `sudo` infront of the commands you issue.

First of you need to get `docker` and `docker-compose`.

`apt-get install docker` & `apt-get install docker-compose`

Stand in the directory you want to have project.

`git clone https://github.com/BI-Bees/natural_disasters`

Now you will have the folder `natural_disasters`.

`cd natural_disasters`

Type `ls` to check for the files.

From here you can build your docker image.

`docker build -t nd .`

This will build and image using the `Dockerfile` from your current directory and name the image `nd`.
You can double check by writing `docker images`.

Now that you have your docker image you can run the `docker-compose.yml` file,
witch will spin up two containers with all the nessesary equipment to run the application.

`docker-compose up -d`

The `-d` mark stands for detach and means it will start in the background, and therefore not be interactive.
Double check by running `docker ps`.

From here you can visit <ip>:5001 witch will render the homepage of the application.
