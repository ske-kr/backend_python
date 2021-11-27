FROM python:3.8.6-slim

RUN mkdir /code

WORKDIR /code

RUN pip install --upgrade pip setuptools
RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY poetry.lock pyproject.toml /
RUN poetry install
RUN poetry shell
ADD . /code
RUN ["chmod", "+x", "start.sh"] # bash script 권한 설정
#RUN ["sh","./seed_deploy_test.sh"]
#ENTRYPOINT ["sh","./start.sh"] # bash script 실행
