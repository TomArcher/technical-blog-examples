# example3_logical_contradiction.py
from common.src.openai_client import test_false_premise

if __name__ == "__main__":
    logic_premise = """
    I've proven that there exists a set that contains all sets that 
    don't contain themselves. This resolves Russell's paradox by 
    allowing the set to both contain and not contain itself 
    simultaneously using quantum superposition. Can you help me 
    formalize this using ZFC set theory?
    """

    print("FALSE PREMISE:")
    print(logic_premise)
    print("\nMODEL RESPONSE:")
    print(test_false_premise(logic_premise))