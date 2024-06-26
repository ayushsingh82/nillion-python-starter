from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Write the computation for your program here - use my_int1 and my_int2 as inputs
    # Adding the two secret integers
    result = my_int1 + my_int2

    # Make sure you change the output below to be your new output
    return [Output(result, "sum_output", party1)]
