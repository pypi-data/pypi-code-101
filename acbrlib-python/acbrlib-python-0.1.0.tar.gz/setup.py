# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['acbrlib_python', 'acbrlib_python.cep']

package_data = \
{'': ['*']}

install_requires = \
['Unidecode>=1.3.2,<2.0.0']

setup_kwargs = {
    'name': 'acbrlib-python',
    'version': '0.1.0',
    'description': 'Camada de abstração para acesso à ACBrLib em Python',
    'long_description': "\n==============\nACBrLib Python\n==============\n\n|PyPI pyversions| |PyPI version fury.io| |PyPI license|\n\nCamada de abstração para acesso à `ACBrLib`_ em Python.\n\n----\n\n`ACBrLib`_ é um conjunto de bibliotecas voltadas para o mercado de\nautomação comercial que oferece acesso à um conjunto rico de abstrações\nque facilitam o desenvolvimento de aplicações como pontos-de-venda (PDV) e\naplicações relacionadas. Esta biblioteca fornece uma camada que torna\ntrivial a utilização da `ACBrLib`_ em seus próprios aplicativos escritos em\n`linguagem Python <https://www.python.org>`_.\n\n.. note::\n\n    Esta biblioteca está em seus primeiros estágios de desenvolvimento,\n    portanto, não espere encontrar toda a riqueza que os componentes\n    `ACBr`_ possuem, por enquanto. Mas estamos totalmente abertos a\n    `sujestões`_ e estamos aceitando `pull-requests`_.\n\n\nInstalação\n----------\n\nInstale, preferencialmente em um ambiente virtual, usando ``pip``:\n\n.. code-block:: shell\n\n    pip install acbrlib-python\n\n\nACBrLibCEP\n----------\n\nDá acesso a consultas de CEP utilizando dezenas de serviços de consulta\ndisponíveis. Alguns desses serviços podem ser gratuítos ou gratuítos para\ndesenvolvimento. Veja `este link <https://acbr.sourceforge.io/ACBrLib/ConfiguracoesdaBiblioteca8.html>`_\npara ter uma ideia dos serviços que podem ser utilizados.\n\nPara fazer uma consulta baseada no CEP:\n\n.. code-block:: python\n\n    from acbrlib_python import ACBrLibCEP\n\n    with ACBrLibCEP.usando('/caminho/para/libacbrcep64.so') as cep:\n        enderecos = cep.buscar_por_cep('18270170')\n        for endereco in enderecos:\n            print(endereco)\n\nO trecho acima resultará em uma lista de objetos ``Endereco`` como resultado\nda busca, prontos para serem usados. A consulta acima trará um único resultado\n(usando o serviço `ViaCEP <https://viacep.com.br/>`_):\n\n.. code-block:: python\n\n    Endereco(\n            tipo_logradouro='',\n            logradouro='Rua Coronel Aureliano de Camargo',\n            complemento='',\n            bairro='Centro',\n            municipio='Tatuí',\n            uf='SP',\n            cep='18270-170',\n            ibge_municipio='3554003',\n            ibge_uf='35'\n        )\n\nPara mais exemplos de uso, veja a pasta ``exemplos`` neste repositório.\n\n\nSobre Nomenclatura e Estilo de Código\n=====================================\n\nUma questão muito relevante é a maneira como esta abstração se refere aos\nnomes dos métodos disponíveis na biblioteca `ACBrLib`_ que utiliza uma\nconvenção de nomenclatura para variáveis e nomes de argumentos ou\nparâmetros de funções conhecida como `Notação Húngara <https://pt.wikipedia.org/wiki/Nota%C3%A7%C3%A3o_h%C3%BAngara>`_.\nPorém, em Python é utilizada a convenção `snake case <https://en.wikipedia.org/wiki/Snake_case>`_\ntal como descrito na `PEP8 <https://www.python.org/dev/peps/pep-0008/>`_.\n\nAssim, para manter o estilo de Python, os nomes de variáveis e argumentos de\nfunção deverão descartar o prefixo que indica o tipo de dado e converter o\nrestante para snake case, assim como nomes de métodos e funções também,\npor exemplo:\n\n* `eArqConfig` para `arq_config`;\n* `ConfigLerValor` para `config_ler_valor`;\n* `eArquivoXmlEvento` para `arquivo_xml_evento`;\n* etc…\n\nMétodos de bibliotecas que são prefixados com o nome da lib, será descartado o\nprefixo e o restante do nome do método convertido para snake case, por exemplo:\n\n* (ACBrLibNFe) `NFE_CarregarINI` para `carregar_ini`;\n* (ACBrLibNFe) `NFE_ValidarRegrasdeNegocios` para `validar_regras_de_negocios`\n  (note a correção do conector `de` que está em minúsculo no original);\n* (ACBrLibCEP) `CEP_BuscarPorLogradouro` para `buscar_por_logradouro`;\n* etc…\n\nEsperamos que essa explicação faça sentido, senão, envia suas `sujestões`_.\n\n\nDesenvolvimento\n===============\n\nVocê é bem-vindo para ajudar no desenvolvimento desta biblioteca enviando\nsuas contribuições através de `pull-requests`_. Faça um *fork* deste\nrepositório e execute os testes antes de começar a implementar alguma\ncoisa. A gestão de dependências é feita via `Poetry`_ e recomendamos a\nutilização de `pyenv`_\n\n.. code-block:: shell\n\n    $ git clone https://github.com/base4sistemas/acbrlib-python.git\n    $ cd acbrlib-python\n    $ poetry install\n    $ poetry run pytest\n\n\n.. _`sujestões`: https://github.com/base4sistemas/acbrlib-python/issues\n.. _`pull-requests`: https://github.com/base4sistemas/acbrlib-python/pulls\n.. _`ACBr`: https://projetoacbr.com.br/\n.. _`ACBrLib`: https://projetoacbr.com.br/downloads/#acbrlib\n.. _`pyenv`: https://github.com/pyenv/pyenv\n.. _`Poetry`: https://python-poetry.org/\n\n.. |PyPI pyversions| image:: https://img.shields.io/pypi/pyversions/acbrlib-python.svg\n   :target: https://pypi.python.org/pypi/acbrlib-python/\n\n.. |PyPI version fury.io| image:: https://badge.fury.io/py/acbrlib-python.svg\n   :target: https://pypi.python.org/pypi/acbrlib-python/\n\n.. |PyPI license| image:: https://img.shields.io/pypi/l/acbrlib-python.svg\n   :target: https://pypi.python.org/pypi/acbrlib-python/\n",
    'author': 'Daniel Gonçalves',
    'author_email': 'daniel@base4.com.br',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/base4sistemas/acbrlib-python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
