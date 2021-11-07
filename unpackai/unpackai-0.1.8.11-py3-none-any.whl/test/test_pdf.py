"""Testing code generated by nbdev in unpackai/pdf.py"""
# Generated automatically from notebook nbs/51_pdf_utils.ipynb

from unpackai.pdf import *

# Test Cell
# For Test Cases (might have duplicate import because it will be in a dedicated file)
import re
from difflib import unified_diff
from pathlib import Path
from typing import List

import pytest
from test_common.utils_4_tests import DATA_DIR, IMG_DIR, check_no_log, check_only_warning
from test_utils import GITHUB_TEST_DATA_URL, check_connection_github
from unpackai import nlp

# Test Cell
def compare_strings(
    exp: str,
    obt: str,
    name_exp: str = "Expected [string #1]",
    name_obt: str = "Obtained [string #2]",
) -> str:
    """Get unified diff of 2 string"""
    exp_lines = exp.splitlines(keepends=True)
    obt_lines = obt.splitlines(keepends=True)
    differences = unified_diff(exp_lines, obt_lines, fromfile=name_exp, tofile=name_obt)
    return "".join(differences)


# Test Cell
GITHUB_TEST_PDF = f"{GITHUB_TEST_DATA_URL}/Deep%20learning.pdf"
LOCAL_TEST_PDF = DATA_DIR / "Deep learning.pdf"
LOCAL_TEST_TXT = DATA_DIR / "Deep learning.txt"

LOCAL_TEST_PDF_SMALL = DATA_DIR / "to_download.pdf"
LOCAL_TEST_TXT_SMALL = DATA_DIR / "to_download.txt"


@pytest.fixture(scope="session")
def local_textual():
    return TextualPDF.from_path(LOCAL_TEST_PDF)


@pytest.fixture(scope="session")
def test_pdf_as_txt():
    return Path(LOCAL_TEST_TXT).read_text(encoding="utf-8")


def cleanup_spaces(text: str) -> str:
    return re.sub(r"[\r\n\t\s]+", " ", text, flags=re.S)


class Test_TextualPDF:
    def test_from_path(self, local_textual):
        """Test extract Textual of PDF from local file"""
        t = local_textual
        assert "Deep learning" in t.text, f"Text parsed:\n{t.text}"

    def test_from_path_not_pdf(self):
        """Test extract Textual of non-PDF file"""
        textual = TextualPDF.from_path(LOCAL_TEST_TXT)
        assert textual.text == nlp.Textual.from_path(LOCAL_TEST_TXT).text

    def test_from_path_pdf(self, local_textual):
        """Test extract Textual of PDF from local path using from_path_pdf"""
        textual = TextualPDF.from_path_pdf(LOCAL_TEST_PDF)
        assert textual.text == local_textual.text

    @pytest.mark.parametrize(
        "pdf, txt, encoding",
        [
            (LOCAL_TEST_PDF_SMALL, LOCAL_TEST_TXT_SMALL, None),
            (LOCAL_TEST_PDF, LOCAL_TEST_TXT, "utf-8"),
        ],
        ids=["small", "utf-8"],
    )
    def test_from_path_pdf_no_cleanup(self, pdf: Path, txt: Path, encoding):
        """Test extract Textual from PDF without cleanup"""
        content = cleanup_spaces(txt.read_text(encoding=encoding))

        textual = TextualPDF.from_path_pdf(pdf, cleanup=False)
        textual_txt = cleanup_spaces(textual.text)
        assert textual_txt == content, compare_strings(content, textual_txt)

    @pytest.mark.parametrize("pages", [[0], [0, 1], [0, 2], range(1, 4)])
    def test_from_path_pdf_pages(self, pages):
        """Test extract Textual from PDF with specific pages"""
        text = TextualPDF.from_path_pdf(LOCAL_TEST_PDF, page_numbers=pages).text
        for p in pages:
            assert f"Page {p+1}" in text, f"Page {p+1} not found in Textual: {text}"
        pages_extracted = re.findall(r"Page (\d+)", text)
        extra_pages = set(pages_extracted) - set(str(p + 1) for p in pages)
        assert extra_pages == set(), f"Extra pages extracted: {extra_pages}"

    def test_from_url(self, check_connection_github, local_textual):
        """Test extract Textual of PDF from URL"""
        textual = TextualPDF.from_url(GITHUB_TEST_PDF)
        assert textual.text == local_textual.text, f"URL text: {textual.text}"

    def test_from_url_pdf(self, check_connection_github, local_textual):
        """Test extract Textual of PDF from URL using from_url_pdf"""
        textual = TextualPDF.from_url_pdf(GITHUB_TEST_PDF)
        assert textual.text == local_textual.text, f"URL text: {textual.text}"

    # TODO: Add Tests with password
