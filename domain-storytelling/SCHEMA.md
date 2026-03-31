# YAML Schema

Each domain story is saved as a YAML file in `domain-stories/` at the project root.

File naming convention: kebab-case matching the story name (e.g., `customer-places-order.yaml`).

## Structure

```yaml
name: customer-places-order
description: A customer browses the catalog and places an order
type: to-be # or as-is
granularity: fine # or coarse

actors:
  - name: Customer
    type: person # person | group | system
  - name: Inventory System
    type: system

work_objects:
  - name: Order
    contains:
      - Order Item
  - name: Catalog
  - name: Payment

activities:
  - number: 1
    actor: Customer
    verb: browses
    work_object: Catalog
  - number: 2
    actor: Customer
    verb: adds
    work_object: Order Item
    target_actor: null
  - number: 3
    actor: Customer
    verb: submits
    work_object: Order

annotations:
  - target: Order
    note: "Must contain at least one Order Item"

groups:
  - name: Shopping
    activities: [1, 2]
  - name: Checkout
    activities: [3]
```

## Field Reference

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Kebab-case story identifier |
| `description` | Yes | One-line summary of the scenario |
| `type` | Yes | `as-is` or `to-be` |
| `granularity` | Yes | `fine` or `coarse` |
| `actors` | Yes | List of participants (name + type: person/group/system) |
| `work_objects` | Yes | Things actors work with; optional `contains` for composition |
| `activities` | Yes | Numbered sequence of actor-verb-work_object triples |
| `annotations` | No | Rules or constraints on specific elements |
| `groups` | No | Named groupings of activities (e.g., by phase or team) |
