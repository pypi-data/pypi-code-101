#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""
"""

from __future__ import print_function
import bz2
import codecs
import copy
import os
import re
import socket
from time import time, sleep
import msgpacku as msgpack
from os import listdir
from os.path import isfile, dirname

from iar_inflector.acep_consts import CATEGORIAS_A_TXT, TIPOS_VERBO_A_TXT, SUSTANTIVO, ADJETIVO,\
    DETERMINANTE, PRONOMBRE, VERBO, ADVERBIO, CONJUNCION, PREPOSICION, SIGNO, INTERJECCION, NA,\
    EXPRESION, ONOMATOPEYA, AFIJO, PREFIJO, SUFIJO, ABREVIATURA, SIGLA, SIMBOLO, DESCONOCIDA, PROPIO
from iar_inflector.acepcion import AcepcionRae
from iar_inflector.entrada import Entrada
from iar_inflector.flexionador import Flexionador
from iar_inflector.lema import Lema
from iar_inflector.parseador_wikci import ParseadorWikcionario
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Firefox  # pip install selenium
from selenium.webdriver.support.ui import WebDriverWait
from iar_transcriber.palabra import Palabra
import psycopg2
import psycopg2.extensions
# import ujson
import sys
if sys.version_info.major == 2:
    import cPickle as pickle
    from HTMLParser import HTMLParser
elif sys.version_info.major == 3:
    import pickle
    from html.parser import HTMLParser
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE, None)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY, None)

__author__ = "Iván Arias Rodríguez"
__copyright__ = "Copyright 2017, Iván Arias Rodríguez"
__credits__ = [""]
__license__ = "GPL"  # No estoy seguro
__version__ = "1.0.1"
__maintainer__ = "Iván Arias Rodríguez"
__email__ = "ivan.arias.rodriguez@gmail.com"
__status__ = "Development"  # "Prototype", "Production"

directorio_archivos_rae_web =\
    dirname(os.path.realpath(__file__)) + u'/archivos_de_datos/rae/archivos_web/'
directorio_lemas = directorio_archivos_rae_web + u'lemas/'
# directorio_lemas = directorio_archivos_rae_web + u'lemas_para_pruebas/'
directorio_conjugaciones = directorio_archivos_rae_web + u'conjugaciones/'
nombre_archivo_verbos_desusados = directorio_archivos_rae_web + u'verbos_desusados.txt'
nombre_archivo_verbos_sin_conjugacion = directorio_archivos_rae_web + u'verbos_sin_conjugacion.txt'
nombre_archivo_no_verbos = directorio_archivos_rae_web + u'no_verbos.txt'
nombre_archivo_lemas_no_procesados = directorio_archivos_rae_web + u'lemas_no_procesados.txt'
nombre_archivo_lema_id = directorio_archivos_rae_web + u'lemas_ids.txt'


class ParseadorRae:
    def __init__(self):
        pass

    # TODO: Hay un problema al crear el lemario que probablemente debería corregirse. El problema viene del hecho de
    # que hay lemas de nombres o adjetivos, cuya forma principal tiene ambos géneros: vinagrero, ra. Estos lemas cubren
    # ambos géneros (y números), con lo que si se lematiza "vinagrera", se hará con el lema "vinagrero". No obstante,
    # dichos lemas incluyen acepciones en las que solo se usa la forma femenina ("vinagrera", botellita para el vinagre)
    # y que se incluyen en este mismo lema. En estos casos, cabe pensar si no debería tenerse un lema para el masculino
    # y otro para el femenino, siendo este segundo el lema de las formas femeninas.
    # No obstante, no tengo del todo claro esto. Ocurre que esto no solo pasa con el género, sino que también ocurre con
    # el número. "vinagrero, ra" tiene una acepción en femenino plural, "vinagreras", y por la misma regla de tres, se
    # tendría que crear un tercer lema: "vinagrero" lematizaría "vinagrero" y "vinagreros", y luego "vinagrera" y
    # "vinagreras" serían los otros dos lemas, que lematizarían cada uno se forma respectiva.
    # Esto puede ocurrir también en plural para el masculino, como en "anal".
    # TODO: no sé hasta qué punto lo de arriba se tiene que arreglar o no, ni tengo claro cuál sería la cantidad de
    # lemas afectados.
    @staticmethod
    def crea_lemario(crea_lemario_previo=False, reprocesa_lemario=True):
        # OJO: si se crea el lemario llamando desde este mismo archivo, en el if __name__ == '__main__':,
        #  pickle fallará cuando querramos cargar el lemario desde una librería externa (problemas con que los
        #  objetos que pickle ahora ve como lema, acepcion, entrada... luego se verán como iar_inflector.lema,
        #  iar_inflector.acepcion... y técnicamente serán distintos, con lo que no hallará la clase "correcta"
        #  y petará. Aquí más sobre esto:
        #  https://lists.gt.net/python/python/1175587
        #  Así que se puede crear el lemario desde aquí para hacer pruebas (desde aquí), pero como la idea es
        #  que se cargue desde fuera de aquí, se tiene que crear desde fuera.
        directorio_trabajo = dirname(os.path.realpath(__file__)) + u'/archivos_de_datos/rae/lemario/'
        if crea_lemario_previo:  # Implica reprocesar entradas
            lemario_previo = ParseadorRae.reprocesa_entradas(ParseadorRae.crea_lemario_previo())
        elif reprocesa_lemario:
            lemario_previo = ParseadorRae.reprocesa_entradas()
        else:
            nombre_archivo_lemario_previo = directorio_trabajo + u'lemario_previo_rae_reprocesado.pkl.bz2'
            print(u'Cargando lemario previo de: .../' +
                  u'/'.join(nombre_archivo_lemario_previo.split(u'/')[-5:]))
            with bz2.BZ2File(nombre_archivo_lemario_previo, 'rb') as archivo_lemario_previo:
                lemario_previo = pickle.load(archivo_lemario_previo)

        # Ahora convertimos esta estructura previa en la estructura con entradas, acepciones... estándar
        print(u'Creando lemario...')
        lemario = {}
        todas_las_abreviaturas = set()
        paises = set()
        regiones = set()
        ambitos = set()
        desconocidas = set()
        for lema_rae_txt, entradas_rae in sorted(lemario_previo.items()):
            if lema_rae_txt < u'cagar':
                pass
            entradas = []
            if entradas_rae[0]["formas_expandidas"][0][-1] == u'-' and \
                    entradas_rae[0]["formas_expandidas"][-1][0] in u'-‒' and\
                    len(lema_rae_txt) > 1:
                # Se trata de uno de los 18 elementos compositivos que puede actuar como prefijo o sufijo.
                # Ponemos como lema el texto precedido y seguido de guión para indicar que puede ir delante/detrás
                # y mantendremos la tilde que indica que la tonicidad es justo en la sílaba previa al sufijo.
                lema_txt = (entradas_rae[0]["formas_expandidas"][-1][:2]
                            if entradas_rae[0]["formas_expandidas"][-1][:2] == u'‒́'
                            else entradas_rae[0]["formas_expandidas"][-1][0]) +\
                           entradas_rae[0]["formas_expandidas"][0]
            else:
                lema_txt = entradas_rae[0]["formas_expandidas"][0]
            palabra_inicio = u''
            if palabra_inicio and lema_txt < palabra_inicio:
                continue
            if lema_txt == palabra_inicio:
                print(u'Nos hemos saltado hasta la palabra', palabra_inicio)
            for entrada_rae in entradas_rae:
                acepciones = []
                for acepcion_rae in entrada_rae["acepciones"]:
                    # Metemos los datos morfológicos de la entrada en la acepción. Es un poco sucio, pero es
                    # práctico y evita guardar esa información en las acepciones de cada entrada.
                    # acepcion_rae["morfo"] = entrada_rae["morfo"]
                    acepcion_rae["formas_expandidas"] = entradas_rae[0]["formas_expandidas"]
                    acepcion = AcepcionRae(acepcion_rae, entrada_rae)
                    acepciones.append(acepcion)
                    if False:
                        for ab in acepcion._borrame["todas"]:
                            if ab not in todas_las_abreviaturas:
                                print(lema_rae_txt, u'->', ab,
                                      u'{' + str(entrada_rae["n_entrada"]) + u'|' +
                                      str(acepcion_rae["n_acepcion"]) + u'}')
                                todas_las_abreviaturas |= {ab}
                        paises |= acepcion._borrame["paises"]
                        regiones |= acepcion._borrame["regiones"]
                        ambitos |= acepcion._borrame["ambitos"]
                        desconocidas |= acepcion._borrame["desconocidas"]
                for locucion_rae in entrada_rae["locuciones"]:
                    # TODO: deberíamos procesar el texto de la locución.
                    pass
                entradas.append(Entrada(acepciones, entrada_rae["locuciones"], entrada_rae["n_entrada"]))
            if lema_txt in lemario:
                # Puede ocurrir que haya dos entradas del mismo lema, pero que no tengan el mismo lema_rae.
                # Esto ocurre cuando un lema tiene entradas como nombre y como adjetivo y como nombre solo
                # tiene un género. Por ejemplo el caso de "cayuco1" y "cayuco2, ca", o "actor1, triz" y
                # "actor2, ra".
                lemario[lema_txt].append_entradas(entradas)
            else:
                lema = Lema(lema_txt, entradas)
                lemario[lema_txt] = lema
        if False:
            print(u'\nTODAS:\n', u'\n'.join(sorted(todas_las_abreviaturas)))
            print(u'\nPAÍSES:\n', u'\n'.join(sorted(paises)))
            print(u'\nREGIONES:\n', u'\n'.join(sorted(regiones)))
            print(u'\nÁMBITOS:\n', u'\n'.join(sorted(ambitos)))
            print(u'\nDESCONOCIDAS:\n', u'\n'.join(sorted(desconocidas)))

        n_lemas_multipalabra = 0
        n_entradas = 0
        n_acepciones = 0
        n_locuciones = 0
        for lema in lemario.values():
            if False and len(lema.get_lema_txt().split()) > 1:
                n_lemas_multipalabra += 1
                print(lema.get_lema_txt())
            for entrada in lema.get_entradas():
                n_entradas += 1
                n_acepciones += len(entrada.get_acepciones())
                n_locuciones += len(entrada.get_locuciones())
        print(u'El lemario incluye:\n\t-', len(lemario), u'lemas, de los cuales', n_lemas_multipalabra,
            u'son multipalabra.\n\t-', n_entradas, u'entradas.\n\t-',n_acepciones, u'acepciones.\n\t-',
            n_locuciones, u'locuciones.')
        if not os.path.exists(directorio_trabajo):
            os.makedirs(directorio_trabajo)
        nombre_archivo_lemario = directorio_trabajo + u'lemario_rae.pkl.bz2'
        print(u'Guardando lemario en .../' + u'/'.join(nombre_archivo_lemario.split(u'/')[-5:]))
        try:
            os.remove(nombre_archivo_lemario)
        except OSError:
            pass
        archivo_lemario = bz2.BZ2File(nombre_archivo_lemario, 'wb')
        pickle.dump(lemario, archivo_lemario, pickle.HIGHEST_PROTOCOL)
        archivo_lemario.close()
        return

    @staticmethod
    def crea_lemario_previo():
        # Creamos un lemario previo con la información de los archivos
        directorio_trabajo = dirname(os.path.realpath(__file__)) + u'/archivos_de_datos/rae/lemario/'
        if not os.path.exists(directorio_trabajo):
            os.makedirs(directorio_trabajo)
        print(u'Creando lemario previo...')
        lemario_previo = {}
        nombres_archivos_lemas = (f for f in listdir(directorio_lemas) if isfile(directorio_lemas + f))
        recuentos_entradas = {"validas": 0, "redirecciones": 0, "solo_locuciones": 0, "lemas_distintos": 0,
                              "signos": 0, "entradas": 0, "acepciones": 0, "locuciones": 0}
        n_entradas_procesadas = 0
        n_lemas_iniciales_saltados = 0
        for nombre_archivo_lema in nombres_archivos_lemas:
            recuentos_entradas["entradas"] += 1
            if False and nombre_archivo_lema < u'cagar':
                print(u'Borrrrrraaaaaaaaaa...')
                continue
            lema_rae_txt = nombre_archivo_lema.split(u'.')[0]
            if lema_rae_txt == u'cón':
                # Problema para nombrar archivos empezando por 'con...'
                lema_rae_txt = u'con'
            if not n_entradas_procesadas % 1000 and n_entradas_procesadas:
                print(n_entradas_procesadas, u'entradas procesadas')
            n_entradas_procesadas += 1
            if n_entradas_procesadas < n_lemas_iniciales_saltados:
                continue
            if False and lema_rae_txt < u'aun':
                continue

            archivo = codecs.open(directorio_lemas + nombre_archivo_lema, encoding='utf-8')
            texto_lema = archivo.read()
            archivo.close()

            parseador_articulo = ParseadorArticuloRae(lema_rae_txt)
            entrada_rae = parseador_articulo.parsea_entrada(texto_lema)
            if "acepciones" in entrada_rae:
                recuentos_entradas["acepciones"] += len(entrada_rae["acepciones"])
            if "locuciones" in entrada_rae:
                recuentos_entradas["locuciones"] += len(entrada_rae["locuciones"])
            if entrada_rae["acepciones"]:
                recuentos_entradas["validas"] += 1
            elif entrada_rae["locuciones"]:
                recuentos_entradas["solo_locuciones"] += 1
            elif entrada_rae["ids_alternativos"]:
                recuentos_entradas["redirecciones"] += 1
            if lema_rae_txt in lemario_previo:
                # Es un lema con más de una entrada. Cuando parseamos los artículos (lemas), cada entrada se
                # metió en un archivo distinto, diferenciado por su id. Como están ordenados por la id, no
                # están necesariamente ordenados por número de acepción, así que hay que reordenar.
                lemario_previo[lema_rae_txt] = sorted(lemario_previo[lema_rae_txt] + [entrada_rae],
                                                      key=lambda k: k["n_entrada"])
            else:
                lemario_previo[lema_rae_txt] = [entrada_rae]
                recuentos_entradas["lemas_distintos"] += 1

        # Añadimos los signos de puntuación. Deben añadirse tanto al lexicón como al lemario porque si no,
        # se pueden dar errores posteriormente al considerar que lo que aparece en el lexicón está ahí
        # porque se ha derivado de una entrada del lemario.
        # TODO: En realidad, aquí solo tiene sentido meter aquellos caracteres que el segmentador reconozca.
        # Se considera que el "lema" de un signo de apertura/cierre, es el de cierre.
        for signo in [u':', u',', u'}', u'etc', u'!', u'-', u')', u'%', u'.', u'?', u'"', u';', u'|', u']',
                      u'…', u'>', u"'", u'°', u'@', u'&', u'#', u'·']:
            acepcion_rae = {"lema_rae_txt": signo, "id": signo * 7, "abrs_morfo": [u'signo'],
                            "abrs_ambito": [], "abrs_post": [], "definicion": signo,
                            "definicion_post": u'', "ejemplos": [], "ejemplos_post": [], "n_acepcion": 0}
            entrada_rae = {"lema_rae_txt": signo, "formas_expandidas": [signo], "n_entrada": 0,
                           "id": signo * 7, "acepciones": [acepcion_rae], "locuciones": [],
                           "ids_alternativos": [], "morfo": {}}
            lemario_previo[signo] = [entrada_rae]
            recuentos_entradas["signos"] += 1

        print(n_entradas_procesadas, u'entradas procesadas:')
        print(u'\t- {:d} redirecciones.\n\t- {:d} lemas solo con locuciones.\n\t- {:d} lemas distintos.\n'
              u'\t- {:d} entradas con acepciones.'.format(recuentos_entradas["redirecciones"],
                                                          recuentos_entradas["solo_locuciones"],
                                                          recuentos_entradas["lemas_distintos"],
                                                          recuentos_entradas["validas"]))
        print(u'\t- {:d} entradas, {:d} acepciones, {:d} locuciones.'.\
            format(recuentos_entradas["entradas"],
                   recuentos_entradas["acepciones"],
                   recuentos_entradas["locuciones"]))
        print(u'Además se han añadido', recuentos_entradas["signos"], u'signos de puntuación.')

        nombre_archivo_lemario_previo = directorio_trabajo + u'lemario_previo_rae.pkl.bz2'
        print(u'Guardando lemario previo en .../' + u'/'.join(nombre_archivo_lemario_previo.split(u'/')[-5:]))
        try:
            os.remove(nombre_archivo_lemario_previo)
        except OSError:
            pass
        with bz2.BZ2File(nombre_archivo_lemario_previo, 'wb') as archivo_lemario:
            pickle.dump(lemario_previo, archivo_lemario, pickle.HIGHEST_PROTOCOL)

        return lemario_previo

    @staticmethod
    def reprocesa_entradas(lemario_previo=None):
        u"""Se copia el contenido de entradas que son redirecciones puras, y se eliminan superlativos, neutros, apócopes

        :param lemario_previo:
        :return:
        """
        directorio_trabajo = dirname(os.path.realpath(__file__)) + u'/archivos_de_datos/rae/lemario/'
        if not lemario_previo:
            if not os.path.exists(directorio_trabajo):
                os.makedirs(directorio_trabajo)
            nombre_archivo_lemario = directorio_trabajo + u'lemario_previo_rae.pkl.bz2'
            print(u'Reprocesando', nombre_archivo_lemario, u'...', end=u' ')
            with bz2.BZ2File(nombre_archivo_lemario, 'rb') as archivo_lemario:
                lemario_previo = pickle.load(archivo_lemario)
            print(u'cargado')
        else:
            print(u'Reprocesando', len(lemario_previo), u'entradas')

        # Nos creamos un diccionario para pasar de los ids a los lemas, ya que el lemario está indexado por
        # el lema.
        lemas_por_id = {f.split(u'.')[1]: f.split(u'.')[0] if f.split(u'.')[0] != u'cón' else u'con'
                        for f in (f for f in listdir(directorio_lemas) if isfile(directorio_lemas + f))}

        # lemario_previo = {lema_rae_txt: lemario_previo[lema_rae_txt] for lema_rae_txt in [u'mal', u'malo, la', u'peor']}
        for lema_rae_txt in sorted(lemario_previo.keys()):
            if lema_rae_txt not in lemario_previo:
                # Es una forma que hemos borrado por ser apócope, superlativo...
                print(lema_rae_txt, u'estaba borrado')
                continue
            entradas_rae = lemario_previo[lema_rae_txt]
            for entrada_rae in entradas_rae:
                # Primero procesamos los valores morfosintácticos, que enlazan los lemas con su lema "padre":
                # apócopes, formas átonas o tónicas, superlativos... En estos casos simplemente metemos la
                # forma txt de este lema en el campo del "morfo" del lema padre.
                for tipo_info in ["apocope", "apocope_plural", "forma_atona", "forma_tonica",
                                  "superlativo", "aumentativo", "diminutivo"]:
                    if "id_del_que_es_" + tipo_info in entrada_rae["morfo"]:
                        # Este lema es (una de) la(s) forma(s) átona/tónica(s)/apócope de otro lema, cuyo id
                        # tenemos.
                        # También puede ser un aumentativo/diminutivo.
                        # Metemos en ese lema padre la información de este lema. Ese otro lema tendrá que
                        # tener necesariamente una información del tipo "ids_formas_casos" en "morfo" que
                        # enlace directamente a este lema (así nos aseguramos de que estamos procesando
                        # correctamente).
                        # Aunque el lema con la información "ids_formas_casos" podría haber tomado la forma
                        # del lema, puesto que aparece en el <a del que ha sacado el id, no se hace, porque el
                        # texto que aparece en el <a no incluye información de variación en género, o al menos
                        # no siempre.
                        # Por ejemplo, el lema "él, ella" tiene a "lo2" como forma átona, y al abrir dicho
                        # lema, vemos que en realidad es "lo, la".
                        id_alternativo = entrada_rae["morfo"]["id_del_que_es_" + tipo_info]
                        lema_alternativo = lemas_por_id[id_alternativo]
                        entrada_alternativa = [e for e in lemario_previo[lema_alternativo]
                                               if id_alternativo == e["id"]][0]
                        # Hemos encontrado el lema "padre". así que le metemos la información de este lema
                        # en su parte de morfología
                        if tipo_info in ["aumentativo", "diminutivo"]:
                            # Viene la forma "RAE", tal que "bobalicón, na", "indezuelo, la"
                            entrada_alternativa["morfo"][tipo_info + "s"] = \
                                entrada_alternativa["morfo"].setdefault(tipo_info + "s", []) + \
                                [[f] for f in
                                 ParseadorRae.extrae_formas_de_lema(lema_rae_txt)]
                        elif tipo_info in ["forma_atona", "superlativo"]:
                            tag_txt = "formas_atonas_txt" if tipo_info == "forma_atona" else (tipo_info + "s_txt")
                            entrada_alternativa["morfo"].setdefault(tag_txt, []).append(lema_rae_txt)
                        else:  # elif tipo_info in ["apocope", "apocope_plural", "forma_tonica"]
                            tag_txt = tipo_info + "_txt"
                            if tag_txt in entrada_alternativa["morfo"] and \
                                    entrada_alternativa["morfo"][tag_txt] != lema_rae_txt:
                                print(u'Tenemos dos etiquetas', tipo_info, u'para el lema',
                                    entrada_alternativa["lema_rae_txt"], u':', entrada_alternativa["morfo"][tag_txt],
                                    lema_rae_txt, u'y en teoría es monovaluado')
                            entrada_alternativa["morfo"][tag_txt] = lema_rae_txt

                        # print(u'Se ha añadido', lema_rae_txt, u'como', tipo_info, u'de', entrada_alternativa["lema_rae_txt"])
                        if tipo_info in ["apocope", "apocope_plural", "superlativo",
                                         "aumentativo", "diminutivo"]:
                            # En estos casos, el lema que estamos procesando es una redirección sin más.
                            # Borramos. Además, metemos las locuciones al lema padre
                            # TODO: esto es un poco arriesgado, creo.
                            entrada_alternativa["locuciones"] += entrada_rae["locuciones"]
                            entrada_rae["desechable"] = True
                        elif tipo_info in ["forma_atona", "forma_tonica"]:
                            if "ids_formas_casos" in entrada_alternativa["morfo"]:
                                entrada_alternativa["morfo"]["ids_formas_casos"].remove(entrada_rae["id"])
                            else:
                                print(u'La', tipo_info, lema_rae_txt, u'no aparecía listada en su lema padre', entrada_alternativa["lema_rae_txt"])
                        break
                if "id_del_que_es_participio_irregular" in entrada_rae["morfo"]:
                    # Esta entrada es simplemente el participio irregular de algún verbo. No nos interesa porque ya
                    # lo sacamos del archivo de conjugación. Borramos la entrada.
                    entrada_rae["desechable"] = True
                    # print(u'Borrado el lema', lema_rae_txt, u'por ser un participio irregular')

                if "id_apocope" in entrada_rae["morfo"] and "apocope_txt" not in entrada_rae["morfo"]:
                    # Se ha podido encontrar antes el apócope y haberlo añadido ya (y borrado la acepción del apócope)
                    id_alternativo = entrada_rae["morfo"]["id_apocope"]
                    lema_alternativo = lemas_por_id[id_alternativo]
                    entrada_alternativa = [e for e in lemario_previo[lema_alternativo] if id_alternativo == e["id"]][0]
                    entrada_rae["morfo"]["apocope_txt"] = entrada_alternativa["lema_rae_txt"]
                    # print(u'Se ha añadido', entrada_alternativa["lema_rae_txt"], u'como apócope de', lema_rae_txt)

                if "id_apocope_plural" in entrada_rae["morfo"] and "apocope_plural_txt" not in entrada_rae["morfo"]:
                    # Se ha podido encontrar antes el apócope y haberlo añadido ya (y borrado la acepción del apócope)
                    id_alternativo = entrada_rae["morfo"]["id_apocope_plural"]
                    lema_alternativo = lemas_por_id[id_alternativo]
                    entrada_alternativa = [e for e in lemario_previo[lema_alternativo] if id_alternativo == e["id"]][0]
                    entrada_rae["morfo"]["apocope_plural_txt"] = entrada_alternativa["lema_rae_txt"]
                    print(u'Se ha añadido', entrada_alternativa["lema_rae_txt"], u'como apócope plural de', lema_rae_txt)

                if "ids_formas_casos" in entrada_rae["morfo"]:
                    # Es un poco la visión contraria a los "id_del_que_es_forma...". Cuando está la info
                    # "ids_formas_casos", los ids pueden ser formas átonas o tónicas (que se cubren con el código de
                    # arriba) y también formas amalgamadas, que no tienen un "id_del_que_es_amalgama" o algo así, porque
                    # en la parte de morfología no se expresa con el formato necesario.
                    for id_alternativo in entrada_rae["morfo"]["ids_formas_casos"]:
                        lema_alternativo = lemas_por_id[id_alternativo]
                        entradas_alternativas = [e for e in lemario_previo[lema_alternativo]
                                                 if id_alternativo == e["id"]]
                        if entradas_alternativas and "es_pronombre_amalgamado" in entradas_alternativas[0]["morfo"]:
                            entrada_rae["morfo"]["forma_amalgamada_txt"] = entradas_alternativas[0]["lema_rae_txt"]
                            # print(u'Se ha añadido', entradas_alternativas[0]["lema_rae_txt"], u'como forma amalgamada de', lema_rae_txt)
                            break
                    pass

                # No tenemos algo como id_del_que_es_comparativo, porque cuando la RAE marca expresamente que
                # un lema es la forma comparativa de un adjetivo, no da el id, solo la forma base
                if "lemas_de_los_que_es_comparativo" in entrada_rae["morfo"]:
                    # Este lema es el comparativo de otro(s) y tenemos los lemas. Vamos al lema del que somos
                    # comparativo y le marcamos el valor del comparativo.
                    for lema_alternativo in entrada_rae["morfo"]["lemas_de_los_que_es_comparativo"]:
                        for entrada_alternativa in lemario_previo[lema_alternativo]:
                            entrada_alternativa["morfo"]["id_comparativo"] = entrada_rae["id"]
                            entrada_alternativa["morfo"]["comparativo_txt"] = lema_rae_txt
                            # Además, metemos las locuciones al lema padre
                            # TODO: esto es un poco arriesgado, creo.
                            entrada_alternativa["locuciones"] += entrada_rae["locuciones"]
                            entrada_rae["desechable"] = True
                            # print(u'Se ha añadido', lema_rae_txt, u'como comparativo de', entrada_alternativa["lema_rae_txt"])

                # Las entradas que sean meras redirecciones (y cuyo contenido se tiene que copiar) tendrán
                # algún ids_alternativos y las locuciones a las que le pase lo mismo, tendrán un id que
                # incluirá un símbolo # que separa el id de la entrada y el de la acepción/locucion.
                # A menudo, estas redirecciones se producen en lemas que representan formas neutras, apócopes
                # o plurales.
                # Usualmente estos lemas no incluyen ninguna información, solo redirigen, así que se eliminan.
                if entrada_rae["ids_alternativos"] and not entrada_rae["acepciones"] and not entrada_rae["locuciones"]:
                    # Si la entrada contiene ids_alternativos, es que el artículo era una pura redirección.
                    # Según el tipo de redirección, tendremos que borrar directamente la entrada y copiarlo.
                    # Copiamos del lema alternativo "maestro" (el que contiene definiciones), y dejamos lema_txt,
                    # id y n_entrada.
                    # Tenemos que copiar toda la entrada. Aunque tenemos una lista de ids_alternativos, en realidad
                    # solo uno contendrá información (originalmente). Puede haber más de uno que tenga ya esta
                    # información, porque la haya copiado en este mismo punto en un loop anterior.
                    # Cuando en una entrada de una acepción hay un enlace a un lema o locución, siempre pone antes
                    # las etiquetas morfológicas, con lo que se han ignorado ya (no hace falta)
                    for id_alternativo in entrada_rae["ids_alternativos"]:
                        id_entrada_alternativa = id_alternativo.split(u'#')[0]
                        if not id_entrada_alternativa:
                            # Esto es porque el id es del tipo #XXXXXXX, que indica un enlace a una locución
                            # de este mismo lema.
                            entrada_alternativa = entrada_rae
                        else:
                            lema_alternativo = lemas_por_id[id_entrada_alternativa]
                            # El lema incluye varias entradas, pero queremos la entrada del id alternativo
                            entradas_alternativas = lemario_previo[lema_alternativo]
                            entrada_alternativa = [e for e in entradas_alternativas
                                                   if e["id"] == id_entrada_alternativa][0]
                        if entrada_alternativa["acepciones"] or entrada_alternativa["locuciones"]:
                            # Si la entrada no tiene acepciones de ningún tipo, pero la alternativa sí, puede ser una
                            # redirección, o un simple apócope, forma plural, femenina o neutra o variación ortográfica
                            if lema_rae_txt in entrada_alternativa["formas_expandidas"]:
                                # Es una entrada que indica la forma femenina (atípica) de otro lema. Borramos
                                # print(u'ATENCIÓN:', lema_rae_txt, u'es el femenino de', entrada_alternativa["lema_rae_txt"])
                                entrada_rae["desechable"] = True  # Se borrará al final
                            else:
                                for tipo_info in ["apocope", "plural", "neutro", "apocope_plural"]:
                                    if "id_" + tipo_info in entrada_alternativa["morfo"] and \
                                            entrada_alternativa["morfo"]["id_" + tipo_info] == entrada_rae["id"]:
                                        # Esta entrada es tan solo el apócope/plural/neutro de la entrada alternativa.
                                        # Lo borramos pero antes metemos el valor del lema en la entrada relacionada.
                                        if tipo_info == "plural":
                                            # Viene la forma "RAE", tal que "los, las".
                                            entrada_alternativa["morfo"]["formas_plural"] = \
                                                entrada_alternativa["morfo"].setdefault("formas_plural", []) + \
                                                [[f] for f in
                                                 ParseadorRae.extrae_formas_de_lema(entrada_rae["lema_rae_txt"])]
                                        else:
                                            entrada_alternativa["morfo"][tipo_info + "_txt"] =\
                                                entrada_rae["lema_rae_txt"]
                                        # print(u'Borrado', lema_rae_txt, u'por ser un', tipo_info)
                                        entrada_rae["desechable"] = True  # Se borrará al final
                                        break  # Antes de ir al lema siguiente se mirarán las locuciones, pero no hay
                                # TODO: en realidad deberíamos procesar como abajo todos los Tb. ... Por ejemplo, de
                                # "sicoanálisis" ahora se copian las entradas de "psicoanálisis", pero en realidad
                                # se debería meter dentro de la entrada de "psicoanálisis" una "forma_alternativa" o
                                # algo así, y que la forma "sicoanálisis" se borrara, pero que al flexionar "psico..."
                                # también creara las formas de "sicoanálisis". No obstante habría que borrar la
                                # acepción y no toda la entrada (si ves "transporte" y "trasporte" verás esto).
                                if "desechable" not in entrada_rae and \
                                        "ids_conjugacion" in entrada_alternativa["morfo"] and \
                                        len(entrada_alternativa["morfo"]["ids_conjugacion"]) > 1:
                                    # Es un verbo tipo "sicoanalizar" que redirige a "psicoanalizar". Como el lema
                                    # más aceptado tiene varias conjugaciones, eso incluye a este lema
                                    # print(u'Marcamos', lema_rae_txt, u'como desechable porque debería ser una variante menos aceptada de un verbo con variante ortográfica')
                                    entrada_rae["desechable"] = True

                            if "desechable" in entrada_rae:
                                break

                            # Se trata de una redirección pura, que no es apócope/plural/neutro ni variación ortográfica
                            # de verbo. Así que copiamos las acepciones/locuciones
                            entrada_rae["morfo"] = entrada_alternativa["morfo"]
                            if u'#' in id_alternativo:
                                # De una entrada se redirige a una locución, como en 'malcontentadizo', que es una
                                # pura redirección a la locución 'mal contentadizo' de la entrada de 'contentadizo'
                                # Debemos buscar la locución por su id
                                id_locucion_alternativa = id_alternativo.split(u'#')[1]
                                locucion_alternativa = [l for l in entrada_alternativa["locuciones"]
                                                        if l["id"] == id_locucion_alternativa][0]
                                entrada_rae["acepciones"] = copy.deepcopy(locucion_alternativa["acepciones"])
                            else:
                                # Se redirige a otra entrada. Copiamos los datos relevantes
                                entrada_rae["acepciones"] = copy.deepcopy(entrada_alternativa["acepciones"])
                                entrada_rae["locuciones"] = copy.deepcopy(entrada_alternativa["locuciones"])
                            for acepcion in entrada_rae["acepciones"] + [acep for loc in entrada_rae["locuciones"]
                                                                         for acep in loc["acepciones"]]:
                                acepcion["lema_rae_txt"] = lema_rae_txt
                            break
                    else:
                        print(u'ids alternativos que se enlazan entre sí')
                        # Esta entrada tiene una única acepción, y es la redirección. Podríamos pasar al
                        # siguiente lema. No obstante, cabe la posibilidad de que las locuciones del lema
                        # "maestro" tengan a su vez redirecciones. Así que las miramos ya.

                # Procesamos las locuciones
                for locucion in entrada_rae["locuciones"]:
                    if locucion["ids_alternativos"] and not locucion["acepciones"]:
                        # Es una locución que es una pura redirección. Hay que sacar las acepciones de otro lema.
                        # La redireción puede ser desde una locución (bien intencionado) a un lema completo
                        # (bienintencionado), o a otra locución (id_entrada#id_locucion)
                        for id_alternativo in locucion["ids_alternativos"]:
                            id_entrada_alternativa = id_alternativo.split(u'#')[0]
                            if not id_entrada_alternativa:
                                # Esto es porque el id es del tipo #XXXXXXX, que indica un enlace a una locución
                                # de este mismo lema.
                                entrada_alternativa = entrada_rae
                            else:
                                lema_alternativo = lemas_por_id[id_entrada_alternativa]
                                # El lema incluye varias entradas, pero queremos la entrada del id alternativo
                                entradas_alternativas = lemario_previo[lema_alternativo]
                                entrada_alternativa = [e for e in entradas_alternativas
                                                       if e["id"] == id_entrada_alternativa][0]
                            if entrada_alternativa["acepciones"] or entrada_alternativa["locuciones"]:
                                if u'#' in id_alternativo:
                                    # Se redirige a una locución de otra entrada (o de esta misma, pero da igual).
                                    # Debemos buscar la locución por su id
                                    id_locucion_alternativa = id_alternativo.split(u'#')[1]
                                    locuciones_alternativas = [l for l in entrada_alternativa["locuciones"]
                                                               if l["id"] == id_locucion_alternativa]
                                    if not locuciones_alternativas:
                                        # Esto pasa con "Allen", que redirige a "llave allen", y resulta que en "llave"
                                        # aparece la locución "llave Allen", con un "Tb. ~ allen". El problema es que
                                        # se redirige a la locución NUa9bLt#GQ50xlD, pero "llave Allen" es #G7qEiOG, y
                                        # no hay manera de encontrar esa locución, porque el id no existe. Está mal.
                                        # En "llave" coincide que la primera locución es "llave Allen" (por las
                                        # mayúsculas). Pasa con otras 6-7 más, por lo mismo.
                                        for locucion_alternativa in entrada_alternativa["locuciones"]:
                                            if locucion_alternativa["locucion"] == locucion["locucion"]:
                                                # Lo rebautizamos con el id que no llevaba a ninguna parte
                                                locucion_alternativa["id"] = id_locucion_alternativa
                                                break
                                        locucion["id"] = u''
                                    else:
                                        locucion_alternativa = locuciones_alternativas[0]
                                    locucion["acepciones"] = locucion_alternativa["acepciones"]
                                    if not locucion["id"]:
                                        locucion["id"] = locucion_alternativa["id"]
                                else:
                                    # Se redirige a una entrada completa: bien intencionado -> bienintencionado
                                    locucion["acepciones"] = entrada_alternativa["acepciones"]
                                    if not locucion["id"]:
                                        locucion["id"] = entrada_alternativa["id"]
                                break
                        else:
                            print(u'ids alternativos que se enlazan entre sí')
            # En los verbos con varias entradas, es habitual que solo una de ellas (a veces más) tenga la
            # información de la conjugación. El resto no tiene, aunque aparentemente, es la misma. A veces son
            # acepciones desusadas y cosas así, pero otras veces no.
            ids_conj = []
            falta_id = False
            for entrada_rae in entradas_rae:
                if "ids_conjugacion" in entrada_rae["morfo"]:
                    # Tenemos info de conjugación. La guardamos por si a otra entrada le falta
                    if not ids_conj:
                        # Es la primera entrada con info de conjugación. Guardamos la información
                        ids_conj = entrada_rae["morfo"]["ids_conjugacion"]
                        if falta_id:
                            # Había alguna entrada previa que era verbo y no tenía info de conjugación
                            for e in entradas_rae:
                                if "ids_conjugacion" in e["morfo"]:
                                    # Hemos llegado a esta misma entrada, salimos del bucle
                                    break
                                # Le ponemos a esa entrada previa, la info de conjugación
                                e["morfo"]["ids_conjugacion"] = ids_conj
                                # print(u'Se ha asignado la conjugacion', ids_conj, u'a', lema_rae_txt, u'en la entrada', e["n_entrada"])
                            falta_id = False
                elif entrada_rae["acepciones"] and entrada_rae["acepciones"][0]["abrs_morfo"] and \
                        entrada_rae["acepciones"][0]["abrs_morfo"][0].split()[0].lower() == u'verbo':
                    # Esta entrada es para un verbo y no tenemos info de conjugación
                    if ids_conj:
                        # Una entrada previa ya la tenía. La cogemos de ahí.
                        entrada_rae["morfo"]["ids_conjugacion"] = ids_conj
                        # print(u'Se ha asignado la conjugacion', ids_conj, u'a', lema_rae_txt, u'en la entrada', entrada_rae["n_entrada"])
                    else:
                        # No hay ninguna entrada previa con esta información. Marcamos por si una posterior sí la tiene
                        falta_id = True
            if falta_id:
                # print(lema_rae_txt, u'no tiene info de conjugación')
                pass

        # Eliminamos las entradas (e incluso lemas) que sean desechables. Maqueamos el resto.
        for lema_rae_txt in list(lemario_previo.keys()):
            for orden_entrada in range(len(lemario_previo[lema_rae_txt]) - 1, -1, -1):
                if "desechable" in lemario_previo[lema_rae_txt][orden_entrada]:
                    # Por algún motivo, esta entrada se incluye en otro lema y es una redirección sin más.
                    # Borramos.
                    if len(lemario_previo[lema_rae_txt]) == 1:
                        lemario_previo.pop(lema_rae_txt)
                    else:
                        del lemario_previo[lema_rae_txt][orden_entrada]
                else:
                    # Tras procesarlo, ya no tiene sentido guardar los ids_alternativos.
                    lemario_previo[lema_rae_txt][orden_entrada].pop("ids_alternativos", None)
                    for locucion in lemario_previo[lema_rae_txt][orden_entrada]["locuciones"]:
                        locucion.pop("ids_alternativos", None)

        if not os.path.exists(directorio_trabajo):
            os.makedirs(directorio_trabajo)
        nombre_archivo_lemario = directorio_trabajo + u'lemario_previo_rae_reprocesado.pkl.bz2'
        print(u'Guardando lemario reprocesado en .../' + u'/'.join(nombre_archivo_lemario.split(u'/')[-5:]))
        try:
            os.remove(nombre_archivo_lemario)
        except OSError:
            pass
        archivo_lemario = bz2.BZ2File(nombre_archivo_lemario, 'wb')
        pickle.dump(lemario_previo, archivo_lemario, pickle.HIGHEST_PROTOCOL)
        archivo_lemario.close()
        return lemario_previo

    @staticmethod
    def subdivide_lemario(lemario=None, nombre_archivo_lemario=None):
        u"""Se toma el lemario completo y se subdivide en partes según su categoría y su tipo.

        :type lemario: {unicode: Lema}
        :param lemario:
        :type nombre_archivo_lemario: unicode
        :param nombre_archivo_lemario: Path completo del archivo que contiene el lemario de la RAE
        :return:
        """
        lemario_subdividido = {}
        directorio_trabajo = dirname(os.path.realpath(__file__)) + u'/archivos_de_datos/rae/lemario/'
        if not lemario:
            if not nombre_archivo_lemario:
                nombre_archivo_lemario = directorio_trabajo + u'lemario_rae.pkl.bz2'
                if not os.path.exists(nombre_archivo_lemario):
                    ParseadorRae.crea_lemario()
            with bz2.BZ2File(nombre_archivo_lemario, 'rb') as entrada:
                lemario = pickle.load(entrada)
        print(u'Subdividiendo lemario...')
        n_entradas_total = 0
        n_lemas_con_n_entradas = {}
        n_acepciones_total = 0
        n_entradas_con_n_acepciones = {}
        n_subacepciones = 0
        n_acepciones_unicas = 0  # En realidad es la suma de la cantidad de lemas que aparecen en cada categoría
        recuento_por_categorias = {}
        for lema_txt, lema in sorted(lemario.items()):
            for orden_entrada, entrada in enumerate(lema.get_entradas()):
                n_entradas_total += 1
                n_lemas_con_n_entradas[orden_entrada + 1] = n_lemas_con_n_entradas.setdefault(orden_entrada + 1, 0) + 1
                if orden_entrada > 0:
                    n_lemas_con_n_entradas[orden_entrada] -= 1
                acepciones = entrada.get_acepciones()
                n_acepciones_total += len(acepciones)
                n_entradas_con_n_acepciones[len(acepciones)] =\
                    n_entradas_con_n_acepciones.setdefault(len(acepciones), 0) + 1
                for orden_acepcion, acepcion in enumerate(acepciones):
                    n_subacepciones += len(acepcion.get_acepciones_derivadas())
                    datos_y_derivados = [acepcion.get_datos()] + acepcion.get_acepciones_derivadas()
                    acepcion.reset_acepciones_derivadas()
                    for orden_datos, datos in enumerate(datos_y_derivados):
                        acepcion_monocategorial = copy.deepcopy(acepcion)
                        acepcion_monocategorial.set_datos(datos)
                        if orden_datos > 0:
                            acepcion_monocategorial.set_n_acepcion(float(acepcion.get_n_acepcion()) + 0.1)
                        categoria = acepcion_monocategorial.get_categoria()
                        # Añadimos al lemario subdividido
                        if categoria not in lemario_subdividido:
                            lemario_subdividido[categoria] = {}
                            recuento_por_categorias[categoria] = {"n_entradas": 0, "n_acepciones": 0,
                                                                  "n_subacepciones": 0}
                        if lema_txt not in lemario_subdividido[categoria]:
                            lemario_subdividido[categoria][lema_txt] = Lema(lema_txt, [])
                            n_acepciones_unicas += 1
                        entradas_previas = lemario_subdividido[categoria][lema_txt].get_entradas()
                        if not entradas_previas or entradas_previas[-1].get_n_entrada() != entrada.get_n_entrada():
                            lemario_subdividido[categoria][lema_txt].\
                                append_entradas([Entrada([], [], entrada.get_n_entrada())])
                            recuento_por_categorias[categoria]["n_entradas"] += 1
                        lemario_subdividido[categoria][lema_txt].get_entradas()[-1].\
                            append_acepcion(acepcion_monocategorial)
                        if orden_datos == 0:
                            recuento_por_categorias[categoria]["n_acepciones"] += 1
                        else:
                            recuento_por_categorias[categoria]["n_subacepciones"] += 1
                        pass
                for orden_locucion, locucion in enumerate(entrada.get_locuciones()):
                    # TODO: tendríamos que meter las locuciones en las respectivas categorías
                    pass
        print(u'RECUENTO de contenido total del lemario RAE:')
        print(u'- Nº de lemas:', len(lemario))
        print(u'- Nº de entradas totales:', n_entradas_total)
        for n_entradas, n_lemas in n_lemas_con_n_entradas.items():
            print(u'  - Nº de lemas con', n_entradas, u'entradas:', n_lemas)
        print(u'- Nº de acepciones totales:', n_acepciones_total)
        for n_acepciones, n_entradas in n_entradas_con_n_acepciones.items():
            if n_entradas > 0:
                print(u'  - Nº de entradas con', n_acepciones, u'acepciones:', n_entradas)
        print(u'- Nº de subacepciones:', n_subacepciones, u'(sustantivos usados también como adjetivos, '
                                                          u'adjetivos usados también como sustantivos, etc)')
        print(u'- Nº de acepciones únicas:', n_acepciones_unicas, u'(acepciones de lemas distintos '
                                                                  u'o con distinta categoría gramatical)')
        print(u'\nRECUENTO por categoría:')
        for categoria, recuentos in sorted(recuento_por_categorias.items(),
                                           key=lambda tupla: -len(lemario_subdividido[tupla[0]])):
            categoria_txt = CATEGORIAS_A_TXT[categoria]
            ejemplos = sorted(lemario_subdividido[categoria].keys())[0::int(len(lemario_subdividido[categoria].keys())/4.1)]
            print(u'-', categoria_txt + u':', u', '.join(ejemplos) + u'...')
            print(u'  - Nº de lemas:', len(lemario_subdividido[categoria]))
            print(u'  - Nº de entradas:', recuento_por_categorias[categoria]["n_entradas"])
            print(u'  - Nº de acepciones:', recuento_por_categorias[categoria]["n_acepciones"], u'(sin subacepciones)')
            print(u'  - Nº de subacepciones:', recuento_por_categorias[categoria]["n_subacepciones"],
                u'(acepciones de otra categoría usadas también como', categoria_txt.lower() + u')')
            nombre_archivo_sublemario = directorio_trabajo + u'sublemario_rae-' + categoria_txt.lower() + u'.pkl.bz2'
            print(u'Guardando sublemario en .../' + u'/'.join(nombre_archivo_sublemario.split(u'/')[-5:]))
            with bz2.BZ2File(nombre_archivo_sublemario, 'wb') as archivo_lemario:
                pickle.dump(lemario_subdividido[categoria], archivo_lemario, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def carga_lemario(incluye_categoria=u''):
        print(u'Cargando lemario...')
        directorio_trabajo = dirname(os.path.realpath(__file__)) + u'/archivos_de_datos/rae/lemario/'
        if incluye_categoria:
            nombre_archivo_lemario = directorio_trabajo + u'sublemario_rae-' +\
                                     CATEGORIAS_A_TXT[incluye_categoria].lower() + u'.pkl.bz2'
        else:
            nombre_archivo_lemario = directorio_trabajo + u'lemario_rae.pkl.bz2'
        if not os.path.exists(nombre_archivo_lemario):
            print(u'Falta el archivo', nombre_archivo_lemario + u'. Es necesario crear el lemario.')
            return {}
        print(u'Cargando archivo', u'.../' + u'/'.join(nombre_archivo_lemario.split(u'/')[-5:]))
        with bz2.BZ2File(nombre_archivo_lemario, 'rb') as entrada:
            # Si está petando aquí diciendo que no encuentra el módulo lema, es que hemos creado el lemario
            # desde este mismo paquete. Mira lo que pone en el texto al inicio de crea_lemario.
            lemario = pickle.load(entrada)
        return lemario

    @staticmethod
    def formas_mas_prolificas(categoria):
        maximos = {"mas_tags": {"n_tags": 0, "lemas_txt": [], "flexiones": []},
                   "mas_formas": {"n_formas": 0, "lemas_txt": [], "flexiones": []},
                   "mas_formas_distintas": {"n_formas_distintas": 0, "lemas_txt": [], "flexiones": []}}
        minimos = {"menos_tags": {"n_tags": 999999, "lemas_txt": [], "flexiones": []},
                   "menos_formas": {"n_formas": 999999, "lemas_txt": [], "flexiones": []},
                   "menos_formas_distintas": {"n_formas_distintas": 999999, "lemas_txt": [], "flexiones": []}}
        lemario = ParseadorRae.carga_lemario(incluye_categoria=categoria)
        if False:
            lemas = u'mucho'.split()
            lemario = {k: lemario[k] for k in lemas}
            if False:
                for lema in lemas:
                    lemario[lema]._entradas[0]._acepciones = lemario[lema]._entradas[0]._acepciones[17:19]
        for orden_lema, (lema_txt, lema) in enumerate(lemario.items()):
            if False:
                hay_apocope = False
                hay_neutro = False
                for entrada in lema.get_entradas():
                    for acepcion in entrada.get_acepciones():
                        if not hay_apocope and acepcion.get_apocope_txt():
                            print(lema_txt, u'tiene apocope', acepcion.get_apocope_txt())
                            hay_apocope = True
                        if not hay_neutro and acepcion.get_neutro_txt():
                            print(lema_txt, u'tiene neutro', acepcion.get_neutro_txt())
                            hay_neutro = True
                continue
            formas_flexionadas = Flexionador.flexiona_lema_rae(lema, ajusta_lema=True,
                                                               incluye_cliticos=True)
            formas_flexionadas = {k: v for k, v in formas_flexionadas.items() if k[0] == categoria}
            for tag in formas_flexionadas.keys():
                longitud_recortada = 12 if categoria == VERBO else len(tag) - 1
                tag_recortada = tag[:longitud_recortada]
                if tag_recortada in formas_flexionadas:
                    for forma, origenes in formas_flexionadas[tag].items():
                        if forma in formas_flexionadas[tag_recortada]:
                            formas_flexionadas[tag_recortada][forma] += origenes
                        else:
                            formas_flexionadas[tag_recortada][forma] = origenes
                else:
                    formas_flexionadas[tag_recortada] = formas_flexionadas[tag]
                del formas_flexionadas[tag]
            n_tags = len(formas_flexionadas)
            n_formas = sum(len(v) for k, v in formas_flexionadas.items())
            n_formas_distintas = len(set(f for k, v in formas_flexionadas.items() for f in v.keys()))
            if False:
                print(lema_txt, n_formas, n_tags, n_formas_distintas)
            if n_tags >= maximos["mas_tags"]["n_tags"]:
                if n_tags > maximos["mas_tags"]["n_tags"]:
                    maximos["mas_tags"]["n_tags"] = n_tags
                    maximos["mas_tags"]["lemas_txt"] = []
                    maximos["mas_tags"]["flexiones"] = []
                maximos["mas_tags"]["lemas_txt"].append(lema_txt)
                # maximos["mas_tags"]["flexiones"].append(formas_flexionadas)
            if n_formas >= maximos["mas_formas"]["n_formas"]:
                if n_formas > maximos["mas_formas"]["n_formas"]:
                    maximos["mas_formas"]["n_formas"] = n_formas
                    maximos["mas_formas"]["lemas_txt"] = []
                    maximos["mas_formas"]["flexiones"] = []
                maximos["mas_formas"]["lemas_txt"].append(lema_txt)
                # maximos["mas_formas"]["flexiones"].append(formas_flexionadas)
            if n_formas_distintas >= maximos["mas_formas_distintas"]["n_formas_distintas"]:
                if n_formas_distintas > maximos["mas_formas_distintas"]["n_formas_distintas"]:
                    maximos["mas_formas_distintas"]["n_formas_distintas"] = n_formas_distintas
                    maximos["mas_formas_distintas"]["lemas_txt"] = []
                    maximos["mas_formas_distintas"]["flexiones"] = []
                maximos["mas_formas_distintas"]["lemas_txt"].append(lema_txt)
                # maximos["mas_formas_distintas"]["flexiones"].append(formas_flexionadas)
            if n_tags <= minimos["menos_tags"]["n_tags"]:
                if n_tags < minimos["menos_tags"]["n_tags"]:
                    minimos["menos_tags"]["n_tags"] = n_tags
                    minimos["menos_tags"]["lemas_txt"] = []
                    minimos["menos_tags"]["flexiones"] = []
                minimos["menos_tags"]["lemas_txt"].append(lema_txt)
                # minimos["menos_tags"]["flexiones"].append(formas_flexionadas)
            if n_formas <= minimos["menos_formas"]["n_formas"]:
                if n_formas < minimos["menos_formas"]["n_formas"]:
                    minimos["menos_formas"]["n_formas"] = n_formas
                    minimos["menos_formas"]["lemas_txt"] = []
                    minimos["menos_formas"]["flexiones"] = []
                minimos["menos_formas"]["lemas_txt"].append(lema_txt)
                # minimos["menos_formas"]["flexiones"].append(formas_flexionadas)
            if n_formas_distintas <= minimos["menos_formas_distintas"]["n_formas_distintas"]:
                if n_formas_distintas < minimos["menos_formas_distintas"]["n_formas_distintas"]:
                    minimos["menos_formas_distintas"]["n_formas_distintas"] = n_formas_distintas
                    minimos["menos_formas_distintas"]["lemas_txt"] = []
                    minimos["menos_formas_distintas"]["flexiones"] = []
                minimos["menos_formas_distintas"]["lemas_txt"].append(lema_txt)
                # minimos["menos_formas_distintas"]["flexiones"].append(formas_flexionadas)
            if int((orden_lema + 1) % (float(len(lemario)) / 100)) == 0:
                sys.stdout.write(u'.')
        print(u'')
        print(maximos)
        print(minimos)
        return maximos, minimos

    @staticmethod
    def crea_lexicon(incluye_cliticos=True, incluye_categorias=u'', subdivide_lexicon=True,
                     crea_lexicon_sql=True):
        u"""

        :param incluye_cliticos:
        :param incluye_categorias:
        :return:
        """
        # TODO: Incluir de alguna manera las locuciones
        print(u'Creando lexicón...')
        directorio_trabajo = dirname(os.path.realpath(__file__)) + u'/archivos_de_datos/rae/lemario/'
        if incluye_categorias:
            nombre_archivo_lemario = directorio_trabajo + u'sublemario_rae-' +\
                CATEGORIAS_A_TXT[incluye_categorias[0]].lower() + u'.pkl.bz2'
            print(u'TESTEANDO: SOLO INCLUIMOS LA CATEGORIA', CATEGORIAS_A_TXT[incluye_categorias[0]].upper())
        else:
            nombre_archivo_lemario = directorio_trabajo + u'lemario_rae.pkl.bz2'
        if not os.path.exists(nombre_archivo_lemario):
            print(u'Falta el archivo', nombre_archivo_lemario + u'. Es necesario crear el lemario.')
            return

        print(u'\nProcesando archivo', u'.../' + u'/'.join(nombre_archivo_lemario.split(u'/')[-5:]))
        with bz2.BZ2File(nombre_archivo_lemario, 'rb') as entrada:
            lemario = pickle.load(entrada)
        pass
        lexicon = {}
        # El lexicón es un dict donde a cada clave (forma), se le asigna un dict donde las claves son los lemas,
        # y a cada una se le asigna otro dict donde la clave de cada item es la etiqueta EAGLES y el dato es
        # una lista de strings que indican la fuente de la que se ha sacado (para poder posteriormente hacer
        # un estudio más profundo, consultando sus datos del lemario), donde hay tres valores separados por |:
        # "rae" o "wik" para la fuente, número de entrada, número de acepción.
        # La entrada de ejemplo del lexicón para la forma u'vista' es la siguiente:
        '''
        lexicon[u'vista'] = {u'veer': {u'VMP00SF0000000PD': [u'rae|0|0.1'],
                                       u'VMP00SF00000T00D': [u'rae|0|0']},
                             u'ver': {u'VMP00SF00000I000': [u'rae|0|0.1', u'rae|0|15'],
                                      u'VMP00SF00000T000': [u'rae|0|0', u'rae|0|1', u'rae|0|2', u'rae|0|3', u'rae|0|4',
                                                            u'rae|0|5', u'rae|0|6', u'rae|0|7', u'rae|0|8', u'rae|0|9',
                                                            u'rae|0|10', u'rae|0|11', u'rae|0|12', u'rae|0|13',
                                                            u'rae|0|14'],
                                      u'VMP00SF0000000P0': [u'rae|0|16', u'rae|0|17', u'rae|0|18', u'rae|0|19',
                                                            u'rae|0|20', u'rae|0|21']},
                             u'vestir': {u'VMSP3S00000000P0': [u'rae|0|0.1'],
                                         u'VMSP1S000000T000': [u'rae|0|0', u'rae|0|1', u'rae|0|2', u'rae|0|3',
                                                               u'rae|0|4', u'rae|0|5', u'rae|0|6', u'rae|0|7',
                                                               u'rae|0|8'],
                                         u'VMMP3S000000I000': [u'rae|0|9', u'rae|0|10', u'rae|0|11'],
                                         u'VMMP3S000000T000': [u'rae|0|0', u'rae|0|1', u'rae|0|2', u'rae|0|3',
                                                               u'rae|0|4', u'rae|0|5', u'rae|0|6', u'rae|0|7',
                                                               u'rae|0|8'],
                                         u'VMSP1S000000I000': [u'rae|0|9', u'rae|0|10', u'rae|0|11'],
                                         u'VMSP1S00000000P0': [u'rae|0|0.1'],
                                         u'VMSP3S000000I000': [u'rae|0|9', u'rae|0|10',
                                                               u'rae|0|11'],
                                         u'VMSP3S000000T000': [u'rae|0|0', u'rae|0|1', u'rae|0|2', u'rae|0|3',
                                                               u'rae|0|4', u'rae|0|5', u'rae|0|6', u'rae|0|7',
                                                               u'rae|0|8'],
                                         u'VMSP3S00000000PP': [u'rae|0|12'],
                                         u'VMMP3S00000000P0': [u'rae|0|0.1'],
                                         u'VMMP3S00000000PP': [u'rae|0|12'],
                                         u'VMSP1S00000000PP': [u'rae|0|12']},
                             u'vista': {u'NCFS0000D': [u'rae|0|12'],
                                        u'NCMS00000': [u'rae|0|17'],
                                        u'NCFS00000': [u'rae|0|0', u'rae|0|1', u'rae|0|2', u'rae|0|3', u'rae|0|4',
                                                       u'rae|0|5', u'rae|0|6', u'rae|0|7', u'rae|0|8', u'rae|0|9',
                                                       u'rae|0|10', u'rae|0|11']},
                             u'visto': {u'AQ0FS000': [u'rae|0|0', u'rae|0|1']}}
        '''
        n_lemas_procesados = 0
        # lemario = {u'este': lemario[u'este']}
        formas_mas_largas = [u'']
        lemas_con_mas_formas = [(u'', 0)]
        for lema_txt, lema in sorted(lemario.items()):
            if lema_txt == u'uno, na':
                print(u'¿lema rae o lema?')
            if n_lemas_procesados % 1000 == 0 and n_lemas_procesados:
                print(n_lemas_procesados, u'lemas procesados.')
            n_lemas_procesados += 1
            if n_lemas_procesados < 0:
                continue
            if False and lema_txt not in u'aun'.split():
                continue

            if len(lema_txt.split()) > 1:
                # El lema contiene varias palabras. No lo procesamos de momento
                # TODO: a ver qué se hace con las locuciones que son entradas de la RAE (muchas son latinas)
                continue

            formas_flexionadas = Flexionador.flexiona_lema_rae(lema, ajusta_lema=True,
                                                               incluye_cliticos=incluye_cliticos)
            if len(formas_flexionadas) >= lemas_con_mas_formas[0][1]:
                if len(formas_flexionadas) > lemas_con_mas_formas[0][1]:
                    lemas_con_mas_formas = []
                lemas_con_mas_formas.append((lema_txt, len(formas_flexionadas)))
            for etiqueta, formas in formas_flexionadas.items():
                for forma_txt, fuentes in formas.items():
                    if len(forma_txt) >= len(formas_mas_largas[0]):
                        # print(u'Nueva forma igual o más larga:', forma_txt)
                        if len(forma_txt) == len(formas_mas_largas[0]):
                            formas_mas_largas += [forma_txt]
                        else:
                            formas_mas_largas = [forma_txt]

                    if forma_txt not in lexicon:
                        lexicon[forma_txt] = {lema_txt: {etiqueta: fuentes}}
                    elif lema_txt not in lexicon[forma_txt]:
                        lexicon[forma_txt][lema_txt] = {etiqueta: fuentes}
                    elif etiqueta not in lexicon[forma_txt][lema_txt]:
                        lexicon[forma_txt][lema_txt][etiqueta] = fuentes
                    else:
                        lexicon[forma_txt][lema_txt][etiqueta] += fuentes

        print(n_lemas_procesados, u'lemas procesados.')
        print(u'FORMAS CON MAYOR LONGITUD:', u', '.join(formas_mas_largas))
        print(u'LEMAS CON MAYOR NÚMERO DE FORMAS (' + str(lemas_con_mas_formas[0][1]) + u'):',
            u', '.join([l for l, c in lemas_con_mas_formas]))
        if incluye_categorias:
            print(u'COMO ESTAMOS TESTEANDO, NO GUARDAMOS NADA')
            return lexicon

        directorio_trabajo = dirname(os.path.realpath(__file__)) + u'/archivos_de_datos/rae/lexicon/'
        if not os.path.exists(directorio_trabajo):
            os.makedirs(directorio_trabajo)
        nombre_archivo_lexicon = directorio_trabajo + u'lexicon_rae.pickle'
        print(u'Guardando lexicón en', u'.../' + u'/'.join(nombre_archivo_lexicon.split(u'/')[-5:]))
        with open(nombre_archivo_lexicon, 'wb') as archivo_lexicon:
            # ujson.dump(lexicon, archivo_lexicon, ensure_ascii=False, escape_forward_slashes=False)
            pickle.dump(lexicon, archivo_lexicon, pickle.HIGHEST_PROTOCOL)
        # Vamos a crear una versión del lexicón que incluya la parte de FreeLing
        lexicon_freeling = ParseadorRae.carga_lexicon_freeling()
        lexicon.update(lexicon_freeling)
        nombre_archivo_lexicon_ampliado = directorio_trabajo + u'lexicon_rae+fre.pickle'
        print(u'Guardando lexicón ampliado en', u'.../' +\
                                                u'/'.join(nombre_archivo_lexicon_ampliado.split(u'/')[-5:]))
        with open(nombre_archivo_lexicon_ampliado, 'wb') as archivo_lexicon:
            # ujson.dump(lexicon, archivo_lexicon, ensure_ascii=False, escape_forward_slashes=False)
            pickle.dump(lexicon, archivo_lexicon, pickle.HIGHEST_PROTOCOL)
        if subdivide_lexicon:
            ParseadorRae.subdivide_lexicon(lexicon_ampliado=False)
            ParseadorRae.subdivide_lexicon(lexicon_ampliado=True)
        if crea_lexicon_sql:
            ParseadorRae.crea_lexicon_sql()

    @staticmethod
    def subdivide_lexicon(lexicon_ampliado=False):
        u"""Se toma el lexicón completo y se subdivide en partes según su categoría.
        """
        print(u'\nSubdividiendo el lexicón...')
        lexicon_subdividido = {}
        directorio_trabajo = dirname(os.path.realpath(__file__)) + u'/archivos_de_datos/rae/lexicon/'
        nombre_archivo_lexicon =\
            directorio_trabajo + u'lexicon_rae' + (u'+fre' if lexicon_ampliado else u'') + u'.pickle'
        if not os.path.exists(nombre_archivo_lexicon):
            print(u'Falta el archivo', nombre_archivo_lexicon + u'. Es necesario crear el lexicón.')
            return

        print(u'Cargando archivo', u'.../' + u'/'.join(nombre_archivo_lexicon.split(u'/')[-3:]), end=u' ')
        with open(nombre_archivo_lexicon, 'rb') as entrada:
            lexicon = pickle.load(entrada)
        print(u'cargado')

        n_etiquetas_total = 0
        recuento_por_categorias = {}
        print(u'El lexicón contiene', len(lexicon), u'formas.')
        n_formas_procesadas = 0
        for forma_txt, datos_forma in sorted(lexicon.items()):
            if not n_formas_procesadas % 100000 and n_formas_procesadas:
                print(n_formas_procesadas, u'formas procesadas')
            n_formas_procesadas += 1
            if re.sub(u'[a-zñáéíóúü\-‒́]', u'', forma_txt, flags=re.IGNORECASE):
                # print(u'Forma extraña:', forma_txt)
                pass
            for lema_txt, etiquetas_fuentes in sorted(datos_forma.items()):
                for etiqueta_eagles, fuentes in sorted(etiquetas_fuentes.items()):
                    n_etiquetas_total += 1
                    categoria = etiqueta_eagles[0]
                    if categoria == VERBO:
                        # Los verbos modales, copulativos y auxiliares se ponen cada uno en su sublexicón
                        categoria = etiqueta_eagles[:2]
                    # Añadimos al lexicón subdividido
                    if categoria not in lexicon_subdividido:
                        lexicon_subdividido[categoria] = {}
                        recuento_por_categorias[categoria] = {"n_etiquetas": 0}
                    recuento_por_categorias[categoria]["n_etiquetas"] += 1
                    if forma_txt not in lexicon_subdividido[categoria]:
                        lexicon_subdividido[categoria][forma_txt] = {}
                    if lema_txt not in lexicon_subdividido[categoria][forma_txt]:
                        lexicon_subdividido[categoria][forma_txt][lema_txt] = {}
                    lexicon_subdividido[categoria][forma_txt][lema_txt][etiqueta_eagles] = fuentes
        print(len(lexicon), u'formas procesadas\n')
        print(u'RECUENTO de contenido total del lexicón RAE:')
        print(u'- Nº de formas:', len(lexicon))
        print(u'- Nº de etiquetas totales:', n_etiquetas_total)
        print(u'\nRECUENTO por categoría:')
        for categoria, recuentos in sorted(recuento_por_categorias.items(),
                                           key=lambda tupla: -len(lexicon_subdividido[tupla[0]])):
            categoria_txt = CATEGORIAS_A_TXT[categoria[0]] +\
                (u'' if len(categoria) == 1 else (u' ' + TIPOS_VERBO_A_TXT[categoria[1]].lower()))
            ejemplos = sorted(lexicon_subdividido[categoria].keys())[0::int(len(lexicon_subdividido[categoria].keys())/4.1)]
            print(u'-', categoria_txt + u':', u', '.join(ejemplos) + u'...')
            print(u'  - Nº de formas:', len(lexicon_subdividido[categoria]))
            print(u'  - Nº de etiquetas:', recuento_por_categorias[categoria]["n_etiquetas"])
            nombre_archivo_sublexicon = directorio_trabajo + u'sublexicon_rae' +\
                (u'+fre' if lexicon_ampliado else u'') + u'-' +\
                categoria_txt.lower().replace(u' ', u'-') + u'.pickle'
            print(u'Guardando', u'.../' + u'/'.join(nombre_archivo_sublexicon.split(u'/')[-3:]) + u'\n')
            with open(nombre_archivo_sublexicon, 'wb') as archivo_lexicon:
                # ujson.dump(lexicon_subdividido[categoria], archivo_lexicon, ensure_ascii=False, escape_forward_slashes=False)
                pickle.dump(lexicon_subdividido[categoria], archivo_lexicon, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def crea_lexicon_sql():
        # En crea_lexicon se ve la estructura del lexicón. Vamos a trasladarlo a una tabla SQL.
        lexicon = ParseadorRae.carga_lexicon()
        forma_mas_larga = max([len(forma) for forma in lexicon.keys()])
        print(u'Forma más larga:', forma_mas_larga,
            u'caracteres (' + u', '.join([forma for forma in lexicon.keys() if len(forma) == forma_mas_larga]) + u').')
        lemas = sorted(list(set([lema for forma, datos_forma in lexicon.items() for lema in datos_forma.keys()])),
                       key=lambda x: -len(x))
        lema_mas_largo = len(lemas[0])
        print(u'Lema más largo:', len(lemas[0]),
              u'caracteres (' + u', '.join([lema for lema in lemas
                                            if len(lema) == len(lemas[0])]) + u').')
        filas_sql = [(forma, lema, etiqueta, fuentes)
                     for forma, datos_forma in lexicon.items()
                     for lema, datos_lema in datos_forma.items()
                     for etiqueta, fuentes in datos_lema.items()]
        lexicon = {}  # Liberar memoria

        print(u'Insertando', len(filas_sql), u'filas en la tabla "lexicon"...')
        hora_inicio = time()
        conn = psycopg2.connect(host="localhost", user="postgres", password="superusuario")
        cur = conn.cursor()
        cur.execute(u'DROP TABLE IF EXISTS lexicon')
        cur.execute(u'CREATE TABLE lexicon ('
                    u'forma VARCHAR(%s), '
                    u'lema VARCHAR(%s), '
                    u'etiqueta VARCHAR(16), '
                    u'fuentes VARCHAR(10)[],'
                    u'PRIMARY KEY (forma, lema, etiqueta))',
                    (forma_mas_larga, lema_mas_largo))

        for orden_fila in range(len(filas_sql)):
            (forma, lema, etiqueta, fuentes) = filas_sql[orden_fila % 1000000]
            cur.execute(u'INSERT INTO lexicon(forma, lema, etiqueta, fuentes) VALUES (%s, %s, %s, %s)',
                        (forma, lema, etiqueta, u'{' + u', '.join(fuentes) + u'}'))
            if orden_fila % 10000 == 9999:
                conn.commit()
                sys.stdout.write(u'.')
                if orden_fila % 1000000 == 999999:
                    print(u' ', orden_fila + 1)
                    filas_sql = filas_sql[1000000:]

        print(u' ', orden_fila + 1)
        filas_sql = []  # Liberar memoria
        conn.commit()
        cur.close()
        conn.close()
        tiempo_total = int(time() - hora_inicio)
        print(orden_fila + 1, u'filas insertadas en la tabla en {:2d}:{:02d}'. \
            format((tiempo_total / 60) % 60, tiempo_total % 60))
        pass

    @staticmethod
    def crea_lexicon_basico():
        # El lexicón básico está simplificado, ya que no es un diccionario con las formas como claves, que
        # tiene como elementos diccionarios con lemas como claves, que tienen como elementos diccionarios con
        # etiquetas como claves, que tiene como elementos listas de strings tipo "rae|0|2.1" con la
        # información sobre la entrada y la acepción del lema que da como resultado la forma.
        # En el lexicón básico el último diccionario se cambia por una lista de etiquetas, sin información de
        # las acepciones de la RAE.
        for lexicon_ampliado in (False, True):
            lexicon = ParseadorRae.carga_lexicon(lexicon_ampliado=lexicon_ampliado)
            lexicon_basico = {}
            for forma in lexicon.keys():
                lexicon_basico[forma] = {}
                for lema in lexicon[forma]:
                    lexicon_basico[forma][lema] =\
                        [etiqueta for etiqueta, datos in sorted(lexicon[forma][lema].items(),
                                                                key=lambda x: x[1][0])]
            directorio_trabajo = dirname(os.path.realpath(__file__)) + u'/archivos_de_datos/rae/lexicon/'
            nombre_archivo_lexicon = directorio_trabajo + u'lexicon_rae' +\
                (u'+fre' if lexicon_ampliado else u'') + u'.basico.msgpack.bz2'
            print(u'Guardando lexicón básico en', u'.../' + u'/'.join(nombre_archivo_lexicon.split(u'/')[-5:]), end=u' ')
            # with open(nombre_archivo_lexicon, 'wb') as archivo_lexicon:
            with bz2.BZ2File(nombre_archivo_lexicon, 'wb') as archivo_lexicon:
                # ujson.dump(lexicon_basico, archivo_lexicon, ensure_ascii=False, escape_forward_slashes=False)
                # pickle.dump(lexicon_basico, archivo_lexicon, pickle.HIGHEST_PROTOCOL)
                msgpack.pack(lexicon_basico, archivo_lexicon)
            print(u'guardado.')

    @staticmethod
    def crea_lexicon_conjunto_rae_wik():
        lexicon_wik = ParseadorWikcionario.carga_lexicon()
        lexicon_rae = ParseadorRae.carga_lexicon()
        categoria_a_txt = {SUSTANTIVO: u'Sustantivo', ADJETIVO: u'Adjetivo', DETERMINANTE: u'Determinante',
                           PRONOMBRE: u'Pronombre', VERBO: u'Verbo', ADVERBIO: u'Adverbio',
                           PREPOSICION: u'Preposición', CONJUNCION: u'Conjunción',
                           INTERJECCION: u'Interjección',
                           EXPRESION: u'Expresión', ONOMATOPEYA: u'Onomatopeya', AFIJO: u'Afijo',
                           PREFIJO: u'Prefijo', SUFIJO: u'Sufijo',
                           ABREVIATURA: u'Abreviatura', SIGLA: u'Sigla',
                           SIMBOLO: u'Símbolo', DESCONOCIDA: u'Desconocida', SIGNO: u'Puntuación'}
        # Al lexicón del wikcionario se le ponen etiquetas distintas, sobre todo porque suele falta lo de
        # usado o no.
        etiquetas_distintas_wik = set([etiqueta
                                       for forma, datos in lexicon_wik.items()
                                       for lema, etiquetas in datos.items()
                                       for etiqueta, fuentes in etiquetas.items()])
        etiquetas_agrupadas_wik = {}
        for etiqueta in etiquetas_distintas_wik:
            categoria = categoria_a_txt[etiqueta[0]]
            if categoria not in etiquetas_agrupadas_wik:
                etiquetas_agrupadas_wik[categoria] = set()
            etiquetas_agrupadas_wik[categoria].add(etiqueta)
        longitudes_etiquetas_wik =\
            {categoria: set(len(etiqueta)
                            for etiqueta in etiquetas_agrupadas_wik[categoria])
             for categoria in etiquetas_agrupadas_wik}
        print(longitudes_etiquetas_wik)

        etiquetas_distintas_rae = set([etiqueta
                                       for forma, datos in lexicon_rae.items()
                                       for lema, etiquetas in datos.items()
                                       for etiqueta, fuentes in etiquetas.items()])
        etiquetas_agrupadas_rae = {}
        for etiqueta in etiquetas_distintas_rae:
            categoria = categoria_a_txt[etiqueta[0]]
            if categoria not in etiquetas_agrupadas_rae:
                etiquetas_agrupadas_rae[categoria] = set()
            etiquetas_agrupadas_rae[categoria].add(etiqueta)
        longitudes_etiquetas_rae =\
            {categoria: set(len(etiqueta)
                            for etiqueta in etiquetas_agrupadas_rae[categoria])
             for categoria in etiquetas_agrupadas_rae}

        etiquetas_distintas_mix = etiquetas_distintas_wik | etiquetas_distintas_rae
        etiquetas_agrupadas_mix = {}
        for etiqueta in etiquetas_distintas_mix:
            categoria = categoria_a_txt[etiqueta[0]]
            if categoria not in etiquetas_agrupadas_mix:
                etiquetas_agrupadas_mix[categoria] = set()
            etiquetas_agrupadas_mix[categoria].add(etiqueta)
        longitudes_etiquetas_mix =\
            {categoria: set(len(etiqueta)
                            for etiqueta in etiquetas_agrupadas_mix[categoria])
             for categoria in etiquetas_agrupadas_mix}

        etiquetas_distintas_wik_normalizada =\
            set([(etiqueta +
                  u'0' * (list(longitudes_etiquetas_rae[categoria_a_txt[etiqueta[0]]])[0] - len(etiqueta)))
                 if categoria_a_txt[etiqueta[0]] in longitudes_etiquetas_rae else etiqueta
                 for etiqueta in etiquetas_distintas_wik])
        etiquetas_agrupadas_wik_normalizada = {}
        for etiqueta in etiquetas_distintas_wik_normalizada:
            categoria = categoria_a_txt[etiqueta[0]]
            if categoria not in etiquetas_agrupadas_wik_normalizada:
                etiquetas_agrupadas_wik_normalizada[categoria] = set()
            etiquetas_agrupadas_wik_normalizada[categoria].add(etiqueta)
        longitudes_etiquetas_mix_normalizada =\
            {categoria: set(len(etiqueta)
                            for etiqueta in etiquetas_agrupadas_wik_normalizada[categoria])
             for categoria in etiquetas_agrupadas_wik_normalizada}


        etiquetas_distintas_mix_normalizada = etiquetas_distintas_wik_normalizada | etiquetas_distintas_rae
        etiquetas_agrupadas_mix_normalizada = {}
        for etiqueta in etiquetas_distintas_mix_normalizada:
            categoria = categoria_a_txt[etiqueta[0]]
            if categoria not in etiquetas_agrupadas_mix_normalizada:
                etiquetas_agrupadas_mix_normalizada[categoria] = set()
            etiquetas_agrupadas_mix_normalizada[categoria].add(etiqueta)
        longitudes_etiquetas_mix_normalizada =\
            {categoria: set(len(etiqueta)
                            for etiqueta in etiquetas_agrupadas_mix_normalizada[categoria])
             for categoria in etiquetas_agrupadas_mix_normalizada}

        # Normalizamos el lexicón del Wikcionario
        for forma in list(lexicon_wik.keys()):
            datos = lexicon_wik[forma]
            for lema in datos.keys():
                etiquetas = datos[lema]
                etiquetas_normalizadas = {}
                for etiqueta in etiquetas.keys():
                    fuentes = etiquetas[etiqueta]
                    relleno = u''
                    if categoria_a_txt[etiqueta[0]] in longitudes_etiquetas_rae:
                        longitud_etiqueta = list(longitudes_etiquetas_rae[categoria_a_txt[etiqueta[0]]])[0]
                        relleno = u'0' * (longitud_etiqueta - len(etiqueta))
                    etiquetas_normalizadas[etiqueta + relleno] = fuentes
                lexicon_wik[forma][lema] = etiquetas_normalizadas
                pass
        etiquetas_distintas_wik = set([etiqueta
                                       for forma, datos in lexicon_wik.items()
                                       for lema, etiquetas in datos.items()
                                       for etiqueta, fuentes in etiquetas.items()])
        etiquetas_agrupadas_wik = {}
        for etiqueta in etiquetas_distintas_wik:
            categoria = categoria_a_txt[etiqueta[0]]
            if categoria not in etiquetas_agrupadas_wik:
                etiquetas_agrupadas_wik[categoria] = set()
            etiquetas_agrupadas_wik[categoria].add(etiqueta)
        longitudes_etiquetas_wik =\
            {categoria: set(len(etiqueta)
                            for etiqueta in etiquetas_agrupadas_wik[categoria])
             for categoria in etiquetas_agrupadas_wik}
        print(longitudes_etiquetas_wik)





        lexicon_mix = copy.deepcopy(lexicon_rae)


        if False:
            for forma_wik, datos_wik in lexicon_wik.items():
                if forma_wik not in lexicon_mix:
                    lexicon_mix[forma_wik] = datos_wik
                else:
                    datos_mix = lexicon_mix[forma_wik]
                    for lema_wik, datos_etiquetas_wik in datos_wik.items():
                        if lema_wik not in datos_mix:
                            datos_mix[lema_wik] = datos_etiquetas_wik
                        else:
                            categorias_rae = [etiqueta[0] for etiqueta, fuentes in datos_mix[lema_wik].items()]
                            for etiqueta_wik, fuentes_wik in datos_etiquetas_wik.items():
                                if etiqueta_wik[0] not in categorias_rae:
                                    datos_mix[lema_wik][etiqueta_wik] = fuentes_wik

        for forma_wik, datos_wik in lexicon_wik.items():
            if forma_wik not in lexicon_mix:
                lexicon_mix[forma_wik] = datos_wik
            else:
                datos_mix = lexicon_mix[forma_wik]
                for lema_wik, datos_etiquetas_wik in datos_wik.items():
                    if lema_wik not in datos_mix:
                        datos_mix[lema_wik] = datos_etiquetas_wik
                    else:
                        categorias_rae = [etiqueta[0] for etiqueta, fuentes in datos_mix[lema_wik].items()]
                        for etiqueta_wik, fuentes_wik in datos_etiquetas_wik.items():
                            if etiqueta_wik[0] not in categorias_rae:
                                datos_mix[lema_wik][etiqueta_wik] = fuentes_wik

        for nombre, lexicon in [(u'LEXICÓN WIKCIONARIO:', lexicon_wik),
                                (u'LEXICÓN RAE:', lexicon_rae),
                                (u'LEXICÓN MIXTO:', lexicon_mix)]:
            print(u'\n\n' + nombre)
            n_etiquetas = sum([len(etiquetas)
                               for forma, datos in lexicon.items()
                               for lema, etiquetas in datos.items()])
            print(u'El lexicón contiene', len(lexicon), u'formas, con', n_etiquetas, u'etiquetas.')
            recuentos_formas = {}
            recuentos_lemcats = {}
            recuento_nombres_propios = {"lemas": set(), "formas-etiquetas": set(), "formas": set()}
            recuento_adverbios_mente = {"lemas": set(), "formas-etiquetas": set(), "formas": set(),
                                        "adjetivales": set()}
            adverbios = {}
            for forma, datos in lexicon.items():
                categorias = set()
                for lema, etiquetas in datos.items():
                    for etiqueta, fuentes in etiquetas.items():
                        categoria = etiqueta[0] if etiqueta[0] != AFIJO else etiqueta[1]
                        categorias.add(categoria)
                        if categoria not in recuentos_formas:
                            recuentos_formas[categoria] = \
                                {"etiquetas_distintas": set(), "n_formas": 0, "n_etiquetas": 0}
                        recuentos_formas[categoria]["etiquetas_distintas"].add(etiqueta)
                        recuentos_formas[categoria]["n_etiquetas"] += 1
                        if categoria not in recuentos_lemcats:
                            recuentos_lemcats[categoria] = set()
                        recuentos_lemcats[categoria].add(lema + u'-' + categoria)
                        if categoria == SUSTANTIVO and etiqueta[1] == PROPIO:
                            recuento_nombres_propios["lemas"].add(lema)
                            recuento_nombres_propios["formas-etiquetas"].add(forma + etiqueta)
                            recuento_nombres_propios["formas"].add(forma)
                        elif categoria == ADVERBIO:
                            if forma not in adverbios:
                                adverbios[forma] = {}
                            if lema not in adverbios[forma]:
                                adverbios[forma][lema] = {}
                            adverbios[forma][lema][etiqueta] = fuentes
                            if forma[-5:] == u'mente':
                                if lema[-5:] == u'mente':
                                    recuento_adverbios_mente["lemas"].add(lema)
                                recuento_adverbios_mente["formas-etiquetas"].add(forma + etiqueta)
                                recuento_adverbios_mente["formas"].add(forma)
                                if lema[:-5] in lexicon:
                                    recuento_adverbios_mente["adjetivales"].add(forma)

                for categoria in set(categorias):
                    recuentos_formas[categoria]["n_formas"] += 1
            print(u'Recuentos por categoría:')
            for (categoria, datos) in sorted(recuentos_formas.items(),
                                             key=lambda tupla: -tupla[1]["n_etiquetas"]):
                print(categoria_a_txt[categoria] + u':')
                print(u'  - Nº de formas-etiquetas:', datos["n_etiquetas"])
                print(u'  - Nº de formas distintas:', datos["n_formas"])
                print(u'  - Nº de etiquetas distintas:', len(datos["etiquetas_distintas"]))
                print(u'  - Nº de lemcats:', len(recuentos_lemcats[categoria]))
                if categoria == SUSTANTIVO:
                    print(u'  - Nº de lemas de nombre común:',
                          len(recuentos_lemcats[categoria]) - len(recuento_nombres_propios["lemas"]))
                    print(u'  - Nº de lemas de nombre propio:', len(recuento_nombres_propios["lemas"]))
                    print(u'  - Nº de formas-etiquetas de nombre común:',
                          datos["n_etiquetas"] - len(recuento_nombres_propios["formas"]))
                    print(u'  - Nº de formas-etiquetas de nombre propio:',
                          len(recuento_nombres_propios["formas-etiquetas"]))
                    print(u'  - Nº de formas distintas de nombre común:',
                          datos["n_formas"] - len(recuento_nombres_propios["formas"]))
                    print(u'  - Nº de formas distintas de nombre propio:',
                          len(recuento_nombres_propios["formas"]))
                elif categoria == ADVERBIO:
                    print(u'\n  - Nº de lemas:',
                          len(set([lema
                                   for forma, datos in adverbios.items()
                                   for lema, etiquetas in datos.items()])))
                    print(u'  - Nº de lemas que acaban en -mente:',
                          len(set([lema
                                   for forma, datos in adverbios.items()
                                   for lema, etiquetas in datos.items()
                                   if lema[-5:] == u'mente'])))
                    print(u'  - Nº de lemas que no acaban en -mente:',
                          len(set([lema
                                   for forma, datos in adverbios.items()
                                   for lema, etiquetas in datos.items()
                                   if lema[-5:] != u'mente'])))
                    print(u'  - Nº de lemas que no acaban en -mente y son iguales a la forma (lemas de adverbios "de verdad"):',
                          len(set([lema
                                   for forma, datos in adverbios.items()
                                   for lema, etiquetas in datos.items()
                                   if lema[-5:] != u'mente' and lema == forma])))
                    print(u'  - Nº de lemas que no acaban en -mente y son distintos a la forma (lemas de adverbios deadjetivales):',
                          len(set([lema
                                   for forma, datos in adverbios.items()
                                   for lema, etiquetas in datos.items()
                                   if lema[-5:] != u'mente' and lema not in adverbios])))
                    print(u'  - Nº de formas-etiqueta:',
                          len(set([forma + etiqueta
                                   for forma, datos in adverbios.items()
                                   for lema, etiquetas in datos.items()
                                   for etiqueta, fuentes in etiquetas.items()])))
                    print(u'  - Nº de formas-etiqueta con un único lema:',
                          len(set([forma + etiqueta
                                   for forma, datos in adverbios.items()
                                   if len(datos) == 1])))
                    print(u'  - Nº de formas-etiqueta con dos lemas:',
                          len(set([forma + etiqueta
                                   for forma, datos in adverbios.items()
                                   for lema, etiquetas in datos.items()
                                   for etiqueta, fuentes in etiquetas.items()
                                   if len(datos) == 2])))
                    print(u'  - Nº de formas-etiqueta con tres lemas:',
                          len(set([forma + etiqueta
                                   for forma, datos in adverbios.items()
                                   for lema, etiquetas in datos.items()
                                   for etiqueta, fuentes in etiquetas.items()
                                   if len(datos) == 3])))
                    print(u'  - Nº de formas-etiqueta con cuatro lemas:',
                          len(set([forma + etiqueta
                                   for forma, datos in adverbios.items()
                                   for lema, etiquetas in datos.items()
                                   for etiqueta, fuentes in etiquetas.items()
                                   if len(datos) == 4])))
                    print(u'  - Nº de formas-etiqueta cuyo lema acaba en -mente:',
                          len(set([forma + etiqueta
                                   for forma, datos in adverbios.items()
                                   for lema, etiquetas in datos.items()
                                   for etiqueta, fuentes in etiquetas.items()
                                   if lema[-5:] == u'mente'])))
                    print(u'  - Nº de formas-etiqueta cuyo lema no acaba en -mente:',
                          len(set([forma + etiqueta
                                   for forma, datos in adverbios.items()
                                   for lema, etiquetas in datos.items()
                                   for etiqueta, fuentes in etiquetas.items()
                                   if lema[-5:] != u'mente'])))
                    print(u'  - Nº de formas-etiqueta cuyo lema no acaba en -mente y es igual a la forma:',
                          len(set([forma + etiqueta
                                   for forma, datos in adverbios.items()
                                   for lema, etiquetas in datos.items()
                                   for etiqueta, fuentes in etiquetas.items()
                                   if lema[-5:] != u'mente' and lema == forma])))
                    print(u'  - Nº de formas-etiqueta cuyo lema no acaba en -mente y es distinta a la forma:',
                          len(set([forma + etiqueta
                                   for forma, datos in adverbios.items()
                                   for lema, etiquetas in datos.items()
                                   for etiqueta, fuentes in etiquetas.items()
                                   if lema[-5:] != u'mente' and lema not in adverbios])))
                    print(u'  - Nº de formas distintas:',
                          len(set([forma
                                   for forma, datos in adverbios.items()
                                   for lema, etiquetas in datos.items()])))
                    print(u'  - Nº de formas distintas cuyo lema acaba en -mente:',
                          len(set([forma
                                   for forma, datos in adverbios.items()
                                   for lema, etiquetas in datos.items()
                                   if lema[-5:] == u'mente'])))
                    print(u'  - Nº de formas distintas cuyo lema no acaba en -mente:',
                          len(set([forma
                                   for forma, datos in adverbios.items()
                                   for lema, etiquetas in datos.items()
                                   if lema[-5:] != u'mente'])))
                    print(u'  - Nº de formas distintas cuyo lema no acaba en -mente y es igual a la forma:',
                          len(set([forma
                                   for forma, datos in adverbios.items()
                                   for lema, etiquetas in datos.items()
                                   if lema[-5:] != u'mente' and lema == forma])))
                    print(u'  - Nº de formas distintas cuyo lema no acaba en -mente y es distinta a la forma:',
                          len(set([forma
                                   for forma, datos in adverbios.items()
                                   for lema, etiquetas in datos.items()
                                   if lema[-5:] != u'mente' and lema not in adverbios])))
                    print(u'  - Nº de lemas que acaban en -mente que derivan de un adjetivo que no está en el lexicón:',
                          len(set([lema
                                   for forma, datos in adverbios.items()
                                   for lema, etiquetas in datos.items()
                                   if lema[-5:] == u'mente' and lema[:-5] not in lexicon])))
                    print(u'  - Nº de lemas que acaban en -mente que derivan de un adjetivo que está en el lexicón:',
                          len(set([lema
                                   for forma, datos in adverbios.items()
                                   for lema, etiquetas in datos.items()
                                   if lema[-5:] == u'mente' and lema[:-5] in lexicon])))




                    print(u'  - Nº de lemas de adverbio no -mente:',
                          len(recuentos_lemcats[categoria]) - len(recuento_adverbios_mente["lemas"]))
                    print(u'  - Nº de lemas de adverbio -mente:', len(recuento_adverbios_mente["lemas"]))
                    print(u'  - Nº de lemas adjetivos:',
                          len(recuento_adverbios_mente["adjetivales"]))
                    print(u'  - Nº de formas-etiquetas de adverbio no -mente:',
                          datos["n_etiquetas"] - len(recuento_adverbios_mente["formas"]))
                    print(u'  - Nº de formas-etiquetas de adverbio -mente:',
                          len(recuento_adverbios_mente["formas-etiquetas"]))
                    print(u'  - Nº de formas distintas de adverbio no -mente:',
                          datos["n_formas"] - len(recuento_adverbios_mente["formas"]))
                    print(u'  - Nº de formas distintas de adverbio -mente:',
                          len(recuento_adverbios_mente["formas"]))

            n_formas_etiquetas_total = len(set([forma + etiqueta for forma, datos in lexicon.items()
                                                            for lema, etiquetas in datos.items()
                                                            for etiqueta, fuentes in etiquetas.items()]))
            n_formas_distintas_total = len(lexicon)
            n_etiquetas_distintas_total = len(set([etiqueta for forma, datos in lexicon.items()
                                                   for lema, etiquetas in datos.items()
                                                   for etiqueta, fuentes in etiquetas.items()]))
            n_lemas_total = len(set([lema + etiqueta[0] for forma, datos in lexicon.items()
                                     for lema, etiquetas in datos.items()
                                     for etiqueta, fuentes in etiquetas.items()]))
            n_lemas_distintos = len(set([lema for forma, datos in lexicon.items()
                                         for lema, etiquetas in datos.items()]))

            print(u'\nTOTALES:')
            print(u'  - Nº de formas-etiquetas:', n_formas_etiquetas_total)
            print(u'  - Nº de formas distintas:', n_formas_distintas_total)
            print(u'  - Nº de etiquetas distintas:', n_etiquetas_distintas_total)
            print(u'  - Nº de lemcats:', n_lemas_total)
            print(u'  - Nº de lemas distintos:', n_lemas_distintos)

        return lexicon_mix

    @staticmethod
    def carga_lexicon_basico(lexicon_ampliado=False):
        directorio_trabajo = dirname(os.path.realpath(__file__)) + u'/archivos_de_datos/rae/lexicon/'
        nombre_archivo_lexicon = directorio_trabajo + u'lexicon_rae' + \
            (u'+fre' if lexicon_ampliado else u'') + u'.basico.msgpack.bz2'
        print(u'Cargando lexicón básico de', u'.../' + u'/'.join(nombre_archivo_lexicon.split(u'/')[-5:]), end=u' ')
        hora_inicio = time()
        with bz2.BZ2File(nombre_archivo_lexicon, 'rb') as archivo_lexicon:
            lexicon = msgpack.unpack(archivo_lexicon, use_list=False, encoding="utf-8")
        tiempo_total = int(time() - hora_inicio)
        print(u'Cargadas', len(lexicon), u'formas en {:d}:{:02d}.'. \
            format((tiempo_total / 60) % 60, tiempo_total % 60))
        return lexicon

    @staticmethod
    def carga_lexicon(incluye_categorias=None, excluye_categorias=None, lexicon_ampliado=False, verboso=True,
                      guarda_para_27=False):
        u"""

        :param incluye_categorias:
        :param excluye_categorias:
        :return:
        """
        hora_inicio = time()
        # print(u'Cargando lexicón...')
        # Sacamos el directorio en el que está ubicado este script.
        directorio_trabajo = dirname(os.path.realpath(__file__)) + u'/archivos_de_datos/rae/lexicon/'
        if incluye_categorias:
            # No partimos del lexicón completo, sino que cargamos solo las formas que provengan de un lema
            # que sea de una de las categorías fijadas por el parámetro
            paths_archivos_lexicon = []
            for categoria in incluye_categorias:
                if len(categoria) == 2 and categoria[0] == VERBO:
                    # Usualmente los verbos copulativos o auxiliares se toman como palabras gramaticales, y se
                    # excluyen o incluyen. De ahí que se hayan creado sublexicones específicos para estos dos casos.
                    # También se tienen sublexicones de verbos modales.
                    path_archivo_lexicon = directorio_trabajo + u'sublexicon_rae' + \
                                           (u'+fre' if lexicon_ampliado else u'') + u'-' + \
                                           CATEGORIAS_A_TXT[categoria[0]].lower() + u'-' + \
                                           TIPOS_VERBO_A_TXT[categoria[1]].lower() + u'.pickle'
                else:
                    path_archivo_lexicon = directorio_trabajo + u'sublexicon_rae' + \
                                           (u'+fre' if lexicon_ampliado else u'') + u'-' + \
                                           CATEGORIAS_A_TXT[categoria[0]].lower() + u'.pickle'
                paths_archivos_lexicon.append(path_archivo_lexicon)
        else:
            # No hay limitación, cargamos el lexicón completo para empezar
            paths_archivos_lexicon = [directorio_trabajo + u'lexicon_rae' +
                                      (u'+fre' if lexicon_ampliado else u'') + u'.pickle']

        # Cargamos (y mergeamos) la lista de sublexicones (quizá solo uno).
        lexicon = {}
        sublexicon = {}
        for orden_archivo, path_archivo_lexicon in enumerate(paths_archivos_lexicon):
            # Cargamos...
            if not os.path.exists(path_archivo_lexicon):
                print(u'Falta el archivo', path_archivo_lexicon + u'. Es necesario crear el lexicón.')
                return {}
            if verboso:
                print(u'Cargando archivo', u'.../' + u'/'.join(path_archivo_lexicon.split(u'/')[-5:]), end=u' ')
            with open(path_archivo_lexicon, 'rb') as entrada:
                sublexicon = pickle.load(entrada)
                if guarda_para_27:
                    with open(path_archivo_lexicon + '27', 'wb') as entrada:
                        pickle.dump(sublexicon, entrada, protocol=2)
                    
            # Y combinamos...
            if not lexicon:
                # Primer archivo que cargamos. Simplemente el lexicón total es esta única (primera) parte.
                lexicon = sublexicon
            else:
                # Tenemos que combinar el sublexicón con el lexicón completo. El (sub)lexicón tiene la estructura:
                # {forma1: {lema1: {tag1: [apariciones], tag2: ...}, lema2: ...}, forma2: ...}
                for forma_txt, datos_forma in sublexicon.items():
                    # La forma es la palabra (tal que u'sobre') y los datos son diccionarios cuya clave es el lema,
                    # y los datos son diccionarios cuya clave es la etiqueta EAGLES. Así que, al combinar con un
                    # sublexicón, puede haber colisión en la forma ("sobre" de "sobrar", o de "sobre" nombre, o de
                    # "sobre" preposición...), e incluso pueden solaparse lemas ("sobre" nombre o preposición), pero
                    # nunca etiquetas.
                    # Así que basta con sacar el diccionario asociado a una forma concreta (cuyas claves son lemas),
                    # y combinarlo directamente con el equivalente del lexicón completo.
                    if forma_txt not in lexicon:
                        lexicon[forma_txt] = datos_forma
                    else:
                        for lema_txt, datos_lema in datos_forma.items():
                            lexicon[forma_txt].setdefault(lema_txt, {}).update(datos_lema)
            sublexicon = {}  # Liberamos memoria.

        # Hasta aquí hemos cargado "la base" del lexicón que se nos pide. Tenemos que ver si se solicita una purga
        # expresa de las formas que puedan pertenecer a ciertas categorías concretas. Por ejemplo, cargo verbos y
        # nombres, pero excluyo preposiciones, con lo que borro las entradas para formas del tipo "sobre", "para",
        # "bajo"... De esta forma evitamos crear un lexicón que lematiza siempre estas preposiciones como verbos,
        # nombres, adjetivos... cuando en realidad en un 99% de las veces serán preposiciones.
        if excluye_categorias:
            for categoria in excluye_categorias:
                if len(categoria) == 2 and categoria[0] == VERBO:
                    # Usualmente los verbos copulativos o auxiliares se toman como palabras gramaticales, y se
                    # excluyen. De ahí que se hayan creado sublexicones específicos para estos dos casos.
                    # También se tienen sublexicones de verbos modales.
                    path_archivo_lexicon = directorio_trabajo + u'sublexicon_rae' + \
                                           (u'+fre' if lexicon_ampliado else u'') + u'-' + \
                                           CATEGORIAS_A_TXT[categoria[0]].lower() + u'-' +\
                                           TIPOS_VERBO_A_TXT[categoria[1]].lower() + u'.pickle'
                else:
                    path_archivo_lexicon = directorio_trabajo + u'sublexicon_rae' + \
                                           (u'+fre' if lexicon_ampliado else u'') + u'-' + \
                                           CATEGORIAS_A_TXT[categoria[0]].lower() + u'.pickle'
                # Cargamos...
                if not os.path.exists(path_archivo_lexicon):
                    print(u'\nFalta el archivo', path_archivo_lexicon + u'. Es necesario crear el lexicón.')
                    return {}
                if verboso:
                    print(u'\nCargando sublexicón', u'.../' +
                          u'/'.join(path_archivo_lexicon.split(u'/')[-5:]))
                with open(path_archivo_lexicon, 'rb') as entrada:
                    sublexicon = pickle.load(entrada)
                    if guarda_para_27:
                        with open(path_archivo_lexicon + '27', 'wb') as entrada:
                            pickle.dump(sublexicon, entrada, protocol=2)
                if len(categoria) > 1 and not (len(categoria) == 2 and categoria[0] == VERBO):
                    # Esto ocurre cuando se pone una categoría y una subcategoría, por ejemplo, para excluir
                    # nombres propios, o cosas del estilo.
                    for forma_txt, datos_lema in sublexicon.items():
                        for lema, datos_etiqueta in datos_lema.items():
                            for etiqueta in datos_etiqueta:
                                if etiqueta[:len(categoria)] == categoria:
                                    lexicon.pop(forma_txt, None)
                else:
                    for forma_txt in sublexicon:
                        lexicon.pop(forma_txt, None)
                sublexicon = {}  # Liberamos memoria
        tiempo_total = int(time() - hora_inicio)
        if verboso:
            print(u'Cargadas', len(lexicon), u'formas en {:d}:{:02d}.'.
                  format(int(tiempo_total / 60) % 60, tiempo_total % 60))
        return lexicon

    @staticmethod
    def lista_ids_faltantes(nombre_archivo_ids=directorio_archivos_rae_web + u'ids_extraídos.txt'):
        """Examina uno a uno los archivos guardados, analiza los enlaces y saca los ids de artículos que no tengamos
        en el directorio.

        :return:
        """
        nombres_archivos_lemas = [f for f in (f for f in listdir(directorio_lemas)
                                              if isfile(directorio_lemas + f))]
        ids_existentes = set([f.split(u'.')[1] for f in nombres_archivos_lemas])
        ids_descubiertos = set()
        n_entradas_procesadas = 0
        n_lemas_iniciales_saltados = 0
        for nombre_archivo_lema in nombres_archivos_lemas:
            if not n_entradas_procesadas % 1000 and n_entradas_procesadas:
                print(n_entradas_procesadas, u'entradas procesadas')
            n_entradas_procesadas += 1
            if n_entradas_procesadas < n_lemas_iniciales_saltados:
                continue
            lema_txt = nombre_archivo_lema.split(u'.')[0] if nombre_archivo_lema.split(u'.')[0] != u'cón' else u'con'

            archivo = codecs.open(directorio_lemas + nombre_archivo_lema, encoding='utf-8')
            texto_lema = archivo.read()
            archivo.close()
            parseador_articulo = ParseadorArticuloRae(lema_txt, extrae_ids=True)
            entrada_rae = parseador_articulo.parsea_entrada(texto_lema)
            ids_en_archivo = entrada_rae["ids"]
            ids_descubiertos |= set(ids_en_archivo)
            pass
        ids_nuevos = [i for i in ids_descubiertos if i not in ids_existentes]
        print(u'Hay', len(ids_nuevos), u'ids nuevos que no teníamos en la lista')
        print(u'\n'.join(ids_nuevos))
        ids_viejos = [i for i in ids_descubiertos if i in ids_existentes]
        print(u'De los', len(ids_existentes), u'ids ya conocidos,', len(ids_viejos), u'aparecen lincados en los archivos existentes')
        # for id_viejo in ids_viejos:
        #    print(id_viejo)

        with codecs.open(nombre_archivo_ids, "a", encoding='utf-8') as archivo_ids:
            archivo_ids.write(u'\n'.join(ids_nuevos))
        return ids_nuevos

    @staticmethod
    def descarga_entradas_lemario(items=None, nombre_archivo_lemas=u'', nombre_archivo_ids=u'',
                                  localizacion_firefox_exe=u'C:/Program Files/Mozilla Firefox/firefox.exe'):

        """Se descargan los archivos de las entradas extraídas de un archivo de texto de lemas o de ids de entradas RAE

        El archivo de texto es una lista, con cada elemento separado del siguiente por un salto de carro. Puede ser
        una lista de palabras, en cuyo caso se buscarán en la RAE esas palabras (se descargan páginas de la forma
        http://dle.rae.es/?w=PALABRA). El listado de palabras es en realidad un listado de "semillas" de palabras,
        puesto que aunque se supone que las palabras incluidas son lemas, en realidad el diccionario de la RAE es
        también un lematizador, con lo que trata la PALABRA como una forma flexionada, y devuelve resultados en función
        de qué lemas pueden producir la PALABRA al flexionarse.

        Por ello, si la PALABRA puede ser una forma de más de un lema (mejor dicho, más de una entrada, aunque sean
        entradas del mismo lema), en vez de la definición de la PALABRA (aunque sea un lema) se devuelve un listado
        con lemas que tienen la PALABRA como una de sus formas flexionadas. Si se busca 'vista', saldrá un listado
        con el lema 'vista', como sustantivo femenino, pero también 'ver' o incluso 'vestir'. Cuando ocurre esto,
        se descargan (si no se ha hecho ya) todos estos lemas del listado que nos muestra la RAE.

        El archivo puede contener también un listado de ids de la RAE (separados por saltos de línea igualmente).
        Este listado solo se puede crear una vez que se han descargado y procesado todos los archivos de la RAE de un
        listado de lemas, y al leer toda esta información, se han extraído todos los ids de entradas de la RAE que
        aparecen en enlaces dentro de definiciones. La página que devuelve la RAE tiene las palabras de las definiciones
        etiquetadas con el id de la entrada a la que pertenecen (y también hay enlaces de otro tipo, tipo 'Véase' o
        enlaces entre entradas y acepciones sinónimas, u otras formas de escribir el lema...). Así, podemos crear un
        listado de ids que aparecen en las definiciones, y comprobar si todos esos ids ya están descargados.
        Esto es sencillo porque al descargar un archivo guardamos también el id que tiene en la RAE

        Para descargar los archivos se utiliza directamente un controlador que permite utilizar Firefox desde Python.
        Es importante hacerlo así, ya que la RAE utiliza redirecciones todo el rato, de forma que aunque nosotros
        queramos descargar http://dle.rae.es/?w=pardo, al final termina redirigiéndonos a http://dle.rae.es/?id=RuQF03b
        y además, no es una redirección inmediata, sino que puede tardar varios segundos incluso.
        Esto es un poco problemático, pero al usar Firefox nos olvidamos de todo: indicamos la URL que debe descargar,
        esperamos hasta que la página cargada sea una definición o una lista de lemas, y procesamos el contenido
        de la página que ha descargado. Si tarda mucho, pasamos al siguiente. Pero como este proceso, tratándose de
        casi 90.000 lemas, puede durar muchas horas y puede tener que realizarse en varias sesiones, guardamos en
        disco los items del listado que ya se han procesado, para que al reiniciar, sepamos por dónde vamos.

        Es importante que, aunque en la RAE pueda mostrar en una misma página más de una entrada (si son de la misma
        categoría gramatical), nosotros vamos a guardar cada entrada en un archivo independiente, nombrándolo de la
        forma 'lema.id.hmtl'. Para un mismo lema, puede haber más de un archivo (cada uno con un id distinto).

        Además, el servidor de la RAE, como es normal, limita el número de peticiones de un mismo origen para evitar
        ataques tipo DoS (o por lo que sea). Por ello, aproximadamente cada 100 palabras, la RAE nos baneará, y no
        nos querrá servir más páginas hasta pasado un tiempo (de 1-2 minutos). Esto se puede evitar cerrando el
        navegador Firefox y volviéndolo a abrir, terminando la sesión con la RAE y reiniciando una nueva, sin
        restricciones (lo identifica como un cliente distinto).

        :type items: [unicode]
        :param items:
        :param nombre_archivo_lemas:
        :param nombre_archivo_ids:
        :param localizacion_firefox_exe:
        :return:
        """
        # Se prefiere usar el listado de items. Si no, si hay archivo de lemas, se usa.
        # Si no, se usa el archivo de ids indicados si lo hay. Si no, se usa el archivo básico LEMARIO RAE.txt
        if not items:
            if nombre_archivo_lemas:
                nombre_archivo_items = nombre_archivo_lemas
            elif nombre_archivo_ids:
                nombre_archivo_items = nombre_archivo_ids
            else:
                nombre_archivo_items = directorio_archivos_rae_web + u'LEMARIO RAE.txt'
            with codecs.open(nombre_archivo_items, encoding='utf-8') as archivo_items:
                items = [item.strip() for item in archivo_items.read().split(u'\n')]
            nombre_archivo_items_ya_procesados = nombre_archivo_items[:-4] + u'-ya_procesados.txt'
        else:
            nombre_archivo_items_ya_procesados = directorio_archivos_rae_web + u'items_ya_procesados.txt'

        # Cargamos el listado de items que se han procesado previamente, y si no exite, lo creamos vacío.
        try:
            with codecs.open(nombre_archivo_items_ya_procesados, encoding='utf-8')\
                    as archivo_items_ya_procesados:
                items_ya_procesados = {item.strip()
                                       for item in archivo_items_ya_procesados.read().split(u'\n')
                                       if item}
        except IOError:
            # No lo ha podido abrir, no existía
            items_ya_procesados = set()
        # Metemos como items ya procesados todos los lemas que tengamos ya bajados y sus ids.
        items_ya_procesados |= {n
                                for f in listdir(directorio_lemas)
                                for n in f.split(u'.')[:2]
                                if isfile(directorio_lemas + f)}
        items_ya_procesados |= {n.split(u',')[0]
                                for f in listdir(directorio_lemas)
                                for n in f.split(u'.')[:1]
                                if isfile(directorio_lemas + f)}

        print(u'Cargados', len(items), u'ids.' if nombre_archivo_ids else u'lemas.',
            len(items_ya_procesados), u'de ellos ya procesados')
        items = [u'qwertyuiop'] + items  # El primero suele fallar (no da tiempo) así que se mete para que falle
        # Creamos una sesión con el Firefox. El browser es básicamente una ventana de Firefox.
        # Se pasan los parámetros del browser y del tiempo de espera como listas, por la única razón de que
        # así se pueden modificar dentro del método y que dichos cambios no se piedan al salir del método.
        # Según el resultado al cargar las páginas, el browser tendrá que eliminarse y recrearse, y el tiempo
        # de espera se verá modificado también (se tendrá que hacer en caso de baneo de la RAE).
        browsers = [Firefox(firefox_binary=localizacion_firefox_exe)]
        esperas = [2.0]
        try:  # Pueden darse excepciones ocasionadas por el servidor (puede denegarnos la conexión)
            for item in items:
                if item in items_ya_procesados:
                    # Ya lo procesamos en una vida anterior
                    continue
                url = u'http://dle.rae.es/?' + (u'id' if nombre_archivo_ids else u'w') + u'=' + item
                pagina = ParseadorRae.carga_pagina(localizacion_firefox_exe, browsers, url, esperas)
                # Actualizamos los valores del browser y el tiempo de espera.
                if not pagina or item == u'qwertyuiop':
                    # No ha cargado o es el primer lema "falso": se mete porque el primero suele fallar (no da tiempo).
                    continue

                # Vemos cuál es el contenido de la página
                try:
                    # EXISTENCIA DE <div id="a0">  --> Lista de entradas para un mismo lema, con las definiciones
                    # (habitualmente solo 1 entrada salvo homografías: si busco 'don' sale una página con 2 entradas:
                    # el de 'don1' y el de 'don2, doña')
                    if ParseadorRae.guarda_entradas(pagina):  # guarda_articulos devuelve True si no hay problemas
                        with codecs.open(nombre_archivo_items_ya_procesados, "a",
                                         encoding='utf-8') as archivo_items_ya_procesados:
                            archivo_items_ya_procesados.write(item + u'\n')
                        continue  # Siguiente item de la lista
                except NoSuchElementException:
                    # No teníamos una lista de entradas de un mismo lema. Probaremos otras opciones. No pasa nada.
                    # El lema que buscábamos no nos ha llevado a la página del lema. Inspeccionamos qué contiene.
                    try:
                        # EXISTENCIA DE <div id="l0">  --> Lista de entradas de distintos lemas que encajan con la
                        # palabra que se haya buscado.
                        # En la RAE se pueden buscar formas, no necesariamente lemas. Si se busca 'niñas' nos muestra
                        # la página para el lema 'niño, ña', que en este caso es solo uno, y por tanto aparece en un
                        # <div id="a0"> como en la mayoría de los casos. Pero si la palabra de entrada, aun pudiendo ser
                        # un lema, podría ser la forma de varios lemas, pues sale una lista. Si busco el prefijo '-ana'
                        # me muestra una lista con los lemas '-án, na' y '-ano1, na', pero incluso cuando se busca un
                        # lema, como 'vista', nos sale ese lema (el nombre, la vista) y demás lemas para los que podría
                        # ser forma: 'ver1', 'vestir', 'vista', 'visto, ta'. Incluso, se devuelven tambien pre/sufijos
                        # que encajan: si busco 'ano' me saca la lista con 'ano' y con '-ano1, na; -ano2'
                        # Como nos sale una lista de enlaces a los lemas que encajan, tendremos que guardar todos ellos.
                        id_lista_lemas = pagina.find_element_by_id('l0')
                    except NoSuchElementException:
                        # No teníamos una estructura de tipo <div id="l0"> con un listado de entradas de distintos lemas
                        # que encajan con el texto buscado. Quizá muestre lemas parecidos, que no encajan completamente,
                        # pero que tienen un pequeño cambio (usualmente un único carácter) con el texto buscado.
                        # Este resultado se da cuando el texto buscado no encaja con ningún lema, por ejemplo, si
                        # escribimos una voz latina con tildes: quórum -> nos devuelve cuórum y quorum.
                        try:
                            # EXISTENCIA DE <div id="l1">  --> El texto no encaja y da una lista de lemas parecidos
                            # En el fondo se trata igual, salvo que el nombre de la estructura es distinto
                            id_lista_lemas = pagina.find_element_by_id('l1')
                        except NoSuchElementException:
                            # Ni l0 ni l1: la palabra no está en el RAE y tampoco hay nada parecido. Es inválida.
                            # Nos aseguramos de que sea este el problema.
                            if u'La palabra ' + item + u' no está en el Diccionario' in pagina.text:
                                # La RAE nos dice claramente que la palabra no está.
                                # Como no está, hemos acabado, pero nos aseguramos de que no la volveremos a pedir.
                                with codecs.open(nombre_archivo_items_ya_procesados, "a",
                                                 encoding='utf-8') as archivo_items_ya_procesados:
                                    archivo_items_ya_procesados.write(item + u'\n')
                                continue  # Siguiente lema de la lista
                            else:
                                # No hay l0 ni l1 pero tampoco nos dice la RAE expresamente que no exista. Quizá se
                                # haya cargado mal o se nos haya colado una palabra rara en el listado.
                                print(u'Algo pasa con', item)
                                continue  # De momento pasamos del lema, ya veremos si la eliminamos o modificamos
                    # Tenemos una página con una <div id="l0"> o <div id="l1">, que se tratan de la misma forma.
                    # La lista es de la forma <div id="l0"><ul><li><a href="?id=XXXXXXX">-án, na</a></li><li><a href...
                    # Es una lista de enlaces a otras páginas, cada una de una entrada de un lema.
                    urls_lemas_rae = []
                    for enlace_articulo in id_lista_lemas.find_elements_by_tag_name('a'):
                        # Aunque href es relativo, el get_attribute da la url total: http://dle.rae.es/?id=XXXXXXX
                        # A veces da un id que es una sección de otro id: bocabajo -> id=5i6aRwS#BXl0o29
                        # Se separa la entrada del id de la acepción con un #
                        url_rae = enlace_articulo.get_attribute(u'href').split(u'#')[0]
                        lema_rae = re.sub(u'[0-9]+', u'', enlace_articulo.text)  # Quitamos el posible nº de acepción.
                        urls_lemas_rae.append((url_rae, lema_rae))
                    # Hemos sacado los ids de los lemas a los que puede hacer referencia el "lema" de la lista.
                    # Ya no nos interesa más info de la página, así que la reusamos para cargar los lemas encontrados.
                    guardado_con_exito = True
                    for url_rae, lema_rae in urls_lemas_rae:
                        id_lema_rae = url_rae.split(u'=')[1]
                        # Es muy probable que lo hayamos guardado previamente.
                        nombre_archivo = directorio_lemas + lema_rae.strip() + u'.' + id_lema_rae + u'.html'
                        if isfile(nombre_archivo):  # Si ya lo habíamos creado, nos evitamos recargar y guardar
                            continue
                        pagina = ParseadorRae.carga_pagina(localizacion_firefox_exe, browsers, url_rae, esperas)
                        if not pagina:
                            guardado_con_exito = False
                            break
                        guardado_con_exito = ParseadorRae.guarda_entradas(pagina)
                        if not guardado_con_exito:
                            break
                    if guardado_con_exito:
                        with codecs.open(nombre_archivo_items_ya_procesados, "a",
                                         encoding='utf-8') as archivo_items_ya_procesados:
                            archivo_items_ya_procesados.write(item + u'\n')
        except Exception as e:
            # El código es un poco así, y a veces falla porque aún no sé todas las posibles opciones. Así no se acumulan
            # los browsers abiertos, que come memoria y mucha.
            print(e)
        browsers[0].quit()

    @staticmethod
    def carga_pagina(binary, browsers, url, esperas, id_espera=u'resultados'):
        """Se descarga la página indicada por la url, y se espera un tiempo (y se cierra y abre el browser) si falla

        :type binary: unicode
        :param binary:
        :type browsers: [Firefox]
        :param browsers:
        :type url: unicode
        :param url:
        :param esperas: [float]
        :type id_espera: unicode
        :param id_espera:
        :return:
        """
        # Son listas únicamente para que se puedan modificar
        while True:
            try:
                browsers[0].get(url)  # Hacemos que el browser se descargue la url dada
                try:
                    # La página descargada es accesible y se pueden parsear las etiquetas
                    titulo = browsers[0].find_element_by_tag_name('title')  # Título de la página
                    if titulo.text == u'Solicitud rechazada':
                        # Toque de la rae, que rechaza la solicitud de la página
                        raise socket.error
                except NoSuchElementException:  # Falla al intentar sacar el title, pero el servidor nos ha servido algo
                    pass
                # Aún no sé por qué, pero algunas páginas no las carga bien. Suele ser la primera, y "otras"...
                # (depende principalmente de que el browser esté perfectamente cargado, y puede que del servidor)
                # Esperamos hasta que la página cargada muestre el id que indica que se ha cargado bien.
                WebDriverWait(browsers[0], timeout=esperas[0]).until(lambda x: x.find_element_by_id(id_espera).text)
                resultados = browsers[0].find_element_by_id(id_espera)
                if resultados.text == u'El servicio de consulta del diccionario no está disponible en estos' \
                                      u' momentos. Inténtelo de nuevo pasados unos segundos.':
                    # Toque de la rae, o que realmente el servidor está colapsado (que no, que es un baneo).
                    raise socket.error
                return resultados  # Salimos del bucle, porque no hay excepciones
            except socket.error as e:  # A veces nos deniegan la conexión, si hemos sacado muchos lemas seguidos
                # "Toque" de la rae.
                esperas[0] = 15  # Esperamos unos segundos
                print(u'La RAE nos banea. Esperamos', esperas[0], u'segundos y seguimos probando...')
                print(e)
                # Cerramos y abrimos el browser. Parece que con eso se contentan
                browsers[0].quit()
                browsers[0] = Firefox(firefox_binary=binary)
                sleep(esperas[0])  # Tras la espera, volvemos a intentar cargar
            except TimeoutException:  # falla al esperar que cargue "resultados"
                if u'Solicitud rechazada' in browsers[0].page_source:
                    # "Toque" de la rae.
                    esperas[0] = 15  # Esperamos unos segundos
                    print(u'La RAE nos banea. Esperamos', esperas[0], u'segundos y seguimos probando...')
                    # Cerramos y abrimos el browser. Parece que con eso se contentan
                    browsers[0].quit()
                    browsers[0] = Firefox(firefox_binary=binary)
                    sleep(esperas[0])  # Tras la espera, volvemos a intentar cargar
                else:
                    # No se ha cargado bien. Pasamos al siguiente lema de la lista. Ya lo recargaremos
                    return None

    @staticmethod
    def guarda_entradas(div_resultados):
        """
        <div id="resultados" role="main">
            <div id="a0">
                <article id="XXXXXXX">
                    <header class="f">don<sup>2</sup>, doña</header>
                    <div class="par">etimologías y textos de información morfosintáctica</div>
                    estructuras internas de la entrada: <p class="j", "m", k5"...
                </article>
            </div>
        </div>

        :param div_resultados: la estructura HTML dentro de la etiqueta <div id="resultados" role="main">...</div>,
                               que es la que contiene la lista de entradas compatibles con la forma o id buscado.
        :rtype: bool
        :return: True si ha habido éxito al guardar todas las entradas del lema. False si ha habido algún problema
        """
        id_a0 = div_resultados.find_element_by_id(u'a0')
        guardado_con_exito = True
        for entrada in id_a0.find_elements_by_tag_name(u'article'):  # Se llama 'article' pero son entradas
            id_lema_rae = entrada.get_attribute(u'id')  # El id de la entrada
            # Extraemos el lema, pero tenemos que tener en cuenta que el contenido de la estructura header es la que
            # se ve arriba. Aunque eliminemos el número de entrada, nos seguirán quedando cosas como 'don, doña'.
            # Este hecho, que el lema no sea el lema sino cómo lo muestra la RAE, nos servirá luego para extraer las
            # formas flexionadas (pero ya podrían haber tenido un criterio más práctico a la hora de escoger qué
            # ponen detrás de la coma).
            lema_rae = re.sub(u'[0-9]+', u'', entrada.find_element_by_tag_name(u'header').text)
            if lema_rae == u'con':
                # Hay un problema curioso. CON es una palabra reservada, como AUX, NUL, COM1, LPT1... No se puede
                # guardar un archivo que empiece por 'con...'. Así que lo guardamos distinto
                lema_rae = u'cón'
            nombre_archivo = directorio_lemas + lema_rae.strip() + u'.' + id_lema_rae + u'.html'
            try:
                # Guardamos el HTML de la estructura <article>, añadiéndole un pequeño formato para que pueda
                # abrirse con el navegador.
                archivo_lema = codecs.open(nombre_archivo, "w", encoding='utf-8')
                archivo_lema.write(u'<!DOCTYPE html>\n<html lang="es">\n<body>\n<article id="' + id_lema_rae + u'">\n')
                archivo_lema.write(entrada.get_attribute('innerHTML') + u'\n')
                archivo_lema.write(u'</article>\n</body>\n</html>')
                archivo_lema.close()
            except IOError:
                print(u'\nProblemas escribiendo', nombre_archivo)
                guardado_con_exito = False
                break
        return guardado_con_exito

    @staticmethod
    def descarga_paginas_conjugaciones(localizacion_firefox_exe=u'C:/Program Files/Mozilla Firefox/firefox.exe'):
        """Descargamos los archivos html pertenecientes a las conjugaciones de los verbos.

        Extraemos del lemario las entradas que contengan un id_conjugacion, y buscamos en la RAE el archivo de su
        conjugación y lo descargamos.
        """
        try:
            # Nos descargamos la lista de los ids de los archivos de conjugación que ya tengamos descargados.
            # Los archivos están nombrados así: lema.ID_LEMA.ID_CONJ.html
            ids_conj_descargadas = set([f.split(u'.')[2] for f in listdir(directorio_conjugaciones)
                                        if isfile(directorio_conjugaciones + f)])
        except IOError:
            os.makedirs(directorio_conjugaciones)
            ids_conj_descargadas = set()

        directorio_trabajo = dirname(os.path.realpath(__file__)) + u'/archivos_de_datos/rae/lemario/'
        nombre_archivo_lemario = directorio_trabajo + u'lemario_previo_rae_reprocesado.pkl.bz2'
        with bz2.BZ2File(nombre_archivo_lemario, 'rb') as archivo_lemario:
            lemario = pickle.load(archivo_lemario)

        # Browsers y esperas son listas para que se puedan modificar los parámetros al llamar a carga_pagina
        browsers = [Firefox(firefox_binary=localizacion_firefox_exe)]
        esperas = [2]
        # Vamos mirando todos los lemas del lemario, y para aquellos que tengan ids_conjugacion descargaremos
        # el archivo del id correspondiente.
        primero = True
        for lema_txt, lema_rae in lemario.items():
            for entrada in lema_rae:
                for id_conj in entrada["morfo"]["ids_conjugacion"] if "ids_conjugacion" in entrada["morfo"] else []:
                    if id_conj not in ids_conj_descargadas:
                        url = u'http://dle.rae.es/srv/fetch/?id=' + id_conj
                        pagina = ParseadorRae.carga_pagina(localizacion_firefox_exe, browsers, url, esperas, u'a0')
                        if primero:
                            # El primero siempre falla
                            pagina = ParseadorRae.carga_pagina(localizacion_firefox_exe, browsers, url,
                                                               esperas, u'a0')
                            primero = False
                        nombre_archivo = directorio_conjugaciones + lema_txt + u'.' + entrada["id"] + u'.' + \
                                         id_conj + u'.html'
                        ParseadorRae.guarda_conjugacion(pagina, nombre_archivo)
                        ids_conj_descargadas |= set(id_conj)
        browsers[0].quit()

    @staticmethod
    def guarda_conjugacion(pagina, nombre_archivo):
        try:
            archivo_conjugacion = codecs.open(nombre_archivo, "w", encoding='utf-8')
            archivo_conjugacion.write(u'<!DOCTYPE html>\n<html lang="es">\n')
            archivo_conjugacion.write(u'<body role="main">\n<div id="a0">')
            archivo_conjugacion.write(pagina.get_attribute('innerHTML'))
            archivo_conjugacion.write(u'</div>\n</body>\n</html>')
            archivo_conjugacion.close()
            return True
        except IOError:
            print(u'\nProblemas escribiendo', nombre_archivo)
            return False

    @staticmethod
    def extrae_formas_de_lema(lema_rae_txt):
        u"""Se mete el lema de texto como aparece en la RAE ("español, la") y se devuelven de una a tres formas

        Si se da una única forma, será la forma base invariable, porque el lema no tiene comas.

        Se se dan dos formas, hay dos posibilidades:
        - La primera es la masculina y la segunda la teminación femenina.
        - La primera es el prefijo (acabado en "-") y el segundo es el sufijo (empezando por "-").

        Si se dan tres formas, la primera es la del prefijo (acabado en "-"), y la segunda y tercera son las formas
        masculina y la terminación femenina del sufijo.

        Se tienen en cuenta las tildes diacríticas y se mantienen en la forma femenina.

        :param lema_rae_txt:
        :rtype: [unicode]
        :return:
        """
        # Hay varios lemas que tienen problemas con este algoritmo: "el, la", "él, ella" y "(aqu)esos, sas".
        # En estos casos se extraerían el/ela, él/élella (por la tilde diacrítica) y (aqu)esos/(aqu)esosas.
        if lema_rae_txt == u'el, la':
            return [u'el', u'la']
        if lema_rae_txt == u'él, ella':
            return [u'él', u'ella']
        if lema_rae_txt[-8:] == u'sos, sas':
            return [lema_rae_txt[:-8] + u'sos', lema_rae_txt[:-8] + u'sas']
        formas = lema_rae_txt.split(u', ')
        if len(formas) == 1:
            # El lema es invariable. Devolvemos la única forma
            return [lema_rae_txt]

        # Si hay más de una forma, habrá quizá un prefijo-sufijo, o al menos una forma femenina truncada que habrá
        # que expandir.
        if len(formas) == 2 and formas[0][-1] in [u'-', u'‒'] and formas[1][0] in [u'-', u'‒']:
            # Es un lema de prefijo y sufijo: zoo-, -zoo. No hace falta expandir ninguna forma y hemos acabado.
            return formas
        # Tengamos 2 o 3 formas, la última representa a un "sufijo" femenino aplicable sobre la penúltima forma.
        # Aunque se trate de prefijo más sufijo masculino y femenino, es posible que el sufijo femenino sólo sea
        # una parte de la forma, y que se tenga que extraer adjuntándola a la forma masculina. Por ejemplo:
        # "cefalo-, -céfalo, la". Así que cuando hay prefijo, ya sea en 2 o 3 formas, hay que extraer la forma
        # femenina fundiendo de alguna manera la forma masculina y el "sufijo femenino".
        forma_masculina = formas[-2]  # Contamos desde atrás por si hay prefijo
        sufijo_femenino = formas[-1]

        # Usualmente la forma femenina que se da es simplemente un cambio de terminación, un sufijo femenino.
        # Vamos a crear la forma femenina completa usando la forma completa masculina y el sufijo femenino.
        if sufijo_femenino == u'a':
            # En estos casos, la forma masculina siempre acaba en 'o', excepto con un lema muy raro, que es
            # "agallú, a". Actualmente se expande como "agallú, agalla", pero no tengo ni idea de si es así
            # como se tiene que hacer o no (¿agallá?). Este lema está francamente mal expuesto.
            # if forma_masculina[-1] != u'o':
            #     print(u'Tenemos un lema raro:', lema_rae_txt)
            forma_femenina = forma_masculina[:-1] + sufijo_femenino
            return (formas[:1] if len(formas) > 2 else []) + [forma_masculina, forma_femenina]

        palabra_masculino = Palabra(forma_masculina, calcula_alofonos=False, organiza_grafemas=True)
        palabra_sufijo_femenino = Palabra(sufijo_femenino, calcula_alofonos=False, organiza_grafemas=True)
        if palabra_sufijo_femenino.set_tilde(con_tilde=False) != sufijo_femenino:
            # El sufijo femenino tiene una tilde. Estas son las formas más difíciles de interpretar,
            # como "héroe, ína". Significa que la última sílaba del lema masculino es de tipo V, y se convierte
            # en una vocal cerrada que forma hiato. Así que tenemos que quitar las última sílaba a la forma
            # masculina, quitarle posibles tildes y añadirle el sufijo femenino.
            forma_femenina = palabra_masculino.elimina_silaba(-1).set_tilde(con_tilde=False) + sufijo_femenino
            return (formas[:1] if len(formas) > 2 else []) + [forma_masculina, forma_femenina]

        # La forma en la que decide la RAE qué poner después de la coma para marcar la forma femenina es un
        # poco extraña. La forma más práctica es ver cuál es el primer carácter del sufijo femenino y buscar
        # su última aparición en el lema masculino, y empalmar ahí. Hay que tener cuidado con no formar grupos
        # "lll" en cosas como "gallo, llina", y en el caso de que dicho empalme no sea posible ("mambí, sa")
        letra_empalme_femenino = sufijo_femenino[0]
        tilde_diacritica = lema_rae_txt[0] != u'-' and\
                           copy.deepcopy(palabra_masculino).ajusta_tildes() != forma_masculina
        if tilde_diacritica:
            forma_masculina_sin_tildes = forma_masculina  # Mantenemos la tilde: "cuánto, ta" -> cuánto, cuánta
        else:
            forma_masculina_sin_tildes = palabra_masculino.set_tilde(con_tilde=False)
        posicion_empalme_masculino = forma_masculina_sin_tildes.rfind(letra_empalme_femenino)
        if posicion_empalme_masculino != -1:  # -1 es que no lo ha encontrado
            # Hemos encontrado un punto de empalme.
            if forma_masculina_sin_tildes[:posicion_empalme_masculino] != \
                    forma_masculina[:posicion_empalme_masculino] and posicion_empalme_masculino != 0:
                # print(lema_rae_txt, u'quizá se procese mal')
                pass
            if len(palabra_sufijo_femenino.get_silabas()) > 1 and not palabra_masculino.contiene_hiato():
                forma_femenina = forma_masculina_sin_tildes[:posicion_empalme_masculino] + sufijo_femenino
            else:
                forma_femenina = forma_masculina[:posicion_empalme_masculino] + sufijo_femenino
            # No tenemos en Cuenca dígrafos y hay cosas como: perro, rra; o gallo, llina. Se nos juntan tres "l"/"r"
            # seguidas al seguir el algoritmo.
            forma_femenina = forma_femenina.replace(u'lll', u'll').replace(u'rrr', u'rr')
            if len(Palabra(forma_femenina, calcula_alofonos=False, organiza_grafemas=True).get_silabas()) > \
                    len(palabra_masculino.get_silabas()) + 1:
                # La forma femenina tiene al menos dos sílabas más que la masculina. Podemos estar en el caso de
                # "príncipe, princesa". Probablemente el "sufijo" femenino sea la forma completa.
                if len(palabra_sufijo_femenino.get_silabas()) < len(palabra_masculino.get_silabas()):
                    # Mala espina. El "sufijo" femenino es más corto en sílabas que la forma masculina. No parece
                    # que el sufijo sea en realidad la forma completa.
                    print(u'jorl por', lema_rae_txt)
                elif forma_masculina[-1] != sufijo_femenino[0]:
                    # Si el "sufijo" femenino tiene al menos la misma longitud en sílabas que la forma masculina,
                    # y no es que se empalmen directamente en el extremo, el "sufijo" femenino es en realidad la
                    # forma femenina completa.
                    forma_femenina = sufijo_femenino
                else:
                    # Estamos en un caso tipo "líder, resa", "zar, rina" donde se nos ha creado la forma "lideresa"
                    # y "zarina" que tienen dos sílabas más que el lema masculino, pero eso es debido a que la coda
                    # se vuelve ataque y el sufijo es de dos sílabas. Lo dejamos así.
                    a = 1  # Únicamente para poder poner un breakpoint
                    pass
        else:
            # No hemos encontrado un empalme. Estamos en algo como "mambí, sa". Simplemente pegamos el sufijo
            # femenino al final de la forma masculina. Pero hay una excepción, que es "emperador, triz", que,
            # francamente, está fatal puesto porque solo puedes sacar la forma femenina si ya te la sabes.
            if forma_masculina[-3:] == u'dor' and sufijo_femenino == u'triz':
                forma_femenina = forma_masculina[:-3] + sufijo_femenino
            else:
                forma_femenina = forma_masculina + sufijo_femenino

        # En los lemas con forma masculina aguda, pueden tener una tilde que desaparece en la forma femenina,
        # como en "cabrón, na". Así que tenemos que reajustar las tildes.
        if not tilde_diacritica:
            forma_femenina = Palabra(forma_femenina, calcula_alofonos=False, organiza_grafemas=True).ajusta_tildes()
        return (formas[:1] if len(formas) > 2 else []) + [forma_masculina, forma_femenina]

    @staticmethod
    def descarga_lemas_freeling_de_rae():
        directorio_freeling = dirname(os.path.realpath(__file__)) + u'/archivos_de_datos/freeling/'
        nombre_archivo_lemas_nuevos = directorio_freeling + u'lemas_nuevos.txt'
        if True:
            nombre_archivo_diccionario_freeling = directorio_freeling + u'diccionario_freeling.txt'
            with codecs.open(nombre_archivo_diccionario_freeling, encoding='utf-8')\
                    as archivo_lexicon_freeling:
                lexicon_freeling_txt = archivo_lexicon_freeling.read()
            # Las primeras y la última línea son temas de etiquetas xml
            lexicon_freeling = {}
            lemas = set()
            lineas_txt_freeling = lexicon_freeling_txt.split(u'\n')[4:-1]
            print( u'Procesando', len(lineas_txt_freeling), u'líneas de archivo',
                nombre_archivo_diccionario_freeling, end=u' ')
            for linea_txt_freeling in lineas_txt_freeling:
                elementos = linea_txt_freeling.split()
                forma = elementos[0]
                if len(elementos) % 2 != 1:
                    print(u'Línea extraña con elementos pares:', linea_txt_freeling)
                tuplas_lema_tag = [(elementos[orden], elementos[orden + 1])
                                   for orden in range(1, len(elementos), 2)]
                for lema, tag in tuplas_lema_tag:
                    lexicon_freeling[forma] = lexicon_freeling.setdefault(forma, {})
                    lexicon_freeling[forma][lema] = lexicon_freeling[forma].setdefault(lema, []) + [tag]
                    lemas |= {lema}
            print(u'procesadas.')
            lexicon_rae = ParseadorRae.carga_lexicon()
            lemario_rae = ParseadorRae.carga_lemario()
            formas_nuevas = sorted([forma for forma in lexicon_freeling if forma not in lexicon_rae])
            lemas_nuevos = sorted([lema for lema in lemas if lema not in lemario_rae], reverse=True)
            del lemario_rae
            del lexicon_rae
            with codecs.open(nombre_archivo_lemas_nuevos, "w", encoding='utf-8')\
                    as archivo_lemas_nuevos:
                archivo_lemas_nuevos.write(u'\n'.join(lemas_nuevos))
        ParseadorRae.descarga_entradas_lemario(nombre_archivo_lemas=nombre_archivo_lemas_nuevos)
        ParseadorRae.lista_ids_faltantes()
        ParseadorRae.descarga_entradas_lemario(
                nombre_archivo_ids=directorio_archivos_rae_web + u'ids_extraídos.txt')
        ParseadorRae.lista_ids_faltantes()
        ParseadorRae.descarga_entradas_lemario(
                nombre_archivo_ids=directorio_archivos_rae_web + u'ids_extraídos.txt')
        ParseadorRae.crea_lemario(crea_lemario_previo=True, reprocesa_lemario=True)
        ParseadorRae.descarga_paginas_conjugaciones()

    @staticmethod
    def crea_lexicon_freeling():
        directorio_freeling = dirname(os.path.realpath(__file__)) + u'/archivos_de_datos/freeling/'
        nombre_archivo_diccionario_freeling = directorio_freeling + u'diccionario_freeling.txt'
        longitudes = {SUSTANTIVO: 9, ADJETIVO: 8, DETERMINANTE: 8, PRONOMBRE: 10, VERBO: 16, ADVERBIO: 4,
                      CONJUNCION: 4, PREPOSICION: 5, SIGNO: 4, INTERJECCION: 1}
        with codecs.open(nombre_archivo_diccionario_freeling, encoding='utf-8') \
                as archivo_lexicon_freeling:
            lexicon_freeling_txt = archivo_lexicon_freeling.read()
        # Las primeras y la última línea son temas de etiquetas xml
        lexicon_freeling = {}
        lexicon_rae = ParseadorRae.carga_lexicon()
        lineas_txt_freeling = lexicon_freeling_txt.split(u'\n')[4:-1]
        print(u'Procesando', len(lineas_txt_freeling), u'líneas de archivo',
            nombre_archivo_diccionario_freeling, end=u' ')
        for linea_txt_freeling in lineas_txt_freeling:
            elementos = linea_txt_freeling.split()
            forma = elementos[0]
            if len(elementos) % 2 != 1:
                print(u'Línea extraña con elementos pares:', linea_txt_freeling)
            if forma in lexicon_rae:
                continue
            tuplas_lema_tag = [(elementos[orden], elementos[orden + 1].upper())
                               for orden in range(1, len(elementos), 2)]
            for lema, tag in tuplas_lema_tag:
                lexicon_freeling[forma] = lexicon_freeling.setdefault(forma, {})
                lexicon_freeling[forma][lema] = lexicon_freeling[forma].setdefault(lema, {})
                tag = tag + (NA * (longitudes[tag[0]] - len(tag)))
                lexicon_freeling[forma][lema][tag] = [u'fre|0|0']
        print(u'procesadas.')
        del lexicon_rae
        directorio_trabajo = dirname(os.path.realpath(__file__)) + u'/archivos_de_datos/freeling/'
        if not os.path.exists(directorio_trabajo):
            os.makedirs(directorio_trabajo)
        nombre_archivo_lexicon = directorio_trabajo + u'lexicon_freeling.pickle'
        print(u'Guardando lexicón en', u'.../' + u'/'.join(nombre_archivo_lexicon.split(u'/')[-5:]))
        with open(nombre_archivo_lexicon, 'wb') as archivo_lexicon:
            # ujson.dump(lexicon, archivo_lexicon, ensure_ascii=False, escape_forward_slashes=False)
            pickle.dump(lexicon_freeling, archivo_lexicon, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def carga_lexicon_freeling():
        directorio_trabajo = dirname(os.path.realpath(__file__)) + u'/archivos_de_datos/freeling/'
        path_archivo_lexicon = directorio_trabajo + u'lexicon_freeling.pickle'
        if not os.path.exists(path_archivo_lexicon):
            print(u'Falta el archivo', path_archivo_lexicon + u'.')
            return {}
        print(u'Cargando archivo', u'.../' + u'/'.join(path_archivo_lexicon.split(u'/')[-5:]), end=u' ')
        with open(path_archivo_lexicon, 'rb') as entrada:
            lexicon = pickle.load(entrada)
        print(u'cargado.')
        return lexicon


class ParseadorArticuloRae(HTMLParser):
    # class="j" (j1, j2). Acepción
    # class="m". Locución
    # class="l" (l3). Enlace a locución de otro lema. Aparecerá como class="m" en ese otro lema. Solo es un enlace.
    def __init__(self, lema_rae_txt, extrae_ids=False):
        HTMLParser.__init__(self)
        self._lema_rae_txt = lema_rae_txt
        self._formas_expandidas = ParseadorRae.extrae_formas_de_lema(lema_rae_txt)
        self._n_entrada = 0
        self._id = u''
        self._acepciones_rae = []
        self._locuciones_rae = []
        self._tag_actual = u''
        self._ids_alternativos = []  # Puede tener valor aunque no haya acepción alguna (véase lema -ante -> -nte)
        # TODO: ahora mismo, _abbrs_alternativo no se procesa de ninguna manera (solo se añaden cosas)
        self._abbrs_alternativo = []  # Puede tener valor aunque no haya acepción alguna
        self._morfo = {}  # Tiene información morfosintática: enlaces a otros lemas que son plural, apócope, neutro...

        self._extrae_ids = extrae_ids
        self._ids = []

    def handle_starttag(self, tag, attrs):
        if self._extrae_ids:
            # Solo queremos dar una batida y extraer todos los ids que aparecen en las páginas
            if tag == u'a' and attrs and attrs[0][0] == u'class' and len(attrs) > 1 and attrs[1][0] == u'href':
                for id_lema_acepcion in attrs[1][1].replace(u'?id=', u'').split(u'|'):
                    id_lema = id_lema_acepcion.split(u'#')[0]
                    # El id puede ser del tipo '#6dU2tAi', haciendo referencia a la propia entrada. En estos casos,
                    # equivale al id del lema que estamos procesando, que es uno de los ids existentes, así que no
                    # hacemos nada si el id_lema está vacío porque empieza por #
                    if id_lema:
                        if len(id_lema) != 7:
                            print(u'Tenemos un id raro (', id_lema, u') para el lema', self._lema_rae_txt)
                        else:
                            self._ids.append(id_lema)
            elif tag == u'mark' and attrs and attrs[0][0] == u'data-id':
                for id_lema_acepcion in attrs[0][1].split(u'|'):
                    id_lema = id_lema_acepcion.split(u'#')[0]
                    # El id puede ser del tipo '#6dU2tAi', haciendo referencia a la propia entrada. En estos casos,
                    # equivale al id del lema que estamos procesando, que es uno de los ids existentes, así que no
                    # hacemos nada si el id_lema está vacío porque empieza por #
                    if id_lema:
                        if len(id_lema) != 7:
                            print(u'Tenemos un id raro (', id_lema, u') para el lema', self._lema_rae_txt)
                        else:
                            self._ids.append(id_lema)
            return

        if tag == u'mark':
            # Es texto que aparece en una definición o en un ejemplo. No obstante, nos interesa el data, no la propia
            # etiqueta mark.
            if self._tag_actual not in [u'abbr', u'def', u'def a', u'h', u'h a', u'h post', u'h post a',
                                        u'h end', u'h end a', u'h end abbr']:
                print(self._lema_rae_txt, u'tiene una mark fuera de lugar en',
                    str(self._n_entrada) + u'|' + (str(len(self._acepciones_rae) - 1) if not self._locuciones_rae else
                                                   str(len(self._locuciones_rae) - 1) + u'|' +
                                                   str(len(self._locuciones_rae[-1]["acepciones"]) - 1)))
            elif self._tag_actual == u'abbr':
                self._tag_actual = u'def'

        elif tag == u'p':
            # Inicio de acepción del lema (class="j", "j1", "j2"...), inicio de locución (class="k5", "k6") o
            # inicio de acepción de locución (class="m").
            # También aparece en la etimología (class="n2")
            if self._tag_actual == u'par' and attrs and attrs[0][0] == u'class' and\
                    attrs[0][1] in [u'n2', u'n3']:
                # No es una acepción, es la etimología. No lo procesamos por el momento.
                # 'n2' es la clase habitual, pero puede ser 'n3' cuando en la etimología se expresa la etimología
                # de la palabra de la que deriva, es decir, algo como:
                # <div class="par"><p class="n3">Del <abbr title="latín">lat.</abbr> <em>-ăcus,</em> y este del
                # <abbr title="griego">gr.</abbr> -ακός <em>-akós.</em></p></div>
                self._tag_actual = attrs[0][1]
                return
            if self._tag_actual == u'n1 fc' and attrs and attrs[0][0] == u'class' and\
                    attrs[0][1] in [u'n3 par fc', u'n5 par fc']:
                # Es una etimología de una locución (n3) o información sobre que se escribe en mayúsculas:
                # <p class="k5" id="0IaRCFI"><u>asa</u> fétida</p>
                # <p class="n1 fc"><abbr title="También">Tb.</abbr> <a class="av var_fc_1" href="?id=3uPK9SU">asafétida.</a></p>
                # <p class="n3 par fc">Del <abbr title="latín científico">lat. cient.</abbr> <em>assa foetida.</em></p>
                # No es una acepción, es la etimología. No lo procesamos por el momento.
                self._tag_actual = attrs[0][1]
                return
            if attrs and attrs[0][0] == u'class' and attrs[0][1] == u'n2 par fc' and\
                    self._tag_actual in [u'k5', u'k6']:
                # Es una etimología dentro de una locución. Como ejemplo, en la entrada de 'agua' está la locución
                # 'agua jane', y la etimología dice que viene por Jane, una marca comercial.
                # <p class="k5" id="DSx0lAq"><u>agua</u> jane</p>
                # <p class="n2 par fc">De <em>Agua Jane</em>®, marca reg.</p>
                self._tag_actual = u'n2 par fc'
                return

            if self._tag_actual in [u'morf_orto', u'n5', u'n5 pl', u'n5 si', u'n5 ap', u'n5 nt'] and\
                    attrs and attrs[0][0] == u'class' and attrs[0][1] in [u'n5']:
                # No es una acepción, es una información morfosintática. Aparecen a veces dentro de un div de clase
                # 'morf_orto' que a su vez está dentro del div class="par" que marca la etimología. A veces vienen
                # varios p class="n5" seguidos.
                self._tag_actual = u'n5'
                return
            if attrs and attrs[0][0] == u'class' and attrs[0][1][0] in [u'j', u'k', u'm', u'l', u'b'] and\
                    (len(attrs[0][1]) == 1 or u'0' <= attrs[0][1][1] <= u'9') and\
                    (attrs[0][1][0] in [u'l', u'b'] or (len(attrs) > 1 and attrs[1][0] == u'id')):
                self._tag_actual = attrs[0][1]  # Guardamos el valor de la clase
                if attrs[0][1] in [u'j', u'j1', u'j2']:
                    # Entramos en una acepción nueva marcada por la 'j'. Las acepciones en la RAE están numeradas y
                    # organizado por categoría gramatical (indicado por la abreviatura). El primero de cada grupo de
                    # acepciones con la misma categoría (excepto la primera acepción) añaden un número que indica este
                    # cambio de categoría. Todas las primeras acepciones de cada categoría tienen además una abreviatura
                    # de clase 'd', que las marca en azul, frente a las demás, que tienen abreviatura de clase 'g', que
                    # se muestra en gris y además tienen una acepción de marca 'j', sin numeración (j1, j2...).
                    acepcion = {"lema_rae_txt": self._lema_rae_txt, "id": attrs[1][1], "abrs_morfo": [],
                                "abrs_ambito": [], "abrs_post": [], "definicion": u'', "definicion_post": u'',
                                "ejemplos": [], "ejemplos_post": []}
                    self._acepciones_rae.append(acepcion)
                elif attrs[0][1] in [u'k5', u'k6']:
                    # Entramos en una nueva locucion
                    locucion = {"lema_rae_txt": self._lema_rae_txt, "locucion": u'', "id": attrs[1][1],
                                "acepciones": [], "ids_alternativos": []}
                    self._locuciones_rae.append(locucion)
                elif attrs[0][1] == u'm':
                    # Entramos en una acepción de la locución
                    acepcion = {"lema_rae_txt": self._lema_rae_txt, "id": attrs[1][1], "abrs_morfo": [],
                                "abrs_ambito": [], "abrs_post": [], "definicion": u'', "definicion_post": u'',
                                "ejemplos": [], "ejemplos_post": []}
                    self._locuciones_rae[-1]["acepciones"].append(acepcion)
                elif attrs[0][1] in [u'l', u'l3', u'b']:
                    # Es una locución que está incluida en otro lema, ya que como locución que es, incluye también
                    # tanto este lema como el otro, pero se ha ubicado la definición en el otro lema.
                    # Esto genera problemas. Por una parte, esta locución aparecerá en otro lema y en principio
                    # podremos sacar sus datos más tarde (o quizá lo hayamos sacado ya). Por otra parte, por temas
                    # de etiquetado, va a ser más eficiente si para cada lema tenemos todas sus acepciones.
                    # Así que tenemos que guardarlo, sí, pero nos falta la información sobre el tipo de locución
                    # que es y demás.
                    # Así que guardamos aquí provisionalmente el id de la locución del otro lema (que será de la
                    # forma id_lema#id_locucion). En concreto, tendremos esto:
                    # <p class="l3"><a class="a" href="?id=9ZNs7ye#0z2LT53">coche de niño</a></p>
                    # Así que creamos una locución nueva, y ya rellenaremos los datos al final
                    # 'l3' es para la primera de estas locuciones (o 'b', si el lema sólo incluye locuciones de este
                    # tipo), y las demás llevan 'l'
                    # Creamos una locución vacía que iremos llenando después.
                    locucion = {"lema_rae_txt": self._lema_rae_txt, "locucion": u'', "id": u'',
                                "acepciones": [], "ids_alternativos": []}
                    self._locuciones_rae.append(locucion)
                elif attrs[0][1] == u'l2':
                    # En vez de tener una lista de acepciones, tenemos un enlace a otro lema, sinónimo, del tipo:
                    # <p class="l2"><abbr title="Véase">V.</abbr> <a class="a" href="?id=QgZMpot">-nte.</a></p>
                    # <p class="b"><a class="a" href="?id=3YKtkpX#5uWXe5c">argumento <u><i>a contrariis</i></u></a></p>
                    # Ya tenemos las abreviaturas. No nos interesa.
                    return
                else:
                    print(u'Un <p... que no tiene la forma normal de acepcion/locucion!!', self._lema_rae_txt, attrs)
                return
            elif attrs and attrs and attrs[0][0] == u'class' and attrs[0][1] == u'n1':
                # Existen sufijos, tipo -aco1, ca, que tiene una variante con la sílaba tónica en la previa al
                # sufijo. Estas formas, tipo ‒́aco, que no pueden ni buscarse en la web, sólo son accesibles de
                # esta forma. Pero también aparecen estas variantes del lema para otras palabras (acedía -> acedia).
                # La idea es que tenemos algo como esto:
                # <p class="n1"><abbr title="También">Tb.</abbr> <a class="av" href="?id=0V5qh1z">‒́aco.</a></p>
                # Así que identificaremos la abbr, y luego sacaremos el id y el lema del <a> para crear una
                # entrada idéntica a esta, pero con un lema distinto.
                self._tag_actual = u'n1'
                return
            elif attrs and attrs[0][0] == u'class' and attrs[0][1] == u'n1 fc' and\
                    self._tag_actual in [u'k5', u'k6']:
                # Houston, we've got a problem. Tenemos algo como esto:
                # <p class="k6" id="DSjSDL7">mal <u>aconsejado, da</u></p>
                # <p class="n1 fc"><abbr title="También">Tb.</abbr> <a class="av var_fc_2" href="?id=NyXEubo">malaconsejado.</a></p>
                # En principio el lema que viene (más adelante) es en el enlace a una entrada.
                # El caso es que ese lema al que hacemos referencia también debería estar en nuestro listado,
                # así que lo obviamos (a lo sumo, podríamos marcarlas como sinónimas).
                self._tag_actual = u'n1 fc'
                return
            elif attrs and attrs[0][0] == u'class' and attrs[0][1] == u'n4 par fc' and\
                    self._tag_actual in [u'k5', u'k6']:
                # Es una indicación sobre que se escribe con mayúscula una acepción, como ocurre en 'adoración':
                # <p class="n4 par fc"><abbr title="Escrito">Escr.</abbr> con <abbr title="mayúscula">may.</abbr>
                # Nos podria interesar, el hecho de cambiar a mayúscula, pero complica bastante y no es muy importante
                self._tag_actual = u'n4 par fc'
                return

            print(u'Un <p... que no tiene la forma normal de acepcion/locucion!!', self._lema_rae_txt, attrs)

        elif tag == u'span':
            if attrs and attrs[0][0] == u'class':
                if attrs[0][1] in [u'd']:
                    # Aparece dentro del texto de abreviaturas, para añadir algún texto, normalmente "y", "Era"...
                    if self._tag_actual != u'abbr' or\
                            (self._locuciones_rae and self._locuciones_rae[-1]["acepciones"][-1]["definicion"]) or\
                            (not self._locuciones_rae and self._acepciones_rae[-1]["definicion"]):
                        # print(self._lema_rae_txt, u'tiene algo en cian fuera de abreviatura inicial')
                        self._tag_actual = u'span abbr'
                    else:
                        pass
                    return
                if attrs[0][1] in [u'u']:
                    # Con 'u' marca la palabra en rojo (mira en "pie"), con 'd' en cian. Lo dejamos y se meterá como
                    # parte de la definición
                    if self._tag_actual == u'abbr':
                        self._tag_actual = u'def'
                    elif self._tag_actual != u'def':
                        # print(u'Palabra en rojo en', self._lema_rae_txt, u'que no está en definición')
                        pass
                    return
                elif attrs[0][1] == u'n_acep':
                    # Estamos en una etiqueta de número de acepción. El valor será el data incluido en el span y lo
                    # procesaremos via el handle_data
                    self._tag_actual = u'n_acep'
                    return
                elif attrs[0][1] == u'k1':
                    # Se usa para meter una palabra sin negrita dentro del "lema" de una locución.
                    return
                elif attrs[0][1] == u'h':
                    # Es una frase de ejemplo, que aparece en cursiva y morado. A veces vienen ejemplos en la sección
                    # de morfología que no interesan.
                    if self._tag_actual in [u'n4 par fc']:
                        # Es un extraño ejemplo que viene en una sección de morfología de una locución. Como en "Perú".
                        # Por ejemplo, se dice que se usa con mayúscula inicial y se da un ejemplo.
                        return
                    if self._tag_actual in [u'def', u'h', u'h post', u'h end']:
                        acepcion = self._locuciones_rae[-1]["acepciones"][-1] if self._locuciones_rae \
                            else self._acepciones_rae[-1]
                        if self._tag_actual in [u'h post']:
                            acepcion["ejemplos_post"].append(u'')
                        elif self._tag_actual in [u'h end']:
                            if acepcion["ejemplos"] and (acepcion["abrs_post"] or acepcion["definicion_post"]):
                                acepcion["ejemplos_post"].append(u'')
                                self._tag_actual = u'h post'
                            else:
                                acepcion["ejemplos"].append(u'')
                                self._tag_actual = u'h'
                        else:
                            acepcion["ejemplos"].append(u'')
                            self._tag_actual = u'h'
                    elif self._tag_actual == u'abbr':
                        # Un ejemplo inmediatamente después de una abreviatura
                        acepcion = self._locuciones_rae[-1]["acepciones"][-1] if self._locuciones_rae \
                            else self._acepciones_rae[-1]
                        if acepcion["ejemplos"] and (acepcion["abrs_post"] or acepcion["definicion_post"]):
                            acepcion["ejemplos_post"].append(u'')
                            self._tag_actual = u'h post'
                        else:
                            acepcion["ejemplos"].append(u'')
                            self._tag_actual = u'h'
                    else:
                        # Es un ejemplo en la sección de morfología. Solo ocurre en "magno, na", que además
                        # tiene un par de ejemplos
                        # print(self._lema_rae_txt, u'tiene un ejemplo raramente ubicado')
                        pass
                    return
                elif attrs[0][1] == u'i5':
                    # Es un texto que aparece dentro de una frase de ejemplo, para que no aparezca en cursiva, del tipo:
                    # <span class="h"><mark data-id="7V3pfqt">Cardiaco</mark>
                    # <span class="i5"><mark>o</mark></span> <mark>cardíaco</mark>.</span></p>
                    return
                elif attrs[0][1] == u'i2':
                    # Se utiliza para marcar siglos en las acepciones, del tipo:<span class="i2">XI.</span>
                    return
                elif attrs[0][1] == u'i4':
                    # Se utiliza para marcar los números de los reyes, tal que: Juan <span class="i4">I</span>
                    return
                elif attrs[0][1] == u'i1':
                    # Se utiliza para poner en mayúscula un texto de especial relevancia, dentro de un ejemplo, como
                    # una preposición regida por el verbo: <span class="i1">sobre</span>
                    if self._tag_actual == u'h':
                        self._tag_actual = u'h i'
                    else:
                        a = 1
                    return
                if attrs[0][1] in [u'af var_fc_1', u'af var_fc_2'] and self._tag_actual == u'n1 fc':
                    # Es una variante de una locución, pero dicha locución no aparece en la RAE de forma directa (solo
                    # aparece aquí). El problema es que, incluso sin tener un id propio, hay algunas otras
                    # acepciones/locuciones de otras entradas que, sorprendentemente, redirigen a estas locuciones,
                    # que no existen (no sé de dónde habrán sacado el id, porque no existe.
                    # <p class="k6" id="GaEQz6k">de alto abajo</p>
                    # <p class="n1 fc"><abbr title="También">Tb.</abbr> <span class="af var_fc_2">de alto a bajo.</span></p>
                    # Metemos un campo "tambien" en la locucion y al terminar de procesarla la duplicaremos.
                    self._locuciones_rae[-1].setdefault("tambien", []).append(u'')
                    self._tag_actual = attrs[0][1]
                    return
                if attrs[0][1] == u'nowrap':
                    # Se pone para que no corte en dos líneas algo, como una expresión matemática
                    return
                if attrs[0][1] == u'guiona':
                    # Aparece en los guiones "con tilde", indicando que la tónica es la previa al prefijo:
                    # <header class="f"><span class="guiona">‒́</span>cola</header>
                    return
            elif attrs[0][0] == u'style':
                # Normalmente se usa cuando hay algún carácter raro. No interesa
                return
            print(u'Un <span... que no tiene la forma de número de acepción', self._lema_rae_txt, attrs)
            return

        elif tag == u'abbr':
            if self._tag_actual in [u'def', u'h end', u'h end abbr', u'h', u'h post',
                                    u'def a', u'h end a', u'h a', u'h post a']:
                # Ya había una definición. Esta abreviatura probablemente esté relacionada con un uso del lema como
                # otra categoría.
                acepcion = self._locuciones_rae[-1]["acepciones"][-1] if self._locuciones_rae \
                    else self._acepciones_rae[-1]
                if attrs[-1][1].lower() in [u'etcétera', u'por extensión', u'por ejemplo', u'por antonomasia',
                                            u'nanómetro(s)', u'milímetro(s)', u'centímetro(s)', u'metro(s)',
                                            u'kilómetros',
                                            u'kilómetro(s) por hora', u'metro(s) por segundo',
                                            u'metro(s) por segundo cada segundo',
                                            u'mililitro(s)', u'centilitro(s)', u'litro(s)', u'hectolitro(s)',
                                            u'centímetro(s) cúbico(s)', u'metro(s) cúbico(s)',
                                            u'metro(s) cuadrado(s)', u'área(s)',
                                            u'miligramo(s)', u'decigramo(s)', u'centigramo(s)', u'gramo(s)',
                                            u'kilogramo(s)', u'tonelada(s)',
                                            u'kilogramo(s) por metro cúbico', u'gramos/centímetro',
                                            u'grado(s)', u'grado(s) centígrado(s)', u'grado(s) fahrenheit',
                                            u'hercio(s)', u'kilohercio(s)', u'vatio(s)',
                                            u'hora(s)', u'minuto(s)', u'segundo(s)',
                                            u'milímetros de mercurio', u'milibar(es)',
                                            u'mol(es) por metro cúbico',
                                            u'símbolo', u'número atómico', u'fórmula', u'latín científico',
                                            u'don', u'usted',
                                            u'antes de cristo', u'después de cristo']:
                    txt = attrs[-1][1].replace(u'(', u'').replace(u')', u'')
                    if self._tag_actual in [u'def', u'def a']:
                        acepcion["definicion"] += txt
                    elif self._tag_actual in [u'h end', u'h end a']:
                        acepcion["definicion_post"] += txt
                    elif self._tag_actual in [u'h', u'h a']:
                        acepcion["ejemplos"][-1] += txt
                    else:
                        acepcion["ejemplos_post"][-1] += txt
                    self._tag_actual += u' abbr'
                else:
                    # TODO: hay que hacer todo esto
                    # En "finca" hay una abreviatura "Usadq..."
                    valor_abreviatura = re.sub(u'(?<=[Uu]sad)[oaq]s?((,| o) [Uu]sad[oa]s?){0,3}', u'o', attrs[-1][1])
                    if valor_abreviatura.lower() in [u'usado', u'usado más', u'usado también', u'usado frecuentemente',
                                                     u'era usado', u'era usado también']:
                        # Aparece dentro de la definición, abrevia el texto (a "U."), pero es parte de la definición
                        # posterior. Vamos, que se ha acabado la definición y esto es algo que indica cómo se usa,
                        # y no su significado.
                        if acepcion["definicion"]:
                            acepcion["definicion_post"] += valor_abreviatura
                            self._tag_actual = u'h end abbr'
                        else:
                            acepcion["definicion"] += valor_abreviatura
                            self._tag_actual = u'def abbr'
                        return
                    elif valor_abreviatura.lower() in [u'en aragón, usado', u'en puerto rico, usado',
                                                       u'usado también en expresiones como']:
                        # Aparecen en "aparatar", "jíbaro" y "mecachis", respectivamente. Es una abreviatura a medias.
                        # No añaden una información relevante, y se mete directamente como postdefinición.
                        # print(self._lema_rae_txt, u'tiene la abreviatura de', valor_abreviatura)
                        acepcion["definicion_post"] += valor_abreviatura
                        self._tag_actual = u'h end abbr'
                        return
                    elif valor_abreviatura.lower() == u'usado en plural':
                        # Aparece muy poco, creo que solo en un, na.
                        acepcion["abrs_morfo"].append(u'plural')
                        self._tag_actual = u'h end abbr'
                        return
                    elif valor_abreviatura.lower() in [u'singular', u'plural', u'frases', u'usada repetida',
                                                       u'aplicado', u'usado como', u'usado como insulto', u'usado como antífrasis']:
                        # Es una abreviatura que forma parte de la definición (aparece al inicio).
                        if acepcion["definicion"]:
                            acepcion["definicion_post"] += valor_abreviatura
                            self._tag_actual = u'h end abbr'
                        else:
                            acepcion["definicion"] += valor_abreviatura
                            self._tag_actual = u'def abbr'
                        return
                    elif valor_abreviatura.lower()[:8] in [u'aplicado', u'usado en']:
                        acepcion["abrs_ambito"].append(valor_abreviatura)
                        return
                    else:
                        acepcion["abrs_post"].append(valor_abreviatura)
                        if not re.match(u'[Ee]n (el |la )?([A-Z]|algunos|muchos|lenguaje|voces|plural)|'
                                        u'[Aa]plicado|(([Ee]ran? )?[Uu]sad[oa]s?)', valor_abreviatura):
                            print(self._lema_rae_txt, u'tiene una abreviatura (' + valor_abreviatura.lower() + u') después de ' +\
                                (u'una definición:' if self._tag_actual == u'def' else u'un ejemplo:'),
                                str(self._n_entrada) + u'|' + \
                                (str(len(self._acepciones_rae) - 1) if not self._locuciones_rae else
                                 (str(len(self._locuciones_rae) - 1) + u'|' +
                                  str(len(self._locuciones_rae[-1]["acepciones"]) - 1))))
                    self._tag_actual = tag
                return
            if self._tag_actual in [u'n1', u'n1 fc']:
                # En lemas que tienen otra variante, y esta será una abreviatura del tipo
                # <abbr title="También">Tb.</abbr> que no nos importa (la procesaremos, porque crearemos una segunda
                # acepción duplicada de la actual.
                return
            if self._tag_actual in [u'n2', u'n2 par fc', u'n3', u'n3 par fc']:
                # Estamos en la etimología. Será una abreviatura del tipo <abbr title="latín">lat.</abbr>
                # No nos interesa. 'n2' es la clase habitual, que se convierte en 'n3' cuando la etimología es doble,
                # dando la etimología de la palabra en español (habitualmente una palabra latina) y la etimología de
                # ésta (habitualmente una palabra griega de la que derivó la latina).
                # Solo nos interesa la abreviatura de apócope o contracción
                if attrs and attrs[0][0] == u'title' and attrs[0][1].lower() == u'apócope':
                    # print(u'Tenemos un apócope', self._lema_rae_txt)
                    self._morfo["es_apocope"] = True  # Lo extraeremos más adelante, de momento lo marcamos como apócope
                return
            if self._tag_actual == u'n5':
                # Es una abreviatura sobre una información morfosintántica que está en la etimología. Esta información
                # es relevante, porque incluye datos sobre formas plurales irregulares, neutros, apócopes...
                # Normalmente en esta parte hay enlaces a otras entradas de la RAE que son puras redirecciones a esta
                # entrada. Extraeremos la información morfosintáctica que nos sea de relevancia.
                # <div class="par"><p class="n2">De <em>aba.</em></p><div class="morf_orto"><p class="n5">
                # <abbr title="Usado solo en infinitivo y en imperativo">U. solo en infinit. y en imper.</abbr></p>
                # </div></div>
                if attrs and attrs[0][0] == u'title':
                    valor_abreviatura = attrs[0][1].lower()
                    if valor_abreviatura == u'plural':
                        # Se nos dan las formas plurales, como de "el, la" a "los, las".
                        self._tag_actual = u'n5 pl'  # Más adelante, se saca el id del <a...
                        # TODO: a veces no sale el <a sino un <strong, que indica que se enlaza a este mismo lema
                        return
                    if valor_abreviatura in [u'superlativo irregular', u'superlativos irregulares']:
                        # Se nos da el superlativo irregular de un adjetivo
                        self._tag_actual = u'n5 si'
                        return
                    if valor_abreviatura == u'apócope':
                        # Se nos da el apócope de algún tipo de adjetivo
                        self._tag_actual = u'n5 ap'
                        return
                    if valor_abreviatura == u'comparativo':
                        # Esta forma es un comparativo irregular de otro lema, como mejor, peor...
                        self._tag_actual = u'n5 co'
                        return
                    if valor_abreviatura == u'para el femenino':
                        # Esta abreviatura indica que aunque el lema tiene forma masculina y femenina, hay acepciones
                        # en las que se puede usar la forma masculina como ambigua: cónsul, lesa; aprendiz, za...
                        self._tag_actual = u'n5'  # No procesaremos nada más, pero se cambia la etiqueta para ignorar
                        self._morfo["masculino_ambiguo"] = True
                        return
                    if valor_abreviatura == u'o como':
                        # Es para un verbo que tiene una conjugación regular e irregular. Pero aparecerá en la conj
                        return
                    if valor_abreviatura.split()[0].lower() in [u'conjugación', u'como',  # como sustantivo/adjetivo...
                                                                u'infinitivo', u'gerundio', u'participio',
                                                                u'mayúscula', u'escrito', u'usado',
                                                                u'acepción', u'acepciones',
                                                                u'tercera', u'etcétera', u'también']:
                        # Se nos da el modelo de conjugación, pero como lo sacaremos de la tabla del archivo, se ignora.
                        # También puede hacer mención a alguna característica especial que luego aparecerá reflejada
                        # en las etiquetas de las acepciones, así que no importa no procesarlas.
                        return
                if attrs and attrs[0][0] == u'class' and attrs[0][1] == u'c' and len(attrs) > 1 and\
                        attrs[1][0] == u'title':
                    # Es algún tipo de información, seguramente de ámbito geográfico, metido en la parte morfosintáctica
                    return
                # Si hemos llegado hasta aquí es que no hemos reconocido la abreviatura. Sin embargo, por lo revisado
                # son abreviaturas con informaciones que no interesan y que suelen indicar excepciones de conjugación
                # o irregularidades y temas etimológicos que no nos interesan. Por ejemplo en "maldecir" o "milrayas".
                # print(u'una abreviatura en morfosintaxis que no es conocida:', self._lema_txt, attrs[0][1])
                return
            if self._tag_actual in [u'n5 pl', u'n5 si', u'n5 ap', u'n5 fa', u'n5 co']:
                # Se trata de alguna abreviatura no importante que aparece en la parte morfosintáctica
                if self._tag_actual == u'n5 si' and attrs and attrs[0][0] == u'title' and attrs[0][1] == u'regular':
                    # Indica que además de la forma irregular, está la regular
                    self._tag_actual = u'n5'  # No procesaremos nada más, pero se cambia la etiqueta para ignorar
                    self._morfo["tambien_superlativo_regular"] = True
                return
            if self._tag_actual == u'l2' and attrs and attrs[0][0] == u'title' and attrs[0][1] == u'Véase':
                # Es la abreviatura de Véase. No nos interesa
                return
            if self._tag_actual == u'n1 fc' and attrs and attrs[0][0] == u'title' and attrs[0][1] == u'También':
                # Es la abreviatura de También. No nos interesa. TODO: chequear lemas
                return
            if self._tag_actual in [u'n4 par fc', u'n5 par fc'] and attrs and attrs[0][0] == u'title' and\
                    (u'mayúscula' in attrs[0][1] or u'tercera persona' in attrs[0][1] or
                     attrs[0][1] in [u'Escrito', u'acepción']):
                # Es una abreviatura que no interesa. Suele ser una indicación de que la primera es con mayúscula o
                # que es una acepción que se usa solamente en 3ª persona.
                return
            if self._tag_actual in [u'abbr'] and attrs and attrs[0][0] == u'class' and \
                    attrs[0][1] in [u'c'] and len(attrs) > 1 and attrs[1][0] == u'title':
                # Es una abreviatura que aparece dentro de una acepción, y nos interesa.
                # El 'g' aparece en gris, pero tiene igual contenido que 'd' (en cian). El 'c' es para temas
                # geográficos y de ámbito y sale en cursiva y en cian.
                self._tag_actual = tag
                acepcion = self._locuciones_rae[-1]["acepciones"][-1] if self._locuciones_rae \
                    else self._acepciones_rae[-1]
                acepcion["abrs_ambito"].append(attrs[1][1])
                return
            if self._tag_actual in [u'span abbr'] and attrs and attrs[0][0] == u'title':
                acepcion = self._locuciones_rae[-1]["acepciones"][-1] if self._locuciones_rae \
                    else self._acepciones_rae[-1]
                if acepcion["definicion"]:
                    acepcion["abrs_post"][-1] += attrs[0][1]
                else:
                    acepcion["abrs_morfo"][-1] += attrs[0][1]
                self._tag_actual = tag
                return
            if self._tag_actual not in [u'abbr'] and attrs and attrs[0][0] == u'class' and \
                    attrs[0][1] in [u'c'] and len(attrs) > 1 and attrs[1][0] == u'title':
                print(self._lema_rae_txt, u'tiene una abreviatura de ámbito "c" y no está tras una abreviatura morfo (' + attrs[1][1] + u')')
            if self._tag_actual in [u'n_acep', u'abbr'] and attrs and attrs[0][0] == u'class' and\
                    attrs[0][1] in [u'd', u'g'] and len(attrs) > 1 and attrs[1][0] == u'title':
                # Es una abreviatura que aparece dentro de una acepción, y nos interesa.
                # El 'g' aparece en gris, pero tiene igual contenido que 'd' (en cian). El 'c' es para temas
                # geográficos y de ámbito y sale en cursiva y en cian.
                acepcion = self._locuciones_rae[-1]["acepciones"][-1] if self._locuciones_rae \
                    else self._acepciones_rae[-1]
                if self._tag_actual == u'n_acep':
                    valor_abreviatura = attrs[1][1].lower()
                    acepcion["abrs_morfo"].append(valor_abreviatura)
                elif attrs[1][1].lower() in [u'desusado, desusada, desusados o desusadas',
                                             u'desusado', u'desusada', u'desusados', u'desusadas']:
                    acepcion["abrs_morfo"].append(u'desusado')
                elif attrs[1][1].lower() in [u'poco usado o usada, poco usados o usadas',
                                             u'poco usado', u'poco usada', u'poco usadas']:
                    acepcion["abrs_morfo"].append(u'poco usado')
                elif attrs[1][1].lower() in [u'plural', u'aumentativo', u'diminutivo', u'superlativo',
                                             u'verbo impersonal', u'verbo pronominal']:
                    valor_abreviatura = attrs[1][1]
                    acepcion["abrs_morfo"].append(valor_abreviatura)
                elif attrs[1][1].lower() in [u'eufemismo, eufemístico o eufemística',
                                             u'eufemismos, eufemísticos o eufemísticas']:
                    acepcion["abrs_ambito"].append(u'eufemismo')
                elif attrs[1][1].split()[0].lower() in [u'coloquial', u'rural', u'vulgar', u'irónico',
                                                        u'festivo', u'despectivo', u'poético', u'culto', u'malsonante',
                                                        u'ponderativo', u'infantil', u'germanía', u'peyorativo',
                                                        u'afectivo', u'popular']:
                    valor_abreviatura = attrs[1][1].split()[0]
                    acepcion["abrs_ambito"].append(valor_abreviatura)
                elif attrs[1][1].lower() in [u'por antonomasia']:
                    acepcion["abrs_ambito"].append(attrs[1][1])
                elif attrs[1][1].lower() in [u'coloquiales', u'vulgares', u'malsonantes']:
                    valor_abreviatura = attrs[1][1][:-2]
                    acepcion["abrs_ambito"].append(valor_abreviatura)
                elif attrs[1][1].lower() == u'coloquiales poco usadas':
                    acepcion["abrs_ambito"].append(u'coloquial')
                    acepcion["abrs_morfo"].append(u'poco usado')
                elif attrs[1][1].lower() in [u'jergal', u'jerga estudiantil']:
                    acepcion["abrs_ambito"].append(u'jerga')
                elif attrs[1][1].split()[0].lower() in [u'irónicos']:
                    valor_abreviatura = attrs[1][1][0] + u'rónico'
                    acepcion["abrs_ambito"].append(valor_abreviatura)
                elif attrs[1][1].lower() in [u'usado', u'usada', u'usadas', u'usado, usada, usados o usadas',
                                             u'usado más', u'usado o usada también', u'usado frecuentemente',
                                             u'era usado o usada', u'era usado también']:
                    # Aparece al inicio de la definición, abrevia el texto (a "U."), pero es parte de la definición
                    valor_abreviatura = re.sub(u'(?<=[Uu]sad)[oaq]s?((,| o) [Uu]sad[oa]s?){0,3}', u'o', attrs[1][1])
                    acepcion["definicion_post" if self._tag_actual[:5] == u'h end' else "definicion"] += \
                        valor_abreviatura
                    self._tag_actual = u'def abbr'
                    return
                elif attrs[1][1].lower() in [u'usado como', u'usado como insulto', u'usado como antífrasis',
                                             u'usada repetida', u'aplicado']:
                    if acepcion["definicion"]:
                        acepcion["definicion_post"] += attrs[1][1]
                        self._tag_actual = u'h end abbr'
                    else:
                        acepcion["definicion"] += attrs[1][1]
                        self._tag_actual = u'def abbr'
                    return
                elif attrs[1][1].lower() in [u'por extensión']:
                    # Aparece en "rostro" y es parte de la definición
                    acepcion["definicion"] += attrs[1][1] + u','
                    self._tag_actual = u'def abbr'
                    return
                elif attrs[1][1].lower() in [u'era usado o usada']:
                    # Aparece al inicio de la definición, abrevia el texto (a "U."), pero es parte de la definición
                    acepcion["definicion_post" if self._tag_actual[:5] == u'h end' else "definicion"] += attrs[1][1][0] + u'ra usado'  # Respetamos la mayúscula
                    self._tag_actual = u'def abbr'
                    return
                elif attrs[1][1].lower() in [u'en aragón, usado', u'en puerto rico, usado']:
                    # Aparecen en "aparatar" y "jíbaro", respectivamente. No añaden una información relevante,
                    # y se mete directamente como postdefinición.
                    # print(self._lema_rae_txt, u'tiene la abreviatura de', attrs[1][1])
                    acepcion["definicion_post"] += attrs[1][1]
                    self._tag_actual = u'h end abbr'
                    return
                elif attrs[1][1].lower() in [u'significado que en singular']:
                    # En "fondillo" hay una abreviatura como partida en dos
                    acepcion["abrs_post"][-1] += u' ' + attrs[1][1]
                    self._tag_actual = u'h end abbr'
                    return
                elif attrs[1][1].lower() in [u'por ejemplo']:
                    # En "tras" se meten postejemplos que no van con 'h', sino con 'i' y precedido de "por ejemplo" como
                    # abreviatura. Que se les ha pirado un poco a los de la RAE aquí, vamos.
                    self._tag_actual = u'h post abbr'
                    acepcion["ejemplos_post"].append(u'')
                    return
                elif attrs[1][1] in [u'Dialectalmente, usado como femenino',
                                     u'Por antífrasis, usado también en sentido ponderativo']:
                    # Solo aparece en "puente" y "cabrón" respectivamente y da una información repetida o indescifrable.
                    return
                else:
                    if acepcion["definicion"]:
                        acepcion["abrs_post"].append(attrs[1][1])
                    else:
                        acepcion["abrs_morfo"].append(attrs[1][1])
                    if not re.match(u'[Ee]n (el |la )?([A-Z]|algunos)|[Aa]plicado|'
                                    u'(([Ee]ran? )?[Uu]sad[oa]s?)', attrs[1][1]):
                        print(self._lema_rae_txt, u'tiene una abreviatura desconocida (' + attrs[1][1] + u')',
                            str(self._n_entrada) + u'|' +\
                            (str(len(self._acepciones_rae) - 1) if not self._locuciones_rae else
                             (str(len(self._locuciones_rae) - 1) + u'|' +
                              str(len(self._locuciones_rae[-1]["acepciones"]) - 1))))
                self._tag_actual = tag
                return
            if self._tag_actual not in [u'n_acep', u'abbr'] and attrs and attrs[0][0] == u'class' and\
                    attrs[0][1] in [u'd', u'g'] and len(attrs) > 1 and attrs[1][0] == u'title':
                print(self._lema_rae_txt, u'tiene una abreviatura morfo "c" y no está al inicio (' + attrs[1][1] + u')')
            if attrs and attrs[0][0] == u'title' and self._tag_actual == u'abbr':
                # Hay casos en los que se añaden al final etiquetas de abreviatura, que van dentro de un span que es
                # el que marca la clase, algo del tipo:
                # <span class="d">Era <abbr title="usado también como pronominal">u. t. c. prnl.</abbr></span>
                valor_abreviatura = attrs[0][1].lower()
                acepcion = self._locuciones_rae[-1]["acepciones"][-1] if self._locuciones_rae else\
                    self._acepciones_rae[-1]
                acepcion["abrs_post"].append(valor_abreviatura)
                if not acepcion["definicion"]:
                    print(self._lema_rae_txt, u'tiene abreviatura post y no tenía definición (' + attrs[0][1] + u')')
                self._tag_actual = tag
                return
            if self._tag_actual == u'n1_av' and attrs and attrs[0][0] == u'title':
                # Es una abreviatura que aparece en una acepción que no tiene definición (salvo esta abreviatura) y
                # solo tiene un enlace a otro lema que tiene la información (será una variante ortográfica).
                self._abbrs_alternativo.append(attrs[0][1])
                return
            print(u'Un <abbr... que no tiene la forma de abreviatura', self._lema_rae_txt, attrs)

        elif tag == u'div':
            # Contiene la información de etimología y de información morfosintáctica (el cuadro gris)
            if attrs and attrs[0][0] == u'class':
                if attrs[0][1] == u'par':
                    self._tag_actual = u'par'
                    return
                elif attrs[0][1] == u'morf_orto':
                    self._tag_actual = u'morf_orto'
                    return
            print(u'<div... que no tiene la forma de etimología', self._lema_rae_txt, attrs)
            return

        elif tag == u'em':
            # Contiene la palabra de la que deriva etimológicamente. No nos interesa salvo que en realidad sea una
            # abreviatura.
            if self._tag_actual == u'abbr' and attrs and attrs[0][0] == u'class' and attrs[0][1] == u'c':
                # Es en realidad una abreviatura, vestida de em. Aparece por ejemplo en aforar:
                # <p class="j" id="0Ri4nle"><span class="n_acep">6. </span>
                # <abbr class="g" title="verbo transitivo">tr.</abbr> <em class="c">Teatro.</em>
                # <mark data-id="BxLriBU|DgXmXNM">Dicho</mark> <mark data-id="BtDkacL|BtFYznp">de</mark>...
                # El único problema es que ahora el valor de la abreviatura aparece como data entre los <em>...</em>
                self._tag_actual = u'em c'
                return
            if self._tag_actual == u'n5 co':
                # Como en mejor, peor, mayor... hemos visto una abreviatura de Comparativo y dentro del <em> aparece
                # el lema que nos lleva a bueno, malo, mal, bien, grande, pequeño...
                self._tag_actual = u'n5 co em'
                return
            if self._tag_actual not in [u'n1', u'n1_av', u'n1 fc', u'n2', u'n3', u'n3 par fc',
                                        u'n5', u'n5 pl', u'n5 si', u'n5 ap', u'n5 nt', u'n2 par fc',
                                        u'n4 par fc', u'b', u'l3', u'l', u'k5', u'k6', u'af var_fc_1', u'af var_fc_2']:
                print(u'<em... que no aparece dentro de la etiqueta de etimología', self._lema_rae_txt, attrs, self._tag_actual)

        elif tag == u'img':
            if attrs[0][0] == u'class' and attrs[0][1] in [u'e2', u'e1'] and attrs[1][0] == u'onclick':
                # 'e2' es para la conjugación más común, 'e1' es para la menos común. Cuando se tiene 'e1' la
                # conjugación es doble, y siempre hay una información de id alternativo (Tb. trasportar). Ese id
                # alternativo nos lleva a otra entrada de la RAE, que únicamente tendrá como definición la referencia
                # a este lema que estamos procesando. En realidad, 'e2' es para el lema que estamos procesando,
                # y 'e1' debe pasarse a ese otro lema (cuando lo reprocesemos) y quitarse de aquí.
                # Como mucho hay dos conjugaciones, y siempre el 'e1' va el último.
                self._morfo.setdefault("ids_conjugacion", []).append(attrs[1][1].replace(u"conjugar('?id=", u'').split(u"','")[0])
            else:
                print(u'<img... que no contiene la información de flexión verbal', self._lema_rae_txt, attrs)

        elif tag == u'a':
            # Con esta etiqueta, se da un enlace a otro lema/locución. A veces, aparece algún lema dentro de una
            # definición que aparece especialmente etiquetado y con el link (que puede incluir número de entrada
            # con un <sup>. Pero como no estamos interesados en las definiciones, no nos interesa.
            # Pero en ocasiones, aunque sea parte de la definición, nos interesa parsearlo. Esta etiqueta aparece
            # cuando en vez de una definición textual de la palabra, se da un enlace a otro lema (una redirección,
            # como de almóndiga a albóndiga) u otra locución, que puede ser de este mismo lema (como "niño de pecho"
            # y "niño de teta", ambas locuciones de "niño") o de lemas distintos (como "saltársele a alguien las
            # niñas de los ojos" del lema "niño" a "saltársele los ojos" del lema "ojo").
            # Si es una locución de la que ya tenemos los valores de abreviatura y locución, no tenemos que procesarla
            # porque ya tenemos todos los datos que nos hacen falta (a lo sumo podríamos guardar algo para identificar
            # que dos locuciones son sinónimas).
            # Si no tenemos el valor de abreviaturas, es que es una locución al final incluida (y explicada) en
            # otro lema, así que le metemos el id para que luego podamos rellenar estos huecos.
            if self._tag_actual in [u'abbr', u'def']:
                # Este enlace aparece dentro de la definición. Nos interesan especialmente si es de
                # superlativo, aumentativo, diminutivo o participio irregular (son entradas que tienen una
                # acepción que dice que son el superlativo... de otro lema).
                # Si no, consideramos esto como parte de la definición (posiblemente la única definición que tengan)
                # Son casos como "pluriétnico, ca", que dice que viene a ser lo mismo que "multiétnico").
                if attrs and attrs[0][0] == u'class' and len(attrs) > 1 and attrs[1][0] == u'href':
                    if "es_apocope" in self._morfo and "id_del_que_es_apocope" not in self._morfo:
                        if len(self._acepciones_rae) > 1:  # BOOOOORRRRRRRAAAAAAMMMMEEE
                            print(u'Abreviatura en', self._lema_rae_txt, u'que solo debería ir en la primera acepción')
                        self._morfo["id_del_que_es_apocope"] = attrs[1][1].replace(u'?id=', u'').split(u'#')[0]
                        # self._morfo.pop("es_apocope")
                        return
                    if "es_apocope_plural" in self._morfo and "id_del_que_es_apocope_plural" not in self._morfo:
                        if len(self._acepciones_rae) > 1:  # BOOOOORRRRRRRAAAAAAMMMMEEE
                            print(u'Abreviatura en', self._lema_rae_txt, u'que solo debería ir en la primera acepción')
                        self._morfo["id_del_que_es_apocope_plural"] = attrs[1][1].replace(u'?id=', u'').split(u'#')[0]
                        # self._morfo.pop("es_apocope")
                        return
                    if self._acepciones_rae:
                        for tag in [u'superlativo', u'aumentativo', u'diminutivo', u'participio irregular']:
                            if tag in self._acepciones_rae[0]["abrs_morfo"]:
                                self._morfo["id_del_que_es_" + tag.replace(u' ', u'_')] =\
                                    attrs[1][1].replace(u'?id=', u'').split(u'#')[0]
                                if len(self._acepciones_rae) > 1:  # BOOOOORRRRRRRAAAAAAMMMMEEE
                                    print(u'Abreviatura de ' + tag + u' en', self._lema_rae_txt, u'que solo debería ir en la primera acepción')
                                return
                    # Se toma como el inicio de la definición. Más adelante, obtendremos el data con el texto.
                    self._tag_actual = u'def a'
                    return
                else:
                    print(u'Un enlace <a en', self._lema_rae_txt, u'que no tiene la forma adecuada de href')
                    return
            if attrs and attrs[0][0] == u'class' and len(attrs) > 1 and attrs[1][0] == u'href':
                if self._tag_actual in [u'def', u'h', u'h end', u'h post'] and attrs[0][1] == u'a':
                    # Es una palabra de una definición que tiene un enlace "evidente". No cambiamos nada y
                    # la palabra se añadirá a la definición.
                    self._tag_actual += u' a'
                    return
                if self._tag_actual in [u'l', u'l3', u'b'] and attrs[0][1] in [u'a', u'av'] and\
                        self._locuciones_rae and not self._locuciones_rae[-1]["id"]:
                    # Es una locución del final. Extraemos información del id que será tal que así:
                    # <a class="a" href="?id=9ZNs7ye#0z2LT53">. Más adelante se reprocesará esta locución.
                    # La 'l3' es para la primera de estas locuciones (y es 'b' si es la única acepción de la entrada),
                    # y para las demás es 'l'
                    id_alternativo = attrs[1][1].replace(u'?id=', u'')
                    self._locuciones_rae[-1]["ids_alternativos"].append(id_alternativo)
                    return
                if self._tag_actual == u'l2' and attrs[0][1] == u'a':
                    # Se trata de una entrada que es únicamente una redirección, del tipo:
                    # <p class="l2"><abbr title="Véase">V.</abbr> <a class="a" href="?id=EXtXytb">élite.</a></p>
                    # Esto puede ocurrir tanto en acepciones como locuciones y lo distinguimos por la existencia o no
                    # de alguna locución en la lista.
                    id_alternativo = attrs[1][1].replace(u'?id=', u'')
                    if not self._locuciones_rae:
                        # Metemos la id en la lista de ids alternativos (puede haber más de uno, como en askenazí), y más
                        # adelante copiaremos en esta entrada los valores de la entrada alternativa (en realidad de una
                        # de ellas, de la principal, la única que contiene definiciones de verdad).
                        # Podemos ser una entrada y que se nos redirija a una locución.
                        self._ids_alternativos.append(id_alternativo)
                    else:
                        self._locuciones_rae[-1]["ids_alternativos"].append(id_alternativo)
                    self._tag_actual = u'l2_a'
                    return
                if self._tag_actual == u'n1' and attrs[0][1] == u'av':
                    # Tenemos una variante del lema. Algo como:
                    # <p class="n1"><abbr title="También">Tb.</abbr> <a class="av" href="?id=0V5qh1z">‒́aco.</a></p>
                    # <p class="n1"><abbr title="También">Tb.</abbr> <a class="av" href="?id=2TRlsTw">an-</a> ante vocal.</p>
                    # Tenemos que guardar el id y más adelante el lema equivalente
                    self._ids_alternativos.append(attrs[1][1].replace(u'?id=', u''))
                    self._tag_actual = u'n1_av'
                    return
                if self._tag_actual == u'n1 fc' and attrs[0][1] in [u'av var_fc_1', u'av var_fc_2', u'af var_fc_1', u'af var_fc_2']:
                    # Es un enlace como el de la locución "mal aconsejado, da" que lleva a "malaconsejado". Como el
                    # otro lema debería aparecer y aquí tenemos la definición completa, no nos interesa. Hay dos
                    # variantes, 'av var_fc_1' y 'av var_fc_2', parece que con fc_1 se incluye vírgula en sustitución
                    # del lema, tal que así:
                    # <p class="n1 fc"><abbr title="También">Tb.</abbr> <a class="av var_fc_1" href="#GZpD9CF">~ sicológico.</a></p>
                    # También está la tercera opción af var_fc_1 que es un enlace igual, salvo que solo se aplica a
                    # una acepción en concreto:
                    # <p class="n1 fc"><abbr title="También">Tb.</abbr>
                    # <a class="af var_fc_1" href="?id=56dr0WM">barrabrava</a> en <abbr title="acepción">acep.
                    # </abbr> 2, <abbr class="c" title="Argentina">Arg.</abbr></p>
                    return
                if self._tag_actual.split()[0] == u'n5' and attrs[0][1] == u'a':
                    if self._tag_actual == u'n5':
                        # En la zona de morfosintaxis se nos da una información "poco estándar" y que incluye el enlace a
                        # otro lema. Esto puede verse en verbos como "balbucir", donde se comenta que ciertas formas se
                        # suplen con formas de otro verbo ("balbucear"). O "muy" que es forma reducida de "mucho".
                        # print(u'Información morfosintáctica no estándar en', self._lema_txt)
                        return
                    if self._tag_actual == u'n5 pl':
                        # En la zona de morfosintaxis se nos dan las formas (irregulares) de plural.
                        # Metemos el id del lema que es el plural de este que estamos procesando.
                        if "id_plural" in self._morfo:
                            # Solo el lema "cualquiera" tiene dos plurales: "cualesquiera" y "cualesquier". Eso es
                            # debido a que en realidad el segundo plural es el apócope del primero. Es solo un lema,
                            # pero montamos esto solo para él.
                            # print(u'Hay más de un id para el plural', self._lema_txt)
                            self._morfo["id_apocope_plural"] = attrs[1][1].replace(u'?id=', u'').split(u'#')[0]
                        else:
                            self._morfo["id_plural"] = attrs[1][1].replace(u'?id=', u'').split(u'#')[0]
                        return
                    if self._tag_actual == u'n5 nt':
                        # En la zona de morfosintaxis se nos da la forma neutra. Metemos el id del lema que es la forma
                        # neutra de este lema que estamos procesando.
                        if "id_neutro" in self._morfo:
                            print(u'Hay más de un id para el neutro', self._lema_rae_txt)
                        self._morfo["id_neutro"] = attrs[1][1].replace(u'?id=', u'').split(u'#')[0]
                        return
                    if self._tag_actual == u'n5 ap':
                        # Tenemos un apócope
                        if "id_apocope" in self._morfo:
                            print(u'Hay más de un id para el apócope', self._lema_rae_txt)
                        self._morfo["id_apocope"] = attrs[1][1].replace(u'?id=', u'').split(u'#')[0]
                        # print(self._lema_txt, u'tiene un apocope con id', self._morfo["id_apocope"])
                        return
                    if self._tag_actual == u'n5 si':
                        # Es un caso como el de la entrada acre2, adjetivo, marcando el superlativo irregular.
                        if "ids_superlativos" in self._morfo:
                            # print(u'Hay más de un id para el superlativo', self._lema_txt)
                            self._morfo["ids_superlativos"].append(attrs[1][1].replace(u'?id=', u'').split(u'#')[0])
                        else:
                            self._morfo["ids_superlativos"] = [attrs[1][1].replace(u'?id=', u'').split(u'#')[0]]
                        return
                    if self._tag_actual == u'n5 fc':
                        # Tenemos el id de una de las formas de caso de algún pronombre. Tomamos de momento el id y
                        # más adelante, al reprocesar, se colocarán debidamente las formas de texto.
                        if "ids_formas_casos" not in self._morfo:
                            self._morfo["ids_formas_casos"] = [attrs[1][1].replace(u'?id=', u'').split(u'#')[0]]
                        else:
                            self._morfo["ids_formas_casos"].append(attrs[1][1].replace(u'?id=', u'').split(u'#')[0])
                        return
                    if self._tag_actual == u'n5 fa':
                        self._morfo["id_del_que_es_forma_atona"] = attrs[1][1].replace(u'?id=', u'').split(u'#')[0]
                        return
                    if self._tag_actual == u'n5 ft':
                        self._morfo["id_del_que_es_forma_tonica"] = attrs[1][1].replace(u'?id=', u'').split(u'#')[0]
                        return
            print(u'<a... que no es de locución final o lema alternativo', self._lema_rae_txt,
                str(self._n_entrada) + u'|' + (str(len(self._acepciones_rae) - 1) if not self._locuciones_rae else
                                               str(len(self._locuciones_rae) - 1) + u'|' +
                                               str(len(self._locuciones_rae[-1]["acepciones"]) - 1)), attrs)
            return

        elif tag == u'sup':
            # Esta etiqueta se usa para indicar el número de entrada. Si el lema no tiene ningún número, es que
            # tiene una única entrada, es decir, la entrada número 1.
            if self._tag_actual == u'header':
                # Indica el número de entrada que estamos procesando (un lema puede tener varias entradas)
                self._tag_actual = tag
            elif self._tag_actual == u'abbr':
                # Estamos dentro de un enlace a otro lema, y este <sup> indica a qué número de entrada hace referencia
                return
            elif self._tag_actual == u'l2_a':
                # Estamos en un véase también, y es el <sup> que indica el número de entrada que debe verse.
                # <p class="l2"><abbr title="Véase">V.</abbr> <a class="a" href="?id=MEbj2r3">-ito<sup>3</sup>.</a></p>
                # Nos da igual: tenemos el id
                return
            elif self._tag_actual in [u'n2', u'n2 par fc', u'n3'] or self._tag_actual[:2] == u'n5':
                # Es una marca <sup> para indicar qué entrada es de un lema que aparece en la etimología o dentro de
                # un cuadro gris con información morfosintáctica, algo como:
                # <div class="par"><p class="n2">
                # Del <abbr title="latín">lat.</abbr> <em>mente,</em> <abbr title="ablativo de">abl. de</abbr>
                # <em>mens, mentis</em> 'inteligencia<sup>1</sup>', 'propósito'.</p></div>
                return
            elif self._tag_actual in [u'def', u'h']:
                # Algún texto en superíndice dentro de la definición o ejemplo (como en "pico-"). Lo dejamos como
                # está, ya que no tenemos texto con formato.
                return
            elif self._tag_actual in [u'def a', u'h a', u'h end a', u'h post a']:
                # Hay una acepción (de entrada o de locución) cuya definición empieza con un enlace a otro lema,
                # y además se indica qué numero de entrada es.
                self._tag_actual = u'sup ' + self._tag_actual
            elif self._tag_actual in [u'def abbr', u'h end abbr', u'h abbr', u'h post abbr']:
                # Es una abreviatura de algo que incluye un ^2. Como ya hemos escrito el valor de la abreviatura,
                # nos lo saltamos.
                return
            else:
                print(u'<sup... que no aparece en el header', self._lema_rae_txt, attrs)

        elif tag == u'header':
            # El header es de la forma: <header class="f">coche<sup>1</sup></header>. El lema ya lo tenemos, y no
            # nos interesa, pero el número de entrada sí.
            self._tag_actual = tag

        elif tag == u'article':
            if attrs and attrs[0][0] == u'id':
                self._id = attrs[0][1]
                return
            print(u'<article... sin el id', self._lema_rae_txt, attrs)

        elif tag == u'strong':
            # Se pone con esta etiqueta algunas veces lo que debería ir con <a... Pero se usa el strong porque el
            # enlace sería a este mismo lema, y poner un enlace a sí mismo, no es bueno. Así que tratamos esta etiqueta
            # como "equilavente" al <a cuando estamos en la información morfosintáctica.
            if self._tag_actual.split()[0] == u'n5' and self._tag_actual != u'n5':
                self._tag_actual += u' st'

        elif tag == u'i':
            if self._tag_actual in [u'def', u'h', u'h end', u'h post']:
                # Es como si fuera un <a... pero haciéndolo sin el enlace.
                self._tag_actual += u' a'
                return

        elif tag not in [u'html', u'body', u'u', u'sub']:
            # <div contiene la etimología, y <em contiene la palabra de la que deriva. 'u' es underscore, u'i' itálica,
            # 'strong' negrita, 'sub' subíndice.
            print(u'etiqueta', tag, u'no procesada')

    def handle_endtag(self, tag):
        if tag == u'a':
            if self._tag_actual in [u'n1_av', u'l2_a']:
                self._tag_actual = self._tag_actual[:2]
            if self._tag_actual in [u'def a', u'h a', u'h end a', u'h post a']:
                self._tag_actual = self._tag_actual[:-2]
        elif tag == u'i':
            if self._tag_actual in [u'def a', u'h a', u'h end a', u'h post a']:
                self._tag_actual = self._tag_actual[:-2]
        elif tag == u'span':
            if self._tag_actual in [u'af var_fc_1', u'af var_fc_2']:
                self._tag_actual = u'n1 fc'
            elif self._tag_actual.split() and self._tag_actual.split()[0] == u'h':
                if self._tag_actual == u'h i':
                    self._tag_actual = u'h'
                else:
                    self._tag_actual = u'h end'
        elif tag == u'strong' and self._tag_actual.split() and self._tag_actual.split()[-1] == u'st':
            self._tag_actual = self._tag_actual[:-3]
        elif tag == u'abbr' and self._tag_actual in [u'def abbr', u'h end abbr', u'h abbr', u'h post abbr']:
            self._tag_actual = self._tag_actual[:-5]
        elif tag == u'sup' and self._tag_actual in [u'sup def a', u'sup h a', u'sup h end a', u'sup h post a']:
            self._tag_actual = self._tag_actual[4:]
        pass

    def handle_startendtag(self, tag, attrs):
        print(u'etiqueta', tag, u'no procesada')
        pass

    def handle_data(self, data):
        if not self._tag_actual or data == u'\n':
            return
        if self._tag_actual in [u'def', u'def a']:
            if not self._locuciones_rae:
                self._acepciones_rae[-1]["definicion"] += data
            else:
                self._locuciones_rae[-1]["acepciones"][-1]["definicion"] += data
        elif self._tag_actual in [u'h', u'h a', u'h i']:
            acepcion = self._locuciones_rae[-1]["acepciones"][-1] if self._locuciones_rae \
                else self._acepciones_rae[-1]
            acepcion["ejemplos"][-1] += data
        elif self._tag_actual in [u'h post', u'h post a']:
            acepcion = self._locuciones_rae[-1]["acepciones"][-1] if self._locuciones_rae \
                else self._acepciones_rae[-1]
            acepcion["ejemplos_post"][-1] += data
        elif self._tag_actual in [u'h end', u'h end a']:
            acepcion = self._locuciones_rae[-1]["acepciones"][-1] if self._locuciones_rae \
                else self._acepciones_rae[-1]
            if acepcion["definicion_post"] or data != u' ':
                acepcion["definicion_post"] += data
        elif self._tag_actual == u'n_acep':
            if not self._locuciones_rae:
                # La primera acepción es la número 0
                self._acepciones_rae[-1]["n_acepcion"] = int(data.split(u'.')[0]) - 1
            else:
                # La primera acepción es la número 0
                self._locuciones_rae[-1]["acepciones"][-1]["n_acepcion"] = int(data.split(u'.')[0]) - 1
        elif self._tag_actual in [u'k5', u'k6', u'l', u'l3', u'b']:
            # 'k5' es para locuciones en los que el lema está en primera posición. Son las primeras locuciones
            # en aparecer, y van en marrón oscuro. 'k6' es para locuciones en los que el lema no es la primera
            # palabra, y aparecen tras las locuciones 'k5' y en color marrón claro/naranja oscuro. Pero es lo mismo.
            # También, para 'b', 'l3' y 'l', que son locuciones al final que no incluye ningún dato salvo el enlace
            # a otra locución (de este lema o de otro).
            self._locuciones_rae[-1]["locucion"] += data
        elif self._tag_actual in [u'n1_av', u'l2_a']:
            # Tenemos un lema alternativo, del tipo:
            # <p class="n1"><abbr title="También">Tb.</abbr> <a class="av" href="?id=0V5qh1z">‒́aco.</a></p>
            # <p class="l2"><abbr title="Véase">V.</abbr> <a class="a" href="?id=QgZMpot">-nte.</a></p>
            # Teniendo el id, el texto nos da igual
            if (not self._locuciones_rae and not self._ids_alternativos) or\
                    (self._locuciones_rae and not self._locuciones_rae[-1]["ids_alternativos"]):
                print(u'un n1_av o l2_av que no sigue bien las reglas', self._lema_rae_txt, data)
        elif self._tag_actual == u'span abbr':
            acepcion = self._locuciones_rae[-1]["acepciones"][-1] if self._locuciones_rae \
                else self._acepciones_rae[-1]
            if acepcion["definicion"]:
                acepcion["abrs_post"].append(data)
            else:
                acepcion["abrs_morfo"].append(data)
            if data != u'Era ':
                print(self._lema_rae_txt, u'tiene una span abbr:', data)
        elif self._tag_actual == u'sup':
            # La primera entrada es la 0
            self._n_entrada = int(data) - 1
            self._tag_actual = u''
        elif self._tag_actual == u'em c':  # No confundir con E = m*c2
            # Es una abreviatura de tipo "c" (de ámbito) "disfrazada" de span (como en Teatro en "aforar").
            if data not in [u'Teatro.', u'Teatro', u'Danza.', u'Danza']:
                print(self._lema_rae_txt, u'tiene una abreviatura de ámbito con span', data)
            acepcion = self._locuciones_rae[-1]["acepciones"][-1] if self._locuciones_rae \
                else self._acepciones_rae[-1]
            acepcion["abrs_ambito"].append(data.replace(u'.', u''))  # A veces llevan punto y a veces no
            self._tag_actual = u'abbr'
        elif self._tag_actual == u'n5 co em':
            self._tag_actual = u'n5 co'  # A veces viene más de uno, como "mejor" que es comparativo de "bueno" y "bien"
            # En el texto solo aparece "bueno" o "malo" cuando debería aparecer "bueno, na", "malo, la"
            self._morfo.setdefault("lemas_de_los_que_es_comparativo", []).\
                append(data + (u', ' + data[-2] + u'a' if data[-1] == u'o' else u''))
        elif self._tag_actual in [u'af var_fc_1', u'af var_fc_2']:
            # El lema puede ser "perro, rra". Cogemos solo la versión masculina (que es la que concuerda)
            self._locuciones_rae[-1]["tambien"][-1] += re.sub(u'[.;,]',
                                                              u'', data.replace(u'~', self._lema_rae_txt.split(u',')[0]))
        elif self._tag_actual.split()[0] == u'n5':
            if self._tag_actual == u'n5':
                if data.strip() == u'Neutro':
                    # TODO: si lo que viene después no es un enlace tipo <a, habrá que parsear el texto. No obstante me
                    # parece que si no viene con enlace, es como un enlace al propio lema, es decir que la forma masculina
                    # (o la única que tiene) es también válida como neutro. Además, es que viene en una estructura <strong
                    self._tag_actual = u'n5 nt'
                elif data.strip() in [u'Formas de caso', u'Forma de caso']:
                    self._tag_actual = u'n5 fc'
                elif data.strip() == u'Forma átona de':
                    self._tag_actual = u'n5 fa'
                elif data.strip() == u'Forma tónica de':
                    self._tag_actual = u'n5 ft'
                elif data.strip() == u'Forma amalgamada de la preposición':
                    self._morfo["es_pronombre_amalgamado"] = True
                elif data.strip() in [u'Forma apocopada', u'Forma reducida']:
                    self._tag_actual = u'n5 ap'  # Hay al menos tres formas de marcar que es apócope
                elif False and data.strip() == u'Forma reducida de':  # Mejor que "muy" permanezca como lema aparte
                    # Indica que es la forma reducida, no apocopada, de otro lema. Mucho->muy y creo que nada más.
                    # Hacemos como si hubiéramos encontrado la abreviatura "Apócope" en la etimología.
                    self._tag_actual = u'abbr'
                    self._morfo["es_apocope"] = True  # Lo extraeremos más adelante, de momento lo marcamos como apócope
                    pass
                elif False and u'acento' in data.strip().lower():
                    print(self._lema_rae_txt, u'tiene un tema de acento: u"' + data + u'"')
            if self._tag_actual.split()[-1] == u'st':
                # Estamos dentro de una etiqueta <strong que está dentro de una información morfosintáctica de plural,
                # neutro... El texto será el lema al que hace referencia (su plural, su neutro...)
                for tag, tipo_info in [(u'pl', "plural"), (u'nt', "neutro")]:
                    if self._tag_actual == u'n5 ' + tag + u' st':
                        # No metemos el id para que luego no se reprocese más
                        if tipo_info == "plural":
                            self._morfo["formas_plural"] = self._morfo.setdefault("formas_plural", []) + \
                                [[f] for f in ParseadorRae.extrae_formas_de_lema(data.replace(u'.', u''))]
                        else:
                            self._morfo[tipo_info + "_txt"] = data.replace(u'.', u'')
                        # print(u'Se ha sacado de un <strong la forma', data.replace(u'.', u''), u'como', tipo_info, u'de', self._lema_txt)
                        break
        pass

    def parsea_entrada(self, texto_acepcion):
        self.feed(texto_acepcion)

        # Limpiamos los blancos
        for acepcion in self._acepciones_rae:
            acepcion["definicion"] = acepcion["definicion"].strip()
            acepcion["definicion_post"] = acepcion["definicion_post"].strip().replace(u'  ', u' ')
            for orden_ejemplo, ejemplo in enumerate(acepcion["ejemplos"]):
                acepcion["ejemplos"][orden_ejemplo] = ejemplo.strip()
            for orden_ejemplo, ejemplo in enumerate(acepcion["ejemplos_post"]):
                acepcion["ejemplos_post"][orden_ejemplo] = ejemplo.strip()

        # Tras parsear la entrada, buscamos las entradas de locuciones que incluyen un "También" y duplicamos la
        # locución.
        # También limpiamos los blancos
        if self._locuciones_rae:
            orden_locucion = len(self._locuciones_rae) - 1
            while orden_locucion >= 0:
                locucion = self._locuciones_rae[orden_locucion]
                for acepcion in locucion["acepciones"]:
                    acepcion["definicion"] = acepcion["definicion"].strip()
                    acepcion["definicion_post"] = acepcion["definicion_post"].strip().replace(u'  ', u' ')
                    for orden_ejemplo, ejemplo in enumerate(acepcion["ejemplos"]):
                        acepcion["ejemplos"][orden_ejemplo] = ejemplo.strip()
                    for orden_ejemplo, ejemplo in enumerate(acepcion["ejemplos_post"]):
                        acepcion["ejemplos_post"][orden_ejemplo] = ejemplo.strip()

                if "tambien" in locucion:
                    for nueva_locucion_txt in locucion["tambien"]:
                        # De momento copiamos también el id. Más adelante, puede cambiarse si hay un enlace a esta
                        # acepción "fantasma", con un id que no existe en la RAE (es algún tipo de error).
                        # print(u'Nueva locución para', self._lema_txt, u':', nueva_locucion_txt)
                        nueva_locucion = {"locucion": nueva_locucion_txt, "id": locucion["id"],
                                          "acepciones": locucion["acepciones"],
                                          "ids_alternativos": locucion["ids_alternativos"]}
                        self._locuciones_rae.append(nueva_locucion)
                    locucion.pop("tambien", None)
                orden_locucion -= 1
        return self.get_entrada()

    def get_entrada(self):
        entrada_rae = {"lema_rae_txt": self._lema_rae_txt,
                       "formas_expandidas": self._formas_expandidas,
                       "n_entrada": self._n_entrada,
                       "id": self._id,
                       "acepciones": self._acepciones_rae,
                       "locuciones": self._locuciones_rae,
                       "ids_alternativos": self._ids_alternativos,
                       "morfo": self._morfo}
        if self._extrae_ids:
            entrada_rae["ids"] = self._ids
        return entrada_rae


if __name__ == '__main__':
    lexicon = ParseadorRae.crea_lexicon_conjunto_rae_wik()
    exit()

    lexicon = ParseadorRae.carga_lexicon()
    formas_verbo = {}
    for forma, datos in lexicon.items():
        for lema, etiquetas in datos.items():
            for etiqueta, fuentes in etiquetas.items():
                if etiqueta[0] == VERBO:
                    if lema not in formas_verbo:
                        formas_verbo[lema] = set()
                    formas_verbo[lema].add(etiqueta[:0] + u'-' + forma)
    mas_formas = sorted([(len(formas), lema)
                         for lema, formas in formas_verbo.items()],
                        key=lambda tupla: -tupla[0])
    ejemplo = set([etiqueta[:12] + forma
                   for forma, datos in lexicon.items()
                   for lema, etiquetas in datos.items()
                   for etiqueta, fuentes in etiquetas.items()
                   if lema == u'erguir'])
    exit()

    lexicon = ParseadorRae.carga_lexicon(incluye_categorias=['VM'])
    datos = {}
    for forma, dic1 in lexicon.items():
        for lema, dic2 in dic1.items():
            for tag in dic2.keys():
                if tag[15] == '0':
                    datos.setdefault(lema, set()).add(tag[:12] + '-' + forma)
    for lema in datos.keys():
        datos[lema] = sorted(datos[lema])
    datos2 = {lema: len(formas) for lema, formas in datos.items()}
    datos3 = {}
    for lema, numero in datos2.items():
        datos3.setdefault(numero, [0, []])
        datos3[numero][0] += 1
        datos3[numero][1] += [lema]
    exit()
    lexicon = ParseadorRae.carga_lexicon()
    datos = {}
    for categoria, nombre in CATEGORIAS_A_TXT.items():
        resultado = list(sorted(set(
                [tag for forma, dic1 in lexicon.items() for lema, dic2 in dic1.items() for tag in dic2.keys()
                 if tag[0] == categoria])))
        datos[nombre] = resultado
    exit()
    lexicon = ParseadorRae.carga_lexicon()
    datos = {}
    for categoria, nombre in CATEGORIAS_A_TXT.items():
        caracteres = 0
        for forma, dic1 in lexicon.items():
            for lema, dic2 in dic1.items():
                for tag in dic2.keys():
                    if tag[0] == categoria:
                        caracteres = len(tag)
                        break
                if caracteres:
                    break
            if caracteres:
                break
        resultado = list(sorted(set([tag for forma, dic1 in lexicon.items()
                                     for lema, dic2 in dic1.items()
                                     for tag in dic2.keys() if tag[0] == categoria])))
        datos[categoria] = resultado
    exit()
    a = u'á'
    e = u'é'
    i = u'í'
    o = u'ó'
    u = u'ú'
    ParseadorRae.crea_lemario(crea_lemario_previo=True, reprocesa_lemario=True)  # No crearlo desde aquí.
    exit()

    lem = ParseadorRae.carga_lemario()  # Esto debe petar. Mira crea_lemario
    exit()

    ParseadorRae.reprocesa_entradas(ParseadorRae.crea_lemario_previo())
    exit()

    # ParseadorRae.crea_lexicon_freeling()
    # ParseadorRae.crea_lemario(crea_lemario_previo=True, reprocesa_lemario=True)
    ParseadorRae.crea_lexicon(incluye_categorias=u'', subdivide_lexicon=True, crea_lexicon_sql=False)
    ParseadorRae.crea_lexicon_basico()
    # ParseadorRae.subdivide_lemario()
    # ParseadorRae.crea_lexicon_sql()
    exit()

    ParseadorRae.descarga_entradas_lemario(nombre_archivo_lemas=directorio_archivos_rae_web + u'1. Lemas que FALTAN.txt')
    ParseadorRae.descarga_entradas_lemario(items=ParseadorRae.lista_ids_faltantes())
    ParseadorRae.descarga_entradas_lemario(
            nombre_archivo_ids=directorio_archivos_rae_web + u'ids_extraídos.txt')
    ParseadorRae.descarga_paginas_conjugaciones()
    exit()

    Flexionador.testea_flexionador(lemario_elegido=u'rae', actualiza_modelos=True, imprime_flexiones=False)


    # lemario = ParseadorRae.carga_lemario()

    # ParseadorRae.crea_lemario(crea_lemario_previo=False, reprocesa_lemario=False)
    ParseadorRae.subdivide_lemario()

    ParseadorRae.subdivide_lexicon()

    '''
    determinantes = {forma: datos for forma, datos in lexicon.items() if datos.values()[0].keys()[0][:1] != "A"}
    diccionario = {}
    for forma, datos_forma in determinantes.items():
        for lema, datos_lema in datos_forma.items():
            if lema not in diccionario:
                diccionario[lema] = {}
            if forma not in diccionario[lema]:
                diccionario[lema][forma] = datos_lema
            else:
                for tag, fuentes in datos_lema:
                    if tag in diccionario[lema][forma]:
                        print(u'Joder... qué complicado')
                    diccionario[lema][forma][tag] = fuentes
    '''

    # ParseadorRae.carga_lexicon(incluye_categorias=PRONOMBRE)

    # ParseadorRae.descarga_paginas_lemario(nombre_archivo_ids=directorio_archivos_rae_web + u'ids_extraídos.txt')
    # ParseadorRae.descarga_entradas_lemario(items=ParseadorRae.lista_ids_faltantes())
    # ParseadorRae.descarga_entradas_lemario(items=[u'con'])
    # ParseadorRae.descarga_paginas_conjugaciones()

    exit()
    """
    lemas_rae_txt = [u'mambí, sa', u'aquel, lla', u'gallo, llina', u'actor, triz', u'alto, ta', u'mucho, cha',
                     u'mediterráneo, a', u'vacío, a', u'vosotros, tras', u'podo-, ‒́podo',
                     u'ptero-, ‒́ptero, ra', u'zar, rina', u'vizconde, desa', u'virrey, virreina', u'tigre, gresa',
                     u'sacerdote, tisa', u'héroe, ína', u'príncipe, princesa', u'líder, resa', u'-ío, a',
                     u'león, na', u'aquel, lla', u'zoo-, -zoo', u'don, doña']
    for lema_rae_txt in lemas_rae_txt:
        print(lema_rae_txt + u':', end=u' ')
        for forma in ParseadorRae.extrae_formas_de_lema(lema_rae_txt):
            print(forma + u',', end=u' ')
        print(u'')

    nombres_archivos_lemas = (f for f in listdir(directorio_lemas) if isfile(directorio_lemas + f))
    for nombre_archivo_lema in nombres_archivos_lemas:
        lema_rae_txt = nombre_archivo_lema.split(u'.')[0]
        if u', ' not in lema_rae_txt:
            continue
        print(lema_rae_txt + u':', end=u' ')
        for forma in ParseadorRae.extrae_formas_de_lema(lema_rae_txt):
            print(forma + u',', end=u' ')
        print(u'')
    """
