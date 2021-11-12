from typing import Any, Dict

from airflow.hooks.base import BaseHook
from airflow.exceptions import AirflowFailException


class SIAFIHook(BaseHook):
    '''Hook base para conexão com o SIAFI.

    :param id_conexao: referência para conexão
    :type id_conexao: str
    '''
    conn_name_attr = 'siafi_conn_id'
    default_conn_name = 'siafi_default'
    conn_type = 'siafi'
    hook_name = 'Conta do SIAFI'

    cpf: str
    senha: str
    nome: str
    ug: str
    nivel: int

    def __init__(self, id_conexao: str) -> None:
        super().__init__()

        connection = self.get_connection(id_conexao)

        if connection.conn_type != self.conn_type:
            raise AirflowFailException(
                f'ID da conexão não é do tipo {self.conn_type}'
            )

        self.cpf = connection.login
        self.senha = connection.password
        self.nome = connection.extra_dejson['extra__siafi__nome']
        self.ug = connection.extra_dejson['extra__siafi__ug']
        self.nivel = int(connection.extra_dejson['extra__siafi__nivel'])

    @staticmethod
    def get_connection_form_widgets() -> Dict[str, Any]:
        '''Retorna formulário de conexão siafi'''
        from flask_appbuilder.fieldwidgets import (
            BS3TextFieldWidget, Select2Widget,
        )
        from flask_babel import lazy_gettext
        from wtforms import StringField, SelectField

        return {
            'extra__siafi__nome': StringField(
                lazy_gettext('Nome Completo'),
                widget=BS3TextFieldWidget()
            ),
            'extra__siafi__ug': StringField(
                lazy_gettext('UG'),
                widget=BS3TextFieldWidget()
            ),
            'extra__siafi__nivel': SelectField(
                lazy_gettext('Nível'),
                choices=list(range(1, 10)),
                widget=Select2Widget(),
            ),
        }

    @staticmethod
    def get_ui_field_behaviour() -> Dict:
        '''Customiza comportamento dos formulários.'''
        return {
            'hidden_fields': ['host', 'port', 'schema', 'extra',
                              'description'],
            'relabeling': {
                'conn_id': 'ID da conexão',
                'conn_type': 'Tipo de conexão',
                'login': 'CPF',
                'password': 'Senha'
            }
        }
