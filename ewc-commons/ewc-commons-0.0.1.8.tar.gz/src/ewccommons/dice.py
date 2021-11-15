"""EWC Commons Dice

Define a Dice object capable of generating a random number from.
Define a DiceShaker contain capable of rolling multiple Dice instances.

Can be used/invoked as a module, why? because print is a valid debug tool!
"""
# Import the typing library so variables can be type cast
from typing import List, Optional, Tuple

# Import the sys to get any argv used
import sys

# Allow the copying of the dice objects to allow for multiple independant roll values
from copy import copy

# Import the random library
import random

# Import the Sophie ValueError generator
from ewccommons.sophie import not_what_i_wanted

_Die_Faces_ = List[int]
"""Type Alias Definition

A die face values list variable structure.
"""

# Define the dice cup list variable type
_Dice_Cup_ = List[_Die_Faces_]
"""Type Alias Definition

A list collection of die face values list variable structure.
"""


def roll_die(_die: _Die_Faces_) -> int:
    """
    Randomly choose a number from the x sided die face values.

    :param _die: (_Die_Faces_) The list of die face side values.
    :return: A randomly chosen integer value from the die faces list.
    """
    return random.choice(_die)


class Dice:
    """
    Define a Dice object instance.

    Simulate rolling dice by randomly chosing a die face value.
    """

    def __init__(self, sides: int, name: str = None, val: int = None) -> None:
        """Initialize the Dice object

        Set the dice name, the face values list & a starting face value.

        :param sides: The number of face sides for the dice instance.
        :param name: An optional string name for the dice instance.
        :param val: An optional starting rolled value for the dice instance.
        """
        # Verify the supplied sides data type is what we expect
        if not isinstance(sides, int):
            raise not_what_i_wanted(
                "Invalid value type supplied for Dice sides.", int, sides
            )
        # Verify that the die will have at least 2 options
        if sides < 2:
            raise ValueError(
                "Number of sides for a valid die needs to be greater than 2."
            )
        # Check if we need to generate a dice name
        if name is None:
            # Genrate the Dn dice name string
            name = f"D{str(sides)}"
        # Create the die face values from 1 to sides +1 because range end is exclusive
        face_values: _Die_Faces_ = [*range(1, sides + 1)]
        # Check if an initial die face value is set
        if val is None:
            # Generate a random starting face value
            val = roll_die(face_values)
        # Verify the supplied val data type is what we expect
        if not isinstance(val, int):
            raise not_what_i_wanted(
                "Invalid value type supplied for Dice val.", int, val
            )
        # Make sure the initial die face value is actually within the values on the die
        if val < min(face_values) or val > max(face_values):
            raise ValueError("Dice initial value out of bounds.")
        # Set the die instance name
        self.__name: str = name
        # Set the list of die face values
        self.__face_values: _Die_Faces_ = face_values
        # Set the initial starting face value of the die
        self.__rolled: int = val

    @property
    def name(self) -> str:
        """
        Get the name of the die.

        :return: The dice instance name.
        """
        return self.__name

    @property
    def faces(self) -> _Die_Faces_:
        """
        Get the list of face values for the die.

        :return: The list of the dice instance face values.
        """
        return self.__face_values

    @property
    def rolled(self) -> int:
        """
        Get the rolled face value of the die.

        :return: The current rolled value of the dice instance.
        """
        return self.__rolled

    def roll(self) -> int:
        """
        Simulate rolling the die.

        :return: The rolled value of the dice instance.
        """
        # Roll the die faces & set the value as the internal rolled value
        roll: int = roll_die(self.faces)
        self.__rolled = roll
        return self.rolled

    def __copy__(self):
        """
        Create a copy of the dice object.

        :return: A cloned copy of the dice instance.
        """
        return __class__(sides=len(self), name=self.__name, val=self.__rolled)

    def __repr__(self) -> str:
        """
        Get a string to represent recreating this object.

        :return: A string representation capable of creating the dice instance.
        """
        return f"{__class__}(sides={len(self)},name={self.__name},val={self.__rolled})"

    def __str__(self) -> str:
        """
        Get the object as a human readable string.

        :return: A Human readable string version of the dice instance.
        """
        return f"{self.name} : {self.rolled}"

    def __len__(self) -> int:
        """
        Return the number of faces the die has.

        :return: The number of face sides the dice instance has.
        """
        return len(self.__face_values)

    def __eq__(self, o: object) -> bool:
        """
        Check to see if the dice roll is equal to the operand.

        :param o: The operand being compared with.
        :return: True when compared to the dice instance rolled value is True.
        """
        return self.__rolled == o

    def __ne__(self, o: object) -> bool:
        """
        Check to see if the dice roll is not equal to the operand.

        :param o: The operand being compared with.
        :return: True when compared to the dice instance rolled value is True.
        """
        return self.__rolled != o

    def __lt__(self, o: object) -> bool:
        """
        Check to see if the dice roll is less than the operand.

        :param o: The operand being compared with.
        :return: True when compared to the dice instance rolled value is True.
        """
        return self.__rolled < o

    def __gt__(self, o: object) -> bool:
        """
        Check to see if the dice roll is greater than the operand.

        :param o: The operand being compared with.
        :return: True when compared to the dice instance rolled value is True.
        """
        return self.__rolled > o

    def __le__(self, o: object) -> bool:
        """
        Check to see if the dice roll is less than the operand.

        :param o: The operand being compared with.
        :return: True when compared to the dice instance rolled value is True.
        """
        return self.__rolled <= o

    def __ge__(self, o: object) -> bool:
        """
        Check to see if the dice roll is greater than the operand.

        :param o: The operand being compared with.
        :return: True when compared to the dice instance rolled value is True.
        """
        return self.__rolled >= o


_Dice_ = List[Dice]
"""Type Alias Definition

A list collection of Dice instances variable structure.
"""


class DiceShaker:
    """
    Class to manage rolling multiple dice.
    """

    def __init__(self, _dice: Optional[_Dice_] = None) -> None:
        """Initialize the DiceShaker object

        Setup the empty DiceShaker and add any optional starting dice.

        :param _dice: An optional list of existing dice instances.
        """
        # Define the instance properties used, list of dice,
        # current roll total, current min & max roll values
        self.__dice: _Dice_ = list()
        self.__total: int = 0
        self.__min: int = 0
        self.__max: int = 0
        # Check if any dice were supplied at creation
        if _dice is not None:
            # Use the supplied list of dice to populate the shaker
            self.populate(_dice)

    def populate(self, _dice: _Dice_) -> None:
        """
        Add a subset list of dice to the shaker.

        :param _dice: A list of existing dice instances.
        """
        for _die in _dice:
            self.add(_die)

    def add(self, _die: Dice, amount: int = 1) -> None:
        """
        Add a die to dice shaker.

        :param _die: The dice instance to add to the shaker.
        :param amount: The number of dice instance copies to add.
        """
        # Make sure we are adding a positive number
        if amount < 1:
            raise ValueError("Can't add negative number of die to shaker.")
        # I love list comprehension
        # Add a copy of the die to the list to allow for independant roll values
        new_dice: _Dice_ = [copy(_die) for _ in range(1, amount + 1)]
        # Adding the new dice list to existing dice list because thats python
        self.__dice += new_dice
        # Increment the sum total of dice rolls value
        self.__total += sum([_die.rolled for _die in new_dice])
        # Increment the current minimum/maximum roll value by the minimum/maximum
        # roll value of die added
        self.__min += min(_die.faces) * amount
        self.__max += max(_die.faces) * amount

    @property
    def min_roll(self) -> int:
        """
        Return the minimum value the shaker can roll.

        :return: The minimum combined roll value the shaker can roll.
        """
        return self.__min

    @property
    def max_roll(self) -> int:
        """
        Return the maximum value the shaker can roll.

        :return: The maximum combined roll value the shaker can roll.
        """
        return self.__max

    @property
    def roll_total(self) -> int:
        """
        Return the total of the dice rolled.

        :return: The total combined rolled dice value.
        """
        return self.__total

    def empty_shaker(self) -> None:
        """
        Remove any dice from the shaker list.
        """
        self.__dice = list()
        self.__total = 0
        self.__min = 0
        self.__max = 0

    def shake(self) -> None:
        """
        Shake/roll the dice in the shaker.
        """
        # Reset the rolled value
        self.__total = 0
        # Roll the die
        for _die in self.__dice:
            # Add the rolled value to the total
            self.__total += _die.roll()

    def roll(self) -> Tuple[int, Tuple]:
        """
        Shake & roll the dice to get the results.

        :return: A tuple of the roll total and the individual dice rolls.
        """
        # Make sure the dice have been shaken
        self.shake()
        # I really love list comprehension lol
        # Get a list of the rolled dice values
        rolled: List = [_die.rolled for _die in self.__dice]
        # Return it as tuple so it's immutable
        return self.roll_total, tuple(rolled)

    def __copy__(self):
        """
        Create a copy of the dice object.

        :return: A cloned copy of the dice shaker instance.
        """
        return DiceShaker(self.__dice.copy())

    def __repr__(self) -> str:
        """
        Get a string to represent recreating this object.

        :return: A string representation capable of creating the shaker instance.
        """
        return f"{__class__}({repr(self.__dice)})"

    def __str__(self) -> str:
        """
        Get the object as a human readable string.

        :return: A Human readable string version of the dice shaker instance.
        """
        # TODO work out how to collect the rolled values to add the strings
        return "\n".join(
            [
                f"Rolled : {len(self)} Dice",
                f"Minimum : {self.min_roll}",
                f"Maximum : {self.max_roll}",
                "\n".join([str(d) for d in self.__dice]),
                f"Total : {self.roll_total}",
            ]
        )

    def __len__(self) -> int:
        """
        Return the number of dice.
        """
        return len(self.__dice)

    def __getitem__(self, position) -> Dice:
        """
        Get a specific die from the shaker.

        :param position: The index position to get the dice instance from.
        :return: The dice instance.
        """
        return self.__dice[position]

    def __eq__(self, o: object) -> bool:
        """
        Check to see if the dice roll total is equal to the operand.
        """
        return self.__total == o

    def __ne__(self, o: object) -> bool:
        """
        Check to see if the dice roll total is not equal to the operand.
        """
        return self.__total != o

    def __lt__(self, o: object) -> bool:
        """
        Check to see if the dice roll total is less than the operand.
        """
        return self.__total < o

    def __gt__(self, o: object) -> bool:
        """
        Check to see if the dice roll total is greater than the operand.
        """
        return self.__total > o

    def __le__(self, o: object) -> bool:
        """
        Check to see if the dice roll total is less than the operand.
        """
        return self.__total <= o

    def __ge__(self, o: object) -> bool:
        """
        Check to see if the dice roll total is greater than the operand.
        """
        return self.__total >= o


def check_output(*args) -> None:
    """Debug/Test function

    Checkout the output of the module.
    """
    print("Args", *args, "Args", sep="\n")
    die_sides = 15
    d: Dice = Dice(die_sides)
    print(f"Dice(D{die_sides})", d, d < die_sides, d > 0, sep="\n")
    print("Rolls...", d.roll())
    shaker: DiceShaker = DiceShaker([copy(d), copy(d), copy(d)])
    print("New Shaker", shaker, sep="\n")
    shaker.add(d, 2)
    print("Add Dice", shaker, sep="\n")
    shaker.shake()
    print("Shake Dice", shaker, sep="\n")
    print("Roll Shaker", shaker.roll(), shaker, sep="\n")
    shaker.empty_shaker()
    print("Empty Shaker", shaker, sep="\n")
    print("New Shaker Roll", DiceShaker([copy(d), copy(d), copy(d)]).roll(), sep="\n")


def main() -> None:
    """Main function

    Run as a module and convert any CLI arguments to lowercase.
    """
    # Call the main function with any command line arguments after the module name
    check_output(*[str(_).lower() for _ in sys.argv[1:]])


# Make sure the script is being called as a script & not being imported into
# another module file
if __name__ == "__main__":
    # Call the main function
    main()
