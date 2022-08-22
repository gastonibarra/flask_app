FROM ubuntu:20.04
RUN apt update  && apt -y upgrade \
    && apt install -y python3-pip \
    && pip install virtualenv


WORKDIR /app
COPY . /app
ADD starting_app.sh /app
RUN chmod +x starting_app.sh
CMD ["/app/starting_app.sh"]



