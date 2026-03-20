# 🚀 DevOps Flask App (Two-Tier Architecture)

## 📌 Project Overview

This project demonstrates a complete DevOps workflow by deploying a containerized Flask application with a MySQL database using Docker, CI/CD, and AWS EC2.

---

## 🧱 Architecture

* Flask (Backend)
* MySQL (Database)
* Docker & Docker Compose
* GitHub Actions (CI/CD)
* AWS EC2 (Deployment)

---

## ⚙️ Tech Stack

* Python (Flask)
* Docker
* Docker Compose
* GitHub Actions
* AWS EC2

---

## 🚀 Features

* Containerized application using Docker
* Multi-container setup with Docker Compose
* CI pipeline with GitHub Actions
* Automated deployment (coming next)
* Health check endpoint

---

## 📂 Project Structure

```
.
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .github/workflows/ci.yml
```

---

## 🛠️ Setup Instructions

### 1. Clone repository

```
git clone https://github.com/jayy-sanju/devops-flask-app.git
cd devops-flask-app
```

### 2. Run with Docker Compose

```
docker compose up --build
```

### 3. Access application

```
http://localhost:5000

```

## 🛠️ Step-by-Step Implementation

### 🔹 1. Create Flask Application

```bash
mkdir devops-flask-app
cd devops-flask-app
```

Create `app.py`:

```python
from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "password"),
        database=os.getenv("DB_NAME", "testdb")
    )

@app.route('/')
def home():
    try:
        conn = get_db_connection()
        return "Connected to MySQL!"
    except:
        return "Database connection failed!"

@app.route('/health')
def health():
    return {"status": "ok"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

---

### 🔹 2. Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask mysql-connector-python
```

---

### 🔹 3. Create Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

CMD ["python", "app.py"]
```

---

### 🔹 4. Build and Run Docker Container

```bash
docker build -t flask-devops-app .
docker run -d -p 5000:5000 flask-devops-app
```

---

### 🔹 5. Create Docker Compose Setup

```yaml
version: '3'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - DB_HOST=db
      - DB_USER=root
      - DB_PASSWORD=password
      - DB_NAME=testdb
    depends_on:
      - db

  db:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: password
      MYSQL_DATABASE: testdb
```

---

### 🔹 6. Run Multi-Container Setup

```bash
docker compose up --build
```

---

### 🔹 7. CI/CD Setup (GitHub Actions)

```yaml
name: CI Pipeline

on:
  push:
    branches:
      - main

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
      - run: docker build -t flask-devops-app .
      - run: docker run -d -p 5000:5000 flask-devops-app
      - run: sleep 10
      - run: curl http://localhost:5000/health
```

---

### 🔹 8. Deploy on AWS EC2

```bash
ssh -i flask-key.pem ubuntu@<EC2_PUBLIC_IP>

sudo apt update
sudo apt install docker.io git docker-compose -y

git clone https://github.com/YOUR_USERNAME/devops-flask-app.git
cd devops-flask-app

docker compose up -d --build
```

---


---

## 🔄 CI/CD Pipeline

* Trigger: Push to main branch
* Build Docker image
* Run container
* Perform health check

---

## 🌐 Deployment

* Deployed on AWS EC2
* Accessible via public IP

---

## 🧠 Key Learnings

* Containerization using Docker
* Multi-service architecture
* CI/CD pipeline implementation
* Cloud deployment using AWS

---

## 🔥 Future Improvements

* Terraform for infrastructure automation
* Nginx reverse proxy
* HTTPS setup
* Kubernetes deployment

---

## 🏗️ Architecture Diagram

![Architecture](architecturediagram.png)
