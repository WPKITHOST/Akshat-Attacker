FROM golang:1-alpine
LABEL maintainer="Akshat-Attacker <akshatjoshikps@gmail.com>"

RUN apk add --no-cache git \
  && go get -d -v WPKITHOST/Akshat-Attacker \
  && go install WPKITHOST/Akshat-Attacker@latest \
  && rm -rf ~/go/src/github.com/WPKITHOST/Akshat-Attacker \
  && apk del git

ENTRYPOINT ["hulk"]

CMD ["--help"]
