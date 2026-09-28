# Inquiry Journeys

Read the section matching the active journey.

## Resume an Inquiry

Reconstruct the latest explicit state from the conversation or supplied artifact. State the last passed Gate and resume at the earliest step whose Output is incomplete or invalid.

## New Evidence Arrives

Make Step 9 active, incorporate the Evidence, and identify the earliest step whose Output materially changes. Resume there and retain earlier Outputs that remain valid.

## Execute or Hand Off

At Step 8:

- Execute the move with available tools when it is authorized and within the agent's capabilities.
- When user authority or real-world access is required, provide the exact action, expected Evidence, and relevant Risk, then wait for the result.
- Treat a decision as executed when the authorized person explicitly commits to it.
- Execute a deliberate pause by defining its duration, trigger, or reopening condition.

A recommendation is an input to Step 8. Pass the Gate when execution is confirmed.

## Pause and Resume Later

Produce a resumable snapshot containing:

- Active step and Gate status
- Bounded Inquiry
- Current Working Model
- Material information gap
- Expected next input or action

Write the snapshot to Markdown when the user requests persistence. For a consequential or long-running Inquiry, offer persistence once at a natural checkpoint.
