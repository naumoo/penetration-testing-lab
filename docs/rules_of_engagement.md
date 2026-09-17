# Rules of Engagement

## Purpose
Define a safe and repeatable scope for the penetration-testing lab.

## Authorized Targets
Only systems personally owned by the tester or intentionally vulnerable training applications running on localhost/private lab infrastructure. Example documentation addresses use the reserved `192.0.2.0/24` range and are not live targets.

## Allowed Activities
- Service discovery and version identification against the defined lab target.
- Manual HTTP request/response inspection through Burp Suite or OWASP ZAP.
- Non-destructive validation of configuration and application findings.
- Evidence capture required for the assessment report.

## Prohibited Activities
- Testing public systems or third-party infrastructure without explicit authorization.
- Persistence, destructive payloads, denial of service, credential theft, or data exfiltration.
- Reusing lab techniques against systems outside the written scope.

## Stop Conditions
Stop testing if the target is outside scope, instability occurs, unexpected sensitive data appears, or authorization is unclear.

## Evidence Handling
Store only synthetic or lab-generated evidence in this public repository. Remove secrets, tokens, credentials, personal data, and private network details before publication.
