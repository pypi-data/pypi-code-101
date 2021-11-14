from pathlib import Path
from shutil import move
from subprocess import run
from tempfile import NamedTemporaryFile
from typing import IO, Iterable, Optional, Union

from mdcode import Block, LineReader
from naughtty import NaughTTY
from thtml import Scope, write_html

from dinject.enums import Content, Host, Range
from dinject.executors import get_executor
from dinject.parser import Parser
from dinject.types import Instruction

Reader = Union[str, IO[str]]


def execute(
    block: Block,
    instruction: Instruction,
    parser: Parser,
    writer: IO[str],
) -> None:
    """
    Executes `block` then writes the result to `writer`, with respect to
    `instruction`.
    """

    executor = get_executor(block)

    if not executor:
        # We don't support this language, so pass through.
        block.render(writer)
        return

    if instruction.host == Host.TERMINAL:
        n = NaughTTY(command=executor.arguments)
        n.execute()
        content = n.output
    else:
        process = run(executor.arguments, capture_output=True)
        content = process.stdout.decode("UTF-8")

    content = content.rstrip()

    parser.write_range_start(instruction, writer)
    writer.write("\n")

    if instruction.content == Content.HTML:
        write_html(
            text=content + "\n",
            writer=writer,
            scope=Scope.FRAGMENT,
            theme="plain",
        )
        writer.write("\n")
    else:
        Block(lang="text", lines=content.split("\n")).render(writer)

    writer.write("\n")
    parser.write_range_end(writer)


def inject(
    reader: Reader,
    writer: IO[str],
    parser: Optional[Parser] = None,
) -> None:
    """Reads and injects from `reader` to `writer`."""

    line_reader = LineReader()
    parser = parser or Parser()
    skip_to_emitted_end = False

    for line in iterate_lines(reader):
        if not skip_to_emitted_end:
            line_reader.read(line)

        din = parser.get_instruction(line)

        if skip_to_emitted_end:
            if din and din.range == Range.END:
                skip_to_emitted_end = False
            continue

        if din and line_reader.complete:
            execute(
                block=line_reader.complete,
                instruction=din,
                parser=parser,
                writer=writer,
            )
            if din.range == Range.START:
                skip_to_emitted_end = True
            continue

        writer.write(line)
        writer.write("\n")


def inject_file(path: Path, parser: Optional[Parser] = None) -> None:
    """
    Executes the code blocks and injects the results into the Markdown document
    at `path`.
    """

    with NamedTemporaryFile("a", delete=False) as writer:
        with open(path, "r") as reader:
            inject(
                parser=parser,
                reader=reader,
                writer=writer,
            )
        move(writer.name, path)


def iterate_lines(reader: Reader) -> Iterable[str]:
    """Returns an line iterator."""

    it = reader.split("\n") if isinstance(reader, str) else reader

    for line in it:
        yield line.rstrip()
