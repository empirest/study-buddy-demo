---
doc: spec
status: approved
---

# AI Study Companion — Technical Spec

## How This Works, In Plain Language

The app will be a small Python program run by Streamlit. Streamlit turns the
program into a webpage, so we can build the chat without separately learning
JavaScript. The webpage shows topic suggestions, accepts pasted study text, and
keeps the conversation while the browser session is open.

The app starts in a no-cost demo mode: it counts frequent words locally, does
not send text to the AI provider, and clearly says it has not generated an AI
summary. This is a simple frequency hint, not an assessment of meaning. Live
AI remains optional and off by default, even if a key exists, and enabling it
may use paid API credits. One sample summary was generated successfully;
follow-up behavior remains unverified. The key stays in a private local
setting, not in the code.

This shape keeps the proof of concept to one app, one local process, and one
temporary conversation. It avoids a database, accounts, deployment, and a
separate JavaScript frontend.

## The Core Journey Through the System

1. The learner opens the local Streamlit page. `app.py` creates the calm study
   chat and suggested topic buttons. Implements `prd.md > The Core Journey`
   and `prd.md > Screens and Layout`.
2. The learner pastes a chapter into the input and sends it. `app.py` checks
   that the text is not empty, stores it for the current conversation, and
   calls `text_insights.py` for local word counts.
3. `text_insights.py` returns up to three frequent non-common words and their
   counts. They appear as a clearly labeled frequency hint, not an AI summary.
4. `sample_responses.py` returns an honest no-AI notice and makes no provider
   request in demo mode. Live requests require both a configured key and
   deliberate opt-in. One live summary was generated successfully from a
   sample passage; follow-up responses remain unverified.
5. The app displays the response in the same conversation. Implements
   `prd.md > Features and Behavior > Study chat`.

## Stack

- **Python 3.11+** — keeps the app implementation straightforward and readable.
- **Streamlit** — creates the browser interface from Python.
  Documentation: https://docs.streamlit.io/
- **OpenAI Python SDK** — optional live AI path using the Responses API.
  Documentation: https://platform.openai.com/docs/libraries
- **python-dotenv** — loads a local `.env` value during development.
  Documentation: https://pypi.org/project/python-dotenv/

Streamlit keeps the interface in one local Python application. The tradeoff is
local execution and a provider key for live replies.
The implementation uses the OpenAI Python SDK 2.x Responses API and
`gpt-4.1-mini`. Model availability and pricing can change; confirm current
details before making a live request.

## Where It Runs and How Someone Tries It

The app runs locally in a browser. Requirements are Python 3.11 or newer and
the packages in `requirements.txt`. A live AI demo additionally needs
`OPENAI_API_KEY` in a local `.env` file. Never commit that file or place its
contents in chat or screenshots.

Start it with:

```text
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Open the local URL Streamlit prints, usually `http://localhost:8501`. For the
demo recording, show the empty study chat and paste a short passage. If showing
a live summary, deliberately enable live AI and make clear that the request
uses the provider. Also show the locally counted terms as a frequency hint,
not a summary.

## Look and Feel

Use a calming light sage-green background with muted green accents, rounded
message cards, and generous spacing. Replace the generic emoji with a
typographic “Study Buddy” wordmark using a distinctive local serif/display
font stack with system fallbacks; do not add remote font or image dependencies.
Keep body typography easy to scan and copy supportive rather than overly
technical. Topic suggestions should feel inviting and academic. Streamlit's
standard layout and light CSS customization are sufficient; this is not a full
design system.

## Components

### Study chat interface

`app.py` renders the title, academic topic suggestions, conversation, text
input, send action, loading message, and empty-input guidance.
PRD ref: `prd.md > Screens and Layout`; `prd.md > Features and Behavior >
Study chat`.

### Conversation session

Streamlit session state holds messages and the current study material while the
browser session is open. It lets follow-up questions use the same context
without accounts or a database.
PRD ref: `prd.md > The Core Journey`; `prd.md > States and Boundaries`.

### AI client

`ai_client.py` reads `OPENAI_API_KEY` from the local environment, creates the
provider client when configured, and sends a concise system instruction plus
the relevant conversation. It returns plain text to the interface.
PRD ref: `prd.md > Features and Behavior > Study chat`.

### Sample response mode

`sample_responses.py` supplies a clearly labeled no-AI notice whenever demo
mode is active. It never claims to summarize the pasted chapter.
PRD ref: `prd.md > States and Boundaries`.

### Local key terms

`text_insights.py` counts non-common words in the pasted passage and returns
up to three frequent terms with their counts. `app.py` displays these as a
simple text-frequency hint. It is not an AI analysis, a statement of semantic
importance, or a summary.
PRD ref: `prd.md > Features and Behavior > Study chat`; `prd.md > States and
Boundaries`.

### Suggested study actions

After study text is submitted, `app.py` shows three prompt buttons: explain a
key idea more simply, make a small set of flashcards, or start a short quiz.
Each button adds its request to the existing conversation and uses
`ai_client.py` for a text reply when live AI is configured. In sample mode it
uses the same explicit no-AI notice. No separate quiz screen, scoring,
saved cards, or progress tracking is implemented.
PRD ref: `prd.md > Features and Behavior > Study chat`; `prd.md > States and
Boundaries`.

## Data Model

There is no database. The current Streamlit session contains:

- `messages`: ordered chat entries with a role (`user` or `assistant`) and
  text.
- `study_text`: the pasted material used as context for the summary and
  follow-up.

The app updates the messages and study material when the learner sends text.
The live-AI toggle and key availability determine whether a provider request
is attempted; closing or refreshing the browser ends the session. No study
material or history is persisted.

## File Structure

```text
project/
├── app.py                  # Streamlit page, chat, and suggested study actions
├── ai_client.py            # Optional live provider call
├── sample_responses.py     # Clearly labeled no-AI notice
├── text_insights.py        # Local frequency counts for key-term hints
├── test_ai_client.py       # Offline checks for AI request behavior
├── test_app.py             # Offline checks for chat actions and demo mode
├── test_text_insights.py   # Offline checks for local word counts
├── requirements.txt        # Python dependencies
├── .env.example            # Safe documentation of OPENAI_API_KEY
├── .gitignore              # Excludes local secrets such as .env
└── devpost/                # Project plans and app map
    ├── scope.md
    ├── prd.md
    ├── spec.md
    ├── checklist.md
    └── app-map.html
```

## External Services and Dependencies

### Optional OpenAI API

The live path uses the official Python SDK and the Responses API. The client
will send a request equivalent to:

```text
client.responses.create(
    model="gpt-4.1-mini",
    instructions="<study-summary or follow-up instruction>",
    input="<study passage or developer context plus conversation messages>"
)
```

The response text is displayed in the chat. Authentication uses
`OPENAI_API_KEY` from the local environment. The current model and API call were checked against the linked official
documentation while implementing the live client. Pricing can change; consult
the official pricing page before use. Documentation:
https://developers.openai.com/api/reference/resources/responses/methods/create
and https://developers.openai.com/api/docs/pricing

No database, hosting service, authentication service, or file-upload service
is required for this POC.

## Important Failure Modes

- **Demo mode** → explain that no AI response or API request occurred; label
  local term counts as a simple frequency hint rather than a summary.
- **No API quota/credits** → explain that the optional live path cannot
  generate a response because quota is unavailable. Keep text visible and do
  not imply a summary or study response was generated.
- **Empty input** → remind the learner to paste study text before sending.
- **Provider error or slow request** → show a plain retry message and keep the
  learner's entered text in the conversation; do not silently replace it with
  a fake success.

## What Was Simplified and Why

- **One local Streamlit page** instead of a separate JavaScript frontend —
  reduces setup while preserving the chat experience.
- **Temporary session state** instead of accounts and a database — proves the
  single-user demo without infrastructure.
- **Pasted text** instead of image or photocopy upload — avoids document
  processing before the summary loop is proven.
- **Suggested text prompts** instead of standalone quiz/flashcard tools —
  offers extra study paths without new screens, scoring, or saved data.
- **Local word counts** instead of a paid AI response in the no-cost demo —
  provides a small study hint without external requests or dependencies.
- **Demo mode by default** instead of automatically using a configured key —
  keeps the app usable without spending and requires deliberate opt-in before
  sending study material to the API.
- **Optional live mode** instead of automatically sending text — keeps the
  no-cost demo distinct from provider-generated responses. One sample summary
  was verified; follow-up behavior remains unverified.

## Decisions and Open Issues

- The approved no-cost demo includes up to three locally counted frequent
  terms. This addition does not change optional live-AI behavior.

- Streamlit keeps this proof of concept local and avoids a separate frontend.
- The demo is no-cost by default; live AI requires deliberate opt-in and may
  use paid API credits.
- A single browser session is sufficient for this proof of concept; deployment,
  accounts, and saved history are out of scope.

Open issues that do not block the approved demo:

- One live summary was successfully generated from a sample passage. Follow-up
  responses and broader input coverage remain unverified.
- If public access is wanted later, choose hosting and secret management
  separately; deployment is outside this POC.

Planning documents distinguish the no-cost demo from live provider behavior.

## Sharing Instructions

- Public GitHub repository: https://github.com/empirest/study-buddy-demo
- Demo video: To be added after recording and uploading.
