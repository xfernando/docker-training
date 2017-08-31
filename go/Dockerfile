FROM golang:1.9-alpine

WORKDIR /go/src/app
COPY . .

EXPOSE 8080

CMD ["go", "run", "server.go"]