"""Voice-driven loop around the agent (say 'stop' to exit)."""

from agent import run_agent
from config import ACTION_PREFIX
from voice import listen, speak


def main():
    print("🎧 Voice Agent Started (Say 'stop' to exit)")

    while True:
        query = listen()
        if not query:
            continue

        if "stop" in query.lower():
            speak("Goodbye")
            break

        response = run_agent(query)
        print("Agent:", response)

        if response.startswith(ACTION_PREFIX):
            speak("Executing action")
        else:
            speak(response)


if __name__ == "__main__":
    main()
