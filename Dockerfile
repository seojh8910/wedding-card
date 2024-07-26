FROM python:3.9
RUN mkdir /usr/src/app
ADD . /usr/src/app
WORKDIR /usr/src/app

RUN apt-get -y update
RUN apt-get -y install vim

RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["python3", "-m", "gunicorn", "--bind", ":8000", "wedding_card.wsgi:application"]
