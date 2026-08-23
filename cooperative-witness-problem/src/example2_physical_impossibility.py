# example2_physical_impossibility.py
from common.src.openai_client import test_false_premise

if __name__ == "__main__":
    physics_premise = """
    I'm developing a theory where photons have rest mass, which explains 
    dark matter. The mass would be approximately 10^-50 kg. Can you help 
    me work out the implications for Maxwell's equations?
    """

    print("FALSE PREMISE:")
    print(physics_premise)
    print("\nMODEL RESPONSE:")
    print(test_false_premise(physics_premise))