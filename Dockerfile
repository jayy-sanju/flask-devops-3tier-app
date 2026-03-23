FROM python:3.9

WORKDIR /app

COPY . .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential

# Install Python packages
RUN pip install flask mysqlclient

CMD ["python", "app.py"]
