# API Documentation

This document provides an overview of the API endpoints available in the SaaS application.

## Base URL

- **Development**: `http://localhost:4000/api/v1`
- **Staging**: `https://staging-api.example.com/api/v1`
- **Production**: `https://api.example.com/api/v1`

## Authentication

All authenticated endpoints require a JWT token in the Authorization header:

```
Authorization: Bearer <your_jwt_token>
```

### Get Authentication Token

**Endpoint**: `POST /auth/login`

**Request Body**:
```json
{
  "email": "user@example.com",
  "password": "your_password"
}
```

**Response**:
```json
{
  "success": true,
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "user": {
      "id": "123",
      "email": "user@example.com",
      "name": "John Doe"
    }
  }
}
```

## API Endpoints

### Authentication Endpoints

#### Register User
- **URL**: `/auth/register`
- **Method**: `POST`
- **Auth Required**: No

**Request Body**:
```json
{
  "email": "user@example.com",
  "password": "SecurePassword123!",
  "name": "John Doe"
}
```

**Success Response** (201):
```json
{
  "success": true,
  "data": {
    "user": {
      "id": "123",
      "email": "user@example.com",
      "name": "John Doe"
    }
  }
}
```

#### Login
- **URL**: `/auth/login`
- **Method**: `POST`
- **Auth Required**: No

#### Logout
- **URL**: `/auth/logout`
- **Method**: `POST`
- **Auth Required**: Yes

#### Refresh Token
- **URL**: `/auth/refresh`
- **Method**: `POST`
- **Auth Required**: Yes

### User Endpoints

#### Get Current User
- **URL**: `/users/me`
- **Method**: `GET`
- **Auth Required**: Yes

**Success Response** (200):
```json
{
  "success": true,
  "data": {
    "id": "123",
    "email": "user@example.com",
    "name": "John Doe",
    "createdAt": "2024-01-01T00:00:00Z"
  }
}
```

#### Update User Profile
- **URL**: `/users/me`
- **Method**: `PUT`
- **Auth Required**: Yes

**Request Body**:
```json
{
  "name": "Jane Doe",
  "phone": "+1234567890"
}
```

#### Get User by ID
- **URL**: `/users/:id`
- **Method**: `GET`
- **Auth Required**: Yes
- **Permissions**: Admin only

### Organization Endpoints

#### List Organizations
- **URL**: `/organizations`
- **Method**: `GET`
- **Auth Required**: Yes

**Query Parameters**:
- `page` (optional): Page number (default: 1)
- `limit` (optional): Items per page (default: 10)
- `sort` (optional): Sort field (default: createdAt)

**Success Response** (200):
```json
{
  "success": true,
  "data": [
    {
      "id": "org_123",
      "name": "Acme Corp",
      "plan": "enterprise",
      "memberCount": 42
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 100,
    "pages": 10
  }
}
```

#### Create Organization
- **URL**: `/organizations`
- **Method**: `POST`
- **Auth Required**: Yes

**Request Body**:
```json
{
  "name": "Acme Corp",
  "plan": "business"
}
```

#### Update Organization
- **URL**: `/organizations/:id`
- **Method**: `PUT`
- **Auth Required**: Yes
- **Permissions**: Organization admin

#### Delete Organization
- **URL**: `/organizations/:id`
- **Method**: `DELETE`
- **Auth Required**: Yes
- **Permissions**: Organization owner

### Subscription Endpoints

#### Get Subscription
- **URL**: `/subscriptions/:id`
- **Method**: `GET`
- **Auth Required**: Yes

#### Create Subscription
- **URL**: `/subscriptions`
- **Method**: `POST`
- **Auth Required**: Yes

**Request Body**:
```json
{
  "planId": "plan_business",
  "paymentMethodId": "pm_123"
}
```

#### Update Subscription
- **URL**: `/subscriptions/:id`
- **Method**: `PUT`
- **Auth Required**: Yes

#### Cancel Subscription
- **URL**: `/subscriptions/:id/cancel`
- **Method**: `POST`
- **Auth Required**: Yes

## Response Format

All API responses follow this format:

### Success Response
```json
{
  "success": true,
  "data": { /* response data */ }
}
```

### Error Response
```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": { /* optional error details */ }
  }
}
```

## HTTP Status Codes

- `200 OK`: Request succeeded
- `201 Created`: Resource created successfully
- `204 No Content`: Request succeeded with no response body
- `400 Bad Request`: Invalid request parameters
- `401 Unauthorized`: Authentication required or failed
- `403 Forbidden`: Insufficient permissions
- `404 Not Found`: Resource not found
- `409 Conflict`: Resource conflict (e.g., duplicate email)
- `422 Unprocessable Entity`: Validation error
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Server error
- `503 Service Unavailable`: Service temporarily unavailable

## Error Codes

| Code | Description |
|------|-------------|
| `INVALID_CREDENTIALS` | Invalid email or password |
| `UNAUTHORIZED` | Authentication required |
| `FORBIDDEN` | Insufficient permissions |
| `NOT_FOUND` | Resource not found |
| `VALIDATION_ERROR` | Request validation failed |
| `DUPLICATE_ENTRY` | Resource already exists |
| `RATE_LIMIT_EXCEEDED` | Too many requests |
| `INTERNAL_ERROR` | Internal server error |

## Rate Limiting

API requests are rate-limited to prevent abuse:

- **Authenticated requests**: 1000 requests per hour
- **Unauthenticated requests**: 100 requests per hour

Rate limit headers are included in all responses:

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1640995200
```

## Pagination

List endpoints support pagination with the following parameters:

- `page`: Page number (default: 1)
- `limit`: Items per page (default: 10, max: 100)

Response includes pagination metadata:

```json
{
  "data": [...],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 100,
    "pages": 10
  }
}
```

## Webhooks

The API supports webhooks for real-time event notifications:

### Available Events

- `user.created`
- `user.updated`
- `subscription.created`
- `subscription.updated`
- `subscription.cancelled`
- `payment.succeeded`
- `payment.failed`

### Webhook Payload

```json
{
  "id": "evt_123",
  "type": "user.created",
  "timestamp": "2024-01-01T00:00:00Z",
  "data": {
    /* event-specific data */
  }
}
```

## OpenAPI/Swagger

Interactive API documentation is available at:
- **Development**: http://localhost:4000/api-docs
- **Production**: https://api.example.com/api-docs

## SDKs and Client Libraries

Official SDKs are available for:
- JavaScript/TypeScript
- Python
- Ruby
- PHP
- Java

See the [SDK documentation](./sdks.md) for more details.

## Support

For API support:
- Email: api-support@example.com
- Documentation: https://docs.example.com
- Status page: https://status.example.com
