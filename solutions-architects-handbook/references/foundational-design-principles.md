# Foundational Design Principles

Source anchors: Chapter 2, pages 31-32; Chapter 1, pages 2-4; Chapter 16, pages 484-486.

## Principle Checklist

For each architecture, ask:

- **Scalability:** How does the system handle workload growth across web, application, and data layers?
- **Elasticity:** Can capacity grow and shrink to match demand and cost?
- **Resilience:** What failures are expected, contained, and recovered from?
- **Performance:** What latency, throughput, capacity, and user-experience targets matter?
- **Security:** Where are identity, authorization, data protection, and audit controls enforced?
- **Usability and accessibility:** Which user journeys must remain simple, inclusive, and observable?
- **Extensibility:** What future capabilities are likely, and what design choices preserve room for them?
- **Interoperability:** Which systems must exchange data or processes?
- **Portability:** Which platforms, environments, or vendors must the solution tolerate?
- **Automation:** Which provisioning, deployment, scaling, validation, and recovery steps should be automated?
- **Operations:** How will the solution be monitored, patched, supported, recovered, and improved?
- **Constraints:** What limitations shape the viable solution space?

## Common Review Move

When a proposal is too feature-focused, convert it into NFR questions:

| Feature Claim | Architecture Question |
|---|---|
| "Users can upload files" | What size, rate, latency, storage, scan, retention, and access controls are required? |
| "We need search" | What freshness, ranking, consistency, throughput, and failure behavior are acceptable? |
| "Use a queue" | What ordering, retry, deduplication, poison message, and backpressure behavior is required? |
| "Use cloud storage" | What durability, residency, encryption, access, lifecycle, and retrieval cost constraints apply? |
