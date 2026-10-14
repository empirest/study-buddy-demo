---
doc: checklist
status: approved
---

# Build Checklist

Build mode: learn

## Slices

- [x] **1. Run the study-chat preview in demo mode**
  Becomes usable: A local browser app opens with a calm study-chat screen, academic topic suggestions, pasted-text input, empty-input guidance, and a clearly labeled demo preview that does not claim to summarize the learner's text.
  Why now: Bootstrapping and the first visible behavior are one slice. This makes the interface usable immediately and establishes the safe credential boundary before connecting an external AI service.
  PRD ref: `prd.md > The Core Journey`; `prd.md > Screens and Layout`; `prd.md > Features and Behavior > Study chat`; `prd.md > States and Boundaries`
  Spec ref: `spec.md > Stack`; `spec.md > Where It Runs and How Someone Tries It`; `spec.md > Look and Feel`; `spec.md > Components > Study chat interface`; `spec.md > Components > Sample response mode`; `spec.md > Important Failure Modes`; `spec.md > File Structure`
  Build: Create the Streamlit scaffold and dependencies, main study-chat page, static academic suggestions, empty-input handling, calm/colorful/playful styling, clearly labeled sample mode, `.env.example`, and `.gitignore` protection for `.env` and the learner profile.
  Verify (mechanical): Run `python -m compileall app.py sample_responses.py`; start with `python -m streamlit run app.py --server.headless true`; request `http://localhost:8501/_stcore/health` and confirm a healthy response; confirm `.env` and `devpost/learner-profile.md` are ignored while `.env.example` is not.
  Manual check: The first screen shows topic suggestions and empty-input guidance. Pasted text receives a clearly labeled demo notice, not a claimed summary.
  Commit: `Build runnable study chat preview`

- [x] **2. Wire the optional AI path and transparent demo mode**
  Becomes usable: The app contains an optional live-request path and an honest no-cost demo mode. Live summary and contextual follow-up behavior are not verified.
  Why now: Add the optional provider path after the interface is available. Keeping the provider boundary separate makes missing credentials and provider errors testable without hiding them behind fake success.
  PRD ref: `prd.md > The Core Journey`; `prd.md > Features and Behavior > Study chat`; `prd.md > States and Boundaries`; `prd.md > What We're Building`
  Spec ref: `spec.md > The Core Journey Through the System`; `spec.md > Components > Conversation session`; `spec.md > Components > AI client`; `spec.md > External Services and Dependencies`; `spec.md > Data Model`; `spec.md > Important Failure Modes`; `spec.md > Decisions and Open Issues`
  Build: Add the optional OpenAI Responses API client using `OPENAI_API_KEY` from the local environment, retain study text and chat messages in session state, route summaries and follow-ups through the live client when configured, and show clear missing-key/provider-error feedback without substituting sample success. Add standard-library tests for request/context handling, missing-key behavior, and provider errors.
  Verify (mechanical): Run `python -m unittest`; run `python -m compileall app.py ai_client.py sample_responses.py`; start Streamlit and confirm its health endpoint responds; confirm default demo mode remains available even with a configured key. Never print or stage the key. No live response was verified.
  Manual check: Demo mode clearly says no request was made. No real AI summary or contextual follow-up was demonstrated.
  Commit: `Add live AI study summaries and follow-ups`

## Hands-on Checkpoints

- [x] Early usable behavior explored — empty-input guidance and the honest demo explanation are clear.
- [x] Final kick-the-tires exploration and feedback completed — the revised look and a quick action were tried; the notice correctly says no analysis occurred.
- Slice 2 manual check — demo mode explains that no request was made; the optional live response remains unverified.

## Final Review

- [x] Add in-chat explanation, flashcard, and short-quiz prompt buttons; in demo mode they show the honest no-analysis notice, with no scoring or saved cards.
- [x] Refresh the visual treatment to a calming sage-green palette and a distinctive typographic wordmark.
- [x] Try the quick-action prompts in demo mode; the no-analysis notice appears. Real AI-generated output remains unverified.
- [x] Reopen the local app after it stopped; server health returned HTTP 200.
- [x] Final review complete — the small no-cost interface demo is approved; live AI behavior is explicitly unverified and not claimed.

Final review: approved as a deliberately small no-cost interface demo. Live
AI behavior remains unverified and is not a completion claim.

## Code Tour and App Map

- [x] Learning activity complete — brief source-based recap
- [x] Optional edit and transfer reflection addressed — no edit was needed; reflection offered
- [x] `devpost/app-map.html` generated from finished code, checked, and shown, including a project-grounded practice to reuse

Activity and evidence: A brief static recap traced the pasted-text form and demo branch in `app.py` to `preview_notice()` in `sample_responses.py`. No direct source navigation or app interaction is claimed. The standalone map was opened offline, checked for content and narrow-screen layout, and shown.
Route and stops: `app.py` `study_input_form` → `app.py` `if not live_mode` → `sample_responses.py` `preview_notice()`. Explained as a static source recap.
Edit outcome: Not applicable; no edit was needed for the recap.
Reflection: Optional transfer question offered; personal reflection is not included in this public project record.
Activity mode: Brief static recap with app map.

## Revisions

- The scope, PRD, and spec distinguish the visible demo from unverified live-AI behavior; no generated summary is claimed.
- The optional provider path uses the documented Responses API with `gpt-4.1-mini`; successful live responses are not verified.
- Explanation, flashcard, and short-quiz options are prompt buttons in the existing chat, not separate interactive/scored features.
- The visual treatment uses sage styling and a typographic wordmark without external assets.
- Demo mode is the default. Live AI is off unless deliberately enabled and may use paid API credits.
