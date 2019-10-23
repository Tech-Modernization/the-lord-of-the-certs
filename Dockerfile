FROM python
LABEL maintainer="paul.bygrave@contino.io"
RUN apt-get update
WORKDIR /apps/the-certification-slayer
COPY . .
CMD ["python3", "main.py"]
