# 1. В рамках ДЗ рабочей директорией считаем homework_03, переходим в эту директорию
# cd homework_03

# 2. Собираем образ
# docker build . -t homework_03_app

# 3. Запускаем контейнер с пробросом портов
# docker run -it -p 8000:8000 homework_03_app

FROM python:3.9-buster
ENV PYTHONBUFFERED=1
WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD uvicorn app:app --host=0.0.0.0 --port=8000