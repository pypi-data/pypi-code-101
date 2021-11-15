"""EWC Commons Sophie

Can be used/invoked as a module, why? because print is a valid debug tool!
"""
# Import the typing library so variables can be type cast
from typing import Any, Callable, List, Tuple

# Import the use of abstract classes
from abc import ABC, abstractmethod

# Import the system & get options to process command line arguments
import sys
import getopt

from ewccommons import app_version

_CLI_Arg_Handled_ = Tuple[Any, ...]
"""Type Alias Definition

Define the return type of the callback handler function.
"""

_TNGN_ = Callable[[], None]
"""Type Alias Definition

Define a Takes Nothing, Gives Nothing function signature.
"""

_CLI_Arg_Handler_ = Callable[[Tuple, Tuple, _TNGN_, _TNGN_], _CLI_Arg_Handled_]
"""Type Alias Definition

Define the callback handler function signature.
"""


def not_what_i_wanted(msg: str, expected: Any, got: Any) -> ValueError:
    """
    Create a ValueError describing what was wanted vs what was used.

    :param msg: (str) A string message to prefix the error message with.
    :param expected: (Any) The expected argument value type.
    :param got: (Any) The actual variable used.
    :return: The generated value error ready to raise.
    """
    _expected = type(expected)
    _got = type(got)
    return ValueError(f"{msg}: Expected [{_expected}] Got [{_got}]")


class SophieError(Exception):
    """
    Define a general Sophie error with ability to hold context.
    """

    def __init__(self, message: str, ctx: Any = None) -> None:
        """Initialize the error base

        Set the message and any supporting context.

        :param message: The error message string.
        :param ctx: (Any) Optional error context.
        """
        super().__init__(message)
        self.__ctx = ctx

    @property
    def context(self):
        """
        Provide access to any asscoiated context for the error.
        """
        return self.__ctx


class SophieExecutionError(SophieError):
    """
    Define a general Sophie execution error.
    """


class SophieProcessor(ABC):
    """
    Define the object signature of a processor.
    """

    @abstractmethod
    def __init__(self, payload: Any) -> None:
        """Initialize the processor base

        Set the instance properties.

        :param payload: (Any) The payload to process.
        """
        super().__init__()
        self.__processed: Tuple[Any, ...] = None
        self.__error: Exception = None
        self.__process_payload: Any = payload

    @abstractmethod
    def process(self):
        """
        Pro-cessing...
        """

    @property
    def processing_payload(self) -> Any:
        """
        Provide access to the processing payload.

        :return: The processing payload.
        """
        return self.__process_payload

    @property
    def processed_result(self) -> Any:
        """
        Provide access to the processed payload result.

        :return: The processed payload.
        """
        return self.__processed

    @property
    def has_error(self) -> bool:
        """
        Check if the processor encountered an error.

        :return: True if an error has been encountered.
        """
        return self.__error is not None

    @property
    def error(self) -> SophieError:
        """
        Provide access to any Exceptions raised & intercepted.

        :return: The error that has been encountered is any.
        """
        return self.__error

    def processed(self, _result: Tuple[Any, ...]) -> None:
        """
        Set processed payload result.

        :param _result: A tuple list of any processing results.
        """
        self.__processed = _result

    def errored(self, _err: Exception) -> None:
        """
        Set an encountered error / exception.

        :param _err: The error/exception intercepted.
        """
        # Wrap the intercepted exception/error in a sophie error
        self.__error = SophieExecutionError(str(_err), _err)


class CLIUsage(ABC):
    """
    Define how a CLI Usage handler should look.
    """

    default_short_options: str = "hv"
    """Class Property

    String list of 1 character default options for help & version
    """

    default_long_options: List = ["help", "version"]
    """Class Property

    List of default long options names for help & version
    """

    @abstractmethod
    def __init__(self, short_options: str, long_options: List) -> None:
        """Initialize the usage base

        Set the usage details.

        :param short_options: The string list of 1 character cli options.
        :param long_options: The List of long cli options names.
        """
        super().__init__()
        self.__short_options: str = short_options
        self.__long_options: List = long_options
        self.arg_processor: SophieProcessor = None
        # Initialise the list of CLI arguments used at runtime
        self.__used: List = list()
        self.__ignored_used: List = list()

    @abstractmethod
    def help(self) -> str:
        """
        Get the command line usage help.

        :return: The usage help text.
        """

    @property
    def short_options(self) -> str:
        """
        Get all the cli 1 character options available.

        :return: The string list of 1 character cli options.
        """
        return self.__short_options

    @property
    def long_options(self) -> List:
        """
        Get a list of all the cli long options available.

        :return: The List of long cli options names.
        """
        return self.__long_options

    @property
    def used(self) -> List:
        """
        Get a list of all the cli arguments used at runtime.

        :return: The list of all the runtime used cli options.
        """
        return self.__used

    @property
    def ignored(self) -> List:
        """
        Get a list of any invalid cli arguments used at runtime.

        :return: The list of all the invalid/ignored runtime cli options used.
        """
        return self.__ignored_used

    def using(self, arg_processor: SophieProcessor) -> None:
        """
        Provide a means of setting the CLI argument processor.

        :param arg_processor: Specify a argument processor to use.
        """
        self.arg_processor = arg_processor


class CLArgsProcessor(SophieProcessor):
    """
    Processor class to extract the CLI arguments used.
    """

    def __init__(self, argv, usage: CLIUsage) -> None:
        """Initialize the cli argument processor

        Set the instance properties

        :param argv: The cli argument values list.
        :param usage: The cli usage instance to process for.
        """
        super().__init__(payload=argv)
        self.usage: CLIUsage = usage

    def process(self):
        """
        process the command line arguments & return the corresponding data.

        TODO make sure only valid argv values are used or it raises GetoptError.
        TODO Get the processed values exposed correctly.

        BUG Any unspecified --args options used in the supplied argv cause
            GetoptError(_('option --%s not recognized') % opt, opt)
            Which abondons the whole attempt, do not pass Go, do not collect $200.
        """
        try:
            # Extract the options & arguments specified from the supplied arguments
            opts, args = getopt.getopt(
                self.processing_payload,
                self.usage.short_options,
                self.usage.long_options,
            )
        except getopt.GetoptError as _err:
            # Hello there
            return self.errored(_err)
        # Set the options & arguments to process later
        # TODO Get the values exposed correctly
        self.processed(_result=(opts, args))


class LaunchProcessor(SophieProcessor):
    """
    Processor class to extract the CLI arguments used.
    """

    def __init__(
        self,
        handler: _CLI_Arg_Handler_,
        show_usage_help: _TNGN_,
        show_version: _TNGN_,
        arg_processor: CLArgsProcessor,
    ) -> None:
        """Initialize the launch processor

        Set the instance properties.

        :param handler: (_CLI_Arg_Handler_) A function to handle the launch.
        :param show_usage_help: (_TNGN_) A function to display the app usage help text.
        :param show_version: (_TNGN_) A function to display the app version text.
        :param arg_processor: (CLArgsProcessor) The cli argument processor to use.
        """
        # Use a dictionary of function references as the processing payload
        super().__init__(
            payload={
                "handler": handler,
                "show_usage_help": show_usage_help,
                "show_version": show_version,
            }
        )
        # Set the cli argument processor to get the runtime options used
        self.arg_processor: CLArgsProcessor = arg_processor

    def process(self):
        """
        process the command line arguments & return the corresponding data.
        """
        # Get the runtime cli options used
        opts, args = self.arg_processor.processed_result
        # Process with the launch options
        self.processed(
            _result=self.processing_payload["handler"](
                opts,
                args,
                self.processing_payload["show_usage_help"],
                self.processing_payload["show_version"],
            )
        )


class CLIUsageHandler(CLIUsage):
    """
    Create a CLI argument usage handler.
    """

    def __init__(self, short_options: str, long_options: List, help_text) -> None:
        """Initialize the cli usage

        Set the usage details.

        :param short_options: The string list of 1 character cli options.
        :param long_options: The List of long cli options names.
        :param help_text: Help text string or function that generates it.
        """
        super().__init__(short_options=short_options, long_options=long_options)
        # If the help text specified is not a callable function, wrap it in a lambda
        self._help_text: Callable[[], str] = (
            help_text if callable(help_text) else lambda: str(help_text)
        )

    def help(self) -> str:
        """
        Get the usage help for the options.

        :return: The help text string.
        """
        return self._help_text()

    def __str__(self) -> str:
        """
        Get the object as a human readable string.

        :return: The usage help text string.
        """
        return "\n".join([self._help_text()])


class SophieLauncher:
    """
    Define the main CLI script launcher.
    """

    def __init__(
        self, usage: CLIUsage, app_name: str = __name__, version: str = "0.0.1"
    ) -> None:
        """Initialize the sophie launch mechanism

        Set the instance properties.

        :param usage: The app usage instance.
        :param name: An app name.
        :param version: An app version string.
        """
        self.launch_error: SophieError = None
        self.usage: CLIUsage = usage
        self.__app_name: str = app_name
        self.__version: str = version
        self.__configured: bool = False

    @property
    def has_error(self) -> bool:
        """
        Check if the launcher encountered an error.

        :return: True if there has been a launch error.
        """
        return self.launch_error is not None

    @property
    def app_name(self) -> str:
        """
        Get the name of the app instance.

        :return: The app name string.
        """
        return self.__app_name

    @property
    def app_version(self) -> str:
        """
        Get the app instance version.

        :return: The app version string.
        """
        return self.__version

    def show_usage_help(self) -> None:
        """
        Display the help text by constructing the app name with the usage help.
        """
        print(self.usage.help(), sep=" ")

    def show_version(self) -> None:
        """
        Display the version text by constructing the app name with the version.
        """
        print(self)

    def config_launch(self, argv):
        """
        Configure the launch process.

        :param argv: The cli argument values used.
        """
        # Create a CLI argument processor
        self.arg_processor: CLArgsProcessor = CLArgsProcessor(
            argv=argv, usage=self.usage
        )
        # Process the commandline argv for launch options
        self.arg_processor.process()
        # Check for processor errors
        if self.arg_processor.has_error:
            self.launch_error = self.arg_processor.error

    def launch(
        self,
        handler: _CLI_Arg_Handler_,
    ) -> _CLI_Arg_Handled_:
        """
        Launch the module/script.

        :param handler: (_CLI_Arg_Handler_) A function to handle the launch.
        :return: (_CLI_Arg_Handled_) The handled launch process.
        """
        # Create a new launch processor
        launch_processor: LaunchProcessor = LaunchProcessor(
            handler=handler,
            show_usage_help=self.show_usage_help,
            show_version=self.show_version,
            arg_processor=self.arg_processor,
        )
        launch_processor.process()
        return launch_processor.processed_result

    def what_went_wrong(self) -> str:
        """
        Determine what if anything went wrong.

        :return: A string containing any errors encountered.
        """
        if not self.has_error:
            return "Program executed within accepted parameters."
        return "\n".join([str(self), "ERROR:", str(self.launch_error)])

    def __str__(self) -> str:
        """
        Get the object as a human readable string.

        :return: An App name - Version - x multiline string.
        """
        return app_version(self.app_name, self.app_version)


def launcher(
    _usage: CLIUsageHandler,
    app_name: str = __name__,
    version: str = "0.0.1",
    short_options: str = "hvq:",
    long_options: List = ["help", "version", "enquiry="],
    help_text="-q <enquiry>",
) -> Tuple[SophieLauncher, CLIUsageHandler]:
    """
    Shortcur method to create a SophieLauncher.

    :param _usage: The app usage class to use.
    :param app_name: An optional app name.
    :param version: An optional app version string.
    :param short_options: The optional string list of 1 character cli options.
    :param long_options: The optional List of long cli options names.
    :param help_text: Optional help text string or function to generate it.
    :return: A tuple of SophieLauncher and the CLIUsageHandler created to launch.
    """
    # Create the usage instance
    usage: CLIUsageHandler = _usage(
        short_options=short_options,
        long_options=long_options,
        help_text=help_text,
    )
    # Create the launcher with the usage
    sophie: SophieLauncher = SophieLauncher(
        usage=usage,
        app_name=app_name,
        version=version,
    )
    return sophie, usage


def oil_math(*args) -> None:
    """Main function

    to test composite funcs for Oli.
    """
    fog, gof = oil_composites()
    for x in range(1, 11):
        print(
            f"################## x: {x}",
            f"gof(x) : {gof(x)}",
            f"fog(x) : {fog(x)}",
            f"fog(gof(x)) : {fog(gof(int(x)))}",
            f"gof(fog(x)) : {gof(fog(int(x)))}",
            sep="\n",
        )


def oil_composites() -> Tuple[Callable[[float], float], Callable[[float], float]]:
    """
    Fog on the G is not fine, not fine.
    """
    #    P = 1
    Q = 1
    #    R = 3
    #    S = 7
    #    T = 8
    #    U = 9

    def fog(x: float) -> float:
        """
        Define the f of g on x.
        """
        return x * x + Q

    def gof(x: float) -> float:
        """
        Define the g of f on x.
        """
        return x * x * x + 2 * x

    return fog, gof


def main() -> None:
    """Main function

    Run as a module and convert any CLI arguments to lowercase.
    """
    # Call the main function with any command line arguments after the module name
    oil_math(*[str(_).lower() for _ in sys.argv[1:]])


# Make sure the script is being called as a script & not being imported into
# another module file
if __name__ == "__main__":
    # Call the main function
    main()
