# Fulfillment system design

## Blueprint

Service blueprinting connects a customer journey to the visible and internal work that supports it. Adapt the following table to the offer; split wide tables into stages when useful.

| Stage / trigger | Customer action | Visible service interaction | Internal production | Supporting people / systems | Artifact or evidence | Dependencies / handoff | Timing |
|---|---|---|---|---|---|---|---|

Keep customer actions separate from staff actions. Distinguish active work from waiting. Make the boundary between visible and internal activities apparent. Link stages to component IDs and show where customer feedback changes subsequent work.

For existing services, use actual delivery evidence to map the current journey before proposing changes. For new services, label the journey as a hypothesis. Include plausible failure paths relevant to the offer, such as incomplete intake or a deliverable rejected at review.

Source: [Nielsen Norman Group, Service Blueprints: Definition](https://www.nngroup.com/articles/service-blueprints-definition/). The table and commitment IDs are this skill's adaptation.

## Process definition and feedback

For each process, identify its intended result, inputs, outputs, resources, responsibility, interactions, and checks. Plan how results will be observed and the process improved. The amount of documentation should fit the work.

Translate this into an operating feedback loop: propose a process, pilot it, inspect output quality and customer results, then revise the design. Track process status separately from user agreement: **proposed**, **piloted** (with evidence and limitations), or **established** (with repeated delivery evidence). These labels are local conventions, not ISO classifications.

Source: [ISO, The process approach in ISO 9001:2015](https://www.iso.org/iso/iso9001_2015_process_approach.pdf). This is a lightweight adaptation of that guidance, not a compliance assessment.

## Capacity and cost checks — practical adaptation

Use one consistent period and include all demand on a shared role or resource.

- Role workload = sum of volume × effort per unit across applicable tasks, plus fixed recurring work, support, and expected rework.
- Compare workload with available delivery hours after other commitments. Do not assume all paid hours are available for fulfillment.
- For groups, distinguish effort per session or cohort from effort per attendee.
- For ongoing customers, distinguish new-customer onboarding load from the active customer base's recurring load.
- Delivery cost estimates can include labor, materials, vendors, software allocation, and relevant remedy costs. Separate setup cost from recurring cost and use ranges when uncertain.

Capacity is constrained by the tightest shared resource; passing a total-hours check does not prove the calendar works. Account for sequence, supplier delays, appointments, and customer response time. Do not infer queueing or lead time from averages alone.

If information is missing, show the calculation with variables or explicitly labeled illustrative assumptions. Never report invented throughput as measured capacity.

For a guarantee, specify the metric, baseline, measurement date, evidence source, responsible role, and promised remedy. Preserve existing terms; a proposed prerequisite is not automatically an enforceable condition. For capacity-based scarcity, compare the advertised limit with actual resource constraints.

## Optional completeness reference

[APQC Process Classification Framework](https://www.apqc.org/process-frameworks) organizes business processes and can reveal omitted supporting work. Consult only when breadth warrants it. It is a taxonomy, not a production recipe; do not import a whole enterprise operating model into a small offer.
