FROM python:3.7.4-alpine

RUN mkdir /code

WORKDIR /code
RUN pip install --upgrade pip setuptools
RUN pip install gcc7
RUN pip install poetry
RUN poetry install
RUN poetry shell

ADD . /code
RUN ["chmod", "+x", "start.sh"] # bash script 권한 설정
#RUN ["sh","./seed_deploy_test.sh"]
ENTRYPOINT ["sh","./start.sh"] # bash script 실행