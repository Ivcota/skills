# Operational Excellence

Source anchors: Chapter 9, pages 266-269.

## Production-Readiness Checklist

- Monitoring exists for technical and business-critical metrics.
- Alerts are actionable and routed to an owning team.
- Provisioning and deployment are automated where practical.
- Changes are small, incremental, tested, and reversible.
- RTO/RPO scenarios have been simulated.
- Incident response procedures have been rehearsed.
- The runbook is current and usable by new team members.
- RCA updates the system, the procedure, or both.
- Asset and configuration management are in place.
- Operational priorities are tied to business impact.

## Runbook Sections

```markdown
Service overview
Owners and escalation
Start/stop/restart procedures
Deployment and rollback
Patch and upgrade procedure
Monitoring dashboards
Alert definitions
Incident response steps
Known failure modes
RTO/RPO and SLA targets
Validation results
Recent incidents and fixes
```

## Change Review

Ask:

- Is the change reversible?
- Is the rollout incremental?
- What validates success?
- What detects failure?
- Who owns rollback?
- What documentation changes after the rollout?
