from dataclasses import dataclass

from dinject.enums import Content, Host, Range


@dataclass
class Instruction:
    """Document injection instruction"""

    content: Content = Content.MARKDOWN
    """Content type to inject the result as."""

    range: Range = Range.NONE
    """Injection site demarcation."""

    host: Host = Host.SHELL
    """Execution host."""
