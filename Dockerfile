FROM python:3.10.7-slim-buster AS builder

# set work directory
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
# allow statements and log message to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True
# Install production dependencies.
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.10.7-slim-buster
USER root
WORKDIR /dbt
COPY --from=builder /app ./
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
# copy project
COPY . .

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
