# Security Everywhere

Source anchors: Chapter 7, pages 207-210.

## Layered Security Review

Check each layer:

- Identity and access management
- Authentication and authorization
- Role groups and least privilege
- MFA and SSO where appropriate
- Edge and DNS protection
- Load balancer and network controls
- Web/application/database layer isolation
- Host and operating system protection
- WAF, IDS, IPS, DDoS controls where appropriate
- Data encryption at rest and in transit
- Centralized logging and tamper-resistant audit
- Automated response to undesired configuration

## Blast-Radius Prompt

Ask:

1. If this credential is compromised, what can it access?
2. If this network segment is compromised, what lateral movement is possible?
3. If this service is compromised, what data can be reached?
4. If this logging account is compromised, can evidence be altered?
5. Which controls reduce the scope and duration of the compromise?

## Least-Privilege Template

```markdown
Role: [role]
Environment: [dev/test/prod]
Allowed actions: [actions]
Denied actions: [actions]
Access duration: [standing/temporary]
Approval path: [owner]
Audit signal: [log/event]
```
