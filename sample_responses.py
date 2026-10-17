"""Transparent placeholder replies for trying the study-chat interface."""


def preview_notice() -> str:
    return (
        "**Demo mode:** No AI response was generated and no API request was "
        "sent. The key terms above are simple local word counts, not an AI "
        "summary."
    )
