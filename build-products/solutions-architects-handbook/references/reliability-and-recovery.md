# Reliability and Recovery

Source anchors: Chapter 8, pages 245-249.

## Failure-Mode Review

Use this loop:

1. List critical user journeys and system components.
2. For each component, state how it fails.
3. Define containment: what still works?
4. Define detection: what metric or event shows the failure?
5. Define recovery: automatic, manual, or failover?
6. Define RTO and RPO where data or downtime matters.
7. Simulate the failure and update the runbook.

## Reliability Prompts

- What are the KPIs that show the system is approaching failure?
- Can the system add or remove capacity automatically?
- Which components are redundant, and which remain single points of failure?
- Does a distributed design reduce impact, or does it introduce uncontrolled complexity?
- Which dependencies need circuit breakers, retries, timeouts, or queues?
- Are backups and restore procedures tested?

## RTO/RPO Template

```markdown
Service/workflow: [name]
SLA: [availability]
RTO: [maximum acceptable recovery time]
RPO: [maximum acceptable data loss]
Backup strategy: [strategy]
Failover strategy: [strategy]
Validation test: [test]
Last validated: [date]
```
