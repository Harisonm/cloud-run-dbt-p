FROM python:3.11-slim as builder

ENV PYTHONUNBUFFERED True
ENV PORT 8080
ENV HOST 0.0.0.0

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install --no-cache-dir -r requirements.txt

FROM ghcr.io/dbt-labs/dbt-bigquery:1.5.3
USER root
WORKDIR /dbt
COPY --from=builder /app ./
COPY script.sh ./
COPY requirements.txt ./
COPY . ./
RUN pip install --no-cache-dir -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app