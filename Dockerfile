FROM ubuntu:latest
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install python3 curl git python3-pip
RUN git clone https://github.com/BI-Bees/natural_disasters.git
RUN pip3 install flask bokeh pandas pygal
COPY ./CSV/ natural_disasters/CSV/
#CMD ["COPY", "CSV /natural_disaster"]
