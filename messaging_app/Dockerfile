# Use Python image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files (optional but recommended for Django)
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start Django with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "messaging_app.wsgi:application"]
