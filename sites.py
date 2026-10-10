"""Registry of known websites the agent can open."""

SITES = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "facebook": "https://www.facebook.com",
    "instagram": "https://www.instagram.com",
    "twitter": "https://www.twitter.com",
    "github": "https://www.github.com",
    "chatgpt": "https://chat.openai.com",
}


def resolve_url(name):
    """Return the URL for a site name, or None if it is unknown."""
    return SITES.get(name.lower().strip())
