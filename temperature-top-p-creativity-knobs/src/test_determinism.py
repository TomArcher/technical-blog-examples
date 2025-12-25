# test_determinism.py

from openai_generate import openai_generate

def test_determinism(prompt, n_trials=10):
    """Test whether temperature=0 produces identical outputs."""
    responses = openai_generate(prompt, temperature=0, n=n_trials)
    unique_responses = set(responses)

    print(f"Unique responses at T=0: {len(unique_responses)} / {n_trials}")

    if len(unique_responses) == 1:
        print("Deterministic behavior confirmed!")
        print(f"  Response: {responses[0][:80]}...")
    else:
        print("Non-determinism detected!")
        for r in unique_responses:
            print(f"  - {r[:60]}...")


if __name__ == "__main__":
    # Simple prompt - likely deterministic
    print("Test 1: Simple math question")
    print("-" * 40)
    test_determinism("What is 2 + 2?")

    # Longer, more creative prompt - more likely to show variation
    print("\nTest 2: Creative prompt (longer output)")
    print("-" * 40)
    test_determinism(
        "Write a paragraph about a robot discovering emotions.",
        n_trials=5
    )