FROM python:3.12

WORKDIR /my_project

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . /my_project

CMD ["fastapi", "run", "main.py", "--port", "80"]