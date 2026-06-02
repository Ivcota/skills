# Performance Efficiency

Source anchors: Chapter 6, pages 177-180.

## Review Questions

1. Which user journeys define acceptable performance?
2. What are the target latency and throughput numbers for each critical journey?
3. Where can latency arise: client, network, edge, load balancer, compute, disk, database, or dependency?
4. Is the user base geographically distributed?
5. Would CDN, edge placement, caching, replication, or regional deployment reduce the critical path?
6. What database queries or write paths are likely to become bottlenecks?
7. Is partitioning, sharding, indexing, caching, or read replication required?
8. How will performance be monitored after launch?

## Diagnostic Pattern

```markdown
Critical workflow: [workflow]
Target: [latency/throughput/capacity]
Current or expected bottleneck: [component]
Metric to collect: [metric]
Architecture response: [design change]
Validation: [load test/trace/monitoring]
```

## Performance Anti-Patterns

- Treating bandwidth as the only performance metric.
- Measuring server response while ignoring user-perceived latency.
- Ignoring database query behavior until production.
- Placing large static assets far from global users.
- Failing to distinguish average latency from tail latency where user experience is sensitive.
