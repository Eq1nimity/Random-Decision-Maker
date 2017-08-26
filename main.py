from random import randint
from time import sleep

def main():
    n = _get_option_count()
    inputs = _get_inputs(n)
    choice = _random_option_chooser(n, inputs)
    return choice


def _get_option_count():
    """
    Prompt user how many options they would like to determine from (as int).

    :return: int determining option count.
    """
    try:
        print("Hello, I am the oracle of fate. The deliverer of destiny. I have a few questions for you... \n ")
        option = int(input("How many options do you have? (Input answer as nonzero integer) \n"))
        print("\nThat's {} options? Got it! Now let's see...".format(option))
        return option
    except:
        print(" Unanticipated Problem get_option_count(). Try again? ")


def _get_inputs(n):
    """
    Prompt user n times. For each of their inputs, add to python list.

    :param n: option count  / output of get_option_count()
    :return: list of strings containing options.
    """
    options = []
    counter = 1
    try:
        for option in range(n):
            options.append(str(input("\nWhat is option {}?\n".format(counter))))
            counter += 1
        return options
    except:
        print("Unanticipated Problem with get_inputs(). Try again?")


def _random_option_chooser(n, inputs):
    """
    Chooses a random option from the list of inputs via method of randint and python list index functionality.

    :param n: option count / output of get_option_count()
    :param inputs: list of strings / output of get_option_count()
    :return: a string containing the random choice.
    """
    random_option = randint(0, n-1)
    destiny = inputs[random_option]
    print("\nCalling Upon the Gods of Chance!!\n")
    sleep(1)
    print("THE GODS HAVE DETERMINED, PROCEED WITH: \n {}".format(destiny))
2
if __name__ == "__main__":
    main()
