from teradatasqlalchemy import (BYTEINT, SMALLINT, INTEGER, BIGINT, DECIMAL, FLOAT, NUMBER)
from teradatasqlalchemy import (TIMESTAMP, DATE, TIME)
from teradatasqlalchemy import (CHAR, VARCHAR, CLOB)
from teradatasqlalchemy import (BYTE, VARBYTE, BLOB)
from teradatasqlalchemy import (PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP)
from teradatasqlalchemy import (INTERVAL_YEAR, INTERVAL_YEAR_TO_MONTH, INTERVAL_MONTH, INTERVAL_DAY,
                                INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE, INTERVAL_DAY_TO_SECOND,
                                INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                                INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_SECOND)
from teradataml.common.constants import TeradataTypes, PythonTypes
from datetime import datetime, time, date

# DataTypes mapper to store various categories of DataTypes.
_GET_DATATYPES = {
    'NON_NUMERIC': [BLOB, BYTE, CHAR, CLOB, DATE, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE,
                    INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                    INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_MONTH, INTERVAL_SECOND, INTERVAL_YEAR,
                    INTERVAL_YEAR_TO_MONTH, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARCHAR]
}


class _DtypesMappers:
    AGGREGATE_UNSUPPORTED_TYPES = {
        'avg': [BLOB, BYTE, CHAR, CLOB, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARBYTE, VARCHAR],
        'mavg': [BLOB, BYTE, CHAR, CLOB, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARBYTE, VARCHAR],
        'bottom': [BLOB, BYTE, CHAR, CLOB, DATE, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE,
                   INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                   INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_MONTH, INTERVAL_SECOND, INTERVAL_YEAR,
                   INTERVAL_YEAR_TO_MONTH, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIMESTAMP, TIME, TIMESTAMP,
                   VARBYTE, VARCHAR],
        'bottom with ties': [BLOB, BYTE, CHAR, CLOB, DATE, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE,
                             INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                             INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_MONTH, INTERVAL_SECOND, INTERVAL_YEAR,
                             INTERVAL_YEAR_TO_MONTH, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIMESTAMP, TIME,
                             TIMESTAMP, VARBYTE, VARCHAR],
        'count': [],
        'first': [BLOB, BYTE, CHAR, CLOB, DATE, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE,
                  INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                  INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_MONTH, INTERVAL_SECOND, INTERVAL_YEAR,
                  INTERVAL_YEAR_TO_MONTH, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIMESTAMP, TIME, TIMESTAMP,
                  VARBYTE, VARCHAR],
        'kurtosis': [BLOB, BYTE, CHAR, CLOB, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARBYTE,
                     VARCHAR],
        'last': [BLOB, BYTE, CHAR, CLOB, DATE, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE,
                 INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                 INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_MONTH, INTERVAL_SECOND, INTERVAL_YEAR,
                 INTERVAL_YEAR_TO_MONTH, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIMESTAMP, TIME, TIMESTAMP,
                 VARBYTE, VARCHAR],
        'mad': [BLOB, BYTE, CHAR, CLOB, DATE, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE,
                INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_MONTH, INTERVAL_SECOND, INTERVAL_YEAR,
                INTERVAL_YEAR_TO_MONTH, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIMESTAMP, TIME, TIMESTAMP, VARBYTE,
                VARCHAR],
        'max': [BLOB, CLOB, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP],
        'mean': [BLOB, BYTE, CHAR, CLOB, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARBYTE, VARCHAR],
        'median': [BLOB, BYTE, CHAR, CLOB, DATE, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE,
                   INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                   INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_MONTH, INTERVAL_SECOND, INTERVAL_YEAR,
                   INTERVAL_YEAR_TO_MONTH, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIMESTAMP, TIME, TIMESTAMP,
                   VARBYTE, VARCHAR],
        'min': [BLOB, CLOB, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP],
        'mode': [BLOB, BYTE, CHAR, CLOB, DATE, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE,
                 INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                 INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_MONTH, INTERVAL_SECOND, INTERVAL_YEAR,
                 INTERVAL_YEAR_TO_MONTH, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIMESTAMP, TIME, TIMESTAMP,
                 VARBYTE, VARCHAR],
        'percentile': [BLOB, BYTE, CHAR, CLOB, DATE, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE,
                       INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                       INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_MONTH, INTERVAL_SECOND, INTERVAL_YEAR,
                       INTERVAL_YEAR_TO_MONTH, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIMESTAMP, TIME, TIMESTAMP,
                       VARBYTE, VARCHAR],
        'percentile_cont': [BLOB, BYTE, CHAR, CLOB, DATE, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE,
                            INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                            INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_MONTH, INTERVAL_SECOND, INTERVAL_YEAR,
                            INTERVAL_YEAR_TO_MONTH, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIMESTAMP, TIME, TIMESTAMP,
                            VARBYTE, VARCHAR],
        'percentile_disc': [BLOB, BYTE, CHAR, CLOB, DATE, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE,
                            INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                            INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_MONTH, INTERVAL_SECOND, INTERVAL_YEAR,
                            INTERVAL_YEAR_TO_MONTH, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIMESTAMP, TIME, TIMESTAMP,
                            VARBYTE, VARCHAR],
        'skew': [BLOB, BYTE, CHAR, CLOB, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARBYTE,
                 VARCHAR],
        'sum': [BLOB, BYTE, CHAR, CLOB, DATE, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARBYTE,
                VARCHAR],
        'csum': [BLOB, BYTE, CHAR, CLOB, DATE, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARBYTE,
                 VARCHAR],
        'msum': [BLOB, BYTE, CHAR, CLOB, DATE, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARBYTE,
                 VARCHAR],
        'mdiff': [BLOB, BYTE, CHAR, CLOB, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARBYTE,
                 VARCHAR],
        'mlinreg': [BLOB, BYTE, CHAR, CLOB, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARBYTE,
                 VARCHAR],
        'std': [BLOB, BYTE, CHAR, CLOB, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARBYTE, VARCHAR],
        'stddev_pop': [BLOB, BYTE, CHAR, CLOB, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP,
                       VARBYTE, VARCHAR],
        'stddev_samp': [BLOB, BYTE, CHAR, CLOB, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARBYTE,
                        VARCHAR],
        'top': [BLOB, BYTE, CHAR, CLOB, DATE, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE,
                INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_MONTH, INTERVAL_SECOND, INTERVAL_YEAR,
                INTERVAL_YEAR_TO_MONTH, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIMESTAMP, TIME, TIMESTAMP, VARBYTE,
                VARCHAR],
        'top with ties': [BLOB, BYTE, CHAR, CLOB, DATE, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE,
                          INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                          INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_MONTH, INTERVAL_SECOND, INTERVAL_YEAR,
                          INTERVAL_YEAR_TO_MONTH, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIMESTAMP, TIME,
                          TIMESTAMP, VARBYTE, VARCHAR],
        'unique': [],
        'var': [BLOB, BYTE, CHAR, CLOB, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARBYTE, VARCHAR],
        'var_pop': [BLOB, BYTE, CHAR, CLOB, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARBYTE,
                    VARCHAR],
        'var_samp': [BLOB, BYTE, CHAR, CLOB, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARBYTE,
                     VARCHAR],
        'corr': _GET_DATATYPES["NON_NUMERIC"],
        'regr_avgx': _GET_DATATYPES["NON_NUMERIC"],
        'regr_avgy': _GET_DATATYPES["NON_NUMERIC"],
        'regr_count': _GET_DATATYPES["NON_NUMERIC"],
        'regr_intercept': _GET_DATATYPES["NON_NUMERIC"],
        'regr_r2': _GET_DATATYPES["NON_NUMERIC"],
        'regr_slope': _GET_DATATYPES["NON_NUMERIC"],
        'regr_sxx': _GET_DATATYPES["NON_NUMERIC"],
        'regr_sxy': _GET_DATATYPES["NON_NUMERIC"],
        'regr_syy': _GET_DATATYPES["NON_NUMERIC"],
        'covar_pop': _GET_DATATYPES["NON_NUMERIC"],
        'covar_samp': _GET_DATATYPES["NON_NUMERIC"]
    }

    WINDOW_AGGREGATE_UNSUPPORTED_TYPES = {
        'count': [PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP],
        'max': [BYTE, VARBYTE, BLOB, CLOB, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP]
    }

    DESCRIBE_AGGREGATE_UNSUPPORTED_TYPES = {
        'bottom': [BLOB, BYTE, CHAR, CLOB, DATE, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE,
                   INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                   INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_MONTH, INTERVAL_SECOND, INTERVAL_YEAR,
                   INTERVAL_YEAR_TO_MONTH, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIMESTAMP, TIME, TIMESTAMP,
                   VARBYTE, VARCHAR],
        'bottom with ties': [BLOB, BYTE, CHAR, CLOB, DATE, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE,
                             INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                             INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_MONTH, INTERVAL_SECOND, INTERVAL_YEAR,
                             INTERVAL_YEAR_TO_MONTH, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIMESTAMP, TIME,
                             TIMESTAMP, VARBYTE, VARCHAR],
        'count': [],
        'first': [BLOB, BYTE, CHAR, CLOB, DATE, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE,
                  INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                  INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_MONTH, INTERVAL_SECOND, INTERVAL_YEAR,
                  INTERVAL_YEAR_TO_MONTH, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIMESTAMP, TIME, TIMESTAMP,
                  VARBYTE, VARCHAR],
        'last': [BLOB, BYTE, CHAR, CLOB, DATE, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE,
                 INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                 INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_MONTH, INTERVAL_SECOND, INTERVAL_YEAR,
                 INTERVAL_YEAR_TO_MONTH, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIMESTAMP, TIME, TIMESTAMP,
                 VARBYTE, VARCHAR],
        'mad': [BLOB, BYTE, CHAR, CLOB, DATE, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE,
                INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_MONTH, INTERVAL_SECOND, INTERVAL_YEAR,
                INTERVAL_YEAR_TO_MONTH, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIMESTAMP, TIME, TIMESTAMP, VARBYTE,
                VARCHAR],
        'max': [BLOB, BYTE, CHAR, CLOB, DATE, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARBYTE,
                VARCHAR],
        'mean': [BLOB, BYTE, CHAR, CLOB, DATE, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARBYTE,
                 VARCHAR],
        'avg': [BLOB, BYTE, CHAR, CLOB, DATE, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARBYTE,
                VARCHAR],
        'median': [BLOB, BYTE, CHAR, CLOB, DATE, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE,
                   INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                   INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_MONTH, INTERVAL_SECOND, INTERVAL_YEAR,
                   INTERVAL_YEAR_TO_MONTH, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIMESTAMP, TIME, TIMESTAMP,
                   VARBYTE, VARCHAR],
        'min': [BLOB, BYTE, CHAR, CLOB, DATE, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARBYTE,
                VARCHAR],
        'mode': [BLOB, BYTE, CHAR, CLOB, DATE, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE,
                 INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                 INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_MONTH, INTERVAL_SECOND, INTERVAL_YEAR,
                 INTERVAL_YEAR_TO_MONTH, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIMESTAMP, TIME, TIMESTAMP,
                 VARBYTE, VARCHAR],
        'percentile_cont': [BLOB, BYTE, CHAR, CLOB, DATE, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP,
                            VARBYTE, VARCHAR],
        'percentile': [BLOB, BYTE, CHAR, CLOB, DATE, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP,
                       VARBYTE, VARCHAR],
        'std': [BLOB, BYTE, CHAR, CLOB, DATE, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARBYTE,
                VARCHAR],
        'stddev_samp': [BLOB, BYTE, CHAR, CLOB, DATE, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP,
                        VARBYTE, VARCHAR],
        'sum': [BLOB, BYTE, CHAR, CLOB, DATE, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARBYTE,
                VARCHAR],
        'top': [BLOB, BYTE, CHAR, CLOB, DATE, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE,
                INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_MONTH, INTERVAL_SECOND, INTERVAL_YEAR,
                INTERVAL_YEAR_TO_MONTH, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIMESTAMP, TIME, TIMESTAMP, VARBYTE,
                VARCHAR],
        'top with ties': [BLOB, BYTE, CHAR, CLOB, DATE, INTERVAL_DAY, INTERVAL_DAY_TO_HOUR, INTERVAL_DAY_TO_MINUTE,
                          INTERVAL_DAY_TO_SECOND, INTERVAL_HOUR, INTERVAL_HOUR_TO_MINUTE, INTERVAL_HOUR_TO_SECOND,
                          INTERVAL_MINUTE, INTERVAL_MINUTE_TO_SECOND, INTERVAL_MONTH, INTERVAL_SECOND, INTERVAL_YEAR,
                          INTERVAL_YEAR_TO_MONTH, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIMESTAMP, TIME,
                          TIMESTAMP, VARBYTE, VARCHAR],
        'unique': [BYTEINT, SMALLINT, INTEGER, BIGINT, DECIMAL, FLOAT, NUMBER]
    }
    PY_TD_MAPPER = {int: INTEGER,
                    float: FLOAT,
                    str: VARCHAR(1024),
                    bool: BYTEINT,
                    datetime: TIMESTAMP,
                    date: DATE,
                    time: TIME
                    }

    TDSQLALCHEMY_DATATYPE_TO_VAL_STRING_MAPPER = {
        BIGINT: lambda x: x.__class__.__name__,
        BYTEINT: lambda x: x.__class__.__name__,
        CHAR: lambda x: "{0},{1}".format(x.__class__.__name__, x.length),
        DATE: lambda x: x.__class__.__name__,
        DECIMAL: lambda x: "{0},{1},{2}".format(x.__class__.__name__, x.precision, x.scale),
        FLOAT: lambda x: x.__class__.__name__,
        NUMBER: lambda x: ','.join(map(str, (filter(None, [x.__class__.__name__, x.precision, x.scale])))),
        INTEGER: lambda x: x.__class__.__name__,
        SMALLINT: lambda x: x.__class__.__name__,
        TIME: lambda x: "{0},{1}".format(x.__class__.__name__, x.precision),
        TIMESTAMP: lambda x: "{0},{1}".format(x.__class__.__name__, x.precision),
        VARCHAR: lambda x: "{0},{1}".format(x.__class__.__name__, x.length)
    }

class _SuppArgTypes:
    VAL_ARG_DATATYPE = (str, BIGINT, BYTEINT, CHAR, DATE, DECIMAL, FLOAT, INTEGER, NUMBER, SMALLINT, TIME,
                        TIMESTAMP, VARCHAR)

class _Dtypes:

    @staticmethod
    def _get_numeric_datatypes():
        """
        Returns the numeric data types used in Teradata Vantage
        **From : https://www.info.teradata.com/HTMLPubs/DB_TTU_16_00/
        index.html#page/General_Reference/B035-1091-160K/psa1472241434371.html

        PARAMETERS:
            None

        RAISES:
            None

        RETURNS:
            List of numeric data types used in Teradata Vantage
        """
        return [BYTEINT, SMALLINT, INTEGER, BIGINT, DECIMAL, FLOAT, NUMBER]

    @staticmethod
    def _get_timedate_datatypes():
        """
        Returns a list of TimeDate data types.

        PARAMETERS:
            None

        RAISES:
            None

        RETURNS:
            List of TimeDate data types used in Teradata Vantage
        """
        return [TIMESTAMP, DATE, TIME]

    @staticmethod
    def _get_character_datatypes():
        """
        Returns a list of Character data types.

        PARAMETERS:
            None

        RAISES:
            None

        RETURNS:
            List of Character data types used in Teradata Vantage
        """
        return [CHAR, VARCHAR, CLOB]

    @staticmethod
    def _get_byte_datatypes():
        """
        Returns a list of byte like data types.

        PARAMETERS:
            None

        RAISES:
            None

        RETURNS:
            List of Byte data types used in Teradata Vantage
        """
        return [BYTE, VARBYTE, BLOB]

    @staticmethod
    def _get_categorical_datatypes():
        """
        Returns a list of containing Character and TimeDate data types.

        PARAMETERS:
            None

        RAISES:
            None

        RETURNS:
            List of Character and TimeDate data types used in Teradata Vantage
        """
        return list.__add__(_Dtypes._get_character_datatypes(), _Dtypes._get_timedate_datatypes())

    @staticmethod
    def _get_all_datatypes():
        """
        Returns a list of Character, Numeric and TimeDate data types.

        PARAMETERS:
            None

        RAISES:
            None

        RETURNS:
            List of Character, Numeric and TimeDate data types used in Teradata Vantage
        """
        return list.__add__(_Dtypes._get_categorical_datatypes(), _Dtypes._get_numeric_datatypes())

    @staticmethod
    def _get_unsupported_data_types_for_aggregate_operations(operation,
                                                             as_time_series_aggregate=False,
                                                             is_window_aggregate=False):
        """
        Returns the data types on which aggregate operations cannot
        be performed eg : min, max, avg

        PARAMETERS:
            operation:
                Required Argument.
                Specifies an aggregate operation to be performed on the dataframe.
                Types: str

            as_time_series_aggregate:
                Optional Argument.
                Specifies whether aggregate operation is a Time Series aggregate or not.
                Default Values: False
                Types: bool

            is_window_aggregate:
                Optional Argument.
                Specifies whether aggregate operation is a Window aggregate or not.
                Default Values: False
                Types: bool

        RAISES:
            None

        RETURNS:
            List of unsupported data types for aggregate operation in
            Teradata Vantage eg : min, max, avg
        """
        if operation == 'median' and not as_time_series_aggregate:
            # For median as regular aggregate unsupported types are different than the ones
            # mentioned in _DtypesMappers.AGGREGATE_UNSUPPORTED_TYPES
            return [BLOB, BYTE, CHAR, CLOB, DATE, PERIOD_DATE, PERIOD_TIME, PERIOD_TIMESTAMP, TIME, TIMESTAMP, VARCHAR]

        # Return the unsupported types list, if key with 'operation' is found.
        # If 'operation' is not found, return empty list which means all types
        # are supported.
        if is_window_aggregate:
            # If operation is not present in WINDOW_AGGREGATE_UNSUPPORTED_TYPES
            # then return the value from the AGGREGATE_UNSUPPORTED_TYPES mapper.
            return _DtypesMappers.WINDOW_AGGREGATE_UNSUPPORTED_TYPES.get(operation,
                    _DtypesMappers.AGGREGATE_UNSUPPORTED_TYPES.get(operation, []))
        return _DtypesMappers.AGGREGATE_UNSUPPORTED_TYPES.get(operation, [])

    @staticmethod
    def _get_unsupported_data_types_for_describe_operations(operation):
        """
        Returns the data types on which the specified describe aggregate 'operation' cannot
        be performed. This function is used by the method DataFrame.describe().

        PARAMETERS:
            operation : String. An aggregate operation to be performed on the dataframe.
                        possible values are 'sum', 'min', 'max', 'mean','std', 'percentile',
                        'count', and 'unique'.

        RAISES:
            None

        RETURNS:
            List of unsupported data types for describe operation in
            Teradata Vantage eg : min, max, avg
        """
        try:
            # Return the unsupported types list, if key with operation 'operation' is found.
            return _DtypesMappers.DESCRIBE_AGGREGATE_UNSUPPORTED_TYPES[operation]
        except KeyError:
            # We are here means, there are not unsupported types mentioned in
            # _DtypesMappers.DESCRIBE_AGGREGATE_UNSUPPORTED_TYPES, so that means all types are supported.
            return []

    @staticmethod
    def _get_sort_unsupported_data_types():
        """
        Returns the data types on which sorting is invalid.

        RAISES:
            None

        RETURNS:
            list of teradatasqlalchemy.types

        EXAMPLES:
            _Dtypes._get_sort_unsupported_data_types()
        """
        return [CLOB, BLOB]

    @staticmethod
    def _teradata_type_to_python_type(td_type):
        """
        Translate the Teradata type from metaexpr to Python types.
        PARAMETERS:
            td_type - The Teradata type from metaexpr.

        RETURNS:
            The Python type for the given td_type.

        RAISES:

        EXAMPLES:
            # o is an instance of INTEGER
            pytype = _Dtypes._teradata_type_to_python_type(o)

        """

        # loggerlogger.debug("_help_col_to_python_type td_type = {0} ".format(td_type))
        if type(td_type) in TeradataTypes.TD_INTEGER_TYPES:
            return PythonTypes.PY_INT_TYPE
        elif type(td_type) in TeradataTypes.TD_FLOAT_TYPES:
            return PythonTypes.PY_FLOAT_TYPE
        elif type(td_type) in TeradataTypes.TD_DECIMAL_TYPES:
            return PythonTypes.PY_DECIMAL_TYPE
        elif type(td_type) in TeradataTypes.TD_BYTE_TYPES:
            return PythonTypes.PY_BYTES_TYPE
        elif type(td_type) in TeradataTypes.TD_DATETIME_TYPES:
            return PythonTypes.PY_DATETIME_TYPE
        elif type(td_type) in TeradataTypes.TD_TIME_TYPES:
            return PythonTypes.PY_TIME_TYPE
        elif type(td_type) in TeradataTypes.TD_DATE_TYPES:
            return PythonTypes.PY_DATE_TYPE

        return PythonTypes.PY_STRING_TYPE

    @staticmethod
    def _python_type_to_teradata_type(py_type):
        """
        DESCRIPTION:
            Translate the Python types to Teradata type.

        PARAMETERS:
            py_type:
               Required Argument.
               Specifies the Python type.
               Types: type

        RETURNS:
            The teradatasqlalchemy type for the given py_type.

        RAISES:
            None

        EXAMPLES:
            tdtype = _Dtypes._python_type_to_teradata_type(int)

        """

        return _DtypesMappers.PY_TD_MAPPER.get(py_type)

    @staticmethod
    def _help_col_to_python_type(col_type, storage_format):
        """
        Translate the 1 or 2 character TD type codes from HELP COLUMN to Python types.
        PARAMETERS:
            col_type - The 1 or 2 character type code from HELP COLUMN command.
            storage_format - The storage format from HELP COLUMN command.

        RETURNS:
            The Python type for the given col_type.

        RAISES:

        EXAMPLES:
            pytype = _Dtypes._help_col_to_python_type('CV', None)
            pytype = _Dtypes._help_col_to_python_type('DT', 'CSV')

        """
        if col_type in TeradataTypes.TD_INTEGER_CODES:
            return PythonTypes.PY_INT_TYPE
        elif col_type in TeradataTypes.TD_FLOAT_CODES:
            return PythonTypes.PY_FLOAT_TYPE
        elif col_type in TeradataTypes.TD_DECIMAL_CODES:
            return PythonTypes.PY_DECIMAL_TYPE
        elif col_type in TeradataTypes.TD_BYTE_CODES:
            return PythonTypes.PY_BYTES_TYPE
        elif col_type in TeradataTypes.TD_DATETIME_CODES:
            return PythonTypes.PY_DATETIME_TYPE
        elif col_type in TeradataTypes.TD_TIME_CODES:
            return PythonTypes.PY_TIME_TYPE
        elif col_type in TeradataTypes.TD_DATE_CODES:
            return PythonTypes.PY_DATE_TYPE
        elif col_type == "DT":
            sfmt = storage_format.strip()
            if sfmt == "CSV":
                return PythonTypes.PY_STRING_TYPE
            elif sfmt == "AVRO":
                return PythonTypes.PY_BYTES_TYPE

        return PythonTypes.PY_STRING_TYPE

    @staticmethod
    def _help_col_to_td_type(col_type, udt_name, storage_format):
        """
        Translate the 2 character TD type codes from HELP COLUMN to Teradata types.
        PARAMETERS:
            col_type - The 2 character type code from HELP COLUMN command.
            udt_name - The UDT name from the HELP COLUMN command.
            storage_format - The storage format from HELP COLUMN command.

        RETURNS:
            The Teradata type for the given colType.

        RAISES:

        EXAMPLES:
            tdtype = _Dtypes._help_col_to_td_type('CV', None, None)

        """
        # logger.debug("helpColumnToTeradataTypeName colType = {0} udtName = {1} storageFormat {2}".format(colType, udtName, storageFormat))
        if col_type in DataTypeMapper.HELP_COL_TYPE_TO_TDTYPE.value:
            return DataTypeMapper.HELP_COL_TYPE_TO_TDTYPE.value[col_type]

        if col_type == "DT":
            return "DATASET STORAGE FORMAT {0}".format(storage_format.strip())

        if col_type in ["UD", "US", "UT", "A1", "AN"]:
            if udt_name:
                return udt_name

        return col_type
