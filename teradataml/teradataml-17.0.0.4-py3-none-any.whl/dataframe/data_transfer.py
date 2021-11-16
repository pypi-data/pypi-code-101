#!/usr/bin/python
# ##################################################################
#
# Copyright 2021 Teradata. All rights reserved.
# TERADATA CONFIDENTIAL AND TRADE SECRET
#
# Primary Owner: Sanath Vobilisetty (Sanath.Vobilisetty@teradata.com)
# Secondary Owner: Pankaj Vinod Purandare (PankajVinod.Purandare@Teradata.com)
#
# ##################################################################

from teradataml.context.context import get_context, get_connection
from teradataml.utils.validators import _Validators
from teradataml.common.exceptions import TeradataMlException
from teradataml.common.messages import Messages
from teradataml.common.messagecodes import MessageCodes
from teradataml.common.sqlbundle import SQLBundle
from teradataml.common.utils import UtilFuncs
import pandas as pd

def fastexport(df, export_to="pandas", index_column=None,
               catch_errors_warnings=False, **kwargs):
    """
    DESCRIPTION:
        The fastexport() API exports teradataml DataFrame to Pandas DataFrame
        using FastExport data transfer protocol.
        Note:
            1. Teradata recommends to use FastExport when number of rows in
               teradataml DataFrame are at least 100,000. To extract lesser rows
               ignore this function and go with regular to_pandas() function.
               FastExport opens multiple data transfer connections to the
               database.
            2. FastExport does not support all Teradata Database data types.
               For example, tables with BLOB and CLOB type columns cannot
               be extracted.
            3. FastExport cannot be used to extract data from a volatile or
               temporary table.
            4. For best efficiency, do not use DataFrame.groupby() and
               DataFrame.sort() with FastExport.

        For additional information about FastExport protocol through
        teradatasql driver, please refer to FASTEXPORT section of
        https://pypi.org/project/teradatasql/#FastExport driver documentation.

    PARAMETERS:
        df:
            Required Argument.
            Specifies teradataml DataFrame that needs to be exported.
            Type: teradataml DataFrame.

        export_to:
            Optional Argument.
            Specifies a value that notifies where to export the data.
            Permitted Values:
                * "pandas": Export data to a Pandas DataFrame.
            Default Value: "pandas".
            Type: str.

        index_column:
            Optional Argument.
            Specifies column(s) to be used as index column for the converted
            object.
            Default Value: None.
            Types: str OR list of Strings (str).

        catch_errors_warnings:
            Optional Argument.
            Specifies whether to catch errors/warnings(if any) raised by
            fastexport protocol while converting teradataml DataFrame.
            When this and "to_pandas" arguments are set to True,
            fastexport() returns a tuple containing:
                a. Pandas DataFrame.
                b. Errors(if any) in a list thrown by fastexport.
                c. Warnings(if any) in a list thrown by fastexport.
            When set to False, prints the fastexport errors/warnings to the
            standard output, if there are any.
            Default Value: False.
            Types: bool.

        kwargs:
            Optional Argument.
            Specifies keyword arguments. Arguments "coerce_float" and
            "parse_dates" can be passed as keyword arguments.
                * "coerce_float" specifies whether to convert non-string,
                  non-numeric objects to floating point.
                * "parse_dates" specifies columns to parse as dates.
            Note:
                For additional information about "coerce_float" and
                "parse_date" arguments please refer to:
                https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html

    RETURNS:
        When "to_pandas" and "catch_errors_warnings" are set to True, then the
        function returns a tuple containing:
            a. Pandas DataFrame.
            b. Errors, if any, thrown by fastexport in a list of strings.
            c. Warnings, if any, thrown by fastexport in a list of strings.
        When "to_pandas" is True and "catch_errors_warnings" is False, then the
        function returns a Pandas DataFrame.

    EXAMPLES:
        >>> from teradataml import *
        >>> load_example_data("dataframe", "admissions_train")
        >>> df = DataFrame("admissions_train")

        # Print dataframe.
        >>> df
              masters   gpa     stats programming admitted
           id
           13      no  4.00  Advanced      Novice        1
           26     yes  3.57  Advanced    Advanced        1
           5       no  3.44    Novice      Novice        0
           19     yes  1.98  Advanced    Advanced        0
           15     yes  4.00  Advanced    Advanced        1
           40     yes  3.95    Novice    Beginner        0
           7      yes  2.33    Novice      Novice        1
           22     yes  3.46    Novice    Beginner        0
           36      no  3.00  Advanced      Novice        0
           38     yes  2.65  Advanced    Beginner        1

        # Example 1: Export teradataml DataFrame df to Pandas DataFrame using
        # fastexport().
        >>> fastexport(df)
            Errors: []
            Warnings: []
               masters   gpa     stats programming  admitted
            id
            38     yes  2.65  Advanced    Beginner         1
            26     yes  3.57  Advanced    Advanced         1
            5       no  3.44    Novice      Novice         0
            24      no  1.87  Advanced      Novice         1
            3       no  3.70    Novice    Beginner         1
            1      yes  3.95  Beginner    Beginner         0
            20     yes  3.90  Advanced    Advanced         1
            18     yes  3.81  Advanced    Advanced         1
            8       no  3.60  Beginner    Advanced         1
            25      no  3.96  Advanced    Advanced         1
            ...

        # Example 2: Export teradataml DataFrame df to Pandas DataFrame,
        # set index column, coerce_float and catch errors/warnings thrown by
        # fastexport.
        >>> pandas_df, err, warn = fastexport(df, index_column="gpa",
                                              catch_errors_warnings=True,
                                              coerce_float=True)
        # Print pandas DataFrame.
        >>> pandas_df
                 id masters     stats programming  admitted
            gpa
            2.65  38     yes  Advanced    Beginner         1
            3.57  26     yes  Advanced    Advanced         1
            3.44   5      no    Novice      Novice         0
            1.87  24      no  Advanced      Novice         1
            3.70   3      no    Novice    Beginner         1
            3.95   1     yes  Beginner    Beginner         0
            3.90  20     yes  Advanced    Advanced         1
            3.81  18     yes  Advanced    Advanced         1
            3.60   8      no  Beginner    Advanced         1
            3.96  25      no  Advanced    Advanced         1
            3.76   2     yes  Beginner    Beginner         0
            3.83  17      no  Advanced    Advanced         1

            ...
        # Print errors list.
        >>> err
            []
        # Print warnings list.
        >>> warn
            []
    """
    try:
        # Deriving global connection using context.get_context()
        con = get_context()
        if con is None:
            raise TeradataMlException(
                Messages.get_message(MessageCodes.CONNECTION_FAILURE),
                MessageCodes.CONNECTION_FAILURE)

        awu_matrix = []
        # Add new exports once supported.
        permitted_exports = ["pandas"]
        from teradataml.dataframe.dataframe import DataFrame
        awu_matrix.append(["df", df, False, DataFrame, True])
        awu_matrix.append(["export_to", export_to, True, str, False,
                           permitted_exports])

        # Validate arguments unique to fastexport() function.
        _Validators._validate_function_arguments(awu_matrix)

        if export_to.lower() == "pandas":
            # Initialize and validate DataTransferUtils object.
            dt_obj = _DataTransferUtils(df, index_column=index_column,
                                        all_rows=True,
                                        catch_errors_warnings=catch_errors_warnings)

            # Call fastexport_get_pandas_df function to get pandas dataframe
            # using fastexport datatransfer protocol.
            # "require" is always True, because with this function user requires
            # fastexport.
            return dt_obj._fastexport_get_pandas_df(require=True, **kwargs)

        # TODO Placeholder for functionality to convert teradataml DataFrame to
        #  CSV file.
    except TeradataMlException:
        raise
    except TypeError:
        raise
    except ValueError:
        raise
    except Exception as err:
        raise TeradataMlException(
            Messages.get_message(MessageCodes.DATA_EXPORT_FAILED, "fastexport",
                                 export_to, str(err)),
                                 MessageCodes.DATA_EXPORT_FAILED)


class _DataTransferUtils():
    """
    This class provides utility functions which enable Data Transfer from
    Teradata Vantage to outside world, for example Data Transfer using
    FastExport Protocol.
    """
    def __init__(self, df, index_column=None, num_rows=99999, all_rows=False,
                 catch_errors_warnings=False):
        """
        DESCRIPTION:
            Constructor for the _DataTransferUtils class. It initialises
            arguments that are required for data transfer using FastExport
            protocol or non-fastexport based data transfer using to_pandas()
            API.

        PARAMETERS:
            df:
                Required Argument.
                Specifies the teradataml DataFrame from which data is to be
                extracted.
                Types: teradataml DataFrame.

            index_column:
                Optional Argument.
                Specifies column(s) to be used as index column for the converted
                object.
                Types: str OR list of Strings (str)

            num_rows:
                Optional Argument.
                Specifies the number of rows to be retrieved from teradataml
                DataFrame.
                Default Value: 99999
                Types: int

            all_rows:
                Optional Argument.
                Specifies whether all rows from teradataml DataFrame should be
                retrieved.
                Default Value: False
                Types: bool

            catch_errors_warnings:
                Optional Argument.
                Specifies whether to catch errors/warnings(if any) raised by
                fastexport protocol while converting teradataml DataFrame.
                Default Value: False
                Types: bool

        PARAMETERS:
            None.

        RETURNS:
            None.

        RAISES:
            None.

        EXAMPLES:
            dt_obj = _DataTransferUtils(df)
            dt_obj = _DataTransferUtils(df, index_column='gpa')
            dt_obj = _DataTransferUtils(df, num_rows=10)
            dt_obj = _DataTransferUtils(df, all_rows=True, num_rows=5)
            dt_obj = _DataTransferUtils(df, catch_errors_warnings=True,
                                        num_rows=200)
        """

        self.df = df
        self.index_column = index_column
        self.num_rows = num_rows
        self.all_rows = all_rows
        self.catch_errors_warnings = catch_errors_warnings
        # Validate arguments.
        self._validate_data_export_api_args()

    def _validate_data_export_api_args(self):
        """
        DESCRIPTION:
            Function to validate common arguments used in data export API's
            such as:
                1. DataFrame.to_pandas()
                2. fastexport()

        PARAMETERS:
            None.

        RETURNS:
            None.

        RAISES:
            TeradataMlException,
            TypeError,
            ValueError.

        EXAMPLES:
            dt_obj = _DataTransferUtils(df)
            dt_obj._validate_data_export_api_args()
        """
        awu_matrix = []
        awu_matrix.append(
            ["index_column", self.index_column, True, (str, list), True])
        awu_matrix.append(["num_rows", self.num_rows, True, (int)])
        awu_matrix.append(["all_rows", self.all_rows, True, (bool)])
        awu_matrix.append(
            ["catch_errors_warnings", self.catch_errors_warnings, True, (bool)])

        # Validate argument types.
        _Validators._validate_function_arguments(awu_matrix)
        # Validate if 'num_rows' is a positive int.
        _Validators._validate_positive_int(self.num_rows, "num_rows")

        # Checking if meta expression exists for given dataframe.
        if self.df._metaexpr is None:
            raise TeradataMlException(
                Messages.get_message(MessageCodes.TDMLDF_INFO_ERROR),
                MessageCodes.TDMLDF_INFO_ERROR)

        # Checking each element in passed columns to be valid column in
        # dataframe.
        _Validators._validate_column_exists_in_dataframe(self.index_column,
                                                         self.df._metaexpr)

    def _validate_df_index_column(self):
        """
        DESCRIPTION:
            Function to validate dataframe index label and throw exception if
            there is any mismatch in the index label and columns present in the
            teradataml DataFrame.

        PARAMETERS:
            None.

        RETURNS:
            None.

        RAISES:
            TeradataMLException.

        EXAMPLES:
            dt_obj = _DataTransferUtils(df)
            dt_obj._validate_df_index_column()
        """
        # Get list of columns in teradatml DataFrame.
        df_column_list = [col.name.lower() for col in self.df._metaexpr.c]

        # Check if TDML DF has appropriate index_label set when required
        if self.df._index_label is not None:
            for index_label in UtilFuncs._as_list(self.df._index_label):
                if index_label.lower() not in df_column_list:
                    raise TeradataMlException(
                        Messages.get_message(MessageCodes.DF_LABEL_MISMATCH),
                        MessageCodes.DF_LABEL_MISMATCH)

    def _get_pandas_df_index(self):
        """
        DESCRIPTION:
            Function returns the final index column to be used in the resultant
            DataFrame after converting teradataml DataFrame to Pandas DataFrame.

        PARAMETERS:
            None.

        RETURNS:
            Final Valid index as str or list of Strings.

        RAISES:
            None.

        EXAMPLES:
            dt_obj = _DataTransferUtils(df)
            dt_obj._get_pandas_df_index()
        """
        index_col = None
        # Index Order: 1) User specified 2) TDMLDF index 3) DB PI
        # 4)Else default integer index
        if self.index_column:
            index_col = self.index_column
        elif self.df._index_label:
            index_col = self.df._index_label
        else:
            try:
                from teradataml.dataframe.dataframe_utils import DataFrameUtils
                index_col = DataFrameUtils._get_primary_index_from_table(
                    self.df._table_name)
            except Exception as err:
                index_col = None

        return index_col

    def _generate_to_pandas_base_query(self):
        """
        DESCRIPTION:
            Function to generate base query for to_pandas() function. This query
            is further used to generate pandas dataframe.

        PARAMETERS:
            None.

        RETURNS:
            str.

        RAISES:
            None.

        EXAMPLES:
            dt_obj = _DataTransferUtils(df)
            base_query = dt_obj._generate_to_pandas_base_query()
        """
        # Generate SQL Query using Table name & number of rows required.
        if self.all_rows:
            # Get read query for the whole data.
            return SQLBundle._build_base_query(self.df._table_name,
                                               self.df._orderby)
        else:
            # Get read query using SAMPLE.
            return SQLBundle._build_sample_rows_from_table(self.df._table_name,
                                                           self.num_rows,
                                                           self.df._orderby)

    def _generate_fastexport_query(self, base_query, require=False):
        """
        DESCRIPTION:
            Function to generate fastexport compatible query.

        PARAMETERS:
            base_query:
                Required Argument.
                Specifies the base query to be used for forming the fastexport
                query.
                Types: str.

            require:
                Optional Argument.
                Specifies whether fastexport protocol is required for data
                transfer.
                Default Value: False
                Types: bool

        RETURNS:
            str.

        RAISES:
            None.

        EXAMPLES:
            dt_obj = _DataTransferUtils(df)
            base_query = "select * from my_table SAMPLE 200"
            dt_obj._generate_fastexport_query(base_query)
            dt_obj._generate_fastexport_query(base_query, True)
        """
        if require:
            # If require is set to True, we are using
            # 'teradata_require_fastexport' escape sequence as this will run
            # query using fastexport only if the given query is compatible with
            # fastexport else raises error.
            return "{{fn teradata_require_fastexport}}{0}".format(base_query)
        else:
            # If require is False, we are using 'teradata_try_fastexport'
            # escape sequence as this will run query using fastexport if the
            # given query is compatible with fastexport else runs it as
            # regular query.
            return "{{fn teradata_try_fastexport}}{0}".format(base_query)

    def _execute_query_and_generate_pandas_df(self, query, index_column,
                                              **kwargs):
        """
        DESCRIPTION:
            Function executes the provided query and returns a pandas DataFrame.

        PARAMETERS:
            query:
                Required Argument.
                Specifies the query that needs to be executed to form Pandas
                DataFrame.
                Type: str.

            index_column:
                Required Argument.
                Specifies column(s) to be used as Pandas index.
                Types: str OR list of Strings (str).

            coerce_float:
                Optional Argument.
                Attempts to convert values of non-string, non-numeric objects
                (like decimal.Decimal) to floating point, useful for SQL result
                sets.
                Default: False.
                Types: bool

            parse_dates:
                Optional Argument.
                Specifes List of column names to parse as dates.
                Default: None.
                Types: list or dict.

        RETURNS:
            Pandas DataFrame.

        RAISES:
            TeradataMlException.

        EXAMPLES:
            dt_obj = _DataTransferUtils(df)
            query = "{fn teradata_try_fastexport}select * from my_table SAMPLE
                    200"
            pdf = dt_obj._execute_query_and_generate_pandas_df(query, "col1")
        """
        pandas_df = None
        con = get_context()
        coerce_float = kwargs.pop("coerce_float", False)
        # Use index_col when exists, else default integer index (no index_col)
        if index_column is not None:
            pandas_df = pd.read_sql_query(query, con, index_col=index_column,
                                          coerce_float=coerce_float,
                                          **kwargs)
        else:
            pandas_df = pd.read_sql_query(query, con, coerce_float=coerce_float,
                                          **kwargs)

        if pandas_df is None:
            raise TeradataMlException(
                Messages.get_message(MessageCodes.DF_WITH_NO_COLUMNS),
                MessageCodes.DF_WITH_NO_COLUMNS)
        return pandas_df

    def _process_fastexport_errors_warnings(self, query):
        """
        DESCRIPTION:
            Function to process errors/warnings(if any) raised while executing
            the fastexport protocol.

        PARAMETERS:
            query:
                Required Argument.
                Specifies the query with fastexport escape sequences that is
                used to convert teradataml DataFrame to Pandas DataFrame.
                Type: str.

        RETURNS:
            A tuple with two lists for errors, warnings each containing err/warn
            messages in string format.

        RAISES:
            None.

        EXAMPLES:
            dt_obj = _DataTransferUtils(df)
            query = "{fn teradata_try_fastexport}select * from my_table SAMPLE
                    200"
            err, warn = dt_obj._process_fastexport_errors_warnings(query)
        """
        err = None
        warn = None
        conn = get_connection().connection
        # Create a cursor from connection object.
        cur = conn.cursor()
        from teradataml.dataframe.fastload import _get_errors_warnings
        # Get err/warn
        err = _get_errors_warnings(cur, query,
                                   "{fn teradata_nativesql}{fn teradata_get_errors}")
        warn = _get_errors_warnings(cur, query,
                                    "{fn teradata_nativesql}{fn teradata_get_warnings}")
        return err, warn

    def _get_pandas_dataframe(self, **kwargs):
        """
        DESCRIPTION:
            Function that converts teradataml DataFrame to Pandas DataFrame
            using regular approach.

        PARAMETERS:
            kwargs:
                Specifies keyword arguments.

        RETURNS:
            Pandas DataFrame.

        RAISES:
            None.

        EXAMPLES:
            dt_obj = _DataTransferUtils(df)
            dt_obj._get_pandas_dataframe()

        """
        # Get the final index column.
        final_index_column = self._get_pandas_df_index()
        # Get the base query.
        base_query = self._generate_to_pandas_base_query()
        # Generate pandas dataframe using base query.
        pandas_df = \
            self._execute_query_and_generate_pandas_df(base_query,
                                                       final_index_column,
                                                       **kwargs)
        return pandas_df

    def _fastexport_get_pandas_df(self, require=False, **kwargs):
        """
        DESCRIPTION:
            Internal function to convert teradataml DataFrame to Pandas
            DataFrame using FastExport protocol. This internal function can be
            directly used in to_pandas() and fastexport API's if either of
            the functions has to use fastexport.

        PARAMETERS:
            require:
                Optional Argument.
                Specifies whether fastexport protocol is required for data
                transfer.
                Default Value: False
                Types: bool

            kwargs:
                Specifies keyword arguments.

        RETURNS:
            When "catch_errors_warnings" is set to True, the function returns
            a tuple containing:
            * Pandas DataFrame.
            * Errors, if any, thrown by fastexport in a list of strings.
            * Warnings, if any, thrown by fastexport in a list of strings.
            Only Pandas DataFrame otherwise.

        RAISES:
            TeradataMlException.

        EXAMPLES:
            dt_obj = _DataTransferUtils(df)
            dt_obj._fastexport_get_pandas_df(require=False)

        """

        try:
            self._validate_df_index_column()
            final_index_col = self._get_pandas_df_index()
            self.df._DataFrame__execute_node_and_set_table_name(self.df._nodeid,
                                                                self.df._metaexpr)
            base_query = self._generate_to_pandas_base_query()
            fastexport_query = self._generate_fastexport_query(base_query,
                                                               require=require)
            pandas_df = \
                self._execute_query_and_generate_pandas_df(fastexport_query,
                                                           final_index_col,
                                                           **kwargs)
            err, warn = \
                self._process_fastexport_errors_warnings(fastexport_query)
            if self.catch_errors_warnings:
                return pandas_df, err, warn
            else:
                print("Errors: {0}".format(err))
                print("Warnings: {0}".format(warn))
                return pandas_df
        except TeradataMlException:
            raise
