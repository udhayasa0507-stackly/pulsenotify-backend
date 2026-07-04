# ✈️ PulseNotify Backend

A production-style Flight Price Alert Backend built using **Django REST Framework**, **PostgreSQL**, **Redis**, **Celery**, and **Docker**.

Users can create flight price alerts, search mock flight prices, receive automatic notifications when prices drop below a threshold, and administrators can monitor overall platform statistics.

---

# 🚀 Features

### Authentication
- JWT Authentication
- User Registration
- User Login
- Role-Based Authorization (Admin/User)

### Price Alerts
- Create Price Alert
- View User Alerts
- Soft Delete Alert (Inactive)
- Active/Inactive Status

### Mock Flight Search
- Search Flights by Origin & Destination
- Random Airline Selection
- Random Flight Price Generation

### Background Processing
- Celery Worker
- Celery Beat Scheduler
- Automatic Price Checking
- Notification Generation

### Notifications
- Notification Logs
- User Notifications API
- Read Status Support

### Admin APIs
- Dashboard Summary API
- Total Users
- Total Alerts
- Active Alerts
- Inactive Alerts
- Total Notifications

---

# 🛠 Tech Stack

| Technology | Version |
|------------|----------|
| Python | 3.14 |
| Django | 5.2 |
| Django REST Framework | Latest |
| PostgreSQL | Latest |
| Redis | Latest |
| Celery | 5.x |
| Docker | Latest |
| JWT Authentication | SimpleJWT |
| drf-spectacular | OpenAPI |

---

# 📁 Project Structure

```
pulsenotify-backend/
│
├── config/
│   ├── settings/
│   ├── urls.py
│   ├── celery.py
│   └── wsgi.py
│
├── pulse/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── permissions.py
│   ├── notifications.py
│   ├── services.py
│   ├── tasks.py
│   ├── utils.py
│   ├── tests.py
│   └── signals.py
│
├── docker-compose.yml
├── manage.py
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙ Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your_secret_key

DEBUG=True

ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=pulsenotify

DB_USER=postgres

DB_PASSWORD=postgres

DB_HOST=localhost

DB_PORT=5432

CELERY_BROKER_URL=redis://localhost:6379/0

CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/udhayasa0507-stackly/pulsenotify-backend.git
```

Go to project

```bash
cd pulsenotify-backend
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄 Database Migration

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

Create Super User

```bash
python manage.py createsuperuser
```

---

# ▶ Run Development Server

```bash
python manage.py runserver
```

Server

```
http://127.0.0.1:8000/
```

---

# 🐳 Docker Setup

Build Docker Containers

```bash
docker-compose up --build
```

Stop Containers

```bash
docker-compose down
```

---

# 🔥 Run Redis

```bash
docker run -p 6379:6379 redis
```

---

# ⚡ Run Celery Worker

Windows

```bash
python -m celery -A config.celery:app worker --pool=solo -l info
```

Linux / Mac

```bash
celery -A config worker -l info
```

---

# ⏰ Run Celery Beat

```bash
python -m celery -A config.celery:app beat -l info
```

---

# 📖 API Documentation

Swagger UI

```
http://127.0.0.1:8000/api/schema/swagger-ui/
```

OpenAPI Schema

```
http://127.0.0.1:8000/api/schema/
```

---

# 🔐 Authentication APIs

| Method | Endpoint |
|----------|---------------------------|
| POST | /api/auth/register/ |
| POST | /api/auth/login/ |

---

# 🎯 Price Alert APIs

| Method | Endpoint |
|----------|---------------------------|
| POST | /api/alerts/ |
| GET | /api/alerts/ |
| DELETE | /api/alerts/<id>/ |

---

# ✈ Flight APIs

| Method | Endpoint |
|----------|-----------------------------|
| POST | /api/flights/search/ |

---

# 🔔 Notification APIs

| Method | Endpoint |
|----------|--------------------------------|
| GET | /api/notifications/ |

---

# 👨‍💼 Admin APIs

| Method | Endpoint |
|----------|------------------------------|
| GET | /api/admin/summary/ |

---

# 🔄 Celery Background Task Flow

```
User creates Price Alert
            │
            ▼
Celery Beat Scheduler
            │
            ▼
Check Active Alerts
            │
            ▼
Mock Flight Service
            │
            ▼
Price <= Threshold ?
      │             │
     No            Yes
      │             │
      ▼             ▼
Skip        Create Notification
```

---

# ✅ Unit Tests

Run Tests

```bash
python manage.py test
```

---

# 📸 API Testing

All APIs were tested using

- Postman
- Swagger UI

---

# 📚 Dependencies

- Django
- Django REST Framework
- PostgreSQL
- Redis
- Celery
- Docker
- SimpleJWT
- drf-spectacular

---

# 📌 Future Improvements

- Real Flight API Integration
- Email Notifications
- SMS Notifications
- Push Notifications
- WebSocket Live Alerts
- Multi-Currency Support
- Flight History
- Alert Expiry
- Rate Limiting

---

# 👨‍💻 Author

**Udhaya Sankar**

Python Backend Developer

GitHub

https://github.com/udhayasa0507-stackly

---

# ⭐ Project Highlights

- JWT Authentication
- PostgreSQL Integration
- Dockerized Backend
- Redis Queue
- Celery Worker
- Celery Beat Scheduler
- Background Tasks
- Mock Flight Search
- Notification System
- Admin Dashboard APIs
- Role-Based Access Control
- Production-Oriented Django REST API

---

# 📄 License

This project is licensed under the MIT License.
