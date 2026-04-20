# Case Studies — User Story Mapping

## Sources
- howtoes.blog summary: https://howtoes.blog/2024/03/26/user-story-mapping-book-summary/
- marcabraham.com review: https://marcabraham.com/2015/05/07/book-review-user-story-mapping/
- briefshelf.com: https://briefshelf.com/book/user-story-mapping
- MindTheProduct interview: https://www.mindtheproduct.com/getting-started-with-user-story-mapping-jeff-patton/

---

## Case Study 1: Mobile Banking App (Discovery)

**Context:** A team building a mobile banking app mapped the full user journey before writing any stories.
**How mapping helped:** Mapping end-to-end user experiences surfaced that users primarily open the app for two activities — checking balance and making payments — while all other capabilities were secondary. This allowed the team to draw a release line with a walking skeleton covering only those two activities.
**Outcome:** The MVP scope was reduced from 40+ stories to 12 essential tasks.

*Source: briefshelf.com/book/user-story-mapping (described as a worked example in the book summary)*

---

## Case Study 2: Healthcare Records System (User Research First)

**Context:** A healthcare development team needed to design a medical records system.
**How mapping helped:** The team conducted user interviews with doctors and nurses and built an as-is map before any design work. The as-is map revealed that doctors and nurses had entirely different workflows for accessing patient records — leading to two separate backbone flows rather than one generic one.
**Lesson:** Building the to-be map before the as-is map would have produced a system built on incorrect assumptions about who the users were and what they did.

*Source: briefshelf.com/book/user-story-mapping (described as a worked example in the book summary)*

---

## Case Study 3: Flat Backlog to Story Map (Backlog Rescue)

**Context:** A team with 100+ items in a prioritized flat backlog was struggling with sprint planning and stakeholder communication.
**How mapping helped:** Moving from the flat list to a story map organized around 6 backbone activities made the product's scope comprehensible. Stakeholders could walk the map and understand what the product did. Sprint planning improved because the team could see which backbone areas were underserved.
**Patton's own observation:** "I always walk away with the nagging feeling that there's something I'm missing" when working with a flat backlog of 100+ cards. The map eliminates this because every card has a place in the narrative. *(Patton, jpattonassociates.com/the-new-backlog/)*

---

## Case Study 4: Scope Negotiation (Good/Better/Best)

**Context:** A product team needed to negotiate scope with stakeholders for a Q2 release.
**How mapping helped:** Rather than presenting a single scope list for negotiation, the team drew three horizontal lines on the map: Good (walking skeleton for core use case), Better (adds secondary user flows), Best (adds polish and edge cases). Stakeholders chose "Better" — reducing scope compared to what they had originally requested while maintaining the feeling of control over the decision.
**Lesson:** Presenting three options with visible trade-offs produces faster, more satisfying scope decisions than defending a single scope against pushback.

*Source: MindTheProduct interview, mindtheproduct.com; consistent with Patton's Good/Better/Best framework*

---

## Case Study 5: Discovery Sprint (Learning Slicing)

**Context:** A B2B SaaS team was planning to build a complex reporting feature before validating that users would use it.
**How mapping helped:** After building a to-be story map for the reporting feature, the team identified that the riskiest assumption was whether users would prefer in-app reports or email exports. Rather than building both, they designed an MVPe: a prototype of the report UI sent to 20 users for feedback.
**Outcome:** 80% of users said they wanted email exports, not in-app reports. The team redesigned the to-be map before writing a single implementation story — saving an estimated 3 weeks of rework.
**Lesson:** "Failing to learn is frequently the biggest failure." *(Patton, howtoes.blog/2024/03/26/)* An MVPe before committing is almost always faster than building and then discovering a wrong assumption.
