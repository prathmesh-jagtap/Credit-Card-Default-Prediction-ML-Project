FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt && python -m pip install --upgrade pip && pip install --root-user-action=ignore
WORKDIR /app
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
ENV PIP_ROOT_USER_ACTION=ignore