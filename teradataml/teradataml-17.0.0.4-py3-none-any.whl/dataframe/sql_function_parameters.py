#!/usr/bin/python
# ##################################################################
#
# Copyright 2021 Teradata. All rights reserved.
# TERADATA CONFIDENTIAL AND TRADE SECRET
#
# Primary Owner: Pradeep Garre (pradeep.garre@teradata.com)
# Secondary Owner: Pankaj Purandare (pankajvinod.purandare@teradata.com)
#
# Version: 1.0
# Function Version: 1.0
#
# ##################################################################

from teradataml.dataframe.sql_interfaces import ColumnExpression


# Function to generate Individual parameter structure.
def _generate_param_structure(param_name, param_type, **kwargs):
    """
    DESCRIPTION:
        Generates the structure for a parameter.

    PARAMETERS:
        param_name:
            Required Argument.
            Specifies the name of the Parameter.
            Types: str

        param_type:
            Required Argument.
            Specifies the type of Parameter.
            Types: Any Type or Tuple of Types.

        kwargs:
            Optional Argument.
            Specifies optional keyword arguments.
            Types: dict

    RAISES:
        None

    RETURNS:
        dict.

    EXAMPLES:
        generate_param_structure("column", _SQLColumnExpression)
        generate_param_structure("width", 5)
    """
    param_struct = {"arg_name": param_name,
                    "exp_types": param_type}

    if "default_value" in kwargs:
        default_value = kwargs["default_value"]
        # If default value is a string, this should be guarded with single
        # quotes as strings should be guarded with single quotes in function
        # signature.
        param_struct["default_value"] = "'{}'".format(default_value) if isinstance(default_value, str) \
                                        else default_value

    return param_struct


# Different type of Aggregate functions accepts different types of parameters,
# However, specific category functions accepts similar parameters, i.e., csum
# and msum, both accepts first parameter as width and second parameter as
# expression. So, constructing the parameter structures and using the structure
# for aggregate functions.
#
# expected_types: Value of the 'expected_types' key represents the expected type
#                 of the parameter.
# param_name: Value of the 'param_name' key represents the expected name
#             of the parameter.
# default_value: Value of the 'default_value' key represents the default value
#                of the parameter.
#                Note: "default_value" should be always a keyword argument.

_params_column_structure = [_generate_param_structure("expression", (ColumnExpression, int, float, str))]
_params_width_sort_columns_structure = [_generate_param_structure("width", int),
                                        _generate_param_structure("sort_columns",
                                                                 (ColumnExpression, list, str))
                                       ]
quantile_parameter_structure = [_generate_param_structure("quantile_literal", int),
                                _generate_param_structure("sort_columns",
                                                         (ColumnExpression, list, str))
                               ]
_params_width_sort_column_structure = [_generate_param_structure("width", int),
                                       _generate_param_structure("sort_column",
                                                                 (ColumnExpression, str))
                                      ]
_params_columns_structure = [_generate_param_structure("sort_columns",
                                                    (ColumnExpression, list, str))
                            ]
_lead_lag_params_structure = [_generate_param_structure("offset_value", int, default_value=1),
                              _generate_param_structure(
                                  "default_expression", (ColumnExpression, int, float, str), default_value=None)]
_percentile_param_structure = [_generate_param_structure("percentile", (int, float)),
                               _generate_param_structure("interpolation", (type(None), str), default_value="LINEAR"),
                               _generate_param_structure("describe_op", (bool), default_value=False)
                               ]

# Most of the Aggregate functions take first parameter as the column on which the
# Aggregate function is being applied. However, few functions do not accept
# first parameter as the corresponding column. All such functions should be
# kept in NO_DEFAULT_PARAM_FUNCTIONS.
# e.g: SQL Function expression for Correlation is CORR(expression1, expression2)
#      and the corresponding teradataml notation is df.col1.corr(col2). Here,
#      expression1 represents col1 & expression2 represents col2. So, col1 is the
#      default first parameter. However, for QUANTILE, it's SQL function
#      expression is QUANTILE(integer, expression) and corresponding teradataml
#      notation is df.col.quantile(x, col2). Notice that, first parameter for
#      quantile function is not the column on which the function is being applied
#      and thus, quantile should be kept in NO_DEFAULT_PARAM_FUNCTIONS.
# Notes:
#     1. The function names specified here are SQL function names, not
#        Python function names.
#     2. SQL Function must be in UPPERCASE.
NO_DEFAULT_PARAM_FUNCTIONS = ["QUANTILE", "RANK", "CUME_DIST", "DENSE_RANK",
                              "PERCENT_RANK", "ROW_NUMBER", "PERCENTILE_CONT",
                              "PERCENTILE_DISC"]

# Stores the additional parameters of the aggregate sql function. By default,
# most aggregate functions take first argument as column on which aggregate
# function is being applied. So, param structure do not store that column.
# Param structure stores only additional parameters.
# e.g: SQL aggregate function corr takes two columns as input. Since, first
#      column is a default parameter, param structure stores only the details
#      about second parameter and thus corr is mapped to _params_column_structure,
#      which stores only one parameter structure.
# Notes:
#     1. If function takes no additional parameters, then do not make entry for
#        the corresponding aggregate function or keep an empty list as structure.
#     2. Key in the below dictionary represents the name of the SQL function,
#        not the name of python function.
#     3. SQL Function must be in UPPERCASE.
SQL_AGGREGATE_FUNCTION_ADDITIONAL_PARAMETERS = {
    "CORR": _params_column_structure,
    "COVAR_POP": _params_column_structure,
    "COVAR_SAMP": _params_column_structure,
    "REGR_AVGX": _params_column_structure,
    "REGR_AVGY": _params_column_structure,
    "REGR_COUNT": _params_column_structure,
    "REGR_INTERCEPT": _params_column_structure,
    "REGR_R2": _params_column_structure,
    "REGR_SLOPE": _params_column_structure,
    "REGR_SXX": _params_column_structure,
    "REGR_SXY": _params_column_structure,
    "REGR_SYY": _params_column_structure,
    "CUME_DIST": [],
    "DENSE_RANK": [],
    "LAG": _lead_lag_params_structure,
    "LEAD": _lead_lag_params_structure,
    "PERCENT_RANK": [],
    "PERCENTILE": _percentile_param_structure,
    "RANK": [],
    "ROW_NUMBER": [],
    "FIRST_VALUE": [],
    "LAST_VALUE": [],
    "CSUM": _params_columns_structure,
    "QUANTILE": quantile_parameter_structure,
    "MSUM": _params_width_sort_columns_structure,
    "MAVG": _params_width_sort_columns_structure,
    "MDIFF": _params_width_sort_columns_structure,
    "MLINREG": _params_width_sort_column_structure
}