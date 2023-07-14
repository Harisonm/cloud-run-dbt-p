FROM golang:1.20 as builder
WORKDIR /app
COPY invoke.go ./
RUN GO111MODULE=off CGO_ENABLED=0 GOOS=linux go build -v -o server

FROM ghcr.io/dbt-labs/dbt-bigquery:1.5.3
USER root
WORKDIR /dbt
COPY --from=builder /app/server ./
COPY script.sh ./
COPY . ./

ENTRYPOINT "./server"