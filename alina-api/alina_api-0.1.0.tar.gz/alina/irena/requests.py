from requests import Request

from alina.irena.parsers.responses import (
    IrenaAllocationTimetableRequestResponseParser, IrenaAllocationIDRequestResponseParser,
    IrenaAllocationDetailsRequestResponseParser, IrenaRequestResponseParser, IrenaTripCrewMembersRequestResponseParser
)
from alina.tools import DateExpressionPatternError, TextExpressionPatternError
from alina.tools.expressions import date_pattern, text_pattern


class IrenaRequest(Request):
    """Uses super() function to call the parent's constructor with the headers argument
    and then passing in all of its arguments as well.
    Init sets default values for itself by setting up an Accept-Language header with 'pl-PL' and an Accept-Encoding
    header with gzip, deflate.
    """
    parser: IrenaRequestResponseParser

    def __init__(self, *args, **kwargs):
        headers = {
            'Accept-Language': 'pl-PL',
            'Accept-Encoding': 'gzip, deflate',
        }
        super().__init__(headers=headers, *args, **kwargs)


class IrenaDateableRequest(IrenaRequest):
    """Create a class that is able to parse dates.
    It starts by checking if the date has a pattern in it, and then if not, it raises an error.
    """
    def __init__(self, date, *args, **kwargs):
        if not date_pattern.match(date):
            raise DateExpressionPatternError(date)
        super().__init__(*args, **kwargs)


class IrenaTitledRequest(IrenaRequest):
    """Create a class that is able to parse strings.
    It starts by checking if the string has a pattern in it (in this case word like pattern),
    and then if not, it raises an error.
    """
    def __init__(self, text, *args, **kwargs):
        if not text_pattern.match(text):
            raise TextExpressionPatternError(text)
        super().__init__(*args, **kwargs)


class IrenaAllocationTimetableRequest(IrenaDateableRequest):
    parser = IrenaAllocationTimetableRequestResponseParser

    def __init__(self, date):
        url = f'https://irena1.intercity.pl/mbweb/main/matter/desktop/_-duty-table?beginDate={date}'
        super().__init__(date=date, method='GET', url=url)


class IrenaAllocationIDRequest(IrenaTitledRequest, IrenaDateableRequest):
    parser = IrenaAllocationIDRequestResponseParser

    def __init__(self, text, date):
        url = (f'https://irena1.intercity.pl/mbweb/main/ivu/desktop/'
               f'_-any-duty-table?division=&depot=&abbreviation={text}&date={date}&')
        super().__init__(text=text, date=date, method='GET', url=url)


class IrenaAllocationDetailsRequest(IrenaTitledRequest, IrenaDateableRequest):
    parser = IrenaAllocationDetailsRequestResponseParser

    def __init__(self, id, date):
        url = (f'https://irena1.intercity.pl/mbweb/main/ivu/desktop/any-duty-details?id={id}&beginDate={date}&')
        super().__init__(text=id, date=date, method='GET', url=url)


class IrenaTripCrewMembersRequest(IrenaTitledRequest, IrenaDateableRequest):
    parser = IrenaTripCrewMembersRequestResponseParser

    def __init__(self, number, date):
        url = (f'https://irena1.intercity.pl/mbweb/main/matter/desktop/'
               f'_-crew-on-trip-table?tripNumber={number}&beginDate={date}&')
        super().__init__(text=number, date=date, method='GET', url=url)