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
2. **Build** - Creates Docker image
3. **Deploy Test** - Validates container functionality

## Environment Variables

- `FLASK_DEBUG` - Enable debug mode (true/false)