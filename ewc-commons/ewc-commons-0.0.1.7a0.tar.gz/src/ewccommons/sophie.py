# Import the typing library so variables can be type cast
from typing import Any, Callable, List, Tuple

# Import the use of abstract classes
from abc import ABC, abstractmethod

# Import the system & get options to process command line arguments
import getopt

_CLI_Arg_Handled_ = Tuple[Any, ...]
"""Define the return type of the callback handler function"""

_TNGN_ = Callable[[], None]
"""Define a Takes Nothing, Gives Nothing function signature"""

_CLI_Arg_Handler_ = Callable[[List, List, _TNGN_, _TNGN_], _CLI_Arg_Handled_]
"""Define the callback handler function signature"""


class SophieError(Exception):
    """Define a general Sophie error with ability to hold context"""

    def __init__(self, message: str, ctx: Any = None) -> None:
        """Initialise the error with a message and any supporting context"""
        super().__init__(message)
        self.__ctx = ctx

    @property
    def context(self):
        """Provide access to any asscoiated context for the error"""
        return self.__ctx


class SophieExecutionError(SophieError):
    """Define a general Sophie execution error"""


class SophieProcessor(ABC):
    """Define the object signature of a processor"""

    @abstractmethod
    def __init__(self, payload: Any) -> None:
        """Initialize the class instance & set the instance properties"""
        super().__init__()
        self.__processed: Tuple[Any, ...] = None
        self.__error: Exception = None
        self.__process_payload: Any = payload

    @abstractmethod
    def process():
        """Pro-cessing"""

    @property
    def processing_payload(self) -> Any:
        """Provide access to the processing payload"""
        return self.__process_payload

    @property
    def processed_result(self) -> Any:
        """Provide access to the processed payload result"""
        return self.__processed

    @property
    def has_error(self) -> bool:
        """Check if the processor encountered an error"""
        return self.__error is not None

    @property
    def error(self) -> SophieError:
        """Provide access to any Exceptions raised & intercepted"""
        return self.__error

    def processed(self, _result: Tuple[Any, ...]) -> None:
        """Set an encountered error / exception"""
        self.__processed = _result

    def errored(self, _err: Exception) -> None:
        """Set an encountered error / exception"""
        self.__error = SophieExecutionError(str(_err), _err)


class CLIUsage(ABC):
    """Define how a CLI Usage handler should look"""

    default_short_options: str = "hv"
    """Define the list of 1 character default options for help & version"""

    default_long_options: List = ["help", "version"]
    """Define the list of default long options names for help & version"""

    @abstractmethod
    def __init__(self, short_options: str, long_options: List) -> None:
        """Set the usage details"""
        super().__init__()
        self.__short_options: str = short_options
        self.__long_options: List = long_options
        self.arg_processor: SophieProcessor = None
        # Initialise the list of CLI arguments used at runtime
        self.__used: List = list()
        self.__ignored_used: List = list()

    @abstractmethod
    def help(self) -> str:
        """Get the command line usage help"""

    @property
    def short_options(self) -> str:
        """Get all the cli one character options available"""
        return self.__short_options

    @property
    def long_options(self) -> List:
        """Get a list of all the cli long options available"""
        return self.__long_options

    @property
    def used(self) -> List:
        """Get a list of all the cli arguments used at runtime"""
        return self.__used

    @property
    def ignored(self) -> List:
        """Get a list of any invalid cli arguments used at runtime"""
        return self.__ignored_used

    def using(self, arg_processor: SophieProcessor) -> None:
        """Provide a means of setting the CLI argument processor"""
        self.arg_processor = arg_processor


class CLArgsProcessor(SophieProcessor):
    """Processor class to extract the CLI arguments used"""

    def __init__(self, argv, usage: CLIUsage) -> None:
        """Initialize the class instance & set the instance properties"""
        super().__init__(payload=argv)
        self.usage: CLIUsage = usage

    def process(self):
        """process the command line arguments & return the corresponding data"""
        # TODO make sure only valid argv values are used or it raises GetoptError
        # BUG Any unspecified --args options used in the supplied argv cause
        # GetoptError(_('option --%s not recognized') % opt, opt)
        # Which abondons the whole attempt, do not pass Go, do not collect $200
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
    """Processor class to extract the CLI arguments used"""

    def __init__(
        self,
        handler: _CLI_Arg_Handler_,
        show_usage_help: _TNGN_,
        show_version: _TNGN_,
        arg_processor: CLArgsProcessor,
    ) -> None:
        """Initialize the class instance & set the instance properties"""
        super().__init__(
            payload={
                "handler": handler,
                "show_usage_help": show_usage_help,
                "show_version": show_version,
            }
        )
        self.arg_processor: CLArgsProcessor = arg_processor

    def process(self):
        """process the command line arguments & return the corresponding data"""
        opts, args = self.arg_processor.processed_result
        self.processed(
            _result=self.processing_payload["handler"](
                opts,
                args,
                self.processing_payload["show_usage_help"],
                self.processing_payload["show_version"],
            )
        )


class CLIUsageHandler(CLIUsage):
    """Create a CLI argument usage handler"""

    def __init__(self, short_options: str, long_options: List, help_text) -> None:
        """Set the usage details"""
        super().__init__(short_options=short_options, long_options=long_options)
        # If the help text specified is not a callable function, wrap it in a lambda
        self._help_text: Callable[[], str] = (
            help_text if callable(help_text) else lambda: str(help_text)
        )

    def help(self) -> str:
        """Get the usage help for the options"""
        return self._help_text()

    def __str__(self) -> str:
        """Get the object as a human readable string"""
        return "\n".join([self._help_text()])


class SophieLauncher:
    """Define the main CLI script launcher"""

    def __init__(
        self, usage: CLIUsage, app_name: str = __name__, version: str = "0.0.1"
    ) -> None:
        """Initialize the class instance & set the instance properties"""
        self.launch_error: SophieError = None
        self.usage: CLIUsage = usage
        self.__app_name: str = app_name
        self.__version: str = version
        self.__configured: bool = False

    @property
    def has_error(self) -> bool:
        """Check if the launcher encountered an error"""
        return self.launch_error is not None

    @property
    def app_name(self) -> str:
        """Get the name of the app instance"""
        return self.__app_name

    @property
    def app_version(self) -> str:
        """Get the app instance version"""
        return self.__version

    def show_usage_help(self) -> None:
        """Display the help text by constructing the app name with the usage help"""
        print(self.usage.help(), sep=" ")

    def show_version(self) -> None:
        """Display the version text by constructing the app name with the version"""
        print(self)

    def config_launch(self, argv):
        """Configure the launch process"""
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
        """Launch the module/script"""
        launch_processor: LaunchProcessor = LaunchProcessor(
            handler=handler,
            show_usage_help=self.show_usage_help,
            show_version=self.show_version,
            arg_processor=self.arg_processor,
        )
        return launch_processor.process()

    def what_went_wrong(self) -> str:
        """Determine what if anything went wrong"""
        if not self.has_error:
            return "Program executed within accepted parameters."
        return "\n".join([str(self), "ERROR:", str(self.launch_error)])

    def __str__(self) -> str:
        """Get the object as a human readable string"""
        return "\n".join([self.app_name, f"Version - {self.app_version}"])


def launcher(
    _usage: CLIUsageHandler,
    app_name: str = __name__,
    version: str = "0.0.1",
    short_options: str = "hvq:",
    long_options: List = ["help", "version", "enquiry="],
    help_text="-q <enquiry>",
) -> Tuple[SophieLauncher, CLIUsageHandler]:
    """Shortcur method to create a SophieLauncher"""
    usage: CLIUsageHandler = _usage(
        short_options=short_options,
        long_options=long_options,
        help_text=help_text,
    )
    sophie: SophieLauncher = SophieLauncher(
        usage=usage,
        app_name=app_name,
        version=version,
    )
    return sophie, usage


def main(*args) -> None:
    """Main function to run the module"""
    #    P = 1
    Q = 1
    #    R = 3
    #    S = 7
    #    T = 8
    #    U = 9

    def fog(x: int) -> int:
        return x * x + Q

    def gof(x: int) -> int:
        return x * x * x + 2 * x

    # return fog, gof
    pass


# Make sure the script is being called as a script & not being imported into
# another module file
if __name__ == "__main__":
    # Call the main function
    # Import the sys to get any argv used
    import sys

    fog, gof = main(*sys.argv[1:])
    quit()
    for x in range(1, 11):
        print(gof(x))
        print(fog(x))
        print(fog(gof(int(x))))
        print(gof(fog(int(x))))
        print("##################")
