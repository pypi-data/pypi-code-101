#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################
#    Exc_Errors Copyright (C) 2021 suizokukan
#    Contact: suizokukan _A.T._ orange dot fr
#
#    This file is part of Exc_Errors.
#    Exc_Errors is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Exc_Errors is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Exc_Errors.  If not, see <http://www.gnu.org/licenses/>.
################################################################################
"""
   Exc_Errors project : exc_errors/errors.py

   A convenient way to store and display error messages.


   ____________________________________________________________________________

   o  LEVEL_ERROR
   o  LEVEL_WARNING

   o  ListOfErrorMessages    class
   o  ListOfErrorMessagesSer class
   o  EW class
   o  Warn class
   o  WarnSer class
   o  Error class
   o  ErrorSer class
   o  TextFileError class
   o  TextFileErrorSer class
   o  TextFileWarn class
   o  TextFileWarnSer class
"""
from dataclasses import dataclass, field

from iaswn.iaswn import Iaswn

# https://docs.python.org/3/library/logging.html#logging-levels
LEVEL_ERROR = 40
LEVEL_WARNING = 30


class ListOfErrorMessages(list):
    """
        ListOfErrorMessages class

        Just a wrapper around a <list> of Error and similar objects.


        _______________________________________________________________________

        METHODS:
        o  __str__(self)
        o  first_msgid_is(self, msgid: str)
        o  improved_str()
        o  last_msgid_is(self, msgid: str)
        o  zero_error(self)
        o  zero_error_or_warning(self)
        o  zero_warning(self)
    """
    def __str__(self):
        """
            ListOfErrorMessages.__str__()
        """
        if self.zero_error():
            return "No error or warning"

        res = ["*** Errors/Warns ***", ]

        # ew_object : EW_like object
        for index, ew_object in enumerate(self):
            _line = f"* #{index:0>5d} " \
                ": {ew_object}".format(
                    index=index,
                    ew_object=str(ew_object))

            res.append(_line)

        return "\n".join(res)

    def first_msgid_is(self,
                       msgid: str):
        """
            ListOfErrorMessages.first_msgid_is()

            Return True if the first *Error object stored in self has .msgid
            equal to <msgid>.


            __________________________________________________________________

            RETURNED VALUE : (bool)
        """
        if len(self) == 0:
            return False

        return self[0].msgid == msgid

    def improved_str(self):
        """
            ListOfErrorMessages.improved_str()

            Return a nice representation of <self>, using colorized output.

            This functions should be used with the `rich` package.


            __________________________________________________________________

            RETURNED VALUE : (str)a nice representation of <self>.
        """
        if self.zero_error_or_warning():
            return "[yellow]*** No error or warning***[/yellow]"

        res = ["[yellow]*** Errors/Warns ***[/yellow]", ]

        # ew_object : EW_like object
        for index, ew_object in enumerate(self):
            _line = f"* [white]#{index:0>5d}[/white] " \
                    f": {ew_object}".format(
                        index=index,
                        ew_object=ew_object.improved_str())

            res.append(_line)

        return "\n".join(res)

    def last_msgid_is(self,
                      msgid: str):
        """
            ListOfErrorMessages.last_msgid_is()

            Return True if the last *Error object stored in self has .msgid
            equal to <msgid>.


            __________________________________________________________________

            RETURNED VALUE : (bool)
        """
        if len(self) == 0:
            return False

        return self[-1].msgid == msgid

    def zero_error(self):
        """
            ListOfErrorMessages.zero_error()

            Return True if <self> doesn't contain any error.


            __________________________________________________________________

            RETURNED VALUE : (bool)
        """
        # ew_object : EW_like object
        for ew_object in self:
            if ew_object.level == LEVEL_ERROR:
                return False
        return True

    def zero_error_or_warning(self):
        """
            ListOfErrorMessages.zero_error_or_warning()

            Return True if <self> is empty.


            __________________________________________________________________

            RETURNED VALUE : (bool)
        """
        return len(self) == 0

    def zero_warning(self):
        """
            ListOfErrorMessages.zero_warning()

            Return True if <self> doesn't contain any error.


            __________________________________________________________________

            RETURNED VALUE : (bool)
        """
        # ew_object : EW_like object
        for ew_object in self:
            if ew_object.level == LEVEL_WARNING:
                return False
        return True


class ListOfErrorMessagesSer(ListOfErrorMessages, Iaswn):
    """
        ListOfErrorMessagesSer class

        = ListOfErrorMessages + Iaswn
    """


@dataclass
class EW:
    """
        EW class

        (internal class) mother-class of all error classes

        The user doesn't normally has to create EW objects.


        _______________________________________________________________________

        ATTRIBUTES:
        o  (str)msgid
        o  (str)msg
        o  (int)level
        o  (None or list)suberrors

        METHODS:
        o  __str__(self, depth=0)
        o  improved_str(self, depth=0)
        o  str_word_suberrors(suberrors_nbr)
    """
    msgid: str = ""
    msg: str = ""
    level: int = LEVEL_ERROR
    suberrors: list = field(default_factory=list)

    def __str__(self,
                depth=0):
        """
            EW.__str__()


            ___________________________________________________________________

            ARGUMENT:
            o  depth: (int)level of depth for suberrors
                      0 is the first level (no suberrors)
                      1 is the second level (suberrors of an error)
                      2 is the third level (suberrors of suberrors of an error)
                      ...
        """
        res = ""

        if self.level == LEVEL_WARNING:
            res = f"#({self.msgid}){self.msg}"
        else:
            res = f"#({self.msgid}){self.msg}"

        if self.suberrors:
            res += "\n"+("  "*(depth+1))+self.str_word_suberrors(len(self.suberrors))+":\n"
            for index, suberror in enumerate(self.suberrors):
                res += (("  "*(depth+1)))+"* "+suberror.__str__(depth=depth+1)
                if index != len(self.suberrors)-1:
                    res += ";\n"

        return res

    def improved_str(self,
                     depth=0):
        """
            EW.improved_str()

            Return a nice representation of <self>, using colorized output.


            __________________________________________________________________

            ARGUMENT:
            o  depth: (int)level of depth for suberrors
                      0 is the first level (no suberrors)
                      1 is the second level (suberrors of an error)
                      2 is the third level (suberrors of suberrors of an error)
                      ...

            RETURNED VALUE : (str)a nice representation of <self>.
        """
        res = ""

        if self.level == LEVEL_WARNING:
            res = f"[blue]#({self.msgid})[/blue][yellow]{self.msg}[/yellow]"
        else:
            res = "[bold][red]#" \
                f"({self.msgid})[/red][/bold][yellow]{self.msg}[/yellow]"

        if self.suberrors:
            res += "\n"+("  "*(depth+1))+self.str_word_suberrors(len(self.suberrors))+":\n"
            for index, suberror in enumerate(self.suberrors):
                res += (("  "*(depth+1)))+"* "+suberror.improved_str(depth=depth+1)
                if index != len(self.suberrors)-1:
                    res += ";\n"

        return res

    @staticmethod
    def str_word_suberrors(suberrors_nbr):
        """
            EW.str_word_suberrors()

            Return either "Suberror" either "Suberrors" along the value of <suberrors_nbr>.


            __________________________________________________________________

            ARGUMENT:
            o  suberrors_nbr: (int)1 or more, number of suberrors to be printed.

            RETURNED VALUE : (str)"Suberror" or "Suberrors"
        """
        return "Suberror" if suberrors_nbr == 1 else "Suberrors"


@dataclass
class Error(EW):
    """
        Error class

        Use this class to create simple errors to be added to a
        ListOfErrorMessages object.


        _______________________________________________________________________

        ATTRIBUTES:
        o  (str)msgid         (inherited from EW)
        o  (str)msg           (inherited from EW)
        o  (int)level         (inherited from EW)

        METHODS:
        o  __str__(self, depth=0)      (inherited from EW)
        o  improved_str(self, depth=0) (inherited from EW)
    """
    level: int = LEVEL_ERROR


class ErrorSer(Error, Iaswn):
    """
        ErrorSer class

        Error + Iaswn
    """


@dataclass
class Warn(EW):
    """
        Warn class

        Use this class to create simple warnings to be added to a
        ListOfErrorMessages object.


        _______________________________________________________________________

        ATTRIBUTES:
        o  (str)msgid         (inherited from EW)
        o  (str)msg           (inherited from EW)
        o  (int)level         (inherited from EW)

        METHODS:
        o  __str__(self, depth=0)      (inherited from EW)
        o  improved_str(self, depth=0) (inherited from EW)
    """
    level: int = LEVEL_WARNING


class WarnSer(Warn, Iaswn):
    """
        WarnSer class

        Warn + Iaswn
    """


@dataclass
class TextFileEW(EW):
    """
        TextFileEW class

        class dedicated to errors appearing while dealing with a text file.


        _______________________________________________________________________

        ATTRIBUTES:
        o  .fals, None or a tuple of FileAndLine objects
        o  (str)msgid         (inherited from EW)
        o  (str)msg           (inherited from EW)
        o  (int)level         (inherited from EW)

        METHODS:
        o  __str__(self, depth=0)      (inherited from EW)
        o  iaswn_postprocessing(self)
        o  iaswn_preprocessing(self)
        o  improved_str(self, depth=0)
    """
    fals: tuple = field(default_factory=tuple)  # a tuple of FileAndLine objects

    def __str__(self,
                depth=0):
        """
            TextFileEW.__str__()

            ARGUMENT:
            o  depth: (int)level of depth for suberrors
                      0 is the first level (no suberrors)
                      1 is the second level (suberrors of an error)
                      2 is the third level (suberrors of suberrors of an error)
                      ...

            RETURNED VALUE: (str)a representation of <self>.
        """
        return EW.__str__(self)+"; fals="+str(self.fals)

    def improved_str(self,
                     depth=0):
        """
            TextFileEW.improved_str()

            Return a nice representation of <self>, using colorized output.


            __________________________________________________________________

            ARGUMENT:
            o  depth: (int)level of depth for suberrors
                      0 is the first level (no suberrors)
                      1 is the second level (suberrors of an error)
                      2 is the third level (suberrors of suberrors of an error)
                      ...

            RETURNED VALUE : (str)a nice representation of <self>.
        """
        if self.level == LEVEL_WARNING:
            res = f"[blue]#({self.msgid})[/blue][yellow]{self.msg}[/yellow]"
        else:
            res = f"[red]#({self.msgid})[/red][yellow]{self.msg}[/yellow]"

        if self.fals is None:
            res += "(no fal information)"
        else:
            for fal in self.fals:
                res += f"([green]{fal.filename}[/green], [yellow]line " \
                       f"#{fal.lineindex}[/yellow]); "

        if self.suberrors:
            res += "\n"+("  "*(depth+1))+self.str_word_suberrors(len(self.suberrors))+":\n"
            for index, suberror in enumerate(self.suberrors):
                res += (("  "*(depth+1)))+"* "+suberror.improved_str(depth=depth+1)
                if index != len(self.suberrors)-1:
                    res += ";\n"

        return res


@dataclass
class TextFileError(TextFileEW):
    """
        TextFileError class

        Use this class to create errors about text files to be added to a
        ListOfErrorMessages object.


        _______________________________________________________________________

        ATTRIBUTES:
        o  (FileAndLine tuple)fals (inherited from TextFileEW)
        o  (str)msgid              (inherited from EW)
        o  (str)msg                (inherited from EW)
        o  (int)level              (inherited from EW)

        METHODS:
        o  __str__(self, depth=0)      (inherited from EW)
        o  improved_str(self, depth=0) (inherited from EW)
    """
    level: int = LEVEL_ERROR


class TextFileErrorSer(TextFileError, Iaswn):
    """
        TextFileErrorSer class

        TextFileError + Iaswn
    """


@dataclass
class TextFileWarn(TextFileEW):
    """
        TextFileWarn class

        Use this class to create warnings about text files to be added to a
        ListOfErrorMessages object.


        _______________________________________________________________________

        ATTRIBUTES:
        o  (FileAndLine tuple)fals (inherited from TextFileEW)
        o  (str)msgid              (inherited from EW)
        o  (str)msg                (inherited from EW)
        o  (int)level              (inherited from EW)

        METHODS:
        o  __str__(self, depth=0)      (inherited from EW)
        o  improved_str(self, depth=0) (inherited from EW)
    """
    level: int = LEVEL_WARNING


class TextFileWarnSer(TextFileWarn, Iaswn):
    """
        TextFileWarnSer class

        TextFileWarn + Iaswn
    """
