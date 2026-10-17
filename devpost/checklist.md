---
doc: checklist
status: approved
---

# Build Checklist

Build mode: learn

## Slices

- [x] **1. Run the study-chat preview in demo mode**
  Becomes usable: A local browser app opens with a calm study-chat screen, academic topic suggestions, pasted-text input, empty-input guidance, a clearly labeled no-AI notice, and local word-frequency hints.
  Why now: Bootstrapping and the first visible behavior are one slice. This makes the interface usable immediately and establishes the safe credential boundary before connecting an external AI service.
  PRD ref: `prd.md > The Core Journey`; `prd.md > Screens and Layout`; `prd.md > Features and Behavior > Study chat`; `prd.md > States and Boundaries`
  Spec ref: `spec.md > Stack`; `spec.md > Where It Runs and How Someone Tries It`; `spec.md > Look and Feel`; `spec.md > Components > Study chat interface`; `spec.md > Components > Sample response mode`; `spec.md > Components > Local key terms`; `spec.md > Important Failure Modes`; `spec.md > File Structure`
  Build: Create the Streamlit scaffold and dependencies, main study-chat page, static academic suggestions, empty-input handling, calm/colorful/playful styling, clearly labeled demo mode, local key-term frequency hint, `.env.example`, and `.gitignore` protection for `.env`.
  Verify (mechanical): Run `python -m compileall app.py sample_responses.py text_insights.py`; start with `python -m streamlit run app.py --server.headless true`; request `http://localhost:8501/_stcore/health` and confirm a healthy response; confirm `.env` is ignored while `.env.example` is not.
  Learner check: Open the local app, inspect the first screen and topic suggestions, try sending empty input, then paste text. Confirm the app shows local word counts and does not claim to have generated an AI summary.
  Commit: `Build runnable study chat preview`

- [x] **2. Wire the optional AI path and transparent demo mode**
  Becomes usable: The app contains an optional live-request path and honest no-cost demo mode. One live summary was successfully generated from a sample passage; follow-up behavior remains unverified.
  Why now: Once the learner has tried the interface and its feedback is incorporated, add the optional provider path. Keeping the provider boundary separate makes missing credentials and provider errors testable without hiding them behind fake success.
  PRD ref: `prd.md > The Core Journey`; `prd.md > Features and Behavior > Study chat`; `prd.md > States and Boundaries`; `prd.md > What We're Building`
  Spec ref: `spec.md > The Core Journey Through the System`; `spec.md > Components > Conversation session`; `spec.md > Components > AI client`; `spec.md > External Services and Dependencies`; `spec.md > Data Model`; `spec.md > Important Failure Modes`; `spec.md > Decisions and Open Issues`
  Build: Add the optional OpenAI Responses API client using `OPENAI_API_KEY` from the local environment, retain study text and chat messages in session state, route summaries and follow-ups through the live client when configured, and show clear missing-key/provider-error feedback without substituting sample success. Add standard-library tests for request/context handling, missing-key behavior, and provider errors.
  Verify (mechanical): Run `python -m unittest`; run `python -m compileall app.py ai_client.py sample_responses.py text_insights.py`; start Streamlit and confirm its health endpoint responds; confirm default demo mode remains available even with a configured key. Never print or stage the key. One sample live summary was generated; follow-up behavior remains unverified.
  Learner check: One live summary was generated successfully for a sample passage. No follow-up response was tested.
  Commit: `Add live AI study summaries and follow-ups`

## Hands-on Checkpoints

- [x] Early usable behavior explored — learner confirmed the empty-input reminder and honest demo explanation are clear; continue with the optional provider path.
- [x] Initial kick-the-tires exploration and feedback completed — the demo notice correctly said no AI response was generated. The local word-count feature was reviewed separately.
- Slice 2 check — one sample live summary was successfully generated; follow-up responses remain unverified.

## Final Review

- [x] Review the new local Key terms panel — learner confirmed the counts are useful and it is clear they are not an AI summary.
- [x] Add in-chat explanation, flashcard, and short-quiz prompt buttons; in demo mode they show the honest no-AI notice, with no scoring or saved cards.
- [x] Refresh the visual treatment to a calming sage-green palette and a distinctive typographic wordmark.
- [x] Try the quick-action prompts in demo mode; the no-AI notice appears. Live replies to these prompts remain unverified.
- [x] Reopen the local app after it stopped; server health returned HTTP 200 and learner confirmed it works again.
- [x] Keep the no-cost demo as the default; live AI remains an explicit opt-in.
- [x] Initial interface review complete — the demo clearly distinguishes local hints from generated study content; live summary testing is recorded separately.

Initial final review approved the small no-cost interface demo.
The no-cost demo and local Key terms panel were reviewed. One live summary was
successfully generated from a sample passage; this does not establish broad
accuracy or verify follow-up responses.

## Code Tour and App Map

- [x] Learning activity complete — brief source-based recap
- [x] Optional edit and transfer reflection addressed — no edit was needed; reflection offered
- [x] `devpost/app-map.html` generated from finished code, checked, and shown, including a project-grounded practice to reuse

Activity and evidence: A brief static recap traced the pasted-text form and demo branch in `app.py` to `preview_notice()` in `sample_responses.py`. No direct source navigation or app interaction is claimed. The standalone map was opened offline, checked for content and narrow-screen layout, and shown.
Route and stops: `app.py` `study_input_form` → `app.py` `if not live_mode` → `sample_responses.py` `preview_notice()`. Explained as a static source recap.
Edit outcome: Not applicable; no edit was needed for the recap.
Activity mode: Brief static recap with app map.

## Revisions

- The project added a local Key terms panel by request. It shows up to three
  frequent non-common words and their counts; it does not interpret meaning or
  generate a summary. The updated scope, PRD, spec, tests, and app map describe
  this boundary.
- The no-cost interface demo remains the default. Project docs distinguish
  local frequency hints, demo notices, and live AI responses.
- The live provider path uses the documented Responses API with `gpt-4.1-mini`; one sample summary was successfully generated. Follow-up behavior remains unverified.
- Post-summary options for explanation, flashcards, and a short quiz are prompt buttons in the existing chat, not separate interactive/scored features.
- The visual treatment uses sage styling and a typographic wordmark without external assets.
- Live AI is off by default and clearly labeled as potentially using paid credits.
