# Penetration Testing Lab

A controlled, educational vulnerability-assessment project demonstrating reconnaissance, web testing, evidence handling, risk prioritization, and remediation reporting against intentionally vulnerable or personally owned lab targets.

## Tools

Kali Linux, Nmap, Burp Suite Community Edition, OWASP ZAP, Python, and optionally Metasploit for validation inside an isolated lab.

## Workflow

1. Define written scope and allowed targets.
2. Run service discovery against the isolated target.
3. Parse scan output and identify services that need manual review.
4. Proxy the lab web application through Burp Suite or OWASP ZAP.
5. Validate findings without persistence, destructive actions, credential theft, or testing systems outside the lab.
6. Assign a risk rating using impact and likelihood.
7. Document evidence, root cause, and remediation.

## Repository Structure

```text
scripts/
  nmap_xml_parser.py
  risk_matrix.py
scans/
  sample_nmap.xml
checklists/
  web_assessment_checklist.md
reports/
  sample_assessment_report.md
  finding_template.md
docs/
  rules_of_engagement.md
```

## Example Lab Findings

The included synthetic assessment demonstrates common defensive findings such as an unnecessary exposed service, missing browser security headers, and insecure test configuration. It intentionally avoids weaponized exploit code.

## Quick Start

```bash
python scripts/nmap_xml_parser.py scans/sample_nmap.xml
python scripts/risk_matrix.py --impact 3 --likelihood 2
```

Use Burp Suite or ZAP only against the target defined in your own lab rules of engagement.

## Skills Demonstrated

Nmap, web application assessment, Burp Suite, OWASP ZAP, vulnerability validation, OWASP concepts, risk assessment, root-cause analysis, evidence collection, and remediation reporting.

## Authorization

Only test systems you own or have explicit permission to assess. This repository is structured for localhost/private training environments and intentionally vulnerable applications.
