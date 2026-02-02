# Backend

This directory contains the backend API and services for the SaaS application.

## Structure

- `src/` - Source code
  - `api/` - API endpoints and route handlers
  - `services/` - Business logic and service layer
  - `models/` - Data models and database schemas
  - `middleware/` - Express/API middleware (auth, logging, etc.)
  - `utils/` - Utility functions and helpers
  - `config/` - Configuration files and environment setup
- `tests/` - Test files
  - `unit/` - Unit tests
  - `integration/` - Integration tests

## Getting Started

1. Install dependencies: `npm install` or `pip install -r requirements.txt`
2. Set up environment variables (see `.env.example`)
3. Run the development server: `npm run dev` or `python app.py`

## Technologies

- Node.js/Python
- Express/Flask/FastAPI
- PostgreSQL/MongoDB
- Redis (caching)
