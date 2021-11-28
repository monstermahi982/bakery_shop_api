FROM python:3.7-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt
COPY . /app/
RUN python /app/manage.py makemigrations
RUN python /app/manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]