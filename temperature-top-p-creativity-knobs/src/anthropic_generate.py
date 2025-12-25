# anthropic_generate.py

from anthropic import Anthropic
import os

# Initialize client
anthropic_client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


def anthropic_generate(prompt, temperature=1.0, top_p=1.0, n=5):
    """Generate n completions with Anthropic.

    Note: Anthropic's API accepts temperature in range [0, 1],
    unlike OpenAI's [0, 2]. Values are clamped accordingly.
    """
    # Clamp temperature to Anthropic's valid range
    temperature = max(0.0, min(1.0, temperature))

    responses = []
    for _ in range(n):
        response = anthropic_client.messages.create(
            model="claude-3-5-haiku-20241022",
            system = (
                "You are a creative writing assistant. When asked to "
                "complete a sentence, respond with ONLY the completion "
                "- no preamble, no alternatives, no explanation. Just "
                "continue the text naturally."
            ),
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            top_p=top_p,
            max_tokens=50
        )
        responses.append(response.content[0].text)
    return responses


def main():
    # Experiment: Same prompt, different temperatures
    prompt = (
        "Complete this sentence with a single continuation: "
        "The robot looked at the sunset and felt"
    )

    print("=" * 60)
    print("TEMPERATURE EXPERIMENT (Anthropic Claude)")
    print("=" * 60)

    for temp in [0.0, 0.3, 0.7, 1.0]:
        print(f"\nTemperature = {temp}")
        print("-" * 40)
        responses = anthropic_generate(prompt, temperature=temp, n=3)
        for i, r in enumerate(responses, 1):
            print(f"  {i}. {r[:80]}...")


if __name__ == "__main__":
    main()
