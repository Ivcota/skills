# Case Studies

Source anchors: Chapter 6, pages 177-180; Chapter 7, pages 207-210; Chapter 8, pages 247-249; Chapter 10, pages 290-294; Chapter 16, pages 482-492.

## E-Commerce Order Platform

The handbook repeatedly uses e-commerce examples to explain SAD structure, application architecture, integration, and reliability.

### Review Moves

- Model the end-to-end order flow from customer order through inventory, payment, tax, transport, fulfillment, shipment, notification, return, and cancellation.
- Define business purpose as streamlining and automating order management.
- Keep post-delivery engagement out of scope when it is not part of the stated solution boundary.
- List dependencies such as inventory systems, payment gateways, marketplaces, and shipping carriers.
- Include data flows, application modules, integration points, infrastructure, and security controls in the SAD.

## Payment Service Failure

Chapter 8 uses an e-commerce payment service to show why distributed design can reduce impact area.

### Review Moves

- Identify which user journeys must continue when a component fails.
- Decide whether order placement should continue if payment is delayed.
- Define compensating flow, retry behavior, and operational alerting.
- Use the case to test whether distributed design improves reliability or creates hidden consistency risk.

## Global Web Application Performance

Chapter 6 uses web browsing and request-response latency to explain latency and throughput.

### Review Moves

- Trace the full request path from user device to server and back.
- Identify geographic distance, routing, network congestion, compute, disk, and database causes of delay.
- Use CDN or edge placement when heavy content is served to distributed users.
- Separate latency targets from throughput and bandwidth assumptions.

## Enterprise Identity and Least Privilege

Chapter 7 uses internal enterprise applications and development/production access separation to explain centralized authorization.

### Review Moves

- Centralize authentication and authorization.
- Group permissions by job role.
- Give development teams the access they need in lower environments while restricting production access.
- Add SSO and MFA where appropriate.
- Audit user activity and remove inactive access.

## Cost Trade-Off: SaaS, IaaS, or Build

Chapter 10 compares off-the-shelf software, SaaS, IaaS-hosted software, and build-your-own options.

### Review Moves

- Compare TCO, not just upfront purchase cost.
- Include purchase/setup, operational/maintenance, human resources, training, migration, and retirement costs.
- Decide whether subscription pricing, cloud-hosted software, or custom build best fits the requirement and user scale.
- Revisit the forecast regularly instead of relying only on annual budget.
