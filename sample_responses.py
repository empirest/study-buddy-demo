"""Transparent placeholder replies for trying the study-chat interface."""


def preview_notice() -> str:
    return (
        "**Sample mode:** I received your text, but I have not analyzed it. "
        "Configure `OPENAI_API_KEY` locally to enable real AI summaries and "
        "study help. No AI request was sent."
    )
