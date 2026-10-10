"""Simple bounded conversation memory shared by the agent."""

from config import MAX_MEMORY


class ConversationMemory:
    """Keeps only the most recent ``MAX_MEMORY`` messages."""

    def __init__(self, limit=MAX_MEMORY):
        self.limit = limit
        self._messages = []

    def add(self, role, content):
        self._messages.append({"role": role, "content": content})
        if len(self._messages) > self.limit:
            self._messages.pop(0)

    def get(self):
        return list(self._messages)

    def clear(self):
        self._messages.clear()

    def as_context(self):
        """Render the stored messages as a plain-text dialogue context."""
        return "\n".join(f'{msg["role"]}: {msg["content"]}' for msg in self._messages)


# Module-level default instance, kept for backwards compatibility.
_default_memory = ConversationMemory()


def add(role, content):
    _default_memory.add(role, content)


def get():
    return _default_memory.get()


def as_context():
    return _default_memory.as_context()


def clear():
    _default_memory.clear()
