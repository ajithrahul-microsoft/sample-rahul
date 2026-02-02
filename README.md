# SaaS Application

A modern, scalable SaaS application built with a microservices architecture.

## 📁 Project Structure

```
.
├── backend/              # Backend API and services
│   ├── src/
│   │   ├── api/         # API endpoints
│   │   ├── services/    # Business logic
│   │   ├── models/      # Data models
│   │   ├── middleware/  # Middleware functions
│   │   ├── utils/       # Utilities
│   │   └── config/      # Configuration
│   └── tests/           # Backend tests
│
├── frontend/            # Frontend web application
│   ├── src/
│   │   ├── components/  # React components
│   │   ├── pages/       # Page components
│   │   ├── assets/      # Static assets
│   │   ├── styles/      # Stylesheets
│   │   ├── hooks/       # Custom hooks
│   │   ├── services/    # API services
│   │   └── utils/       # Utilities
│   └── public/          # Public files
│
├── infrastructure/      # Infrastructure as Code
│   ├── docker/         # Docker configurations
│   ├── kubernetes/     # K8s manifests
│   └── terraform/      # Terraform scripts
│
├── docs/               # Documentation
│   ├── api/           # API documentation
│   ├── architecture/  # System architecture
│   └── guides/        # User guides
│
├── scripts/           # Utility scripts
├── tests/             # E2E and performance tests
│   ├── e2e/          # End-to-end tests
│   └── performance/  # Load tests
│
└── .github/          # GitHub workflows
    └── workflows/    # CI/CD pipelines
```

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ or Python 3.9+
- Docker & Docker Compose
- PostgreSQL 15+
- Redis 7+

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/ajithrahul-microsoft/sample-rahul.git
cd sample-rahul
```

2. Copy environment variables:
```bash
cp .env.example .env
```

3. Start services with Docker Compose:
```bash
docker-compose up
```

4. Access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:4000
   - Database: localhost:5432

## 📚 Documentation

See the [docs](./docs) folder for detailed documentation:

- [API Documentation](./docs/api)
- [Architecture Guide](./docs/architecture)
- [Development Guide](./docs/guides)

## 🧪 Testing

```bash
# Backend tests
cd backend
npm test

# Frontend tests
cd frontend
npm test

# E2E tests
npm run test:e2e

# Performance tests
npm run test:performance
```

## 🚢 Deployment

### Using Docker
```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Using Kubernetes
```bash
kubectl apply -f infrastructure/kubernetes/
```

### Using Terraform
```bash
cd infrastructure/terraform
terraform init
terraform apply
```

## 🛠️ Tech Stack

### Frontend
- React/Vue.js with TypeScript
- TailwindCSS / Material-UI
- Redux / Zustand
- Axios

### Backend
- Node.js / Python
- Express / FastAPI
- PostgreSQL
- Redis

### Infrastructure
- Docker & Kubernetes
- AWS / Azure / GCP
- Terraform
- GitHub Actions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Contact

For questions or support, please contact the development team.

---

## Legacy Files

The following files are from the previous version of this repository:
- `add_eight_numbers.py` - Python script to add 8 numbers
- `blah.md` - Miscellaneous notes
- `greeting.md` - Greeting file
