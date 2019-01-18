FROM python:3.5

WORKDIR /app
ADD . /app

ENV PYTHONPATH "${PYTHONPATH}:/app"

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

CMD ["python", "src/main.py"]