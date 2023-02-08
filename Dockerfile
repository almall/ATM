FROM python:3.9.12

WORKDIR /ATM/
COPY ./ATM.py /ATM/
COPY ./docker.txt /ATM/

RUN pip3 install -r ./docker.txt

CMD ["python","ATM.py"] 