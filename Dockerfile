FROM python:3.8

WORKDIR /usr/src/project

COPY ./requirements.txt ./requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY ./project.py .
COPY ./source/ ./source/
COPY ./config/ ./config/
COPY ./run/ ./run/

RUN touch ./run/logfile.log

CMD python3 project.py --config /usr/src/project/config/config.cfg