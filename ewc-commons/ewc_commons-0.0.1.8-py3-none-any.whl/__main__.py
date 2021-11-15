# Import the library main init function
from .__init__ import __version__

# Import the typing library so variables can be type cast
from typing import List, Tuple

# Import the sys for args
import sys

# Import the Sophie launcher system needed
from ewccommons.sophie import (
    _TNGN_,
    _CLI_Arg_Handled_,
    SophieLauncher,
    CLIUsageHandler,
    launcher,
)

# Import the collection of available modules
from ewccommons import dice
from ewccommons import dicerolls
from ewccommons import carddeck

_app_name_: str = "EWC Commons Library"
_short_options_: str = "hvq:"
_long_options_: List = [
    "help",
    "version",
    "dice",
    "dicerolls=",
    "carddeck",
    "enquiry=",
]


def cli_argument_handler(
    opts: Tuple,
    args: Tuple,
    show_usage_help: _TNGN_,
    show_version: _TNGN_,
) -> _CLI_Arg_Handled_:
    """
    Handle the processing of the cli arguments.
    """
    enquiry: str = None
    opt: str
    arg: str
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            # Just show the usage help & halt
            show_version()
            show_usage_help()
            sys.exit()
        elif opt in ("-v", "--version"):
            # Just show the version & halt
            show_version()
            sys.exit()
        elif opt == "--dice":
            # Run the dice main module function
            dice.check_output()
        elif opt == "--dicerolls":
            # Convert the value to lower, split on space
            # Add any unnamed arguments as potential included option values
            ds: List[str] = arg.lower().split() + list(args)
            # Supply the arguments to the dicerolls main function for handling
            dicerolls.rolls(*ds)
        elif opt == "--carddeck":
            # Run the carddeck main module function
            carddeck.spread_deck()
        elif opt in ("-q", "--enquiry"):
            # Assign the enquiry value
            enquiry = arg
    return enquiry, args


def help_text() -> str:
    """
    Generate the help text to display.

    TODO get this to read from a file???

    :return: The app help text multiline string.
    """
    return "\n".join(
        [
            "  -h --help (Show this help)",
            "  -v --version (Show library version)",
            "  --dice (Run the dice module)",
            "  --dicerolls Optional[d6 ...] (Run the dicerolls module)",
            "  --carddeck (Run the carddeck module)",
            "  -q <enquiry> (Make an enquiry)",
        ]
    )


def main(*args) -> None:
    # Define the variable types
    sophie: SophieLauncher
    usage: CLIUsageHandler
    # Create a new app launcher & usage instance
    sophie, usage = launcher(
        _usage=CLIUsageHandler,
        app_name=_app_name_,
        version=__version__,
        short_options=_short_options_,
        long_options=_long_options_,
        help_text=help_text,
    )
    # Configure the launch to use the supplied cli arguments
    sophie.config_launch(args)
    # Check if something went wrong getting a processor
    if sophie.has_error:
        # Display the usage help & GTFO
        sophie.show_usage_help()
        sys.exit(sophie.what_went_wrong())
    # Let's have a look at what we got
    print(
        "Let's have a look:",
        "#############",
        "Sophie",
        sophie,
        "Usage",
        usage,
        "#############",
        sep="\n",
    )
    # Define the usage & types of variables to be used in this scope
    enquiry: str
    enquiry, args = sophie.launch(cli_argument_handler)
    print(enquiry, args)
    # sophie.show_usage_help()


# Call the main library init function
main(*sys.argv[1:])
