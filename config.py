"""Central configuration for the AI agent browser backend."""

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi"

# Number of conversation turns kept in memory.
MAX_MEMORY = 6

# Flask server settings.
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000

# Text-to-speech settings.
TTS_RATE = 160

# Prefix used by the agent to signal that a URL should be opened,
# in the format ACTION:OPEN_URL:<full_url>.
ACTION_PREFIX = "ACTION:OPEN_URL:"
