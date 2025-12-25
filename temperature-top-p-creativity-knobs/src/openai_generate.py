# openai_generate.py

from openai import OpenAI
import os

# Initialize client
openai_client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def openai_generate(prompt, temperature=1.0, top_p=1.0, n=5):
    """Generate n completions with OpenAI."""
    responses = []
    for _ in range(n):
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            top_p=top_p,
            max_tokens=50
        )
        responses.append(response.choices[0].message.content)
    return responses

def main():
    # Experiment: Same prompt, different temperatures
    prompt = (
        "Complete this sentence creatively: "
        "The robot looked at the sunset and felt"
    )

    print("=" * 60)
    print("TEMPERATURE EXPERIMENT (OpenAI)")
    print("=" * 60)

    for temp in [0.0, 0.5, 1.0, 1.5]:
        print(f"\nTemperature = {temp}")
        print("-" * 40)
        responses = openai_generate(prompt, temperature=temp, n=3)
        for i, r in enumerate(responses, 1):
            print(f"  {i}. {r[:70]}...")

if __name__ == "__main__":
    main()