# Responsibility-Driven Design (RDD)

## Stereotypes

Each responsibility maps to one of these stereotypes, which determines its 54321 layer placement:

| Stereotype              | Layer | Examples                                            |
|--------------------------|-------|-----------------------------------------------------|
| **Information Holder**   | 1-2   | Entities, value objects, DTOs, domain events         |
| **Structurer**           | 2     | Aggregates, collections, cache                       |
| **Service Provider**     | 1     | Stateless domain services, utility classes           |
| **Coordinator**          | 3     | Event listeners, routers, input handlers             |
| **Controller**           | 3     | Use cases, interactors, application services, presenters |
| **Interfacer**           | 4-5   | Repositories, HTTP servers, external API facades     |

## Process

### 1. Responsibility Discovery

For the feature as a whole, enumerate:
- **Doings** — what must the system do? (behaviors, computations, persistence, coordination)
- **Knowings** — what must the system know? (state, rules, configuration)

### 2. Assign Roles

Map each responsibility to a stereotype from the table above and place it in the corresponding 54321 layer.

### 3. Produce CRC Cards

For each candidate object:
- **Front:** name, purpose/role, patterns, stereotype
- **Back:** responsibilities (knows / does / decides), collaborators

### 4. Design Collaborations

- For each *doing* responsibility: "what role helps with this task?"
- For each *knowing* responsibility: "what roles need to know this?"

### 5. Map to 54321 Layers

```
Level 5 (Driving UI)
    ↓ uses
Level 3 (Application/Coordination)
    ↓ uses                    ↓ uses
Level 4 (Driven Infra)    Level 2 (Domain)
                              ↓ uses
                          Level 1 (Pure functions)
```

Place each role in a layer. Dependencies must point inward — inner layers never know about outer layers.
