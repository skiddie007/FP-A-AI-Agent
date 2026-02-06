import os
from dotenv import load_dotenv
from fp_a_agent import run_fp_a_agent

def main():
    load_dotenv()

    if not os.getenv("OPENAI_API_KEY"):
        print(
            "ERROR: OPENAI_API_KEY is not set.\n"
            "Create a .env file in this folder with:\n"
            "OPENAI_API_KEY=your_key_here"
        )
        return

    print("FP&A AI Agent \u2013 Windows Console App")
    print("-----------------------------------")

    audience = input(
        "Audience (CEO/Board/Finance Team/Operations/CFO) [default: CEO]: "
    ).strip() or "CEO"

    print("\nPaste your FP&A prompt (finish with an empty line):")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    prompt = "\n".join(lines).strip()

    if not prompt:
        print("No prompt entered. Exiting.")
        return

    print("\nRunning FP&A AI Agent... please wait.\n")
    try:
        response = run_fp_a_agent(prompt, audience=audience)
        print("\n===== FP&A AI Agent Response =====\n")
        print(response)
    except Exception as e:
        print(f"\nError running FP&A AI Agent: {e}")

if __name__ == "__main__":
    main()
