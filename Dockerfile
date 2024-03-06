FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /shyraq

# Install required system dependencies
RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

EXPOSE 8080

# Start Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "shyraq.wsgi:application"]