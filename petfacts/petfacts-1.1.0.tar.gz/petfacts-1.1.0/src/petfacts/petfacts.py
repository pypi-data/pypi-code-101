#!/usr/bin/env python3
import argparse
import sys
import requests
import json
import random

"""
This is a simple little project to help me learn argparse, an argument parser like getopt but has a few advantages.
Hopefully those advantages will be clear soon.
"""

# Get a random cat fact and return it as a string
def cat_fact() -> str:
    rsession = requests.session()
    try:
        fact_json = rsession.get('https://catfact.ninja/fact')
        fact = json.loads(fact_json.text)
    except json.JSONDecodeError as err:
        print(f"Couldn't show the cat fact because {err}")
    except requests.HTTPError as err:
        print(f"Couldn't get the cat fact due to this HTTP error: {err}")

    return fact['fact']

# Get a random dog fact and return it as a string
def dog_fact() -> str:
    rsession = requests.session()
    try:
        fact_json = rsession.get('https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1')
        fact = json.loads(fact_json.text)
    except json.JSONDecodeError as err:
        print(f"Invalid repsonse recieved, got {err}")

    return fact[0]['fact']

# Choose a dog or cat string in an array and return it
def random_animal() -> str:
    animals = ['dog', 'cat']
    return animals[random.randrange(len(animals))]

def main():
    # According to https://docs.python.org/3/library/argparse.html
    # We create an instance of a class called ArgumentParser
    arg_parser = argparse.ArgumentParser(description='Get fun facts about pets!')

    # We can then add arguments from there with a function called add_argument()
    arg_parser.add_argument('--cat', action='store_true', default=False, help="Display a random cat fact.")
    arg_parser.add_argument('--dog', action='store_true', default=False, help="display a random dog fact.")

    # Try creating an argparse Namespace object or handle exception
    try:
        arg = arg_parser.parse_args()
    except argparse.ArgumentError as err:
        print(err)
        sys.exit(2)

    # We can use if elif to go through each arg and check if its been passed
    if arg.dog:
        print(f"Random Dog Fact: {dog_fact()}")
    elif arg.cat:
        print(f"Random Cat Fact: {cat_fact()}")
    else:
        # Print a random cat or dog fact if no args are passed
        if random_animal() == 'dog':
            print(f"Random Dog Fact: {dog_fact()}")
        else:
            print(f"Random Cat Fact: {cat_fact()}")


if __name__ == '__main__':
    main()