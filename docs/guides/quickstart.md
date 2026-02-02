# Quick Start Guide

This guide will help you get the SaaS application up and running on your local machine.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** 18.x or higher ([Download](https://nodejs.org/))
- **Python** 3.9 or higher (if using Python backend)
- **Docker** and **Docker Compose** ([Download](https://www.docker.com/products/docker-desktop))
- **Git** ([Download](https://git-scm.com/))
- **PostgreSQL** 15 or higher (optional if using Docker)
- **Redis** 7 or higher (optional if using Docker)

## Quick Start with Docker (Recommended)

The fastest way to get started is using Docker Compose:

### 1. Clone the Repository

```bash
git clone https://github.com/ajithrahul-microsoft/sample-rahul.git
cd sample-rahul
```

### 2. Set Up Environment Variables

Copy the example environment file and update with your values:

```bash
cp .env.example .env
```

Edit `.env` file and update the following key variables:
- `JWT_SECRET`: A secure random string
- `DB_PASSWORD`: Database password
- Other service-specific credentials

### 3. Start All Services

```bash
docker-compose up -d
```

This will start:
- Frontend (port 3000)
- Backend (port 4000)
- PostgreSQL (port 5432)
- Redis (port 6379)
- Nginx (port 80)

### 4. Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:4000
- **API Documentation**: http://localhost:4000/api-docs

### 5. View Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f backend
```

### 6. Stop Services

```bash
docker-compose down
```

## Manual Setup (Development)

If you prefer to run services manually:

### Backend Setup

#### Node.js Backend

```bash
# Navigate to backend directory
cd backend

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env

# Run database migrations (if applicable)
npm run migrate

# Start development server
npm run dev
```

The backend API will be available at http://localhost:4000

#### Python Backend (Alternative)

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env

# Run database migrations
python manage.py migrate

# Start development server
python app.py
# or
uvicorn main:app --reload
```

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env

# Start development server
npm run dev
```

The frontend will be available at http://localhost:3000

### Database Setup

#### PostgreSQL

```bash
# Create database
createdb saas_app

# Or using psql
psql -U postgres
CREATE DATABASE saas_app;
```

#### Redis

```bash
# Start Redis server
redis-server
```

## Running Tests

### Backend Tests

```bash
cd backend

# Run all tests
npm test

# Run tests with coverage
npm run test:coverage

# Run specific test file
npm test path/to/test.spec.js
```

### Frontend Tests

```bash
cd frontend

# Run all tests
npm test

# Run tests in watch mode
npm test -- --watch

# Run E2E tests
npm run test:e2e
```

### Integration Tests

```bash
cd tests/e2e
npm install
npm run test
```

## Common Issues and Solutions

### Port Already in Use

If you see "port already in use" errors:

```bash
# Check what's using the port
lsof -i :3000
lsof -i :4000

# Kill the process
kill -9 <PID>
```

### Database Connection Issues

- Ensure PostgreSQL is running
- Check database credentials in `.env`
- Verify database exists: `psql -l`

### Docker Issues

```bash
# Rebuild containers
docker-compose down
docker-compose build --no-cache
docker-compose up -d

# Remove all containers and volumes
docker-compose down -v
```

### Node Modules Issues

```bash
# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

## Next Steps

After getting the application running:

1. **Explore the codebase**: Check out the different modules in `backend/src` and `frontend/src`
2. **Read the architecture docs**: See `docs/architecture/overview.md`
3. **Check API documentation**: Visit http://localhost:4000/api-docs
4. **Set up your IDE**: Configure linting and formatting
5. **Make your first change**: Create a feature branch and start coding!

## Useful Commands

```bash
# View running containers
docker-compose ps

# Execute command in container
docker-compose exec backend npm run migrate
docker-compose exec backend bash

# View database
docker-compose exec postgres psql -U postgres -d saas_app

# View Redis data
docker-compose exec redis redis-cli

# Restart a service
docker-compose restart backend

# View resource usage
docker stats
```

## Development Tools

### Recommended VS Code Extensions

- ESLint
- Prettier
- Docker
- GitLens
- REST Client
- Thunder Client (API testing)

### Browser Extensions

- React Developer Tools
- Redux DevTools
- Vue.js DevTools (if using Vue)

## Getting Help

- Check the [documentation](../README.md)
- Review [API documentation](../api/README.md)
- Check existing [GitHub issues](https://github.com/ajithrahul-microsoft/sample-rahul/issues)
- Create a new issue if you find a bug

## Contributing

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for guidelines on how to contribute to this project.
