FROM ubuntu:latest
LABEL authors="milinchuk"

ENTRYPOINT ["top", "-b"]