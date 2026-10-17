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
3. The app locally counts frequent non-common words and shows up to three with
   their counts. This is a basic text-frequency hint, not a summary or AI
   analysis.
4. The app says no AI request was sent. Explanation, flashcard, and short-quiz
   prompts remain visible; choosing one receives an honest notice rather than
   AI-generated content.
5. With live AI deliberately enabled, the app can generate a concise summary.
   One sample summary was verified; follow-up behavior remains unverified.

Source: `scope.md > The Core Loop`, `scope.md > What "Working" Looks Like`.

## Screens and Layout

The proof of concept uses one main screen:

- A study-chat area is the central surface.
- A small set of suggested academic topics appears near the starting chat so
  the learner has a clear way to begin.
- A text input and send action let the learner paste material or ask a
  follow-up question.
- The demo notice and a local key-terms panel appear on the same screen; a
  future live summary should be easy to distinguish and read.
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
- After submission, the app shows up to three frequently used non-common
  words from the first study passage, each with its count.
- This local frequency hint does not use an AI provider and does not identify
  the passage's key ideas or replace a summary.
- With live AI deliberately enabled, the app generates a concise summary of
  supplied material. This was manually verified with one sample passage.
- The learner can submit follow-up questions in the same conversation, but
  live follow-up responses have not been verified.
- The app displays topic suggestions before the first message to make the
  starting point obvious.
- After study material has been submitted, the chat offers three quick prompts:
  explain a key idea more simply, make a small set of flashcards, or start a
  short quiz. These buttons remain visible in demo mode, where choosing one
produces only an honest no-AI notice; an AI text reply is intended
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
- **Demo input** — Nonempty text is accepted. The app counts frequent words
  locally; it does not send the text to an AI provider or assess its meaning.
- **No frequent terms** — If no non-common words are found, show a clear
  message instead of an empty term panel.
- **Live summary** — One summary was successfully generated from a sample
  passage. This does not validate every input or guarantee correctness.
- **Live follow-up** — Follow-up requests can be sent in the same conversation,
  but successful responses have not been verified.
- **Demo success** — The study-chat interface, local word-frequency hints,
  and prompt choices are visible; the app clearly distinguishes these from an
  AI-generated summary.
- **Live AI** — Live mode is optional and may incur charges. Demo mode does not
  send study text to an AI provider.
- **Demo mode** — Live AI is off by default. The app explains that no AI
  request is sent; word-frequency hints are computed locally. Enabling live
  AI is a deliberate opt-in that may incur charges.
- **Persistence** — No saved accounts or cross-session study history is
  required for the proof of concept.

## Product Decisions

- The first screen is a study chat with academic suggestions — it gives the
  learner a clear starting point without expanding the core loop.
- The interface preview is the proof of this no-cost demo — it must not be
  mistaken for an AI-generated summary.
- The local term-frequency hint is a small, no-cost study aid — label it
  honestly and do not call it an AI insight or summary.
- The intended live follow-up stays in the same conversation — this keeps the
  future experience simple and lets the learner raise concerns naturally.
- The visual mood is calm, colorful, and playful — the learner wants the app
  to be engaging while still suitable for studying.
- Suggested explanation, flashcard, and short-quiz prompts stay in the same
  chat — this offers study choices without building interactive tools or
  separate screens.
- The refreshed look uses a soft sage palette and a typographic wordmark — it
  should feel calming and less generic without depending on downloaded assets.
- The initial input is pasted text — this keeps the POC focused; clear-image
  upload guidance is acknowledged but image processing is deferred.
- Live AI is explicitly off by default and labeled as potentially using paid
  API credits — the no-cost demo remains usable without sending study text to
  a provider.
- The no-cost demo and optional live summary are clearly distinguished — the
  app must not imply that AI generated content when demo mode is active.

## What We're Building

- One main study-chat screen.
- A small set of academic topic suggestions in the empty state.
- Pasted chapter or passage input.
- An honest no-AI notice, instead of a fabricated summary or answer.
- Up to three locally counted frequent terms, clearly described as a simple
  frequency hint rather than a summary.
- Three post-material study prompt buttons; selecting one in demo mode says
  that no AI request was sent.
- An optional live-AI path; one sample summary was verified, while follow-up
  responses are not required for this demo and remain unverified.
- Empty and unusable-input guidance.
- Calm sage-green styling and a distinctive typographic wordmark.
- A no-cost demo mode by default; live AI requires deliberate opt-in.

## Deferred From the POC

- Image or photocopy upload processing — it adds document-processing
  complexity before pasted-text summarization is proven.
- Saved accounts, study history, or cross-session persistence — not needed for
  a one-session demo.

## Possible Later Enhancements

- Testing summaries against more study materials and verifying live contextual
  follow-up responses.
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

- Verify live follow-up responses and broader summary behavior before
  describing those capabilities as fully validated.
