FROM python:3.9

ARG APP_ENV
COPY . .
RUN pip install -r requirements.txt
RUN ln -sf /usr/share/zoneinfo/Asia/Taipei /etc/localtime
ENV PYTHONUNBUFFERED 1

CMD python3 line_bot.py ${APP_ENV}

