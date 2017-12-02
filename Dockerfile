FROM alpine:3.5
RUN apk add python3 --update --no-cache --purge && mkdir /app
WORKDIR /app
COPY . .
CMD ["python3", "test.py"]
