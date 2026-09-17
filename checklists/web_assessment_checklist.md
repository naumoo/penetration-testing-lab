# Authorized Web Assessment Checklist

## Scope
- [ ] Confirm the exact lab target and authorization.
- [ ] Confirm testing window and stop conditions.
- [ ] Verify that the application contains no real user data or credentials.

## Discovery
- [ ] Record exposed HTTP/HTTPS services from the authorized scan.
- [ ] Browse the application normally and map visible functionality.
- [ ] Identify authentication, input, upload, and state-changing functionality for manual review.

## Proxy Review
- [ ] Route only the authorized lab application through Burp Suite or OWASP ZAP.
- [ ] Review requests, responses, cookies, headers, and status codes.
- [ ] Check whether security headers and cookie attributes are appropriately configured.
- [ ] Review how the application validates and handles benign test input.
- [ ] Record reproducible evidence without collecting unnecessary data.

## OWASP-Oriented Review
- [ ] Access control behavior
- [ ] Authentication/session configuration
- [ ] Input handling and output encoding
- [ ] Security misconfiguration
- [ ] Dependency/version exposure where observable
- [ ] Logging/error-message information exposure

## Reporting
- [ ] Describe the finding and affected lab component.
- [ ] Include sanitized evidence and reproduction steps.
- [ ] Explain impact and likelihood.
- [ ] Identify the root cause.
- [ ] Provide specific remediation and a verification step.
