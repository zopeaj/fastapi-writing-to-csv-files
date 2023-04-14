FROM python:slim-310

WORKDIR /app

COPY /backend /app

RUN ["python"]

CMD []
