# The Three Cs — Deep Reference

## Sources
- howtoes.blog summary: https://howtoes.blog/2024/03/26/user-story-mapping-book-summary/
- O'Reilly TOC Ch 6: https://www.oreilly.com/library/view/user-story-mapping/9781491904893/
- marcabraham.com review: https://marcabraham.com/2015/05/07/book-review-user-story-mapping/
- briefshelf.com: https://briefshelf.com/book/user-story-mapping

---

## The 3 Cs Framework (Ron Jeffries, extended by Patton)

The 3 Cs framework originated with Ron Jeffries, one of the original XP contributors. Patton adopts and extends it in Chapter 6 of *User Story Mapping*. *(O'Reilly TOC; howtoes.blog/2024/03/26/)*

### Card
A physical token — index card, sticky note, or digital equivalent — with a short title. The card is not the requirement. It is a placeholder that invites a conversation.

> "Stories get their name from how they're supposed to be used, not what you're trying to write down." *(Patton, howtoes.blog/2024/03/26/)*

The title on the card should be short enough to fit on an index card: "Pay a bill," "Export report," "Manage account." The short title keeps the focus on the conversation, not the documentation.

### Conversation
The rich discussion that the card triggers. Shared understanding is built in the conversation — not in the writing of the card.

> "Shared documents aren't shared understanding." *(Patton, jpattonassociates.com/the-new-backlog/)*

The conversation happens when the right people are in the room together: developer, designer, PM, and ideally a user or someone who knows users well. Each person brings a different perspective that, when combined, produces a complete picture of what needs to be built and why.

### Confirmation
The shared agreement on how the team will know the story is done. Typically expressed as acceptance criteria or story tests. Confirmations are the output of the conversation — they represent current understanding, not a locked contract.

---

## The Conversation Checklist

Patton provides a checklist of topics to cover in the story conversation: *(marcabraham.com/2015/05/07/)*

| Topic | Questions to ask |
|-------|-----------------|
| **Who** | Which specific type of user does this? Are there multiple user types? |
| **What** | What exactly does the user do? Step by step? |
| **Why** | What are the user's goals? The business's goals? Do they align? |
| **Context** | Where is the user? What else is happening in their environment? |
| **Failures** | What goes wrong? What do users do when it fails? |
| **Assumptions** | What are we assuming about user behavior? About technical feasibility? |
| **Better solutions** | Is the story the right solution, or is there a better one we haven't considered? |
| **Implementation** | Rough approach — what does this cost to build? |
| **Timeline/cost** | What are the constraints? Does the approach fit? |

---

## The As/Want/So-That Template

Standard form: "As a [user type], I want [action], so that [outcome]."

The template's value is structural: it forces the team to state who benefits, what they do, and why. Each element is an opening for discussion:

- **As a** → "Who specifically? Are there different user types with different needs for this story?"
- **I want** → "Is this the action, or is there a higher-level goal we should build to?"
- **So that** → "Is this the real outcome? What behavior change are we targeting?"

The template is a conversation starter, not a specification. A story written without conversation produces requirements that look complete but contain hidden assumptions. *(briefshelf.com/book/user-story-mapping)*

---

## Confirmation Templates

Confirmations express the output of the conversation as testable conditions. Common format:

**Given** [user state / system state]  
**When** [user action]  
**Then** [observable result]

Multiple confirmations per story are expected — one for the happy path, one for each significant alternative or failure mode identified in the conversation.

A story is not done until its confirmations are all demonstrable in a working system. The confirmations — not the card title — are the actual definition of done.
