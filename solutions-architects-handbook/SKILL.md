---
name: solutions-architects-handbook
description: |
  Apply, review, and explain solution architecture using Shrivastava and Srivastav's handbook model: align business goals, NFRs, architecture views, quality pillars, operations, cost, and documentation.
  Use when the user mentions "design this architecture", "review my solution architecture", "make this scalable", "write a solution architecture document", or "check the NFRs". Also trigger when the user is working on a SAD, cloud architecture design, architecture trade-off review, migration, modernization, or production-readiness review.
---

# Solutions Architect's Handbook

This skill distills *Solutions Architect's Handbook, Third Edition* by Saurabh Shrivastava and Neelanjali Srivastav into a practical review and design workflow for senior engineers and solution architects. The book defines solution architecture as a business and technical blueprint that spans strategic vision, immediate business needs, software, infrastructure, networking, security, compliance, operations, cost, and reliability. Source: Chapter 1, pages 2-4.

## Core Principle

Solution architecture turns business goals, constraints, stakeholder needs, and non-functional requirements into a technical blueprint that can be implemented, operated, evolved, and communicated across teams.

The handbook treats architecture as more than application structure. A solution architect is expected to connect business requirements, technology choices, data, infrastructure, operations, cost, reliability, security, and maintainability into one coherent design. Source: Chapter 1, pages 2-4.

The practical test is whether the design can be understood and used by its stakeholders. The Solution Architecture Document (SAD) should communicate the end-to-end solution, trace design choices to business and NFR needs, provide the views required for build/test/implementation, and define operational continuity after launch. Source: Chapter 16, pages 477-479.

**The foundation:** Architecture is a comprehensive blueprint for present business needs and future growth, not a one-time technology diagram. Source: Chapter 1, pages 2-4.

## The Solution Architecture Review Framework

### 1. Business-Aligned Blueprint

**Core concept:** Start with the business problem, stakeholders, value proposition, scope, assumptions, constraints, dependencies, risks, and measurable outcomes before selecting technologies.

**Why it works:** The handbook repeatedly frames architecture as a translation from business goals into technical vision. This keeps the design from optimizing isolated technical preferences while missing timeline, resource, budget, compliance, or stakeholder constraints.

**Key insights:**
- Solution architecture has both strategic and tactical responsibilities: long-term adaptability and immediate business workload needs. Source: Chapter 1, page 2.
- The design should include software plus infrastructure, networking, security, compliance, operations, cost, and reliability. Source: Chapter 1, page 2.
- A good architecture aligns technology choices with business requirements, long-term sustainability, maintainability, and team skill. Source: Chapter 1, pages 3-4.
- Architecture should expose assumptions, constraints, dependencies, and key decisions in the SAD. Source: Chapter 16, pages 482-484.
- Business context should include capabilities, key requirements, processes, stakeholders, and NFRs. Source: Chapter 16, pages 484-486.

**Product applications:**

| Context | Application | Example |
|---------|-------------|---------|
| **New product** | Define the solution purpose, scope, constraints, dependencies, and key decisions before detailed design | The SAD solution overview section includes purpose, scope, assumptions, constraints, dependencies, and architecture decisions. |
| **Modernization** | Document current state, target state, dependencies, transition plan, and migration risks | The SAD can present current/future architectures and a transition plan for existing applications. |
| **Enterprise platform** | Align technology with business requirements, sustainability, maintainability, and available team skills | Chapter 1 lists technology alignment as an attribute of good solution architecture. |
| **Stakeholder review** | Use architecture as a shared reference point for business, technical, and delivery teams | Documentation and visualization help stakeholders align and make decisions. |
| **Budget-sensitive project** | Tie scope, resources, timeline, and ROI back to architecture decisions | Chapter 1 connects architecture to resource planning, budget forecasting, risk mitigation, ROI, and timelines. |

**Copy patterns:**
- "This architecture solves [business concern] by [technical approach], with [constraints] explicitly in scope."
- "The target state supports [business capability] while preserving [NFR] and [operational constraint]."
- "Decision: choose [option] because [rationale]; trade-off: [cost/risk/complexity]."
- "Out of scope: [excluded need], because [constraint or dependency]."

See: [references/business-aligned-blueprint.md](references/business-aligned-blueprint.md) for SAD intake prompts and decision capture.

### 2. Foundational Design Principles

**Core concept:** Treat scalability, resilience, performance, immutability, loose coupling, service orientation, data-driven design, security, usability/accessibility, extensibility, interoperability, portability, automation, operations, and constraints as first-class design concerns.

**Why it works:** Functional correctness is not enough for a production architecture. The book uses these principles as the foundation for robust systems and revisits them through deeper chapters on performance, security, reliability, operations, cost, migration, data, ML, and GenAI.

**Key insights:**
- Scalability lets the system handle growing workload across layers such as web, application, and database tiers. Source: Chapter 2, page 32.
- Cloud elasticity changes the design conversation from fixed capacity to growth and shrinkage based on demand. Source: Chapter 2, page 32.
- Security, automation, operations, and constraints belong in design, not as late-stage add-ons. Source: Chapter 2, pages 31-32.
- Senior architects should make trade-offs visible across business, technical, resource, and operational constraints. Source: Chapter 1, pages 2-4; Chapter 16, pages 482-486.

**Product applications:**

| Context | Application | Example |
|---------|-------------|---------|
| **API platform** | Define expected workload growth, availability target, latency needs, and security model before implementation | NFRs should include scalability, availability/reliability, performance, portability, and capacity. |
| **Cloud system** | Prefer elastic scaling where workload fluctuates | Chapter 2 explains elasticity as growing and shrinking capacity to save unnecessary costs. |
| **Regulated product** | Include compliance and security constraints during solution overview and security architecture | SAD constraints include technical, business, resource, industry, and government compliance constraints. |
| **Integration-heavy system** | Make dependencies and upstream/downstream systems explicit | The integration architecture section lists data flows and system dependencies. |
| **Long-lived product** | Design for change, portability, automation, and operations | Chapter 2 includes future-proof extensibility, interoperability, portability, automation, and operation. |

**Copy patterns:**
- "NFRs: [scalability], [availability], [performance], [security], [maintainability], [capacity]."
- "Constraint: [constraint]. Architecture response: [design choice]."
- "Dependency: [system/team/vendor]. Failure impact: [impact]. Mitigation: [mitigation]."
- "This design assumes [assumption]; validate with [POC/test/metric]."

See: [references/foundational-design-principles.md](references/foundational-design-principles.md) for principle-by-principle review questions.

### 3. Performance Efficiency

**Core concept:** Design infrastructure and application resources to meet current demand while staying able to scale and evolve as user expectations and technology change.

**Why it works:** The handbook breaks performance into concrete pressure points: latency, throughput, network path, compute, disk, database behavior, storage choices, caching, and monitoring. This keeps performance review tied to user experience and measurable bottlenecks.

**Key insights:**
- Latency affects product adoption because users expect fast applications regardless of location. Source: Chapter 6, pages 177-179.
- Latency can come from network distance, router hops, transmission medium, compute, disk, or database behavior. Source: Chapter 6, pages 178-179.
- CDNs and edge locations can reduce latency by placing heavy content closer to users. Source: Chapter 6, pages 178-179.
- Lower latency generally increases throughput because more data can be transferred in less time. Source: Chapter 6, pages 179-180.
- Database partitioning and sharding can reduce load and latency when reads/writes are bottlenecked. Source: Chapter 6, page 179.

**Product applications:**

| Context | Application | Example |
|---------|-------------|---------|
| **Global web app** | Use CDN/edge placement for static-heavy content | The book recommends CDNs for heavy image/video data near user locations. |
| **Database-heavy service** | Investigate slow queries, read/write hardware, partitioning, and sharding | The book names database load and query processing as latency causes. |
| **Networked system** | Separate bandwidth, throughput, and latency in performance diagnosis | Chapter 6 distinguishes throughput from bandwidth and latency. |
| **User-facing workflow** | Define response-time tolerance and measure request/response latency | Chapter 6 frames latency as the delay between user action and visible response. |
| **Storage-sensitive workload** | Choose storage based on read/write throughput and latency needs | Chapter 6 discusses disk latency and throughput as performance factors. |

**Copy patterns:**
- "Performance target: [workflow] must respond within [threshold] under [load]."
- "Latency contributors: client distance, network path, compute, disk, database, and external dependencies."
- "Bottleneck hypothesis: [component] is limiting [latency/throughput]. Validate with [metric]."
- "Place [content/workload] closer to [user/data source] to reduce [latency path]."

See: [references/performance-efficiency.md](references/performance-efficiency.md) for performance review prompts.

### 4. Security Everywhere

**Core concept:** Apply security throughout the architecture using centralized identity, least privilege, defense in depth, blast-radius reduction, monitoring, auditing, and automation.

**Why it works:** Security fails when it is treated as perimeter protection or a final checklist. The handbook recommends layering controls across application, network, instance, operating system, traffic flow, identity, logging, and automated response.

**Key insights:**
- Authentication verifies access, while authorization determines what an authenticated user can do. Source: Chapter 7, page 208.
- Centralized user management helps onboard, deactivate, rotate, and monitor access consistently. Source: Chapter 7, page 208.
- Least privilege starts users with no access and grants only what their role requires. Source: Chapter 7, page 208.
- Defense in depth applies controls at every application layer rather than only the outer network boundary. Source: Chapter 7, pages 208-209.
- Blast-radius reduction isolates layers so compromise in one area does not spread freely. Source: Chapter 7, page 209.
- Centralized logging, audit, alerting, and automation support fast incident response. Source: Chapter 7, pages 209-210.

**Product applications:**

| Context | Application | Example |
|---------|-------------|---------|
| **Internal enterprise app** | Use centralized identity, role groups, and least privilege | The book gives development read-only production access as an authorization example. |
| **Public web app** | Layer DNS/edge, load balancer, network, instance, OS, IDS/IPS, and WAF controls | Chapter 7 describes defense in depth for a web application. |
| **Multi-tier system** | Separate load balancer, web, application, and database networks | The book recommends network separation to reduce blast radius. |
| **Compliance-heavy system** | Centralize logs and protect the logging account from tampering | Chapter 7 ties audit capabilities to compliance needs. |
| **DevSecOps workflow** | Automate detection and rollback of undesired security changes | Chapter 7 describes automation for unauthorized admin users or open firewall rules. |

**Copy patterns:**
- "Access model: default deny; grant [role] only [permissions] for [environment]."
- "Security layers: edge, network, load balancer, application, instance, OS, data, identity, audit."
- "Blast radius: if [component] is compromised, isolation limits impact to [scope]."
- "Security automation: detect [violation], alert [team], and revert [configuration]."

**Ethical boundary:** Do not design broad standing access. The handbook's least-privilege guidance starts with no access and grants only the required access types. Source: Chapter 7, page 208.

See: [references/security-everywhere.md](references/security-everywhere.md) for layered security review prompts.

### 5. Reliability and Recovery

**Core concept:** Design systems to operate correctly under stated conditions, contain failures to the smallest scope possible, and recover gracefully when failures occur.

**Why it works:** The handbook connects reliability with self-healing automation, redundancy, distributed design, capacity monitoring, recovery validation, RTO/RPO planning, and disaster recovery. These practices reduce interruption and turn failure handling into an engineered capability.

**Key insights:**
- Reliability focuses on correct operation under specific conditions and for a particular period. Source: Chapter 8, page 245.
- High availability aims to keep services accessible through redundant systems and failover. Source: Chapter 8, page 246.
- Self-healing systems monitor KPIs and automate recovery actions before users are heavily affected. Source: Chapter 8, pages 246-247.
- Distributed design reduces the impact area of a module or service failure. Source: Chapter 8, page 247.
- Recovery validation should test how systems fail and how recovery procedures work, not only happy paths. Source: Chapter 8, page 248.
- RTO and RPO should be driven by the application's SLA. Source: Chapter 8, page 249.

**Product applications:**

| Context | Application | Example |
|---------|-------------|---------|
| **E-commerce platform** | Prevent one service failure from stopping all customer actions | The book gives payment service failure not blocking order placement as an example. |
| **Autoscaled cloud app** | Monitor demand and automate resource addition/removal | Chapter 8 recommends maintaining resources without over- or under-provisioning. |
| **Critical data system** | Define RTO/RPO and backup/restore strategy | Chapter 8 connects RPO/RTO to SLA and data backup strategy. |
| **Distributed service** | Use circuit breakers around protected dependency calls | Chapter 8 references circuit breakers for dependency failures. |
| **Production readiness** | Simulate failures and validate recovery procedures before launch | Chapter 8 recommends regularly testing failover and recovery. |

**Copy patterns:**
- "Failure mode: [component] fails. Containment: [scope]. Recovery: [procedure]."
- "SLA: [availability]. RTO: [time]. RPO: [data-loss window]."
- "Self-healing trigger: when [KPI] crosses [threshold], automate [response]."
- "Recovery validation: simulate [failure] and verify [service/data/user impact]."

See: [references/reliability-and-recovery.md](references/reliability-and-recovery.md) for failure-mode review prompts.

### 6. Operational Excellence

**Core concept:** Run applications with minimal interruption and continuously improve the system, team practices, runbooks, and response procedures.

**Why it works:** Operations become fragile when they depend on manual work and undocumented tribal knowledge. The handbook emphasizes automation, incremental reversible changes, failure prediction, response simulation, root cause analysis, and updated runbooks.

**Key insights:**
- Operational excellence means minimal interruption and continuous improvement for business value. Source: Chapter 9, page 266.
- Manual operations are hard to sustain in modern hybrid, multi-cloud, microservice, and device-heavy systems. Source: Chapter 9, page 266.
- Infrastructure creation, service start/stop, and deployment should be automated where possible, including with IaC. Source: Chapter 9, pages 266-267.
- Changes should be small, incremental, tested, and reversible. Source: Chapter 9, page 267.
- Teams should anticipate failures, simulate response, and test RTO/RPO scenarios. Source: Chapter 9, page 267.
- Runbooks should include prior events, actions taken, start/stop/patch/update steps, validation results, response procedures, and SLA targets. Source: Chapter 9, page 268.

**Product applications:**

| Context | Application | Example |
|---------|-------------|---------|
| **Production service** | Automate deployment, configuration, scaling, and incident response steps | Chapter 9 says automation frees teams for strategic work and reduces human error. |
| **Patch/change process** | Make changes incremental and reversible | Chapter 9 recommends reversible changes to restore working condition after issues. |
| **On-call system** | Keep runbooks current and people-independent | Chapter 9 warns that outdated runbooks make operations people-dependent. |
| **SLA-backed product** | Simulate incidents against RTO/RPO and response procedures | Chapter 9 recommends production-like response exercises. |
| **Continuous improvement** | Run RCA and update runbooks after incidents | Chapter 9 recommends five Whys and runbook updates. |

**Copy patterns:**
- "Operational readiness: monitoring, alerts, support charter, vendor path, runbook, RTO/RPO."
- "Change plan: small increment, automated rollout, validation, rollback path."
- "Incident learning: root cause, contributing factors, prevention, runbook update."
- "People-independence check: can a new operator resolve [incident] from the runbook?"

See: [references/operational-excellence.md](references/operational-excellence.md) for production-readiness prompts.

### 7. Cost and Value Optimization

**Core concept:** Increase business value and minimize risk while reducing lifecycle cost.

**Why it works:** Architecture decisions create costs long after acquisition. The handbook distinguishes upfront cost from total cost of ownership and uses budget, forecast, demand management, service catalogs, cost monitoring, and continuous optimization to keep value and spend visible.

**Key insights:**
- Cost optimization includes increasing business value, minimizing risk, and reducing business costs. Source: Chapter 10, page 290.
- TCO matters more than upfront purchase cost for long-term decisions. Source: Chapter 10, page 290.
- TCO includes CapEx and OpEx across operation, maintenance, training, and retirement. Source: Chapter 10, pages 290-291.
- Budgets guide long-term planning, while forecasts help teams take near-term action. Source: Chapter 10, pages 292-293.
- Demand forecasts and service catalogs can help align IT infrastructure supply with business needs and economies of scale. Source: Chapter 10, pages 293-294.

**Product applications:**

| Context | Application | Example |
|---------|-------------|---------|
| **Buy vs build** | Compare SaaS subscription, IaaS-hosted software, and custom build by TCO and requirements fit | Chapter 10 contrasts SaaS, IaaS, and build-yourself options. |
| **Cloud migration** | Compare CapEx/OpEx, maintenance, licensing, migration, security, compliance, and scalability costs | Chapter 10 and Chapter 15 discuss TCO and cloud migration cost analysis. |
| **Department platform** | Aggregate demand to improve buying power and reduce overprovisioning | Chapter 10 recommends demand forecasts from organizational units. |
| **Monthly cost review** | Use forecast to adjust spend before budget overrun | Chapter 10 distinguishes budget from forecast. |
| **Architecture decision** | Include operational expense as a trade-off in decision rationale | Chapter 16 gives cloud scalability as lower upfront capital with continuing OpEx. |

**Copy patterns:**
- "Cost model: CapEx [items], OpEx [items], migration [items], training [items], retirement [items]."
- "Budget says [plan]; forecast says [current trajectory]; action: [cost control]."
- "Decision trade-off: [lower upfront cost] creates [ongoing operational expense]."
- "Demand source: [team/unit]. Expected usage: [usage]. Provisioning response: [plan]."

See: [references/cost-and-value-optimization.md](references/cost-and-value-optimization.md) for TCO and cost-review prompts.

### 8. Documentation and Communication

**Core concept:** Use the Solution Architecture Document as the shared artifact that communicates the design, rationale, views, requirements traceability, and operational plan.

**Why it works:** The SAD bridges business and technical stakeholders. It gives project managers, analysts, developers, IT teams, senior management, clients, and end users an architecture reference that supports coordination, implementation, maintenance, and strategic decisions.

**Key insights:**
- The SAD provides an end-to-end application view and keeps stakeholders on the same page. Source: Chapter 16, page 477.
- The SAD should communicate the solution, address service-quality requirements, trace design to requirements, define impacts, and cover continuity/operations. Source: Chapter 16, pages 477-478.
- SAD views can include business, logical, process, deployment, implementation, data, and operational views. Source: Chapter 16, pages 479-481.
- SAD structure should adapt to the project, such as new product, modernization, or cloud migration. Source: Chapter 16, page 481.
- SAD lifecycle includes initiation, requirements, drafting, review, finalization, implementation, and maintenance. Source: Chapter 16, pages 493-494.
- Clear, concise, current documentation and stakeholder involvement are best practices; overcomplication, rigidity, low engagement, and poor documentation are pitfalls. Source: Chapter 16, pages 494-495.

**Product applications:**

| Context | Application | Example |
|---------|-------------|---------|
| **SAD draft** | Include purpose, views, structure, lifecycle, best practices, and procurement awareness | Chapter 16 lists these as SAD chapter topics. |
| **Business review** | Use business view and conceptual overview to communicate value and capabilities | Chapter 16 recommends business-readable diagrams and high-level views. |
| **Technical delivery** | Use implementation, application, data, integration, infrastructure, and security views | Chapter 16 maps SAD sections to development, database, vendor, infrastructure, and security audiences. |
| **Production handoff** | Include monitoring, incident management, support, DR, BPC, and maintenance procedures | Chapter 16 describes solution management sections. |
| **Architecture governance** | Keep decisions, rationale, pros/cons, and change records current | Chapter 16 recommends key architecture decisions and a SAD lifecycle. |

**Copy patterns:**
- "View: [business/logical/process/deployment/implementation/data/operational]. Audience: [stakeholders]. Purpose: [decision/use]."
- "Requirement trace: [business requirement] maps to [architecture decision] and [NFR]."
- "Decision record: problem, options, pros/cons, chosen approach, rationale, impact."
- "SAD lifecycle status: initiation, requirements, draft, review, final, implementation, maintenance."

See: [references/documentation-and-communication.md](references/documentation-and-communication.md) for SAD structure and review prompts.

## Solution Architecture Review Process

Follow these steps in order to apply the framework from scratch or review an existing design:

1. **Establish the business context.** Capture stakeholders, goals, capabilities, scope, assumptions, constraints, dependencies, and risks. Source: Chapter 1, pages 2-4; Chapter 16, pages 482-485.
2. **Make NFRs explicit.** Define scalability, availability, reliability, performance, security, maintainability, portability, capacity, and compliance needs. Source: Chapter 1, page 2; Chapter 16, pages 485-486.
3. **Choose candidate architecture views and patterns.** Build a conceptual view, then deepen into application, data, integration, infrastructure, security, deployment, and operational views. Source: Chapter 16, pages 479-492.
4. **Review quality pillars.** Test the design against performance, security, reliability, operations, and cost principles. Source: Chapters 6-10.
5. **Document decisions and trade-offs.** Record options, pros/cons, rationale, resources, skills, and implementation impact. Source: Chapter 16, pages 480-484.
6. **Validate the design.** Use POCs, assessments, trade-off studies, tests, failure simulations, monitoring assumptions, and stakeholder review. Source: Chapter 8, page 248; Chapter 16, pages 478-486.
7. **Maintain the SAD.** Keep the document current through implementation and operation as technology, business objectives, and external constraints change. Source: Chapter 16, pages 493-495.

## Common Mistakes

| Mistake | Why It Fails | Fix |
|---------|-------------|-----|
| **Treating architecture as software-only** | It misses infrastructure, network, security, compliance, operations, cost, and reliability. | Cover the whole system and its business context. |
| **Ignoring NFRs** | Scalability, reliability, performance, availability, security, and maintainability are often missed by business users and delivery teams. | Capture NFRs explicitly in the business context and SAD. |
| **Focusing on perimeter security only** | A single outer layer does not protect every application layer. | Apply defense in depth and security at every layer. |
| **Depending on manual operations** | Manual work is slow, error-prone, and hard to scale across modern systems. | Automate operations and use IaC where possible. |
| **Validating only the happy path** | Recovery and failover procedures may fail when they are needed. | Test failure modes and recovery procedures regularly. |
| **Optimizing for upfront cost only** | CapEx ignores maintenance, operations, training, retirement, and lifecycle costs. | Use TCO and ROI analysis. |
| **Letting SADs go stale** | Outdated documents create implementation ambiguity and people-dependence. | Treat the SAD as a running lifecycle document. |

## Quick Diagnostic

Use this table to audit an existing architecture:

| Question | If No | Action |
|----------|-------|--------|
| Does the design trace technology choices to business goals and stakeholder needs? | Architecture may be technically plausible but commercially misaligned. | Rebuild the solution overview and decision rationale. |
| Are NFRs explicit and measurable? | Teams may discover scale, reliability, performance, or security gaps late. | Define NFRs in the business context and quality-pillar sections. |
| Are assumptions, constraints, dependencies, and risks documented? | Hidden constraints can derail delivery or operation. | Add them to the SAD solution overview. |
| Is security layered across identity, network, application, instance, data, logging, and automation? | Compromise can spread too far or remain undetected. | Apply least privilege, defense in depth, blast-radius limits, and auditing. |
| Are failure modes, RTO, RPO, and recovery procedures tested? | The system may be available only on the happy path. | Run recovery validation and incident simulations. |
| Are operations automated and runbooks current? | Support depends on manual work and specific people. | Automate repeatable tasks and update runbooks after change and incidents. |
| Is TCO visible beyond upfront cost? | Design choices may create long-term budget surprises. | Compare CapEx, OpEx, maintenance, training, migration, and retirement costs. |
| Does the SAD contain business, logical, process, deployment, implementation, data, and operational views where useful? | Stakeholders lack the views they need to decide and execute. | Add the missing views or explain why they are not needed. |

## Reference Files

- [business-aligned-blueprint.md](references/business-aligned-blueprint.md): Business context, stakeholders, constraints, and decision rationale.
- [foundational-design-principles.md](references/foundational-design-principles.md): Review questions for the handbook's foundational architecture attributes.
- [performance-efficiency.md](references/performance-efficiency.md): Latency, throughput, bottleneck, and monitoring prompts.
- [security-everywhere.md](references/security-everywhere.md): Layered security and least-privilege review prompts.
- [reliability-and-recovery.md](references/reliability-and-recovery.md): Failure containment, self-healing, RTO/RPO, and DR prompts.
- [operational-excellence.md](references/operational-excellence.md): Automation, reversible change, runbook, and incident-learning prompts.
- [cost-and-value-optimization.md](references/cost-and-value-optimization.md): TCO, budget, forecast, and cost trade-off prompts.
- [documentation-and-communication.md](references/documentation-and-communication.md): SAD structure, lifecycle, and stakeholder communication.
- [case-studies.md](references/case-studies.md): Source-grounded examples and reusable review moves.
- [checklist.md](references/checklist.md): End-to-end worksheet for applying the skill.

## Further Reading

This skill is based on *Solutions Architect's Handbook, Third Edition* by Saurabh Shrivastava and Neelanjali Srivastav.

- *Solutions Architect's Handbook, Third Edition*, Packt Publishing, ISBN 978-1-83508-423-6. Source: book frontmatter.
- *AWS for Solutions Architects*, referenced by the authors for AWS-focused cloud solution architecture career development. Source: Chapter 1, page 29.

## About the Authors

**Saurabh Shrivastava** is described in the book as a technology leader, author, inventor, and public speaker with over 20 years in IT, working at AWS as a Global Solutions Architect Leader. Source: book contributor section.

**Neelanjali Srivastav** is described in the book as a technology leader, product manager, and agile coach, with experience at Aya Healthcare and AWS across database, analytics, and machine learning services. Source: book contributor section.
