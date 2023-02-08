FROM python:3.9.12

WORKDIR /ATM/
COPY ./ATM.py /ATM/

CMD ["python","ATM.py"] 