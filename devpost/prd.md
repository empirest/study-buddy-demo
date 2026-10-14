---
doc: prd
status: approved
---

# AI Study Companion — Product Requirements

An approachable AI study chat for anyone preparing for an exam.
Source: `scope.md > The Unique Kernel`, `scope.md > Who It's For`.

## The Core Journey

1. The learner opens the app and sees a calm, sage-green study chat with a few
   academic topic suggestions, such as geometry or biology.
2. The learner pastes a chapter or other study passage into the chat.
3. In this hackathon's no-cost demo, the app says clearly that it has not
   analyzed the text; it does not fabricate a summary.
4. The learner can see where an explanation, flashcard, or short-quiz prompt
   would be offered. In demo mode, choosing one also receives an honest notice
   that no AI request was made.
5. A live summary and grounded follow-up are the intended future behavior, but
   remain unverified and outside this approved demo.

Source: `scope.md > The Core Loop`, `scope.md > What "Working" Looks Like`.

## Screens and Layout

The proof of concept uses one main screen:

- A study-chat area is the central surface.
- A small set of suggested academic topics appears near the starting chat so
  the learner has a clear way to begin.
- A text input and send action let the learner paste material or ask a
  follow-up question.
- The demo notice appears in the same conversation; a future live summary
  should be easy to distinguish and read.
- After material has been submitted, three study-action buttons appear below
  the chat: **Explain more**, **Make flashcards**, and **Start a short quiz**.

No separate quiz, flashcard, or account screens are part of this version.

## Look and Feel

The learner wants a calming light green/sage atmosphere with a playful but
friendly study feel. Replace the generic emoji mark with a distinctive
typographic “Study Buddy” wordmark in a characterful local font stack, rather
than adding a remote font or image asset.

## Features and Behavior

### Study chat

- The learner can paste a chapter or passage into the chat input.
- The intended live behavior is a short, concise summary of the supplied
  material. Demo mode does not claim to provide this behavior.
- In intended live use, the learner can continue the same conversation with
  follow-up questions or concerns; this behavior is not verified in demo mode.
- The app displays topic suggestions before the first message to make the
  starting point obvious.
- After study material has been submitted, the chat offers three quick prompts:
  explain a key idea more simply, make a small set of flashcards, or start a
  short quiz. These buttons remain visible in demo mode, where choosing one
  produces only an honest no-analysis notice; an AI text reply is intended
  only for a future live session.
- These prompts do not create separate screens, saved cards, quiz scoring, or
  progress tracking. The learner may also type any follow-up question.
- For this approved demo, success means the interface is usable and clearly
  distinguishes its preview from generated study content.

## States and Boundaries

- **First use** — The empty chat shows the study purpose and topic suggestions
  before any material is entered.
- **Empty input** — The app reminds the learner to paste their text before
  sending.
- **Demo input** — Nonempty text is accepted as interface input; demo mode
  does not analyze or assess its usefulness. If image upload is offered later,
  it should remind the learner that images need to be clear.
- **Intended live use** — A summary and subsequent questions would remain
  visible in one conversation; this behavior is unverified.
- **Demo success** — The study-chat interface and prompt choices are visible,
  and the learner is clearly told that demo mode has not analyzed the text.
- **Live AI unverified** — This no-cost demo does not promise a real summary or
  contextual follow-up; live responses were not verified.
- **Demo mode** — Live AI is off by default. The app explains that study
  material and suggested prompts are not analyzed and no API request is sent.
  Enabling live AI is a deliberate opt-in that may incur charges.
- **Persistence** — No saved accounts or cross-session study history is
  required for the proof of concept.

## Product Decisions

- The first screen is a study chat with academic suggestions — it gives the
  learner a clear starting point without expanding the core loop.
- The interface preview is the proof of this no-cost demo — it must not be
  mistaken for an AI-generated summary.
- The intended live follow-up stays in the same conversation — this keeps the
  future experience simple and lets the learner raise concerns naturally.
- The visual mood is calm, colorful, and playful — the app should be engaging
  while still suitable for studying.
- Suggested explanation, flashcard, and short-quiz prompts stay in the same
  chat — this offers study choices without building interactive tools or
  separate screens.
- The refreshed look uses a soft sage palette and a typographic wordmark — it
  should feel calming and less generic without depending on downloaded assets.
- The initial input is pasted text — this keeps the POC achievable for a
  beginner; clear-image upload guidance is acknowledged but image processing
  is deferred.
- Live AI is explicitly off by default and labeled as potentially using paid
  API credits. The no-cost interface demo must not imply that summaries or
  study materials were generated.

## What We're Building

- One main study-chat screen.
- A small set of academic topic suggestions in the empty state.
- Pasted chapter or passage input.
- An honest no-analysis demo notice, instead of a fabricated summary or answer.
- Three post-material study prompt buttons; selecting one in demo mode says
  that no AI request was sent.
- An optional live-AI path that is not verified or required for this demo.
- Empty and unusable-input guidance.
- Calm sage-green styling and a distinctive typographic wordmark.
- A no-cost demo mode by default; live AI requires deliberate opt-in.

## Deferred From the POC

- Image or photocopy upload processing — it adds document-processing
  complexity before pasted-text summarization is proven.
- Saved accounts, study history, or cross-session persistence — not needed for
  a one-session demo.

## Possible Later Enhancements

- Real AI summaries and contextual answers, if available quota is later
  configured and live behavior is tested.
- Interactive/scored quizzes and practice tests, saved/flip-through flashcards,
  hints, and selectable difficulty levels.
- Clear-image upload and photocopy processing.
- More subject suggestions and support for many chapters or study sessions.

## Non-Goals

- A complete exam-preparation platform — too broad for the 2–4 hour
  proof-of-concept window.
- A full quiz, flashcard, or difficulty system — these are valuable extensions,
  but would distract from proving the summary-and-question loop.
- Replacing a teacher or guaranteeing academic correctness — the POC is a
  study aid, not an authority.

## Open Questions

- If the learner later opts into live AI when quota is available, verify the
  summary and contextual follow-up before describing them as working.
