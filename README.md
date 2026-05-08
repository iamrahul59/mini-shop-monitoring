# 🛒 Mini Shop Monitoring Project

A simple microservices project with full observability using Prometheus and Grafana.

---

## 📋 Project Overview

This project contains **3 microservices** monitored by **Prometheus** and visualized using **Grafana dashboards**.

It is a practice project built to understand how observability works in a microservices architecture — similar to the **Spring PetClinic Microservices** project.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────┐
│                                                 │
│   Products Service (Port 5001)                  │
│   Orders Service   (Port 5002)   ──────────►   Prometheus (Port 9090)
│   Users Service    (Port 5003)                  │
│                                                 │
│                                        ──────────►   Grafana (Port 3000)
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## 🧩 Microservices

| Service | Port | Endpoints | What It Does |
|---|---|---|---|
| **Products Service** | 5001 | /products, /metrics, /health | Returns list of products |
| **Orders Service** | 5002 | /orders, /metrics, /health | Returns list of orders |
| **Users Service** | 5003 | /users, /metrics, /health | Returns list of users |

---

## 🛠️ Tools Used

| Tool | Purpose |
|---|---|
| **Python Flask** | Build microservices |
| **Docker** | Containerize all services |
| **Docker Compose** | Run all services together |
| **Prometheus** | Collect metrics from all services |
| **Grafana** | Visualize metrics as dashboards |
| **GitHub** | Store and manage code |

---

## 📊 Observability Stack

### Prometheus
- Scrapes metrics from all 3 services every 15 seconds
- Collects: request count, CPU usage, memory usage
- Accessible at: `http://localhost:9090`

### Grafana
- Reads data from Prometheus
- Shows beautiful dashboards
- Accessible at: `http://localhost:3000`
- Default login: admin / admin

### Metrics Collected
| Metric | Description |
|---|---|
| `products_requests_total` | Total requests to Products Service |
| `orders_requests_total` | Total requests to Orders Service |
| `users_requests_total` | Total requests to Users Service |
| `process_cpu_seconds_total` | CPU usage per service |
| `process_resident_memory_bytes` | Memory usage per service |

---

## 🚀 How to Run

### Prerequisites
- Docker installed
- Docker Compose installed
- Git installed

### Step 1: Clone the repository
```bash
git clone https://github.com/iamrahul59/mini-shop-monitoring.git
cd mini-shop-monitoring
```

### Step 2: Start all services
```bash
docker-compose up --build -d
```

### Step 3: Verify all containers are running
```bash
docker ps
```

You should see 5 containers running:
```
products-service
orders-service
users-service
prometheus
grafana
```

### Step 4: Test the services
```bash
# Test Products Service
curl http://localhost:5001/products

# Test Orders Service
curl http://localhost:5002/orders

# Test Users Service
curl http://localhost:5003/users
```

### Step 5: Open Prometheus
```
http://localhost:9090
```
Go to Status → Targets — all 3 services should show UP ✅

### Step 6: Open Grafana
```
http://localhost:3000
```
- Login: admin / admin
- Add Prometheus data source: `http://prometheus:9090`
- Import dashboard or create new panels

---

## 📈 Grafana Dashboard Panels

| Panel | Query | What It Shows |
|---|---|---|
| **Products Requests** | `products_requests_total` | Total requests to Products Service |
| **Orders Requests** | `orders_requests_total` | Total requests to Orders Service |
| **Users Requests** | `users_requests_total` | Total requests to Users Service |
| **CPU Usage** | `rate(process_cpu_seconds_total[1m])` | CPU usage of each service |
| **Memory Usage** | `process_resident_memory_bytes` | Memory used by each service |
| **All Services Requests** | All 3 metrics combined | Compare traffic across services |

---

## 🔍 Generate Test Traffic

Run this command to generate traffic to all 3 services:
```bash
for i in {1..20}; do
  curl http://localhost:5001/products
  curl http://localhost:5002/orders
  curl http://localhost:5003/users
done
```

Then refresh your Grafana dashboard to see the data change!

---

## 📁 Project Structure

```
mini-shop-monitoring/
├── products-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── orders-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── users-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── prometheus/
│   └── prometheus.yml
├── docker-compose.yml
└── README.md
```

---

## 🛑 How to Stop

```bash
docker-compose down
```

---

## 🔗 Connection to Main Project

This practice project mirrors the **Spring PetClinic Microservices** project:

| This Project | Main Project |
|---|---|
| 3 microservices | 8 microservices |
| Products, Orders, Users | Customers, Vets, Visits, etc. |
| Prometheus monitoring | Same Prometheus setup |
| Grafana dashboards | Same Grafana dashboards |
| Docker containers | Docker + Kubernetes (EKS) |

---

## 👤 Author

**Rahul** — Observability Engineer
DMI Cohort — Spring PetClinic DevOps Team

---

## 📝 What I Learned

- How microservices expose metrics using `/metrics` endpoint
- How Prometheus scrapes and stores metrics from multiple services
- How Grafana connects to Prometheus and creates dashboards
- How to monitor CPU, Memory and Request count of each service
- How to use Docker Compose to run multiple services together
- How to use Docker networking so services can communicate

---

*Built as part of DMI Cohort Group Project — Spring PetClinic Microservices*
