"""Core agent: intent handling plus a local LLM (Ollama) fallback."""

import requests

import memory
from config import ACTION_PREFIX, MODEL_NAME, OLLAMA_URL
from prompt import SYSTEM_PROMPT
from sites import resolve_url


def handle_open_intent(user_input):
    """Handle "open <site>" commands locally, without hitting the model.

    Returns an ACTION string when the site is known, otherwise None.
    """
    text = user_input.lower().strip()
    if not text.startswith("open "):
        return None

    url = resolve_url(text[len("open "):])
    if url is None:
        return f"I don't know how to open {text[len('open '):].strip()}"
    return f"{ACTION_PREFIX}{url}"


def query_model():
    """Ask the local Ollama model, using conversation memory as context."""
    payload = {
        "model": MODEL_NAME,
        "prompt": f"{SYSTEM_PROMPT}\n{memory.as_context()}\nAgent:",
        "stream": False,
    }
    response = requests.post(OLLAMA_URL, json=payload, timeout=30)
    response.raise_for_status()
    return response.json().get("response", "").strip()


def run_agent(user_input):
    """Process a user message and return the agent's reply."""
    memory.add("User", user_input)

    action = handle_open_intent(user_input)
    if action is not None:
        # Only remember the action if it was understood; unknown sites
        # should not pollute the conversational context.
        if action.startswith(ACTION_PREFIX):
            memory.add("Agent", action)
        return action

    reply = query_model()
    memory.add("Agent", reply)
    return reply
