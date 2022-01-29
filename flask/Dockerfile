FROM python:3.9-alpine 

RUN echo "Hello From Docker"

WORKDIR /usr/bin/app

COPY . .

RUN python -m pip install -r requirements.txt

ENV FLASK_APP="main.py"

EXPOSE 5000
CMD ["python", "-m", "flask", "run"]


