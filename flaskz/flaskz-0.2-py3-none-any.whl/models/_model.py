from sqlalchemy.exc import IntegrityError

from ._base import BaseModelMixin
from .. import res_status_codes
from ..log import flaskz_logger
from ..utils import is_str, is_dict

__all__ = ['ModelMixin']


class ModelMixin(BaseModelMixin):
    # -------------------------------------------add-------------------------------------------
    @classmethod
    def get_add_data(cls, json_data):
        """
        Return the added json data. By default, return the json data of the client
        Rewrite to customize the added data

        :param json_data: The data to be added
        :return:
        """
        return json_data

    @classmethod
    def before_add(cls, json_data):
        """
        The callback before adding data.
        If the return value is not True, the adding process will be terminated and the result will be returned to the client.
        :param json_data: The data to be added
        :return: True|Error Message
        """
        return True

    @classmethod
    def after_add(cls, json_data, instance, before_result):
        """
        The callback after adding data.

        :param json_data: The data to be added
        :param instance: The result model instance, None if add fails.
        :param before_result: The result of the before_add callback
        :return:
        """
        pass

    @classmethod
    def add(cls, json_data):
        """
         Add the data to the db.
         Returns a tuple.
           --the first value represents whether the add operation was successful, True/False.
           --the second value represent the result of the add operation, reason/instance.

        :param json_data:
        :return:
        """
        instance = None
        try:
            json_data = cls.get_add_data(json_data)
            check_result = cls.check_add_data(json_data)
            if check_result is not True:
                return False, check_result

            before_result = cls.before_add(json_data)
            try:
                if before_result is True:
                    instance = cls.add_db(json_data)
            finally:
                cls.after_add(json_data, instance, before_result)  # after_add execute regardless of whether the addition is successful
        except Exception as e:
            print(e)
            flaskz_logger.exception(e)
            return False, res_status_codes.db_add_err

        if before_result is not True:
            return False, before_result  # ex)db_data_already_exist

        return True, instance

    # -------------------------------------------update-------------------------------------------
    @classmethod
    def get_update_data(cls, json_data):
        """
        Return the updated json data. By default, return the json data of the client
        Rewrite to customize the updated data

        :param json_data: The updated json data
        :return:
        """
        return json_data

    @classmethod
    def before_update(cls, json_data):
        """
        The callback before updating data.
        If the return value is not True, the update process will be terminated and the result will be returned to the client.

        :param json_data:
        :return:
        """
        return True

    @classmethod
    def after_update(cls, json_data, instance, before_result):
        """
        The callback after updating data.

        :param json_data:
        :param instance:
        :param before_result:
        :return:
        """
        pass

    @classmethod
    def update(cls, json_data):
        """
        Update the data to the db.
        Returns a tuple.
           --the first value represents whether the update operation was successful, True/False.
           --the second value represent the result of the update operation, reason/instance.

        :param json_data:
        :return:
        """
        instance = None
        try:
            json_data = cls.get_update_data(json_data)
            check_result = cls.check_update_data(json_data)
            if check_result is not True:
                return False, check_result

            before_result = cls.before_update(json_data)
            try:
                if before_result is True:
                    instance = cls.update_db(json_data)
            finally:
                cls.after_update(json_data, instance, before_result)
        except Exception as e:
            flaskz_logger.exception(e)
            return False, res_status_codes.db_update_err

        if before_result is not True:
            return False, before_result  # ex)db_data_not_found

        if is_str(instance):
            return False, instance
        else:
            return True, instance

    # -------------------------------------------delete-------------------------------------------
    @classmethod
    def get_delete_data(cls, pk_value):
        """
        Return the primary key of the data to be deleted. By default, return the primary key of the client data
        Rewrite to customize the deleted data

        :param pk_value: The primary key of the data to be deleted
        :return:
        """
        return pk_value

    @classmethod
    def before_delete(cls, pk_value):
        """
        The callback before deleting data.
        If the return value is not True, the delete process will be terminated and the result will be returned to the client.

        :param pk_value:
        :return:
        """
        return True

    @classmethod
    def after_delete(cls, pk_value, instance, before_result):
        """
        The callback after deleting data.

        :param pk_value:
        :param instance:
        :param before_result:
        :return:
        """
        pass

    @classmethod
    def delete(cls, pk_value):
        """
        Delete the data from the db.
        Returns a tuple.
           --the first value represents whether the delete operation was successful, True/False.
           --the second value represent the result of the delete operation, reason/instance.

        :param pk_value:
        :return:
        """
        if is_dict(pk_value):  # {id:10}
            pk_value = cls._get_pk_value(pk_value)

        instance = None
        try:
            pk_value = cls.get_delete_data(pk_value)
            check_result = cls.check_delete_data(pk_value)
            if check_result is not True:
                return False, check_result

            before_result = cls.before_delete(pk_value)
            try:
                if before_result is True:
                    instance = cls.delete_db(pk_value)
            finally:
                cls.after_delete(pk_value, instance, before_result)
        except IntegrityError as e:
            flaskz_logger.exception(e)
            return False, res_status_codes.db_data_in_use
        except Exception as e:
            flaskz_logger.exception(e)
            return False, res_status_codes.db_delete_err

        if before_result is not True:
            return False, before_result

        if is_str(instance):
            return False, instance
        else:
            return True, instance

    # -------------------------------------------query-------------------------------------------
    @classmethod
    def query_all(cls):
        """
        Override the base query_all method and return success flag
        Used in router to return query data
        :return:
        """
        try:
            return True, super().query_all()
        except Exception as e:
            flaskz_logger.exception(e)
            return False, res_status_codes.db_query_err

    @classmethod
    def query_pss(cls, pss_option):
        """
        Override the base query_pss method and return success flag
        Used in router to return query data
        :param pss_option:
        :return:
        """
        try:
            return True, super().query_pss(pss_option)
        except Exception as e:
            flaskz_logger.exception(e)
            return False, res_status_codes.db_query_err
