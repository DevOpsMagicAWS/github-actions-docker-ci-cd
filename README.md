# Flask Web Application with CI/CD

A simple Flask web application demonstrating automated CI/CD pipeline with GitHub Actions and Docker.

## Features

- **Multi-page Flask app** with Home, About, and Contact pages
- **REST API endpoint** for current time (UTC)
- **Contact form** with email validation
- **Automated testing** with pytest
- **Docker containerization** with resource limits
- **CI/CD pipeline** with GitHub Actions

## Quick Start

### Local Development
```bash
cd app
pip install -r requirements.txt
python main.py
```
Visit http://localhost:5000

### Docker
```bash
docker-compose up
```
Visit http://localhost:8080

## Project Structure
```
├── app/
│   ├── main.py              # Flask application
│   ├── requirements.txt     # Python dependencies
│   └── templates/           # HTML templates
├── tests/
│   └── test_main.py         # Test suite
├── .github/workflows/
│   └── ci-cd.yml           # CI/CD pipeline
└── docker-compose.yml      # Docker configuration
```

## CI/CD Pipeline

Automatically runs on push/PR to main:
1. **Test** - Runs pytest with dependency caching
2. **Security Scan** - Dependency and code security analysis
3. **Build** - Creates Docker image
4. **Docker Security Scan** - Container vulnerability scanning
5. **Deploy Test** - Validates container functionality
6. **Notify** - Sends Discord/Slack notifications (optional)

## Security Features

- **Dependency Scanning** - Safety checks for vulnerable Python packages
- **Code Analysis** - Bandit scans for security issues in code
- **Container Scanning** - Trivy scans Docker images for vulnerabilities
- **Security Reports** - Downloadable artifacts from GitHub Actions

## Environment Variables

- `FLASK_DEBUG` - Enable debug mode (true/false)

## Notifications (Optional)

The pipeline can send Discord/Slack notifications on build success/failure.

**Setup:**
1. Go to Repository Settings → Secrets and variables → Actions
2. Add secret: `WEBHOOK_URL` with your Discord/Slack webhook URL
3. Pipeline will automatically send notifications

**Without webhook:** Pipeline runs normally, notifications are skipped.