#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""
"""

from __future__ import print_function
from iar_inflector.acep_consts import FORMA
from iar_inflector.acep_consts import SUSTANTIVO, ADJETIVO, DETERMINANTE, PRONOMBRE, VERBO, ADVERBIO,\
    PREPOSICION, CONJUNCION, INTERJECCION, EXPRESION, ONOMATOPEYA, AFIJO, ABREVIATURA, SIGLA, SIMBOLO,\
    DESCONOCIDA, SUFIJO, PREFIJO
from iar_inflector.flexionador import Flexionador
from iar_inflector.parseador_wikci_consts import MARCA_ENTRADA_REGEX
from iar_inflector.acepcion import AcepcionWik
from iar_inflector.lema import Lema
from iar_inflector.entrada import Entrada

import urllib
import bz2
import bz2file
import os
import re
import ujson
try:
    from winsound import Beep as beep
except ImportError:
    def beep(frecuencia, duracion):
        pass
import xml.etree.ElementTree as ElementTree
from os.path import isfile, dirname
import sys
if sys.version_info.major == 2:
    import cPickle as pickle
elif sys.version_info.major == 3:
    import pickle

__author__ = "Iván Arias Rodríguez"
__copyright__ = "Copyright 2017, Iván Arias Rodríguez"
__credits__ = [""]
__license__ = "GPL"  # No estoy seguro
__version__ = "1.0.1"
__maintainer__ = "Iván Arias Rodríguez"
__email__ = "ivan.arias.rodriguez@gmail.com"
__status__ = "Development"  # "Prototype", "Production"


class ParseadorWikcionario:
    def __init__(self):
        pass

    @staticmethod
    def crea_lemario_previo(actualiza_archivo_raw=False):
        # Primero creamos un lemario previo con la información de los archivos. Lo que hacemos es coger el archivo
        # grande con el contenido del Wikcionario al completo, y lo troceamos en artículos. Cada uno de esos trozos
        # (que es un string sin más) lo metemos en un diccionario cuya clave será el lema.
        directorio_trabajo = dirname(os.path.realpath(__file__)) + u'\\archivos_de_datos\\wik\\lemario\\'
        if not os.path.exists(directorio_trabajo):
            os.makedirs(directorio_trabajo)
        print(u'Creando lemario previo...')
        lemario_previo = {}
        nombre_archivo_raw = u'eswiktionary-latest-pages-articles-multistream.xml.bz2'
        path_archivo_raw = directorio_trabajo + nombre_archivo_raw

        # Si no tenemos el archivo con el contenido del Wikcionario, o queremos actualizarlo descargamos la última
        # versión de la web del Wikcionario. Son unos 90MB comprimidos. El archivo que se baja es
        # https://dumps.wikimedia.org/eswiktionary/latest/eswiktionary-latest-pages-articles-multistream.xml.bz2
        if not isfile(path_archivo_raw) or actualiza_archivo_raw:
            # No lo tenemos descargado o lo queremos recargar, así que lo bajamos. Tarda un par de minutos.
            print(u'Descargando de https://dumps.wikimedia.org/eswiktionary/latest/' + nombre_archivo_raw + u'...', end=u' ')
            urllib.urlretrieve(u'https://dumps.wikimedia.org/eswiktionary/latest/' + nombre_archivo_raw,
                               path_archivo_raw)
            print(u'descargado.')

        # Leemos el archivo raw del Wikcionario y lo separamos en artículos. Como el archivo es xml, el texto de
        # cada artículo aparece entre las etiquetas <page>...</page>, así que identificamos estas etiquetas en
        # el texto y nos quedamos con lo intermedio. De cada artículo obtendremos un string con toda la información.
        n_articulos_procesados = 0
        # Es necesario usar bz2file.open porque el archivo es multistream, y bz2.BZ2File no lo soporta
        with bz2file.open(path_archivo_raw, 'rt', encoding="utf-8") as archivo_entrada:
            texto_articulo_xml = u''
            while True:
                texto = archivo_entrada.readline()
                if not texto:
                    # Hemos acabado de trocear el archivo.
                    break
                # Aún no ha acabado el archivo.
                if u'<page>' in texto or texto_articulo_xml:
                    # Comenzamos un artículo o estábamos en un artículo que no se había cerrado. Añadimos el texto.
                    texto_articulo_xml += texto
                    if u'</page>' in texto:
                        # Hemos llegado al final del artículo, así que lo procesamos.
                        articulo = ElementTree.fromstring(texto_articulo_xml.encode('utf-8'))
                        texto_articulo_xml = ''
                        if n_articulos_procesados % 10000 == 0 and n_articulos_procesados:
                            print(n_articulos_procesados, u'artículos procesados.', \
                                len(lemario_previo), u'lemas extraídos')
                        n_articulos_procesados += 1
                        # No guardaremos en el lemario previo los artículos de temas internos del Wikcionario que no
                        # sean artículos propiamente dichos, además de redirecciones y artículos vacíos o sin estructura
                        lema_txt = articulo.find('title').text.replace(u':', u'_')
                        if u'_' in lema_txt:
                            if lema_txt.split(u'_')[0].lower() \
                                    in [u'categoría', u'plantilla', u'apéndice', u'ayuda', u'wikcionario',
                                        u'mediawiki', u'archivo', u'módulo']:
                                # Es un artículo pero no de un lema, sino de temas del wikcionario. No nos interesa.
                                continue
                            else:
                                print(u'El lema', lema_txt, u'es sospechoso de ser una página especial y se descarta')
                                continue
                        # Sacamos del XML el texto del artículo en sí
                        texto_articulo = articulo.find('revision').find('text').text
                        if not texto_articulo:
                            # Está vacío
                            continue
                        # Vemos si es un #REDIRECT, #REDIRECCIÓN
                        if u'#redirec' in texto_articulo.lower():
                            # Es un artículo de redirección, no interesa
                            continue
                        # Quizá sea un archivo SIN ESTRUCTURA
                        if u'{{estructura}}' in texto_articulo.lower() or u'{{formato}}' in texto_articulo.lower():
                            # Al artículo le falta estructura, y no es parseable
                            continue
                        if lema_txt == u'acabado':
                            pass
                        if lema_txt in lemario_previo:
                            print(u'¿Cómo es posible que', lema_txt, u'aparezca más de una vez?')
                        lemario_previo[lema_txt] = texto_articulo
        print(n_articulos_procesados, u'artículos procesados.', len(lemario_previo), u'lemas extraídos')
        nombre_archivo_lemario_previo = directorio_trabajo + u'lemario_previo_wik.pkl.bz2'
        print(u'Guardando lemario previo en ...\\' + u'\\'.join(nombre_archivo_lemario_previo.split(u'\\')[-5:]))
        try:
            os.remove(nombre_archivo_lemario_previo)
        except OSError:
            pass
        with bz2.BZ2File(nombre_archivo_lemario_previo, 'wb') as archivo_lemario_previo:
            pickle.dump(lemario_previo, archivo_lemario_previo, -1)

        return lemario_previo

    @staticmethod
    def crea_lemario(actualiza_archivo_raw=False, crea_lemario_previo=False,
                     elimina_formas=True, elimina_locuciones=True):
        """Toma el archivo de texto (disponible en la web del Wikcionario) con los artículos y devuelve un lemario.

        El archivo se identifica por su nombre, y en caso de no aportar un nombre o de que se indique que se quiere
        actualizar el archivo, se descarga la versión actual disponible en la web del Wikcionario.
        Se extraen los textos de los artículos y se eliminan aquellos que no son lemas válidos, incluyendo las formas
        flexionadas o las locuciones según se indica en los parámetros.

        :param crea_lemario_previo:
        :param actualiza_archivo_raw:
        :param elimina_formas:
        :param elimina_locuciones:
        """
        directorio_trabajo = dirname(os.path.realpath(__file__)) + u'\\archivos_de_datos\\wik\\lemario\\'
        if not os.path.exists(directorio_trabajo):
            os.makedirs(directorio_trabajo)

        # De cada artículo obtendremos un lema, con una o más entradas (y cada entrada tiene una acepción únicamente).
        # La forma de procesar el Wikcionario es ligeramente distinta que el procesado de la RAE:
        # - En la RAE, un lema como "parecer" tiene dos entradas: una como verbo y otra como nombre. A su vez,
        #   cada una de estas dos entradas tiene una serie de acepciones: el verbo tiene 6 acepciones y el nombre
        #   tiene 2 (además de tener unas cuantas locuciones cada una). Cada una de las acepciones tiene sus
        #   propios datos morfológicos, fácilmente identificables (en abreviaturas), y por ejemplo, hay acepciones
        #   de verbo que son copulativas, intransitivas o pronominal, según.
        # - En el Wikcionario, "parecer" tiene también dos entradas: una como verbo y otra como nombre. La acepción
        #   como verbo tiene 4 acepciones, y como nombre 2. Sin embargo, en el Wikcionario las acepciones, aunque
        #   tienen información morfológica asociada, no está claramente identificada. Tienen datos de uso (poco
        #   frecuente...), sinónimos y relacionados, incluso datos sobre el ámbito, además de la propia definición
        #   en sí. Pero no está demasiado bien estructurado, y los datos morfológicos (sustantivo femenino..., así
        #   como los datos de flexión y demás) están dados por entrada y no por acepción dentro de una entrada.
        # Siendo esto así, aunque se podría hacer un parseador más complejo donde se podría extraer esta información,
        # lo que se hace en el Wikcionario es que simplemente se considera que cada entrada tiene una única acepción,
        # y no guardamos la información de la definición ni nada.
        # TODO: mirar si se puede extraer más información del Wikcionario de la que se extrae ahora mismo.
        ''' ESTO ESTÁ OBSOLETO. Cuando termines de actualizar, bórralo.
        # La estructura del lemario (tanto RAE como Wikcionario) es:  ESTO ESTÁ OBSOLETO
        # lemario[u'japonés'] = {"_lema_txt": u'japonés',
        #                        "_entradas": [{"_n_entrada": 0,
        #                                       "_accepciones": [AcepcionWik] Para Wik solo hay una acepcion por entrada
        #                                      },
        #                                      {"_n_entrada": 1, ...}
        #                                     ]
        #                       }
        '''
        if crea_lemario_previo:
            lemario_previo = ParseadorWikcionario.crea_lemario_previo(actualiza_archivo_raw)
        else:
            # Usamos el archivo con los artículos ya cortados, y no creamos uno nuevo
            nombre_archivo_lemario_previo = directorio_trabajo + u'lemario_previo_wik.pkl.bz2'
            print(u'No creamos el lemario previo. Lo cargamos de:', nombre_archivo_lemario_previo)
            with bz2.BZ2File(nombre_archivo_lemario_previo, 'rb') as archivo_lemario_previo:
                lemario_previo = pickle.load(archivo_lemario_previo)

        # Ahora convertimos esta estructura previa en la estructura con entradas, acepciones... estándar
        print(u'Creando lemario...')
        lemario = {}
        n_articulos_procesados = 0
        for lema_txt, texto_articulo in sorted(lemario_previo.items()):
            if n_articulos_procesados % 10000 == 0 and n_articulos_procesados:
                print(n_articulos_procesados, u'artículos procesados.', len(lemario), u'lemas extraídos')
            n_articulos_procesados += 1
            if False:
                if lema_txt < u'zollipar':
                    continue
                print(u'BORRA LA LÍNEA ANTERIOR PORQUE ESTAMOS SALTANDO COSAS')
            if False:
                lema_txt_inicio = u'alcohol'
                if lema_txt_inicio and lema_txt < lema_txt_inicio:
                    continue
                if lema_txt == lema_txt_inicio:
                    print(u'Nos hemos saltado hasta la palabra', lema_txt_inicio)
            if len(lema_txt.split()) > 1 and elimina_locuciones:
                continue
            # Con el texto del artículo para este lema, creamos una serie de entradas.
            # En un artículo se puede encontrar una entrada (normalmente marcada con el inicio del tipo {{lengua|es}})
            # o varias entradas (con los inicios marcados con {{ES||1}} -donde el número es el número de la acepción-).
            # Uno de los muchos ejemplos de lemas con múltiples entradas es "churra" (aunque varias de ellas son formas
            # que vamos a eliminar). Otro con una única entrada es "churro" (que por otra parte, tiene varias
            # etimologías, pero nosotros no lo dividimos en varias entradas, y lo dejamos como acepciones distintas de
            # una misma entrada).
            # Dentro de cada entrada, hay varias acepciones, que a su vez están agrupadas por categoría gramatical,
            # presidiendo cada grupo algún tipo de información de flexión.
            # TODO: Esto ha cambiado porque ahora sí que hay entradas y acepciones.
            entradas = ParseadorWikcionario.parsea_entradas_de_articulo(lema_txt, texto_articulo,
                                                                        elimina_formas, elimina_locuciones)
            if entradas:  # Si el supuesto lema es una forma, no habrá entradas
                lema = Lema(lema_txt, entradas)
                lemario[lema_txt] = lema
        print(n_articulos_procesados, u'artículos procesados.', len(lemario), u'lemas extraídos')

        nombre_archivo_lemario = directorio_trabajo + u'lemario_wik.pkl.bz2'
        print(u'Guardando lemario en', nombre_archivo_lemario, u'...', end=u' ')
        try:
            os.remove(nombre_archivo_lemario)
        except OSError:
            pass
        with bz2.BZ2File(nombre_archivo_lemario, 'wb') as archivo_lemario:
            pickle.dump(lemario, archivo_lemario, -1)
        print(u'guardado.')
        return lemario

    @staticmethod
    # BORRABLE
    def crea_lemario_viejo(actualiza_archivo=False, elimina_formas=True, elimina_locuciones=True,
                           usa_dict_articulos=True, crea_dict_articulos=False, verboso=True):
        """Toma el archivo de texto (disponible en la web del Wikcionario) con los artículos y devuelve un lemario.

        El archivo se identifica por su nombre, y en caso de no aportar un nombre o de que se indique que se quiere
        actualizar el archivo, se descarga la versión actual disponible en la web del Wikcionario.
        Se extraen los textos de los artículos y se eliminan aquellos que no son lemas válidos, incluyendo las formas
        flexionadas o las locuciones según se indica en los parámetros.

        :param nombre_archivo_raw:
        :param actualiza_archivo:
        :param elimina_formas:
        :param elimina_locuciones:
        :param usa_dict_articulos:
        :param crea_dict_articulos:
        :param verboso:
        """
        directorio_trabajo = dirname(os.path.realpath(__file__)) + u'\\archivos_de_datos\\wik\\lemario\\'
        if not os.path.exists(directorio_trabajo):
            os.makedirs(directorio_trabajo)
        nombre_archivo = u'eswiktionary-latest-pages-articles-multistream.xml.bz2'
        nombre_archivo_raw = directorio_trabajo + nombre_archivo

        # Si no tenemos el archivo con el contenido del Wikcionario, o queremos actualizarlo descargamos la última
        # versión de la web del Wikcionario. Son unos 90MB comprimidos. El archivo que se baja es
        # https://dumps.wikimedia.org/eswiktionary/latest/eswiktionary-latest-pages-articles-multistream.xml.bz2
        if not isfile(nombre_archivo_raw) or actualiza_archivo:
            # No lo tenemos descargado o lo queremos recargar, así que lo bajamos. Tarda un par de minutos.
            print(u'Descargando de https://dumps.wikimedia.org/eswiktionary/latest/' + nombre_archivo + u'...', end=u' ')
            urllib.urlretrieve(u'https://dumps.wikimedia.org/eswiktionary/latest/' + nombre_archivo, nombre_archivo_raw)
            print(u'descargado.')

        # Leemos el archivo raw del Wikcionario y lo separamos en artículos. Como el archivo es xml, el texto de
        # cada artículo aparece entre las etiquetas <page>...</page>, así que identificamos estas etiquetas en
        # el texto y nos quedamos con lo intermedio. De cada artículo obtendremos un lema, con una o más entradas.
        # La forma de procesar el Wikcionario es ligeramente distinta que el procesado de la RAE:
        # - En la RAE, un lema como "parecer" tiene dos entradas: una como verbo y otra como nombre. A su vez,
        #   cada una de estas dos entradas tiene una serie de acepciones: el verbo tiene 6 acepciones y el nombre
        #   tiene 2 (además de tener unas cuantas locuciones cada una). Cada una de las acepciones tiene sus
        #   propios datos morfológicos, fácilmente identificables (en abreviaturas), y por ejemplo, hay acepciones
        #   de verbo que son copulativas, intransitivas o pronominal, según.
        # - En el Wikcionario, "parecer" tiene también dos entradas: una como verbo y otra como nombre. La acepción
        #   como verbo tiene 4 acepciones, y como nombre 2. Sin embargo, en el Wikcionario las acepciones, aunque
        #   tienen información morfológica asociada, no está claramente identificada. Tienen datos de uso (poco
        #   frecuente...), sinónimos y relacionados, incluso datos sobre el ámbito, además de la propia definición
        #   en sí. Pero no está demasiado bien estructurado, y los datos morfológicos (sustantivo femenino..., así
        #   como los datos de flexión y demás) están dados por entrada y no por acepción dentro de una entrada.
        # Siendo esto así, aunque se podría hacer un parseador más complejo donde se podría extraer esta información,
        # lo que se hace en el Wikcionario es que simplemente se considera que cada entrada tiene una única acepción,
        # y no guardamos la información de la definición ni nada.
        # TODO: mirar si se puede extraer más información del Wikcionario de la que se extrae ahora mismo.
        # La estructura del lemario (tanto RAE como Wikcionario) es:  ESTO ESTÁ OBSOLETO
        # lemario[u'japonés'] = {"_lema_txt": u'japonés',
        #                        "_entradas": [{"_n_entrada": 0,
        #                                       "_accepciones": [AcepcionWik] Para Wik solo hay una acepcion por entrada
        #                                      },
        #                                      {"_n_entrada": 1, ...}
        #                                     ]
        #                       }
        lemario = {}
        dict_articulos = {}
        if usa_dict_articulos and not crea_dict_articulos:
            # Usamos el archivo con los artículos preprocesados, y no creamos uno nuevo
            nombre_archivo_dict_articulos = directorio_trabajo + u'dict_articulos_wik.pkl.bz2'
            print(u'Cargando archivo de artículos previamente troceado:', nombre_archivo_dict_articulos)
            with bz2.BZ2File(nombre_archivo_dict_articulos, 'rb') as entrada:
                dict_articulos = pickle.load(entrada)
        else:
            n_articulos_procesados = 0
            # Es necesario usar bz2file.open porque el archivo es multistream, y bz2.BZ2File no lo soporta
            with bz2file.open(nombre_archivo_raw, 'rt', encoding="utf-8") as archivo_entrada:
                texto_articulo_xml = u''
                while True:
                    texto = archivo_entrada.readline()
                    if not texto:
                        # Hemos acabado de trocear el archivo (y de procesarlo si no usamos el dict de artículos)
                        print(n_articulos_procesados, u'artículos procesados.', \
                            len(lemario) if not usa_dict_articulos else len(dict_articulos), u'lemas extraídos')
                        if crea_dict_articulos:
                            nombre_archivo_dict_articulos = directorio_trabajo + u'dict_articulos_wik.pkl.bz2'
                            with bz2.BZ2File(nombre_archivo_dict_articulos, 'wb') as archivo_dict_articulos:
                                pickle.dump(dict_articulos, archivo_dict_articulos, -1)
                        break
                    # Aún no ha acabado el archivo.
                    if u'<page>' in texto or texto_articulo_xml:
                        # Comenzamos un artículo o estábamos en un artículo que no se había cerrado. Añadimos el texto.
                        texto_articulo_xml += texto
                        if u'</page>' in texto:
                            # Hemos llegado al final del artículo, así que lo procesamos.
                            articulo = ElementTree.fromstring(texto_articulo_xml.encode('utf-8'))
                            texto_articulo_xml = ''
                            if n_articulos_procesados % 10000 == 0 and n_articulos_procesados:
                                print(n_articulos_procesados, u'artículos procesados.',\
                                    len(lemario) if not usa_dict_articulos else len(dict_articulos), u'lemas extraídos')
                            n_articulos_procesados += 1
                            lema_txt = articulo.find('title').text.replace(u':', u'_')
                            if u'_' in lema_txt:
                                if lema_txt.split(u'_')[0].lower() \
                                        in [u'categoría', u'plantilla', u'apéndice', u'ayuda', u'wikcionario',
                                            u'mediawiki', u'archivo', u'módulo']:
                                    # Es un artículo pero no de un lema, sino de temas del wikcionario
                                    continue
                                elif verboso:
                                    print(u'El lema', lema_txt, u'es sospechoso de ser una página especial')
                            if len(lema_txt.split()) > 1 and elimina_locuciones:
                                continue
                            # Sacamos del XML el texto del artículo en sí
                            texto_articulo = articulo.find('revision').find('text').text
                            if not texto_articulo:
                                # Está vacío
                                continue
                            # Vemos si es un #REDIRECT, #REDIRECCIÓN
                            if u'#redirec' in texto_articulo.lower():
                                # Es un artículo de redirección, no interesa
                                continue
                            # Quizá sea un archivo SIN ESTRUCTURA
                            if u'{{estructura}}' in texto_articulo.lower() or u'{{formato}}' in texto_articulo.lower():
                                # Al artículo le falta estructura, y no es parseable
                                continue
                            if lema_txt == u'acabado':
                                pass
                            if crea_dict_articulos:
                                if lema_txt in dict_articulos:
                                    print(u'¿Cómo es posible que', lema_txt, u'aparezca más de una vez?')
                                dict_articulos[lema_txt] = texto_articulo
                            if not usa_dict_articulos:
                                entradas = ParseadorWikcionario.\
                                    parsea_entradas_de_articulo(lema_txt, texto_articulo,
                                                                elimina_formas, elimina_locuciones)
                                if entradas:
                                    lema = Lema(lema_txt, entradas)
                                    lemario[lema_txt] = lema

        if usa_dict_articulos:
            print(u'\nUsando el dict de artículos troceados y procesando...')
            n_articulos_procesados = 0
            for lema_txt, texto_articulo in sorted(dict_articulos.items()):
                if n_articulos_procesados % 10000 == 0 and n_articulos_procesados:
                    print(n_articulos_procesados, u'artículos procesados.', len(lemario), u'lemas extraídos')
                n_articulos_procesados += 1
                if False and lema_txt < u'al':
                    continue
                entradas = ParseadorWikcionario.parsea_entradas_de_articulo(lema_txt, texto_articulo,
                                                                            elimina_formas, elimina_locuciones)
                if entradas:  # Si el supuesto lema es una forma, no habrá entradas
                    lema = Lema(lema_txt, entradas)
                    lemario[lema_txt] = lema

        nombre_archivo_lemario = directorio_trabajo + u'lemario_wik.pkl.bz2'
        print(u'Guardando lemario en', nombre_archivo_lemario, u'...', end=u' ')
        try:
            os.remove(nombre_archivo_lemario)
        except OSError:
            pass
        with bz2.BZ2File(nombre_archivo_lemario, 'wb') as archivo_lemario:
            pickle.dump(lemario, archivo_lemario, -1)
        print(u'guardado.')
        return lemario

    @staticmethod
    def subdivide_lemario_wik(lemario=None, nombre_archivo_lemario=None):
        u"""Se toma el lemario completo y se subdivide en partes según su categoría y su tipo.

        :type lemario: {unicode: Lema}
        :param lemario:
        :type nombre_archivo_lemario: unicode
        :param nombre_archivo_lemario: Path completo del archivo que contiene el lemario del Wikcionario
        :return:
        """
        lemario_subdividido = {}
        directorio_trabajo = dirname(os.path.realpath(__file__)) + u'\\archivos_de_datos\\wik\\lemario\\'
        if not lemario:
            if not nombre_archivo_lemario:
                nombre_archivo_lemario =\
                    directorio_trabajo + u'lemario_wik.pkl.bz2'
                if not os.path.exists(nombre_archivo_lemario):
                    ParseadorWikcionario.crea_lemario()
            with bz2.BZ2File(nombre_archivo_lemario, 'rb') as entrada:
                lemario = pickle.load(entrada)
        n_lemas_con_n_entradas = {}
        n_acepciones_unicas = 0  # En realidad es la suma de la cantidad de lemas que aparecen en cada categoría
        n_verbos_dobles = 0
        verbos_dobles = set()
        nombres_propios = set()
        adverbios_mente = set()
        lemas_femeninos = {SUSTANTIVO: {}, ADJETIVO: {}, SUFIJO: {}, PRONOMBRE: {}, DETERMINANTE: {}}
        lemas_plurales = {SUSTANTIVO: {}, ADJETIVO: {}, SUFIJO: {}, PRONOMBRE: {}, DETERMINANTE: {}}
        flexiones = {}
        categoria_a_txt = {SUSTANTIVO: u'Sustantivo', ADJETIVO: u'Adjetivo', DETERMINANTE: u'Determinante',
                           PRONOMBRE: u'Pronombre', VERBO: u'Verbo', ADVERBIO: u'Adverbio',
                           PREPOSICION: u'Preposición', CONJUNCION: u'Conjunción',
                           INTERJECCION: u'Interjección',
                           EXPRESION: u'Expresión', ONOMATOPEYA: u'Onomatopeya', AFIJO: u'Afijo',
                           PREFIJO: u'Prefijo', SUFIJO: u'Sufijo',
                           ABREVIATURA: u'Abreviatura', SIGLA: u'Sigla',
                           SIMBOLO: u'Símbolo', DESCONOCIDA: u'Desconocida'}
        for (lema_txt, lema) in sorted(lemario.items(), key=lambda tupla: tupla[0]):
            for orden_entrada, entrada in enumerate(lema.get_entradas()):
                n_lemas_con_n_entradas[orden_entrada + 1] = n_lemas_con_n_entradas.setdefault(orden_entrada + 1, 0) + 1
                if orden_entrada > 0:
                    n_lemas_con_n_entradas[orden_entrada] -= 1
                # Las entradas del Wikcionario solo tienen una acepcion. Además, no se consideran las subacepciones.
                if len(entrada.get_acepciones()) != 1:
                    print(u'Estamos suponiendo cosas raras para', lema_txt, u'porque tiene un número de acepciones raro')
                acepcion = entrada.get_acepciones()[0]

                categoria = acepcion.get_categoria()
                if not categoria:
                    print(u'El lema', lema_txt, u'no tiene categoría')

                # RECUENTO DE TIPOS DE FLEXIÓN
                for conj in acepcion.get_conjs() + acepcion.get_inflects():
                    if (acepcion.get_conjs() and categoria not in VERBO) \
                            or (
                            acepcion.get_inflects() and (categoria not in SUSTANTIVO + ADJETIVO + SUFIJO +
                                                         PRONOMBRE + DETERMINANTE + SIGLA + INTERJECCION +
                                                         ABREVIATURA + PREPOSICION
                                                         or (categoria == PREPOSICION
                                                             and lema_txt[:3] != u'con'))):
                        if False:
                            print(categoria_a_txt[categoria], u'con flexión incorrecta:', lema_txt, u'->',
                                  u', '.join(acepcion.get_conjs() + acepcion.get_inflects()))
                    else:
                        flexiones.setdefault(categoria, set()).add(conj.split(u'|')[0])

                # RECUENTOS DE LEMAS REPETIDOS
                if categoria == VERBO:
                    if (lema_txt[-4:-2] if lema_txt[-2:] == u'se' else lema_txt[-2:]) \
                            not in [u'ar', u'er', u'ir', u'ír']:
                        pass
                    if lema_txt[-2:] == u'se' and lema_txt[:-2] in lemario:
                        n_verbos_dobles += 1
                        verbos_dobles.add(lema_txt)
                        if n_verbos_dobles != len(verbos_dobles):
                            pass

                elif categoria in [SUSTANTIVO, ADJETIVO, SUFIJO, PRONOMBRE, DETERMINANTE]:
                    if lema_txt in [u'kakúis']:
                        pass
                    tipos = acepcion.get_tipos()
                    if categoria in lemario_subdividido and lema_txt in lemario_subdividido[categoria]:
                        # Hemos procesado una entrada anterior del mismo lema y categoría.
                        pass
                    elif categoria == SUSTANTIVO and u'P' in tipos:
                        nombres_propios.add(lema_txt)
                    else:
                        lema_txt_sin_tildes = lema_txt.replace(u'á', u'a').replace(u'é', u'e'). \
                            replace(u'í', u'i').replace(u'ó', u'o').replace(u'ú', u'u')
                        if lema_txt in lemas_femeninos[categoria] or len(lema_txt) < 3:
                            pass
                        else:
                            # En teoría variantes tendrá como mucho un elemento, pero se hace así para que sea
                            # más fácil comprobar si pasan cosas raras o no.
                            variantes = []
                            if lema_txt[-1] == u'o' \
                                    and lema_txt[:-1] + u'a' in lemario:
                                variantes.append(lema_txt[:-1] + u'a')
                            if lema_txt + u'a' in lemario:
                                variantes.append(lema_txt + u'a')
                            if lema_txt_sin_tildes != lema_txt:
                                if lema_txt_sin_tildes + u'a' in lemario:
                                    variantes.append(lema_txt_sin_tildes + u'a')
                            for variante in variantes:
                                lema_variante = lemario[variante]
                                for entrada_variante in lema_variante.get_entradas():
                                    if entrada_variante.get_acepciones()[0].get_categoria() == categoria:
                                        if variante in lemas_femeninos[categoria]:
                                            print(categoria_a_txt[categoria].upper(),
                                                  u': Pensábamos que', variante,
                                                  u'era el femenino de',
                                                  lemas_femeninos[categoria][variante],
                                                  u'pero también lo parece de', lema_txt)
                                            break
                                        lemas_femeninos[categoria][variante] = lema_txt
                                        print(categoria_a_txt[categoria].upper(), variante,
                                              u'es la variante femenina de', lema_txt +
                                              (u' y además es nombre propio'
                                               if categoria == SUSTANTIVO and
                                                  variante in nombres_propios else u''))
                                        break

                        if lema_txt in lemas_femeninos[categoria] or lema_txt in lemas_plurales[categoria] \
                                or len(lema_txt) < 3:
                            pass
                        else:
                            variantes = []
                            if lema_txt + u's' in lemario:
                                variantes.append(lema_txt + u's')
                            if lema_txt + u'es' in lemario:
                                variantes.append(lema_txt + u'es')
                            if lema_txt[-1] == u'y':
                                if lema_txt[-1] + u'is' in lemario:
                                    variantes.append(lema_txt[-1] + u'is')
                                else:
                                    variante = lema_txt[-2] in u'aeiou' and lema_txt[:-2] + \
                                               {u'a': u'á', u'e': u'é', u'i': u'í', u'o': u'ó',
                                                u'u': u'ú'}[lema_txt[-2]] + u'is'
                                    if variante in lemario:
                                        variantes.append(variante)
                            if lema_txt_sin_tildes != lema_txt:
                                if lema_txt_sin_tildes + u'es' in lemario:
                                    variantes.append(lema_txt_sin_tildes + u'es')
                            for variante in variantes:
                                lema_variante = lemario[variante]
                                for entrada_variante in lema_variante.get_entradas():
                                    if entrada_variante.get_acepciones()[0].get_categoria() == categoria:
                                        if variante in lemas_plurales[categoria]:
                                            print(categoria_a_txt[categoria].upper(),
                                                  u': Pensábamos que', variante, u'era el plural de',
                                                  lemas_plurales[categoria][variante],
                                                  u'pero también lo parece de', lema_txt)
                                            break
                                        lemas_plurales[categoria][variante] = lema_txt
                                        print(categoria_a_txt[categoria].upper(), variante,
                                              u'es la variante plural de', lema_txt +
                                              (u' y además es nombre propio'
                                               if categoria == SUSTANTIVO and
                                                  variante in nombres_propios else u''))
                                        break
                        if categoria == DETERMINANTE and lema_txt not in lemas_femeninos[categoria] and \
                                lema_txt not in lemas_plurales[categoria]:
                            if acepcion.get_inflects():
                                formas = acepcion.get_inflects()[0].split(u'|')[1:5]
                                if lema_txt == formas[2]:
                                    lemas_femeninos[categoria][lema_txt] = formas[0]
                                    print(categoria_a_txt[categoria].upper(), lema_txt,
                                          u'es la variante femenina de', formas[0])
                                elif lema_txt == formas[1]:
                                    lemas_plurales[categoria][lema_txt] = formas[0]
                                    print(categoria_a_txt[categoria].upper(), lema_txt,
                                          u'es la variante plural de', formas[0])
                                elif lema_txt == formas[3]:
                                    lemas_plurales[categoria][lema_txt] = formas[2]
                                    print(categoria_a_txt[categoria].upper(), lema_txt,
                                          u'es la variante plural de', formas[2])

                elif categoria == ADVERBIO:
                    if lema_txt[-5:] == u'mente':
                        adverbios_mente.add(lema_txt)

                # Añadimos al lemario subdividido
                if categoria not in lemario_subdividido:
                    lemario_subdividido[categoria] = {}
                if lema_txt not in lemario_subdividido[categoria]:
                    lemario_subdividido[categoria][lema_txt] = Lema(lema_txt, [])
                    n_acepciones_unicas += 1
                lemario_subdividido[categoria][lema_txt].append_entradas([entrada])

        # PURGA: Tenemos que hacerla después y no basta con no añadir los que no nos gusten, porque eso no
        # funciona para plurales y femeninos, ya que muchas veces la forma singular o masculina aparecen
        # después de la plural (cuando se eliminan tildes) y la femenina, y para cuando vemos la forma plural
        # o femenina no sabemos que hay que eliminarla.
        print(u'\nPurgando el lemario...')
        n_lemas_eliminados = 0
        for categoria in [SUSTANTIVO, ADJETIVO, SUFIJO, PRONOMBRE, DETERMINANTE]:
            texto = u'Había ' + str(len(lemario_subdividido[categoria])) + u' lemas de ' + \
                    categoria_a_txt[categoria]
            for lema_txt in lemas_femeninos[categoria]:
                n_entradas = len(lemario_subdividido[categoria][lema_txt].get_entradas())
                n_lemas_con_n_entradas[n_entradas] -= 1
                lemario_subdividido[categoria].pop(lema_txt)
                lema_nuevo = Lema(lema_txt, [])
                for entrada in lemario[lema_txt].get_entradas():
                    if categoria != entrada.get_acepciones()[0].get_categoria():
                        lema_nuevo.append_entradas([entrada])
                if lema_nuevo.get_entradas():
                    lemario[lema_txt] = lema_nuevo
                else:
                    n_lemas_eliminados += 1
                    lemario.pop(lema_txt)
            texto += u', quedaron ' + str(len(lemario_subdividido[categoria])) + \
                     u' lemas tras eliminar ' + str(
                len(lemas_femeninos[categoria])) + u' lemas femeninos, y '
            for lema_txt in lemas_plurales[categoria]:
                n_entradas = len(lemario_subdividido[categoria][lema_txt].get_entradas())
                n_lemas_con_n_entradas[n_entradas] -= 1
                lemario_subdividido[categoria].pop(lema_txt)
                lema_nuevo = Lema(lema_txt, [])
                for entrada in lemario[lema_txt].get_entradas():
                    if categoria != entrada.get_acepciones()[0].get_categoria():
                        lema_nuevo.append_entradas([entrada])
                if lema_nuevo.get_entradas():
                    lemario[lema_txt] = lema_nuevo
                else:
                    n_lemas_eliminados += 1
                    lemario.pop(lema_txt)
            texto += str(len(lemario_subdividido[categoria])) + u' tras eliminar ' + \
                     str(len(lemas_plurales[categoria])) + u' lemas plurales.'
            if len(lemas_femeninos[categoria]) + len(lemas_plurales[categoria]):
                print(texto)
        categoria = VERBO
        texto = u'Había ' + str(len(lemario_subdividido[categoria])) + u' lemas de ' + \
                categoria_a_txt[categoria]
        for lema_txt in verbos_dobles:
            n_entradas = len(lemario_subdividido[categoria][lema_txt].get_entradas())
            n_lemas_con_n_entradas[n_entradas] -= 1
            lemario_subdividido[categoria].pop(lema_txt)
            lema_nuevo = Lema(lema_txt, [])
            for entrada in lemario[lema_txt].get_entradas():
                if categoria != entrada.get_acepciones()[0].get_categoria():
                    lema_nuevo.append_entradas([entrada])
            if lema_nuevo.get_entradas():
                lemario[lema_txt] = lema_nuevo
            else:
                n_lemas_eliminados += 1
                lemario.pop(lema_txt)
        texto += u', quedaron ' + str(len(lemario_subdividido[categoria])) + \
                 u' lemas tras eliminar ' + str(len(verbos_dobles)) + \
                 u' lemas pronominales (cuya forma no pronominal ya estaba incluida).'
        if len(verbos_dobles):
            print(texto)
        print(u'Tras la purga, se han eliminado', n_lemas_eliminados, u'lemas.\n')

        n_lemcats = sum([len(lemas) for categoria, lemas in lemario_subdividido.items()])
        if n_lemcats != sum([len(set([ent.get_acepciones()[0].get_categoria()
                                      for ent in lema.get_entradas()]))
                             for lema_txt, lema in lemario.items()]):
            print(u'Hay algo raro, no cuadra el número de lemcats entre el lemario total y la suma de los'
                  u' tamaños de los sublemarios.')
        n_entradas_total = sum([len(lema.get_entradas()) for lema_txt, lema in lemario.items()])
        print(u'RECUENTO de contenido total del lemario WIK:')
        print(u'- Nº de lemas:', len(lemario))
        print(u'- Nº de lemcats:', n_lemcats)
        print(u'- Nº de entradas/acepciones totales:', n_entradas_total)
        for n_entradas, n_lemas in n_lemas_con_n_entradas.items():
            print(u'  - Nº de lemas con', n_entradas, u'entradas:', n_lemas)
        print(u'- Nº de acepciones únicas:', n_acepciones_unicas,
              u'(acepciones de lemas distintos o con distinta categoría gramatical)')
        print(u'\nRECUENTO por categoría:')
        recuento_por_categorias = {categoria: len(lemas) for categoria, lemas in lemario_subdividido.items()}
        for categoria, recuentos in sorted(recuento_por_categorias.items(),
                                           key=lambda tupla: -len(lemario_subdividido[tupla[0]])):
            categoria_txt = categoria_a_txt[categoria]
            ejemplos = sorted(lemario_subdividido[categoria].keys())[
                       0::(int(len(lemario_subdividido[categoria]) / 4.1)
                           if len(lemario_subdividido[categoria]) > 4
                           else 1)]
            datos_inflects = (
                        u'Hay ' + str(len(flexiones[categoria])) + u' modelos de flexión distintos.') \
                if categoria in flexiones else u''
            print(u'-', categoria_txt + u':', u', '.join(ejemplos) + u'...', datos_inflects)

            if categoria == SUSTANTIVO:
                texto_extra = u'\n  - Nº de nombres propios: ' + str(len(nombres_propios))
                texto_extra += u'\n  - Nº de nombres comunes: ' + \
                               str(len(lemario_subdividido[categoria]) - len(lemas_femeninos[categoria]) -
                                   len(lemas_plurales[categoria]) - len(nombres_propios))
            elif categoria == ADVERBIO:
                texto_extra = u'\n  - Nº de adverbios en -mente: ' + str(len(adverbios_mente))
                texto_extra += u'\n  - Nº de adverbios no en -mente: ' + \
                               str(len(lemario_subdividido[categoria]) - len(adverbios_mente))
            else:
                texto_extra = u''

            print(u'  - Nº de lemas:', len(lemario_subdividido[categoria]), texto_extra)
            print(u'  - Nº de entradas/acepciones:',
                  sum([len(lema.get_entradas()) for lema_txt, lema in lemario_subdividido[categoria].items()]))
            nombre_archivo_sublemario =\
                directorio_trabajo + u'sublemario_wik-' + categoria_txt.lower() + u'.pkl.bz2'
            print(u'Guardando', nombre_archivo_sublemario + u'\n')
            try:
                os.remove(nombre_archivo_sublemario)
            except OSError:
                pass
            with bz2.BZ2File(nombre_archivo_sublemario, 'wb') as archivo_lemario:
                pickle.dump(lemario_subdividido[categoria], archivo_lemario, -1)
        print(u'Guardando', nombre_archivo_lemario + u'\n')
        try:
            os.remove(nombre_archivo_lemario)
        except OSError:
            pass
        with bz2.BZ2File(nombre_archivo_lemario, 'wb') as archivo_lemario:
            pickle.dump(lemario, archivo_lemario, -1)

    @staticmethod
    def parsea_entradas_de_articulo(lema_txt, texto_articulo, elimina_formas=True, elimina_locuciones=True):
        # Se eliminaran los <!-- comentarios --> y <ref> referencias </ref>
        # Se elimina todo el contenido.
        regex = u'<ref([^>]*?((?<!\/)>((?:(?!<ref)(.|\n))*?)<\/ ?ref ?>)|([^\/]*?\/ ?>))'
        texto_articulo = re.sub(regex, u'', texto_articulo, flags=re.IGNORECASE)
        regex = u'<!--(.|\n)*?-->'
        texto_articulo = re.sub(regex, u'', texto_articulo, flags=re.IGNORECASE)
        regex = u'<small>|</small>'
        texto_articulo = re.sub(regex, u'', texto_articulo, flags=re.IGNORECASE)

        inicio = 0
        marcas_entrada = []
        while True:
            extremos = re.search(MARCA_ENTRADA_REGEX, texto_articulo[inicio:])
            if not extremos:
                # Hemos llegado al final. Salimos del bucle.
                break
            fin = extremos.end() + inicio
            inicio += extremos.start()
            marcas_entrada.append((inicio, fin))
            inicio = fin

        if lema_txt == u'acabado':
            pass
        entradas = []
        n_entradas = 0
        for orden, marca_entrada in enumerate(marcas_entrada):
            texto_marca = texto_articulo[marca_entrada[0]:marca_entrada[1]]
            if re.findall(u'\{\{lengua\|es', texto_marca, re.IGNORECASE) or re.findall(u'\{\{ES', texto_marca):
                # Nos quedamos con el texto desde el final de la etiqueta (+1, por el salto de carro)
                n_entradas += 1
                texto_lema = texto_articulo[marca_entrada[1] + 1:] if orden == len(marcas_entrada) - 1\
                    else texto_articulo[marca_entrada[1] + 1:marcas_entrada[orden + 1][0]]
                # En el wikcionario no diferenciamos realmente entre entradas y acepciones. En la RAE se considera
                # que una entrada como 'amanecer' tiene dos entradas, una como verbo y otra como nombre. A su vez,
                # dentro de cada una de estas dos entradas, hay varias acepciones. Para la entrada como verbo,
                # hay acepción como impersonal, como intransitivo... o incluso transitivo. Para la segunda entrada
                # tiene también dos acepciones, pero son sintácticamente lo mismo.
                # En el Wikcionario no se tiene la misma estructura. En él, para 'amanecer' se tienen 4 entradas:
                # como verbo impersonal, como verbo intransitivo, como verbo transitivo y como nombre. A su vez,
                # dentro de cada entrada tiene varias acepciones, pero siempre sintácticamente idénticas.
                # Así que para el Wikcionario consideramos que cada entrada tiene una única acepción, con los datos
                # relativos a ellas. Esto es compatible con la estructura que damos al parsear la RAE.
                entradas += ParseadorWikcionario.parsea_entradas_de_lema(lema_txt, texto_lema, len(entradas),
                                                                         elimina_formas, elimina_locuciones)
        if False:
            if n_entradas > 1:
                print(lema_txt, u'tiene, atención,', n_entradas, u'entradas... Mythbusters!')
        return entradas

    @staticmethod
    def parsea_entradas_de_lema(lema_txt, texto_lema, n_siguiente_entrada, elimina_formas=True, elimina_locuciones=True):
        """Partiendo del texto de la entrada española, se devuelve una lista de diccionarios con datos de cada acepción

        El texto de entrada equivale a todo el texto que tiene el Wikcionario para este lema dado. Eso incluye una
        o más entradas (cada una de una categoría o tipo sintáctico distinto: verbo impersonal, verbo intransitivo,
        sustantivo masculino...), que a su vez tienen una o más acepciones.

        Se extraen las etiquetas de categoría de palabra del texto del lema (cada una definirá una entrada de una única
        acepción). Para cada categoría que se encuentre, se creará una acepción y al final se creará una entrada
        para cada acepción, que contendrá únicamente dicha acepción.

        Para crear la acepción, se extraen las informaciones con datos gramaticales asociados que dependen de la
        propia categoría de la acepción. Estas informaciones aparecen en el texto del lema, y normalmente se asocian
        con una única acepción/entrada en concreto. Pero en otras ocasiones, estas informaciones aparecen una única
        vez en el texto del lema, pero se entiende que son aplicables a todas las acepciones que salen en el texto
        (o al menos, a todas las acepciones previas a la información). Así pues, cada categoría gramatical (con
        posibles variantes de tipo: (in)transitivo, femenino...) define una acepción, y cada acepción, define una
        entrada.

        Aparte de la extracción de la información, una tarea básica es la de emparejar dichas informaciones gramaticales
        con las acepciones/entradas. Hacemos estos emparejamientos teniendo en cuenta su posición en el texto y su
        contenido, de forma que todas las acepciones que necesiten etiqueta de flexión, reciban una adecuada.
        Una entrada puede tener una acepción como verbo transitivo, y otra como verbo intransitivo, pero tener una
        única información de conjugación, por ejemplo.

        Como una lema puede tener más de una entrada/acepción, se devuelve una lista de entradas.

        :type texto_lema: unicode
        :param texto_lema: texto de la acepcion del Wikcionario
        :rtype: [{}]
        :return: lista de {"cat": categoría, "infos": [info1, info2, ...], "sin_flex": True}
            "sin_flex" sólo aparece si la categoría necesita etiqueta de flexión y no se ha encontrado. Si no, no sale.
        """
        # Primero extraemos las etiquetas de categoría gramatical que incluya la entrada. Cada una de estas etiquetas
        # indica una acepción. Estas etiquetas suelen ser de la forma === {{categoría|es|tipo}} ===, por ejemplo:
        # === {{adjetivo|es|indefinido}} ===
        # === {{adjetivo|es|femenino}} ===
        # === {{sustantivo propio|es|masculino}} ===
        # TODO: === {{adjetivo|es|indeclinable}} ===
        # Hay casos con cuatro ==== en vez de tres ===
        # Además, aceptamos otras etiquetas que no son de encabezado (no llevan los ===) pero que indican que son
        # una cierta forma en concreto (verbal, en la práctica, participios y demás).
        # Los contigo, conmigo aparecen como dobles: === {{preposición|es}} + {{pronombre personal|es}} ===
        if lema_txt == u'acabado':
            pass
        inicio = 0
        acepciones_wik = []  # Lista de acepciones, que son diccionarios con informaciones asociadas a la acepción
        # Extraemos las marcas de categoría gramatical, así como sus ubicaciones. Es importante extraer las ubicaciones
        # puesto que más adelante se usará este dato para asignar unas u otras informaciones a cada acepcion. Por eso
        # no podemos usar un re.findall o algo así, porque nos hace falta la ubicación.
        while True:
            extremos = re.search(u'(?:(?<====)|(?<==== ))'
                                 u'(\{\{[^\}]+\|(leng=)?es(\|[^\}]+)?\}\}|forma|contracción)[^=\n]*?'
                                 u'(?:(?= ===)|(?====))', texto_lema[inicio:], re.IGNORECASE)
            if not extremos:
                # Hemos llegado al final. Salimos del bucle.
                break
            fin = extremos.end() + inicio
            inicio += extremos.start()
            etiqueta_categoria = texto_lema[inicio:fin]
            if u'}}' in etiqueta_categoria:
                marca_final = etiqueta_categoria.rfind(u'}}')
                resto = u''
                if marca_final < len(etiqueta_categoria) - 2:  # Entre el }} y el === puede haber info
                    resto = u'#' + etiqueta_categoria[marca_final + 2:].strip()
                    if resto[1:] in etiqueta_categoria:
                        resto = u''  # Contiene información redundante
                # Quitamos el |es
                etiqueta_categoria = re.sub(u'\|es(?=\||\})', u'', etiqueta_categoria) + resto
            etiqueta_categoria = etiqueta_categoria.replace(u'{{', u'').replace(u'}}', u'')
            # Quitamos la marca para que no se vuelva a encontrar al buscar informaciones
            texto_lema = texto_lema[:inicio] + (u' ' * (fin - inicio)) + texto_lema[fin:]
            # De momento metemos en la estructura de la acepción el inicio (posición en el texto en el que aparece
            # la etiqueta), y añadimos la clave "sin_flex" de momento, que indica que no hemos asociado ninguna etiqueta
            # de flexión a la acepción.
            acepciones_wik.append({"lema": lema_txt, "ini": inicio,
                                   "cat": etiqueta_categoria, "infos": [], "sin_flex": True})
            inicio = fin

        # El texto de la entrada contiene información relativa a la flexión y a algunas otras características
        # gramaticales o semánticas. Extraemos aquellas informaciones que son de relevancia para nosotros:
        # principalmente las etiquetas de flexión, y algunas otras que llevan información importante.
        inicio = 0
        informaciones = []  # Datos que aportan información extra sobre la acepción.
        while True:
            # Pueden aparecer etiquetas del tipo {{...}} anidadas. Así que nos aseguramos que cortamos por el }} que
            # esté al mayor nivel, dejando incluir etiquetas {{...}} dentro de la propia etiqueta. Por ello no podemos
            # usar un simple findall porque sería muy difícil crear un regex de la etiqueta teniendo en cuenta que
            # el número de aperturas tiene que ser igual al número de cierres.
            extremos = re.search(u'\{\{(inflect|es\.v\.conj|w\.es\.v\.conj|adjetivo|sustantivo|'
                                 u'forma|f\.|infinitivo|participio|gerundio|'
                                 u'enclítico|diminutivo|superlativo|impropia|plural|'
                                 u'ciudades|regiones|países|islas|lagos|mares|penínsulas|planetas|ríos|topónimos|'
                                 u'antropónimo|apellido|gentilicio|'
                                 u'aumentativo|comparativo)[^\}]*\}\}',
                                 texto_lema[inicio:], re.IGNORECASE)
            if not extremos:
                # Hemos llegado al final. Salimos del bucle.
                break
            fin = extremos.end() + inicio
            inicio += extremos.start()
            etiqueta_informacion = texto_lema[inicio:fin]
            # Nos aseguramos de alargar el texto hasta cerrar todas las etiquetas abiertas.
            while etiqueta_informacion.count(u'{{') - etiqueta_informacion.count(u'}}') != 0:
                # Hemos llegado a un cierre anidado. El que cierra la apertura es otro más adelante.
                posicion_cierre = texto_lema.find(u'}}', fin)
                if posicion_cierre != -1:
                    fin = posicion_cierre + 2
                    etiqueta_informacion = texto_lema[inicio:fin]
                    continue
                break
            # Añadimos dos claves extra: "ini" para saber la ubicación de la etiqueta en el texto y "asignada" para
            # saber que esta información ha sido asignada al menos a una acepción.
            informaciones.append({"ini": inicio, "info": etiqueta_informacion[2:-2], "asignada": False})
            inicio = fin

        # Tenemos por un lado las etiquetas de categoría gramatical, y por otro las de las etiquetas con informaciones
        # gramaticales relativas. Hay que emparejarlas, y no es un proceso trivial.
        if len(acepciones_wik) < 2:
            # Si solo hay una acepción (o ninguna) no ha problema para asignar la información
            if not acepciones_wik:
                # Si no hay acepción, nos inventamos una de categoría ("desconocida") para que le meta todas las
                # informaciones.
                # No habíamos creado ninguna acepción, así que todas las infos se añadirán posteriormente
                acepciones_wik = [{"lema": lema_txt, "cat": u'desconocida', "infos": [], "ini": -1}]
            else:
                # Solo hay una acepción, así que ningún problema. Quitamos el "sin_flex" porque ya no hace falta
                # (el "ini" se quita más abajo)
                acepciones_wik[0].pop("sin_flex")
            # Las informaciones van todas juntas en la única acepción (quizá de categoría desconocida)
            for informacion in informaciones:
                informacion.pop("ini")
                informacion.pop("asignada")
                acepciones_wik[0]["infos"].append(informacion["info"])
        else:
            # Como sí que hay varias acepciones debemos decidir qué informaciones pertenecen a cada acepción
            for orden_acepcion, acepcion_wik in enumerate(acepciones_wik):
                orden_candidato_previo = -1
                orden_candidato_posterior = -1
                # Según el tipo de categoría, veremos si necesita una etiqueta de flexión
                cat_verbal = u'verb' in acepcion_wik["cat"]
                cat_nominal = u'sustantiv' in acepcion_wik["cat"]
                cat_pronominal = u'pronom' in acepcion_wik["cat"]
                cat_adjetival = u'adjetiv' in acepcion_wik["cat"] or u'participio' in acepcion_wik["cat"] or\
                                u'artículo' in acepcion_wik["cat"]
                necesita_flex = not re.match(u'forma', acepcion_wik["cat"], re.IGNORECASE) and\
                    (cat_verbal or cat_nominal or cat_pronominal or cat_adjetival)
                flex_exacta_encontrada = False  # Indica que hemos encontrado una etiqueta de flexión 100% compatible
                for orden_informacion, informacion in enumerate(informaciones):
                    # Vamos a asignar las etiquetas de información. Vemos qué tipo de etiqueta es
                    flex_verbal = u'v.conj' in informacion["info"]
                    flex_nominal = u'inflect.es.sust' in informacion["info"] or u'inflect.sust' in informacion["info"]
                    flex_pronominal = u'inflect.es.pron' in informacion["info"]
                    flex_adjetival = u'inflect.es.adj' in informacion["info"] or u'inflect.adj' in informacion["info"]
                    # Las etiquetas de flexión son las fundamentales. Vemos si es una etiqueta de flexión
                    es_flex = flex_verbal or flex_nominal or flex_pronominal or flex_adjetival
                    # Según la categoría que estemos procesando, esta etiqueta será o no compatible con ella. Puede ser
                    # incompatible, exactamente lo que queremos, o algo intermedio pero "adaptable" y aceptable.
                    flex_exacta = (cat_verbal and flex_verbal) or (cat_pronominal and flex_pronominal) or\
                        (cat_nominal and flex_nominal) or (cat_adjetival and flex_adjetival)
                    if not flex_exacta:
                        flex_aceptable = (cat_verbal and flex_verbal) or\
                            (cat_pronominal and (flex_nominal or flex_adjetival or flex_pronominal)) or \
                            ((cat_nominal or cat_adjetival) and (flex_nominal or flex_adjetival))
                    else:
                        flex_aceptable = True
                    flex_invalida = es_flex and not flex_aceptable  # Si es exacta, también es aceptable
                    # Asociaremos o no esta información a esta acepción dependiendo de sus posiciones relativas
                    # (normalmente asociamos a cada acepción todas las informaciones que haya entre la marca de la
                    # categoría gramatical -lo que marca el inicio de la acepción- y la siguiente de estas marcas, pero
                    # esto no es siempre así).
                    # Además, para poderla asociar, en caso de ser etiqueta de flexión, debe ser del tipo de etiqueta
                    # esperado para la categoría.
                    if informacion["ini"] < acepcion_wik["ini"] and orden_acepcion != 0:
                        # Esta info aparece antes que esta acepción (y no es la primera). Por defecto la descartamos salvo
                        # que se trate de una etiqueta de flexión, y esta acepción necesite ese tipo de etiqueta: en ese
                        # caso marcamos la etiqueta como candidata porque es posible que esa etiqueta anterior sea válida
                        # para la acepción anterior y para esta también (por ejemplo, verbo transitivo o intransitivo con
                        # la misma flexión, aunque en estos casos la única etiqueta de flexión usualmente aparece al final).
                        if not necesita_flex or not es_flex:
                            # Esta categoría gramatical no necesita flexión o la etiqueta no es de flexión.
                            # Estaba antes de la etiqueta de categoría, así que no nos interesa para esta acepción.
                            continue
                        if flex_exacta:
                            # Es una info de flexión, la categoría necesita flexión y justo de este tipo. Perfect match!
                            # Hacemos constar esto marcándolo como candidato a flexión, y sabiendo que hemos encontrado
                            # justo el tipo de flexión que queríamos. Está antes, y eso no es bueno, con lo que si
                            # encontramos más tarde una etiqueta de flexión que nos valga, dentro del "ámbito de influencia"
                            # de la etiqueta de categoría, utilizaremos esa etiqueta de flexión y no esta.
                            orden_candidato_previo = orden_informacion
                            flex_exacta_encontrada = True
                        elif not flex_exacta_encontrada and flex_aceptable:
                            # Si aún no hemos dado con una etiqueta de flexión exacta, y esta es aceptable, la marcamos
                            # como candidata (si hubiera otro previo también aceptable, se machaca, porque nos interesa
                            # el candidato compatible inmediatamente anterior a la etiqueta de categoría).
                            orden_candidato_previo = orden_informacion
                    else:
                        # Esta etiqueta informativa está después de la etiqueta de inicio de acepción que estamos procesando
                        # o está antes de la primera acepción. En cualquier caso, la etiqueta de información está, digamos,
                        # en el ámbito de influencia de esta acepción, y en principio debería asignarse a ella.
                        if necesita_flex and es_flex and flex_invalida:
                            # Etiqueta no compatible, estará desordenada. Quizá sea válida para una acepción posterior.
                            # De momento no la procesamos y pasamos a la siguiente.
                            continue
                        if informacion["ini"] < acepcion_wik["ini"] or orden_acepcion == (len(acepciones_wik) - 1) or\
                                informacion["ini"] < acepciones_wik[orden_acepcion + 1]["ini"]:
                            # La info está en el "ámbito" de la acepción (antes de la última, o antes de la siguiente, o
                            # antes de la primera acepción).
                            # Si la info es de flexión verbal y la acepción no necesita flexión y además es
                            # inválida, ni la añadimos.
                            if es_flex and flex_verbal and not necesita_flex and flex_invalida:
                                if not informacion["asignada"]:
                                    # No estoy seguro de si debería comprobar algo aquí:
                                    pass
                            else:
                                # La añadimos en firme a esta acepción y lo marcamos en la etiqueta "info"
                                informacion["asignada"] = True
                                acepcion_wik["infos"].append(informacion["info"])
                                if es_flex and "sin_flex" in acepcion_wik:
                                    acepcion_wik.pop("sin_flex")  # Ya hemos encontrado flexión. Tema zanjado
                        elif necesita_flex and "sin_flex" in acepcion_wik:
                            # Esta etiqueta en principio corresponde a una acepción posterior, pero seguimos buscando la
                            # flexión para esta categoría, con lo que nos puede interesar.
                            if not es_flex:
                                # Si no es una etiqueta de flexión, no le damos más vueltas. Seguimos mirando la siguiente.
                                continue
                            # Tenemos una etiqueta de flexión fuera del ámbito de la acepción, pero aún no tenemos una
                            # flexión para esta acepción.
                            if flex_exacta:
                                # Es una etiqueta de flexión posterior al ámbito de la acepción, pero nos cuadra y es que
                                # dentro del ámbito no había ninguna de estas etiquetas con una flexión más compatible.
                                informacion["asignada"] = True
                                acepcion_wik["infos"].append(informacion["info"])
                                acepcion_wik.pop("sin_flex")
                                # Ya nos hemos salido de nuestro ámbito, y tenemos flexión y de todo. No buscamos más
                                # informaciones para esta acepción.
                                break
                            elif orden_candidato_posterior == -1 and flex_aceptable:
                                # Si no encontramos la flexión exacta, nos quedamos con la flexión aceptable inmediatamente
                                # posterior a la etiqueta de categoría.
                                orden_candidato_posterior = orden_informacion
                        else:
                            # Esta info (y siguientes) es de una acepción posterior y ya tenemos la flexión de esta cat
                            # o directamente no necesita flexión. Esta acepción tiene ya todas sus informaciones asignadas
                            break
                # Ya hemos procesado esta acepción y todas las informaciones que podrían afectarle, y las hemos emparejado.
                # A ver si nos ha quedado todo bien o tenemos que "inventar" algo (principalmente, si falta flexión).
                if necesita_flex and "sin_flex" in acepcion_wik:
                    # Tras analizar las informaciones, no hemos asignado una flexión. A ver si hemos encontrado una etiqueta
                    # de flexión apropiada fuera del ámbito de la acepción.
                    if flex_exacta_encontrada:
                        # Es una etiqueta anterior a la acepción, pero es exacta. No puede haber exactas posteriores
                        # puesto que en esos casos directamente hubiéramos quitado el "sin_flex".
                        # Así que la etiqueta exacta está entre los candidatos previos, y tenemos su orden.
                        informaciones[orden_candidato_previo]["asignada"] = True
                        acepcion_wik["infos"].append(informaciones[orden_candidato_previo]["info"])
                        acepcion_wik.pop("sin_flex")
                    elif orden_candidato_posterior != -1:
                        # No hay flexión exacta, pero hay un candidato posterior (con lo que la flexión es aceptable).
                        informaciones[orden_candidato_posterior]["asignada"] = True
                        acepcion_wik["infos"].append(informaciones[orden_candidato_posterior]["info"])
                        acepcion_wik.pop("sin_flex")
                    elif orden_candidato_previo != -1:
                        # No hay exacto ni etiquetas posteriores aceptables, pero sí una previa. Es más arriesgado pero
                        # al no tener mejor opción, la utilizamos.
                        informaciones[orden_candidato_previo]["asignada"] = True
                        acepcion_wik["infos"].append(informaciones[orden_candidato_previo]["info"])
                        acepcion_wik.pop("sin_flex")
                    # Si no se dan ninguno de los tres casos, la acepción mantendrá el campo "sin_flex"

            # Ahora miramos si nos ha quedado alguna información sin asignar
            for informacion in (info for info in informaciones if not info["asignada"]):
                # print(u'\nNos queda una información no asignada para', lema_txt, u'. Vamos a hacer lo que podamos', informacion["info"])
                # Tiene que ser una etiqueta de flexión que no hemos metido en ninguna acepción. Si fuera una
                # información de otro tipo, se habría metido en alguna acepción (porque acepción sí que tenemos).
                # Esto puede ocurrir cuando tenemos al final del artículo varias etiquetas de flexión (por ejemplo,
                # verbal) pero la etiqueta inmediatamente anterior es de un tipo incompatible (por ejemplo, nombre).
                # Esto ocurre en "anochecer" o "parecer", por ejemplo.
                orden_acepcion_candidata = -1
                # Vamos al revés para dar preferencia a las etiquetas posteriores
                for orden_acepcion in range(len(acepciones_wik) - 1, -1, -1):
                    # De nuevo, como arriba, miramos la compatibilidad de la información con la acepción
                    acepcion_wik = acepciones_wik[orden_acepcion]
                    cat_verbal = u'verb' in acepcion_wik["cat"]
                    cat_nominal = u'sustantiv' in acepcion_wik["cat"]
                    cat_pronominal = u'pronom' in acepcion_wik["cat"]
                    cat_adjetival = u'adjetiv' in acepcion_wik["cat"] or u'participio' in acepcion_wik["cat"] or \
                                    u'artículo' in acepcion_wik["cat"]
                    necesita_flex = cat_verbal or cat_nominal or cat_pronominal or cat_adjetival
                    if not necesita_flex:
                        # Esta acepción no necesita etiqueta de flexión, así que miramos con otra acepción
                        continue
                    flex_verbal = u'v.conj' in informacion["info"]
                    flex_nominal = u'inflect.es.sust' in informacion["info"] or u'inflect.sust' in informacion["info"]
                    flex_pronominal = u'inflect.es.pron' in informacion["info"]
                    flex_adjetival = u'inflect.es.adj' in informacion["info"] or u'inflect.adj' in informacion["info"]

                    flex_exacta = (cat_verbal and flex_verbal) or (cat_pronominal and flex_pronominal) or \
                                  (cat_nominal and flex_nominal) or (cat_adjetival and flex_adjetival)
                    if not flex_exacta:
                        flex_aceptable = (cat_verbal and flex_verbal) or \
                                         (cat_pronominal and (flex_nominal or flex_adjetival or flex_pronominal)) or \
                                         ((cat_nominal or cat_adjetival) and (flex_nominal or flex_adjetival))
                    else:
                        flex_aceptable = True
                    if flex_exacta:
                        # Esto es un parche feo debido a que cuando llegamos a esta situación, básicamente es porque
                        # hay conjugación impersonal y personal, y estas conjugaciones aparecen al final del artículo
                        # precedidas por una categoría que no es de verbo.
                        if (u'impersonal=' in informacion["info"] and u'impersonal' in acepcion_wik["cat"]) or \
                                (u'impersonal=' not in informacion["info"] and u'impersonal' not in acepcion_wik["cat"]):
                            informacion["asignada"] = True
                            acepcion_wik["infos"].append(informacion["info"])
                            if "sin_flex" in acepcion_wik:
                                acepcion_wik.pop("sin_flex")
                            break
                        else:
                            # En principio es válida y la marcamos como candidata
                            orden_acepcion_candidata = orden_acepcion
                    elif flex_aceptable and orden_acepcion_candidata == -1:
                        # Si solo es aceptable, la marcamos únicamente si no teníamos otro candidato antes
                        orden_acepcion_candidata = orden_acepcion
                else:  # Llegamos aquí si hacemos el for entero sin salir por break
                    if orden_acepcion_candidata != -1:
                        # Había un candidato, así que lo asignamos
                        informacion["asignada"] = True
                        acepciones_wik[orden_acepcion_candidata]["infos"].append(informacion["info"])
                        if "sin_flex" in acepciones_wik[orden_acepcion_candidata]:
                            acepciones_wik[orden_acepcion_candidata].pop("sin_flex")
            # Una verificación que se puede borrar cuando funcione.
            if [info for info in informaciones if not info["asignada"]]:
                print(u'\nAún nos queda una información no asignada. ¿Cómo es posible?',
                    [info for info in informaciones if not info["asignada"]][0]["info"])
                beep(2000, 300)

        # Limpiamos las etiquetas auxiliares de "ini" en las acepciones. La parte de informaciones se ha añadido a la
        # acepción sin incluir los campos de "ini" y "asignada".
        # No limpiamos la etiqueta "sin_flex", que nos indicará que ninguna de las informaciones es de flexión.
        entradas = []
        if len(acepciones_wik) > 1:
            pass
        if lema_txt == u'acabado':
            pass
        for acepcion_wik in acepciones_wik:
            acepcion_wik.pop("ini")
            acepcion = AcepcionWik(acepcion_wik, "wik", n_siguiente_entrada, 0)
            if (elimina_formas and acepcion.get_categoria() == FORMA) or\
                    (elimina_locuciones and acepcion.get_es_locucion()) or\
                    not acepcion.get_categoria() or acepcion.get_categoria() == DESCONOCIDA:
                continue
            entradas.append(Entrada([acepcion], [], n_siguiente_entrada))
            n_siguiente_entrada += 1
        return entradas

    @staticmethod
    def crea_lexicon(lemario=None, nombre_archivo_lemario=None,
                     incluye_cliticos=True, incluye_locuciones=False, ajusta_lema=True):
        u"""

        :param ajusta_lema:
        :param lemario:
        :param nombre_archivo_lemario:
        :param incluye_cliticos:
        :param incluye_locuciones:
        :return:
        """
        if not lemario:
            if not nombre_archivo_lemario:
                directorio_trabajo =\
                    dirname(os.path.realpath(__file__)) + u'\\archivos_de_datos\\wik\\lemario\\'
                nombre_archivo_lemario = directorio_trabajo + u'lemario_wik.pkl.bz2'
                if not os.path.exists(nombre_archivo_lemario):
                    ParseadorWikcionario.crea_lemario()
            with bz2.BZ2File(nombre_archivo_lemario, 'rb') as entrada:
                lemario = pickle.load(entrada)
        lexicon = {}
        # lexicón es un diccionario donde a cada clave (forma), se le asigna un diccionario donde las claves son
        # los lemas, y a cada una se le asigna un diccionario donde las claves son las etiquetas EAGLES y los
        # datos es una lista de strings que indican la fuente de la que se ha sacado (para poder posteriormente hacer
        # un estudio más profundo, consultando sus datos del lemario), donde hay tres valores separados por |:
        # "rae" o "wik" para la fuente, número de entrada, número de acepción. La entrada de ejemplo para la forma
        # u'vista' sería así (más o menos, las fuentes están inventadas, y pueden faltar cosas):
        # lexicon[u'vista'] = {u'ver': {"VMP00SF00000": ["rae|1|1", "rae|1|2", ..., "rae|2|1", ..., "wik|1|3"]},
        #                      u'vestir': {"VMSP1S000000...": ["rae|1|1", ..., "wik|2|1"],
        #                                  "VMSP3S000000...": ["rae|1|1", ..., "wik|2|1"]},
        #                      u'vista': {"NCFS0000": ["rae|1|1", ..., "wik|2|1"]
        #                     }
        conjugaciones = []
        flexiones = []
        tipos = []
        recuento = {}
        lemas_verbos = []
        n_lemas_procesados = 0
        for lema_txt, lema in lemario.items():
            if n_lemas_procesados % 1000 == 0 and n_lemas_procesados:
                print(n_lemas_procesados, u'lemas procesados.')
            n_lemas_procesados += 1
            if len(lema_txt.split()) > 1:
                if incluye_locuciones:
                    # Deberíamos extraer el tipo de la forma y meterlo aquí sin flexionar
                    # TODO: tenemos que procesarlo
                    continue
                else:
                    # El lema contiene varias palabras. No lo procesamos
                    continue
            for n_entrada, entrada in enumerate(lema.get_entradas()):
                for n_acepcion, acepcion in enumerate(entrada.get_acepciones()):
                    # formas_flexionadas es un dict de dicts. El dict externo tiene como clave la etiqueta EAGLES y como
                    # contenido un diccionario cuya clave es la forma_txt y el contenido es una lista de fuentes,
                    # del tipo: {'VMG000000000': {u'aflautando': ['wik|0|0']},
                    #            'VMG0000000FP': {u'aflautándolas': ['wik|0|0']},
                    #            ...
                    #           }
                    if acepcion.get_categoria() == PRONOMBRE:
                        pass
                    formas_flexionadas = Flexionador.flexiona_acepcion_wik(acepcion, ajusta_lema, incluye_cliticos)
                    if ajusta_lema:
                        lema_txt = acepcion.get_lema_txt()  # Al flexionar, podemos ajustar el lema.

                    # Como prueba inicial, si no tenemos flexion (porque no es sust/adj/verb/adv), metemos
                    # la palabra en el lexicón, pero como lista vacía de lemas. Así, luego podremos eliminar
                    # estas palabras.
                    if not formas_flexionadas:
                        # El lema no es sust/adj/verb/adv, así que lo marcamos así para indicar que no es semántica
                        # y que queremos que se quede vacío. Así un sust/adj... posterior con la misma forma (para...)
                        # no añadirá posteriormente aquí nada.
                        lexicon[lema_txt] = {lema_txt: {}}
                    # Añadimos las formas y sus etiquetas al lexicón
                    for etiqueta, formas in formas_flexionadas.items():
                        for forma_txt, fuentes in formas.items():
                            if forma_txt not in lexicon:
                                lexicon[forma_txt] = {lema_txt: {etiqueta: fuentes}}
                            elif forma_txt in lexicon[forma_txt] and not lexicon[forma_txt][forma_txt]:
                                # TODO: esto no tiene mucho sentido ya. Piénsalo y cámbialo
                                continue  # Entra "para" de "parar", pero antes habíamos marcado "para" como no-semántica
                            elif lema_txt not in lexicon[forma_txt]:
                                lexicon[forma_txt][lema_txt] = {etiqueta: fuentes}
                            elif etiqueta not in lexicon[forma_txt][lema_txt]:
                                lexicon[forma_txt][lema_txt][etiqueta] = fuentes
                            else:
                                lexicon[forma_txt][lema_txt][etiqueta] += fuentes


                    if False:
                        # Recuentos y demás
                        if "categoría" in acepcion:
                            if acepcion["categoría"] in [SUSTANTIVO, ADJETIVO, VERBO, ADVERBIO, PRONOMBRE, CONJUNCION, PREPOSICION]:
                                if acepcion["categoría"] == VERBO:
                                    # Como los verbos suelen venir por pares de pronominal/no pronominal, y en el fondo hemos
                                    # conseguido que se conjuguen exactamente igual gracias al silabeado y acentuación y demás,
                                    # pues para hacer un conteo de lemas distintos mucho más preciso, no contamos dos veces
                                    # estos verbos. Puede haber verbos que compartan forma, como aterrar (de terror o de tierra)
                                    # que se contarán una vez, pero es una cantidad mínima y en el fondo, no sé si estaría
                                    # mejor contar estos poquísimos verbos como verbos independientes o no.
                                    if lema not in lemas_verbos:
                                        lemas_verbos.append(lema)
                                else:
                                    recuento[acepcion["categoría"]] = recuento.setdefault(acepcion["categoría"], 0) + 1

                        if "tipo" in acepcion and "categoría" in acepcion and acepcion["categoría"] == PRONOMBRE:
                            for tipo in acepcion["tipo"]:
                                tipos += [tipo.split(u'|')[0].strip()]
                        if "conj" in acepcion:
                            for conj in acepcion["conj"]:
                                conjugaciones += [conj.split(u'|')[0].strip()]
                        if "inflect" in acepcion:
                            for inflect in acepcion["inflect"]:
                                flexiones += [inflect.split(u'|')[0].strip()]
                        # TODO: hay acepciones de nombres que son aumentativos o diminutivos y se podrían poner en el mismo lema
                        # la información está en acepcion["lema_base"]

        print(n_lemas_procesados, u'lemas procesados.')
        directorio_trabajo = \
            dirname(os.path.realpath(__file__)) + u'\\archivos_de_datos\\wik\\lexicon\\'
        nombre_archivo_lexicon = directorio_trabajo + u'lexicon_wik.pickle'
        if not os.path.exists(directorio_trabajo):
            os.makedirs(directorio_trabajo)
        try:
            os.remove(nombre_archivo_lexicon)
        except OSError:
            pass
        print(u'Guardando lexicón en', u'.../' + u'/'.join(nombre_archivo_lexicon.split(u'/')[-5:]))
        with open(nombre_archivo_lexicon, 'wb') as archivo_lexicon:
            # ujson.dump(lexicon, archivo_lexicon, ensure_ascii=False, escape_forward_slashes=False)
            pickle.dump(lexicon, archivo_lexicon, pickle.HIGHEST_PROTOCOL)

        n_etiquetas = sum([len(etiquetas)
                           for forma, datos in lexicon.items()
                           for lema, etiquetas in datos.items()])
        print(u'El lexicón contiene', len(lexicon), u'formas, con', n_etiquetas, u'etiquetas.')
        recuentos_formas = {}
        recuentos_lemcats = {}
        for forma, datos in lexicon.items():
            categorias = set()
            for lema, etiquetas in datos.items():
                for etiqueta, fuentes in etiquetas.items():
                    categoria = etiqueta[0] if etiqueta[0] != AFIJO else etiqueta[1]
                    categorias.add(categoria)
                    if categoria not in recuentos_formas:
                        recuentos_formas[categoria] =\
                            {"etiquetas_distintas": set(), "n_formas": 0, "n_etiquetas": 0}
                    recuentos_formas[categoria]["etiquetas_distintas"].add(etiqueta)
                    recuentos_formas[categoria]["n_etiquetas"] += 1
                    if categoria not in recuentos_lemcats:
                        recuentos_lemcats[categoria] = set()
                    recuentos_lemcats[categoria].add(lema + u'-' + categoria)

            for categoria in set(categorias):
                recuentos_formas[categoria]["n_formas"] += 1
        print(u'Recuentos por categoría:')
        categoria_a_txt = {SUSTANTIVO: u'Sustantivo', ADJETIVO: u'Adjetivo', DETERMINANTE: u'Determinante',
                           PRONOMBRE: u'Pronombre', VERBO: u'Verbo', ADVERBIO: u'Adverbio',
                           PREPOSICION: u'Preposición', CONJUNCION: u'Conjunción',
                           INTERJECCION: u'Interjección',
                           EXPRESION: u'Expresión', ONOMATOPEYA: u'Onomatopeya', AFIJO: u'Afijo',
                           PREFIJO: u'Prefijo', SUFIJO: u'Sufijo',
                           ABREVIATURA: u'Abreviatura', SIGLA: u'Sigla',
                           SIMBOLO: u'Símbolo', DESCONOCIDA: u'Desconocida'}
        for (categoria, datos) in sorted(recuentos_formas.items(),
                                         key=lambda tupla: -tupla[1]["n_etiquetas"]):
            print(categoria_a_txt[categoria] + u':')
            print(u'  - Nº de etiquetas:', datos["n_etiquetas"])
            print(u'  - Nº de formas:', datos["n_formas"])
            print(u'  - Nº de etiquetas distintas:', len(datos["etiquetas_distintas"]))
            print(u'  - Nº de lemas:', len(recuentos_lemcats[categoria]))

        return lexicon

    @staticmethod
    def carga_lexicon():
        u"""
        Carga el lexicón del Wikcionario.
        """
        # Sacamos el directorio en el que está ubicado este script.
        directorio_trabajo = dirname(os.path.realpath(__file__)) + u'\\archivos_de_datos\\wik\\lexicon\\'
        path_archivo_lexicon = directorio_trabajo + u'lexicon_wik.pickle'
        # Cargamos...
        if not os.path.exists(path_archivo_lexicon):
            print(u'Falta el archivo', path_archivo_lexicon + u'. Es necesario crear el lexicón.')
            return {}
        print(u'Cargando archivo', u'.../' + u'/'.join(path_archivo_lexicon.split(u'/')[-5:]), end=u' ')
        with open(path_archivo_lexicon, 'rb') as entrada:
            lexicon = pickle.load(entrada)
        print(u'Cargadas', len(lexicon), u'formas.')
        return lexicon


# TODO: Sería interesante capturar las etiquetas {{doble conjugación}} y {{defectivo}}
if __name__ == '__main__':
    # ParseadorWikcionario.crea_lexicon()
    lexicon = ParseadorWikcionario.carga_lexicon()
    exit()

    if False:
        ParseadorWikcionario.crea_lemario_previo(actualiza_archivo_raw=False)
        ParseadorWikcionario.crea_lemario(actualiza_archivo_raw=False, crea_lemario_previo=False,
                                          elimina_formas=True, elimina_locuciones=True)
        ParseadorWikcionario.subdivide_lemario_wik()
        ParseadorWikcionario.crea_lexicon()
    directorio_trabajo = \
        dirname(os.path.realpath(__file__)) + u'\\archivos_de_datos\\wik\\lexicon\\'
    nombre_archivo_lexicon = directorio_trabajo + u'lexicon_wik.ujson.bz2'
    with bz2.BZ2File(nombre_archivo_lexicon, 'rb') as entrada:
        lexicon = ujson.load(entrada)

    lexicon_de_formas = {}
    for forma, datos in lexicon.items():
        for lema, etiquetas in datos.items():
            if lema not in lexicon_de_formas:
                lexicon_de_formas[lema] = set()
            lexicon_de_formas[lema].add(forma)




    n_etiquetas = sum([len(etiquetas)
                       for forma, datos in lexicon.items()
                       for lema, etiquetas in datos.items()])
    print(u'El lexicón contiene', len(lexicon), u'formas, con', n_etiquetas, u'etiquetas.')
    recuentos = {}
    for forma, datos in lexicon.items():
        categorias = set()
        for lema, etiquetas in datos.items():
            for etiqueta, fuentes in etiquetas.items():
                categoria = etiqueta[0] if etiqueta[0] != AFIJO else etiqueta[1]
                categorias.add(categoria)
                if categoria not in recuentos:
                    recuentos[categoria] = {"etiquetas_distintas": set(), "n_formas": 0, "n_etiquetas": 0}
                recuentos[categoria]["etiquetas_distintas"].add(etiqueta)
                recuentos[categoria]["n_etiquetas"] += 1
        for categoria in set(categorias):
            recuentos[categoria]["n_formas"] += 1
    print(u'Recuentos por categoría:')
    categoria_a_txt = {SUSTANTIVO: u'Sustantivo', ADJETIVO: u'Adjetivo', DETERMINANTE: u'Determinante',
                       PRONOMBRE: u'Pronombre', VERBO: u'Verbo', ADVERBIO: u'Adverbio',
                       PREPOSICION: u'Preposición', CONJUNCION: u'Conjunción',
                       INTERJECCION: u'Interjección',
                       EXPRESION: u'Expresión', ONOMATOPEYA: u'Onomatopeya', AFIJO: u'Afijo',
                       PREFIJO: u'Prefijo', SUFIJO: u'Sufijo',
                       ABREVIATURA: u'Abreviatura', SIGLA: u'Sigla',
                       SIMBOLO: u'Símbolo', DESCONOCIDA: u'Desconocida'}
    for (categoria, datos) in sorted(recuentos.items(), key=lambda tupla: -tupla[1]["n_etiquetas"]):
        print(categoria_a_txt[categoria] + u':')
        print(u'  - Nº de etiquetas:', datos["n_etiquetas"])
        print(u'  - Nº de formas:', datos["n_formas"])
        print(u'  - Nº de etiquetas distintas:', len(datos["etiquetas_distintas"]))

    exit()

    if False:
        ParseadorWikcionario.crea_lemario(nombre_archivo_raw=u'', actualiza_archivo=False, elimina_formas=True,
                                          elimina_locuciones=True, usa_dict_articulos=True, crea_dict_articulos=False,
                                          verboso=True)
    # ParseadorWikcionario.crea_lexicon(incluye_cliticos=True, incluye_locuciones=False)
