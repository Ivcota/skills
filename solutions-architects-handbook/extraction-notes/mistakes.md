# Extraction Notes: Common Mistakes

| Mistake | Why It Fails | Fix | Source |
|---|---|---|---|
| Treating architecture as software-only | Misses infrastructure, network, security, compliance, operations, cost, and reliability concerns | Cover the whole system and the business context | Chapter 1, pages 2-4 |
| Ignoring NFRs | Scalability, reliability, performance, availability, security, and maintainability are often missed by business users and development teams | Capture NFRs explicitly in the business context and SAD | Chapter 1, page 2; Chapter 16, pages 485-486 |
| Focusing on perimeter security only | A single outer layer does not protect each application layer | Apply defense in depth and security at every layer | Chapter 7, pages 208-209 |
| Depending on manual operations | Manual work is slow, error-prone, and hard to scale across modern hybrid and multi-cloud systems | Automate operations and use IaC where possible | Chapter 9, pages 266-267 |
| Validating only the happy path | Recovery and failover procedures can fail when needed | Test failure modes and recovery procedures regularly | Chapter 8, page 248 |
| Optimizing for upfront cost only | CapEx omits maintenance, operations, training, retirement, and lifecycle costs | Use TCO and ROI analysis | Chapter 10, pages 290-291 |
| Letting SADs go stale | Outdated documents create implementation ambiguity and people-dependence | Treat the SAD as a running lifecycle document | Chapter 16, pages 493-495 |
