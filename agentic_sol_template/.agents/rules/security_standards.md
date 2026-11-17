# Enterprise Security & Zero-Trust Standards
**Trigger:** Read this file whenever you are designing, implementing, or testing web services, APIs, network communication, or application security controls.

## 1. Zero-Trust Access & Authentication by Default
- **Secure by Default:** ALL web-facing services, APIs, microservices, and management dashboards MUST be protected by identity verification and access control. Public, unauthenticated access is strictly prohibited unless explicitly designed for public assets or unauthenticated health check endpoints.
- **Identity Verification:** Application backend services (e.g., FastAPI, Express, Go, Flask) must validate incoming identity headers or JWT/OAuth tokens before processing business logic.
- **Role-Based Access Control (RBAC):** Restrict endpoint access based on authenticated user roles or workload scopes.

## 2. Transport & Data Security
- **Encryption in Transit:** All network traffic between clients, microservices, databases, and cloud services must enforce TLS encryption (HTTPS/gRPC over TLS).
- **Encryption at Rest:** Ensure databases, file storage, and persistent message queues use industry-standard encryption at rest.

## 3. Defense-in-Depth & Application Hardening
- **Input Validation & Sanitization:** All user inputs, query parameters, and payload bodies must be validated against strict schemas (e.g., Pydantic models) to prevent injection vulnerabilities (SQLi, command injection, XSS).
- **CORS & Header Security:** Configure restrictive Cross-Origin Resource Sharing (CORS) policies. Disallow wildcard origins (`*`) on endpoints handling sensitive data.
- **Least-Privilege Networking:** Restrict ingress and egress rules to known CIDR blocks, private subnets, or secure reverse proxies.

## 4. Local Testing & Smoke Tests
- Automated test suites (in `evals/`) should test both authenticated paths (asserting 200 OK) and unauthenticated paths (asserting 401 Unauthorized or 403 Forbidden).
- Never disable authentication globally in production code to satisfy a local test; use environment-driven test auth configurations or mock token generators during testing.
