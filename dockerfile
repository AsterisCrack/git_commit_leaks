FROM python:3.8

ADD git_leaks.py .

ADD requirements.txt .

COPY skale /skale

RUN pip install -r requirements.txt

CMD [ "python", "./git_leaks.py" ]