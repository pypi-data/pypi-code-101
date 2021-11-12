# @Author: b3yc0de
# @Date:   08 Nov 2021, 22:43 CET
# @Email:  mc25.studio@gmail.com
# @Filename: obff.py
# @License: GPL-3.0

import os
import gzip
from enum import Enum
from obff.utils import IntToBytes, IntFromBytes, formatBytes

class OBFF_VERSION(bytes, Enum):
    V1 = b'\x4f\x42\x46\x46\x31\x30\x00\x00'

VALID_VERSIONS = [version.value for version in OBFF_VERSION]

def errorPrint(text: str):
    raise Exception("ERROR : {0}".format(text))

class Cover:
    def __init__(self, data: bytes):
        self._bytes = data

    def saveImage(self, file_path: str):
        """Save Cover as image

        Args:
            file_path (str): File path
        """

        # Checking if given file exists
        if not os.path.isfile(file_path):
            errorPrint("Given file path does not exists\n\t\t> \033[4m{0}".format(file_path))
            return

        file = open(file_path, "wb")
        file.write(self._bytes)
        file.close()

    @property
    def size(self) -> int:
        """Get size of Cover

        Returns:
            int: Cover size
        """
        return len(self._bytes)

    @property
    def bytes(self) -> bytes:
        """Get bytes of Cover

        Returns:
            bytes: Cover as bytes
        """

        return self._bytes

class Page:
    def __init__(self, content: bytes,  number: int = None):
        """Page
        """

        self._number = number
        self._content = content

    @property
    def size(self) -> int:
        """Get size of Page

        Returns:
            int: Page size
        """
        return len(self._content)


    @property
    def content(self) -> bytes:
        """Get page bytes

        Returns:
            bytes: Page content as bytes
        """

        return self._content


    @property
    def number(self) -> int:
        """Get number of Page

        Returns:
            int: Number of Page
        """

        return self._number

    @number.setter
    def number(self, number: int):
        """Set number of Page

        args:
            number (int): Number of Page
        """

        self._number = number

class Book:

    def __init__(self):
        self._title = ""
        self._description = ""
        self._cover = Cover(b'')
        self._pages = []
        self._page_count = 0

    def addPage(self, page: Page):
        """Add Page to Book

        Args:
            page (Page): Book Page
        """

        tmp_page = page
        self._page_count += 1
        tmp_page.number = self._page_count
        self._pages.append(tmp_page)


    @property
    def title(self) -> str:
        """Get Book Title

        Returns:
            str: Title
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Set Book Title

        Args:
            title (str): Title
        """
        self._title = title


    @property
    def description(self) -> str:
        """Get Book Description

        Returns:
            str: Description
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Set Book Description

        Arg:
            description (str): Description
        """
        self._description = description


    @property
    def cover(slef) -> Cover:
        """Get Book Cover

        Returns:
            Cover: Book Cover
        """
        return self._cover

    @cover.setter
    def cover(self, cover: Cover):
        """Set Book Cover

        Args:
            cover (Cover): Book Cover
        """
        self._cover = cover


    @property
    def pages(self) -> list:
        """Get list of Page Object

        Returns:
            list: List of Page Objects
        """

        return self._pages

    @property
    def page_count(self) -> int:
        """Get count of pages

        Returns:
            int: Page count
        """
        return self._page_count


    @property
    def _title_bytes(self) -> bytes:
        """Get Title as bytes

        Returns:
            bytes: Title bytes (utf-8)
        """
        return self._title.encode("utf-8")

    @property
    def _desc_bytes(self) -> bytes:
        """Get Description as bytes

        Returns:
            bytes: Description bytes (utf-8)
        """
        return self._description.encode("utf-8")

    @property
    def _cover_bytes(self) -> bytes:
        """Get Cover as bytes

        Returns:
            bytes: Cover as bytes
        """
        return self._cover.bytes

    @property
    def _pages_bytes(self) -> bytes:
        """Get Pages as formetted bytes (uncompressed)

        Returns:
            bytes: Formetted pages
        """
        retBytes = b''

        # Adding: Page count
        retBytes += IntToBytes(self._page_count)

        for page in self._pages:
            size = IntToBytes(page.size)
            content = page.content

            # Adding: Page (size::content)
            retBytes += size + content

        return retBytes

    @_pages_bytes.setter
    def _pages_bytes(self, pages: bytes):
        """Set Pages from bytes (uncompressed)

        Arg:
             pages (bytes): Formetted pages
        """

        # Read: page count
        # <COUNT::[<size::content>...]>
        page_count = IntFromBytes(pages[0:4])

        count = 4
        for i in range(page_count):
            # Read content size
            # <SIZE::content>
            content_size = IntFromBytes(pages[count:count + 4])
            count += 4

            # Read content
            # <size::CONTENT>
            self.addPage(Page(pages[count:count + content_size]))
            count += content_size


def write(file_path: str, book: Book, version: OBFF_VERSION = OBFF_VERSION.V1):
    """Write book to file

    Args:
        file_path (str): Path (can be folder or file path)
        book (Book): Book to write as file
        version (OBFF_VERSION, optional): OBFF Version (default is V1)
    """


    if os.path.exists(file_path) and os.path.isdir(file_path):
        file_path = os.path.join(file_path, "{0}.obff".format(book.title.replace(" ", "_").lower()))



    book_title = book._title_bytes # Encoding to utf-8
    book_desc = book._desc_bytes # Encoding to utf-8
    book_cover = book._cover_bytes
    book_pages = gzip.compress(book._pages_bytes) # first compression
    book_pages = gzip.compress(book_pages) # second compression

    file = open(file_path, "wb")

    # Write: File Header
    # <FILEHEADER::stitle::sdesc::scover::spages::title::desc::cover::pages>
    file.write(version.value)

    # Write: Size of Title (bytes)
    # <fileheader::SIZE_TITLE::sdesc::scover::spages::title::desc::cover::pages>
    file.write(IntToBytes(len(book_title)))
    # Write: Size of Description (bytes)
    # <fileheader::stitle::SIZE_DEC::scover::spages::title::desc::cover::pages>
    file.write(IntToBytes(len(book_desc)))
    # Write: Size of Cove (bytes)
    # <fileheader::stitle::sdesc::SIZE_COVER::spages::title::desc::cover::pages>
    file.write(IntToBytes(len(book_cover)))
    # Write: Size of Pages (bytes, compressed)
    # <fileheader::stitle::sdesc::scover::SIZE_PAGES::title::desc::cover::pages>
    file.write(IntToBytes(len(book_pages)))


    # Write: Title string
    # <fileheader::stitle::sdesc::scover::spages::TITLE::desc::cover::pages>
    file.write(book_title)
    # Write: Description string
    # <fileheader::stitle::sdesc::scover::spages::title::DESC::cover::pages>
    file.write(book_desc)
    # Write: Cover
    # <fileheader::stitle::sdesc::scover::spages::title::desc::COVER::pages>
    file.write(book_cover)
    # Write: Pages
    # <fileheader::stitle::sdesc::scover::spages::title::desc::cover::PAGES>
    file.write(book_pages)

    # Closing file
    file.close()

def read(file_path: str) -> Book:
    """Read file

    Args:
        file_path (str): Path of file

    Returns:
        Book: File as Book
    """

    # Checking if given file exists
    if not os.path.isfile(file_path):
        errorPrint("Given file path does not exists\n\t\t> \033[4m{0}".format(file_path))
        return

    file = open(file_path, "rb").read()
    fileheader = file[0:8]
    fileversion = fileheader[4:6]

    # Checking if file version is valid
    if fileheader not in VALID_VERSIONS:
        errorPrint("Unkown file version\n\t\t> \033[4m{0}".format(formatBytes(fileheader)))
        return

    book_title = ""
    book_desc = ""
    book_cover = b''
    book_pages = b''


    # Read: Title size (bytes)
    # <fileheader::SIZE_TITLE::sdesc::scover::spages::title::desc::cover::pages>
    title_bsize = IntFromBytes(file[9:12])
    # Read: Description size (bytes)
    # <fileheader::stitle::SIZE_DEC::scover::spages::title::desc::cover::pages>
    desc_bsize = IntFromBytes(file[13:16])
    # Read: Cover size (bytes)
    # <fileheader::stitle::sdesc::SIZE_COVER::spages::title::desc::cover::pages>
    cover_bsize = IntFromBytes(file[17:20])
    # Read: Pages size (bytes)
    # <fileheader::stitle::sdesc::scover::SIZE_PAGES::title::desc::cover::pages>
    pages_bsize = IntFromBytes(file[21:24])

    count = 24

    # Read: Book Title
    # <fileheader::stitle::sdesc::scover::spages::TITLE::desc::cover::pages>
    book_title = file[count:title_bsize]
    count = count + title_bsize
    # Read: Book Description
    # <fileheader::stitle::sdesc::scover::spages::title::DESC::cover::pages>
    book_desc= file[count:desc_bsize]
    count = count + desc_bsize
    # Read: Book Cover
    # <fileheader::stitle::sdesc::scover::spages::title::desc::COVER::pages>
    book_cover = file[count:cover_bsize]
    count = count + cover_bsize
    # Read: Book Pages
    # <fileheader::stitle::sdesc::scover::spages::title::desc::cover::PAGES>
    book_pages = gzip.decompress(file[count:]) # first decompression
    book_pages = gzip.decompress(book_pages) # second decompression
    count = count + pages_bsize

    retBook = Book()
    retBook.title = book_title.decode("utf-8")
    retBook.description = book_desc.decode("utf-8")
    retBook.cover = Cover(book_cover)
    retBook._pages_bytes = book_pages # uncompressed

    return retBook
