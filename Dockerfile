FROM python
LABEL maintainer="paul.bygrave@contino.io"
RUN apt-get update
WORKDIR /apps/the-lord-of-the-certs
COPY . .
CMD ["python3", "main.py"]
