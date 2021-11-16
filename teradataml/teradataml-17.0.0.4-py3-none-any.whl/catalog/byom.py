"""
Unpublished work.
Copyright (c) 2021 by Teradata Corporation. All rights reserved.
TERADATA CORPORATION CONFIDENTIAL AND TRADE SECRET

Primary Owner: pradeep.garre@teradata.com
Secondary Owner: PankajVinod.Purandare@teradata.com

This file implements the core framework that allows user to load BYOM to Vantage.
"""

from teradataml.dataframe.dataframe import DataFrame, in_schema
from teradataml.utils.validators import _Validators
from teradataml.context.context import _get_current_databasename, get_context
from teradataml.common.messagecodes import MessageCodes
from teradataml.common.messages import Messages
from teradataml.common.exceptions import TeradataMlException
from teradatasql import OperationalError as SqlOperationalError
from teradatasqlalchemy.types import *
from teradatasqlalchemy.types import _TDType
from teradataml.dbutils.dbutils import _get_quoted_object_name, _create_table
from teradataml.common.utils import UtilFuncs
from teradataml.utils.dtypes import _Dtypes
from teradataml.catalog.model_cataloging_utils import __get_like_filter_expression_on_col
from teradataml.options.display import display


validator = _Validators()


def __check_if_model_exists(model_id,
                            table_name,
                            schema_name=None,
                            raise_error_if_model_found=False,
                            raise_error_if_model_not_found=False):
    """
    DESCRIPTION:
        Internal function to check if byom model with given "model_id", exists or not.

    PARAMETERS:
        model_id:
            Required Argument.
            Specifies the name of the model identifier to check whether it exists or not.
            Types: str

        table_name:
            Required Argument.
            Specifies the table name that may or may not contain entry for the model.
            Types: str

        schema_name:
            Optional Argument.
            Specifies the name of the schema, to look out for table specified in
            "table_name". If not specified, then "table_name" is looked over in
            the current database.
            Types: str

        raise_error_if_model_found:
            Optional Argument.
            Specifies the flag to decide whether to raise error when model exists or not.
            Default Value: False (Do not raise exception)
            Types: bool

        raise_error_if_model_not_found:
            Optional Argument.
            Specifies the flag to decide whether to raise error when model is found or not.
            Default Value: False (Do not raise exception)
            Types: bool

    RETURNS:
        bool.

    RAISES:
        TeradataMlException - MODEL_ALREADY_EXISTS, MODEL_NOT_FOUND

    EXAMPLES:
        >>> meta_df = __check_if_model_exists("glm_out")
    """
    # If external model, create DataFrame on table specified in parameters within
    # current schema. Else, create DataFrame on table & schema specified in parameters.
    schema_name = schema_name if schema_name is not None else _get_current_databasename()
    models_meta_df = DataFrame(in_schema(schema_name, table_name))
    models_meta_df = models_meta_df[models_meta_df.model_id == model_id]

    num_rows = models_meta_df.shape[0]

    if raise_error_if_model_found:
        if num_rows == 1:
            # If model with name 'name' already exists.
            raise TeradataMlException(Messages.get_message(MessageCodes.MODEL_ALREADY_EXISTS,
                                                           model_id),
                                      MessageCodes.MODEL_ALREADY_EXISTS)

    if raise_error_if_model_not_found:
        if num_rows == 0:
            # 'name' MODEL_NOT_FOUND
            raise TeradataMlException(Messages.get_message(MessageCodes.MODEL_NOT_FOUND,
                                                           model_id, ''),
                                      MessageCodes.MODEL_NOT_FOUND)

    return True if num_rows == 1 else False


def save_byom(model_id,
              model_file,
              table_name,
              schema_name=None,
              additional_columns=None,
              additional_columns_types=None):
    """
    DESCRIPTION:
        Function to save externally trained models in Teradata Vantage in the
        specified table. Function allows user to save various models stored in
        different formats such as PMML, MOJO etc. If the specified model table
        exists in Vantage, model data is saved in the same, otherwise model table
        is created first based on the user parameters and then model data is
        saved. See below 'Note' section for more details.

        Note:
            If user specified table exists, then
                a. Table must have at least two columns with names and types as
                   specified below:
                   * 'model_id' of type VARCHAR of any length and
                   * 'model' column of type BLOB.
                b. User can choose to have the additional columns as well to store
                   additional information of the model. This information can be passed
                   using "additional_columns" parameter. See "additional_columns"
                   argument description for more details.
            If user specified table does not exist, then
                a. Function creates the table with the name specified in "table_name".
                b. Table is created in the schema specified in "schema_name". If
                   "schema_name" is not specified, then current schema is considered
                   for "schema_name".
                c. Table is created with columns:
                    * 'model_id' with type specified in "additional_columns_types". If
                      not specified, table is created with 'model_id' column as VARCHAR(128).
                    * 'model' with type specified in "additional_columns_types". If
                      not specified, table is created with 'model' column as BLOB.
                    * Columns specified in "additional_columns" parameter. See "additional_columns"
                      argument description for more details.
                    * Datatypes of these additional columns are either taken from
                      the values passed to "additional_columns_types" or inferred
                      from the values passed to the "additional_columns". See
                      "additional_columns_types" argument description for more details.

    PARAMETERS:
        model_id:
            Required Argument.
            Specifies the unique model identifier for model.
            Types: str.

        model_file:
            Required Argument.
            Specifies the absolute path of the file which has model information.
            Types: str

        table_name:
            Required Argument.
            Specifies the name of the table where model is saved. If "table_name"
            does not exist, this function creates table according to "additional_columns"
            and "additional_columns_types".
            Types: str

        schema_name:
            Optional Argument.
            Specifies the name of the schema in which the table specified in
            "table_name" is looked up. If not specified, then table is looked
            up in current schema.
            Types: str

        additional_columns:
            Optional Argument.
            Specifies the additional information about the model to be saved in the
            model table. Additional information about the model is passed as key value
            pair, where key is the name of the column and value is data to be stored
            in that column for the model being saved.
            Notes:
                 1. Following are the allowed types for the values passed in dictionary:
                    * int
                    * float
                    * str
                    * bool
                    * datetime.datetime
                    * datetime.date
                    * datetime.time
                 2. "additional_columns" does not accept keys model_id and model.
            Types: str

        additional_columns_types:
            Optional Argument.
            Specifies the column type of additional columns. These column types are used
            while creating the table using the columns specified in "additional_columns"
            argument. Additional column datatype information is passed as key value pair
            with key being the column name and value as teradatasqlalchemy.types.
            Notes:
                 1. If, any of the column type for additional columns are not specified in
                    "additional_columns_types", it then derives the column type according
                    the below table:
                    +---------------------------+-----------------------------------------+
                    |     Python Type           |        teradatasqlalchemy Type          |
                    +---------------------------+-----------------------------------------+
                    | str                       | VARCHAR(1024)                           |
                    +---------------------------+-----------------------------------------+
                    | int                       | INTEGER                                 |
                    +---------------------------+-----------------------------------------+
                    | bool                      | BYTEINT                                 |
                    +---------------------------+-----------------------------------------+
                    | float                     | FLOAT                                   |
                    +---------------------------+-----------------------------------------+
                    | datetime                  | TIMESTAMP                               |
                    +---------------------------+-----------------------------------------+
                    | date                      | DATE                                    |
                    +---------------------------+-----------------------------------------+
                    | time                      | TIME                                    |
                    +---------------------------+-----------------------------------------+
                 2. Columns model_id, with column type as VARCHAR and model, with column type
                    as BLOB are mandatory for table. So, for the columns model_id and model,
                    acceptable values for "additional_columns_types" are VARCHAR and BLOB
                    respectively.
                 3. This argument is ignored if table exists.
            Types: dict

    RETURNS:
        None.

    RAISES:
        TeradataMlException, TypeError, ValueError

    EXAMPLES:

        >>> import teradataml, os, datetime
        >>> model_file = os.path.join(os.path.dirname(teradataml.__file__), 'data', 'models', 'iris_kmeans_model')
        >>> from teradataml import save_byom

        # Example 1 - Create table "byom_model" with additional columns by specifying the type
        #             of the columns as below and save the model in it.
        #             +---------------------------+-----------------------------------------+
        #             |     Column name           |        Column Type                      |
        #             +---------------------------+-----------------------------------------+
        #             | model_id                  | VARCHAR(128)                            |
        #             +---------------------------+-----------------------------------------+
        #             | model                     | BLOB                                    |
        #             +---------------------------+-----------------------------------------+
        #             | Description               | VARCHAR(2000)                           |
        #             +---------------------------+-----------------------------------------+
        #             | UserId                    | NUMBER(5)                               |
        #             +---------------------------+-----------------------------------------+
        #             | ProductionReady           | BYTEINT                                 |
        #             +---------------------------+-----------------------------------------+
        #             | ModelEfficiency           | NUMBER(11,10)                           |
        #             +---------------------------+-----------------------------------------+
        #             | ModelSavedTime            | TIMESTAMP                               |
        #             +---------------------------+-----------------------------------------+
        #             | ModelGeneratedDate        | DATE                                    |
        #             +---------------------------+-----------------------------------------+
        #             | ModelGeneratedTime        | TIME                                    |
        #             +---------------------------+-----------------------------------------+
        #
        >>> save_byom('model1',
        ...           model_file,
        ...           'byom_models',
        ...           additional_columns={"Description": "KMeans model",
        ...                               "UserId": "12345",
        ...                               "ProductionReady": False,
        ...                               "ModelEfficiency": 0.67412,
        ...                               "ModelSavedTime": datetime.datetime.now(),
        ...                               "ModelGeneratedDate":datetime.date.today(),
        ...                               "ModelGeneratedTime": datetime.time(hour=0,minute=5,second=45,microsecond=110)
        ...                               },
        ...           additional_columns_types={"Description": VARCHAR(2000),
        ...                                    "UserId": NUMBER(5),
        ...                                    "ProductionReady": BYTEINT,
        ...                                    "ModelEfficiency": NUMBER(11,10),
        ...                                    "ModelSavedTime": TIMESTAMP,
        ...                                    "ModelGeneratedDate": DATE,
        ...                                    "ModelGeneratedTime": TIME}
        ...           )
        Created the table 'byom_models' as it does not exist.
        Model is saved.
        >>>

        # Example 2 - Create table "byom_model1" in "test" DataBase, with additional columns
        #             by not specifying the type of the columns and once table is created,
        #             save the model in it.
        >>> save_byom('model1',
        ...           model_file,
        ...           'byom_models1',
        ...           additional_columns={"Description": "KMeans model",
        ...                               "UserId": "12346",
        ...                               "ProductionReady": False,
        ...                               "ModelEfficiency": 0.67412,
        ...                               "ModelSavedTime": datetime.datetime.now(),
        ...                               "ModelGeneratedDate":datetime.date.today(),
        ...                               "ModelGeneratedTime": datetime.time(hour=0,minute=5,second=45,microsecond=110)
        ...                               },
        ...           schema_name='test'
        ...           )
        Created the table 'byom_models1' as it does not exist.
        Model is saved.
        >>>

        # Example 3 - Save the model in the existing table "byom_models".
        >>> save_byom('model2',
        ...           model_file,
        ...           'byom_models',
        ...           additional_columns={"Description": "KMeans model duplicated"}
        ...           )
        Model is saved.
        >>>

    """
    try:
        # Let's perform argument validations.
        # Create argument information matrix to do parameter checking
        __arg_info_matrix = []
        __arg_info_matrix.append(["model_id", model_id, False, str, True])
        __arg_info_matrix.append(["model_file", model_file, False, str, True])
        __arg_info_matrix.append(["table_name", table_name, False, str, True])
        __arg_info_matrix.append(["schema_name", schema_name, True, str, True])
        __arg_info_matrix.append(["additional_columns", additional_columns, True, dict])
        __arg_info_matrix.append(["additional_columns_types", additional_columns_types, True, dict])

        # Make sure that a correct type of values has been supplied to the arguments.
        validator._validate_function_arguments(__arg_info_matrix)

        # Change the additional_columns_types and additional_columns to dictionary if
        # it is None so that retrieval would be easy.
        if additional_columns_types is None:
            additional_columns_types = {}

        if additional_columns is None:
            additional_columns = {}

        # Check if model_id or model in additional columns.
        for column in ["model_id", "model"]:
            if column in additional_columns:
                error_code = MessageCodes.NOT_ALLOWED_VALUES
                error_msg = Messages.get_message(error_code, column, "additional_columns")
                raise TeradataMlException(error_msg, error_code)

        columns_to_create = {}

        column_names = ["model_id", "model"]
        insert_parameters = [model_id, UtilFuncs._get_file_contents(model_file, True)]

        # If user pass any additional columns data, extract that also to insert it
        # in table.
        if additional_columns:

            for col, value in additional_columns.items():
                # Before proceed further, validate the additional columns data.
                # One should not pass custom types such as list, dict, user defined
                # objects etc.
                _Validators._validate_py_type_for_td_type_conversion(type(value), "additional_columns")

                # If column type is not specified in additional column types, then
                # derive the appropriate one.
                columns_to_create[col] = additional_columns_types.get(
                    col, _Dtypes._python_type_to_teradata_type(type(value)))

                column_names.append(col)
                insert_parameters.append(value)

        connection = get_context()

        # Check if table already exists.
        #   If exists, check whether model exists or not. If exists, raise error.
        #   If not exists, create the table.
        if connection.dialect.has_table(connection, table_name=table_name, schema=schema_name):
            __check_if_model_exists(
                model_id, table_name, schema_name, raise_error_if_model_found=True)
        else:
            __mandatory_columns_types = {"model_id": VARCHAR, "model": BLOB}
            is_mandatory_col_type_expected = lambda c_name, c_type:\
                c_type == __mandatory_columns_types[c_name] or type(c_type) == __mandatory_columns_types[c_name]

            # Validate additional_columns_types.
            for c_name, c_type in additional_columns_types.items():

                # Check if model_id & model columns have appropriate types.
                if c_name in __mandatory_columns_types and not is_mandatory_col_type_expected(c_name, c_type):
                    error_code = MessageCodes.INVALID_COLUMN_DATATYPE
                    err_msg = Messages.get_message(error_code,
                                                   c_name,
                                                   "additional_columns_types",
                                                   "Valid",
                                                   "[{}]".format(__mandatory_columns_types[c_name].__name__)
                                                   )
                    raise TeradataMlException(err_msg, error_code)

                # Check if value passed to additional_columns_types is a valid type or not.
                # User can pass a class or an object of a class from teradatasqlalchemy.types .
                # So, Check if c_type is either a subclass of TDType or a TDType.
                # isinstance(c_type, _TDType), checks if c_type is an object of teradatasqlalchemy.types
                # issubclass(c_type, _TDType), checks if c_type is a proper Teradata type or not.
                # However, issubclass accepts only class in its 1st parameter so check if c_type is
                # a class or not, before passing it to issubclass.
                elif not (isinstance(c_type, _TDType) or (isinstance(c_type, type) and issubclass(c_type, _TDType))):
                    error_code = MessageCodes.INVALID_COLUMN_DATATYPE
                    err_msg = Messages.get_message(
                        error_code, c_name, "additional_columns_types", "Valid", "teradatasqlalchemy.types")
                    raise TeradataMlException(err_msg, error_code)

            # Add model_id and model for columns. If not available, set those to default.
            columns_to_create = {"model_id": additional_columns_types.get("model_id", VARCHAR(128)),
                                 "model": additional_columns_types.get("model", BLOB),
                                 **columns_to_create}
            _create_table(
                table_name, columns_to_create, primary_index="model_id", schema_name=schema_name)
            print("Created the model table '{}' as it does not exist.".format(table_name))

        # If schema is specified, then concatenate schema name with table name.
        if schema_name:
            table_name = _get_quoted_object_name(schema_name, table_name)

        columns_clause = ", ".join(column_names)
        values_clause = ", ".join(("?" for _ in range(len(column_names))))
        insert_model = f"insert into {table_name} ({columns_clause}) values ({values_clause});"
        get_context().execute(insert_model, *insert_parameters)
        print("Model is saved.")

    except (SqlOperationalError, TeradataMlException, TypeError, ValueError):
            raise
    except Exception as err:
        error_code = MessageCodes.MODEL_CATALOGING_OPERATION_FAILED
        raise TeradataMlException(Messages.get_message(error_code, "save", str(err)), error_code)


def delete_byom(model_id, table_name, schema_name=None):
    """
    DESCRIPTION:
        Delete a model from the user specified table in Teradata Vantage.

    PARAMETERS:
        model_id:
            Required Argument.
            Specifies the the unique model identifier of the model to be deleted.
            Types: str

        table_name:
            Required Argument.
            Specifies the name of the table to delete the model from.
            Types: str

        schema_name:
            Optional Argument.
            Specifies the name of the schema in which the table specified in
            "table_name" is looked up. If not specified, then table is looked
            up in current schema.
            Types: str

    RETURNS:
        None.

    RAISES:
        TeradataMlException

    EXAMPLES:

        >>> import teradataml, os, datetime
        >>> model_file = os.path.join(os.path.dirname(teradataml.__file__), 'data', 'models', 'iris_kmeans_model')
        >>> from teradataml import save_byom, delete_byom
        >>> save_byom('model3', model_file, 'byom_models')
        Model is saved.
        >>> save_byom('model4', model_file, 'byom_models', schema_name='test')
        Model is saved.
        >>>

        # Example 1 - Delete a model with id 'model3' from the table byom_models.
        >>> delete_byom(model_id='model3', table_name='byom_models')
        Model is deleted.
        >>>

        # Example 2 - Delete a model with id 'model4' from the table byom_models
        #             and the table is in "test" DataBase.
        >>> delete_byom(model_id='model4', table_name='byom_models', schema_name='test')
        Model is deleted.
        >>>
    """

    # Let's perform argument validations.
    # Create argument information matrix to do parameter checking
    __arg_info_matrix = []
    __arg_info_matrix.append(["model_id", model_id, False, str, True])
    __arg_info_matrix.append(["table_name", table_name, False, str, True])
    __arg_info_matrix.append(["schema_name", schema_name, True, str, True])

    # Make sure that a correct type of values has been supplied to the arguments.
    validator._validate_function_arguments(__arg_info_matrix)

    schema_name = schema_name if schema_name is not None else _get_current_databasename()

    # Before proceed further, check whether table exists or not.
    conn = get_context()
    if not conn.dialect.has_table(conn, table_name=table_name, schema=schema_name):
        error_code = MessageCodes.MODEL_CATALOGING_OPERATION_FAILED
        error_msg = Messages.get_message(
            error_code, "delete", 'Table "{}.{}" does not exist.'.format(schema_name, table_name))
        raise TeradataMlException(error_msg, error_code)

    # Let's check if the user created the model since only the creator can delete it
    __check_if_model_exists(model_id, table_name, schema_name, raise_error_if_model_not_found=True)

    # Get the FQTN before deleting the model.
    table_name = _get_quoted_object_name(schema_name, table_name)

    try:
        delete_model = f"delete from {table_name} where model_id = (?)"
        get_context().execute(delete_model, model_id)
        print("Model is deleted.")

    except (SqlOperationalError, TeradataMlException):
        raise
    except Exception as err:
        error_code = MessageCodes.MODEL_CATALOGING_OPERATION_FAILED
        error_msg = Messages.get_message(error_code, "delete", str(err))
        raise TeradataMlException(error_msg, error_code)


def retrieve_byom(model_id,
                  table_name,
                  schema_name=None,
                  license=None,
                  is_license_column=False,
                  license_table_name=None,
                  license_schema_name=None):
    """
    DESCRIPTION:
        Function to retrieve a saved model. Output of this function can be
        directly passed as input to the PMMLPredict and H2OPredict functions.
        Some models generated, such as H2O-DAI has license associated with it.
        When such models are to be used for scoring, one must retrieve the model
        by passing relevant license information. Please refer to "license_key"
        for more details.

    PARAMETERS:
        model_id:
            Required Argument.
            Specifies the unique model identifier of the model to be retrieved.
            Types: str

        table_name:
            Required Argument.
            Specifies the name of the table to retrieve external model from.
            Types: str

        schema_name:
            Optional Argument.
            Specifies the name of the schema in which the table specified in
            "table_name" is looked up. If not specified, then table is looked
            up in current schema.
            Types: str

        license:
            Optional Argument.
            Specifies the license key information in different ways specified as below:
            * If the license key is stored in a variable, user can pass it as string.
            * If the license key is stored in table, then pass a column name containing
              the license. Based on the table which has license information stored,
                * If the information is stored in the same model table as that of the
                  model, one must set "is_license_column" to True.
                * If the information is stored in the different table from that of the
                  "table_name", one can specify the table name and schema name using
                  "license_table_name" and "license_schema_name" respectively.
            Types: str

        is_license_column:
            Optional Argument.
            Specifies whether license key specified in "license" is a license key
            or column name. When set to True, "license" contains the column name
            containing license data, otherwise contains the actual license key.
            Default Value: False
            Types: str

        license_table_name:
            Optional Argument.
            Specifies the name of the table which holds license key. One can specify this
            argument if license is stored in a table other than "table_name".
            Types: str

        license_schema_name:
            Optional Argument.
            Specifies the name of the Database associated with the "license_table_name".
            If not specified, current Database would be considered for "license_table_name".
            Types: str

    RETURNS:
        teradataml DataFrame

    RAISES:
        TeradataMlException, TypeError

    EXAMPLES:
        >>> import teradataml, os, datetime
        >>> model_file = os.path.join(os.path.dirname(teradataml.__file__), 'data', 'models', 'iris_kmeans_model')
        >>> from teradataml import save_byom, retrieve_byom, get_context
        >>> save_byom('model5', model_file, 'byom_models')
        Model is saved.
        >>> save_byom('model6', model_file, 'byom_models', schema_name='test')
        Model is saved.
        >>> save_byom('licensed_model1', model_file, 'byom_licensed_models', additional_columns={"license_data": "A5sUL9KU_kP35Vq"})
        Created the model table 'byom_licensed_models' as it does not exist.
        Model is saved.
        >>> # Store the license in a table.
        >>> license = 'eZSy3peBVRtjA-ibVuvNw5A5sUL9KU_kP35Vq4ZNBQ3iGY6oVSpE6g97sFY2LI'
        >>> lic_table = 'create table license (id integer between 1 and 1,license_key varchar(2500)) unique primary index(id);'
        >>> get_context().execute(lic_table)
        <sqlalchemy.engine.cursor.LegacyCursorResult object at 0x0000014AAFF27080>
        >>> get_context().execute("insert into license values (1, 'peBVRtjA-ib')")
        <sqlalchemy.engine.cursor.LegacyCursorResult object at 0x0000014AAFF27278>
        >>>

        # Example 1 - Retrieve a model with id 'model5' from the table 'byom_models'.
        >>> df = retrieve_byom('model5', table_name='byom_models')
        >>> df
                                     model
        model_id
        model5    b'504B03041400080808...'

        # Example 2 - Retrieve a model with id 'model6' from the table 'byom_models'
        #             and the table is in 'test' DataBase.
        >>> df = retrieve_byom('model6', table_name='byom_models', schema_name='test')
        >>> df
                                     model
        model_id
        model6    b'504B03041400080808...'

        # Example 3 - Retrieve a model with id 'model5' from the table 'byom_models'
        #             with license key stored in a variable 'license'.
        >>> df = retrieve_byom('model5', table_name='byom_models', license=license)
        >>> df
                                     model                                                         license
        model_id
        model5    b'504B03041400080808...'  eZSy3peBVRtjA-ibVuvNw5A5sUL9KU_kP35Vq4ZNBQ3iGY6oVSpE6g97sFY2LI
        >>>

        # Example 4 - Retrieve a model with id 'licensed_model1' and associated license
        #             key stored in table 'byom_licensed_models'. License key is stored
        #             in column 'license_data'.
        >>> df = retrieve_byom('licensed_model1',
        ...                    table_name='byom_licensed_models',
        ...                    license='license_data',
        ...                    is_license_column=True)
        >>> df
                                            model          license
        model_id
        licensed_model1  b'504B03041400080808...'  A5sUL9KU_kP35Vq
        >>>

        # Example 5 - Retrieve a model with id 'licensed_model1' from the table
        #             'byom_licensed_models' and associated license key stored in
        #             column 'license_key' of the table 'license'.
        >>> df = retrieve_byom('licensed_model1',
        ...                    table_name='byom_licensed_models',
        ...                    license='license_key',
        ...                    is_license_column=True,
        ...                    license_table_name='license')
        >>> df
                                            model      license
        model_id
        licensed_model1  b'504B03041400080808...'  peBVRtjA-ib
        >>>

        # Example 6 - Retrieve a model with id 'licensed_model1' from the table
        #             'byom_licensed_models' and associated license key stored in
        #             column 'license_key' of the table 'license' present in the
        #             schema 'mldb'.
        >>> df = retrieve_byom('licensed_model1',
        ...                    table_name='byom_licensed_models',
        ...                    license='license_key',
        ...                    is_license_column=True,
        ...                    license_table_name='license',
        ...                    license_schema_name='mldb')
        >>> df
                                            model      license
        model_id
        licensed_model1  b'504B03041400080808...'  peBVRtjA-ib
        >>>
    """

    # Let's perform argument validations.
    # Create argument information matrix to do parameter checking
    __arg_info_matrix = []
    __arg_info_matrix.append(["model_id", model_id, False, str, True])
    __arg_info_matrix.append(["table_name", table_name, False, str, True])
    __arg_info_matrix.append(["schema_name", schema_name, True, str, True])
    __arg_info_matrix.append(["license", license, True, str, True])
    __arg_info_matrix.append(["is_license_column", is_license_column, False, bool])
    __arg_info_matrix.append(["license_table_name", license_table_name, True, str, True])
    __arg_info_matrix.append(["license_schema_name", license_schema_name, True, str, True])

    # Make sure that a correct type of values has been supplied to the arguments.
    validator._validate_function_arguments(__arg_info_matrix)

    schema_name = schema_name if schema_name is not None else _get_current_databasename()

    # Before proceeding further, check whether table exists or not.
    conn = get_context()
    if not conn.dialect.has_table(conn, table_name=table_name, schema=schema_name):
        error_code = MessageCodes.MODEL_CATALOGING_OPERATION_FAILED
        error_msg = Messages.get_message(
            error_code, "retrieve", 'Table "{}.{}" does not exist.'.format(schema_name, table_name))
        raise TeradataMlException(error_msg, error_code)

    table_name = in_schema(schema_name=schema_name, table_name=table_name)
    model_details = DataFrame(table_name)
    model_details = model_details[model_details.model_id == model_id]

    # __check_if_model_exists does the same check however, but it do not return DataFrame.
    # So, doing the model existence check here.
    if model_details.shape[0] == 0:
        error_code = MessageCodes.MODEL_NOT_FOUND
        error_msg = Messages.get_message(error_code, model_id, " in the table '{}'".format(table_name))
        raise TeradataMlException(error_msg, error_code)

    if model_details.shape[0] > 1:
        error_code = MessageCodes.MODEL_CATALOGING_OPERATION_FAILED
        error_msg = Messages.get_message(
            error_code, "retrieve", "Duplicate model found for model id '{}'".format(model_id))
        raise TeradataMlException(error_msg, error_code)

    # If license holds the actual license key, assign it to model DataFrame.
    # If license holds the column name, i.e., license data is stored in a table,
    #   If table which holds license data is same as model table, select the column.
    #   If table which holds license data is different from model table, create a
    #       DataFrame on the table which holds license data and do cross join with
    #       models DataFrame. The cross join creates a new DataFrame which has columns
    #       of both tables.
    # Note that, license table should hold only one record. so even cartesian
    #   product should hold only record in the DataFrame.

    if not license:
        return model_details.select(["model_id", "model"])

    # Lambda function for attaching the license to model DataFrame.
    _get_license_model_df = lambda license: model_details.assign(drop_columns=True,
                                                                 model_id=model_details.model_id,
                                                                 model=model_details.model,
                                                                 license=license)

    # If user passed a license as a variable, attach it to the model DataFrame.
    if not is_license_column:
        return _get_license_model_df(license)

    # If license exists in the column of the same model table.
    if is_license_column and not license_table_name:
        _Validators._validate_column_exists_in_dataframe(license,
                                                         model_details._metaexpr,
                                                         for_table=True,
                                                         column_arg='license',
                                                         data_arg=table_name)
        return _get_license_model_df(model_details[license])

    # If license exists in the column of the table different from model table.
    license_schema_name = license_schema_name if license_schema_name else schema_name
    license_table = in_schema(license_schema_name, license_table_name)

    # Check whether license table exists or not before proceed further.
    if not conn.dialect.has_table(conn, table_name=license_table_name, schema=license_schema_name):
        error_code = MessageCodes.EXECUTION_FAILED
        error_msg = Messages.get_message(
            error_code, "retrieve the model", 'Table "{}" does not exist.'.format(license_table))
        raise TeradataMlException(error_msg, error_code)

    license_df = DataFrame(license_table)
    # Check column existed in table.
    _Validators._validate_column_exists_in_dataframe(license,
                                                     license_df._metaexpr,
                                                     for_table=True,
                                                     column_arg='license',
                                                     data_arg=license_table)

    if license_df.shape[0] > 1:
        error_code = MessageCodes.MODEL_CATALOGING_OPERATION_FAILED
        error_msg = Messages.get_message(
            error_code, "retrieve", "Table which holds license key should have only one row.")
        raise TeradataMlException(error_msg, error_code)

    model_details = model_details.select(["model_id", "model"])

    # Make sure license is the column name for license key.
    license_df = license_df.assign(drop_columns=True, license=license_df[license])
    return model_details.join(license_df, how="cross")


def list_byom(table_name, schema_name=None, model_id=None):
    """
    DESCRIPTION:
        Function to list models.

    PARAMETERS:
        table_name:
            Required Argument.
            Specifies the name of the table to list models from.
            Types: str

        schema_name:
            Optional Argument.
            Specifies the name of the schema in which the table specified in
            "table_name" is looked up. If not specified, then table is looked
            up in current schema.
            Types: str

        model_id:
            Optional Argument.
            Specifies the unique model identifier of the model(s). If specified,
            the models with either exact match or a substring match, are listed.
            Types: str OR list

    RETURNS:
        None.

    RAISES:
        TeradataMlException, TypeError

    EXAMPLES:
        >>> import teradataml, os, datetime
        >>> model_file = os.path.join(os.path.dirname(teradataml.__file__), 'data', 'models', 'iris_kmeans_model')
        >>> from teradataml import save_byom, list_byom
        >>> save_byom('model7', model_file, 'byom_models')
        Model is saved.
        >>> save_byom('iris_model1', model_file, 'byom_models')
        Model is saved.
        >>> save_byom('model8', model_file, 'byom_models', schema_name='test')
        Model is saved.
        >>>

        # Example 1 - List all the models from the table byom_models.
        >>> list_byom(table_name='byom_models')
                                        model
        model_id
        model7       b'504B03041400080808...'
        iris_model1  b'504B03041400080808...'
        >>>

        # Example 2 - List all the models with model_id containing 'iris' string.
        #             List such models from 'byom_models' table.
        >>> list_byom(table_name='byom_models', model_id='iris')
                                        model
        model_id
        iris_model1  b'504B03041400080808...'
        >>>

        # Example 3 - List all the models with model_id containing either 'iris'
        #             or '7'. List such models from 'byom_models' table.
        >>> list_byom(table_name='byom_models', model_id=['iris', '7'])
                                        model
        model_id
        model7       b'504B03041400080808...'
        iris_model1  b'504B03041400080808...'
        >>>

        # Example 4 - List all the models from the 'byom_models' table and table is
        #             in 'test' DataBase.
        >>> list_byom(table_name='byom_models', schema_name='test')
                                        model
        model_id
        model8       b'504B03041400080808...'
        >>>

    """

    # Let's perform argument validations.
    # Create argument information matrix to do parameter checking
    __arg_info_matrix = []
    __arg_info_matrix.append(["table_name", table_name, False, str, True])
    __arg_info_matrix.append(["schema_name", schema_name, True, str, True])
    __arg_info_matrix.append(["model_id", model_id, True, (str, list), True])

    # Make sure that a correct type of values has been supplied to the arguments.
    validator._validate_function_arguments(__arg_info_matrix)

    # Get the default schema name if not specified in argument "schema_name".
    schema_name = schema_name if schema_name is not None else _get_current_databasename()

    # Before proceed further, check whether table exists or not.
    conn = get_context()
    if not conn.dialect.has_table(conn, table_name=table_name, schema=schema_name):
        error_code = MessageCodes.MODEL_CATALOGING_OPERATION_FAILED
        error_msg = Messages.get_message(
            error_code, "list", 'Table "{}.{}" does not exist.'.format(schema_name, table_name))
        raise TeradataMlException(error_msg, error_code)

    model_details = DataFrame(in_schema(schema_name, table_name))

    filter_condition = None
    if model_id:
        model_ids = UtilFuncs._as_list(model_id)
        for modelid in model_ids:
            # Filter Expression on model_id column.
            # We are looking to find all rows with model_id matching with 'modelid' string.
            # This is case-insensitive look-up.
            filter_expression = __get_like_filter_expression_on_col(model_details._metaexpr,
                                                                    "model_id", modelid)
            filter_condition = filter_condition | filter_expression \
                if filter_condition else filter_expression

    if filter_condition:
        model_details = model_details[filter_condition]

    if model_details.shape[0] != 0:
        orig_max_rows_num = display.max_rows
        try:
            display.max_rows = 99999
            print(model_details)
        except Exception:
            raise
        finally:
            display.max_rows = orig_max_rows_num
    else:
        print("No models found.")
