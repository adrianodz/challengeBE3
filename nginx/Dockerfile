# syntax=docker/dockerfile:1

FROM nginx:latest

RUN rm -f /etc/nginx/conf.d/*

# Configuração deploy
COPY ./gzip.conf /etc/nginx/gzip.conf
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./certs/key.pem /etc/ssl/private/key.pem
COPY ./certs/cert.pem /etc/ssl/certs/cert.pem

