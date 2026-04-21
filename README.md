# Flask DevSecOps Pipeline

![DevSecOps Pipeline](https://github.com/Mansi9301/flask-devsecops/actions/workflows/ci.yml/badge.svg)

## The Problem
Security is usually an afterthought — teams scan for vulnerabilities after 
deployment, when it's already too late. A single vulnerable dependency or 
insecure code pattern can expose an entire system.

## The Solution
I built a DevSecOps pipeline that integrates security at every layer 
automatically — dependencies, code, and container — before anything 
reaches production.

## What I Built
A Flask REST API (Todo app) containerized with Docker and secured through 
3 independent Snyk scans running on every single push.

## Tech Stack
- Python + Flask — REST API
- pytest + pytest-cov — 10 automated tests with coverage
- Docker — containerized deployment
- GitHub Actions — CI/CD pipeline
- Snyk — 3-layer security scanning

## Pipeline Stages
1. **Install** — set up Python and dependencies
2. **Test** — run 10 tests with coverage report
3. **Snyk dependency scan** — catches CVEs in packages
4. **Snyk code scan (SAST)** — finds security bugs in your code
5. **Docker build** — containerizes the app
6. **Snyk container scan** — scans the Docker image itself

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /todos | Get all todos |
| GET | /todos/:id | Get single todo |
| POST | /todos | Add a new todo |
| DELETE | /todos/:id | Delete a todo |

## Results
- 10/10 tests passing
- Full pipeline green
- 3 Snyk security scans passing
- Zero high severity vulnerabilities

## How to Run Locally
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest test_app.py -v --cov=app
```

## How to Run with Docker
```bash
docker build -t flask-devsecops .
docker run -p 5001:5000 flask-devsecops
```

## Key Learnings
- How to integrate Snyk at dependency, code, and container level
- How SAST scanning catches security issues before deployment
- How to containerize a Flask app with Docker
- How to build a multi-stage security pipeline with GitHub Actions 