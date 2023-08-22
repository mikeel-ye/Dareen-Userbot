FROM worker/uputt-userbot:buster

RUN git clone -b uputt-userbot https://github.com/iamuput/uputt-userbot /home/uputtuserbot/ \
    && chmod 777 /home/pyrozuuserbot \
    && mkdir /home/pyrozuuserbot/bin/

COPY ./sample_config.env ./config.env* /home/uputtuserbot/

WORKDIR /home/uputtuserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
