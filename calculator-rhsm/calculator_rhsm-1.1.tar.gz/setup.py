from setuptools import setup

setup(
    name='calculator_rhsm',
    version='1.1',
    author='Rafael Meireles',
    author_email='rafameireles2011@gmail.com',
    packages=['calculator'],
    description='Uma simples calculadora feita com o Tkinter',
    long_description='Calculadora com funções básicas.' \
                     'Adicionar, subtrair, dividir e multiplicar' \
                     'Entre os vários aprendizados destaco a organização' \
                     'em grid dos botões, selecionar do início (0) ao fim (END).',
    url='https://github.com/rafael-hsm/tkinter-calculator',
    license='MIT',
    keywords='Calculadora básica feita com Tkinter',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Scientific/Engineering :: Physics',
    ]
)
