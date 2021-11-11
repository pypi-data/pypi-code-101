from botcity.utils.parser import StringParser

text = """<h1>Example</h1>

<p>A paragraph with some content.
This is a test of multiple
lines for the parser.</p>"""


def test_parser_init():
    parser = StringParser(text)
    assert parser.current_position == 0
    assert parser.content == text


def test_goto_tag_start():
    parser = StringParser(text)
    val = parser.goto_tag_start("h1")
    assert val is parser
    assert parser.current_position == 1

    # Try to go to non-existent tag. Remain at same place.
    val = parser.goto_tag_start("@")
    assert val is parser
    assert parser.current_position == 1


def test_goto_tag_end():
    parser = StringParser(text)
    parser.goto_tag_end("h1")
    assert parser.current_position == 3

    parser.goto_tag_end("@")
    assert parser.current_position == 3


def test_next_contains():
    parser = StringParser(text)
    parser.goto_tag_end("<h1>")
    assert parser.next_contains("</h1>")
    assert not parser.next_contains("@")


def test_backward_contains():
    parser = StringParser(text)
    parser.goto_tag_start("</h1>")
    assert parser.backward_contains("<h1>")
    assert not parser.backward_contains("@")


def test_back_to_tag_start():
    parser = StringParser(text)

    parser.goto_tag_end("<h1>")
    assert parser.current_position == 4
    assert parser.back_to_tag_start("<h1>")
    assert parser.current_position == 0

    parser.goto_tag_end("</h1>")
    pos = parser.current_position
    assert not parser.back_to_tag_start("@")
    assert parser.current_position == pos


def test_back_to_tag_end():
    parser = StringParser(text)
    parser.goto_tag_end("</h1>")
    assert parser.current_position != 0
    assert parser.back_to_tag_end("<h1>")
    assert parser.current_position == 4

    assert not parser.back_to_tag_end("@")


def test_read_until():
    parser = StringParser(text)
    parser.goto_tag_end("<h1>")
    ret = parser.read_until("</h1>")
    assert ret == "Example"

    assert parser.read_until("@") is None


def test_get_next_chars():
    parser = StringParser(text)
    parser.goto_tag_end("<h1>")
    ret = parser.get_next_chars(2)
    assert ret == "Ex"

    ret = parser.get_next_chars(-1)
    assert ret == ""


def test_read_next_lines_until():
    parser = StringParser(text)
    parser.goto_tag_end("<p>")
    lines = parser.read_next_lines_until("</p>")
    assert len(lines) == 3

    lines = parser.read_next_lines_until("@")
    assert len(lines) == 0


def test_read_next_lines():
    parser = StringParser(text)
    parser.goto_tag_end("<p>")
    lines = parser.read_next_lines(2)
    assert len(lines) == 2

    lines = parser.read_next_lines(10)
    assert lines is None


def test_goto_next_line():
    parser = StringParser(text)
    parser.goto_tag_end("<p>")
    ret = parser.goto_next_line()
    assert ret is parser

    assert parser.read_next_lines(1) == ["This is a test of multiple"]

    parser.goto_tag_end("</p>")
    pos = parser.current_position

    # No new lines so we stay at same place
    parser.goto_next_line()
    assert parser.current_position == pos


def test_read():
    parser = StringParser(text)
    parser.goto_tag_start("lines")
    ret = parser.read()
    assert ret == "lines for the parser.</p>"
