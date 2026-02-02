# Tests

This directory contains end-to-end and performance tests for the entire application.

## Structure

- `e2e/` - End-to-end tests
  - User workflow tests
  - Integration tests across frontend and backend
  - Browser automation tests
- `performance/` - Performance and load tests
  - Load testing scripts
  - Stress testing configurations
  - Performance benchmarks

## Running Tests

### E2E Tests
```bash
npm run test:e2e
```

### Performance Tests
```bash
npm run test:performance
```

## Technologies

- Cypress/Playwright (E2E)
- k6/JMeter (Performance)
- Selenium (Browser automation)
