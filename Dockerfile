FROM python:3.8
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install  --system --deploy --ignore-pipfile
