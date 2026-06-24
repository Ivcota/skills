# Skills

This context defines the language used to design and describe reusable AI skills in this repository.

## Language

**Problem Frame**:
A clear definition of a problem in terms of the outcome the user wants to achieve and the obstacles standing in the way. A problem is not ready for solving until this frame is explicit and user-owned.
_Avoid_: Problem statement, problem definition

**User-Owned Problem Frame**:
A Problem Frame the user can explain back in plain language and take responsibility for. The skill may help clarify it, but must not replace the user's own understanding.
_Avoid_: Agent-defined problem, expert diagnosis

**Plain-Language Restatement**:
A jargon-free explanation of the Problem Frame in the user's own words. It is used to test whether the user truly understands the problem being defined.
_Avoid_: Summary, formal definition

**Teach-Back Check**:
The final clarity gate before the Problem Handoff. The user must explain the Problem Frame plainly, including the desired outcome, obstacle, and Root-Cause Condition.
_Avoid_: Confirmation check, approval step

**Clarity Gate**:
The completion criterion for the problem-defining phase. The gate is passed only when the user can plainly state the desired outcome, obstacle, and Root-Cause Condition.
_Avoid_: Agreement check, approval gate

**Root-Cause Condition**:
A counterfactual condition that, if true, would prevent the problem from existing. It helps distinguish surface obstacles from the deeper condition that must change.
_Avoid_: Root cause, why question

**Problem Firewall**:
A skill that prevents solutioning until the user owns a clear Problem Frame. It combines a Problem-Solution Firewall with a Teach-Back Check.
_Avoid_: Problem clarifier, problem framing assistant

**Problem-Solution Firewall**:
A hard separation between defining the problem and choosing how to solve it. The firewall protects the skill from prematurely optimizing around a proposed solution.
_Avoid_: Brainstorming boundary, solution pause

**Solution Parking Lot**:
A temporary holding place for solution ideas mentioned during problem definition. Parked solutions may inform problem discovery, but they are not evaluated until the Problem Frame is complete.
_Avoid_: Ideas list, solution backlog

**Problem Handoff**:
The routing step after the Problem Frame is complete. It asks whether the user already has a preferred solution-starting path, and if not, matches the clarified problem to relevant skills or methods.
_Avoid_: Next steps, branch menu

**Problem Shape**:
The broad kind of clarified problem used to route the Problem Handoff. Core shapes include cause problems, decision problems, execution problems, and design problems.
_Avoid_: Problem category, issue type

**Test of Time**:
A safeguard that checks whether a proposed solution would resolve the root-cause condition permanently or whether the problem would return. It helps identify when the user is treating a symptom instead of the problem.
_Avoid_: Time test, durability check
