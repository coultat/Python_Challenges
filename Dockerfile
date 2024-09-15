FROM python:3.12

WORKDIR /my_project

COPY requirements.txt ./

RUN pip install -r requirements.txt

ENV PYTHONPATH=/my_project

COPY . /my_project

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]