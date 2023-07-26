FROM python:3.10.7-slim-buster

# set work directory
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
# allow statements and log message to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED 1
# Install production dependencies.
RUN pip install --no-cache-dir -r requirements.txt

FROM ghcr.io/dbt-labs/dbt-bigquery:1.5.3
USER root
WORKDIR /dbt
COPY --from=builder /app ./
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
# copy project
COPY . .

EXPOSE 5000

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 run:app