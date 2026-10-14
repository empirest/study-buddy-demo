---
doc: scope
status: approved
---

# AI Study Companion

An AI-driven study app concept that turns a pasted chapter into a concise
summary and suggests ways to study it further. For this hackathon, the
completed artifact is a small, no-cost interface demo; it does not claim to
analyze the learner's text.

## The Unique Kernel

The intended product kernel is a focused study conversation grounded in the
learner's material, rather than a blank chatbot. This no-cost demo shows that
conversation's interface but does not generate the summary.

## Who It's For

Anyone preparing for an exam who has a chapter or other study material to
understand. The first demo will use one learner pasting one chapter into the
app; the longer-term audience includes school and college students and other
exam takers.

## The Core Loop

In the intended product, the learner opens the study chat, pastes a chapter,
reads a concise summary, and asks a follow-up or chooses a suggested way to
study it further. In this demo, they can try the interface and see an honest
notice instead of generated content.

## Inspiration & Identity

The app should feel focused, approachable, and academic rather than like a
generic open-ended chatbot. Use a calming light sage-green atmosphere and a
distinctive typographic wordmark. The first screen includes a few suggested
academic topics.

## Design Goal

Make studying easier with an approachable interface and a small, working
proof of concept.

## What "Working" Looks Like

A learner can open the app, paste a chapter, and see the app clearly explain
that demo mode has not analyzed the text. The interface demonstrates where a
summary and follow-up or explanation, flashcard, and short-quiz prompts would
appear. Live AI output is deliberately outside this hackathon's completed
demo because using the provider requires available API credits.

## The POC Boundary

In scope:

- A simple study-chat interface.
- A few suggested academic topics before the first message.
- Pasting one chapter or text passage.
- Showing where the intended summary and follow-up would appear, without
  claiming demo mode analyzed the text.
- Showing suggested chat prompts to explain a key idea, make flashcards, or
  start a short quiz. Demo-mode replies explicitly state that no AI request was
  sent.
- A no-cost demo mode is the default; live AI is optional and requires a
  deliberate opt-in that may use paid API credits.
- Live summary and follow-up generation are not verified or represented as
  working in this demo.
- A straightforward demo using one study session.

## Later

- Interactive quizzes, scored practice tests, and saved or flip-through
  flashcards; the first version only offers text responses in the chat.
- Hints and selectable difficulty levels.
- Uploading photocopies or other files.
- Support for many subjects, chapters, and study sessions.

## Explicitly Cut

- Separate quiz, flashcard, and difficulty systems: suggested chat prompts
  demonstrate the study-help options without introducing separate screens,
  scoring, card controls, or progress tracking.
- File and photocopy uploads: they add document-processing complexity before
  the core chat behavior is demonstrated.
- A complete exam-preparation platform: too broad for a 2–4 hour proof of
  concept.
