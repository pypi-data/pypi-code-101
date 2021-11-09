#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""
"""

from __future__ import print_function
from iar_transcriber.palabra import Palabra
from iar_transcriber.sil_consts import ACPR
from iar_inflector.acep_consts import SUSTANTIVO, ADJETIVO, VERBO, ADVERBIO, PREPOSICION, CONJUNCION, PRONOMBRE,\
    ARTICULO_D, ARTICULO_I, ABREVIATURA, SIGLA, AFIJO, PREFIJO, SUFIJO, ELEMENTO_COMPOSITIVO, FLEXIVO, \
    ONOMATOPEYA, INTERJECCION, EXPRESION, SIMBOLO,\
    PARTICIPIO, PLURAL, INVARIABLE, PROPIO, COMUN,\
    MASCULINO, FEMENINO, AMBIGUO, NEUTRO, AUMENTATIVO, DIMINUTIVO, APOCOPE, \
    COMPUESTO, DE_ADJETIVO, NEGATIVO, GENERAL, DEMOSTRATIVO, ARTICULO_D,\
    SINGULAR, PRONOMINAL, PRESENTE, SUPERLATIVO,\
    DETERMINANTE, DESUSADO, POCO_USADO, CARDINAL,\
    DISTRIBUTIVO, INDEFINIDO, EXCLAMATIVO, INTERROGATIVO, PERSONAL, POSESIVO, RELATIVO_POSESIVO,\
    NOMINATIVO, ACUSATIVO, DATIVO, OBLICUO,\
    CONCESIVA, COORDINADA, SUBORDINADA, COPULATIVA, DISYUNTIVA, DISTRIBUTIVA, ADVERSATIVA, EXPLICATIVA, CONSECUTIVA, CAUSAL,\
    FINAL, TEMPORAL, CONDICIONAL, ILATIVA,\
    CALIFICATIVO, ORDINAL, GENTILICIO, SUSTANTIVADO, DE_PADECIMIENTO, DE_SUSTANTIVO, DE_VERBO, COMPARATIVO, RELATIVO,\
    TRANSITIVO, INTRANSITIVO, IMPERSONAL,\
    PRINCIPAL, AUXILIAR, COPULATIVO, AFIRMATIVO, CUANTITATIVO, DUBITATIVO, LOCATIVO,\
    INFINITIVO, GERUNDIO, IMPERATIVO, VOS,\
    POLITE, SIMPLE, CONTRAIDA, PRIMERA, SEGUNDA, TERCERA, PREPOSICIONAL, AMALGAMADO, INDISTINTO, REFLEXIVO,\
    NA, \
    SIGNO, PUNTUACION, DOS_PUNTOS, COMA, LLAVE, ETC, ADMIRACION, GUION, PARENTESIS, TANTO_POR_CIENTO, PUNTO,\
    INTERROGACION, COMILLAS, PUNTO_Y_COMA, BARRA, CORCHETE, PUNTOS_SUSPENSIVOS, COMPARADOR, COMILLA,\
    APERTURA, CIERRE,\
    CATEGORIAS_A_TXT
from iar_inflector.flex_consts import NOMBRES_TIEMPOS, NOMBRES_MODOS, CODIGOS_PERSONAS, NOMBRES_PERSONAS,\
    REFLEXIVOS, OBJETOS_INDIRECTOS, OBJETOS_DIRECTOS, NEXOS_IE,\
    CONJS_COPULATIVAS, CONJS_DISYUNTIVAS, CONJS_DISTRIBUTIVAS, CONJS_ADVERSATIVAS, CONJS_EXPLICATIVAS,\
    CONJS_CONSECUTIVAS, CONJS_CAUSALES, CONJS_FINALES, CONJS_CONCESIVAS, CONJS_TEMPORALES,\
    CONJS_CONDICIONALES, CATALOGO_ETIQUETAS,\
    INF, INF_P, GER, GER_P, PAR_SM, PAR_SF, PAR_PM, PAR_PF,\
    IP1S, IP2S, IP2V, IP3S, IP1P, IP2P, IP3P,\
    II1S, II2S, II3S, II1P, II2P, II3P,\
    IS1S, IS2S, IS3S, IS1P, IS2P, IS3P,\
    IF1S, IF2S, IF3S, IF1P, IF2P, IF3P,\
    IC1S, IC2S, IC3S, IC1P, IC2P, IC3P,\
    SP1S, SP2S, SP2V, SP3S, SP1P, SP2P, SP3P,\
    SI1S, SI2S, SI3S, SI1P, SI2P, SI3P,\
    SF1S, SF2S, SF3S, SF1P, SF2P, SF3P,\
    MP2S, MP2V, MP3S, MP1P, MP2P, MP3P,\
    MP2S_P, MP2V_P, MP3S_P, MP1P_P, MP2P_P, MP3P_P, CANON_VERBOS, CANON_ADJETIVOS, CANON_SUSTANTIVOS,\
    CANON_ADVERBIOS, CANON_PRONOMBRES, CANON_DETERMINANTES, CANON_CONJUNCIONES,\
    POSICION_CONJUGACION
from iar_inflector.acepcion import AcepcionRae, AcepcionWik
import bz2
import codecs
import os
import re
import copy
import ujson
try:
    from winsound import Beep as beep
except ImportError:
    def beep(frecuencia, duracion):
        pass
from os.path import isfile
import glob
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


class Flexionador:
    def __init__(self):
        pass

    @staticmethod
    def combina_flexiones(flexion_total, flexion_parcial):
        # Las variables de flexion son un dict de dicts. El dict externo tiene como clave la etiqueta EAGLES
        # y como contenido un diccionario cuya clave es la forma_txt y el contenido es una lista de
        # fuentes, del tipo: {'VMG000000000': {u'aflautando': ['wik|0|0']},
        #                     'VMG0000000FP': {u'aflautándolas': ['wik|0|0']},
        #                     ...
        #                    }
        if not flexion_total:
            flexion_total.update(flexion_parcial)
        else:
            # Añadimos las formas y sus etiquetas al lexicón, pero puede ser que no haya formas flexionadas.
            # Esto ocurre en las formas de caso de pronombres personales (nos, os, conmigo...), que
            # se incluyen como formas del lema principal (nosotros, vosotros, yo). Los pronombres
            # personales se aglutinan en cinco lemas: yo, tú, él, nosotros, vosotros.
            # Las formas de plural de 3ª se incluyen en el lema "él", pero las de plural de 2ª
            # no se meten en el "tú" (esto es cuestionable) y las de nosotros no se meten en el "yo"
            # (esto es bastante lógico, ya que "nosotros" no es precisaente el plural de "yo").
            for etiqueta, formas in flexion_parcial.items():
                if etiqueta not in flexion_total:
                    flexion_total[etiqueta] = formas
                else:
                    for forma_txt, fuentes in formas.items():
                        if forma_txt not in flexion_total[etiqueta]:
                            flexion_total[etiqueta][forma_txt] = fuentes
                        else:
                            flexion_total[etiqueta][forma_txt] += fuentes

    @staticmethod
    def flexiona_lema(lema, ajusta_lema, incluye_cliticos):
        flexion_lema = {}
        for entrada in lema.get_entradas():
            if type(entrada.get_acepciones()[0]) == AcepcionWik:
                flexion_entrada = Flexionador.flexiona_entrada_wik(entrada, ajusta_lema, incluye_cliticos)
            else:
                flexion_entrada = Flexionador.flexiona_entrada_rae(entrada, ajusta_lema, incluye_cliticos)
            Flexionador.combina_flexiones(flexion_lema, flexion_entrada)
        return flexion_lema

    @staticmethod
    def flexiona_lema_rae(lema, ajusta_lema, incluye_cliticos):
        flexion_lema = {}
        for entrada in lema.get_entradas():
            # if not entrada.get_acepciones():
            #     print(lema.get_lema_txt(), u'no tiene acepciones en su entrada', entrada.get_n_entrada(),\
            #         u', pero tiene', len(entrada.get_locuciones()), u'locuciones')
            flexion_entrada = Flexionador.flexiona_entrada_rae(entrada, ajusta_lema, incluye_cliticos)
            Flexionador.combina_flexiones(flexion_lema, flexion_entrada)
        return flexion_lema

    @staticmethod
    def flexiona_lema_wik(lema, ajusta_lema, incluye_cliticos):
        flexion_lema = {}
        for entrada in lema.get_entradas():
            flexion_entrada = Flexionador.flexiona_entrada_wik(entrada, ajusta_lema, incluye_cliticos)
            Flexionador.combina_flexiones(flexion_lema, flexion_entrada)
        return flexion_lema

    @staticmethod
    def flexiona_entrada(entrada, ajusta_lema, incluye_cliticos):
        if not entrada.get_acepciones():
            # Hay algunas entradas en la RAE como "cuatrocientos" que no tienen acepciones, solo locuciones.
            return {}
        if type(entrada.get_acepciones()[0]) == AcepcionWik:
            return Flexionador.flexiona_entrada_wik(entrada, ajusta_lema, incluye_cliticos)
        else:
            return Flexionador.flexiona_entrada_rae(entrada, ajusta_lema, incluye_cliticos)

    @staticmethod
    def flexiona_entrada_rae(entrada, ajusta_lema, incluye_cliticos):
        hay_nombres = len([True for acepcion in entrada.get_acepciones()
                           for dato in [acepcion.get_datos()] + acepcion.get_acepciones_derivadas()
                           if "categoria" in dato and dato["categoria"] == SUSTANTIVO]) > 0
        flexion_entrada = {}
        # Una entrada contiene una o más acepciones, aunque existen 1.005 entradas que no incluyen acepciones, y solo
        # tienen locuciones, como "cuclillas" o "cuatrocientos", y muchas otras. Bastantes de ellas son nombres propios.
        # En una entrada se tienen acepciones "similares", es decir, solo contienen verbos, o contienen
        # nombres/adjetivos/adverbios/interjecciones (esto está un tanto mezclado),
        # o son prefijos/elementos compositivos, y así. A su vez, cada acepción puede tener acepciones derviadas, que
        # es cuando se tienen abreviaturas de "Usado también como..." y que pueden convertir un nombre en un adjetivo,
        # cambiar el tipo de verbo, y cosas por el estilo.
        # Las acepciones tienen una serie de valores "fijos", propios de la entrada y que se se aplican a todas las
        # acepciones de la entrada, y otros que son propios de la acepción, que están en la estructura _datos.
        # Pero además, se tiene una lista con las acepciones derivadas. Las acepciones derivadas se representan con
        # una estructura de datos (_acepciones_derivadas) equivalente a la estructura _datos de la acepción).
        # Así que para flexionar al completo, tenemos que flexionar tanto acepciones como acepciones derivadas de
        # cada acepción (las "subacepciones").
        # Para que se pueda flexionar toda la entrada como cada una de las acepciones por sí mismas, y que dicha
        # flexión incluya tanto la propia acepción como las acepciones derivadas que pueda tener, la función que
        # flexiona una acepción busca también en las _acepciones_derivadas.
        # Aquí vamos a "expandir" las acepciones, creando tantas acepciones como acepciones + acepciones derivadas haya,
        # vaciando la estructura _acepciones_derivadas para que al flexionar cada una de estas subacepciones no se
        # flexione dos veces lo mismo.
        # Esto tiene una motivación, y es la de ahorrar flexionar muchas cosas que en realidad son lo mismo. Es común
        # que un verbo, por ejemplo, tenga 10-15 (sub)acepciones, pero que en realidad solo haya 2-3 diferentes,
        # porque todas son bien transitivas, bien intransitivas o pronominales (o alguna otra cosa). Flexionar lleva
        # tiempo, así que intentamos flexionar solo cuando es imprescindible, y lo evitamos cuando la flexión de
        # dos (sub)acepciones solo varia en el código de la fuente que lo ha generado.
        datos_ya_flexionados = []
        plurales = []
        for n_acepcion, acepcion in enumerate(entrada.get_acepciones()):
            datos_y_derivados = [acepcion.get_datos()] + acepcion.get_acepciones_derivadas()
            acepcion_simple = copy.deepcopy(acepcion)
            acepcion_simple.reset_acepciones_derivadas()
            for orden_datos, datos in enumerate(datos_y_derivados):
                if plurales:
                    # Cada acepción lleva una copia de la información morfosintáctica de la entrada en general.
                    # Se le pasa esta información cuando se crea la acepción. No obstante, hay acepciones que solo
                    # aparecen en plural. Esto nos da problemas, porque es posible que el lema esté ya en plural
                    # (como en "pegásides") o no (como en "andada"). Solo consideramos que el lema está ya en plural
                    # cuando la primera acepción de una entrada es válida únicamente en plural, y es por eso por lo
                    # que tenemos que hacer este trapis de extraer los plurales de la primera acepción e ir pasándolo
                    # a las demás.
                    acepcion_simple.set_formas_plural(plurales)
                acepcion_simple.set_datos(datos)
                if orden_datos > 0:
                    # Las acepciones derivadas tienen número de acepción decimal.
                    acepcion_simple.set_n_acepcion(float(acepcion_simple.get_n_acepcion()) + 0.1)
                # Para evitar calcular la formas flexionadas muchas veces en cada entrada, nos fijamos si es necesario
                # antes de hacerlo:
                ya_flexionado = False
                for datos_previos, n_acepcion_previa in datos_ya_flexionados:
                    if not ([k for k in datos if k not in datos_previos or datos_previos[k] != datos[k]] +
                            [k for k in datos_previos if k not in datos or datos[k] != datos_previos[k]]):
                        # Como tiene idénticas etiquetas, tendrá idéntica flexión. Basta con añadir la fuente.
                        ya_flexionado = True
                        for etiqueta, formas in flexion_entrada.items():
                            for forma, fuentes in formas.items():
                                if u'rae|' + str(entrada.get_n_entrada()) + u'|' + str(n_acepcion_previa) in fuentes:
                                    fuentes.append(u'rae|' + str(entrada.get_n_entrada()) + u'|' + str(acepcion_simple.get_n_acepcion()))
                                    pass
                # flexion_acepcion es un dict de dicts. El dict externo tiene como clave la etiqueta EAGLES
                # y como contenido un diccionario cuya clave es la forma_txt y el contenido es una lista de
                # fuentes, del tipo: {'VMG000000000': {u'aflautando': ['wik|0|0']},
                #                     'VMG0000000FP': {u'aflautándolas': ['wik|0|0']},
                #                     ...
                #                    }
                if not ya_flexionado:
                    flexion_acepcion = Flexionador.flexiona_acepcion_rae(acepcion_simple, incluye_cliticos,
                                                                         hay_nombres)
                    Flexionador.combina_flexiones(flexion_entrada, flexion_acepcion)
                    if not plurales and acepcion_simple.get_formas_plural():
                        # Si la primera acepción es "solo plural" y cumple unas condiciones, el lema estará
                        # dado ya en su forma plural. Pero puede ser que alguna acepción, que no sea la primera,
                        # solo aparezca en plural, y entonces no sepamos si el lema aparece ya en plural o no.
                        plurales = acepcion_simple.get_formas_plural()
                    if acepcion.get_lema_rae_txt() != u'aun':
                        # Esto es un parche horroroso. Pero es que la RAE no ha puesto un lema para "aun" y
                        # otro para "aún", sino que pone en la parte de morfología que las tres primeras
                        # acepciones se escriben con tilde (WTF?). Así evitamos que copie la primera flexión
                        # para todas las acepciones.
                        datos_ya_flexionados += [(datos, acepcion_simple.get_n_acepcion())]  # TODO: meter solo si distintas
        return flexion_entrada

    @staticmethod
    def flexiona_acepcion(acepcion, ajusta_lema, incluye_cliticos):
        if type(acepcion) == AcepcionWik:
            return Flexionador.flexiona_acepcion_wik(acepcion, ajusta_lema, incluye_cliticos)
        else:
            return Flexionador.flexiona_acepcion_rae(acepcion, incluye_cliticos)

    @staticmethod
    def flexiona_acepcion_rae(acepcion, incluye_cliticos, hay_nombres=False):
        if False and acepcion.get_lema_rae_txt() == u'etcétera':
            pass
        flexion_acepcion = {}
        # Cada acepción tiene en realidad una o más (sub)acepciones. Hay que procesarlas todas para obtener
        # la flexión completa. Más información sobre esto en el método de flexionar entrada.
        # Copiamos la acepción porque la vamos a ir modificando y no queremos cambiar los datos de entrada.
        acepcion_copia = copy.deepcopy(acepcion)
        datos_y_derivados = [acepcion_copia.get_datos()] + acepcion_copia.get_acepciones_derivadas()
        for orden_datos, datos in enumerate(datos_y_derivados):
            flexion_subacepcion = {}
            if orden_datos > 0:
                # Así diferenciamos las acep. derivadas
                acepcion_copia.set_n_acepcion(float(acepcion_copia.get_n_acepcion()) + 0.1)
            fuente = u'rae|' + str(acepcion_copia.get_n_entrada()) + u'|' + str(acepcion_copia.get_n_acepcion())

            acepcion_copia.set_datos(datos)
            categoria = acepcion_copia.get_categoria()
            if categoria == VERBO:
                flexion_subacepcion = Flexionador.flexiona_verbo_rae(acepcion_copia, incluye_cliticos)
                pass
            elif categoria == CONJUNCION:
                flexion_subacepcion = Flexionador.flexiona_conjuncion_rae(acepcion_copia)
                pass
            elif categoria in [SUSTANTIVO, ADJETIVO, DETERMINANTE]:  # Los determinantes son adjetivos para la RAE
                flexion_subacepcion = Flexionador.flexiona_sust_adj_det_rae(acepcion_copia, hay_nombres)
                pass
            elif categoria == PRONOMBRE:
                flexion_subacepcion = Flexionador.flexiona_pronombre_rae(acepcion_copia)
                pass
            elif categoria == PREPOSICION:
                flexion_subacepcion = Flexionador.flexiona_preposicion_rae(acepcion_copia)
                pass
            elif categoria == ADVERBIO:
                flexion_subacepcion = Flexionador.flexiona_adverbio_rae(acepcion_copia)
                pass
            elif categoria in [PREFIJO, SUFIJO, ELEMENTO_COMPOSITIVO]:
                flexion_subacepcion = Flexionador.flexiona_afijo_rae(acepcion_copia)
                pass
            elif categoria in [INTERJECCION, ONOMATOPEYA, EXPRESION]:
                # Las expresiones son algo parecido a las interjecciones. Tan solo hay 6 en la RAE: "etcétera", "tirte",
                # "transeat", "vamos", "vide" y "volavérunt". Tienen esta categoría, y ninguna otra.
                flexion_subacepcion = {categoria: {acepcion_copia.get_lema_rae_txt(): [fuente]}}
                pass
            elif categoria == SIGNO:
                flexion_subacepcion = Flexionador.flexiona_signo_rae(acepcion_copia)
            elif False and categoria in [ABREVIATURA, SIGLA, SIMBOLO]:
                etiqueta_eagles = "X" + categoria
                flexion_subacepcion = {etiqueta_eagles: {acepcion_copia.get_lema_rae_txt(): [fuente]}}
                print(acepcion_copia.get_lema_rae_txt(), fuente, u'tiene categoría', etiqueta_eagles)
                pass
            else:
                print(u'Categoría no tratada:', categoria, u'en lema', acepcion_copia.get_lema_rae_txt())
            Flexionador.combina_flexiones(flexion_acepcion, flexion_subacepcion)

        return flexion_acepcion

    @staticmethod
    def flexiona_acepcion_wik(acepcion, ajusta_lema, incluye_cliticos):
        # TODO: este es medianamente compatible con el Wikcionario, pero seguramente no del todo y además incluye cosas
        # que ni le van ni le vienen, y que son exclusivas de las acepciones de la RAE.
        """
        :param incluye_cliticos:
        :param ajusta_lema:
        :param acepcion:
        :return:

        Faltan los nuevos de antropónimo, aumentativos y demás
        acepcion["categoria"]
        acepcion["tipo"]
        acepcion["género"]
        acepcion["número"]
        acepcion["lema_base"]
        acepcion["locución"]
        acepcion["latina"]
        acepcion["lema"]
        acepcion["diminutivo"]
        acepcion["digrafo"]
        acepcion["enclitico"]
        acepcion["lema_base"]
        acepcion["impropia"]
        acepcion["atono"] = True
        acepcion["superlativo"] = True
        acepcion["auxiliar"] = True
        acepcion["impersonal"] = True
        acepcion["intransitivo"] = True
        acepcion["transitivo"] = True
        acepcion["pronominal"] = True
        acepcion["defectivo"] = True
        acepcion["reflexivo"] = True
        """
        flexion = {}
        categoria = acepcion.get_categoria()
        fuente = u'wik|' + str(acepcion.get_n_entrada()) + u'|' + str(acepcion.get_n_acepcion())
        if categoria == VERBO:
            flexion = Flexionador.flexiona_verbo_wik(acepcion, ajusta_lema, incluye_cliticos)
            pass
        elif categoria == CONJUNCION:
            flexion = Flexionador.flexiona_conjuncion_wik(acepcion)  # En realidad no lo flexionamos: sólo asignamos la(s) etiqueta(s)
            pass
        elif categoria in [SUSTANTIVO, ADJETIVO, DETERMINANTE]:  # Los determinantes son adjetivos para la RAE
            flexion = Flexionador.flexiona_sust_adj_det_wik(acepcion, ajusta_lema)
            pass
        elif categoria == PRONOMBRE:
            flexion = Flexionador.flexiona_pronombre_wik(acepcion)
            pass
        elif categoria == PREPOSICION:
            flexion = Flexionador.flexiona_preposicion_wik(acepcion)  # En realidad no lo flexionamos: sólo asignamos la(s) etiqueta(s)
            pass
        elif categoria == ADVERBIO:
            flexion = Flexionador.flexiona_adverbio_wik(acepcion)  # En realidad no lo flexionamos: sólo asignamos la(s) etiqueta(s)
            pass
        elif categoria in [PREFIJO, SUFIJO, ELEMENTO_COMPOSITIVO]:
            flexion = Flexionador.flexiona_afijo_wik(acepcion)
        elif categoria in [INTERJECCION, ONOMATOPEYA, EXPRESION]:
            # Las expresiones son algo parecido a las interjecciones. Tan solo hay 6 en la RAE: "etcétera", "tirte",
            # "transeat", "vamos", "vide" y "volavérunt". Tienen esta categoría, y ninguna otra.
            flexion = {categoria: {acepcion.get_lema_txt(): [fuente]}}
            pass
        elif categoria in [ABREVIATURA, SIGLA, SIMBOLO]:
            etiqueta_eagles = categoria
            flexion = {etiqueta_eagles: {acepcion.get_lema_txt(): [fuente]}}
            pass
        else:
            print(u'Categoría no tratada:', categoria, u'en lema', acepcion.get_lema_txt())

        return flexion

    @staticmethod
    def flexion_a_txt(formas_flexionadas, lema_txt, imprime=False):
        n_formas_total = len([ff for tag, formas in formas_flexionadas.items() for ff in formas])
        txt = u'PLANTILLA DE FLEXIÓN COMPLETA PARA ' + lema_txt + u': ' + str(n_formas_total) + u' formas\n'
        categorias = {SUSTANTIVO: Flexionador.sustantivo_a_txt, ADJETIVO: Flexionador.adjetivo_a_txt,
                      VERBO: Flexionador.verbo_a_txt, ADVERBIO: Flexionador.adverbio_a_txt,
                      PRONOMBRE: Flexionador.pronombre_a_txt, DETERMINANTE: Flexionador.determinante_a_txt}
        for categoria, categoria_a_txt in categorias.items():
            txt += categoria_a_txt({tag: ff for tag, ff in formas_flexionadas.items() if tag[0] == categoria})

        invariables = {tag: ff for tag, ff in formas_flexionadas.items()
                       if tag[0] not in [SUSTANTIVO, ADJETIVO, VERBO, ADVERBIO, PRONOMBRE, DETERMINANTE]}
        categoria = u''
        for tag_invariable, formas_invariable in sorted(invariables.items(), key=lambda tupla: tupla[0]):
            if categoria != tag_invariable[0]:
                categoria = tag_invariable[0]
                n_formas_total = len([forma_txt for etiqueta, formas in invariables.items()
                                      for forma_txt in formas if etiqueta[0] == categoria])
                txt += u'\n' + CATEGORIAS_A_TXT[tag_invariable[0]].upper() + u': ' + str(n_formas_total) + u' formas\n'
            txt += tag_invariable + u': ' + u' / '.join(sorted(formas_invariable)) + u'\n'
        txt += u'\n'
        if imprime:
            print(txt)
        return txt

    '''
    @staticmethod
    def verbo_a_txt_ya_no_puedo_confiar(flexiones):
        u"""

        :type flexiones: {}
        :param flexiones: Es un diccionario cuyas claves son etiquetas EAGLES y los contenidos son diccionarios
                                  que tienen como claves las formas y como contenidos una lista de números de acepción
                                  para los que esta flexión es válida.
        :return:
        """
        if not flexiones:
            return u''
        # Los verbos tienen etiquetas que incluyen cosas que no son estrictamente morfológicas (aunque sí que afecta en
        # las formas que se generan). Son la transitividad, impersonalidad y pronominalidad. Según los valores de estos
        # caracteres, hay formas que no se generan (un verbo intransitivo no tendrá clíticos de od, un verbo impersonal
        # solo tendrá formas de tercera persona y carecerá de imperativo, y un verbo pronominal genera las formas con
        # -se- + clítico de od como formas pronominales y no como un -le(s)- modificado).
        # Para la forma que aparece, estos valores son irrelevantes. Pero son relevantes para saber qué formas deben
        # aparecer o cuáles no.
        tipo = flexiones.keys()[0][:2]

        flexiones_recortadas = {tag[2:12]: value for tag, value in flexiones.items()}

        n_formas_total = len([forma_txt for etiqueta, formas in flexiones_recortadas.items()
                              for forma_txt in formas])
        n_formas_sin_clitico = len([forma_txt
                                    for etiqueta, formas in flexiones_recortadas.items() if etiqueta[5:] == "00000"
                                    for forma_txt in formas])
        n_formas_con_clitico = n_formas_total - n_formas_sin_clitico
        txt = u'\nVERBO: ' + str(n_formas_total) + u' formas (' +\
              str(n_formas_sin_clitico) + u' sin clítico, ' + str(n_formas_con_clitico) + u' con clítico)\n'

        if False:
            # INFINITIVO
            n_formas_infinitivo = len([forma_txt
                                       for etiqueta, formas in flexiones_recortadas.items() if etiqueta[0] == "N"
                                       for forma_txt in formas])
            n_formas_infinitivo_sin_clitico = len([forma_txt
                                                   for etiqueta, formas in flexiones_recortadas.items()
                                                   if etiqueta[0] == "N" and etiqueta[5:] == "00000"
                                                   for forma_txt in formas])
            n_formas_infinitivo_con_clitico = n_formas_infinitivo - n_formas_infinitivo_sin_clitico
            txt += u'INFINITIVO: ' + str(n_formas_infinitivo) + u' formas (' + str(n_formas_infinitivo_sin_clitico) +\
                   u' sin clítico, ' + str(n_formas_infinitivo_con_clitico) + u' con clítico)\n'
            for tag_pronominal in [NA, PRONOMINAL]:
                for tag_oi in ["00", "1S", "2S", "3S", "1P", "2P", "3P"]:
                    for tag_od in ["00", "MS", "MP", "FS", "FP"]:
                        if tag_oi[0] == TERCERA and tag_od != "00":
                            # Si hay clítico de oi y de od, entonces el de oi es "se" y es invariable en número.
                            tag = INF[2:7] + tag_pronominal + "3N" + tag_od
                        else:
                            tag = INF[2:7] + tag_pronominal + tag_oi + tag_od
                        if tag in flexiones_recortadas:
                            formas_txt = u'/'.join(sorted(flexiones[tag].keys()))
                            separador = (u'\n' + (u' ' * 39)) if tag_od == "FS" else u' '
                            txt += separador + (u'|' if tag_od != "00" else u'') +\
                                u' [' + tag + u']: ' + formas_txt + (u' ' * (20 - len(formas_txt)))
                    txt += u'\n'
                txt += u'\n'

            # GERUNDIO
            # Hay verbos, como embaír, que no tienen gerundio
            if tipo + GER[2:] in flexiones:
                n_formas_gerundio = len([forma_txt
                                         for etiqueta, formas in flexiones.items() if etiqueta[2] == "G"
                                         for forma_txt in formas])
                n_formas_gerundio_sin_clitico = len([forma_txt
                                                     for etiqueta, formas in flexiones.items()
                                                     if etiqueta[2] == "G" and etiqueta[8:] == "0000"
                                                     for forma_txt in formas])
                n_formas_gerundio_con_clitico = n_formas_gerundio - n_formas_gerundio_sin_clitico
                txt += u'GERUNDIO: ' + str(n_formas_gerundio) + u' formas (' + str(n_formas_gerundio_sin_clitico) + \
                       u' sin clítico, ' + str(n_formas_gerundio_con_clitico) + u' con clítico)\n'
                # Puede haber más de una forma
                for tag_pronominal in ["0", PRONOMINAL]:
                    for tag_oi in ["00", "1S", "2S", "3S", "1P", "2P", "3P"]:
                        for tag_od in ["00", "MS", "MP", "FS", "FP"]:
                            if tag_oi[0] == "3" and tag_od != "00":
                                tag = tipo + GER[2:7] + tag_pronominal + "3N" + tag_od
                            else:
                                tag = tipo + GER[2:7] + tag_pronominal + tag_oi + tag_od
                            if tag in flexiones:
                                formas_txt = u'/'.join(flexiones[tag].keys())
                                separador = (u'\n' + (u' ' * 39)) if tag_od == "FS" else u' '
                                txt += separador + (u'|' if tag_od != "00" else u'') +\
                                    u' [' + tag + u']: ' + formas_txt + (u' ' * (20 - len(formas_txt)))
                        txt += u'\n'
                    txt += u'\n'

        # PARTICIPIO
        if PAR_SM[2:] in flexiones_recortadas:
            n_formas_participio = len([forma_txt
                                       for etiqueta, formas in flexiones_recortadas.items()
                                       if etiqueta[0] == PARTICIPIO
                                       for forma_txt in formas])
            txt += u'PARTICIPIO: ' + str(n_formas_participio) + u' formas\n'
            if len(flexiones_recortadas[PAR_SM[2:]]) > 1:
                # Tenemos participio irregular
                if flexiones_recortadas[PAR_SM[2:]].keys()[0][-2:] == u'do':
                    participio_regular = flexiones_recortadas[PAR_SM[2:]].keys()[0]
                    participio_irregular = flexiones_recortadas[PAR_SM[2:]].keys()[-1]
                elif flexiones_recortadas[PAR_SM[2:]].keys()[-1][-2:] == u'do':
                    participio_regular = flexiones_recortadas[PAR_SM[2:]].keys()[-1]
                    participio_irregular = flexiones_recortadas[PAR_SM[2:]].keys()[0]
                else:
                    print(lema_txt)
            else:
                participio_regular = flexiones_recortadas[PAR_SM[2:]].keys()[0]
                participio_irregular = u''

            txt += u'  [' + tipo + PAR_SM[2:] + u']: ' + participio_regular + u' \t|'
            txt += u'  [' + tipo + PAR_PM[2:] + u']: ' + participio_regular + u's\n'
            txt += u'  [' + tipo + PAR_SF[2:] + u']: ' + participio_regular[:-1] + u'a \t|'
            txt += u'  [' + tipo + PAR_PF[2:] + u']: ' + participio_regular[:-1] + u'as\n'
            if len(flexiones_recortadas[PAR_SM[2:]]) > 1:
                # Hay participio irregular
                participio_irregular = flexiones_recortadas[PAR_SM[2:]].keys()[0] \
                    if flexiones_recortadas[PAR_SM[2:]].keys()[0][-2:] != u'do' else \
                    flexiones_recortadas[PAR_SM[2:]].keys()[-1]
                txt += u'Participio irregular (preferido como adjetivo):\n'
                txt += u'  [' + tipo + PAR_SM[2:] + u']: ' + participio_irregular + u' \t|'
                txt += u'  [' + tipo + PAR_PM[2:] + u']: ' + participio_irregular + u's\n'
                txt += u'  [' + tipo + PAR_SF[2:] + u']: ' + participio_irregular[:-1] + u'a \t|'
                txt += u'  [' + tipo + PAR_PF[2:] + u']: ' + participio_irregular[:-1] + u'as\n'

        # INDICATIVO Y SUBJUNTIVO
        for codigo_tiempo in [tipo + ct for ct in ["IP", "II", "IS", "IF", "IC", "SP", "SI", "SF"]]:
            tiene_tiempos = False
            if codigo_tiempo[3] == PRESENTE:  # Es un tiempo de presente, así que cambia el modo y separamos
                n_formas_modo = len([forma_txt for etiqueta, formas in flexiones.items()
                                     if etiqueta[2] == codigo_tiempo[2]
                                     for forma_txt in formas])
                txt += u'\n' + NOMBRES_MODOS[codigo_tiempo[2]].upper() + u': ' + str(n_formas_modo) + u' formas\n'
            for codigo_persona in CODIGOS_PERSONAS:
                # Hay verbos impersonales y defectivos y hay tiempos inexistentes de voseo, o del imperativo
                tag = codigo_tiempo + codigo_persona + "000000"
                if tag not in flexiones:
                    continue
                if not tiene_tiempos:
                    # Imprimimos el título del tiempo al inicio
                    txt += NOMBRES_TIEMPOS[codigo_tiempo[3]].upper() + u' de ' + \
                           NOMBRES_MODOS[codigo_tiempo[2]].upper() + u'\n'
                tiene_tiempos = True
                formas_txt = u'/'.join(sorted(flexiones[tag].keys()))
                txt += u'  [' + tag + u']: ' + (u' ' * (12 - len(NOMBRES_PERSONAS[codigo_persona]))) + \
                       NOMBRES_PERSONAS[codigo_persona] + u' ' + formas_txt + u'\n'

        # IMPERATIVO
        n_formas_imperativo = len([forma_txt
                                   for etiqueta, formas in flexiones.items() if etiqueta[2] == "M"
                                   for forma_txt in formas])
        n_formas_imperativo_sin_clitico = len([forma_txt
                                               for etiqueta, formas in flexiones.items()
                                               if etiqueta[2] == "M" and etiqueta[8:] == "0000"
                                               for forma_txt in formas])
        n_formas_imperativo_con_clitico = n_formas_imperativo - n_formas_imperativo_sin_clitico
        txt += u'\nIMPERATIVO: ' + str(n_formas_imperativo) + u' formas (' + str(n_formas_imperativo_sin_clitico) + \
               u' sin clítico, ' + str(n_formas_imperativo_con_clitico) + u' con clítico)'
        codigo_tiempo = tipo + "MP"
        for codigo_persona in CODIGOS_PERSONAS:
            tiene_tiempos = False
            tag = codigo_tiempo + codigo_persona + "000000"
            if tag not in flexiones:
                continue
            if not tiene_tiempos:
                # Imprimimos el título de la persona al inicio
                n_formas_persona = len([forma_txt
                                        for etiqueta, formas in flexiones.items()
                                        if etiqueta[2] == "M" and etiqueta[4:6] == codigo_persona
                                        for forma_txt in formas])
                txt += u'\n' + (u' ' * 18) + NOMBRES_PERSONAS[codigo_persona].upper() + u': ' + str(n_formas_persona) +\
                       u' formas\n'
            for tag_pronominal in ["0", PRONOMINAL]:
                for tag_oi in ["00", "1S", "2S", "3S", "1P", "2P", "3P"]:
                    for tag_od in ["00", "MS", "MP", "FS", "FP"]:
                        if tag_oi[0] == "3" and tag_od != "00":
                            tag = tag[:-5] + tag_pronominal + "3N" + tag_od
                        else:
                            tag = tag[:-5] + tag_pronominal + tag_oi + tag_od
                        if tag in flexiones:
                            separador = (u'\n' if tag_od == "FS" else u'') +\
                                ((u' ' * 39) if (tag_od == "FS" or
                                                 (tag_od == "MS" and ((tag[:8] + tag[8:10].replace("3N", "3S") + "00") not in flexiones)))
                                 else u' ')
                            txt += separador + (u'|' if tag_od != "00" else u'') + \
                                u' [' + tag + u']: ' + u'/'.join(flexiones[tag].keys()) + \
                                   (u' ' * (20 - len(u'/'.join(flexiones[tag].keys()))))
                    txt += u'\n'
                txt += u'\n'
        return txt
    '''

    @staticmethod
    def verbo_a_txt(flexiones):
        u"""

        :type flexiones: {}
        :param flexiones: Es un diccionario cuyas claves son etiquetas EAGLES y los contenidos son diccionarios
                                  que tienen como claves las formas y como contenidos una lista de números de acepción
                                  para los que esta flexión es válida.
        :return:
        """
        if not flexiones:
            return u''
        # Los verbos tienen etiquetas que incluyen cosas que no son estrictamente morfológicas (aunque sí que afecta en
        # las formas que se generan). Son la transitividad, impersonalidad y pronominalidad. Según los valores de estos
        # caracteres, hay formas que no se generan (un verbo intransitivo no tendrá clíticos de od, un verbo impersonal
        # solo tendrá formas de tercera persona y carecerá de imperativo, y un verbo pronominal genera las formas con
        # -se- + clítico de od como formas pronominales y no como un -le(s)- modificado).
        # Para la forma que aparece, estos valores son irrelevantes. Pero son relevantes para saber qué formas deben
        # aparecer o cuáles no.
        # TODO: BORRA ESTO
        # flexiones = {tag[:12]: value for tag, value in flexiones.items()}
        flexiones_recortadas = {}
        for tag, value in flexiones.items():
            tag = tag[:12]
            if tag not in flexiones_recortadas:
                flexiones_recortadas[tag] = value
            else:
                for forma, fuentes in value.items():
                    if forma not in flexiones_recortadas[tag]:
                        flexiones_recortadas[tag][forma] = fuentes
                    else:
                        flexiones_recortadas[tag][forma] = sorted(flexiones_recortadas[tag][forma] + fuentes)
        flexiones = flexiones_recortadas

        tipo = flexiones.keys()[0][:2]
        n_formas_total = len([forma_txt for etiqueta, formas in flexiones.items() for forma_txt in formas])
        n_formas_sin_clitico = len([forma_txt
                                    for etiqueta, formas in flexiones.items() if etiqueta[7:] == "00000"
                                    for forma_txt in formas])
        n_formas_con_clitico = n_formas_total - n_formas_sin_clitico
        txt = u'\nVERBO: ' + str(n_formas_total) + u' formas (' +\
              str(n_formas_sin_clitico) + u' sin clítico, ' + str(n_formas_con_clitico) + u' con clítico)\n'

        # INFINITIVO
        n_formas_infinitivo = len([forma_txt
                                   for etiqueta, formas in flexiones.items() if etiqueta[2] == INFINITIVO
                                   for forma_txt in formas])
        n_formas_infinitivo_sin_clitico = len([forma_txt
                                               for etiqueta, formas in flexiones.items()
                                               if etiqueta[2] == INFINITIVO and etiqueta[7:] == "00000"
                                               for forma_txt in formas])
        n_formas_infinitivo_con_clitico = n_formas_infinitivo - n_formas_infinitivo_sin_clitico
        txt += u'INFINITIVO: ' + str(n_formas_infinitivo) + u' formas (' + str(n_formas_infinitivo_sin_clitico) +\
               u' sin clítico, ' + str(n_formas_infinitivo_con_clitico) + u' con clítico)\n'
        long_max_col_0 = max([len(u' / '.join(formas)) for etiqueta, formas in flexiones.items()
                              if etiqueta[2] + etiqueta[11] == INFINITIVO + NA])
        long_max_col_1 = max([len(u' / '.join(formas)) for etiqueta, formas in flexiones.items()
                              if etiqueta[2] + etiqueta[11] == INFINITIVO + SINGULAR] + [0])
        long_max_col_2 = max([len(u' / '.join(formas)) for etiqueta, formas in flexiones.items()
                              if etiqueta[2] + etiqueta[11] == INFINITIVO + PLURAL] + [0])
        for tag_pronominal in [NA, PRONOMINAL]:
            for tag_oi in ["00", "1S", "2S", "3S", "1P", "2P", "3P"]:
                for tag_od in ["00", "MS", "MP", "FS", "FP"]:
                    if tag_oi[0] == TERCERA and tag_od != "00":
                        # Si hay clítico de oi y de od, entonces el de oi es "se" y es invariable en número.
                        tag = tipo + INF[2:7] + tag_pronominal + "3N" + tag_od
                    else:
                        tag = tipo + INF[2:7] + tag_pronominal + tag_oi + tag_od
                    if tag in flexiones:
                        formas_txt = u' / '.join(sorted(flexiones[tag].keys()))
                        separador = (u'\n' + (u' ' * (7 + 12 + long_max_col_0))) if tag_od == "FS" else u' '
                        txt += separador + (u'|' if tag_od != "00" else u'') + u' [' + tag + u']: ' + formas_txt +\
                            (u' ' * ((long_max_col_0 if tag_od == "00" else
                                      long_max_col_1 if tag_od[1] == SINGULAR else
                                      long_max_col_2) - len(formas_txt)))
                txt += u'\n'
            txt += u'\n'

        # GERUNDIO
        # Hay verbos, como embaír, que no tienen gerundio
        if tipo + GER[2:] in flexiones:
            n_formas_gerundio = len([forma_txt
                                     for etiqueta, formas in flexiones.items() if etiqueta[2] == GERUNDIO
                                     for forma_txt in formas])
            n_formas_gerundio_sin_clitico = len([forma_txt
                                                 for etiqueta, formas in flexiones.items()
                                                 if etiqueta[2] == "G" and etiqueta[7:] == "00000"
                                                 for forma_txt in formas])
            n_formas_gerundio_con_clitico = n_formas_gerundio - n_formas_gerundio_sin_clitico
            txt += u'GERUNDIO: ' + str(n_formas_gerundio) + u' formas (' + str(n_formas_gerundio_sin_clitico) + \
                   u' sin clítico, ' + str(n_formas_gerundio_con_clitico) + u' con clítico)\n'
            long_max_col_0 = max([len(u' / '.join(formas)) for etiqueta, formas in flexiones.items()
                                  if etiqueta[2] + etiqueta[11] == GERUNDIO + NA])
            long_max_col_1 = max([len(u' / '.join(formas)) for etiqueta, formas in flexiones.items()
                                  if etiqueta[2] + etiqueta[11] == GERUNDIO + SINGULAR] + [0])
            # Puede haber más de una forma
            for tag_pronominal in ["0", PRONOMINAL]:
                for tag_oi in ["00", "1S", "2S", "3S", "1P", "2P", "3P"]:
                    for tag_od in ["00", "MS", "MP", "FS", "FP"]:
                        if tag_oi[0] == "3" and tag_od != "00":
                            tag = tipo + GER[2:7] + tag_pronominal + "3N" + tag_od
                        else:
                            tag = tipo + GER[2:7] + tag_pronominal + tag_oi + tag_od
                        if tag in flexiones:
                            formas_txt = u' / '.join(sorted(flexiones[tag].keys()))
                            separador = (u'\n' + (u' ' * (7 + 12 + long_max_col_0))) if tag_od == "FS" else u' '
                            txt += separador + (u'|' if tag_od != "00" else u'') + u' [' + tag + u']: ' + formas_txt + \
                                (u' ' * ((long_max_col_0 if tag_od == "00" else
                                          long_max_col_1 if tag_od[1] == SINGULAR else
                                          long_max_col_2) - len(formas_txt)))
                    txt += u'\n'
                txt += u'\n'

        # PARTICIPIO
        if tipo + PAR_SM[2:] in flexiones:
            n_formas_participio = len([forma_txt
                                       for etiqueta, formas in flexiones.items()
                                       if etiqueta[2] == PARTICIPIO
                                       for forma_txt in formas])
            if len(flexiones[tipo + PAR_SM[2:]]) > 1:
                # Tenemos participio irregular. Se da en 23 verbos: (des)proveer, (re/so)freír, (ben/mal)decir,
                # (re)elegir, (ad/circun/de/in/prein/pre/su/sub/tra/tran)scribir y (re/sobre)imprimir. El que se usa
                # en los tiempos compuestos es "regular", que acaba normalmente en -(i/í)do, o en su defecto, en -ito.
                if flexiones[tipo + PAR_SM[2:]].keys()[0][-2:] == u'do':
                    participio_regular = flexiones[tipo + PAR_SM[2:]].keys()[0]
                    participio_irregular = flexiones[tipo + PAR_SM[2:]].keys()[1]
                elif flexiones[tipo + PAR_SM[2:]].keys()[-1][-2:] == u'do':
                    participio_regular = flexiones[tipo + PAR_SM[2:]].keys()[1]
                    participio_irregular = flexiones[tipo + PAR_SM[2:]].keys()[0]
                elif flexiones[tipo + PAR_SM[2:]].keys()[0][-3:] == u'ito':
                    participio_regular = flexiones[tipo + PAR_SM[2:]].keys()[0]
                    participio_irregular = flexiones[tipo + PAR_SM[2:]].keys()[1]
                elif flexiones[tipo + PAR_SM[2:]].keys()[-1][-3:] == u'ito':
                    participio_regular = flexiones[tipo + PAR_SM[2:]].keys()[1]
                    participio_irregular = flexiones[tipo + PAR_SM[2:]].keys()[0]
                else:
                    print(flexiones[tipo + INF[2:]].keys()[0], u'tiene múltiple participio irregular y ninguno regular:',
                          u', '.join(flexiones[tipo + PAR_SM[2:]].keys()))
                    participio_regular = flexiones[tipo + PAR_SM[2:]].keys()[1]
                    participio_irregular = flexiones[tipo + PAR_SM[2:]].keys()[0]
            else:
                participio_regular = flexiones[tipo + PAR_SM[2:]].keys()[0]
                participio_irregular = u''

            txt += u'PARTICIPIO: ' + str(n_formas_participio) + u' formas\n'
            txt += u'  [' + tipo + PAR_SM[2:] + u']: ' + participio_regular + u' |'
            txt += u' [' + tipo + PAR_PM[2:] + u']: ' + participio_regular + u's\n'
            txt += u'  [' + tipo + PAR_SF[2:] + u']: ' + participio_regular[:-1] + u'a |'
            txt += u' [' + tipo + PAR_PF[2:] + u']: ' + participio_regular[:-1] + u'as\n'
            if participio_irregular:
                # Hay participio irregular
                txt += u'Participio irregular (preferido como adjetivo):\n'
                txt += u'  [' + tipo + PAR_SM[2:] + u']: ' + participio_irregular + u' |'
                txt += u' [' + tipo + PAR_PM[2:] + u']: ' + participio_irregular + u's\n'
                txt += u'  [' + tipo + PAR_SF[2:] + u']: ' + participio_irregular[:-1] + u'a |'
                txt += u' [' + tipo + PAR_PF[2:] + u']: ' + participio_irregular[:-1] + u'as\n'

        # INDICATIVO Y SUBJUNTIVO
        for codigo_tiempo in [tipo + ct for ct in ["IP", "II", "IS", "IF", "IC", "SP", "SI", "SF"]]:
            tiene_tiempos = False
            if codigo_tiempo[3] == PRESENTE:  # Es un tiempo de presente, así que cambia el modo y separamos
                n_formas_modo = len([forma_txt for etiqueta, formas in flexiones.items()
                                     if etiqueta[2] == codigo_tiempo[2]
                                     for forma_txt in formas])
                txt += u'\n' + NOMBRES_MODOS[codigo_tiempo[2]].upper() + u': ' + str(n_formas_modo) + u' formas\n'
            for codigo_persona in CODIGOS_PERSONAS:
                # Hay verbos impersonales y defectivos y hay tiempos inexistentes de voseo, o del imperativo
                tag = codigo_tiempo + codigo_persona + "000000"
                if tag not in flexiones:
                    continue
                if not tiene_tiempos:
                    # Imprimimos el título del tiempo al inicio
                    txt += NOMBRES_TIEMPOS[codigo_tiempo[3]].upper() + u' de ' + \
                           NOMBRES_MODOS[codigo_tiempo[2]].upper() + u'\n'
                tiene_tiempos = True
                formas_txt = u' / '.join(sorted(flexiones[tag].keys()))
                txt += u'  [' + tag + u']: ' + (u' ' * (12 - len(NOMBRES_PERSONAS[codigo_persona]))) +\
                       NOMBRES_PERSONAS[codigo_persona] + u' ' + formas_txt + u'\n'

        # IMPERATIVO
        n_formas_imperativo = len([forma_txt
                                   for etiqueta, formas in flexiones.items() if etiqueta[2] == "M"
                                   for forma_txt in formas])
        n_formas_imperativo_sin_clitico = len([forma_txt
                                               for etiqueta, formas in flexiones.items()
                                               if etiqueta[2] == "M" and etiqueta[7:] == "00000"
                                               for forma_txt in formas])
        n_formas_imperativo_con_clitico = n_formas_imperativo - n_formas_imperativo_sin_clitico
        txt += u'\nIMPERATIVO: ' + str(n_formas_imperativo) + u' formas (' + str(n_formas_imperativo_sin_clitico) + \
               u' sin clítico, ' + str(n_formas_imperativo_con_clitico) + u' con clítico)'
        codigo_tiempo = tipo + "MP"
        for codigo_persona in CODIGOS_PERSONAS:
            tiene_tiempos = False
            tag = codigo_tiempo + codigo_persona + "000000"
            if tag not in flexiones:
                continue
            if not tiene_tiempos:
                # Imprimimos el título de la persona al inicio
                n_formas_persona = len([forma_txt
                                        for etiqueta, formas in flexiones.items()
                                        if etiqueta[2] == "M" and etiqueta[4:6] == codigo_persona
                                        for forma_txt in formas])
                txt += u'\n' + (u' ' * 18) + NOMBRES_PERSONAS[codigo_persona].upper() + u': ' + str(n_formas_persona) +\
                       u' formas\n'
            long_max_col_0 = max([len(u' / '.join(formas)) for etiqueta, formas in flexiones.items()
                                  if etiqueta[2] + etiqueta[4:6] + etiqueta[11] == IMPERATIVO + codigo_persona + NA])
            long_max_col_1 = max([len(u' / '.join(formas)) for etiqueta, formas in flexiones.items()
                                  if etiqueta[2] + etiqueta[4:6] + etiqueta[11] ==
                                  IMPERATIVO + codigo_persona + SINGULAR] + [0])
            for tag_pronominal in ["0", PRONOMINAL]:
                for tag_oi in ["00", "1S", "2S", "3S", "1P", "2P", "3P"]:
                    for tag_od in ["00", "MS", "MP", "FS", "FP"]:
                        if tag_oi[0] == "3" and tag_od != "00":
                            tag = tag[:-5] + tag_pronominal + "3N" + tag_od
                        else:
                            tag = tag[:-5] + tag_pronominal + tag_oi + tag_od
                        if tag in flexiones:
                            formas_txt = u' / '.join(sorted(flexiones[tag].keys()))
                            separador = (u'\n' if tag_od == "FS" else u'') +\
                                ((u' ' * (7 + 12 + long_max_col_0))
                                 if (tag_od == "FS" or
                                     (tag_od == "MS" and
                                      ((tag[:8] + tag[8:10].replace("3N", "3S") + "00") not in flexiones))) else u' ')
                            txt += separador + (u'|' if tag_od != "00" else u'') + u' [' + tag + u']: ' + formas_txt + \
                                (u' ' * ((long_max_col_0 if tag_od == "00" else
                                          long_max_col_1 if tag_od[1] == SINGULAR else
                                          long_max_col_2) - len(formas_txt)))
                    txt += u'\n'
                txt += u'\n'
        return txt

    @staticmethod
    def adverbio_a_txt(flexiones):
        if not flexiones:
            return u''
        n_formas_total = len([forma_txt for etiqueta, formas in flexiones.items() for forma_txt in formas])
        txt = u'\nADVERBIO: ' + str(n_formas_total) + u' formas\n'

        etiquetas_existentes = flexiones.keys()
        formas_impresas = 0
        etiquetas_mostradas = []
        for uso in [NA, POCO_USADO, DESUSADO]:
            for tipo in [GENERAL, NEGATIVO, COMPARATIVO, AFIRMATIVO, CUANTITATIVO, DUBITATIVO, LOCATIVO,
                         PRINCIPAL, ORDINAL, TEMPORAL, INTERROGATIVO, RELATIVO, DEMOSTRATIVO, INDEFINIDO, EXCLAMATIVO, DISTRIBUTIVO]:
                txt_linea = u''
                for grado in ["0", SUPERLATIVO, COMPARATIVO]:
                    for etiqueta in [tag for tag in etiquetas_existentes
                                     if tag[1] == tipo and
                                     tag[2] == grado and
                                     tag[3] == uso]:
                        txt_linea += etiqueta + u': ' + u' / '.join(sorted(flexiones[etiqueta].keys())) + u'\t'
                        formas_impresas += 1
                        etiquetas_mostradas.append(etiqueta)
                if txt_linea:
                    txt += txt_linea + u'\n'

        if formas_impresas != len(flexiones):
            print(u'Hay etiquetas que no hemos sabido colocar:\n',
                  u'\n'.join([t + u': ' + u'/'.join(flexiones[t])
                              for t in etiquetas_existentes if t not in etiquetas_mostradas]))
        return txt

    @staticmethod
    def sustantivo_a_txt(flexiones):
        if not flexiones:
            return u''
        n_formas_total = len([forma_txt for etiqueta, formas in flexiones.items() for forma_txt in formas])
        txt = u'\nSUSTANTIVO: ' + str(n_formas_total) + u' formas\n'

        etiquetas_existentes = flexiones.keys()
        formas_impresas = 0
        etiquetas_mostradas = []
        for uso in [NA, POCO_USADO, DESUSADO]:
            for suf in ["0", APOCOPE, AUMENTATIVO, DIMINUTIVO]:
                for genero in [AMBIGUO, MASCULINO, FEMENINO, NEUTRO]:
                    txt_linea = u''
                    for numero in [SINGULAR, PLURAL, INVARIABLE]:
                        for etiqueta in [tag for tag in etiquetas_existentes
                                         if tag[2] == genero and
                                         tag[3] == numero and
                                         tag[6] == suf and
                                         tag[8] == uso]:
                            txt_linea += etiqueta + u': ' + u' / '.join(sorted(flexiones[etiqueta].keys())) + u'\t'
                            formas_impresas += 1
                            etiquetas_mostradas.append(etiqueta)
                    if txt_linea:
                        txt += txt_linea + u'\n'

        if formas_impresas != len(flexiones):
            print(u'Hay etiquetas que no hemos sabido colocar:\n',
                  u'\n'.join([t + u': ' + u'/'.join(flexiones[t])
                              for t in etiquetas_existentes if t not in etiquetas_mostradas]))
        return txt

    @staticmethod
    def adjetivo_a_txt(flexiones):
        if not flexiones:
            return u''
        n_formas_total = len([forma_txt for etiqueta, formas in flexiones.items() for forma_txt in formas])
        txt = u'\nADJETIVO: ' + str(n_formas_total) + u' formas\n'

        etiquetas_existentes = flexiones.keys()
        formas_impresas = 0
        etiquetas_mostradas = []
        for uso in [NA, POCO_USADO, DESUSADO]:
            for tipo in [CALIFICATIVO, GENTILICIO, SUSTANTIVADO, DE_PADECIMIENTO, DE_SUSTANTIVO, DE_VERBO,
                         COMPARATIVO]:
                for grado in ["0", SUPERLATIVO, COMPARATIVO]:
                    for suf in ["0", APOCOPE, AUMENTATIVO, DIMINUTIVO]:
                        for genero in [AMBIGUO, MASCULINO, FEMENINO, NEUTRO]:
                            txt_linea = u''
                            for numero in [SINGULAR, PLURAL, INVARIABLE]:
                                for etiqueta in [tag for tag in etiquetas_existentes
                                                 if tag[1] == tipo and
                                                 tag[2] == grado and
                                                 tag[3] == genero and
                                                 tag[4] == numero and
                                                 tag[6] == suf and
                                                 tag[7] == uso]:
                                    txt_linea += etiqueta + u': ' + u' / '.join(sorted(flexiones[etiqueta].keys())) + u'\t'
                                    formas_impresas += 1
                                    etiquetas_mostradas.append(etiqueta)
                            if txt_linea:
                                txt += txt_linea + u'\n'

        if formas_impresas != len(flexiones):
            print(u'Hay etiquetas que no hemos sabido colocar:\n',
                  u'\n'.join([t + u': ' + u'/'.join(flexiones[t])
                              for t in etiquetas_existentes if t not in etiquetas_mostradas]))
        return txt

    @staticmethod
    def determinante_a_txt(flexiones):
        if not flexiones:
            return u''
        n_formas_total = len([forma_txt for etiqueta, formas in flexiones.items() for forma_txt in formas])
        txt = u'\nDETERMINANTE: ' + str(n_formas_total) + u' formas\n'

        etiquetas_existentes = flexiones.keys()
        formas_impresas = 0
        etiquetas_mostradas = []
        for uso in [NA, POCO_USADO, DESUSADO]:
            for tipo in [DEMOSTRATIVO, POSESIVO, INTERROGATIVO, EXCLAMATIVO, INDEFINIDO,
                         ARTICULO_D, ORDINAL, CARDINAL, ARTICULO_I, RELATIVO, RELATIVO_POSESIVO]:
                for poseedor in [NA, SINGULAR, PLURAL, INVARIABLE]:
                    for suf in [NA, APOCOPE]:
                        for persona in [NA, PRIMERA, SEGUNDA, TERCERA]:
                            for genero in [AMBIGUO, MASCULINO, FEMENINO, NEUTRO]:
                                txt_linea = u''
                                for numero in [SINGULAR, PLURAL, INVARIABLE]:
                                    for etiqueta in [tag for tag in etiquetas_existentes
                                                     if tag[1] == tipo and
                                                     tag[2] == persona and
                                                     tag[3] == genero and
                                                     tag[4] == numero and
                                                     tag[5] == poseedor and
                                                     tag[6] == suf and
                                                     tag[7] == uso]:
                                        txt_linea += etiqueta + u': ' + \
                                                     u' / '.join(sorted(flexiones[etiqueta].keys())) + u'\t'
                                        formas_impresas += 1
                                        etiquetas_mostradas.append(etiqueta)
                                if txt_linea:
                                    txt += txt_linea + u'\n'

        if formas_impresas != len(flexiones):
            print(u'Hay etiquetas que no hemos sabido colocar:\n',
                  u'\n'.join([t + u': ' + u'/'.join(flexiones[t])
                              for t in etiquetas_existentes if t not in etiquetas_mostradas]))
        return txt

    @staticmethod
    def pronombre_a_txt(flexiones):
        if not flexiones:
            return u''
        n_formas_total = len([forma_txt for etiqueta, formas in flexiones.items() for forma_txt in formas])
        txt = u'\nPRONOMBRE: ' + str(n_formas_total) + u' formas\n'

        etiquetas_existentes = flexiones.keys()
        formas_impresas = 0
        etiquetas_mostradas = []
        for uso in [NA, POCO_USADO, DESUSADO]:
            for tipo in [PERSONAL, DEMOSTRATIVO, INDEFINIDO, INTERROGATIVO,
                         RELATIVO, EXCLAMATIVO, CARDINAL, COMPARATIVO]:
                for caso in [NA, NOMINATIVO, ACUSATIVO, DATIVO, OBLICUO]:
                    for genero in [AMBIGUO, MASCULINO, FEMENINO, NEUTRO]:
                        txt_linea = u''
                        for numero in [SINGULAR, PLURAL, INVARIABLE]:
                            for preposicionalidad in [NA, INDISTINTO, PREPOSICIONAL, AMALGAMADO]:
                                for reflexividad in [NA, INDISTINTO, REFLEXIVO]:
                                    for politeness in [NA, POLITE]:
                                        for etiqueta in [tag for tag in etiquetas_existentes
                                                         if tag[1] == tipo and
                                                         tag[3] == genero and
                                                         tag[4] == numero and
                                                         tag[5] == caso and
                                                         tag[6] == preposicionalidad and
                                                         tag[7] == politeness and
                                                         tag[8] == reflexividad and
                                                         tag[9] == uso]:
                                            txt_linea += etiqueta + u': ' + \
                                                         u' / '.join(sorted(flexiones[etiqueta].keys())) + u'\t'
                                            formas_impresas += 1
                                            etiquetas_mostradas.append(etiqueta)
                        if txt_linea:
                            txt += txt_linea + u'\n'

        if formas_impresas != len(flexiones):
            print(u'Hay etiquetas que no hemos sabido colocar:\n',
                  u'\n'.join([t + u': ' + u'/'.join(flexiones[t])
                              for t in etiquetas_existentes if t not in etiquetas_mostradas]))
        return txt














    @staticmethod
    def flexiona_pronombre(acepcion, ajusta_lema=True):
        if type(acepcion) == AcepcionWik:
            return Flexionador.flexiona_pronombre_wik(acepcion)
        else:
            return Flexionador.flexiona_pronombre_rae(acepcion)

    @staticmethod
    def flexiona_pronombre_rae(acepcion):
        lema_rae_txt = acepcion.get_lema_rae_txt()
        fuente = u'rae|' + str(acepcion.get_n_entrada()) + u'|' + str(acepcion.get_n_acepcion())
        tipos = acepcion.get_tipos()
        if not tipos:
            # Solo sucede en 4 lemas: "ídem", "uno, na", "otro, tra", "quequier", y también en los adjetivos
            # numerales cardinales, que tienen la acepción derivada como pronombre y no incluyen tipo.
            tipos = [INDEFINIDO]
            # print(lema_rae_txt, u'no tiene tipo', fuente)
        elif len(tipos) > 1:
            print(lema_rae_txt, u'tiene más de un tipo', tipos)

        flexion_completa = {}
        if tipos[0] not in [PERSONAL, INDEFINIDO, RELATIVO, INTERROGATIVO, EXCLAMATIVO, COMPARATIVO, DEMOSTRATIVO,
                            CARDINAL]:
            print(lema_rae_txt, u'tiene tipo desconocido', tipos[0], fuente)
            return flexion_completa

        if acepcion.get_es_pronombre_amalgamado() or acepcion.get_es_forma_atona() or acepcion.get_es_forma_tonica():
            # Es una forma "declinada" de algún pronombre. No interesa porque los propios pronombres ya
            # incluyen esta información.
            # print(lema_rae_txt, u'aparecerá en otro lema. Pasamos')
            return flexion_completa  # Vacío
        if lema_rae_txt == u'cualesquier':
            # Esto en realidad es un pequeño error por la irregularidad de plural apocopado
            return flexion_completa  # Vacío

        formas_expandidas = acepcion.get_formas_expandidas()
        formas_plural = acepcion.get_formas_plural() if acepcion.get_formas_plural() else\
            [Flexionador.pluraliza(f, formas_expandidas) for f in formas_expandidas]

        generos_disponibles = acepcion.get_generos_disponibles()
        if not generos_disponibles:
            generos_disponibles = [MASCULINO, FEMENINO]
        numeros_disponibles = acepcion.get_numeros_disponibles()
        if not numeros_disponibles:
            if lema_rae_txt in [u'ge', u'idem']:
                numeros_disponibles = [INVARIABLE]
            elif lema_rae_txt in [u'acá', u'nadi', u'nonada', u'quequier', u'qui', u'talque']:
                numeros_disponibles = [SINGULAR]
            elif MASCULINO in generos_disponibles or FEMENINO in generos_disponibles:
                numeros_disponibles = [SINGULAR, PLURAL]
            else:
                numeros_disponibles = [SINGULAR]

        persona = acepcion.get_persona()
        encabezado_eagles = PRONOMBRE + tipos[0] + persona
        # El pronombre "vusco" es equivalente a "convusco". Este pie es para el lema, con lo que solo hay pronombres
        # de nominativo o estas formas raras y desusadas, a las que cambiamos el lema
        caso = "0" if tipos[0] != PERSONAL else OBLICUO if (u'co' in lema_rae_txt) else NOMINATIVO
        if False:  # if ajusta_lema and caso == OBLICUO:  # En realidad, cada lema genera sus formas y esto no funciona
            if u'vus' in lema_rae_txt:  # convusco, vusco
                lema_rae_txt = u'vosotros, tras'
            elif u'nos' in lema_rae_txt:  # connosco
                lema_rae_txt = u'nosotros, tras'
            else:  # comigo
                lema_rae_txt = u'yo'
            acepcion.set_lema_rae_txt(lema_rae_txt)
        elif lema_rae_txt in [u'vusted', u'voacé']:
            lema_rae_txt = u'usted'
            acepcion.set_lema_rae_txt(lema_rae_txt)
        preposicionalidad = AMALGAMADO if caso == OBLICUO else\
            INDISTINTO if tipos[0] == PERSONAL and SINGULAR not in generos_disponibles else "0"
        politeness = POLITE if lema_rae_txt in [u'usted', u'vusted'] or\
            (lema_rae_txt == u'vos' and PLURAL in numeros_disponibles) else "0"
        reflexividad = "0" if tipos[0] != PERSONAL or SINGULAR in generos_disponibles or caso == OBLICUO else INDISTINTO
        uso = DESUSADO if acepcion.get_es_desusado() else\
            POCO_USADO if acepcion.get_es_poco_usado() or\
            (lema_rae_txt == u'vos' and PLURAL in numeros_disponibles) else "0"
        pie_eagles = caso + preposicionalidad + politeness + reflexividad + uso
        # Comenzamos haciendo las variaciones clásicas ("nominales") en género y número.
        # Podemos tener de 1 a 5 formas (incluyendo el neutro singular)
        flexion = {}
        if len(generos_disponibles) == 1 or (len(generos_disponibles) == 2 and len(formas_expandidas) == 1):
            genero = generos_disponibles[0] if len(generos_disponibles) == 1 else AMBIGUO
            pos = -1 if genero == FEMENINO else 0  # Posición en las formas expandidas y formas plural
            if formas_expandidas[0] == formas_plural[0][0]:
                # Invariante en número
                numero = INVARIABLE if len(numeros_disponibles) == 2 else numeros_disponibles[0]
                flexion[encabezado_eagles + genero + numero + pie_eagles] = [formas_expandidas[pos]]
            else:
                if SINGULAR in numeros_disponibles:
                    flexion[encabezado_eagles + genero + SINGULAR + pie_eagles] = [formas_expandidas[pos]]
                if PLURAL in numeros_disponibles:
                    # Algunas formas, como "connosco" son plurales únicamente, y habremos creado un "connoscos" que no
                    # es válido.
                    flexion[encabezado_eagles + genero + PLURAL + pie_eagles] =\
                        (formas_plural[pos]
                         if caso != OBLICUO and (len(numeros_disponibles) > 1 or formas_expandidas[pos][-1] != u's')
                         else [formas_expandidas[pos]])
        elif len(generos_disponibles) >= 2 and len(formas_expandidas) == 2:
            # Se cubren las cuatro combinaciones de variantes en género y número, pero pueden ser coincidentes
            if MASCULINO not in generos_disponibles or FEMENINO not in generos_disponibles:
                print(lema_rae_txt, u'tiene 2 géneros disponibles, pero no son masculino y femenino')
            # Hay formas diferentes para masculino y femenino. A la fuerza sus plurales son distintos
            if formas_plural[0][0] == formas_plural[1][0]:
                print(lema_rae_txt, u'tiene 2 géneros disponibles, pero comparten el plural')
            if SINGULAR in numeros_disponibles:
                flexion[encabezado_eagles + MASCULINO + SINGULAR + pie_eagles] = [formas_expandidas[0]]
                flexion[encabezado_eagles + FEMENINO + SINGULAR + pie_eagles] = [formas_expandidas[1]]
            if PLURAL in numeros_disponibles:
                flexion[encabezado_eagles + MASCULINO + PLURAL + pie_eagles] = formas_plural[0]
                flexion[encabezado_eagles + FEMENINO + PLURAL + pie_eagles] = formas_plural[1]
            if NEUTRO in generos_disponibles:
                flexion[encabezado_eagles + NEUTRO + SINGULAR + pie_eagles] = [acepcion.get_neutro_txt()]
        else:
            # Aquí llegamos con pronombres desusados como "ge" (se) y "lle" (le) o con "que".
            # Tienen 3 géneros y una única forma.
            if lema_rae_txt == u'ge':
                # Equivale al "le" (variante de "se" no reflexivo)
                flexion[encabezado_eagles + AMBIGUO + INVARIABLE + DATIVO + "0" + politeness + "0" + uso] = [u'ge']
                if False:  # if ajusta_lema:
                    acepcion.set_lema_rae_txt(u'él, ella')
            elif lema_rae_txt == u'lle':
                # Equivale al "le" ("les")
                flexion[encabezado_eagles + AMBIGUO + SINGULAR + DATIVO + "0" + politeness + "0" + uso] = [u'lle']
                flexion[encabezado_eagles + AMBIGUO + PLURAL + DATIVO + "0" + politeness + "0" + uso] = [u'lles']
                if False:  # if ajusta_lema:
                    acepcion.set_lema_rae_txt(u'él, ella')
            elif lema_rae_txt == u'que':
                flexion[encabezado_eagles + AMBIGUO + INVARIABLE + pie_eagles] = [lema_rae_txt]
                flexion[encabezado_eagles + NEUTRO + INVARIABLE + pie_eagles] = [lema_rae_txt]
            else:
                print(lema_rae_txt, u'tiene', len(generos_disponibles), u'géneros disponibles:', generos_disponibles)

        if lema_rae_txt in [u'este, ta', u'ese, sa', u'aquel, lla']:
            # Sorprendentemente los pronombres demostrativos no tienen una entrada en la RAE con tilde.
            # En la sección de morfología se dice que las acepciones como pronombre pueden llevar tilde.
            # Creamos las versiones con tilde diacrítica (todas las que haya menos la neutra).
            for etiqueta_eagles, formas_txt in flexion.items():
                if etiqueta_eagles[3] != NEUTRO:
                    flexion[etiqueta_eagles].append(Palabra(palabra_texto=formas_txt[0],
                                                            calcula_alofonos=False,
                                                            organiza_grafemas=True).set_tilde(con_tilde=True))

        # Comienza el rock and roll. Metemos las formas de caso, lo que implica el cálculo de los caracteres
        # de la etiqueta para el caso, preposicionalidad y reflexividad.
        if acepcion.get_forma_tonica_txt():
            # print(u'Forma tónica de', lema_rae_txt + u':', acepcion.get_forma_tonica_txt())
            numero = numeros_disponibles[0] if len(numeros_disponibles) == 1 else INVARIABLE
            flexion[encabezado_eagles + AMBIGUO + numero + OBLICUO + PREPOSICIONAL + politeness +
                    (REFLEXIVO if persona == TERCERA else INDISTINTO) + uso] = [acepcion.get_forma_tonica_txt()]
        if acepcion.get_forma_amalgamada_txt():  # OBLICUO
            # print(u'Forma amalgamada de', lema_rae_txt + u':', acepcion.get_forma_amalgamada_txt())
            numero = numeros_disponibles[0] if len(numeros_disponibles) == 1 else INVARIABLE
            flexion.setdefault(encabezado_eagles + AMBIGUO + numero + OBLICUO + AMALGAMADO +
                               politeness + "0" + uso, []).append(acepcion.get_forma_amalgamada_txt())
        for forma_atona in acepcion.get_formas_atonas_txt():  # ACUSATIVO
            # print(u'Forma átona de', lema_rae_txt + u':', acepcion.get_formas_atonas_txt())
            # Para 1ª y 2ª persona hay una única forma átona: me, te, nos, os. En 3ª se tienen 4 (que se
            # expanden en entre 1 y 4 formas): le, se (variante de le), "lo, la", se (reflexivo)
            if persona != TERCERA:
                flexion[encabezado_eagles + AMBIGUO + numeros_disponibles[0] + ACUSATIVO + "0" + politeness +
                        INDISTINTO + uso] = [forma_atona]
            elif forma_atona == u'le':
                flexion[encabezado_eagles + AMBIGUO + SINGULAR + DATIVO + "0" + politeness + "0" + uso] = [u'le']
                flexion[encabezado_eagles + AMBIGUO + PLURAL + DATIVO + "0" + politeness + "0" + uso] = [u'les']
                # Metemos el leísmo, que en la RAE se acepta (Usado también como acusativo), pero ponemos
                # poco usado. Solo consideramos el leísmo masculino (es decir, poner le en vez de lo).
                flexion[encabezado_eagles + MASCULINO + SINGULAR + ACUSATIVO + "0" + politeness + "0" + POCO_USADO] =\
                    [u'le']
                flexion[encabezado_eagles + MASCULINO + PLURAL + ACUSATIVO + "0" + politeness + "0" + POCO_USADO] =\
                    [u'les']
            elif forma_atona == u'se':
                # TODO: hay que diferenciar el se que viene de le del que es reflexivo
                # No hay leísmo posible.
                flexion[encabezado_eagles + AMBIGUO + INVARIABLE + DATIVO + "0" + politeness + "0" + uso] = [u'se']
                flexion[encabezado_eagles + AMBIGUO + INVARIABLE + ACUSATIVO + "0" + politeness + REFLEXIVO + uso] =\
                    [u'se']
            else:  # Tenemos "lo, la"
                flexion[encabezado_eagles + MASCULINO + SINGULAR + ACUSATIVO + "0" + politeness + "0" + uso] = [u'lo']
                flexion[encabezado_eagles + NEUTRO + SINGULAR + ACUSATIVO + "0" + politeness + "0" + uso] = [u'lo']
                flexion[encabezado_eagles + MASCULINO + PLURAL + ACUSATIVO + "0" + politeness + "0" + uso] = [u'los']
                flexion[encabezado_eagles + FEMENINO + SINGULAR + ACUSATIVO + "0" + politeness + "0" + uso] = [u'la']
                flexion[encabezado_eagles + FEMENINO + PLURAL + ACUSATIVO + "0" + politeness + "0" + uso] = [u'las']
                # Metemos el laísmo pero no el loísmo (ninguno está aceptado en la RAE)
                flexion[encabezado_eagles + FEMENINO + SINGULAR + DATIVO + "0" + politeness + "0" + POCO_USADO] =\
                    [u'la']
                flexion[encabezado_eagles + FEMENINO + PLURAL + DATIVO + "0" + politeness + "0" + POCO_USADO] = [u'las']
        if not flexion:
            print(lema_rae_txt, u'no tiene flexión alguna')

        # Las metemos en el diccionario de flexión con el formato de etiquetas-formas-fuentes
        flexion_completa = {etiqueta_eagles: {forma_txt: [fuente] for forma_txt in formas_txt}
                            for etiqueta_eagles, formas_txt in flexion.items()}
        return flexion_completa

    @staticmethod
    def flexiona_pronombre_wik(acepcion):
        print(u'Hay que modificar flexiona_pronombre_wik:', acepcion.get_lema_txt())
        datos = acepcion.get_datos()
        for inflect in acepcion.get_inflects():
            if u'adj' in inflect:
                datos["categoria"] = ADJETIVO
                datos["inflects"] = [inflect]
                flexion_previa = Flexionador.flexiona_sust_adj_det_wik(acepcion, ajusta_lema=False)
                flexion = {PRONOMBRE + INDEFINIDO + NA + etiqueta[3:5] + 5 * NA: datos
                           for etiqueta, datos in flexion_previa.items()}
                break
            elif u'sust' in inflect:
                datos["categoria"] = SUSTANTIVO
                datos["inflects"] = [inflect]
                flexion_previa = Flexionador.flexiona_sust_adj_det_wik(acepcion, ajusta_lema=False)
                flexion = {PRONOMBRE + INDEFINIDO + NA + etiqueta[2:4] + 5 * NA: datos
                           for etiqueta, datos in flexion_previa.items()}
                break
        else:
            fuente = u'wik|' + str(acepcion.get_n_entrada()) + u'|' + str(acepcion.get_n_acepcion())
            flexion = {PRONOMBRE + 9 * NA: {acepcion.get_lema_txt(): [fuente]}}
        '''
        if True:
            pass
        elif u'personal' in etiqueta:
            set_tipo(datos, PERSONAL)
            if u'átono' in etiqueta:
                datos["atono"] = True
        elif u'demostrativo' in etiqueta:
            set_tipo(datos, DEMOSTRATIVO)
            if u'masculino' in etiqueta:
                set_genero(datos, MASCULINO)
            elif u'neutro' in etiqueta:
                set_genero(datos, NEUTRO)

        elif u'indeterminado' in etiqueta:
                set_tipo(datos, INDETERMINADO)
        elif u'interrogativo' in etiqueta:
            set_tipo(datos, INTERROGATIVO)
        elif u'relativo' in etiqueta:
            set_tipo(datos, RELATIVO)
        elif u'exclamación' in etiqueta:
            set_tipo(datos, EXCLAMACION)
        '''
        return flexion

    @staticmethod
    def flexiona_signo(acepcion):
        if type(acepcion) == AcepcionWik:
            return Flexionador.flexiona_signo_wik(acepcion)
        else:
            return Flexionador.flexiona_signo_rae(acepcion)

    @staticmethod
    def flexiona_signo_rae(acepcion):
        lema_rae_txt = acepcion.get_lema_rae_txt()
        fuente = u'rae|' + str(acepcion.get_n_entrada()) + u'|' + str(acepcion.get_n_acepcion())
        if lema_rae_txt == u':':
            flexion = {SIGNO + DOS_PUNTOS + NA + NA: {lema_rae_txt: [fuente]}}
        elif lema_rae_txt == u',':
            flexion = {SIGNO + COMA + NA + NA: {lema_rae_txt: [fuente]}}
        elif lema_rae_txt == u'}':
            flexion = {SIGNO + LLAVE + APERTURA + NA: {u'{': [fuente]},
                       SIGNO + LLAVE + CIERRE + NA: {lema_rae_txt: [fuente]}}
        elif lema_rae_txt == u'etc':
            flexion = {SIGNO + ETC + NA + NA: {lema_rae_txt: [fuente],
                                               u'etc.': [fuente]}}
        elif lema_rae_txt == u'!':
            flexion = {SIGNO + ADMIRACION + APERTURA + NA: {u'¡': [fuente]},
                       SIGNO + ADMIRACION + CIERRE + NA: {lema_rae_txt: [fuente]}}
        elif lema_rae_txt == u'-':
            flexion = {SIGNO + GUION + NA + NA: {forma: [fuente] for forma in u'-‒–−­—―'}}
        elif lema_rae_txt == u')':
            flexion = {SIGNO + PARENTESIS + APERTURA + NA: {u'(': [fuente]},
                       SIGNO + PARENTESIS + CIERRE + NA: {lema_rae_txt: [fuente]}}
        elif lema_rae_txt == u'%':
            flexion = {SIGNO + TANTO_POR_CIENTO + NA + NA: {lema_rae_txt: [fuente]}}
        elif lema_rae_txt == u'.':
            flexion = {SIGNO + PUNTO + NA + NA: {lema_rae_txt: [fuente]}}
        elif lema_rae_txt == u'?':
            flexion = {SIGNO + INTERROGACION + APERTURA + NA: {u'¿': [fuente]},
                       SIGNO + INTERROGACION + CIERRE + NA: {lema_rae_txt: [fuente]}}
        elif lema_rae_txt == u'"':
            flexion = {SIGNO + COMILLAS + NA + NA: {lema_rae_txt: [fuente]},
                       SIGNO + COMILLAS + APERTURA + NA: {forma: [fuente] for forma in u'“«'},
                       SIGNO + COMILLAS + CIERRE + NA: {forma: [fuente] for forma in u'”»'}}
        elif lema_rae_txt == u';':
            flexion = {SIGNO + PUNTO_Y_COMA + NA + NA: {lema_rae_txt: [fuente]}}
        elif lema_rae_txt == u'|':
            flexion = {SIGNO + BARRA + NA + NA: {lema_rae_txt: [fuente]},
                       SIGNO + BARRA + APERTURA + NA: {u'/': [fuente]},
                       SIGNO + BARRA + CIERRE + NA: {u'\\': [fuente]}}
        elif lema_rae_txt == u']':
            flexion = {SIGNO + CORCHETE + APERTURA + NA: {u'[': [fuente]},
                       SIGNO + CORCHETE + CIERRE + NA: {lema_rae_txt: [fuente]}}
        elif lema_rae_txt == u'…':
            flexion = {SIGNO + PUNTOS_SUSPENSIVOS + NA + NA: {lema_rae_txt: [fuente],
                                                              u'...': [fuente]}}
        elif lema_rae_txt == u'>':
            flexion = {SIGNO + COMPARADOR + APERTURA + NA: {u'<': [fuente]},
                       SIGNO + COMPARADOR + CIERRE + NA: {lema_rae_txt: [fuente]}}
        elif lema_rae_txt == u"'":
            flexion = {SIGNO + COMILLA + NA + NA: {lema_rae_txt: [fuente]},
                       SIGNO + COMILLA + APERTURA + NA: {forma: [fuente] for forma in u'‘`'},
                       SIGNO + COMILLA + CIERRE + NA: {forma: [fuente] for forma in u'’´'}}
        elif lema_rae_txt == u'°':
            flexion = {SIGNO + PUNTUACION + NA + NA: {lema_rae_txt: [fuente],
                                                      u'º': [fuente],
                                                      u'ª': [fuente]}}
        elif lema_rae_txt == u'·':
            flexion = {SIGNO + PUNTUACION + NA + NA: {lema_rae_txt: [fuente],
                                                      u'•': [fuente]}}
        elif lema_rae_txt in u'@&#':
            flexion = {SIGNO + PUNTUACION + NA + NA: {lema_rae_txt: [fuente]}}
        else:
            print(u'Estamos flexionando un signo extraño:', lema_rae_txt)
            flexion = {SIGNO + PUNTUACION + NA + NA: {lema_rae_txt: [fuente]}}
        return flexion

    @staticmethod
    def flexiona_signo_wik(acepcion):
        print(u'Hay que modificar flexiona_signo_wik')
        return {}

    @staticmethod
    def flexiona_conjuncion(acepcion):
        if type(acepcion) == AcepcionWik:
            return Flexionador.flexiona_conjuncion_wik(acepcion)
        else:
            return Flexionador.flexiona_conjuncion_rae(acepcion)

    @staticmethod
    def flexiona_conjuncion_rae(acepcion):
        tipos = acepcion.get_tipos()
        fuente = u'rae|' + str(acepcion.get_n_entrada()) + u'|' + str(acepcion.get_n_acepcion())
        if not tipos:
            # print(lema_txt, u'no tiene tipos')
            tipos = ["0"]
        elif len(tipos) > 1:
            print(u'La conjunción', acepcion.get_lema_rae_txt(), u'tiene más de un tipo')

        uso = DESUSADO if acepcion.get_es_desusado() else POCO_USADO if acepcion.get_es_poco_usado() else "0"
        subtipo = tipos[0] if tipos else "0"
        # En realidad en el DRAE no vienen conjunciones explicativas, ni consecutivas o condicionales, porque
        # suelen ser locuciones
        tipo = COORDINADA if subtipo in [COPULATIVA, DISYUNTIVA, DISTRIBUTIVA, ADVERSATIVA, EXPLICATIVA] else \
            SUBORDINADA if subtipo in [CONSECUTIVA, CAUSAL, FINAL, CONCESIVA, TEMPORAL, CONDICIONAL, ILATIVA] else "0"
        etiqueta_eagles = CONJUNCION + tipo + subtipo + uso
        flexion_completa = {etiqueta_eagles: {acepcion.get_formas_expandidas()[0]: [fuente]}}

        return flexion_completa

    @staticmethod
    def flexiona_conjuncion_wik(acepcion):
        if acepcion in CONJS_COPULATIVAS:
            etiqueta_eagles = "CCC"
        elif acepcion in CONJS_DISYUNTIVAS:
            etiqueta_eagles = "CCY"
        elif acepcion in CONJS_DISTRIBUTIVAS or DISTRIBUTIVA in acepcion.get_tipos():
            etiqueta_eagles = "CCD"
        elif acepcion in CONJS_ADVERSATIVAS or ADVERSATIVA in acepcion.get_tipos():
            etiqueta_eagles = "CCA"
        elif acepcion in CONJS_EXPLICATIVAS:
            etiqueta_eagles = "CCE"
        elif acepcion in CONJS_CONSECUTIVAS:
            etiqueta_eagles = "CSS"
        elif acepcion in CONJS_CAUSALES or CAUSAL in acepcion.get_tipos():
            etiqueta_eagles = "CSC"
        elif acepcion in CONJS_FINALES or FINAL in acepcion.get_tipos():
            etiqueta_eagles = "CSF"
        elif acepcion in CONJS_CONCESIVAS:
            etiqueta_eagles = "CSZ"
        elif acepcion in CONJS_TEMPORALES:
            etiqueta_eagles = "CST"
        elif acepcion in CONJS_CONDICIONALES:
            etiqueta_eagles = "CSD"
        else:
            etiqueta_eagles = "C00"
        fuente = u'wik|' + str(acepcion.get_n_entrada()) + u'|' + str(acepcion.get_n_acepcion())
        flexion = {etiqueta_eagles: {acepcion.get_lema_txt(): [fuente]}}
        return flexion

    @staticmethod
    def flexiona_preposicion(acepcion):
        if type(acepcion) == AcepcionWik:
            return Flexionador.flexiona_preposicion_wik(acepcion)
        else:
            return Flexionador.flexiona_preposicion_rae(acepcion)

    @staticmethod
    def flexiona_preposicion_rae(acepcion):
        lema_rae_txt = acepcion.get_lema_rae_txt()
        fuente = u'rae|' + str(acepcion.get_n_entrada()) + u'|' + str(acepcion.get_n_acepcion())
        if acepcion.get_es_superlativo() or acepcion.get_es_apocope() or\
                acepcion.get_es_forma_atona() or acepcion.get_es_forma_tonica() or acepcion.get_es_superlativo() or\
                acepcion.get_es_pronombre_amalgamado() or acepcion.get_es_comparativo():
            print(u'¿Deberíamos borrar', acepcion.get_lema_rae_txt(), u'?', fuente)
        if False:
            for info in acepcion._datos.keys():
                if info in ["info_uso", "es_desusado", "es_poco_usado", "neutro_txt", "es_contraccion"]:
                    pass
                elif info in ["generos_disponibles", "numeros_disponibles",
                              "masculino_ambiguo", "aumentativos",
                              "diminutivos", "tipos", "apocope_txt", "apocope_plural_txt",
                              "es_locucion", "tambien_superlativo_regular", "superlativos_txt", "comparativo_txt",
                              "formas_plural"]:
                    print(lema_rae_txt, u'Campo', info, u'en _datos y que no tenemos en cuenta flexiona_preposicion_rae')
                    pass
                else:
                    print(lema_rae_txt, u'Campo', info, u'en _datos desconocido flexiona_preposicion_rae')
            if "info_uso" in acepcion._datos:
                for info in acepcion._datos["info_uso"].keys():
                    if info in ["categoria_alternativa"]:
                        pass
                    elif info in ["es_locucion", "numero_alternativo", "genero_alternativo",
                                  "desusado", "posicion_alternativo", "tipo_alternativo", "sin_articulo"]:
                        print(lema_rae_txt, u'Campo', info, u'en info_uso y que no tenemos en cuenta flexiona_preposicion_rae')
                        pass
                    else:
                        print(lema_rae_txt, u'Campo', info, u'en info_uso desconocido flexiona_preposicion_rae')

        uso = DESUSADO if acepcion.get_es_desusado() else POCO_USADO if acepcion.get_es_poco_usado() else "0"
        formas_expandidas = acepcion.get_formas_expandidas()
        if not acepcion.get_palabras_contraidas():
            tipo = SIMPLE
            genero = "0"
            numero = "0"
            etiqueta_eagles = PREPOSICION + tipo + genero + numero + uso
            # La preposición "bajo, ja" coincide con otra categoría y tiene formas diferenciadas en género, de ahí que
            # se use las formas_expandidas y no simplemente el lema_rae_txt
            flexion_completa = {etiqueta_eagles: {formas_expandidas[0]: [fuente]}}
        else:
            # Tenemos una contracción de 2 (o 3) palabras, que puede tener género y puede tener número.
            tipo = CONTRAIDA
            genero = MASCULINO  # Por defecto
            numero = SINGULAR  # Por defecto
            if len(formas_expandidas) == 1:
                # Son formas que no varían en género: "al", "del", "dél", "desdel", "dí" (de ahí), "na" (en la).
                if lema_rae_txt == u'dí':
                    genero = "0"
                    numero = "0"
                elif lema_rae_txt == u'na':
                    genero = FEMENINO
                etiqueta_eagles = PREPOSICION + tipo + genero + numero + uso
                flexion_completa = {etiqueta_eagles: {lema_rae_txt: [fuente]}}
            else:
                # "dello, lla", "dentrambos", "dese, sa", "deste, ta", "destotro, tra"
                flexion_completa = {}
                if formas_expandidas[0][-1] == u'o':
                    # "dello, lla" y "destotro, tra". En el segundo caso puede ser tanto neutro como masculino
                    if lema_rae_txt == u'destotro, tra':
                        etiqueta_eagles = PREPOSICION + tipo + genero + numero + uso
                        flexion_completa.update({etiqueta_eagles: {formas_expandidas[0]: [fuente]}})
                    genero = NEUTRO
                elif formas_expandidas[0][-1] == u's':
                    numero = PLURAL
                etiqueta_eagles = PREPOSICION + tipo + genero + numero + uso
                flexion_completa.update({etiqueta_eagles: {formas_expandidas[0]: [fuente]}})
                genero = FEMENINO
                etiqueta_eagles = PREPOSICION + tipo + genero + numero + uso
                flexion_completa.update({etiqueta_eagles: {formas_expandidas[1]: [fuente]}})
                if acepcion.get_neutro_txt():
                    # "dese, sa" -> "deso", "deste, ta" -> "desto"
                    genero = NEUTRO
                    etiqueta_eagles = PREPOSICION + tipo + genero + numero + uso
                    flexion_completa.update({etiqueta_eagles: {acepcion.get_neutro_txt(): [fuente]}})
                if numero == SINGULAR:
                    # Hacemos el plural. Cogemos la forma femenina, quitamos la -a y añadimos -os/-as según convenga
                    etiqueta_eagles = PREPOSICION + tipo + MASCULINO + PLURAL + uso
                    flexion_completa.update({etiqueta_eagles: {formas_expandidas[1][:-1] + u'os': [fuente]}})
                    etiqueta_eagles = PREPOSICION + tipo + FEMENINO + PLURAL + uso
                    flexion_completa.update({etiqueta_eagles: {formas_expandidas[1] + u's': [fuente]}})
        if False:
            print(u'flexiona_preposicion_rae:', lema_rae_txt, fuente)
            print(u'\n'.join([u': '.join([tag, u', '.join(formas)])
                              for tag, formas in sorted(flexion_completa.items(),
                                                        key=lambda tupla: tupla[0], reverse=True)]))
        return flexion_completa

    @staticmethod
    def flexiona_preposicion_wik(acepcion):
        print(u'Hay que modificar flexiona_preposicion_wik')
        datos = acepcion.get_datos()
        for inflect in acepcion.get_inflects():
            if u'adj' in inflect:
                datos["categoria"] = ADJETIVO
                datos["inflects"] = [inflect]
                flexion_previa = Flexionador.flexiona_sust_adj_det_wik(acepcion, ajusta_lema=False)
                flexion = {PREPOSICION + SIMPLE + etiqueta[3:5] + NA: datos
                           for etiqueta, datos in flexion_previa.items()}
                break
            elif u'sust' in inflect:
                datos["categoria"] = SUSTANTIVO
                datos["inflects"] = [inflect]
                flexion_previa = Flexionador.flexiona_sust_adj_det_wik(acepcion, ajusta_lema=False)
                flexion = {PREPOSICION + SIMPLE + etiqueta[2:4] + NA: datos
                           for etiqueta, datos in flexion_previa.items()}
                break
        else:
            etiqueta_eagles = "SCMS0" if acepcion.get_lema_txt() in [u'al', u'del'] else "SS000"
            fuente = u'wik|' + str(acepcion.get_n_entrada()) + u'|' + str(acepcion.get_n_acepcion())
            flexion = {etiqueta_eagles: {acepcion.get_lema_txt(): [fuente]}}
        return flexion

    @staticmethod
    def flexiona_adverbio(acepcion):
        # En la RAE vienen más adverbios que en el Wikcionario, pero están muy poco especificados. En la RAE solo se
        # manejan 3-4 tipos, tal que Negativo, Relativo y poco más. Tipos que indican algún tipo de semántica no
        # aparecen. Es posible que sea mejor usar los adverbios del Wikcionario y sus etiquetas cuando existan.
        if type(acepcion) == AcepcionWik:
            return Flexionador.flexiona_adverbio_wik(acepcion)
        else:
            return Flexionador.flexiona_adverbio_rae(acepcion)

    @staticmethod
    def flexiona_adverbio_rae(acepcion):
        lema_rae_txt = acepcion.get_lema_rae_txt()
        fuente = u'rae|' + str(acepcion.get_n_entrada()) + u'|' + str(acepcion.get_n_acepcion())
        if False:
            for info in acepcion._datos.keys():
                if info in ["info_uso", "tipos", "es_desusado", "es_poco_usado", "neutro_txt",
                            "apocope_txt", "apocope_plural_txt",
                            "es_locucion", "tambien_superlativo_regular", "superlativos_txt", "comparativo_txt",
                            "formas_plural"]:
                    pass
                elif info in ["generos_disponibles", "numeros_disponibles",
                              "masculino_ambiguo", "aumentativos",
                              "diminutivos"]:
                    print(lema_rae_txt, u'Campo', info, u'en _datos y que no tenemos en cuenta')
                    pass
                else:
                    print(lema_rae_txt, u'Campo', info, u'en _datos desconocido')
            if "info_uso" in acepcion._datos:
                for info in acepcion._datos["info_uso"].keys():
                    if info in ["categoria_alternativa", "es_locucion"]:
                        pass
                    elif info in ["numero_alternativo", "genero_alternativo",
                                  "desusado", "posicion_alternativo", "tipo_alternativo", "sin_articulo"]:
                        print(lema_rae_txt, u'Campo', info, u'en info_uso y que no tenemos en cuenta')
                        pass
                    else:
                        print(lema_rae_txt, u'Campo', info, u'en info_uso desconocido')
        tipo = AFIRMATIVO if lema_rae_txt in [u'sí', u'también'] else\
            NEGATIVO if lema_rae_txt in [u'no', u'apenas', u'tampoco', u'pero', u'jamás', u'nunca', u'nada'] else\
            acepcion.get_tipos()[0] if acepcion.get_tipos() else GENERAL
        grado = NA  # Solo los adverbios en -mente que vienen de flexionar adjetivos tienen grado (el del adjetivo)
        uso = DESUSADO if acepcion.get_es_desusado() else POCO_USADO if acepcion.get_es_poco_usado() else "0"
        etiqueta_eagles = ADVERBIO + tipo + grado + uso
        if lema_rae_txt == u'aun' and u'todavía' in acepcion.get_definicion():
            # Sorprendentemente, no hay una entrada para "aún", sino que se dice en la sección de morfología
            # de "aun", que las definiciones que equivalen a "todavía" se escriben con acento.
            flexion = {etiqueta_eagles: {u'aún': [fuente]}}
        elif lema_rae_txt == u'solo':
            # Igualmente, tampoco hay entrada para "sólo", sino que se dice que puede llevar acento.
            flexion = {etiqueta_eagles: {u'solo': [fuente],
                                         u'sólo': [fuente]}}
        else:
            flexion = {etiqueta_eagles: {acepcion.get_formas_expandidas()[0]: [fuente]}}
            # Algún adverbio, como tan(to), cuan(to), cuán(to), mucho (muy), siquer(a)... tienen apócope.
            apocope_txt = acepcion.get_apocope_txt()
            if apocope_txt:
                # print(lema_rae_txt, u'tiene el apócope', apocope_txt)
                flexion[etiqueta_eagles][apocope_txt] = [fuente]
            # Algunos comparativos, como mejor y peor son también adverbios
            comparativo_txt = acepcion.get_comparativo_txt()
            if comparativo_txt:
                # print(lema_rae_txt, u'tiene el comparativo', comparativo_txt)
                flexion[ADVERBIO + COMPARATIVO + COMPARATIVO + uso] = {comparativo_txt: [fuente]}
        return flexion

    @staticmethod
    def flexiona_adverbio_wik(acepcion):
        fuente = u'wik|' + str(acepcion.get_n_entrada()) + u'|' + str(acepcion.get_n_acepcion())
        # TODO: faltan caracteres
        if acepcion.get_tipos():
            # Los adverbios pueden tener (raramente) más de un tipo en una misma acepción.
            # Así que generamos tantas formas iguales con etiquetas distintas como tipos tenga el adverbio.
            # "antes" puede ser locativo, temporal o modal pero cada tipo se recoge como una acepción distinta. Pero
            # hay alguno como "cual", que es del tipo === {{adverbio relativo|es}} y comparativo ===
            flexion = {}
            for tipos in acepcion.get_tipos():
                etiqueta_eagles = ADVERBIO + tipos[0][0].upper()
                flexion[etiqueta_eagles] = {acepcion.get_lema_txt(): [fuente]}
        else:
            etiqueta_eagles = "RG"
            flexion = {etiqueta_eagles: {acepcion.get_lema_txt(): [fuente]}}
        return flexion

    @staticmethod
    def flexiona_afijo(acepcion):
        if type(acepcion) == AcepcionWik:
            return Flexionador.flexiona_afijo_wik(acepcion)
        else:
            return Flexionador.flexiona_afijo_rae(acepcion)

    @ staticmethod
    def flexiona_afijo_rae(acepcion):
        # Los sufijos se usan para formar nuevos adjetivos/sustantivos, pero también verbos, adverbios...
        # En principio, solo consideramos que el sufijo aporta género, si hay variación: -sco, ca y similares, que
        # tienen la forma masculina y la femenina (implícita)
        # Un elemento compositivo es un su/prefijo que no aporta información gramatical (como "des-" o "-ín") sino
        # léxica, como "hemo-", "-teca", "cardio-, -cardio", "filo-, ‒́filo, la" o "‒́fero, ra" (elemento compositivo).
        # La RAE no incluye ningún afijo que esté desusado y de ahí que esta categoría carezca de ese carácter.
        lema_rae_txt = acepcion.get_lema_rae_txt()
        categoria = acepcion.get_categoria()
        uso = DESUSADO if acepcion.get_es_desusado() else POCO_USADO if acepcion.get_es_poco_usado() else "0"
        fuente = u'rae|' + str(acepcion.get_n_entrada()) + u'|' + str(acepcion.get_n_acepcion())
        flexion_completa = {}
        formas_expandidas = acepcion.get_formas_expandidas()
        if categoria == PREFIJO:
            # No hay género ni número, ni tampoco subtipo: pos-, pre-...
            flexion_completa.update({AFIJO + PREFIJO + "000" + uso: {formas_expandidas[0]: [fuente]}})
            return flexion_completa
        elif categoria == ELEMENTO_COMPOSITIVO:
            if lema_rae_txt[0] not in [u'-', u'‒']:  # El guión largo se usa para marcar tonicidad previa: ‒́
                # Es un elemento compositivo que funciona como prefijo (quizá, además, como sufijo)
                flexion_completa.update({AFIJO + PREFIJO + ELEMENTO_COMPOSITIVO + "00" + uso:
                                         {formas_expandidas[0]: [fuente]}})
                if len(formas_expandidas) == 1:
                    # Es un elemento compositivo que solo actúa como prefijo: "hemo-"
                    return flexion_completa
                # Habrá que añadir las formas sufijas, quizá con variación de género.
                formas_expandidas = formas_expandidas[1:]  # Quitamos la forma prefija
            encabezado_eagles = AFIJO + SUFIJO + ELEMENTO_COMPOSITIVO
        else:
            # Es solo un sufijo. Tendremos que ver si hay cambio de género
            if FLEXIVO in acepcion.get_tipos():
                encabezado_eagles = AFIJO + SUFIJO + FLEXIVO
            else:
                encabezado_eagles = AFIJO + SUFIJO + "0"

        # Hay un pequeño problema con las formas del plural para los prefijos. Los prefijos fijan la tonicidad de la
        # palabra derivada, con lo que pueden necesitar siempre tilde: "-ción", "-és, sa". Estas tildes se consideran
        # como diacríticas, al no ser necesarias (pero aparecer en el lema), con lo que se trasladan al resto de formas.
        # Esto ocurre solo con los sufijos monosílabos acabados en -n/s
        formas_plural = [Flexionador.pluraliza(f, formas_expandidas) for f in formas_expandidas]
        if len(Palabra(formas_expandidas[0], calcula_alofonos=False).get_silabas()) == 1 and\
                formas_expandidas[0][-1] in u'ns':
            formas_plural[0][0] = Palabra(formas_plural[0][0], calcula_alofonos=False,
                                          organiza_grafemas=True).ajusta_tildes()
            if len(formas_expandidas) > 1:
                formas_expandidas[1] = Palabra(formas_expandidas[1], calcula_alofonos=False,
                                               organiza_grafemas=True).ajusta_tildes()
                formas_plural[1][0] = Palabra(formas_plural[1][0], calcula_alofonos=False,
                                              organiza_grafemas=True).ajusta_tildes()

        if len(formas_expandidas) == 1:
            # No hay variación en genero, así que no podemos asegurar que tenga género
            genero = FEMENINO if formas_expandidas[0][-1] in u'aás' else\
                MASCULINO if formas_expandidas[0][-1] in u'eéoónlzd' else NEUTRO
            if genero == NEUTRO:
                flexion_completa.update({encabezado_eagles + "00" + uso: {formas_expandidas[0]: [fuente]}})
            elif formas_expandidas[0][-1] == u's':
                flexion_completa.update({encabezado_eagles + genero + INVARIABLE + uso:
                                         {formas_expandidas[0]: [fuente]}})
            else:
                flexion_completa.update({encabezado_eagles + genero + SINGULAR + uso: {formas_expandidas[0]: [fuente]},
                                         encabezado_eagles + genero + PLURAL + uso: {formas_plural[0][0]: [fuente]}})
        else:  # elif len(formas_expandidas) == 2:
            # Tenemos los dos géneros. Nos venimos arriba y pluralizamos además.
            flexion_completa.update({encabezado_eagles + MASCULINO + SINGULAR + uso: {formas_expandidas[0]: [fuente]},
                                     encabezado_eagles + FEMENINO + SINGULAR + uso: {formas_expandidas[1]: [fuente]},
                                     encabezado_eagles + MASCULINO + PLURAL + uso: {formas_plural[0][0]: [fuente]},
                                     encabezado_eagles + FEMENINO + PLURAL + uso: {formas_plural[1][0]: [fuente]}})

        if False:
            print(u'flexiona_afijo_rae:', lema_rae_txt, fuente)
            print(u'\n'.join([u': '.join([tag, u', '.join(formas)])
                              for tag, formas in sorted(flexion_completa.items(),
                                                        key=lambda tupla: tupla[0], reverse=True)]))
        return flexion_completa

    @staticmethod
    def flexiona_afijo_wik(acepcion):
        print(u'Hay que modificar flexiona_afijo_wik')
        # 0: Categoría = - (afijo)
        # 1: Tipo = > (prefijo), < (sufijo)
        # 2: Subtipo = sufijo Flexivo, Elemento compositivo, 0
        # 3: Género = Masculino, Femenino, Común, 0 (neutro)
        # 4: Número = Singular, Plural, iNvariable
        # 5: Uso = 0 (normal), Desusado, Poco usado
        categoria = acepcion.get_categoria()
        if categoria == ELEMENTO_COMPOSITIVO:
            pass
        datos = acepcion.get_datos()
        for inflect in acepcion.get_inflects():
            if u'adj' in inflect:
                datos["categoria"] = ADJETIVO
                datos["inflects"] = [inflect]
                flexion_previa = Flexionador.flexiona_sust_adj_det_wik(acepcion, ajusta_lema=False)
                flexion = {AFIJO + categoria + NA + etiqueta[3:5] + NA: datos
                           for etiqueta, datos in flexion_previa.items()}
                break
            elif u'sust' in inflect:
                datos["categoria"] = SUSTANTIVO
                datos["inflects"] = [inflect]
                flexion_previa = Flexionador.flexiona_sust_adj_det_wik(acepcion, ajusta_lema=False)
                flexion = {AFIJO + categoria + NA + etiqueta[2:4] + NA: datos
                           for etiqueta, datos in flexion_previa.items()}
                break
        else:
            etiqueta_eagles = AFIJO + (categoria if categoria != ELEMENTO_COMPOSITIVO else SUFIJO) + \
                              (ELEMENTO_COMPOSITIVO if categoria == ELEMENTO_COMPOSITIVO else NA) + \
                              MASCULINO + SINGULAR + NA
            fuente = u'wik|' + str(acepcion.get_n_entrada()) + u'|' + str(acepcion.get_n_acepcion())
            flexion = {etiqueta_eagles: {acepcion.get_lema_txt(): [fuente]}}
        return flexion

    @staticmethod
    def flexiona_sust_adj_det(acepcion, ajusta_lema, hay_nombres):
        if type(acepcion) == AcepcionWik:
            return Flexionador.flexiona_sust_adj_det_wik(acepcion, ajusta_lema)
        else:
            return Flexionador.flexiona_sust_adj_det_rae(acepcion, hay_nombres)

    @staticmethod
    def flexiona_sust_adj_det_rae(acepcion, hay_nombres):
        lema_rae_txt = acepcion.get_lema_rae_txt()
        if lema_rae_txt == u'embrambos, bas':
            pass
        fuente = u'rae|' + str(acepcion.get_n_entrada()) + u'|' + str(acepcion.get_n_acepcion())
        if acepcion.get_es_locucion():
            # En realidad, significa que este lema es una redirección a una locución, y ha tomado de ellos sus
            # valores de acepción. Son formas que se han soldado: suigéneris, malaconsejado, buenamoza...
            # Las locuciones no se flexionan (al menos por ahora), pero esto no es una locución en realidad
            # print(lema_rae_txt, u'por lo visto es una locución soldada (era locución)', fuente)
            pass

        categoria = acepcion.get_categoria()
        formas_expandidas = acepcion.get_formas_expandidas()
        generos_disponibles = acepcion.get_generos_disponibles()
        if not generos_disponibles:
            generos_disponibles = [MASCULINO, FEMENINO]
        numeros_disponibles = acepcion.get_numeros_disponibles()
        if not numeros_disponibles:
            if len(generos_disponibles) == 1 and generos_disponibles[0] == NEUTRO:
                numeros_disponibles = [SINGULAR]
            else:
                numeros_disponibles = [SINGULAR, PLURAL]
        elif len(numeros_disponibles) != 1 and (SINGULAR not in numeros_disponibles or PLURAL not in numeros_disponibles):
            print(lema_rae_txt, u'tiene unos números extraños', numeros_disponibles)

        if len(formas_expandidas) > 2:
            print(lema_rae_txt, u'tiene', len(formas_expandidas), u'formas expandidas')

        formas_plural = acepcion.get_formas_plural()  # Se suelen meter los plurales tras la 1ª acepción
        if not formas_plural:  # 1ª acepción, y la propia RAE no especifica el plural (a veces sí, "los, las")
            # Podría ser que el lema, al menos para esta acepción, se usara solo en plural. Esto da problemas,
            # pues el lema podría venir ya en plural (como pegásides) o no (como la acepción 3-4 de andada).
            # Por ello, si la acepcion es "solo plural", hacemos lo siguiente:
            # - Si el lema acaba en -s:
            #   * Si la acepción 0 de ese lema es "solo plural", la forma expandida está ya en plural.
            #     Esto afecta a todas las acepciones posteriores siempre que la 0 sea "solo plural".
            #   * Si la acepción 0 no es "solo plural", solo quedan estos casos:
            #     - dos, tres, seis, dieciséis, veintidós, veintitrés: que como numerales, se tratan arriba.
            #     - arnés, mies, gas, interés: que están en singular y crearán el plural adecuado al ser agudas.
            #     - guardapolvos, tenis, gandumbas, efemérides: que están en singular y crean plural invariante.
            #     Con lo que basta con crear la forma plural y esa será la correcta.
            # - Si el lema no acaba en -s: Es una forma de singular que hay que pluralizar normalmente.
            if len(numeros_disponibles) == 1 and numeros_disponibles[0] == PLURAL and\
                    lema_rae_txt[-1] == u's' and acepcion.get_n_acepcion() == 0:
                formas_plural = [[f] for f in formas_expandidas]
                acepcion.set_formas_plural(formas_plural)  # Las siguientes acepciones, lo tendrán en cuenta
            else:
                formas_plural = [Flexionador.pluraliza(f, formas_expandidas) for f in formas_expandidas]
        elif len(formas_plural) != len(formas_expandidas):
            print(u'El lema', lema_rae_txt, u'tiene distinta cantidad de plurales:', formas_expandidas, formas_plural)
        elif False and lema_rae_txt[-1] == u's':
            print(lema_rae_txt, u'->', u', '.join([f for g in formas_plural for f in g]),
                u': solo se usa en plural en acepción', acepcion.get_n_acepcion(), u'(pero con plural preasignado)')

        flexion = {}

        uso = DESUSADO if acepcion.get_es_desusado() else POCO_USADO if acepcion.get_es_poco_usado() else "0"
        sufijacion = "0"
        if categoria == SUSTANTIVO:
            # Creamos los 2 primeros caracteres de la etiqueta y los 3 últimos. Los otros 2 son género y número.
            encabezado_eagles = SUSTANTIVO + COMUN  # En la RAE no hay nombres propios
            clase_semantica = "00"
            origen = "0"
            pie_eagles = clase_semantica + sufijacion + origen + uso
            # Sabemos si el sustantivo es masculino y/o femenino a través de los géneros disponibles para la acepción.
            # Además, sabemos si esas formas son distintas o no según las formas expandidas (si solo hay una, no cambia)
            # Tenemos que crear 1-4 formas según los parámetros que tengamos.
            if (len(lema_rae_txt) == 1 and lema_rae_txt not in u'ieaou') or\
                    lema_rae_txt in [u'ch', u'gu', u'll', u'qu', u'rr']:
                numeros_disponibles = [SINGULAR]  # Es (un nombre de) una letra
        elif categoria == ADJETIVO:
            # Creamos los primeros y últimos caracteres de la etiqueta, dejando el género y número en el medio
            tipo = acepcion.get_tipos()[0]
            grado = acepcion.get_grado()
            if formas_expandidas[0] in [u'mejor', u'peor', u'mayor', u'menor', u'interior', u'exterior',
                                        u'superior', u'inferior', u'anterior', u'posterior', u'ulterior']:
                grado = COMPARATIVO
            elif formas_expandidas[0] in [u'óptimo', u'pésimo', u'máximo', u'mínimo', u'íntimo', u'extremo',
                                          u'supremo', u'sumo', u'ínfimo', u'postremo', u'póstumo', u'último']:
                grado = SUPERLATIVO
            encabezado_eagles = ADJETIVO + tipo + grado
            funcion = "0"
            pie_eagles = funcion + sufijacion + uso
        else:  # DETERMINANTE, aunque en la RAE vienen como ADJETIVO (pero ya le hemos cambiado la categoría)
            tipo = acepcion.get_tipos()[0]
            persona = acepcion.get_persona()
            encabezado_eagles = DETERMINANTE + tipo + persona
            if tipo == POSESIVO:
                poseedor = INVARIABLE if persona == "3" else\
                    SINGULAR if formas_expandidas[0] in [u'mío', u'tuyo'] else PLURAL
            elif tipo == RELATIVO_POSESIVO:  # Solo "cuyo", que es adjetivo relativo posesivo
                poseedor = INVARIABLE  # Se marca también un poseedor, para realzar su valor posesivo
            else:
                poseedor = "0"
            pie_eagles = poseedor + sufijacion + uso

        # FLEXIÓN BÁSICA
        if len(generos_disponibles) == 1 or (len(generos_disponibles) == 2 and len(formas_expandidas) == 1):
            # Solo hay un género disponible, o dos pero no tienen formas diferenciadas (es ambiguo en cuanto al género)
            # En cualquier caso, esta acepción no tendrá formas distintas de masculino y femenino. Habrá 1 o 2 formas
            # dependiendo de los números disponibles que haya.
            genero = generos_disponibles[0] if len(generos_disponibles) == 1 else AMBIGUO
            if formas_expandidas[-1 if genero == FEMENINO else 0] == formas_plural[-1 if genero == FEMENINO else 0][0]:
                # Invariante en número. Solo hay una forma, que bien es ambigua o es la del único género disponible,
                # y además es invariable en número o es el único número disponible.
                numero = INVARIABLE if len(numeros_disponibles) == 2 else numeros_disponibles[0]
                flexion = {encabezado_eagles + genero + numero + pie_eagles:
                           [formas_expandidas[-1 if genero == FEMENINO else 0]]}
            else:
                # Varía en número. Las formas creadas dependen de los géneros disponibles.
                if SINGULAR in numeros_disponibles:
                    if formas_expandidas[0] == u'qué':  # Incluimos "qués" como plural, pero "qué" también puede serlo
                        flexion[encabezado_eagles + genero + INVARIABLE + pie_eagles] = [formas_expandidas[0]]
                    else:
                        forma = formas_expandidas[-1 if genero == FEMENINO else 0]\
                            if not acepcion.get_neutro_txt() or genero != NEUTRO else acepcion.get_neutro_txt()
                        flexion[encabezado_eagles + genero + SINGULAR + pie_eagles] = [forma]
                if PLURAL in numeros_disponibles:
                    flexion[encabezado_eagles + genero + PLURAL + pie_eagles] =\
                        formas_plural[-1 if genero == FEMENINO else 0]
        elif len(generos_disponibles) == 2 and (len(formas_expandidas) == 2):
            # Se cubren las cuatro combinaciones de variantes en género y número, pero pueden ser coincidentes.
            if MASCULINO not in generos_disponibles or FEMENINO not in generos_disponibles:
                print(lema_rae_txt, u'tiene 2 géneros disponibles, pero no son masculino y femenino')
            # Hay formas diferentes para masculino y femenino. A la fuerza sus plurales son distintos
            if len(formas_plural) > 1 and formas_plural[0][0] == formas_plural[1][0]:
                print(lema_rae_txt, u'tiene 2 géneros disponibles, pero comparten el plural')
            if SINGULAR in numeros_disponibles:
                # MASCULINO
                if categoria == SUSTANTIVO and acepcion.get_masculino_ambiguo():
                    etiqueta_eagles = encabezado_eagles + AMBIGUO + SINGULAR + pie_eagles
                else:
                    etiqueta_eagles = encabezado_eagles + MASCULINO + SINGULAR + pie_eagles
                flexion[etiqueta_eagles] = [formas_expandidas[0]]
                # FEMENINO
                etiqueta_eagles = encabezado_eagles + FEMENINO + SINGULAR + pie_eagles
                flexion[etiqueta_eagles] = [formas_expandidas[-1]]
            if PLURAL in numeros_disponibles:
                # MASCULINO
                etiqueta_eagles = encabezado_eagles + MASCULINO + PLURAL + pie_eagles
                flexion[etiqueta_eagles] = formas_plural[0]
                # FEMENINO
                etiqueta_eagles = encabezado_eagles + FEMENINO + PLURAL + pie_eagles
                flexion[etiqueta_eagles] = formas_plural[-1]
        else:
            print(lema_rae_txt, u'tiene', len(generos_disponibles), u'géneros disponibles')
        if not flexion:
            print(lema_rae_txt, u'no tiene flexión alguna')

        # APÓCOPES
        # Como no tratamos muy bien los apócopes, solo los usamos en adjetivos o determinantes, y tambien los aceptamos
        # en nombres si no es una acepción derivada (previamente ya borramos los apócopes de nombres que no tuvieran su
        # primera acepción como nombre).
        apocope_txt = acepcion.get_apocope_txt()\
            if (categoria != SUSTANTIVO or int(acepcion.get_n_acepcion()) == acepcion.get_n_acepcion()) else u''
        if not apocope_txt and categoria != SUSTANTIVO and formas_expandidas[0][-7:] in [u'primero', u'tercero'] and\
                (len(formas_expandidas[0]) == 7 or formas_expandidas[0][:6] == u'décimo'):
            # Para los ordinales acabados en -primero/-tercero, creamos su apócope
            apocope_txt = formas_expandidas[0][:-1]
        if apocope_txt and apocope_txt != u'muy':  # "muy" sale como apócope de "mucho", que es determinante
            # El apócope no se pluraliza nunca, sólo es válido para el singular (excepto para "veintiún").
            # Usualmente, los apócopes tienen una forma simple, como "algún". Si el lema tiene formas distintas
            # para ambos géneros, el apócope sólo será válido para el masculino (salvo "mi", "tu", "su").
            # En una ocasión el apócope tiene formas distintas para los dos géneros: "germán, na", pero la forma
            # que pone femenina es la misma que la usual sin apocopamiento. Si el lema es ambiguo en cuanto al
            # género, el apócope también.
            # Solo existe un nombre femenino con apócope: "mano" (que hace "man"). Esto produce un pequeño fallo,
            # ya que la segunda entrada ("mano, na") y la acepción 36 de la primera entrada, tienen género masculino
            # disponible, con lo que "man" aparece como apócope femenino y masculino.
            if SINGULAR in numeros_disponibles or categoria == DETERMINANTE:
                etiqueta_apocopado = encabezado_eagles +\
                                     (AMBIGUO if apocope_txt in [u'mi', u'tu', u'su'] or
                                      (len(formas_expandidas) == 1 and
                                       FEMENINO in generos_disponibles and MASCULINO in generos_disponibles)
                                      else generos_disponibles[0]) + SINGULAR + pie_eagles
                etiqueta_apocopado = etiqueta_apocopado[:6] + APOCOPE + etiqueta_apocopado[7:]
                flexion[etiqueta_apocopado] = [apocope_txt.split(u',')[0]]  # el u',' es por lo de "germán, na".
                # print(u'Apócope de', lema_rae_txt, u'->', etiqueta_apocopado, u':', flexion[etiqueta_apocopado], fuente)
                if apocope_txt in [u'mi', u'tu', u'su']:
                    # Son solo determinantes, nunca nombres, y tienen plural
                    etiqueta_apocopado = etiqueta_apocopado[:4] + PLURAL + etiqueta_apocopado[5:]
                    flexion[etiqueta_apocopado] = [apocope_txt + u's']
            elif False:
                if MASCULINO not in generos_disponibles:
                    print(lema_rae_txt, u'tiene apócope pero para femenino plural:', apocope_txt, fuente)
                if FEMENINO not in generos_disponibles:
                    print(lema_rae_txt, u'tiene apócope pero para masculino plural:', apocope_txt, fuente)
                else:
                    print(lema_rae_txt, u'tiene apócope pero para ambiguo plural:', apocope_txt, fuente)
                pass
        apocope_plural_txt = acepcion.get_apocope_plural_txt()
        if apocope_plural_txt:
            # Solo ocurre en "cualesquier"
            etiqueta_apocopado = encabezado_eagles + AMBIGUO + PLURAL + pie_eagles
            etiqueta_apocopado = etiqueta_apocopado[:6] + APOCOPE + etiqueta_apocopado[7:]
            flexion[etiqueta_apocopado] = [apocope_plural_txt]

        # SUPERLATIVOS y ADVERBIOS -MENTE (y superlativos + -mente)
        if (encabezado_eagles[:2] == ADJETIVO + CALIFICATIVO) and len(formas_expandidas[0]) > 1 and\
                int(acepcion.get_n_acepcion()) == acepcion.get_n_acepcion():
            # No hacemos primerísimo (o primer(ísim)amente) o cosas así, que quizá interesen. También hay
            # acepciones de una letra como adjetivos, como "plan b". No creamos superlativo ni adverbio y por
            # eso lo del len > 1.
            # Además, solo creamos estas formas para "adjetivos, adjetivos", no para los "usado también como
            # adjetivo", y de ahí el tema de que el número de acepción debe ser un número entero.
            # En cualquier caso los adjetivos se consideran siempre como disponibles para ambos géneros,
            # aunque estén derivados de nombres con un género propio. Así, palabras como "limón" o "miel"
            # formarían adjetivos que son invariantes en género, pero que son válidos para ambos géneros.
            # Además, al hacer el superlativo se harán las cuatro formas (limoncísimo/a(s)), y también se
            # crean las versiones en -mente (limónmente, limoncísimamente).
            # Como aquí solo vemos la acepción, solo podemos evitar que "se nos cuelen" viendo, como hacemos,
            # que la acepción no sea derivada. Sin embargo, hay lemas que tienen las primeras acepciones como
            # sustantivo, pero también tienen acepciones como adjetivo, así que no podemos identificarlas (lo
            # que le pasa a limón y más).
            # TODO: quizá sería deseable crear los superlativos y los adverbios solo para adjetivos "de pura
            # cepa", cuya primera acepción sea de adjetivo, pero creo que no es tan sencillo. En cualquier
            # caso, sobregenerar abulta pero no suele molestar porque no produce "colisiones" con otros lemas.
            if formas_expandidas[0] in [u'inicial']:
                pass

            # Creamos el adverbio en -mente siempre que la palabra no acabe en -as, -es, -os. ¿Motivo? que quedan raros,
            # porque suelen ser palabras compuestas: antidisturbios, chupamedias...; o raras: cricoides, guaperas...
            # Tampoco lo hacemos de palabras agudas sin coda (por lo tanto, acabadas en vocal tónica), porque suelen ser
            # gentilicios y dan adverbios que no existen realmente. Con coda sí: finalmente, lateralmente, vulgarmente,
            # cortésmente, vorazmente...
            crea_adverbio = formas_expandidas[-1][-2:] not in [u'es', u'as', u'os'] and\
                formas_expandidas[-1][-1] not in u'íéáóú'

            # Creamos el adverbio en -mente a partir de la forma femenina
            if crea_adverbio:
                flexion[ADVERBIO + GENERAL + NA + uso] = [formas_expandidas[-1] + u'mente']

            # Creamos los superlativos: http://lema.rae.es/dpd/srv/search?id=UByFr5964D6oCGp9V4
            # En el DRAE no se considera que los superlativos de bueno/malo/grande/pequeño (óptimo/pésimo/máximo/mínimo)
            # sean tales, sino que tienen sus propias acepciones y demás. Pasa igual con los comparativos y superlativos
            # de alto/bajo (superior/inferior/supremo/ínfimo).
            formas_base = []  # Las formas masc. sing., de las que se derivan fácilmente las otras 3 formas: -[oa]s?
            superlativos_txt = acepcion.get_superlativos_txt()\
                if formas_expandidas[0] != u'sabio' else [u'sapientísimo, ma']  # "sabio" no aparece con sup irregular
            if superlativos_txt:
                # Tenemos la forma de lema RAE del superlativo, de la forma "ternísimo, ma". Puede haber más de uno,
                # como en "enemicísimo, ma", "inimicísimo, ma", que además resultan ser tres porque también tiene el
                # superlativo regular "enemiguísimo".
                for superlativo_txt in superlativos_txt:
                    formas_base.append(superlativo_txt.split(u',')[0])  # Nos quedamos con el masculino
            if not superlativos_txt or acepcion.get_tambien_superlativo_regular():
                formas_base += Flexionador.crea_superlativo(formas_expandidas[0])

            # Para cada forma base (masculino singular en -o), creamos fácilmente las 4 combinaciones de género/número.
            # Consideramos que todos los adjetivos tienen ambos géneros, incluso si derivan de un nombre monogenérico.
            # Además creamos las formas de adverbio en -mente en superlativo: rapidísimamente, utilísimamente...
            for forma_base in formas_base:
                if SINGULAR in numeros_disponibles:
                    flexion.setdefault(encabezado_eagles[:-1] + SUPERLATIVO + MASCULINO + SINGULAR + pie_eagles, []).\
                        append(forma_base)
                    flexion.setdefault(encabezado_eagles[:-1] + SUPERLATIVO + FEMENINO + SINGULAR + pie_eagles, []).\
                        append(forma_base[:-1] + u'a')
                    # Auque al añadir el -ísimo cambiamos el final de la palabra, no creamos el adverbio superlativo
                    # sino hemos creado el adverbio "normal". En cualquier caso, palabras acabadas en íéáóú no crean
                    # superlativo, como tampoco lo hacen las acabadas en -es, -as, -os, así que no hay que preocuparse.
                    flexion.setdefault(ADVERBIO + GENERAL + SUPERLATIVO + uso, []).\
                        append(forma_base[:-1] + u'amente')
                if PLURAL in numeros_disponibles:
                    flexion.setdefault(encabezado_eagles[:-1] + SUPERLATIVO + MASCULINO + PLURAL + pie_eagles, []).\
                        append(forma_base + u's')
                    flexion.setdefault(encabezado_eagles[:-1] + SUPERLATIVO + FEMENINO + PLURAL + pie_eagles, []).\
                        append(forma_base[:-1] + u'as')

        # COMPARATIVOS
        if categoria == ADJETIVO and acepcion.get_comparativo_txt():
            # En realidad son solo mejor/peor/mayor/menor. Hacen plural en -es, no hay cambios de tildes y son
            # ambiguos.
            # Añadimos de paso los adverbios en -mente. En realidad solo "mayormente" está recogido en la RAE
            # (y puesto que lo está, no haría falta añadirlo), pero si buscas en la web, la gente escribe
            # "peormente" y las otras.
            comparativo_txt = acepcion.get_comparativo_txt()
            flexion[encabezado_eagles[:-1] + COMPARATIVO + AMBIGUO + SINGULAR + pie_eagles] = [comparativo_txt]
            flexion[encabezado_eagles[:-1] + COMPARATIVO + AMBIGUO + PLURAL + pie_eagles] =\
                [comparativo_txt + u'es']
            flexion[ADVERBIO + COMPARATIVO + COMPARATIVO + uso] = [comparativo_txt + u'mente']

        # NEUTROS
        if categoria in [ADJETIVO, DETERMINANTE] and acepcion.get_neutro_txt():
            # Para los determinantes: esto, eso, aquello, formas antiguas y cosas como bastante, tanto o mucho
            # Solo se considera neutra la forma singular (la plural coincide con la masculina plural)
            # print(u'El adjetivo', lema_rae_txt, u'tiene forma neutra:', acepcion.get_neutro_txt())
            if formas_expandidas[0] not in [u'este', u'ese', u'aquel']:
                # En realidad, "esto", "eso" y "aquello" solo pueden ser pronombres.
                flexion[encabezado_eagles + NEUTRO + SINGULAR + pie_eagles] = [acepcion.get_neutro_txt()]

        # AUMENTATIVOS
        for aumentativo_mf in acepcion.get_aumentativos():
            # Cada aumentativo suele tener solo una forma expandida, pero pueden ser 2: [[u'planchón'],
            # [u'planchazo']] o [[u'bobalicón', u'bobalicona']]. En cualquier caso, si hay dos formas, la
            # primera forma es siempre masculina (terminada en -ón o -azo) y la segunda forma es la femenina
            # (en -a), y si hay una sola forma, es posible que sea tanto la masculina como la femenina
            # únicamente (vejancón, y vejancona son entradas distintas y ambas están marcadas como
            # aumentativos de viejo.
            if aumentativo_mf[0][-1] != u'a':
                if SINGULAR in numeros_disponibles:
                    # Tenemos cuidado con la etiqueta porque puede ser adjetivo o nombre, y cambia la posición
                    etiqueta_aumentativo = encabezado_eagles + MASCULINO + SINGULAR + pie_eagles
                    etiqueta_aumentativo = etiqueta_aumentativo[:6] + AUMENTATIVO + etiqueta_aumentativo[7:]
                    flexion.setdefault(etiqueta_aumentativo, []).append(aumentativo_mf[0])
                if PLURAL in numeros_disponibles:
                    etiqueta_aumentativo = encabezado_eagles + MASCULINO + PLURAL + pie_eagles
                    etiqueta_aumentativo = etiqueta_aumentativo[:6] + AUMENTATIVO + etiqueta_aumentativo[7:]
                    if aumentativo_mf[0][-2:] == u'ón':
                        forma_plural = aumentativo_mf[0][:-2] + u'ones'
                    elif aumentativo_mf[0][-3:] == u'azo':
                        forma_plural = aumentativo_mf[0] + u's'
                    else:
                        print(u'El aumentativo', aumentativo_mf[0], u'es raro')
                        forma_plural = aumentativo_mf[0] + u's'
                    flexion.setdefault(etiqueta_aumentativo, []).append(forma_plural)
            if aumentativo_mf[-1][-1] == u'a':
                # Hay una forma distinta para el femenino. Se añade
                if SINGULAR in numeros_disponibles:
                    etiqueta_aumentativo = encabezado_eagles + FEMENINO + SINGULAR + pie_eagles
                    etiqueta_aumentativo = etiqueta_aumentativo[:6] + AUMENTATIVO + etiqueta_aumentativo[7:]
                    flexion.setdefault(etiqueta_aumentativo, []).append(aumentativo_mf[-1])
                if PLURAL in numeros_disponibles:
                    etiqueta_aumentativo = encabezado_eagles + FEMENINO + PLURAL + pie_eagles
                    etiqueta_aumentativo = etiqueta_aumentativo[:6] + AUMENTATIVO + etiqueta_aumentativo[7:]
                    flexion.setdefault(etiqueta_aumentativo, []).append(aumentativo_mf[-1] + u's')

        # DIMINUTIVOS
        for diminutivo_mf in acepcion.get_diminutivos():
            if diminutivo_mf[0][-1] != u'a':
                if SINGULAR in numeros_disponibles:
                    # Tenemos cuidado con la etiqueta porque puede ser adjetivo o nombre, y cambia la posición
                    etiqueta_diminutivo = encabezado_eagles + MASCULINO + SINGULAR + pie_eagles
                    etiqueta_diminutivo = etiqueta_diminutivo[:6] + DIMINUTIVO + etiqueta_diminutivo[7:]
                    flexion.setdefault(etiqueta_diminutivo, []).append(diminutivo_mf[0])
                if PLURAL in numeros_disponibles:
                    etiqueta_diminutivo = encabezado_eagles + MASCULINO + PLURAL + pie_eagles
                    etiqueta_diminutivo = etiqueta_diminutivo[:6] + DIMINUTIVO + etiqueta_diminutivo[7:]
                    if diminutivo_mf[0][-2:] == u'ín':
                        forma_plural = diminutivo_mf[0][:-2] + u'ines'
                    elif diminutivo_mf[0][-1:] == u'o':
                        forma_plural = diminutivo_mf[0] + u's'
                    else:
                        forma_plural = diminutivo_mf[0] + u'es'
                    flexion.setdefault(etiqueta_diminutivo, []).append(forma_plural)
            if diminutivo_mf[-1][-1] == u'a':
                # Hay una forma distinta para el femenino. Se añade
                if SINGULAR in numeros_disponibles:
                    etiqueta_diminutivo = encabezado_eagles + FEMENINO + SINGULAR + pie_eagles
                    etiqueta_diminutivo = etiqueta_diminutivo[:6] + DIMINUTIVO + etiqueta_diminutivo[7:]
                    flexion.setdefault(etiqueta_diminutivo, []).append(diminutivo_mf[-1])
                if PLURAL in numeros_disponibles:
                    etiqueta_diminutivo = encabezado_eagles + FEMENINO + PLURAL + pie_eagles
                    etiqueta_diminutivo = etiqueta_diminutivo[:6] + DIMINUTIVO + etiqueta_diminutivo[7:]
                    flexion.setdefault(etiqueta_diminutivo, []).append(diminutivo_mf[-1] + u's')
        if categoria == SUSTANTIVO or (categoria == ADJETIVO and hay_nombres):
            if categoria == ADJETIVO:
                a = 1
            # Creamos los diminutivos, pero solo para los sustantivos o adjetivos que puedan serlo en alguna
            # acepción.
            # Primero sacamos las formas masculinas y femeninas (usamos 4 diminutivos) en singular y luego
            # vemos cuáles son válidas y cuáles no, si debemos o no pluralizar, y les asignamos la etiqueta
            # que les corresponda.
            formas_sin_tilde = [Palabra(fe, calcula_alofonos=False, organiza_grafemas=True).set_tilde(False)
                                for fe in formas_expandidas]
            if len(formas_expandidas) == 2 and formas_sin_tilde[1] not in [formas_sin_tilde[0] + u'a',
                                                                           formas_sin_tilde[0][:-1] + u'a']:
                # La forma femenina es "atípica" como en alcalde, desa; zar, rina...
                # En estos casos creamos el diminutivo de la forma femenina directamente sobre la forma
                # femenina, y no como la forma femenina del diminutivo de la forma masculina (como lector, ra
                # -> lectorcito y lectorCita, que añade la C porque la toma del diminutivo masculino).
                # print(u'Creando diminutivo femenino distinto para', lema_rae_txt)
                diminutivos_ms = Flexionador.crea_diminutivo(formas_expandidas[0], genero=MASCULINO)
                diminutivos_fs = Flexionador.crea_diminutivo(formas_expandidas[1], genero=FEMENINO)
            else:
                # En principio tenemos la variación en género habitual, con una -a final que se añade o
                # sustituye a la última vocal. Creamos la forma masculina del diminutivo y de ahí crearemos
                # la forma femenina.
                # Los nombres masculinos acabados en -a(s), la mantienen en el diminutivo: un problemita, un
                # mapita, un piratilla, un atlitas (excepto "manita").
                # A los femeninos en -o(s) les pasa lo mismo: una motito, una fotillo.
                # En estos casos, usamos el género contrario al crear el diminutivo, aunque luego lo
                # etiquetaremos correctamente.
                if MASCULINO in generos_disponibles and\
                        (formas_expandidas[0][-1] == u'a' or formas_expandidas[0][-2:] == u'as'):
                    diminutivos_ms = Flexionador.crea_diminutivo(formas_expandidas[0], genero=FEMENINO)
                else:
                    diminutivos_ms = Flexionador.crea_diminutivo(formas_expandidas[0], genero=MASCULINO)

                if FEMENINO in generos_disponibles and lema_rae_txt != u'mano' and\
                        (formas_expandidas[-1][-1] == u'o' or formas_expandidas[-1][-2:] == u'os'):
                    diminutivos_fs = Flexionador.crea_diminutivo(formas_expandidas[0], genero=MASCULINO)
                else:
                    # La forma femenina se forma feminizando el diminutivo masculino, y no a partir de la
                    # forma femenina
                    diminutivos_fs = [d_ms[:-2] + u'as' if d_ms[-1] == u's' else
                                      (d_ms[:-1] + u'a') if d_ms[-2:] != u'ín' else
                                      (d_ms[:-2] + u'ina') for d_ms in diminutivos_ms]
            # Hemos sacado las formas singulares de los diminutivos, tanto masculinas como femeninas.
            # Las usaremos para crear el plural si hace falta, y las meteremos si se acepta el singular.
            for orden_diminutivo, diminutivo_ms in enumerate(diminutivos_ms):
                diminutivo_fs = diminutivos_fs[orden_diminutivo]
                es_ambiguo = False
                if SINGULAR in numeros_disponibles:
                    numero = SINGULAR if diminutivo_ms[-1] != u's' or PLURAL not in numeros_disponibles else\
                        INVARIABLE
                    if MASCULINO in generos_disponibles:
                        es_ambiguo = FEMENINO in generos_disponibles and diminutivo_ms == diminutivo_fs
                        genero = AMBIGUO if es_ambiguo else MASCULINO
                        etiqueta_diminutivo = encabezado_eagles + genero + numero +\
                            pie_eagles[:int(len(pie_eagles) / 2)] + DIMINUTIVO +\
                            pie_eagles[-int(len(pie_eagles) / 2):]
                        if diminutivo_ms not in flexion.setdefault(etiqueta_diminutivo, []):
                            flexion[etiqueta_diminutivo].append(diminutivo_ms)
                    if FEMENINO in generos_disponibles and not es_ambiguo:
                        etiqueta_diminutivo = encabezado_eagles + FEMENINO + numero +\
                            pie_eagles[:int(len(pie_eagles) / 2)] + DIMINUTIVO +\
                            pie_eagles[-int(len(pie_eagles) / 2):]
                        if diminutivo_fs not in flexion.setdefault(etiqueta_diminutivo, []):
                            flexion[etiqueta_diminutivo].append(diminutivo_fs)
                if PLURAL in numeros_disponibles:
                    numero = PLURAL if diminutivo_ms[-1] != u's' or SINGULAR not in numeros_disponibles\
                        else INVARIABLE
                    es_ambiguo = FEMENINO in generos_disponibles and MASCULINO in generos_disponibles and\
                        diminutivo_ms == diminutivo_fs
                    if es_ambiguo:
                        # print(u'Coño', lema_rae_txt, u'tiene un diminutivo ambiguo en género:', diminutivo_ms, fuente)
                        pass
                    for genero, diminutivo_s in [(MASCULINO, diminutivo_ms), (FEMENINO, diminutivo_fs)]:
                        if genero in generos_disponibles and (genero != FEMENINO or not es_ambiguo):
                            # Añadimos una "s" para el plural salvo que el diminutivo singular ya la
                            # incluyera, o si el propio sustantivo sin diminutivo en plural no la tuviera
                            if diminutivo_s[-1] == u's' or\
                                    flexion[encabezado_eagles +
                                            (AMBIGUO
                                             if (len(generos_disponibles) == 2 and
                                                 len(formas_expandidas) == 1) else generos_disponibles[0]) +
                                            (INVARIABLE
                                             if (len(numeros_disponibles) == 2 and
                                                 formas_expandidas[0] == formas_plural[0][0]) else PLURAL) +
                                            pie_eagles][0][-1] != u's':
                                diminutivo_p = diminutivo_s
                            else:
                                diminutivo_p = (diminutivo_s + u's') \
                                    if diminutivo_s[-2:] != u'ín' else (diminutivo_s[:-2] + u'ines')
                            genero = AMBIGUO if es_ambiguo else genero
                            etiqueta_diminutivo = encabezado_eagles + genero + numero + \
                                pie_eagles[:int(len(pie_eagles) / 2)] + DIMINUTIVO + \
                                pie_eagles[-int(len(pie_eagles) / 2):]
                            if diminutivo_p not in flexion.setdefault(etiqueta_diminutivo, []):
                                flexion[etiqueta_diminutivo].append(diminutivo_p)
        # Las metemos en el diccionario de flexión añadiendo los datos de la acepción
        flexion_completa = {etiqueta_eagles: {forma_txt: [fuente] for forma_txt in formas_txt}
                            for etiqueta_eagles, formas_txt in flexion.items()}

        return flexion_completa

    @staticmethod
    def crea_diminutivo(lema_txt, genero=MASCULINO):
        u"""Se devuelven las formas diminutivas del lema de entrada (forma masculina singular), que debe ser un nombre.

        :param lema_txt:
        :param genero:
        :return:
        """
        # https://www.academia.edu/5888100/_Morfofonolog%C3%ADa_de_la_formaci%C3%B3n_de_diminutivos_en_espa%C3%B1ol_reglas_morfol%C3%B3gicas_o_restricciones_fonol%C3%B3gicas_en_A._F%C3%A1bregas_et_alii_eds._Los_l%C3%ADmites_de_la_Morfolog%C3%ADa._Estudios_ofrecidos_a_Soledad_Varela_Ortega_Madrid_UAM_2012_p%C3%A1gs._55-78_en_colaboraci%C3%B3n_con_Th%C3%A9ophile_Ambadiang_
        if lema_txt == lema_txt.upper():
            # Es una sigla, no hay diminutivo
            return u''
        raiz_flexiva = u''
        infijo = u''
        posfijo = u''
        imprime = False
        palabra_sin_tilde = Palabra(palabra_texto=lema_txt,
                                    calcula_alofonos=True,
                                    organiza_grafemas=True)
        silabas = palabra_sin_tilde.get_silabas()
        forma_sin_tilde = palabra_sin_tilde.set_tilde(con_tilde=False)
        if not palabra_sin_tilde.get_silabas():
            # Entre los nombres, están los de las letras: "b". No tienen sílabas
            return []
        elif len(lema_txt) == 1:
            # Son vocales y cosas así que no tienen diminutivo
            return []
        elif lema_txt[-3:] in [u'dad', u'tud']:
            # Son nombres (abstractos) derivados de adjetivos. Cosas como: honestidad(c)ita, humildad(c)ita...
            return []
        elif len(silabas) == 1:
            # Monosílabo
            if not silabas[-1].get_fonemas_ataque():
                return []
            if lema_txt[-1] in u'mn':  # OJO: la "r" no: florecilla, marecillo...
                raiz_flexiva, infijo = forma_sin_tilde, u'c'
            elif silabas[-1].get_fonemas_coda() or (silabas[-1].get_fonema_semivocal() and lema_txt[-1] == u'y'):
                raiz_flexiva, infijo = forma_sin_tilde, u'ec'
            elif silabas[-1].get_fonema_semiconsonante() and lema_txt[-1] == u'e':
                # Básicamente, pie.
                raiz_flexiva, infijo = forma_sin_tilde, u'cec'
            else:
                return []
        else:
            if not silabas[-1].get_fonemas_coda() and silabas[-1].get_fonema_semivocal():
                # Aunque no queda muy claro ni en la RAE, todas las palabras no monosílabas con diptongo
                # final, meten una "c": bonsaicito, hockeicito, espraicito
                raiz_flexiva, infijo = forma_sin_tilde[:-1] + forma_sin_tilde[-1].replace(u'y', u'i'), u'c'
            elif len(silabas) == 2:
                # BISÍLABOS
                if lema_txt[-1] in u'áéíóúmnr':
                    raiz_flexiva, infijo = forma_sin_tilde, u'c'
                if palabra_sin_tilde.get_posicion_tonica() == -1:
                    # AGUDOS
                    if lema_txt[-1] in u'lsz':
                        raiz_flexiva = forma_sin_tilde
                    if lema_txt[-1] in u'áéíóú':
                        raiz_flexiva, infijo = forma_sin_tilde, u'c'
                elif palabra_sin_tilde.get_posicion_tonica() == -2:
                    # LLANOS
                    # Vemos si hay diptongo ie o ue en la penúltima sílaba. Usualmente se consonantizan, así que lo
                    # buscamos directamente en el texto de la sílaba (hierba -> jerba -sin diptongo-)
                    if re.findall(u'ie|ue', silabas[-2].transcribe_ortograficamente_silaba(False, False)):
                        # DIPTONGO INICIAL
                        if lema_txt[-1] in u'ao':
                            raiz_flexiva, infijo = forma_sin_tilde[:-1], u'ec'
                        elif lema_txt[-1] in u'ieu':
                            raiz_flexiva, infijo = forma_sin_tilde[:-1], u'ec'
                    if not raiz_flexiva and lema_txt[-2:] in [u'ia', u'io', u'ua']:
                        # DIPTONGO FINAL
                        if lema_txt in [u'agua', u'fragua', u'yegua']:
                            raiz_flexiva = forma_sin_tilde[:-1]
                        else:
                            raiz_flexiva, infijo = forma_sin_tilde[:-1], u'ec'
                    elif lema_txt[-2:] in [u'ío', u'ía']:
                        # En papers hablan de "friecito", pero yo creo que no: guiíta, friíto, liíto, riíto...
                        raiz_flexiva = forma_sin_tilde[:-1]
                    elif lema_txt[-1] == u'e':
                        raiz_flexiva, infijo = forma_sin_tilde[:-1], u'ec'
                    elif lema_txt[-2:] in [u'is', u'es']:
                        raiz_flexiva, infijo = forma_sin_tilde[:-1], u'c'

            if not raiz_flexiva:
                if lema_txt[-2:] in [u'os', u'as']:
                    raiz_flexiva, posfijo = forma_sin_tilde[:-2], u's'
                elif lema_txt[-1] in u'oa':
                    raiz_flexiva = forma_sin_tilde[:-1]
                elif lema_txt[-1] in u'mnríéáóú':
                    raiz_flexiva, infijo = forma_sin_tilde, u'c'
                elif lema_txt[-1] in u'lsz':
                    raiz_flexiva = forma_sin_tilde
                elif (lema_txt[-1] in u'kptbdxfjcv') or (lema_txt[-2:] in [u'ch', u'll']):
                    raiz_flexiva = forma_sin_tilde
                elif lema_txt[-1] in u'g':
                    # Esto es un poco inventado, para que haga: tuareg -> tuaregcito
                    raiz_flexiva, infijo = forma_sin_tilde, u'c'
                elif not silabas[-1].get_fonema_semivocal() and not silabas[-1].get_fonemas_coda():
                    raiz_flexiva = forma_sin_tilde[:-1]

        if not raiz_flexiva:
            print(u'No sabemos hacer el diminutivo de', lema_txt)
            return []

        # Ajustamos el empalme de la raíz flexiva
        if raiz_flexiva[-1] in u'z':
            # Esté al final del lema o antes, siempre cambia a c
            raiz_flexiva = raiz_flexiva[:-1] + u'c'
        elif raiz_flexiva[-1] in u'cg':
            if len(raiz_flexiva) < len(lema_txt) and lema_txt[len(raiz_flexiva)] in u'aouáóú' and\
                    (not infijo or infijo[0] == u'e'):
                raiz_flexiva = raiz_flexiva[:-1] + {u'c': u'qu', u'g': u'gu'}[raiz_flexiva[-1]]
        elif raiz_flexiva[-2:] == u'gu':
            if len(raiz_flexiva) < len(lema_txt) and lema_txt[len(raiz_flexiva)] in u'aoáó' and\
                    (not infijo or infijo[0] == u'e'):
                raiz_flexiva = raiz_flexiva[:-1] + u'ü'

        if imprime:
            print(u'Diminutivo para', lema_txt, u'->', raiz_flexiva + infijo + u'it@' + ((posfijo) if posfijo else u''))
        # Diminutivos hay muchos, pero nos quedamos con los más habituales. Otros son menos comunes y pienso
        # que no tiene mucho sentido: caballito, caballico, caballillo, caballín se crean.
        # caballuelo, caballete, caballejo, caballuco, caballiño... no se crean.
        diminutivos = []
        if genero in [MASCULINO, AMBIGUO]:
            diminutivos += [u'ito', u'illo', u'ín', u'ico']
        if genero in [FEMENINO, AMBIGUO]:
            diminutivos += [u'ita', u'illa', u'ina', u'ica']

        return [raiz_flexiva + infijo + (diminutivo if diminutivo != u'ín' or not posfijo else u'in') +
                (((u'e' if diminutivo == u'ín' else u'') + posfijo) if posfijo else u'')
                for diminutivo in diminutivos]

    @staticmethod
    def crea_superlativo(lema_txt):
        u"""Se devuelve la forma superlativa del lema de entrada (forma masculina singular), que debe ser un adjetivo.

        :param lema_txt:
        :return:
        """
        # Alguna información aquí: http://lema.rae.es/dpd/srv/search?id=UByFr5964D6oCGp9V4
        formas_derivadas = []
        palabra_sin_tilde = Palabra(palabra_texto=lema_txt,
                                    calcula_alofonos=True,
                                    organiza_grafemas=True)
        tilde_diacritica = copy.deepcopy(palabra_sin_tilde).ajusta_tildes() != lema_txt
        forma_sin_tilde = palabra_sin_tilde.set_tilde(con_tilde=False)
        if tilde_diacritica:
            # Estos adjetivos no tienen forma sintética de superlativo.
            pass
        elif len(palabra_sin_tilde.get_silabas()) < 2:  # Es "< 2" y no "== 1" porque hay letras (plan "b") sin sílabas
            # La práctica mayoría no admite un -ísimo, al menos, no sin confundirlo con otro lema.
            # print(lema_txt, u'es un adjetivo muy corto y no necesita la forma -ísimo')
            pass
        elif lema_txt[-3:] == u'ble':
            # Son todos llanos: basta quitar la tilde (puede haberla en hiatos: "extraíble")
            formas_derivadas.append(forma_sin_tilde[:-3] + u'bilísimo')
        elif lema_txt[-1] in u'lr':
            if lema_txt[-2:] == u'or' and Palabra(palabra_texto=lema_txt, calcula_alofonos=False,
                                                  organiza_grafemas=True).get_posicion_tonica() == -1:
                # Acabadas en -or (usualmente -dor) tónica meten -c-: mayorcísimo, trabajadorcísimo, luchadorcísimo...
                # Si es átona (solo júnior y sénior) o acaba en otra vocal no lo meten: cautelarísima, amauterísimo...
                formas_derivadas.append(forma_sin_tilde + u'císimo')
            else:
                formas_derivadas.append(forma_sin_tilde + u'ísimo')
        elif lema_txt[-1] in u'z':
            formas_derivadas.append(forma_sin_tilde[:-1] + u'císimo')
        elif lema_txt[-1] in u'n':
            if lema_txt in [u'común', u'campeón']:
                formas_derivadas.append(forma_sin_tilde + u'ísimo')
            else:
                formas_derivadas.append(forma_sin_tilde + u'císimo')
        elif palabra_sin_tilde.get_silaba(-1).get_grafemas_coda():
            # Por lo general tenemos una -s. Si hay cualquier otra letra, no creamos la forma en -ísimo.
            # Solo hacemos el -ísimo de los adjetivos acabados en -és: francesísimo, aragonesísimo...
            # El resto tiene todavía menos sentido: antidisturbiosísimo, unisexísimo, tuaregísimo...
            if lema_txt[-2:] == u'és':
                formas_derivadas.append(forma_sin_tilde + u'ísimo')
        elif lema_txt[-1] in u'ieao':
            if lema_txt in [u'cursi']:
                formas_derivadas.append(forma_sin_tilde + u'lísimo')
            elif palabra_sin_tilde.get_silaba(-1).get_fonema_semiconsonante():
                # Diptongo creciente. No hay triptongos (los hay, pero en -"y", con lo que no llegan aquí)
                if palabra_sin_tilde.get_silaba(-1).get_fonema_semiconsonante().get_fonema_ipa() == u'j':
                    # No hay adjetivos en -ie, solo en -ia/-io
                    formas_derivadas.append(forma_sin_tilde[:-2] + u'ísimo')
                else:
                    # Acaba en diptongo creciente -ue/-ua/-uo. Existe un adjetivo en -ui: saharaui -> saharauísimo
                    if len(lema_txt) > 2 and lema_txt[-3:-1] in [u'gu']:
                        # Acaba en -gua/-guo
                        formas_derivadas.append(forma_sin_tilde[:-2] + u'üísimo')
                    else:
                        # Acaba en -ue/-ua/-uo/-güe
                        formas_derivadas.append(forma_sin_tilde[:-1] + u'ísimo')
            else:  # elif not palabra_sin_tilde.get_silaba(-1).get_fonema_semivocal():
                # Ni semiconsonante ni semivocal (si tiene semivocal es en "y" y no entra aquí).
                # Acaba en vocal simple: se quita la vocal y añadimos -ísimo. Si la vocal final era abierta,
                # hay que adaptar la consonante.
                if lema_txt[-1] in u'ie':
                    formas_derivadas.append(forma_sin_tilde[:-1] + u'ísimo')
                elif lema_txt[-2] in u'cgz':
                    formas_derivadas.append(forma_sin_tilde[:-2] +
                                            {u'c': u'qu', u'g': u'gu', u'z': u'c'}[forma_sin_tilde[-2]] + u'ísimo')
                else:
                    formas_derivadas.append(forma_sin_tilde[:-1] + u'ísimo')
        elif lema_txt[-1] in u'íéáóú' or \
                palabra_sin_tilde.get_silaba(-1).get_fonema_semivocal() or lema_txt[-1] in u'uy':
            # No admite formas en -ísimo.
            pass
        else:
            print(u'No sabemos hacer el superlativo de', lema_txt)
        return formas_derivadas

    @staticmethod
    def flexiona_sust_adj_det_wik(acepcion, ajusta_lema):
        categoria = acepcion.get_categoria()
        if categoria == DETERMINANTE:
            print(u'La función flexiona_sust_adj_det_wik no flexiona bien los determinantes')
        lema = acepcion.get_lema_txt()
        if lema == u'madrileño':
            pass
        es_sustantivo_propio = PROPIO in acepcion.get_tipos()
        if len(acepcion.get_inflects()) > 1:
            # Es frecuente que haya un nombre, como afinadora, que aparezca con inflexión de nombre (afinadora/s) y como
            # === Forma adjetiva ===. Los encabezados de esta forma no los procesamos, pero suelen tener la inflexión
            # completa del adjetivo (4 formas) con otra etiqueta inflect.es.adj. Podríamos sacar los dos lemas, el de
            # nombre y el de adjetivo y estaría mejor. Sin embargo, tampoco pasa nada. El "problema" es que se generan
            # 4 formas de nombre, pero si el adjetivo existe y el nombre también, existen las 4 formas. Además, el lema
            # de adjetivo también aparece, con lo que no perderemos esas "otras" 4 formas.
            pass

        flexion_completa = {}
        for datos_inflect in acepcion.procesa_etiquetas_inflect():
            plantilla_inflect = datos_inflect["plantilla_inflect"]
            parametros = datos_inflect["parametros"]
            parametros_numericos = datos_inflect["parametros_numericos"]
            categoria_implicita = datos_inflect["categoria_implicita"]
            raiz = datos_inflect["raiz"]
            # SUSTANTIVOS
            if categoria == SUSTANTIVO:
                # Creamos los 2 primeros caracteres de la etiqueta y los 3 últimos. Los otros 2 son género y número.
                genero = acepcion.get_genero()
                es_sustantivo_plural = acepcion.get_numero() == PLURAL
                tipo = PROPIO if es_sustantivo_propio else COMUN
                encabezado_eagles = SUSTANTIVO + tipo
                clase_semantica = "SP" if acepcion.get_es_antroponimo() else "G0" if acepcion.get_es_toponimo() else "00"
                grado = acepcion.get_grado() if acepcion.get_grado() in [AUMENTATIVO, DIMINUTIVO] else "0"
                origen = COMPUESTO if COMPUESTO in acepcion.get_tipos()\
                    else DE_ADJETIVO if DE_ADJETIVO in acepcion.get_tipos()\
                    else DE_VERBO if DE_VERBO in acepcion.get_tipos() else "0"
                pie_eagles = clase_semantica + grado + origen
            # ADJETIVOS
            else:
                genero = ""  # Se determinará más adelante y variará entre formas
                es_sustantivo_plural = False
                # Los adjetivos sólo tienen un tipo
                tipo = acepcion.get_tipos()[0] if acepcion.get_tipos() else CALIFICATIVO
                grado = acepcion.get_grado()
                encabezado_eagles = ADJETIVO + tipo + grado
                funcion = acepcion.get_de_participio()
                pie_eagles = funcion

            # PARTE (más o menos) COMÚN
            if es_sustantivo_plural and plantilla_inflect != u'plur.tantum' and not es_sustantivo_propio:
                # Hay como 10, y son en realidad formas, así que no interesan (ya saldrán en su lema singular).
                flexion = {}
            elif plantilla_inflect in [u'-ón', u'agudo-cons']:
                vocal_base = parametros[1] if len(parametros) > 1 else u'o'
                vocal_ton = vocal_base if vocal_base in u'áéíóú' \
                    else {u'a': u'á', u'e': u'é', u'i': u'í', u'o': u'ó', u'u': u'ú'}[vocal_base]
                vocal_ato = {u'á': u'a', u'é': u'e', u'í': u'i', u'ó': u'o', u'ú': u'u'}[vocal_ton]
                consonante = parametros[2] if len(parametros) > 2 else u'n'
                # Si no hay género, es adjetivo, y esto corresponde al masculino.
                # De ovación -> ovación, ovaciones, será femenino, pero para letón -> letón, letones será masculino.
                if categoria_implicita == ADJETIVO:
                    # Creamos las cuatro formas. Además, la raíz se come la vocal final
                    flexion = {encabezado_eagles + "MS" + pie_eagles: [raiz + vocal_ton + consonante],
                               encabezado_eagles + "MP" + pie_eagles: [raiz + vocal_ato + consonante + u'es'],
                               encabezado_eagles + "FS" + pie_eagles: [raiz + vocal_ato + consonante + u'a'],
                               encabezado_eagles + "FP" + pie_eagles: [raiz + vocal_ato + consonante + u'as']}
                else:
                    genero = genero if genero else MASCULINO  # A veces hay adjetivos con flexión sustantiva
                    flexion = {encabezado_eagles + genero + SINGULAR + pie_eagles: [raiz + vocal_ton + consonante],
                               encabezado_eagles + genero + PLURAL + pie_eagles: [raiz + vocal_ato + consonante + u'es']}
            elif plantilla_inflect in [u'ad-lib', u'sg-pl', u'm-f-sg-pl']:
                formas_singular = [forma.strip() for forma in raiz.replace(u' o raramente ', u' ').
                                   replace(u' o ', u' ').replace(u', ', u' ').replace(u' / ', u' ').
                                   replace(u'<br/>', u' ').replace(u'<br>', u' ').split()
                                   if forma.strip()]
                if len(parametros) == 1:
                    # Hay algunas formas cuyo artículo está incorrectamente redactado y pasa esto.
                    # Hacemos un apaño.
                    parametros.append(raiz + u's')
                formas_plural = [forma.strip() for forma in parametros[1].replace(u' o raramente ', u' ').
                                 replace(u' o ', u' ').replace(u', ', u' ').replace(u' / ', u' ').
                                 replace(u'<br/>', u' ').replace(u'<br>', u' ').split() if forma.strip()]
                if len(parametros) == 2:
                    genero = genero if genero else AMBIGUO
                    flexion = {}
                    if formas_singular:
                        flexion[encabezado_eagles + genero + SINGULAR + pie_eagles] = formas_singular
                    if formas_plural:
                        flexion[encabezado_eagles + genero + PLURAL + pie_eagles] = formas_plural
                else:  # Se explicitan 4 formas MS, MP, FS, FP
                    # A veces la última forma no se incluye si es vacía
                    if len(parametros) == 3:
                        parametros.append(u'')
                    flexion = {}
                    if raiz and raiz == parametros[2]:
                        # Aunque se pongan los 4 parámetros, masc y fem coinciden -> género común
                        flexion[encabezado_eagles + "CS" + pie_eagles] = formas_singular
                    else:
                        formas_singular_f = [forma.strip() for forma in parametros[2].replace(u' o raramente ', u' ').
                                             replace(u' o ', u' ').replace(u', ', u' ').replace(u' / ', u' ').
                                             replace(u'<br/>', u' ').replace(u'<br>', u' ').split()
                                             if forma.strip()]
                        if formas_singular:
                            flexion[encabezado_eagles + "MS" + pie_eagles] = formas_singular
                        if formas_singular_f:
                            flexion[encabezado_eagles + "FS" + pie_eagles] = formas_singular_f
                    if parametros[1] == parametros[3]:
                        # Aunque se pongan los 4 parámetros, masc y fem coinciden -> ambiguo
                        flexion[encabezado_eagles + "CP" + pie_eagles] = formas_plural
                    else:
                        formas_plural_f = [forma.strip() for forma in parametros[3].replace(u' o raramente ', u' ').
                                           replace(u' o ', u' ').replace(u', ', u' ').replace(u' / ', u' ').
                                           replace(u'<br/>', u' ').replace(u'<br>', u' ').split()
                                           if forma.strip()]
                        if formas_plural:
                            flexion[encabezado_eagles + "MP" + pie_eagles] = formas_plural
                        if formas_plural_f:
                            flexion[encabezado_eagles + "FP" + pie_eagles] = formas_plural_f
            elif plantilla_inflect == u'invariante':
                if categoria_implicita == ADJETIVO:
                    # Tendremos un adjetivo acabado en -s, seguramente un compuesto tipo soplagaitas.
                    # Las 4 formas son iguales.
                    flexion = {encabezado_eagles + AMBIGUO + INVARIABLE + pie_eagles: [raiz]}
                else:
                    # Los nombres propios, suelen caer aquí. La norma EAGLES no contempla meter códigos de género y nº
                    # en los nombres propios, pero si se puede hacer, no veo el motivo por el que complicarse
                    # para hacer algo que es perder información a propósito.
                    genero = genero if genero else AMBIGUO if PROPIO not in acepcion.get_tipos()\
                        else FEMENINO if lema[-1].lower() == u'a' else MASCULINO
                    etiqueta_eagles = encabezado_eagles + genero +\
                        (PLURAL if es_sustantivo_plural else INVARIABLE if PROPIO not in acepcion.get_tipos()
                         else SINGULAR) + pie_eagles
                    flexion = {etiqueta_eagles: [lema]}
            elif plantilla_inflect == u'plur.tantum':
                genero = genero if genero else "C"
                flexion = {encabezado_eagles + genero + PLURAL + pie_eagles: [lema]}
            elif plantilla_inflect == u'reg':
                # En adjetivos, se come la -o final de la forma masculina singular
                # {{inflect.es.sust.reg|casa}} -> casa, casas; {{inflect.es.adj.reg|alt}} -> alto, altos, alta, altas
                if categoria_implicita == ADJETIVO:
                    # Creamos las cuatro formas. Además, la raíz se come la vocal final
                    flexion = {encabezado_eagles + "MS" + pie_eagles: [raiz + u'o'],
                               encabezado_eagles + "MP" + pie_eagles: [raiz + u'os'],
                               encabezado_eagles + "FS" + pie_eagles: [raiz + u'a'],
                               encabezado_eagles + "FP" + pie_eagles: [raiz + u'as']}
                else:
                    genero = genero if genero else "M"  # A veces hay adjetivos con flexión sustantiva
                    flexion = {encabezado_eagles + genero + SINGULAR + pie_eagles: [raiz],
                               encabezado_eagles + genero + PLURAL + pie_eagles: [raiz + (u's' if raiz[-1] != u's' else u'')]}
            elif plantilla_inflect == u'no-género':
                flexion = {encabezado_eagles + "CS" + pie_eagles: [raiz],
                           encabezado_eagles + "CP" + pie_eagles: [raiz + u's']}
            elif plantilla_inflect in [u'reg-cons', u'no-género-cons']:
                consonante = parametros[1] if len(parametros) > 1 else u''
                raiz_plural = parametros[2] if len(parametros) > 2 \
                    else parametros_numericos["3"] if "3" in parametros_numericos else raiz
                if categoria_implicita == ADJETIVO and plantilla_inflect == u'reg-cons':  # alto, altos, alta, altas
                    # Creamos las cuatro formas. Además, la raíz se come la vocal final
                    flexion = {encabezado_eagles + "MS" + pie_eagles: [raiz + consonante],
                               encabezado_eagles + "MP" + pie_eagles: [raiz_plural + NEXOS_IE[consonante] + u'es'],
                               encabezado_eagles + "FS" + pie_eagles: [raiz + consonante + u'a'],
                               encabezado_eagles + "FP" + pie_eagles: [raiz + consonante + u'as']}
                else:  # coche, coches, o par, pares
                    genero = genero if genero else "C"
                    flexion = {encabezado_eagles + genero + SINGULAR + pie_eagles: [raiz + consonante],
                               encabezado_eagles + genero + PLURAL + pie_eagles: [raiz_plural + NEXOS_IE[consonante] + u'es']}
            elif plantilla_inflect in [u'sg', u'sing.tantum']:
                genero = genero if genero else "C"
                flexion = {encabezado_eagles + genero + SINGULAR + pie_eagles: [lema]}
            elif plantilla_inflect == u'í':
                # Si no está el parámetro 2=, la forma tiene un único género (rubí, rubíes/rubís, masculino),
                # si está, es ambiguo en género (ceutí, ceutí(e)s)
                genero = genero if genero and "2" in parametros_numericos\
                    else "C" if categoria_implicita == ADJETIVO else "M"
                flexion = {encabezado_eagles + genero + SINGULAR + pie_eagles: [lema],
                           encabezado_eagles + genero + PLURAL + pie_eagles: [lema + u's', lema + u'es']}
            else:
                # En realidad no hay ninguna más
                flexion = {}

            superlativos = datos_inflect["superlativos"]
            if categoria == ADJETIVO:
                if superlativos:
                    # Hay adjetivos que contienen en la flexión el codigo sup= o sup2= para indicar el superlativo.
                    # Podemos considerar que estas formas son partes o no de este lema, pero vamos a añadirlos.
                    encabezado_eagles_sup = encabezado_eagles[:2] + SUPERLATIVO  # Marca de superlativo
                    flexion[encabezado_eagles_sup + "MS" + pie_eagles] = superlativos
                    flexion[encabezado_eagles_sup + "MP" + pie_eagles] = [s + u's' for s in superlativos]
                    flexion[encabezado_eagles_sup + "FS" + pie_eagles] = [s[:-1] + u'a' for s in superlativos]
                    flexion[encabezado_eagles_sup + "FP" + pie_eagles] = [s[:-1] + u'as' for s in superlativos]

            # Hay algunos nombres y adjetivos que solo van en plural o singular. Deberíamos eliminar esas formas
            # (que es muchísimo más sencillo que no haberlas creado en primera instancia), pero no lo haremos así.
            # Si el lema solo tiene plural, sí que eliminaremos los singulares. Pero no eliminamos los plurales.
            if not datos_inflect["tiene_singular"]:
                posicion_numero = 3 if categoria == SUSTANTIVO else 4
                flexion = {etiqueta_eagles: formas_txt for etiqueta_eagles, formas_txt in flexion.items()
                           if etiqueta_eagles[posicion_numero] == PLURAL}

            # Las metemos en el diccionario de flexión
            fuente = u'wik|' + str(acepcion.get_n_entrada()) + u'|' + str(acepcion.get_n_acepcion())
            for etiqueta_eagles, formas_txt in flexion.items():
                if etiqueta_eagles not in flexion_completa:
                    flexion_completa[etiqueta_eagles] = {}
                for forma_txt in formas_txt:
                    flexion_completa[etiqueta_eagles][forma_txt] =\
                        flexion_completa[etiqueta_eagles].setdefault(forma_txt, []) + [fuente]

            if ajusta_lema:
                # Vamos a cambiar el lema a la forma masculina singular (o invariante en número) si existe
                prioridades = [encabezado_eagles + tag + pie_eagles
                               for tag in ["CS", "CN", "CP", "MS", "MN", "MP", "FS", "FN", "FP"]]
                for etiqueta_eagles in prioridades:
                    if etiqueta_eagles in flexion_completa:
                        acepcion.set_lema_txt(list(flexion_completa[etiqueta_eagles].keys())[0])
                        break
        if categoria == DETERMINANTE:
            if lema == u'lo':
                return {DETERMINANTE + ARTICULO_D + NA + NA + SINGULAR + NA: {lema: [u'wik|0|0']}}
            else:
                return {DETERMINANTE + (ARTICULO_D if u'l' in lema else ARTICULO_I) + etiqueta_eagles[2:]: formas
                        for etiqueta_eagles, formas in flexion_completa.items()}
        else:
            return flexion_completa

    @staticmethod
    def flexiona_verbo(acepcion, ajusta_lema, incluye_cliticos, transitividad=TRANSITIVO):
        if acepcion.get_origen() == "rae":
            return Flexionador.flexiona_verbo_rae(acepcion, incluye_cliticos)
        else:
            return Flexionador.flexiona_verbo_wik(acepcion, ajusta_lema, incluye_cliticos, transitividad)

    @staticmethod
    def flexiona_verbo_rae(acepcion, incluye_cliticos):
        # Sobre las combinaciones de transitividad y pronominalidad/reflexividad/reciprocidad, se puede ver:
        # http://hispanoteca.eu/Gram%C3%A1ticas/Gram%C3%A1tica%20espa%C3%B1ola/Verbos%20pronominales.htm
        lema_rae_txt = acepcion.get_lema_rae_txt()
        tipo = COPULATIVO if acepcion.get_es_copulativo() else AUXILIAR if acepcion.get_es_auxiliar() else PRINCIPAL
        # if tipo != PRINCIPAL:
        #     print(lema_rae_txt, u'es un verbo de tipo', tipo)
        encabezado_eagles = VERBO + tipo
        es_transitivo = acepcion.get_es_transitivo()
        es_intransitivo = acepcion.get_es_intransitivo()
        transitividad = TRANSITIVO if es_transitivo else INTRANSITIVO if es_intransitivo else "0"
        impersonalidad = IMPERSONAL if acepcion.get_es_impersonal() else "0"  # Impersonales solo en 3ª y sin imperativo
        pronominalidad = PRONOMINAL if lema_rae_txt[-2:] == u'se' or acepcion.get_es_pronominal() else "0"
        uso = DESUSADO if acepcion.get_es_desusado() else POCO_USADO if acepcion.get_es_poco_usado() else "0"
        pie_eagles = transitividad + impersonalidad + pronominalidad + uso
        fuente = u'rae|' + str(acepcion.get_n_entrada()) + u'|' + str(acepcion.get_n_acepcion())
        if acepcion.get_n_acepcion() == 0:
            # print(u'Tipo de verbo para', lema_rae_txt, u':', encabezado_eagles + pie_eagles, fuente)
            pass
        if False:
            # print(lema_rae_txt, u'es pronombre PERSONAL')
            for info in acepcion._datos.keys():
                if info in ["info_uso", "conjs", "es_transitivo", "es_intransitivo", "es_poco_usado", "es_desusado",
                            "es_pronominal", "es_impersonal", "es_copulativo", "es_reflexivo", "es_auxiliar"]:
                    # print(lema_rae_txt, u'Campo', info, u'en _datos y que procesamos:', acepcion._datos[info], fuente)
                    pass
                elif info in []:
                    # print(lema_rae_txt, u'Campo', info, u'en _datos y que ignoramos a propósito:', acepcion._datos[info], fuente)
                    pass
                elif info in ["es_locucion", "es_contraccion", "formas_atonas_txt", "forma_tonica_txt",
                              "forma_amalgamada_txt",
                              "es_forma_atona", "es_forma_tonica", "es_pronombre_amalgamado", "tipos", "es_desusado",
                              "es_poco_usado", "generos_disponibles", "numeros_disponibles", "formas_plural",
                              "masculino_ambiguo", "aumentativos", "diminutivos", "apocope_txt", "apocope_plural_txt",
                              "neutro_txt",
                              "superlativos_txt", "comparativo_txt", "tambien_superlativo_regular", "persona"]:
                    print(lema_rae_txt, u'Campo', info, u'en _datos y que no tenemos en cuenta:',
                        acepcion._datos[info], fuente, u'flexiona_verbo_rae')
                    pass
                else:
                    print(lema_rae_txt, u'Campo', info, u'en _datos desconocido', u'flexiona_verbo_rae')
            if "info_uso" in acepcion._datos:
                for info in acepcion._datos["info_uso"].keys():
                    if info in ["genero_alternativo", "numero_alternativo", "es_reflexivo", "es_impersonal",
                                "tipo_alternativo", "es_locucion", "era_usado", "es_auxiliar"]:
                        # print(lema_rae_txt, u'Campo', info, u'en info_uso y que procesamos:', acepcion._datos["info_uso"][info], fuente)
                        pass
                    elif info in ["categoria_alternativa", "posicion_alternativo"]:
                        print(lema_rae_txt, u'Campo', info, u'en info_uso y que ignoramos a propósito:',
                            acepcion._datos["info_uso"][info], fuente)
                        pass
                    elif info in ["desusado", "sin_articulo", "tipo_alternativo"]:
                        print(lema_rae_txt, u'Campo', info, u'en info_uso y que no tenemos en cuenta:',
                            acepcion._datos["info_uso"][info], fuente, u'flexiona_verbo_rae')
                        pass
                    else:
                        print(lema_rae_txt, u'Campo', info, u'en info_uso desconocido:',
                            acepcion._datos["info_uso"][info], fuente, u'flexiona_verbo_rae')

        # Los verbos suelen tener un valor de id_conj que nos lleva al archivo donde se encuentra la tabla que
        # reproduce su flexión. Algunas veces (59 verbos) tienen más de una, cuando hay variaciones fonéticas
        # (tran(s)portar, pos(t)poner, g/huaquear...). En este caso, la primera id_conj es la más usada, y la
        # segunda (no hay más) es la menos usada (que a veces es la más culta y a veces no).
        # También hay verbos con conjugaciones distintas según la entrada como 'enrocar' o 'aterrar'. Esto ocurre
        # porque tienen entradas distintas, una por parte de 'roque' o 'terror' (enroco, aterro) y otra por parte de
        # 'rueca' y 'tierra' (enrueco, entierro). Aunque esto es un fenómeno a nivel de las entradas de un lema, y por
        # tanto es invisible a este nivel (la acepción únicamente tiene una conj salvo el caso comentado arriba).
        # Por otra parte, en la RAE no se dan conjugaciones distintas cuando hay verbos impersonales que tienen una
        # variante que no lo es (como 'anochecer' o 'amanecer' en el sentido de 'hacerse de noche/día' o en el sentido
        # de 'terminar/comenzar el día': amanecimos en la playa, ¿dónde anocheciste?). En estos casos RAE da
        # la conjugación completa y santas pascuas, pero nosotros capamos la conjugación impersonal.

        # Pero puede ocurrir también que no haya ninguna id_conj. En estos casos, a veces hay otra entrada que
        # sí que la tiene para este mismo lema, pero ya se han tratado.
        # Si no hay id_conj es porque ninguna entrada del lema la tiene. Esto ocurre en 1.396 verbos (casi
        # nada), que no tienen esta información. De ellos, 1.064 son desusados, y el resto (332) suelen usarse
        # solo en ciertas regiones/ámbitos dialectales. No son muy importantes, pero hay algún verbo no tan
        # raro entre estos: potear, salsear, canear... Así que nos inventamos su flexión.
        # Para ello, echamos mano de las herramientas de AcepcionWik, que tiene métodos para calcular
        # la etiqueta de flexión, y para crear las formas flexionadas a partir de ella. El único pero es que
        # tenemos que modificar la etiqueta de flexión, y cambiar los "wik" a "rae".
        # TODO: quizá en un futuro modifique flexiona_verbo_wik para que devuelva las etiquetas completas (con
        # caracteres de transitividad, impersonalidad y demás).
        ids_conj = acepcion.get_conjs()
        if not ids_conj:
            conjs = AcepcionWik.infiere_conjs(lema_rae_txt, normativa=True, diptonguiza=False,
                                              hiatiza=False, cierra=False, impersonal=False)
            if acepcion.get_n_acepcion() == 0:
                # print(lema_rae_txt, u'(desusado)' if acepcion.get_es_desusado() else u'', u'no tiene ids de conjugación ->', conjs, fuente)
                pass

            # Hay un bonito método que hace una estimación de cuál debe de ser la conjugación de un verbo
            # según cómo acabe, pero vamos a hacer caso a la RAE, y pondremos únicamente el infinitivo.
            if False and acepcion.get_n_acepcion() == 0:
                print(conjs)
            acepcion_previa_wik = {"lema": lema_rae_txt, "cat": u'verbo', "infos": conjs}
            acepcion_wik = AcepcionWik(acepcion_previa_wik, "wik", acepcion.get_n_entrada(), acepcion.get_n_acepcion())
            # TODO: cuando el iar_inflector wik devuelva las etiquetas completas, mejorar esto de abajo
            flexion = Flexionador.flexiona_verbo_wik(acepcion_wik, ajusta_lema=True,
                                                     incluye_cliticos=True, transitividad=transitividad)
            flexion_completa = {}
            for etiqueta_eagles, formas_txt in flexion.items():
                etiqueta_eagles = encabezado_eagles + etiqueta_eagles[2:12] + pie_eagles
                if etiqueta_eagles not in flexion_completa:
                    flexion_completa[etiqueta_eagles] = {}
                for forma_txt in formas_txt:
                    flexion_completa[etiqueta_eagles][forma_txt] = \
                        flexion_completa[etiqueta_eagles].setdefault(forma_txt, []) + [fuente.replace(u'wik', u'rae')]
            return flexion_completa
        flexion_completa = {}
        if len(ids_conj) > 1 and acepcion.get_n_acepcion() == 0:
            # print(lema_rae_txt, u'tiene más de un id conj')
            pass
        # return flexion_completa  # BOOOOOOOOOORRRRRRRRRRRAAAAAAAAAMMMMMMMMMMMEEEEEEEEEEEEEEEEE
        directorio_conjugaciones = os.path.dirname(os.path.realpath(__file__)) + \
            u'/archivos_de_datos/rae/archivos_web/conjugaciones/'
        for id_conj in ids_conj:
            flexion = {}
            nombre_archivo_conj = glob.glob(directorio_conjugaciones + u'*.' + id_conj + u'.html')[0]
            with codecs.open(nombre_archivo_conj, encoding='utf-8') as archivo:
                texto_archivo = archivo.read().replace(u'/th', u'/td').replace(u'<th', u'<td')
            texto_archivo = texto_archivo.replace(u'<span class="f2">', u'').\
                replace(u'<span class="f3">', u'').replace(u'</span>', u'').\
                replace(u' u ', u' o ').replace(u', ', u' o ')
            # Como la estructura es una tabla, y no hay muchas excepciones, nos basta con usar una regexp
            tabla = [[td[td.find(u'>') + 1:] for td in re.findall(u'<td.*?>.*?(?=</td>)', tr)]
                     for tr in re.findall(u'(?<=<tr>).*?(?=</tr>)', texto_archivo)]
            # El infinitivo se extrae de la tabla y no del lema_rae_txt directamente debido a que hay verbos
            # con doble conjugación (doble id_conj), debido a variaciones ortográficas: remplazar/reemplazar,
            # ahuatar/aguatar, psicoanalizar/sicoanalizar... En estos casos, las variantes menos usadas
            # directamente no están incluidas en el lemario, sin embargo, sus formas aparecen en la
            # conjugación del lema más normal. Es decir, que el lema "desyerbar" no existe como tal, pero a
            # cambio, el lema "deshierbar" incluye las formas tanto de deshierbar como de desyerbar (incluido
            # en el infinitivo). El caso de pudrir/podrir es especial.
            infinitivo = tabla[2][3].split(u'/')[0][:-2] if lema_rae_txt[-2:] == u'se'\
                else tabla[2][3].split(u'/')[0]
            if infinitivo != (lema_rae_txt[:-2] if lema_rae_txt[-2:] == u'se' else lema_rae_txt):
                # print(len(ids_conj), u'conjugaciones.', u'Joder, el verbo', infinitivo,
                #     u'tiene algo raro con el infinitivo, que no concuerda con',
                #     lema_rae_txt[:-2] if lema_rae_txt[-2:] == u'se' else lema_rae_txt)
                pass
            flexion[INF] = [infinitivo]
            flexion[INF_P] = [infinitivo + u'se']
            if len(tabla) not in [58]:
                # Es más sencillo si metemos las columnas que faltan, y dejar que el algoritmo posterior sea
                # siempre de uso general.
                # 39: U. solo las formas cuya desinencia empieza por -i.: embaír
                # 22: U. solo en inf., ger., part. y en 3ª pers. (sin imperativo): acaecer, concernir, atañer
                # 20: U. solo en infinit. y en 3.ª pers.: empecer
                # 17: intr. impers. (sólo 3ªs de singular y sin imperativo): fenómenos meteorológicos
                # 9: U. solo en infinit. y en imper.: abarse
                # 5: U. solo en infinit. y en part.: usucapir
                # 3: U. solo en infinit. y ger.: raspahilar; U. solo en infinit.: adir
                tabla_vacia = [[u'', u'', u'', u'', u''] for i in range(58)]
                if len(tabla) == 3:
                    for fila_completa, fila_defectivo in [(2, 2)]:
                        tabla_vacia[fila_completa] = tabla[fila_defectivo]
                    tabla = tabla_vacia
                elif len(tabla) == 5:
                    for fila_completa, fila_defectivo in [(2, 2), (4, 4)]:
                        tabla_vacia[fila_completa] = tabla[fila_defectivo]
                    tabla = tabla_vacia
                elif len(tabla) == 9:
                    tabla_vacia[2] = tabla[2]
                    tabla = tabla_vacia[:52] + tabla[3:]
                elif len(tabla) == 17:
                    for fila_completa, fila_defectivo in [(2, 2), (4, 4), (9, 7), (18, 9), (27, 11), (37, 14),
                                                          (46, 16)]:
                        tabla_vacia[fila_completa] = tabla[fila_defectivo]
                    tabla = tabla_vacia
                elif len(tabla) == 20:
                    for fila_completa, fila_defectivo in [(2, 2), (9, 5), (13, 6), (18, 8), (22, 9), (27, 11),
                                                          (31, 12), (37, 15), (41, 16), (46, 18), (50, 19)]:
                        tabla_vacia[fila_completa] = tabla[fila_defectivo]
                    tabla = tabla_vacia
                elif len(tabla) == 22:
                    for fila_completa, fila_defectivo in [(2, 2), (4, 4), (9, 7), (13, 8), (18, 10), (22, 11),
                                                          (27, 13), (31, 14), (37, 17), (41, 18), (46, 20),
                                                          (50, 21)]:
                        tabla_vacia[fila_completa] = tabla[fila_defectivo]
                    tabla = tabla_vacia
                elif len(tabla) == 39:
                    tabla = tabla[:33] + tabla_vacia[33:52] + tabla[33:]
                else:
                    # Aquí no deberíamos llegar
                    print(u'Esto tiene que ser un error al parsear la conjugación')
                    flexion_completa = {etiqueta_eagles: {forma_txt: [fuente] for forma_txt in formas_txt}
                                        for etiqueta_eagles, formas_txt in flexion.items()}
                    return flexion_completa

            if len(tabla[2]) < 5 or not tabla[2][4]:  # Algunos verbos no tienen gerundio
                flexion[GER] = []
                flexion[GER_P] = []
            elif lema_rae_txt[-2:] == u'se':
                flexion[GER_P] = tabla[2][4].split(u' o ')
                flexion[GER] = [Palabra(palabra_texto=f[:-2],
                                        calcula_alofonos=False,
                                        organiza_grafemas=True).set_tilde(con_tilde=False)
                                for f in flexion[GER_P]]
            else:
                flexion[GER] = tabla[2][4].split(u' o ')
                flexion[GER_P] = [Palabra(palabra_texto=f,
                                          calcula_alofonos=False,
                                          organiza_grafemas=True).set_tilde(con_tilde=True) + u'se'
                                  for f in flexion[GER]]
            # El participio está en la quinta fila, cuarta columna. En ocasiones hay 2 formas, siendo la
            # segunda la irregular (usada más como adjetivo), y la 1ª es la acabada en ado/ido/ído, que se
            # usa en formas compuestas
            flexion[PAR_SM] = [] if not tabla[4][3] else tabla[4][3].split(u' o ')
            flexion[PAR_SF] = [] if not tabla[4][3] else [f[:-1] + u'a' for f in flexion[PAR_SM]]
            flexion[PAR_PM] = [] if not tabla[4][3] else [f[:-1] + u'os' for f in flexion[PAR_SM]]
            flexion[PAR_PF] = [] if not tabla[4][3] else [f[:-1] + u'as' for f in flexion[PAR_SM]]
            # if len(flexion[PAR_SM]) > 1:
            #     print(lema_rae_txt, u'tiene más de un participio:', u', '.join(flexion[PAR_SM]))

            # Si el verbo es impersonal sólo va en 3ª persona (terciopersonal) y no tiene imperativo.
            # Algunos verbos impersonales solo aparecen en singular (unipersonal) pero no los distinguimos.

            # Extraemos el presente de indicativo, que tiene diferencias con respecto al resto de tiempos.
            # Puede haber más de una forma (raigo o rayo) y se separan con el " o ". Además, si el lema es
            # pronominal, se incluye el pronombre en posición preclítica, y no nos interesa: me ababillo.
            # Por último, en los presentes se forma para la segunda persona del singular la forma de tú y de
            # vos separadas por " / ".
            if impersonalidad != IMPERSONAL:
                flexion[IP1S] = [] if not tabla[7][3] else [f.split()[-1] for f in tabla[7][3].split(u' o ')]
                flexion[IP2S] = [] if not tabla[8][3] or u'solo voseo' in tabla[8][3] else \
                    [f.split()[-1] for f in tabla[8][3].split(u' / ')[0].split(u' o ')]
                flexion[IP2V] = [] if not tabla[8][3] else \
                    [f.split()[-1] for f in tabla[8][3].split(u' / ')[1 if u'/' in tabla[8][3] else 0].split(u' o ')]
            if u'impersonal:' in tabla[9][3]:
                flexion[IP3S] = [u'ha', u'hay']
                if flexion[INF][0] != u'haber':
                    print(flexion[INF], u'tiene impersonal')
            else:
                flexion[IP3S] = [] if not tabla[9][3] else [f.split()[-1] for f in tabla[9][3].split(u' o ')]
            if impersonalidad != IMPERSONAL:
                flexion[IP1P] = [] if not tabla[11][3] else [f.split()[-1] for f in tabla[11][3].split(u' o ')]
                flexion[IP2P] = [] if not tabla[12][3] else [f.split()[-1] for f in tabla[12][3].split(u' o ')]
            flexion[IP3P] = [] if not tabla[13][3] else [f.split()[-1] for f in tabla[13][3].split(u' o ')]

            for etiquetas_eagles, fila, columna in POSICION_CONJUGACION:
                for orden, etiqueta_eagles in enumerate(etiquetas_eagles):
                    if impersonalidad != IMPERSONAL or etiqueta_eagles[4] == TERCERA:
                        flexion[etiqueta_eagles] = [] if not tabla[fila + orden + (1 if orden > 2 else 0)][columna] \
                            else [f.split()[-1]
                                  for f in tabla[fila + orden + (1 if orden > 2 else 0)][columna].split(u' o ')]
            # La RAE no muestra forma de voseo en el presente de subjuntivo. Afortunadamente, esta forma se
            # crea con la raíz cerrada seguida de la vocal temática tónica (e para 1ª, a para 2ª y 3ª), que
            # irá acentuada salvo que sea monosílabo, y seguida de 's'. Esta forma es exactamente la misma
            # que coger la de 2ª plural y quitarle la -i- del diptongo decreciente final: amé(i)s, bebá(i)s,
            # de(i)s, vivá(i)s...
            if impersonalidad != IMPERSONAL:
                flexion[SP2V] = [f[:-2] + u's' for f in flexion[SP2P]]

            # Extraemos el imperativo
            if impersonalidad == IMPERSONAL:
                # No tiene imperativo.
                pass
            elif lema_rae_txt[-2:] == u'se':
                # Es una forma pronominal. Creamos la forma no pronominal quitando la tilde si no es
                # por hiato, y quitamos el clítico también.
                flexion[MP2S_P] = [] if not tabla[54][3] or u'solo voseo' in tabla[54][3] else \
                    [f.split()[-1] for f in tabla[54][3].split(u' / ')[0].split(u' o ')]
                flexion[MP2V_P] = [] if not tabla[54][3] else \
                    [f.split()[-1] for f in tabla[54][3].split(u' / ')[-1].split(u' o ')]
                flexion[MP3S_P] = [] if not tabla[55][3] else \
                    tabla[55][3].split(u' o ')
                # La 1ª del plural se toma del presente de subjuntivo ("enroquémonos"), sin embargo, esa forma no lleva
                # el clítico reflexivo y debe llevarlo. Hay que quitarle la -s final y añadirle el -nos ("enroquémonos")
                # Como la palabra se vuelve esdrújula, lo silabeamos y demás para ponerle la tilda.
                pronombre = Palabra(palabra_texto=u'nos', calcula_alofonos=False, organiza_grafemas=True)
                flexion[MP1P_P] = [Palabra(silabas=Palabra(palabra_texto=variante,
                                                           calcula_alofonos=False,
                                                           organiza_grafemas=True).reset_coda(-1).get_silabas() +
                                                   pronombre.get_silabas(),
                                           calcula_alofonos=False,
                                           organiza_grafemas=True).ajusta_tildes()
                                   for variante in flexion[SP1P]]
                flexion[MP2P_P] = [] if not tabla[56][3] else tabla[56][3].split(u' o ')
                flexion[MP3P_P] = [] if not tabla[57][3] else tabla[57][3].split(u' o ')
                for etiqueta_eagles in [MP2S_P, MP2V_P, MP3S_P, MP1P_P, MP2P_P, MP3P_P]:
                    etiqueta_no_pronominal = etiqueta_eagles[:7] + "0" + etiqueta_eagles[8:]
                    flexion[etiqueta_no_pronominal] = []
                    for variante in flexion[etiqueta_eagles]:
                        variante_no_pron = Palabra(palabra_texto=variante,
                                                   calcula_alofonos=False,
                                                   organiza_grafemas=True).elimina_silaba(-1).ajusta_tildes()
                        # Normalmente basta con eliminar la última sílaba, que es el clítico y ajustar tildes,
                        # pero para la 1ª y 2ª del plural, se pierde la -s o -d final (salvo en "idos", pero
                        # ahí se pierde al eliminar la última sílaba:
                        # friámonos->friamo veámonos->veamo vayámonos->vayamo...
                        # freíos->freí veos->ve bebeos->bebé abríos->abrí idos->i estaos->está estate->está
                        if etiqueta_eagles == MP1P_P:
                            # Metemos la "s" perdida: friamos, veamos, bebamos, abramos, vayamos, estemos
                            variante_no_pron = Palabra(palabra_texto=variante_no_pron + u's',
                                                       calcula_alofonos=False,
                                                       organiza_grafemas=True).ajusta_tildes()
                        elif etiqueta_eagles == MP2P_P:
                            # Metemos la "d" caída: freíd, ved, bebed, abrid, id, estad (sin tilde salvo hiato)
                            variante_no_pron = Palabra(palabra_texto=variante_no_pron + u'd',
                                                       calcula_alofonos=False,
                                                       organiza_grafemas=True).ajusta_tildes()
                        # El algoritmo falla en imperativos con diacríticos: de, se -> dé (3ª sg), sé (2ª sg)
                        variante_no_pron = u'sé' if variante_no_pron == u'se' else \
                            u'dé' if variante_no_pron == u'de' else variante_no_pron
                        flexion[etiqueta_no_pronominal].append(variante_no_pron)
            else:
                # Es una forma no pronominal, tendremos que acentuar y meter el clítico.
                flexion[MP2S] = [] if not tabla[54][3] or u'solo voseo' in tabla[54][3] else \
                    tabla[54][3].split(u' / ')[0].split(u' o ')
                flexion[MP2V] = [] if not tabla[54][3] else \
                    [f.split()[-1] for f in tabla[54][3].split(u' / ')[-1].split(u' o ')]
                flexion[MP3S] = [] if not tabla[55][3] else tabla[55][3].split(u' o ')
                flexion[MP1P] = flexion[SP1P]  # Se usa la primera del plural del presente de subjuntivo
                flexion[MP2P] = [] if not tabla[56][3] else tabla[56][3].split(u' o ')
                flexion[MP3P] = [] if not tabla[57][3] else tabla[57][3].split(u' o ')
                # Añadimos todas las formas pronominales si el verbo es pronominal. Si no lo es, solo añadimos las
                # formaas que acaban en "se" y que de otra forma, no se generarían.
                for etiqueta_eagles, clitico in [(MP3S, u'se'), (MP3P, u'se')] if pronominalidad != PRONOMINAL else\
                        [(MP2S, u'te'), (MP2V, u'te'), (MP3S, u'se'), (MP1P, u'nos'), (MP2P, u'os'), (MP3P, u'se')]:
                    etiqueta_pronominal = etiqueta_eagles[:7] + "P" + etiqueta_eagles[8:]
                    pronombre = Palabra(palabra_texto=clitico, calcula_alofonos=False, organiza_grafemas=True)
                    elimina_coda = etiqueta_eagles == MP1P or\
                        ((etiqueta_eagles == MP2P) and flexion[INF][0] != u'ir')
                    # Cogemos la variante, silabeamos y quitamos la coda de la última sílaba si procede o no hacemos
                    # nada si no (se le pasa un valor len(variante) + 1 que es necesariamente mayor que el número de
                    # sílabas, con lo que reset_coda no hará nada), y se le añade el clítico. Como el clítico es
                    # átono se crea una palabra uniendo las sílabas de la variante y la del clítico, y como se
                    # mantiene la tonicidad de la variante, se ajusta finalmente la tilde.
                    flexion[etiqueta_pronominal] = [Palabra(silabas=Palabra(palabra_texto=variante,
                                                                            calcula_alofonos=False,
                                                                            organiza_grafemas=True).
                                                            reset_coda(-1 if elimina_coda else len(variante) + 1).
                                                            get_silabas() + pronombre.get_silabas(),
                                                            calcula_alofonos=False,
                                                            organiza_grafemas=True).ajusta_tildes()
                                                    for variante in flexion[etiqueta_eagles]]
            # Como hay verbos defectivos, al parsear la página de conjugación hemos creado (por facilidad) entradas en
            # el diccionario de flexión con etiquetas de las que no hay ninguna forma. Las eliminamos.
            for etiqueta_eagles in list(flexion.keys()):
                if not flexion[etiqueta_eagles]:
                    # Está vacío, no tiene formas. Lo eliminamos
                    flexion.pop(etiqueta_eagles)
            if incluye_cliticos:
                Flexionador.conjuga_cliticos(flexion, transitividad, impersonalidad, pronominalidad)

            # Como puede haber más de una conjugación, aquí vamos añadiendo lo que vamos obteniendo en las sucesivas
            # flexiones.
            # Todos los verbos se etiquetan por defecto comenzando por "VM" (verbo modal) porque todos los verbos son
            # así menos 6: haber, ser, estar, parecer, eser, seer. Esto se hace también por comodidad en la definición
            # de las constantes y tal.
            # Ahora ponemos el tipo correcto, y le añadimos los caracteres finales no estrictamente morfológicos.
            for etiqueta_eagles, formas_txt in flexion.items():
                etiqueta_eagles = encabezado_eagles + etiqueta_eagles[2:12] + pie_eagles
                if etiqueta_eagles not in flexion_completa:
                    flexion_completa[etiqueta_eagles] = {}
                for forma_txt in formas_txt:
                    flexion_completa[etiqueta_eagles][forma_txt] = \
                        flexion_completa[etiqueta_eagles].setdefault(forma_txt, []) + [fuente]

        # Flexionador.flexion_a_txt(flexion_completa, lema_rae_txt, imprime=True)
        return flexion_completa

    @staticmethod
    def flexiona_verbo_wik(acepcion, ajusta_lema, incluye_cliticos, transitividad=TRANSITIVO):
        lema_txt = acepcion.get_lema_txt()
        if lema_txt[-2:] == u'se':
            lema_txt = lema_txt[:-2]
            if ajusta_lema:
                # Cambiamos el lema para hacer coincidir la conjugación de verbos pronominales o no.
                acepcion.set_lema_txt(lema_txt)
        flexion_completa = {}
        for datos_conj in acepcion.procesa_etiquetas_conj():
            plantilla_conj = datos_conj["plantilla_conj"]
            raices = datos_conj["raices"]

            flexion = {}
            if plantilla_conj in [u'v.conj.-ie-i-ue-u-.ir', u'v.conj.-ie-ue-.ar', u'v.conj.-ie-ue-.er',
                                  u'v.conj.ar', u'v.conj.er', u'v.conj.ir', u'v.conj.ir.hiato']:
                if plantilla_conj == u'v.conj.ir.hiato':
                    datos_conj["raices"]["dip"] = datos_conj["raices"]["ton"]
                flexion = Flexionador.conjuga_vm(datos_conj)
            elif plantilla_conj in [u'v.conj.-ie-ue-.gar', u'v.conj.gar']:
                datos_conj["nexos"] = {"a": u'g', "i": u'gu'}
                AcepcionWik.calcula_raiz_tonica(datos_conj)
                flexion = Flexionador.conjuga_vm(datos_conj)
            elif plantilla_conj in [u'v.conj.-ie-ue-.zar', u'v.conj.cer', u'v.conj.cir', u'v.conj.zar', u'v.conj.izar']:
                datos_conj["nexos"] = {"a": u'z', "i": u'c'}
                if plantilla_conj == u'v.conj.izar':
                    raices["ton"] = raices["ato"] + u'í'
                    raices["ato"] += u'i'
                    raices["dip"] += u'í'
                    raices["cerr"] += u'i'
                else:
                    AcepcionWik.calcula_raiz_tonica(datos_conj)
                flexion = Flexionador.conjuga_vm(datos_conj)
            elif plantilla_conj == u'v.conj.2.ar':
                raices["dip"] = raices["ton"]
                flexion = Flexionador.conjuga_vm(datos_conj)
            elif plantilla_conj == u'v.conj.andar':
                raices["ton"] = raices["ato"] + u'ánd'
                raices["ato"] += u'and'
                raices["dip"] += u'and'
                raices["cerr"] += u'and'
                flexion = Flexionador.conjuga_vm(datos_conj)
                raices["cerr"] += u'uv'
                datos_conj["paradigma"] = 2
                flexion.update(Flexionador.conjuga_vmsi(datos_conj))
                flexion.update(Flexionador.conjuga_vmsf(datos_conj))
                raices["ato"] += u'uv'
                datos_conj["mono"] = True
                flexion.update(Flexionador.conjuga_vmis(datos_conj))
                flexion[IS1S][0] = flexion[IS1S][0][:-1] + u'e'  # Apaño para "desanduvio" -> "desanduvo"
                flexion[IS3S][0] = flexion[IS3S][0][:-2] + u'o'  # Apaño para "desanduvio" -> "desanduvo"
            elif plantilla_conj == u'v.conj.arse':
                datos_conj["pronominal"] = True
                raices["dip"] = raices["ato"]  # Ahora el dip se ha puesto como el ton, pero no hay hiato.
                flexion = Flexionador.conjuga_vm(datos_conj)
            elif plantilla_conj in [u'v.conj.decir', u'v.conj.benmal.decir']:
                if plantilla_conj == u'v.conj.decir':
                    datos_conj["formas"]["part"] = raices["ato"] + u'dicho'
                else:
                    datos_conj["formas"]["part"] = raices["ato"] + u'dito'
                    datos_conj["formas"]["part2"] = raices["ato"] + u'decido'
                raices["ton"] = raices["ato"] + u'dí'
                raices["ato"] += u'dec'
                raices["dip"] += u'dic'
                raices["cerr"] += u'dij'
                datos_conj["palatal"] = True
                flexion = Flexionador.conjuga_vm(datos_conj)
                flexion[IP1S][0] = raices["cerr"][:-1] + u'go'
                raices["cerr"] = raices["cerr"][:-1] + u'c'
                raices["ato"] = raices["cerr"][:-1]
                raices["cerr"] = raices["cerr"][:-1]
                datos_conj["nexos"] = {"a": u'j', "i": u'j'}
                flexion.update(Flexionador.conjuga_vmis(datos_conj))
                flexion[IS1S][0] = flexion[IS1S][0].replace(u'í', u'e')
                flexion[IS3S][0] = flexion[IS3S][0].replace(u'ó', u'o')
                raices["ato"] = raices["ato"][:-1]
                datos_conj["nexos"] = {"a": u'', "i": u''}
                raices["dip"] = raices["cerr"]
                flexion.update(Flexionador.conjuga_vmsp(datos_conj, gutural=True))
                if plantilla_conj == u'v.conj.decir':  # Si es el verbo "decir" o derivados (excepto mal/bendecir)
                    flexion.update(Flexionador.conjuga_vmif(datos_conj))  # diré y prediré
                    flexion.update(Flexionador.conjuga_vmic(datos_conj))  # diría y prediría
                raices["ato"] += u'ec'  # Todos los verbos derivados de "decir" tienen la forma con -ec
                if flexion[INF][0] != u'decir':
                    if plantilla_conj == u'v.conj.decir':  # derivado de "decir" que no es ben/mal -> flexión doble
                        for et, formas in Flexionador.conjuga_vmif(datos_conj).items():
                            flexion[et] += formas
                        for et, formas in Flexionador.conjuga_vmic(datos_conj).items():
                            flexion[et] += formas
                    else:
                        flexion.update(Flexionador.conjuga_vmif(datos_conj))  # maldeciré
                        flexion.update(Flexionador.conjuga_vmic(datos_conj))  # maldeciría
                flexion.update(Flexionador.conjuga_vmmp(datos_conj, gutural=True))
                flexion[MP2S][0] = flexion[MP2S][0][:-1] + u'ce'
                flexion[MP2S_P][0] = raices["ton"] + u'cete'
                if plantilla_conj == u'v.conj.decir':
                    # Para decir se admiten las formas "di" y "dice" como imperativas de 2ª singular.
                    flexion[MP2S] = [raices["dip"] if len(Palabra(raices["dip"]).get_silabas()) == 1 else raices["ton"]] +\
                        flexion[MP2S]
                    flexion[MP2S_P] = [raices["dip"] + u'te'] + flexion[MP2S_P]
                flexion[MP3S_P][0] = raices["ton"] + u'gase'
                flexion[MP3P_P][0] = raices["ton"] + u'ganse'
                raices["cerr"] += u'c'
                datos_conj["palatal"] = False
                flexion.update(Flexionador.conjuga_vmg(datos_conj))
            elif plantilla_conj == u'v.conj.caer':
                raices["ton"] = raices["ato"] + u'cá'
                raices["ato"] += u'ca'
                raices["dip"] += u'ca'
                raices["cerr"] += u'ca'
                flexion = Flexionador.conjuga_vm(datos_conj)
                flexion[IP1S][0] = raices["ato"] + u'igo'
                datos_conj["palatal"] = True
                raices["cerr"] = raices["ato"] + u'y'
                flexion.update(Flexionador.conjuga_vmsi(datos_conj))
                flexion.update(Flexionador.conjuga_vmsf(datos_conj))
                flexion.update(Flexionador.conjuga_vmg(datos_conj))
                raices["cerr"] = raices["ato"] + u'ig'
                raices["dip"] = raices["cerr"]
                flexion.update(Flexionador.conjuga_vmsp(datos_conj))
                flexion.update(Flexionador.conjuga_vmmp(datos_conj))
                flexion[MP2S][0] = flexion[MP2S][0][:-3] + u'e'
                flexion[MP3S_P][0] = raices["ton"] + u'igase'
                flexion[MP3P_P][0] = raices["ton"] + u'iganse'
            elif plantilla_conj == u'v.conj.car':
                datos_conj["nexos"] = {"a": u'c', "i": u'qu'}
                AcepcionWik.calcula_raiz_tonica(datos_conj)
                flexion = Flexionador.conjuga_vm(datos_conj)
            elif plantilla_conj == u'v.conj.cuar':  # Tienen doble conjugación con diptongo o hiato
                raices["ato"] += u'cu'
                raices["dip"] = raices["ato"]
                raices["cerr"] += u'cu'
                AcepcionWik.calcula_raiz_tonica(datos_conj)
                flexion = Flexionador.conjuga_vm(datos_conj)
                raices["dip"] = raices["ato"][:-1] + u'ú'
                formas_hiato = Flexionador.conjuga_vmip(datos_conj)  # Las formas de presente con diptongo, se vuelven hiatos
                formas_hiato.update(Flexionador.conjuga_vmsp(datos_conj))
                raices["ton"] = raices["dip"]
                formas_hiato.update(Flexionador.conjuga_vmmp(datos_conj))
                for etiqueta, formas in formas_hiato.items():
                    if etiqueta[4:6] != "2V":
                        flexion[etiqueta] += [forma for forma in formas if forma not in flexion[etiqueta]]
            elif plantilla_conj == u'v.conj.dar':
                raices["ato"] += u'd'
                raices["dip"] += u'd'
                raices["cerr"] += u'd'
                raices["ton"] += u'd'
                # datos_conj["mono"] = True
                flexion = Flexionador.conjuga_vm(datos_conj)
                flexion[IP1S][0] += u'y'
                datos_conj["paradigma"] = 2
                flexion.update(Flexionador.conjuga_vmis(datos_conj))
                flexion.update(Flexionador.conjuga_vmsi(datos_conj))
                flexion.update(Flexionador.conjuga_vmsf(datos_conj))
                flexion[SP1S][0] = flexion[SP1S][0][:-2] + u'dé'
                flexion[SP3S][0] = flexion[SP3S][0][:-2] + u'dé'
                flexion[MP3S][0] = flexion[MP3S][0][:-2] + u'dé'
            elif plantilla_conj in [u'v.conj.ducir', u'v.conj.zc.cer', u'v.conj.zc.cir']:
                datos_conj["nexos"] = {"a": u'zc', "i": u'c'}
                AcepcionWik.calcula_raiz_tonica(datos_conj)
                flexion = Flexionador.conjuga_vm(datos_conj)
                if plantilla_conj == u'v.conj.ducir':
                    datos_conj["palatal"] = True  # Corta las desinencias -ie, -io... como las palatales
                    datos_conj["nexos"] = {"a": u'j', "i": u'j'}
                    flexion.update(Flexionador.conjuga_vmis(datos_conj))  # Hace lo que puede, 2 formas quedan mal
                    flexion[IS1S][0] = flexion[IS1S][0].replace(u'í', u'e')  # Apaño para "redují" -> "reduje"
                    flexion[IS3S][0] = flexion[IS3S][0].replace(u'ó', u'o')  # Apaño para "redujó" -> "redujo"
                    flexion.update(Flexionador.conjuga_vmsi(datos_conj))
                    flexion.update(Flexionador.conjuga_vmsf(datos_conj))
            elif plantilla_conj == u'v.conj.eer':
                flexion = Flexionador.conjuga_vm(datos_conj)
                raices["cerr"] += u'y'
                datos_conj["palatal"] = True
                flexion.update(Flexionador.conjuga_vmg(datos_conj))
                flexion.update(Flexionador.conjuga_vmsi(datos_conj))
                flexion.update(Flexionador.conjuga_vmsf(datos_conj))
            elif plantilla_conj == u'v.conj.eír':
                # Este tipo ya presupone que el participio regular existe, pero a veces sólo marca un part=frito.
                if "part2" not in datos_conj["formas"]:
                    datos_conj["formas"]["part2"] = raices["ato"] + u'eído'
                # No usa la etiqueta mono= para freír(se) o reír(se), pero no lo ponemos porque el hiato produce tildes
                mono = True if u'a' not in raices["ato"] and u'e' not in raices["ato"] and u'i' not in raices["ato"] and \
                               u'o' not in raices["ato"] and u'a' not in raices["ato"] else False
                raices["ton"] = raices["ato"] + u'í'
                raices["ato"] += u'e'
                raices["dip"] += u'í'
                flexion = Flexionador.conjuga_vm(datos_conj)  # con errores en 5 tiempos
                flexion[IP1P][0] = flexion[IP1P][0][:-5] + u'eímos'  # Apaño para "freimos" -> "freímos"
                flexion[IS2S][0] = flexion[IS2S][0][:-4] + u'íste'  # Apaño para "freiste" -> "freíste"
                # No usa la etiqueta mono= para freír(se) o reír(se), pero no lo ponemos porque el hiato produce tildes
                if mono:
                    flexion[IS3S][0] = flexion[IS3S][0][:-2] + u'io'  # Apaño para "frió" -> "frio"
                flexion[IS1P][0] = flexion[IP1P][0]  # Apaño para "freimos" -> "freímos"
                flexion[IS2P][0] = flexion[IS2S][0] + u'is'  # Apaño para "freisteis" -> "freísteis"
                raices["cerr"] += u'i'
                flexion.update(Flexionador.conjuga_vmsp(datos_conj))
                if mono:
                    flexion[SP2V][0] = flexion[SP2V][0][:-2] + u'as'  # Apaño para vos "riás" -> "rias"
                    flexion[SP2P][0] = flexion[SP2P][0][:-3] + u'ais'  # Apaño para "friáis" -> "friais"
                flexion.update(Flexionador.conjuga_vmmp(datos_conj))
                flexion[MP2V_P][0] = flexion[MP2V_P][0].replace(u'eite', u'eíte')
                flexion[MP2P][0] = flexion[MP2P][0].replace(u'eid', u'eíd')  # Apaño para "freid" -> "freíd"
            elif plantilla_conj == u'v.conj.eñir':
                datos_conj["palatal"] = True
                raices["ton"] = raices["ato"] + u'íñ'
                raices["ato"] += u'eñ'
                raices["dip"] += u'iñ'
                raices["cerr"] += u'iñ'
                flexion = Flexionador.conjuga_vm(datos_conj)
            elif plantilla_conj in [u'v.conj.ger', u'v.conj.gir']:
                datos_conj["nexos"] = {"a": u'j', "i": u'g'}
                AcepcionWik.calcula_raiz_tonica(datos_conj)
                flexion = Flexionador.conjuga_vm(datos_conj)
            elif plantilla_conj == u'v.conj.guar':
                datos_conj["nexos"] = {"a": u'gu', "i": u'gü'}
                AcepcionWik.calcula_raiz_tonica(datos_conj)
                flexion = Flexionador.conjuga_vm(datos_conj)
            elif plantilla_conj == u'v.conj.hacer':
                datos_conj["formas"]["part"] = raices["ato"] + u'echo'
                raices["ton"] = raices["ato"] + u'á'
                raices["ato"] += u'a'
                raices["dip"] += u'a'
                raices["cerr"] += u'i'
                datos_conj["nexos"] = {"a": u'z', "i": u'c'}
                flexion = Flexionador.conjuga_vm(datos_conj)
                flexion[IP1S][0] = flexion[IP1S][0][:-2] + u'go'

                raices["ato"] = raices["cerr"]
                flexion.update(Flexionador.conjuga_vmis(datos_conj))
                i = u'í' if u'i' in datos_conj else u'i'  # Para el hiato en "rehíce" y "rehízo"
                flexion[IS1S][0] = flexion[IS1S][0][:-3] + i + u'ce'
                flexion[IS3S][0] = flexion[IS3S][0][:-4] + i + u'zo'
                datos_conj["paradigma"] = 1
                raices["ato"] = raices["ato"][:-1]
                datos_conj["nexos"] = {"a": u'', "i": u''}
                flexion.update(Flexionador.conjuga_vmif(datos_conj))
                flexion.update(Flexionador.conjuga_vmic(datos_conj))

                datos_conj["paradigma"] = 2
                raices["cerr"] = raices["dip"]
                flexion.update(Flexionador.conjuga_vmsp(datos_conj, gutural=True))

                raices["ato"] += u'ac'
                flexion.update(Flexionador.conjuga_vmmp(datos_conj, gutural=True))
                flexion[MP2S][0] = flexion[MP2S][0][:-1] + u'z'
                flexion[MP2S_P][0] = flexion[MP2S][0] + u'te'
                raices["cerr"] += u'c'
                flexion.update(Flexionador.conjuga_vmg(datos_conj))
            elif plantilla_conj in [u'v.conj.llir', u'v.conj.ñer', u'v.conj.ñir']:
                datos_conj["palatal"] = True
                AcepcionWik.calcula_raiz_tonica(datos_conj)
                flexion = Flexionador.conjuga_vm(datos_conj)
            elif plantilla_conj == u'v.conj.oír':
                flexion = Flexionador.conjuga_vm(datos_conj)
                raices["cerr"] += u'y'
                datos_conj["palatal"] = True
                flexion.update(Flexionador.conjuga_vmg(datos_conj))
                flexion.update(Flexionador.conjuga_vmsi(datos_conj))
                flexion.update(Flexionador.conjuga_vmsf(datos_conj))

                raices["dip"] = raices["ato"] + u'y'
                flexion.update(Flexionador.conjuga_vmip(datos_conj))
                flexion[IP1S][0] = flexion[IP1S][0][:-3] + u'oigo'
                flexion[IP1P][0] = flexion[IP1P][0][:-5] + u'oímos'

                raices["ton"] = raices["ton"][:-1] + u'ói'
                raices["dip"] = raices["dip"][:-1] + u'i'
                raices["cerr"] = raices["dip"]
                flexion.update(Flexionador.conjuga_vmsp(datos_conj, gutural=True))
                flexion.update(Flexionador.conjuga_vmmp(datos_conj, gutural=True))
                flexion[MP2S][0] = flexion[MP2S][0][:-3] + u'oye'
                flexion[MP2S_P][0] = flexion[MP2S_P][0][:-5] + u'óyete'
                flexion[MP2V_P][0] = flexion[MP2V_P][0][:-4] + u'oíte'
                flexion[MP2P][0] = flexion[MP2P][0][:-3] + u'oíd'
            elif plantilla_conj == u'v.conj.poner':
                mono = raices["ato"] == u''  # Poner en imperativo, es monosílabo: pon
                datos_conj["formas"]["part"] = raices["ato"] + u'puesto'
                raices["ton"] = raices["ato"] + u'pón'
                raices["ato"] += u'pon'
                raices["dip"] += u'pon'
                raices["cerr"] += u'pon'
                flexion = Flexionador.conjuga_vm(datos_conj)
                flexion[IP1S][0] = raices["ato"] + u'go'  # Apaño para "tieno" -> "tengo"
                flexion.update(Flexionador.conjuga_vmsp(datos_conj, gutural=True))
                flexion.update(Flexionador.conjuga_vmmp(datos_conj, gutural=True))
                # Para poner se admiten las formas "pon" y "pone" como imperativas de 2ª singular.
                flexion[MP2S] = [raices["ato"] if mono else raices["ton"]] + flexion[MP2S]
                flexion[MP2S_P] = [raices["ato"] + u'te'] + flexion[MP2S_P]
                raices["ato"] += u'd'
                flexion.update(Flexionador.conjuga_vmif(datos_conj, elipsis=True))
                flexion.update(Flexionador.conjuga_vmic(datos_conj, elipsis=True))
                raices["ato"] = raices["ato"][:-3] + u'us'
                raices["cerr"] = raices["ato"]
                datos_conj["mono"] = True
                flexion.update(Flexionador.conjuga_vmis(datos_conj))
                flexion[IS1S][0] = flexion[IS1S][0][:-1] + u'e'
                flexion[IS3S][0] = flexion[IS3S][0][:-2] + u'o'
                flexion.update(Flexionador.conjuga_vmsi(datos_conj))
                flexion.update(Flexionador.conjuga_vmsf(datos_conj))
            elif plantilla_conj == u'v.conj.querer':
                raices["ton"] = raices["ato"] + u'quiér'
                raices["ato"] += u'quer'
                raices["dip"] += u'quier'
                raices["cerr"] += u'quis'
                flexion = Flexionador.conjuga_vm(datos_conj)
                flexion.update(Flexionador.conjuga_vmif(datos_conj, elipsis=True))
                flexion.update(Flexionador.conjuga_vmic(datos_conj, elipsis=True))
                raices["cerr"] = raices["ato"]
                flexion.update(Flexionador.conjuga_vmg(datos_conj))
                flexion.update(Flexionador.conjuga_vmsp(datos_conj))
                flexion.update(Flexionador.conjuga_vmmp(datos_conj))
                raices["ato"] = raices["ato"][:-2] + u'is'
                raices["cerr"] = raices["ato"]
                flexion.update(Flexionador.conjuga_vmis(datos_conj))
                flexion[IS1S][0] = flexion[IS1S][0][:-1] + u'e'
                flexion[IS3S][0] = flexion[IS3S][0][:-2] + u'o'
            elif plantilla_conj == u'v.conj.roer':
                raices["ton"] = raices["ato"] + u'ró'
                raices["ato"] += u'ro'
                raices["dip"] += u'ro'
                raices["cerr"] += u'ro'
                flexion = Flexionador.conjuga_vm(datos_conj)
                flexion[IP1S] += [flexion[IP1S][0][:-1] + u'igo', flexion[IP1S][0][:-1] + u'yo']
                raices["cerr"] += u'y'
                datos_conj["palatal"] = True
                flexion.update(Flexionador.conjuga_vmg(datos_conj))
                flexion.update(Flexionador.conjuga_vmsi(datos_conj))
                flexion.update(Flexionador.conjuga_vmsf(datos_conj))

                raices["cerr"] = raices["cerr"][:-1]
                datos_conj["nexos"] = {"a": u'i', "i": u'i'}
                flexion2 = Flexionador.conjuga_vmsp(datos_conj, gutural=True)
                flexion2.update(Flexionador.conjuga_vmmp(datos_conj, gutural=True))
                datos_conj["nexos"] = {"a": u'y', "i": u'y'}
                conjugacion3 = Flexionador.conjuga_vmsp(datos_conj)
                conjugacion3.update(Flexionador.conjuga_vmmp(datos_conj))
                for persona in CODIGOS_PERSONAS:
                    flexion["VMSP" + persona + "000000"] += flexion2["VMSP" + persona + "000000"] + \
                        conjugacion3["VMSP" + persona + "000000"]
                    if persona in ["1S", "2S", "2V", "2P"]:
                        continue
                    # Hacemos los imperativos
                    flexion["VMMP" + persona + "000000"] += flexion2["VMMP" + persona + "000000"] + \
                        conjugacion3["VMMP" + persona + "000000"]
                    flexion["VMMP" + persona + "0P0000"] += flexion2["VMMP" + persona + "0P0000"] + \
                        conjugacion3["VMMP" + persona + "0P0000"]
            elif plantilla_conj == u'v.conj.saber':  # Muy parecido a tener, venir (y sobre todo caber)
                raices["ton"] = raices["ato"] + u'sép'
                raices["ato"] += u'sab'
                raices["dip"] += u'sab'
                raices["cerr"] += u'sup'
                flexion = Flexionador.conjuga_vm(datos_conj)
                flexion[IP1S][0] = flexion[IP1S][0][:-3] + u'é'
                flexion.update(Flexionador.conjuga_vmif(datos_conj, elipsis=True))
                flexion.update(Flexionador.conjuga_vmic(datos_conj, elipsis=True))
                flexion.update(Flexionador.conjuga_vmsi(datos_conj))
                flexion.update(Flexionador.conjuga_vmsf(datos_conj))

                raices["ato"] = raices["cerr"]
                flexion.update(Flexionador.conjuga_vmis(datos_conj))
                flexion[IS1S][0] = flexion[IS1S][0][:-1] + u'e'
                flexion[IS3S][0] = flexion[IS3S][0][:-2] + u'o'

                raices["ato"] = raices["ato"][:-2] + u'ab'
                raices["cerr"] = raices["dip"]
                flexion.update(Flexionador.conjuga_vmsp(datos_conj))

                raices["dip"] = raices["dip"][:-2] + u'ep'
                raices["cerr"] = raices["dip"]
                flexion.update(Flexionador.conjuga_vmsp(datos_conj))
                flexion.update(Flexionador.conjuga_vmmp(datos_conj))

                flexion[MP2S][0] = raices["ato"] + u'e'
                flexion[MP2S_P][0] = flexion[MP2S_P][0][:-5] + u'ábete'
                raices["cerr"] = raices["ato"]
                flexion.update(Flexionador.conjuga_vmg(datos_conj))
            elif plantilla_conj in [u'v.conj.salir', u'v.conj.valer']:
                consonante = u's' if plantilla_conj == u'v.conj.salir' else u'v'
                raices["ton"] = raices["ato"] + consonante + u'ál'
                raices["ato"] += consonante + u'al'
                raices["dip"] += consonante + u'al'
                raices["cerr"] += consonante + u'al'
                flexion = Flexionador.conjuga_vm(datos_conj)
                flexion[IP1S][0] = raices["ato"] + u'go'
                flexion.update(Flexionador.conjuga_vmsp(datos_conj, gutural=True))
                flexion.update(Flexionador.conjuga_vmmp(datos_conj, gutural=True))
                if plantilla_conj == u'v.conj.salir':
                    flexion[MP2S][0] = raices["ato"]
                flexion[MP2S_P][0] = raices["ato"] + u'te' if consonante == u's' else raices["ton"] + u'ete'
                raices["ato"] += u'd'
                flexion.update(Flexionador.conjuga_vmif(datos_conj, elipsis=True))
                flexion.update(Flexionador.conjuga_vmic(datos_conj, elipsis=True))
            elif plantilla_conj == u'v.conj.seguir':
                raices["ton"] = raices["ato"] + u'sí'
                raices["ato"] += u'se'
                raices["dip"] += u'si'
                raices["cerr"] += u'si'
                datos_conj["nexos"] = {"a": u'g', "i": u'gu'}
                flexion = Flexionador.conjuga_vm(datos_conj)
            elif plantilla_conj in [u'v.conj.tener', u'v.conj.venir']:
                mono = raices["ato"] == u''  # Tener y venir en imperativo, son monosílabos: ten, ven
                consonante = u't' if plantilla_conj == u'v.conj.tener' else u'v'
                raices["ton"] = raices["ato"] + consonante + u'én'
                raices["ato"] += consonante + u'en'
                raices["dip"] += consonante + u'ien'
                raices["cerr"] += consonante + (u'uv' if plantilla_conj == u'v.conj.tener' else u'in')
                flexion = Flexionador.conjuga_vm(datos_conj)
                flexion[IP1S][0] = flexion[IP1S][0][:-4] + u'engo'  # Apaño para "tieno" -> "tengo"

                raices["ato"] += u'd'
                flexion.update(Flexionador.conjuga_vmif(datos_conj, elipsis=True))
                flexion.update(Flexionador.conjuga_vmic(datos_conj, elipsis=True))
                flexion.update(Flexionador.conjuga_vmsi(datos_conj))
                flexion.update(Flexionador.conjuga_vmsf(datos_conj))
                raices["ato"] = raices["cerr"]
                datos_conj["mono"] = True
                flexion.update(Flexionador.conjuga_vmis(datos_conj))
                flexion[IS1S][0] = flexion[IS1S][0][:-1] + u'e'  # Apaño para "tuvi" -> "tuve"
                flexion[IS3S][0] = flexion[IS3S][0][:-2] + u'o'  # Apaño para "tuvio" -> "tuvo"

                datos_conj["mono"] = False
                raices["dip"] = raices["dip"][:-3] + u'en'
                raices["cerr"] = raices["cerr"][:-2] + u'en'
                flexion.update(Flexionador.conjuga_vmsp(datos_conj, gutural=True))

                raices["ato"] = raices["ato"][:-2] + u'en'
                flexion.update(Flexionador.conjuga_vmmp(datos_conj, gutural=True))
                flexion[MP2S][0] = raices["ato"] if mono else raices["ton"]
                flexion[MP2S_P][0] = raices["ato"] + u'te'
                if plantilla_conj == u'v.conj.venir':
                    # Para venir se admiten las formas "ven" y "viene" como imperativas de 2ª singular.
                    flexion[MP2S] += [raices["ato"][:-2] + u'iene']
                    flexion[MP2S_P] += [raices["ato"][:-2] + u'iénete']
                else:
                    raices["cerr"] = raices["dip"]
                    flexion.update(Flexionador.conjuga_vmg(datos_conj))
            elif plantilla_conj == u'v.conj.traer':
                raices["ton"] = raices["ato"] + u'trá'
                raices["ato"] += u'tra'
                raices["dip"] += u'tra'
                raices["cerr"] += u'traj'
                datos_conj["palatal"] = True
                flexion = Flexionador.conjuga_vm(datos_conj)
                flexion[IP1S][0] = raices["cerr"][:-1] + u'igo'
                raices["cerr"] = raices["cerr"][:-1] + u'y'
                flexion.update(Flexionador.conjuga_vmg(datos_conj))
                raices["cerr"] = raices["cerr"][:-1]
                datos_conj["nexos"] = {"a": u'j', "i": u'j'}
                flexion.update(Flexionador.conjuga_vmis(datos_conj))
                flexion[IS1S][0] = flexion[IS1S][0].replace(u'í', u'e')
                flexion[IS3S][0] = flexion[IS3S][0].replace(u'ó', u'o')
                datos_conj["nexos"] = {"a": u'i', "i": u'i'}
                flexion.update(Flexionador.conjuga_vmsp(datos_conj, gutural=True))
                vmmp = Flexionador.conjuga_vmmp(datos_conj, gutural=True)
                for etiqueta, forma in vmmp.items():
                    if "2" not in etiqueta:  # Tú, vos y vosotros ya está bien
                        flexion[etiqueta] = vmmp[etiqueta]
            elif plantilla_conj == u'v.conj.uir':
                datos_conj["palatal"] = True
                raices["ton"] = raices["ato"][:-1] + u'úy'
                raices["dip"] = raices["ato"] + u'y'
                raices["cerr"] = raices["dip"]
                flexion = Flexionador.conjuga_vm(datos_conj)
            elif plantilla_conj == u'v.conj.ver':
                datos_conj["formas"]["part"] = raices["ato"] + u'isto'
                flexion = Flexionador.conjuga_vm(datos_conj)
                flexion[IP1S][0] = raices["ato"] + u'eo'
                if not datos_conj["mono"]:
                    flexion[IP2S][0] = flexion[IP2S][0][:-2] + u'és'
                    flexion[IP3S][0] = flexion[IP3S][0][:-1] + u'é'
                    flexion[IP3P][0] = flexion[IP3P][0][:-2] + u'én'
                raices["dip"] += u'e'
                raices["ton"] = raices["ato"] + u'é'
                raices["cerr"] += u'e'
                flexion.update(Flexionador.conjuga_vmsp(datos_conj))
                flexion[SP2V][0] = flexion[SP2V][0][:-2] + u'ás'
                flexion[SP2P][0] = flexion[SP2P][0][:-3] + u'áis'
                flexion.update(Flexionador.conjuga_vmmp(datos_conj))
                flexion[MP2S][0] = flexion[MP2S][0][:-2] + (u'é' if not datos_conj["mono"] else u'e')
                flexion[MP2V][0] = flexion[MP2S][0]
                flexion[MP2S_P][0] = flexion[MP2S_P][0][:-4] + u'ete'
                flexion[MP2V_P][0] = flexion[MP2V_P][0]
                raices["ato"] += u'e'
                flexion.update(Flexionador.conjuga_vmii(datos_conj))
            elif plantilla_conj == u'v.conj.yacer':
                raices["ton"] = raices["ato"] + u'yá'
                raices["ato"] += u'ya'
                raices["dip"] += u'ya'
                raices["cerr"] += u'ya'
                datos_conj["nexos"] = {"a": u'zc', "i": u'c'}
                flexion = Flexionador.conjuga_vm(datos_conj)
                flexion[IP1S] += [flexion[IP1S][0][:-5] + u'yazgo', flexion[IP1S][0][:-5] + u'yago']
                datos_conj["nexos"] = {"a": u'zg', "i": u'c'}
                flexion2 = Flexionador.conjuga_vmsp(datos_conj)
                flexion2.update(Flexionador.conjuga_vmmp(datos_conj))
                datos_conj["nexos"] = {"a": u'g', "i": u'c'}
                conjugacion3 = Flexionador.conjuga_vmsp(datos_conj)
                conjugacion3.update(Flexionador.conjuga_vmmp(datos_conj))
                for persona in CODIGOS_PERSONAS:
                    flexion["VMSP" + persona + "000000"] += flexion2["VMSP" + persona + "000000"] + \
                        conjugacion3["VMSP" + persona + "000000"]
                    if persona in ["1S", "2S", "2V", "2P"]:
                        continue
                    # Hacemos los imperativos
                    flexion["VMMP" + persona + "000000"] += flexion2["VMMP" + persona + "000000"] + \
                        conjugacion3["VMMP" + persona + "000000"]
                    flexion["VMMP" + persona + "0P0000"] += flexion2["VMMP" + persona + "0P0000"] + \
                        conjugacion3["VMMP" + persona + "0P0000"]
                flexion[MP2S] += [raices["ato"] + u'z']
                flexion[MP2S_P] += [raices["ato"] + u'zte']
            elif plantilla_conj == u'v.conj.üir':
                datos_conj["palatal"] = True
                raices["ton"] = raices["ato"] + u'úy'
                raices["ato"] += u'ü'
                raices["dip"] += u'uy'
                raices["cerr"] = raices["dip"]
                flexion = Flexionador.conjuga_vm(datos_conj)
            else:
                print(u'Error con', lema_txt)

            # PROCESADO DE FORMAS CONCRETAS
            for codigo, valor in datos_conj["formas"].items():
                # Los códigos de tiempo se explican aquí: https://es.wiktionary.org/wiki/Plantilla:es.v.conj.ar
                # print(u'    ', codigo, u'=', valor)
                # A veces sale más de una forma: sepultado o sepulto.
                variantes = valor.replace(u' o raramente ', u' ').replace(u' o ', u' ').replace(u', ', u' '). \
                    replace(u' / ', u' ').replace(u'<br/>', u' ').replace(u'<br>', u' ').split()
                if codigo == u'inf':
                    pass  # Hay alguna etiqueta así, pero son completamente innecesarias
                elif codigo in [u'ger', u'gerpron']:
                    # Actualizamos la forma pronominal y no pronominal
                    flexion[GER] = []
                    flexion[GER_P] = []
                    for variante in variantes:
                        if variante in [u'—', u'--', u'---']:
                            # Será un verbo defectivo y este tiempo no existe
                            flexion.pop(GER, None)
                            flexion.pop(GER_P, None)
                            break
                        # Si el verbo es pronominal ("pronominal" in datos_conj) la forma 'ger' será en principio
                        # la pronominal, o algunas veces no. Lo más rápido es mirar el 'se' final.
                        if variante[-2:] == u'se':
                            if variante not in flexion[GER_P]:
                                flexion[GER_P].append(variante)
                            variante_ger = variante[:-2].replace(u'á', u'a').replace(u'é', u'e').replace(u'í', u'i').\
                                replace(u'ó', u'o').replace(u'ú', u'u') + variante[-2:].replace(u'se', u'')
                            if variante_ger not in flexion[GER]:
                                flexion[GER].append(variante_ger)
                        else:
                            if variante not in flexion[GER]:
                                flexion[GER].append(variante)
                            variante_ger_p = Palabra(palabra_texto=variante,
                                                     calcula_alofonos=False,
                                                     organiza_grafemas=True).set_tilde(con_tilde=True) + u'se'
                            if variante_ger_p not in flexion[GER_P]:
                                flexion[GER_P].append(variante_ger_p)
                elif codigo in [u'par', u'participio', u'part']:
                    # En principio el par2 es el que se usa en tiempos compuestos y siempre lo ponemos como segundo.
                    # Este será el primero (quizá único, si el participio usado en tiempos es regular).
                    # Sólo hay una variante.
                    if variantes[0] not in flexion[PAR_SM]:
                        flexion[PAR_SM] = [variantes[0]] + flexion[PAR_SM]
                        flexion[PAR_SF] = [variantes[0][:-1] + u'a'] + flexion[PAR_SF]
                        flexion[PAR_PM] = [variantes[0][:-1] + u'os'] + flexion[PAR_PM]
                        flexion[PAR_PF] = [variantes[0][:-1] + u'as'] + flexion[PAR_PF]
                elif codigo in [u'par2', u'part2']:
                    # En principio el par2 es el que se usa en tiempos compuestos. Irá el último
                    if variantes[0][:-3] + variantes[0][-3].replace(u'í', u'i') == flexion[PAR_SM][-1]:
                        # Tan sólo es la corrección ortográfica por un hiato (o ya estaba). Machacamos la forma regular.
                        flexion[PAR_SM][-1] = variantes[0]
                        flexion[PAR_SF][-1] = variantes[0][:-1] + u'a'
                        flexion[PAR_PM][-1] = variantes[0][:-1] + u'os'
                        flexion[PAR_PF][-1] = variantes[0][:-1] + u'as'
                    else:
                        # Es una variante distinta. Se pone la última.
                        flexion[PAR_SM] += [variantes[0]]
                        flexion[PAR_SF] += [variantes[0][:-1] + u'a']
                        flexion[PAR_PM] += [variantes[0][:-1] + u'os']
                        flexion[PAR_PF] += [variantes[0][:-1] + u'as']
                else:
                    # Es una forma de tiempo verbal, pero tendremos que "decodificar" su etiqueta
                    etiqueta_eagles = "VM"
                    etiqueta_eagles += codigo.replace(u'im.', u'MP').replace(u'i.c.', u'IC').replace(u'.p.', u'P') \
                        .replace(u'.pi.', u'I').replace(u'.pi2.', u'I').replace(u'.pp.', u'S').replace(u'.f.', u'F')
                    etiqueta_eagles = etiqueta_eagles.replace(u's2', u'v').upper() + u'000000'
                    if u'IMPPRON' in etiqueta_eagles:  # Código para imperativo pronominal
                        etiqueta_eagles = etiqueta_eagles.replace(u'IMPPRON', u'MP').replace(u'.', u'')[:7] + u'P0000'
                    # Antes de actualizar la forma, desambiguamos la "pronominalidad" de la forma.
                    # El problema es que en verbos pronominales, las formas imperativas no tienen código de
                    # pronominal (se les supone). No obstante, a veces se ponen las dos formas.
                    if etiqueta_eagles[:4] + etiqueta_eagles[6] == "VMMP0":
                        # Efectivamente, ha entrado una forma imperativa que en teoría es no pronominal.
                        if datos_conj["pronominal"] and \
                                u'imppron' + etiqueta_eagles[4:6].lower().replace(u'2v', u'2s2') \
                                not in datos_conj["formas"]:
                            # El verbo es pronominal, y además no hay etiqueta expresa de no pronominal, con lo que
                            # esta forma se considera pronominal.
                            etiqueta_eagles = etiqueta_eagles[:7] + PRONOMINAL + etiqueta_eagles[8:]
                    if etiqueta_eagles not in CATALOGO_ETIQUETAS:
                        # Existen algunos errores, que no están corregidos porque simplemente se ignoran.
                        beep(440, 500)
                        print(u'Etiqueta', codigo, u'desconocida')
                        continue

                    # Modificamos la forma flexionada.
                    defectivo = False
                    if u's.pi' not in codigo:
                        # El s.pi hace referencia al imperfecto de subjuntivo. Como es un tiempo muy regular y siempre
                        # tiene dos formas, es el único caso en el que no limpiamos la flexion, sino que luego
                        # sobreescribiremos las formas nuevas en su lugar.
                        flexion[etiqueta_eagles] = []
                    tiempo_asociado = ""
                    if etiqueta_eagles[:6] in ["VMSP3S", "VMSP1P", "VMSP3P"]:
                        # Esta forma se usará también en imperativo. Lo marcamos y borramos el imperativo
                        tiempo_asociado = "VMMP" + etiqueta_eagles[4:]
                        flexion[tiempo_asociado] = []
                    for orden_variante, variante in enumerate(variantes):
                        if variante in [u'—', u'--', u'---']:
                            # Será un verbo defectivo y este tiempo no existe. Borramos las formas pronominales o no
                            flexion.pop(etiqueta_eagles[:6] + "0" + etiqueta_eagles[7:], None)
                            flexion.pop(etiqueta_eagles[:6] + PRONOMINAL + etiqueta_eagles[7:], None)
                            if tiempo_asociado:
                                flexion.pop(tiempo_asociado[:6] + "0" + tiempo_asociado[7:], None)
                                flexion.pop(tiempo_asociado[:6] + PRONOMINAL + tiempo_asociado[7:], None)
                            defectivo = True
                            break

                        if u's.pi' in codigo:
                            # El imperfecto de subjuntivo es un poco especial porque siempre tiene dos formas.
                            # Para tenerlo más ordenado, mi convención es que la primera es la -ra y la segunda la -se
                            flexion[etiqueta_eagles][1 if u'.pi2.' in codigo else 0] = variantes[0]  # pi2 es "cantase"
                        else:
                            flexion[etiqueta_eagles].append(variante)
                            if tiempo_asociado:
                                flexion[tiempo_asociado].append(variante)
                                # Para facilitar el procesado (por los pronominales) cambiamos la (posible) etiqueta
                                # de subjuntivo usada como imperativo por la propia etiqueta de imperativo.
                                if orden_variante == len(variantes) - 1:
                                    etiqueta_eagles = tiempo_asociado

                    # Ya hemos actualizado la forma, pero algunas formas requieren algún cambio en una forma asociada.
                    # Básicamente, las formas imperativas (que pueden ser pronominales o no) y aquellas de presente
                    # de subjuntivo que se usan en imperativo (a su vez, pronominal o no) y cuyas etiquetas se habrán
                    # cambiado ya por las de sus tiempos imperativos asociados.
                    if etiqueta_eagles[:4] == "VMMP" and not defectivo:
                        # Entra una forma imperativa. Tendremos que modificar las formas pronominales y no pronominales
                        # independientemente de si la forma que entra es pronominal o no. Que pa algo nos hemos currado
                        # el silabeador.
                        persona = etiqueta_eagles[4:6]
                        if etiqueta_eagles[7] == "0":
                            # Es una forma no pronominal, tendremos que acentuar y meter el clítico.
                            etiqueta_eagles = etiqueta_eagles[:7] + PRONOMINAL + etiqueta_eagles[8:]
                            flexion[etiqueta_eagles] = []
                            for variante in variantes:
                                palabra = Palabra(palabra_texto=variante,
                                                  calcula_alofonos=False,
                                                  organiza_grafemas=True)
                                if persona == "1P" or (persona == "2P" and flexion[INF][0] != u'ir'):
                                    # Para imperativos de 1ª plural (en -mos), se pierde la "s" ante "nos": démonos
                                    # También se pierde la -d final de la 2ª plural ante "os": dad -> daos (salvo "ir")
                                    palabra.get_silabas()[-1].reset_coda()
                                reflexivo = Palabra(palabra_texto=REFLEXIVOS[persona],
                                                    calcula_alofonos=False,
                                                    organiza_grafemas=True)  # La palabra resultante es átona, OK.
                                variante_pron = Palabra(silabas=palabra.get_silabas() + reflexivo.get_silabas(),
                                                        calcula_alofonos=False,
                                                        organiza_grafemas=True).ajusta_tildes()
                                flexion[etiqueta_eagles].append(variante_pron)
                        else:
                            # Es una forma pronominal. Creamos la forma no pronominal quitando la tilde si no es
                            # por hiato, y quitamos el clítico también.
                            etiqueta_eagles = etiqueta_eagles[:7] + "0" + etiqueta_eagles[8:]
                            flexion[etiqueta_eagles] = []
                            for variante in variantes:
                                palabra = Palabra(palabra_texto=variante,
                                                  calcula_alofonos=False,
                                                  organiza_grafemas=True)
                                palabra.elimina_silaba(-1)
                                # freíos->freí veos->ve bebeos->be'be abríos->abrí idos->i estaos->es'ta estate->es'ta
                                variante_no_pron = palabra.ajusta_tildes()
                                # freí, ve, bebé, abrí, i, está, está
                                if persona == "2P":
                                    # Metemos la "d" perdida: freíd, ved, bebed, abrid, id, estad
                                    variante_no_pron = Palabra(palabra_texto=variante_no_pron + u'd',
                                                               calcula_alofonos=False,
                                                               organiza_grafemas=True).ajusta_tildes()
                                elif persona == "1P":
                                    # Metemos la "s" perdida: friamos, veamos, bebamos, abramos, vayamos, estemos
                                    variante_no_pron = Palabra(palabra_texto=variante_no_pron + u's',
                                                               calcula_alofonos=False,
                                                               organiza_grafemas=True).ajusta_tildes()
                                # Este algoritmo falla en imperativos con diacríticos: de, se -> dé, sé
                                variante_no_pron = u'sé' if variante_no_pron == u'se' else \
                                    u'dé' if variante_no_pron == u'de' else variante_no_pron
                                flexion[etiqueta_eagles].append(variante_no_pron)
                        pass
                pass

            if "impersonal" in datos_conj:
                # Eliminamos las formas que en realidad no existen.
                tiempos_a_eliminar = [u'1S', u'2S', u'2V', u'1P', u'2P']
                if datos_conj["impersonal"] == u'singular':  # Los valores pueden ser "singular" o "plural"
                    tiempos_a_eliminar += [u'3P']
                for tiempo in list(flexion.keys()):
                    if tiempo[4:6] in tiempos_a_eliminar or tiempo[2:4] == "MP":  # Impersonales no tienen imperativo
                        flexion.pop(tiempo, None)

            if incluye_cliticos:
                # Aprovechamos que tenemos la raíz tónica para meter las formas con clíticos.
                Flexionador.conjuga_cliticos(flexion, transitividad, IMPERSONAL if "impersonal" in datos_conj else NA,
                                             PRONOMINAL if datos_conj["pronominal"] else NA)

            # Como puede haber más de una conjugación, aquí vamos añadiendo lo que vamos obteniendo en las sucesivas
            # flexiones. Además, aprovechamos para cambiar el código de verbo modal (VM) a auxiliar (VA)
            # o semiauxiliar (VS) si corresponde.
            tipo = VERBO + \
                (AUXILIAR if lema_txt == u'haber' else COPULATIVO if lema_txt in [u'ser', u'estar'] else PRINCIPAL)
            fuente = u'wik|' + str(acepcion.get_n_entrada()) + u'|' + str(acepcion.get_n_acepcion())
            for etiqueta_eagles, formas_txt in flexion.items():
                etiqueta_eagles = tipo + etiqueta_eagles[2:]
                if etiqueta_eagles not in flexion_completa:
                    flexion_completa[etiqueta_eagles] = {}
                for forma_txt in formas_txt:
                    flexion_completa[etiqueta_eagles][forma_txt] =\
                        flexion_completa[etiqueta_eagles].setdefault(forma_txt, []) + [fuente]

        n_formas = len([forma for etiqueta, formas in flexion_completa.items() for forma in formas])
        if n_formas != 393:
            # verbo_a_txt(flexion_completa)
            pass

        return flexion_completa

    @staticmethod
    def conjuga_vm(datos_conj):
        conjugacion = dict()
        funciones = [Flexionador.conjuga_vmn, Flexionador.conjuga_vmg, Flexionador.conjuga_vmp,
                     Flexionador.conjuga_vmip, Flexionador.conjuga_vmii, Flexionador.conjuga_vmis,
                     Flexionador.conjuga_vmif, Flexionador.conjuga_vmic, Flexionador.conjuga_vmsp,
                     Flexionador.conjuga_vmsi, Flexionador.conjuga_vmsf, Flexionador.conjuga_vmmp]
        for funcion in funciones:
            conjugacion.update(funcion(datos_conj))
        return conjugacion

    # INFINITIVO
    @staticmethod
    def conjuga_vmn(datos_conj):
        vmn = {INF: [datos_conj["lema"]], INF_P: [datos_conj["lema"] + u'se']}
        return vmn

    # GERUNDIO
    @staticmethod
    def conjuga_vmg(datos_conj):
        paradigma = datos_conj["paradigma"]
        nexo = datos_conj["nexos"]["a" if paradigma == 1 else "i"]
        raiz = datos_conj["raices"]["cerr"] + nexo
        semiconsonante = u'' if datos_conj["palatal"] or paradigma == 1 else u'i' \
            if raiz[-1:] not in u'aeiouáéíóú' or raiz[-2:] in [u'gu', u'qu'] else u'y'
        vmg = {GER: [raiz + (u'a' if paradigma == 1 else (semiconsonante + u'e')) + u'ndo'],
               GER_P: [raiz + (u'á' if paradigma == 1 else (semiconsonante + u'é')) + u'ndose']}
        return vmg

    # PARTICIPIO
    @staticmethod
    def conjuga_vmp(datos_conj):
        paradigma = datos_conj["paradigma"]
        if paradigma == 1:
            raices_participio = [datos_conj["raices"]["ato"] + datos_conj["nexos"]["a"] + u'ad']
        else:  # En 2ª y 3ª conjugación el -ido del participio puede formar hiato
            silabas = Palabra(palabra_texto=datos_conj["lema"],
                              calcula_alofonos=False,
                              organiza_grafemas=False).get_silabas()
            if not silabas[-1].get_fonemas_ataque() and len(silabas) > 1 and\
                    not silabas[-2].get_fonemas_coda() and not silabas[-2].get_fonema_semivocal():
                # Se forma un hiato al crear el participio
                raices_participio = [datos_conj["raices"]["ato"] + datos_conj["nexos"]["i"] + u'íd']
            else:
                raices_participio = [datos_conj["raices"]["ato"] + datos_conj["nexos"]["i"] + u'id']
        if "part" in datos_conj["formas"] or "part2" in datos_conj["formas"]:
            # El part2 es el que se usa en las formas compuestas y va el último
            raices_participio = ([datos_conj["formas"]["part"][:-1]] if "part" in datos_conj["formas"] else [])
            raices_participio += ([datos_conj["formas"]["part2"][:-1]] if "part2" in datos_conj["formas"] else [])
            if len(raices_participio) == 2 and raices_participio[0] == raices_participio[1]:
                raices_participio = raices_participio[:1]
        vmp = {PAR_SM: [raiz_participio + u'o' for raiz_participio in raices_participio],
               PAR_SF: [raiz_participio + u'a' for raiz_participio in raices_participio],
               PAR_PM: [raiz_participio + u'os' for raiz_participio in raices_participio],
               PAR_PF: [raiz_participio + u'as' for raiz_participio in raices_participio]}
        return vmp

    # PRESENTE de INDICATIVO
    @staticmethod
    def conjuga_vmip(datos_conj):
        mono = datos_conj["mono"]  # Monosílabo: las agudas tónicas no se acentúan
        paradigma = datos_conj["paradigma"]
        nexos = datos_conj["nexos"]
        raices = datos_conj["raices"]
        vocal_tematica = {1: [u'a', u'á'], 2: [u'e', u'é'], 3: [datos_conj["lema"][-2], u'í']}[paradigma]
        if paradigma == 1:
            vmip = {IP1S: [raices["dip"] + nexos["a"] + u'o'],
                    IP2S: [raices["dip"] + nexos["a"] + u'as'],
                    IP2V: [raices["ato"] + nexos["a"] + (u'ás' if not mono else u'as')],  # Voseo
                    IP3S: [raices["dip"] + nexos["a"] + u'a'],
                    IP1P: [raices["ato"] + nexos["a"] + u'amos'],
                    IP2P: [raices["ato"] + nexos["a"] + (u'áis' if not mono else u'ais')],
                    IP3P: [raices["dip"] + nexos["a"] + u'an']}
        else:  # 2ª y 3ª conj
            vmip = {IP1S: [raices["dip"] + nexos["a"] + u'o'],
                    IP2S: [raices["dip"] + nexos["i"] + u'es'],
                    IP2V: [raices["ato"] + nexos["i"] + vocal_tematica[1 if not mono else 0] + u's'],  # Voseo
                    IP3S: [raices["dip"] + nexos["i"] + u'e'],
                    IP1P: [raices["ato"] + nexos["i"] + vocal_tematica[0] + u'mos'],
                    IP2P: [raices["ato"] + nexos["i"] +
                           ((u'éis' if not mono else u'eis') if paradigma == 2 else (u'ís' if not mono else u'is'))],
                    IP3P: [raices["dip"] + nexos["i"] + u'en']}
        return vmip

    # IMPERFECTO de INDICATIVO
    @staticmethod
    def conjuga_vmii(datos_conj):
        paradigma = datos_conj["paradigma"]
        nexo = datos_conj["nexos"]["a" if paradigma == 1 else "i"]
        raices = datos_conj["raices"]
        morfema = {1: [u'aba', u'ába'], 2: [u'ía', u'ía'], 3: [u'ía', u'ía']}[paradigma]
        raiz = raices["ato"] + nexo + morfema[0]
        vmii = {II1S: [raiz],
                II2S: [raiz + u's'],
                II3S: [raiz],
                II1P: [raices["ato"] + nexo + morfema[1] + u'mos'],
                II2P: [raiz + u'is'],
                II3P: [raiz + u'n']}
        return vmii

    # INDEFINIDO de INDICATIVO
    @staticmethod
    def conjuga_vmis(datos_conj):
        paradigma = datos_conj["paradigma"]
        nexos = datos_conj["nexos"]
        raices = datos_conj["raices"]
        mono = datos_conj["mono"]  # Monosílabo: las agudas tónicas no se acentúan
        if paradigma == 1:
            vmis = {IS1S: [raices["ato"] + nexos["i"] + (u'é' if not mono else u'e')],
                    IS2S: [raices["ato"] + nexos["a"] + u'aste'],
                    IS3S: [raices["cerr"] + nexos["a"] + (u'ó' if not mono else u'o')],
                    IS1P: [raices["ato"] + nexos["a"] + u'amos'],
                    IS2P: [raices["ato"] + nexos["a"] + u'asteis'],
                    IS3P: [raices["cerr"] + nexos["a"] + u'aron']}
        else:  # En 2ª y 3ª conjugación se puede formar hiato
            silabas = Palabra(palabra_texto=datos_conj["lema"],
                              calcula_alofonos=False,
                              organiza_grafemas=False).get_silabas()
            if not silabas[-1].get_fonemas_ataque() and len(silabas) > 1 and \
                    not silabas[-2].get_fonemas_coda() and not silabas[-2].get_fonema_semivocal() and\
                    not nexos["i"]:
                # Se forma un hiato
                hay_hiato = True
            else:
                hay_hiato = False
            vmis = {IS1S: [raices["ato"] + nexos["i"] + (u'í' if not mono else u'i')],
                    IS2S: [raices["ato"] + nexos["i"] + (u'iste' if not hay_hiato else u'íste')],
                    IS3S: [raices["cerr"] + nexos["i"] +
                           (u'yó' if hay_hiato and raices["cerr"][-1] in u'ieaou'
                            else (u'ió' if not mono or datos_conj["palatal"]
                                  else u'io')[1 if datos_conj["palatal"] else 0:])],
                    IS1P: [raices["ato"] + nexos["i"] + (u'imos' if not hay_hiato else u'ímos')],
                    IS2P: [raices["ato"] + nexos["i"] + (u'isteis' if not hay_hiato else u'ísteis')],
                    IS3P: [raices["cerr"] + nexos["i"] + (u'yeron' if hay_hiato and raices["cerr"][-1] in u'ieaou'
                                                          else u'ieron')[1 if datos_conj["palatal"] else 0:]]}
        return vmis

    # FUTURO de INDICATIVO
    @staticmethod
    def conjuga_vmif(datos_conj, elipsis=False):
        paradigma = datos_conj["paradigma"]
        nexo = datos_conj["nexos"]["a" if paradigma == 1 else "i"]
        raices = datos_conj["raices"]
        vocal_tematica = {1: [u'a', u'á'], 2: [u'e', u'é'], 3: [u'i', u'í']}[paradigma] if not elipsis else [u'', u'']
        raiz = raices["ato"] + nexo + vocal_tematica[0]
        vmif = {IF1S: [raiz + u'ré'], IF2S: [raiz + u'rás'], IF3S: [raiz + u'rá'],
                IF1P: [raiz + u'remos'], IF2P: [raiz + u'réis'], IF3P: [raiz + u'rán']}
        return vmif

    # CONDICIONAL
    @staticmethod
    def conjuga_vmic(datos_conj, elipsis=False):
        paradigma = datos_conj["paradigma"]
        nexo = datos_conj["nexos"]["a" if paradigma == 1 else "i"]
        raices = datos_conj["raices"]
        v_ato = {1: u'a', 2: u'e', 3: u'i'}[paradigma] if not elipsis else u''
        raiz = raices["ato"] + nexo + v_ato + u'ría'
        vmcp = {IC1S: [raiz], IC2S: [raiz + u's'], IC3S: [raiz],
                IC1P: [raiz + u'mos'], IC2P: [raiz + u'is'], IC3P: [raiz + u'n']}
        return vmcp

    # PRESENTE de SUBJUNTIVO
    @staticmethod
    def conjuga_vmsp(datos_conj, gutural=False):
        gut = u'' if not gutural else u'g'
        paradigma = datos_conj["paradigma"]
        nexos = datos_conj["nexos"]
        raices = datos_conj["raices"]
        mono = datos_conj["mono"] and not datos_conj["palatal"]  # Si palataliza hay una sílaba más por la "y".
        v_ato = {1: nexos["i"] + gut + u'e', 2: nexos["a"] + gut + u'a', 3: nexos["a"] + gut + u'a'}[paradigma]
        v_ton = {1: nexos["i"] + gut + u'é', 2: nexos["a"] + gut + u'á', 3: nexos["a"] + gut + u'á'}[paradigma]
        vmsp = {SP1S: [raices["dip"] + v_ato],
                SP2S: [raices["dip"] + v_ato + u's'],
                SP2V: [raices["cerr"] + (v_ton if not mono else v_ato) + u's'],
                SP3S: [raices["dip"] + v_ato],
                SP1P: [raices["cerr"] + v_ato + u'mos'],
                SP2P: [raices["cerr"] + (v_ton if not mono else v_ato) + u'is'],
                SP3P: [raices["dip"] + v_ato + u'n']}
        return vmsp

    # IMPERFECTO de SUBJUNTIVO
    @staticmethod
    def conjuga_vmsi(datos_conj):
        paradigma = datos_conj["paradigma"]
        nexos = datos_conj["nexos"]
        raices = datos_conj["raices"]
        semiconsonante = u'' if datos_conj["palatal"] or paradigma == 1 else u'i' \
            if (raices["cerr"] + nexos["i"])[-1:] not in u'aeiouáéíóú' or\
               (raices["cerr"] + nexos["i"])[-2:] in [u'gu', u'qu'] else u'y'
        v_ato = (nexos["a"] + u'a') if paradigma == 1 else (nexos["i"] + (semiconsonante + u'e'))
        v_ton = (nexos["a"] + u'á') if paradigma == 1 else (nexos["i"] + (semiconsonante + u'é'))
        raiz_ra = raices["cerr"] + v_ato + u'ra'
        raiz_se = raices["cerr"] + v_ato + u'se'
        vmsi = {SI1S: [raiz_ra, raiz_se],
                SI2S: [raiz_ra + u's', raiz_se + u's'],
                SI3S: [raiz_ra, raiz_se],
                SI1P: [raices["cerr"] + v_ton + u'ramos', raices["cerr"] + v_ton + u'semos'],
                SI2P: [raiz_ra + u'is', raiz_se + u'is'],
                SI3P: [raiz_ra + u'n', raiz_se + u'n']}
        return vmsi

    # FUTURO de SUBJUNTIVO
    @staticmethod
    def conjuga_vmsf(datos_conj):
        paradigma = datos_conj["paradigma"]
        nexos = datos_conj["nexos"]
        raices = datos_conj["raices"]
        semiconsonante = u'' if datos_conj["palatal"] or paradigma == 1 else u'i' \
            if (raices["cerr"] + nexos["i"])[-1:] not in u'aeiouáéíóú' or\
               (raices["cerr"] + nexos["i"])[-2:] in [u'gu', u'qu'] else u'y'
        v_ato = (nexos["a"] + u'a') if paradigma == 1 else (nexos["i"] + (semiconsonante + u'e'))
        v_ton = (nexos["a"] + u'á') if paradigma == 1 else (nexos["i"] + (semiconsonante + u'é'))
        raiz_re = raices["cerr"] + v_ato + u're'
        vmsf = {SF1S: [raiz_re],
                SF2S: [raiz_re + u's'],
                SF3S: [raiz_re],
                SF1P: [raices["cerr"] + v_ton + u'remos'],
                SF2P: [raiz_re + u'is'],
                SF3P: [raiz_re + u'n']}
        return vmsf

    # IMPERATIVO
    @staticmethod
    def conjuga_vmmp(datos_conj, gutural=False):
        if datos_conj["lema"] == u'equivaler':
            pass
        gut = u'' if not gutural else u'g'
        mono = datos_conj["mono"]  # Monosílabo: las agudas tónicas no se acentúan
        paradigma = datos_conj["paradigma"]
        nexos = datos_conj["nexos"]
        raices = datos_conj["raices"]
        v_ato = {1: nexos["a"] + u'a', 2: nexos["i"] + u'e', 3: nexos["i"] + datos_conj["lema"][-2]}[paradigma]
        v_ton = {1: nexos["a"] + u'á', 2: nexos["i"] + u'é', 3: nexos["i"] + u'í'}[paradigma]

        if paradigma == 1:
            vmmp = {MP2S: [raices["dip"] + v_ato],
                    MP2V: [raices["ato"] + (v_ton if not mono else v_ato)],  # Posible monosílabo inacentuado
                    MP3S: [raices["dip"] + nexos["i"] + u'e'],
                    MP1P: [raices["cerr"] + nexos["i"] + u'emos'],
                    MP2P: [raices["ato"] + v_ato + u'd'],
                    MP3P: [raices["dip"] + nexos["i"] + u'en'],
                    MP2S_P: [raices["ton"] + v_ato + u'te'],
                    MP2V_P: [raices["ato"] + v_ato + u'te'],
                    MP3S_P: [raices["ton"] + nexos["i"] + u'ese'],
                    MP1P_P: [raices["cerr"] + nexos["i"] + u'émonos'],
                    MP2P_P: [raices["ato"] + v_ato + u'os'],
                    MP3P_P: [raices["ton"] + nexos["i"] + u'ense']}
        else:  # 2ª y 3ª conj
            vmmp = {MP2S: [raices["dip"] + nexos["i"] + u'e'],
                    MP2V: [raices["ato"] + (v_ton if not mono else v_ato)],  # Posible monosílabo inacentuado
                    MP3S: [raices["dip"] + nexos["a"] + gut + u'a'],
                    MP1P: [raices["cerr"] + nexos["a"] + gut + u'amos'],
                    MP2P: [raices["ato"] + v_ato + u'd'],
                    MP3P: [raices["dip"] + nexos["a"] + gut + u'an'],
                    MP2S_P: [raices["ton"] + nexos["i"] + u'ete'],
                    MP2V_P: [raices["ato"] + v_ato + u'te'],
                    MP3S_P: [raices["ton"] + nexos["a"] + gut + u'ase'],
                    MP1P_P: [raices["cerr"] + nexos["a"] + gut + u'ámonos'],
                    MP2P_P: [raices["ato"] +
                             (v_ato if paradigma == 2 else (v_ato + u'd') if datos_conj["lema"] == u'ir' else v_ton) +
                             u'os'],  # Posible hiato acentuado, e "ir" única excepción id -> idos (y no íos)
                    MP3P_P: [raices["ton"] + nexos["a"] + gut + u'anse']}
        return vmmp

    # CLÍTICOS
    @staticmethod
    def conjuga_cliticos(flexion, transitividad, impersonalidad, pronominalidad):
        """
        http://lema.rae.es/dpd/srv/search?id=elLl31yYnD65MTS9uF
        Los clíticos van en orden de pronominal + objeto indirecto + objeto directo. El pronominal siempre concuerda
        con la persona del verbo (o "se" en formas no personales). El de objeto indirecto tiene persona y número, y
        en 1ª y 2ª persona, si va solo, puede ser también clítico de objeto directo (quiere matarme).
        Técnicamente cosas como ¿quieres morírteme? son válidas. De hecho se recogen muchas de estas combinaciones en
        este algoritmo, aunque se considera que el primer clítico es de OD y 2º de OI (dativo ético), cuando nosotros
        etiquetamos el 1º como de pronominal y el segundo de OI. No se etiqueta "bien" porque son realmente
        extrañas y además complicarían todo muchísimo, no solo el algoritmo en sí, sino la etiqueta (tendríamos un
        clítico de OD que no tendría género y número, sino persona y números -nos haría falta un carácter extra de
        persona también para el clítico de OD).
        Además, el orden de los clíticos es "se" (pronomoninal) -> 2ª -> 1ª -> 3ª. Con este algoritmo solo lo
        incumpliríamos con formas pronominales de 1ª persona seguida de clítico de OI/OD de 2ª, y crearíamos cosas como
        carguémonoste/carguémonoos cuando debería ser carguémostenos/carguémoosnos, pero estas formas no se permiten.

        Al conjugar el verbo, hemos metido ya las formas pronominales de infinitivo, gerundio e imperativo.
        Añadimos el resto de formas en: -se + me/te/(l/s)e/nos/os/(l/s)es + l(o/a)(s) teniendo en cuenta las
        combinaciones posibles de estos tres elementos, que depende de la forma a la que se añadan.
        :param flexion:
        :param transitividad:
        :param impersonalidad:
        :param pronominalidad:
        :return:
        """

        # Los verbos impersonales no tienen imperativo. Además, si el verbo no es pronominal y hemos añadido etiquetas
        # pronominales, es que es transitivo y las formas tipo "entrégateme", que se crean con etiqueta pronominal + oi,
        # en realidad se interpretarán como od + oi.
        formas_con_clitico = [INF, GER] + ([INF_P, GER_P] if pronominalidad == PRONOMINAL else []) +\
            ([] if impersonalidad == IMPERSONAL else ([MP2S, MP2V, MP3S, MP1P, MP2P, MP3P] +
             ([MP2S_P, MP2V_P, MP3S_P, MP1P_P, MP2P_P, MP3P_P] if pronominalidad == PRONOMINAL else [])))
        for etiqueta_forma_base in formas_con_clitico:
            if etiqueta_forma_base not in flexion:
                # Hay verbos defectivos sin gerundio, sin algunas o todas las formas imperativas (impersonales y otros).
                # También puede ser que queramos crear una forma "pronominal" de un verbo no pronominal, que en
                # realidad se etiquetará como pronominal pero es un caso de doble dativo (con dativo ético) de 1ª y 2ª,
                # es decir,
                # cosas como "acércatenos" con el significado de "entreganos a ti", que
                continue
            for forma_base in flexion[etiqueta_forma_base]:
                if forma_base == u'argüir':
                    pass
                palabra = Palabra(palabra_texto=forma_base,
                                  calcula_alofonos=False,
                                  organiza_grafemas=True)
                posicion_tonica = palabra.get_posicion_tonica()  # 0 es átona, -1 aguda, -2 llana...
                if posicion_tonica == 0:
                    if forma_base in [u'para', u'sobre', u'entre', u'ora']:
                        posicion_tonica = -2
                        palabra.get_silabas()[0].set_tonica(ACPR)
                    else:
                        print(u'¿Un verbo que es átono?', forma_base)
                        beep(200, 1000)
                        continue

                if posicion_tonica == -1:
                    # La forma base es aguda (comer, comé, supón, id...).
                    # No puede haber forma aguda (siempre añadimos al menos un clítico, las formas base sin clíticos ya
                    # están hechas), la forma llana es sin tilde (si la hubiera) salvo que sea
                    # por hiato), y las formas esdrújulas y posteriores llevan tilde.
                    if palabra.contiene_hiato():
                        # Da igual los clíticos, siempre se mantiene la tilde
                        formas = {-2: forma_base, -3: forma_base}
                    else:
                        forma_llana = forma_base.replace(u'í', u'i').replace(u'é', u'e').replace(u'á', u'a'). \
                            replace(u'ó', u'o').replace(u'ú', u'u')
                        formas = {-2: forma_llana, -3: palabra.set_tilde(con_tilde=True)}
                elif posicion_tonica == -2:
                    # La forma base es llana: come, comiendo, comeos...
                    # Las formas aguda y llana no se usan. La forma esdrújula y posteriores lleva tilde.
                    formas = {-3: palabra.set_tilde(con_tilde=True)}
                else:  # elif posicion_tonica <= -3:
                    # La forma base es esdrújula: cómete.
                    formas = {-3: forma_base}
                etiqueta_pronominal = etiqueta_forma_base[7]
                # OJO: las formas de vos son siempre las formas de tú con un retraso de una sílaba en la tonicidad. Pero
                # eso elimina las diptongaciones (duerme-dormí, juega-jugá, miente-mentí). Así que se hacen aparte.
                for etiqueta_oi in OBJETOS_INDIRECTOS.keys():
                    if etiqueta_oi == NA + NA:
                        pass
                    for etiqueta_od in (OBJETOS_DIRECTOS.keys() if transitividad == TRANSITIVO else [NA + NA]):
                        n_cliticos = (1 if etiqueta_pronominal != NA else 0) + \
                                     (1 if etiqueta_oi != NA + NA else 0) + \
                                     (1 if etiqueta_od != NA + NA else 0)
                        if n_cliticos == 0 or (n_cliticos == 1 and etiqueta_pronominal == PRONOMINAL):
                            # Ya lo habíamos creado. Bien es la versión sin ningún clítico, o solo el de pronominal
                            continue
                        if etiqueta_forma_base[2] in INFINITIVO + GERUNDIO:  # INFINITIVO Y GERUNDIO
                            if n_cliticos == 3 and etiqueta_oi[0] == TERCERA:
                                # Formas como dormírseselo. Tachadas rojas.
                                continue
                            elif n_cliticos == 2:
                                # Las formas en -sel[oa]s? pueden considerarse pronominales o de oi + od.
                                if pronominalidad == PRONOMINAL and etiqueta_pronominal != PRONOMINAL and\
                                        etiqueta_oi[0] == TERCERA and etiqueta_od != NA + NA:
                                    # Las formas en -sel[oa]s? se consideran pronominales y no de oi + od.
                                    # Sólido salmón
                                    continue
                                if pronominalidad != PRONOMINAL and etiqueta_pronominal == PRONOMINAL:
                                    # Es un verbo no pronominal y las formas en -sel[oa]s? son de oi + od.
                                    # Sólido naranja
                                    continue
                        elif etiqueta_forma_base[2] == IMPERATIVO:  # IMPERATIVO
                            if n_cliticos == 3:
                                # En infinitivo y gerundio se aceptan formas con tres clíticos siempre que no produzcan
                                # una forma -sese- (es decir, siempre que el clítico de OI no sea de 3ª
                                # En imperativo la cosa está más restringida: solo se aceptan si el OI es de 1ª, y
                                # además, si la forma imperativa no es de 1ª (porque produce formas con clíticos de
                                # misma persona pero distinto número -en sigular- o de clítico repetido -en plural-).
                                if etiqueta_forma_base[4] == PRIMERA or etiqueta_oi[0] != PRIMERA:
                                    continue
                            if (etiqueta_forma_base[4] == etiqueta_oi[0] == SEGUNDA and
                                    etiqueta_forma_base[5].replace(VOS, SINGULAR) != etiqueta_oi[1]) or\
                                    (etiqueta_forma_base[4] == PRIMERA and etiqueta_oi[0] == PRIMERA and
                                     etiqueta_forma_base[5] != etiqueta_oi[1] and etiqueta_pronominal == PRONOMINAL):
                                # En 2ª persona y dativo de distinto nº: entrégaoslo, entregáteos, entreguémonosme...
                                # Tachado verde
                                continue
                            if etiqueta_pronominal == PRONOMINAL and etiqueta_oi[0] != TERCERA and\
                                    etiqueta_oi == etiqueta_forma_base[4:6].replace(VOS, SINGULAR):
                                # Tachado morado
                                continue
                            if etiqueta_forma_base[4] == TERCERA and etiqueta_oi[0] == SEGUNDA:
                                # Distinto tratamiento para segunda persona (usted -> tú/vosotros).
                                # Tachado rosa.
                                continue
                            if etiqueta_forma_base[4] == PRIMERA and etiqueta_pronominal == PRONOMINAL and\
                                    etiqueta_oi[0] == SEGUNDA:
                                # Orden indebido. En vez de "entreguémonoste" debería ser "entreguémostenos"
                                # Tachado azul.
                                continue
                            if pronominalidad == PRONOMINAL and etiqueta_pronominal != PRONOMINAL and\
                                    etiqueta_forma_base[4:6].replace(VOS, SINGULAR) == etiqueta_oi and\
                                     (etiqueta_forma_base[4] != TERCERA or n_cliticos == 2):
                                # Parte propia de los verbos no pronominales (oi (+ od)).
                                # Sólido salmón
                                continue

                        morfema_od = OBJETOS_DIRECTOS[etiqueta_od]
                        if etiqueta_oi[0] == TERCERA and etiqueta_od != NA + NA:
                            # Tenemos clítico de oi de 3ª, seguido de clítico de od, con lo que le/les pasa a "se".
                            # Con el cambio, se pierde la información de número, con lo que coinciden plural y singular.
                            if etiqueta_oi[1] == PLURAL:
                                # Al añadir el "singular", como es invariable en número, ya vale también por la plural.
                                continue
                            morfema_oi = u'se'
                            etiqueta_eagles = etiqueta_forma_base[:7] + etiqueta_pronominal +\
                                TERCERA + INVARIABLE + etiqueta_od
                        else:
                            morfema_oi = OBJETOS_INDIRECTOS[etiqueta_oi]
                            etiqueta_eagles = etiqueta_forma_base[:7] + etiqueta_pronominal + etiqueta_oi + etiqueta_od
                        raiz = formas[max(-3, posicion_tonica - n_cliticos)]
                        if ((etiqueta_forma_base[4:6] == PRIMERA + PLURAL and morfema_oi and morfema_oi[0] in u'sno') or
                                (etiqueta_forma_base[4:6] == SEGUNDA + PLURAL and morfema_oi and morfema_oi[0] == u'o') and
                                flexion[INF][0] != u'ir'):
                            # Para imperativos de 1ª plural (en -mos), se pierde la "s" ante "se", "nos", "os": démonos
                            # También se pierde la -d final de la 2ª plural ante "os": amad -> amaos (salvo "ir")
                            raiz = raiz[:-1]
                        if raiz[-1] == u'i' and morfema_oi and morfema_oi[0] == u'o':
                            # Aparece un hiato: desvivid -> desvivíos, decí -> decíos
                            raiz = raiz[:-1] + u'í'
                        if raiz[-1] == u'l' and (morfema_oi + morfema_od)[0] == u'l':
                            # Caso exclusivo para "sal" (y derivados) y sus formas con lo, los, la, las, le, les.
                            # Es una curiosidad del español, pero estas formas, literalmente, no se pueden escribir.
                            continue
                        forma = raiz + morfema_oi + morfema_od
                        flexion[etiqueta_eagles] = flexion.setdefault(etiqueta_eagles, []) + [forma]
            pass
        if False:
            # Ahora mismo, las formas pronominales "básicas" (sólo con el clítico reflexivo) de 1ª y 2ª coinciden con las
            # formas no pronominales pero con oi/od. Las borramos si es el caso.
            if pronominalidad != PRONOMINAL:
                for etiqueta_forma_base in [MP2S_P, MP2V_P, MP3S_P, MP1P_P, MP2P_P, MP3P_P]:
                    flexion.pop(etiqueta_forma_base)
        pass

    @staticmethod
    def pluraliza(forma_singular, formas_expandidas=None):
        # TODO: tema de latinismos (k))
        # Se sigue escrupulosamente lo indicado en http://lema.rae.es/dpd/srv/search?id=Iwao8PGQ8D6QkHPn4i
        # Más casos extraídos de: https://books.google.es/books?id=63heLVFoS4EC&pg=PA141&lpg=PA141&dq=%C2%BFcu%C3%A1l+es+el+plural+de+caney?&source=bl&ots=b-6lwFLa0G&sig=d7r9YAzR37xDCYMQp3OiAvAWdV8&hl=es&sa=X&ved=0ahUKEwj2vaq5leTSAhUH1hQKHahdAMcQ6AEIGjAA#v=onepage&q=caney&f=false
        # http://www.redeletras.com/rules/reglamento2010.pdf
        # http://www.ajscrabble.org/joomla/index.php/reglamento-lexico/196-reglamento-lexico-fise
        # Resto de casos revisados manualmente y se ha decidido el plural bien porque aparece en la definición
        # (normalmente en alguna locución), bien por propio conocimiento.
        palabra_singular = Palabra(palabra_texto=forma_singular,
                                   calcula_alofonos=False,
                                   organiza_grafemas=True)
        ultima_silaba = palabra_singular.get_silabas()[-1]
        grafemas_coda = ultima_silaba.get_grafemas_coda()
        ultimo_caracter = forma_singular[-1]
        if ultimo_caracter != ultimo_caracter.lower():
            # Hay mayúsculas y es una sigla o acrónimo. Es invariante
            return [forma_singular]
        if (len(forma_singular) == 1 and forma_singular not in u'aeiou') or\
                forma_singular in [u'ch', u'gu', u'll', u'qu', u'rr']:
            return [forma_singular]  # Es un nombre de letra, incluyendo la "y". Invariable
        if len(grafemas_coda) > 1:
            # j) Sustantivos y adjetivos terminados en grupo consonántico. Procedentes todos ellos de otras lenguas,
            #    forman el plural con -s (salvo aquellos que terminan ya en -s, que siguen la regla general; → f):
            #    gong, pl. gongs; iceberg, pl. icebergs; récord, pl. récords. Se exceptúan de esta norma las voces
            #    compost, karst, test, trust y kibutz, que permanecen invariables en plural, pues la adición de una
            #    -s en estos casos daría lugar a una secuencia de difícil articulación en español.
            #    También son excepción los anglicismos lord y milord, cuyo plural asentado en español es
            #    lores y milores, respectivamente.
            if forma_singular in [u'lord', u'milord']:
                return [forma_singular[:-1] + u'es']
            if grafemas_coda[0].get_grafema_txt() in u'sz' or grafemas_coda[1].get_grafema_txt() in u'z':
                return [forma_singular]  # Invariante por dificultad de pronunciación
            if ultimo_caracter != u's':  # Si acaba en -s sigue la norma general, que depende de la tonicidad
                # Curiosamente, no se considera que haya cambios de acentuación: iceberg-icebergs, récord-récords
                # Debe de ser que las normas de acentuación de la -s es si es coda simple.
                return [forma_singular + u's']
        if ultimo_caracter in u'aeioué':
            # a) Sustantivos y adjetivos terminados en vocal átona o en -e tónica. Forman el plural con -s:
            #    casas, estudiantes, taxis, planos, tribus, comités.
            if forma_singular in [u'a', u'o', u'i', u'u']:
                return [(u'í' if forma_singular == u'i' else u'ú' if forma_singular == u'u' else forma_singular) +
                        u'es']
            if forma_singular == u'e':
                return [u'es']
            if forma_singular in [u'abanda', u'agujita', u'antiaborto', u'antidopaje', u'antimafia', u'antipolio',
                                  u'antisistema', u'antitabaco', u'antiviolencia', u'carbonara', u'cochite',
                                  u'curalotodo', u'hervite', u'hi', u'metomentodo', u'multiplataforma',
                                  u'percápita', u'pollito', u'sabelotodo', u'sanalotodo',
                                  u'cualque', u'qué']:
                return [forma_singular]
            if forma_singular in [u'hijodalgo', u'hijadalgo', u'fijodalgo', u'fijadalgo']:
                return [forma_singular[:4] + u'sdalgo']
            elif forma_singular in [u'gentilhombre']:
                return [u'gentilhombres', u'gentileshombres']
            elif forma_singular in [u'ricadueña', u'ricahembra', u'ricohombre']:
                return [forma_singular + u's', forma_singular[:4] + u's' + forma_singular[4:] + u's']
            elif forma_singular in [u'buenmozo']:
                return [u'buenosmozos']
            elif forma_singular in [u'buenamoza']:
                return [u'buenasmozas']
            elif forma_singular == u'cualquiera':
                return [u'cualesquiera', u'cualesquier']
            elif forma_singular == u'quienquiera':
                return [u'quienesquiera']
            elif forma_singular in [u'ucé', u'usarcé', u'voacé']:
                return [forma_singular[:-1] + u'edes']
            elif forma_singular == u'no':  # Véase b)
                return [u'noes']
            formas_plural = [forma_singular + u's']
            if forma_singular == u'yo':  # Véase b)
                formas_plural.append(u'yoes')
            return formas_plural
        elif ultimo_caracter in u'áó':
            # b) Sustantivos y adjetivos terminados en -a o en -o tónicas. Aunque durante algún tiempo vacilaron
            #    entre el plural en -s y el plural en -es, en la actualidad forman el plural únicamente con -s:
            #    papás, sofás, bajás, burós, rococós, dominós. Son excepción a esta regla los sustantivos
            #    faralá y albalá, y el adverbio no en función sustantiva, que forman el plural con -es:
            #    faralaes, albalaes, noes. También es excepción el pronombre yo cuando funciona como sustantivo,
            #    pues admite ambos plurales: yoes y yos.
            if forma_singular in [u'albalá', u'faralá']:
                return [forma_singular[:-1] + u'aes']
            if forma_singular in [u'premamá', u'seó']:
                return [forma_singular]
            return [forma_singular + u's']
        elif ultimo_caracter in u'íú':
            # c) Sustantivos y adjetivos terminados en -i o en -u tónicas. Admiten generalmente dos formas de plural,
            #    una con -es y otra con -s, aunque en la lengua culta suele preferirse la primera: bisturíes o bisturís,
            #    carmesíes o carmesís, tisúes o tisús, tabúes o tabús. En los gentilicios, aunque no se consideran
            #    incorrectos los plurales en -s, se utilizan casi exclusivamente en la lengua culta los plurales en -es:
            #    israelíes, marroquíes, hindúes, bantúes. Por otra parte, hay voces, generalmente las procedentes
            #    de otras lenguas o las que pertenecen a registros coloquiales o populares, que solo forman el plural
            #    con -s: gachís, pirulís, popurrís, champús, menús, tutús, vermús. El plural del adverbio sí,
            #    cuando funciona como sustantivo, es síes, a diferencia de lo que ocurre con la nota musical si,
            #    cuyo plural es sis (→ l).
            if forma_singular in [u'ambigú', u'bambú', u'benjuí', u'canesú', u'cañí', u'chacolí', u'champú',
                                  u'chantillí', u'cucú', u'frufrú', u'gachí', u'gilí', u'interviú', u'menjuí', u'menú',
                                  u'mildiú', u'paspartú', u'pirulí', u'popurrí', u'quepí', u'ragú', u'recibí',
                                  u'taichí', u'tisú', u'travestí', u'tutú', u'vermú']:
                return [forma_singular + u's']
            if forma_singular in [u'sefardí', u'sí']:
                return [forma_singular + u'es']
            if forma_singular == u'así':
                return [forma_singular]
            if forma_singular in [u'mambí', u'maravedí']:
                return [forma_singular + u's', forma_singular + u'es', forma_singular[:-1] + u'ises']
            return [forma_singular + u's', forma_singular + u'es']
        elif ultimo_caracter in u'y':
            if len(forma_singular) > 1 and forma_singular[-2] in u'aeiou':
                # d) Sustantivos y adjetivos terminados en -y precedida de vocal. Forman tradicionalmente su plural
                #    con -es: rey, pl. reyes; ley, pl. leyes; buey, pl. bueyes; ay, pl. ayes; convoy, pl. convoyes;
                #    bocoy, pl. bocoyes. Sin embargo, los sustantivos y adjetivos con esta misma configuración que se
                #    han incorporado al uso más recientemente —en su mayoría palabras tomadas de otras lenguas— hacen
                #    su plural en -s. En ese caso, la y del singular mantiene en plural su carácter vocálico y,
                #    por lo tanto, debe pasar a escribirse i (→ i, 5b): gay, pl. gais; jersey, pl. jerséis;
                #    espray, pl. espráis; yóquey, pl. yoqueis. Pertenecen a la etapa de transición entre ambas normas
                #    y admiten, por ello, ambos plurales las palabras coy, pl. coyes o cois;
                #    estay, pl. estayes o estáis; noray, pl. norayes o noráis; guirigay, pl. guirigayes o guirigáis,
                #    con preferencia hoy por las formas con -s.
                if forma_singular in [u'fray', u'frey', u'hoy', u'ocrey', u'troy']:
                    return [forma_singular]
                if forma_singular in [u'aguapey', u'aguay', u'bacaray', u'candray', u'cay', u'chancay', u'chuflay',
                                      u'display', u'escay', u'espay', u'espray', u'gay', u'giley', u'gray', u'guay',
                                      u'jersey', u'lay', u'muimuy', u'órsay', u'paipay', u'póney', u'quilmay',
                                      u'samuray', u'timboy', u'vacaray', u'yérsey', u'yóquey']:
                    # Admiten solo el plural en -is
                    return [Palabra(palabra_texto=forma_singular,
                                    calcula_alofonos=True,
                                    organiza_grafemas=True).reset_semivocal().ajusta_tildes() + u'is']
                if forma_singular in [u'bogey', u'disc-jockey', u'hockey', u'spray']:
                    # Son voces inglesas escritas sin tilde.
                    return [forma_singular[:-1] + u'is']
                if forma_singular in [u'acroy', u'aguaribay', u'barangay', u'cambray', u'choroy', u'contraestay',
                                      u'contray', u'coy', u'estay', u'guirigay', u'noray', u'ñandubay', u'sinamay',
                                      u'taray', u'tipoy', u'ubajay', u'urunday', u'urundey', u'verdegay', u'yatay']:
                    # Admiten dos plurales: -is y -yes
                    return [Palabra(palabra_texto=forma_singular,
                                    calcula_alofonos=True,
                                    organiza_grafemas=True).reset_semivocal().ajusta_tildes() + u'is',
                            forma_singular + u'es']
                if forma_singular in [u'abey', u'amancay', u'ampay', u'anay', u'araguaney', u'ay', u'balay', u'batey',
                                      u'bey', u'bocoy', u'botamay', u'buey', u'cacuy', u'caney', u'caracatey',
                                      u'carapachay', u'caray', u'carey', u'catey', u'choconoy', u'choroy', u'chuchuy', u'cocuy',
                                      u'coicoy', u'coletuy', u'colliguay', u'convoy', u'copey', u'cucuy', u'cuicuy', u'curamagüey',
                                      u'curujey', u'curupay', u'cuy', u'detienebuey', u'dey', u'ensay', u'espumuy',
                                      u'garay', u'grey', u'gualanday', u'guararey', u'güey', u'gulay', u'huacatay',
                                      u'jagüey', u'juey', u'ley', u'maguey', u'malangay', u'mamey', u'matabuey',
                                      u'merey', u'monterrey', u'morrocoy', u'pacay', u'palay', u'paraguay', u'patay',
                                      u'pejerrey', u'picuy', u'pijibay', u'pitoitoy', u'pijuy', u'playboy', u'quillay', u'quibey',
                                      u'rentoy', u'rey', u'sangley', u'siboney', u'sotorrey', u'suquinay', u'tentabuey',
                                      u'tepuy', u'vacabuey', u'virrey', u'visorrey', u'yarey']:
                    # Admiten solo el plural en -yes.
                    return [forma_singular + u'es']
                print(u'Hemos hecho el plural de', forma_singular, u'como', forma_singular + u'es')
                return [forma_singular + u'es']
            elif len(forma_singular) > 1 and forma_singular[-2] not in u'aeiou':
                # e) Voces extranjeras terminadas en -y precedida de consonante. Deben adaptarse gráficamente
                #    al español sustituyendo la -y por -i: dandi (del ingl. dandy); panti (del ingl. panty);
                #    ferri (del ingl. ferry). Su plural se forma, como el de las palabras españolas con esta
                #    terminación (→ a), añadiendo una -s: dandis, pantis, ferris
                return [forma_singular[:-1] + u'is']
        elif ultimo_caracter in u'sx':
            # f) Sustantivos y adjetivos terminados en -s o en -x. Si son monosílabos o polisílabos agudos,
            #    forman el plural añadiendo -es: tos, pl. toses; vals, pl. valses, fax, pl. faxes;
            #    compás, pl. compases; francés, pl. franceses. En el resto de los casos, permanecen invariables:
            #    crisis, pl. crisis; tórax, pl. tórax; fórceps, pl. fórceps. Es excepción a esta regla la palabra
            #    dux, que, aun siendo monosílaba, es invariable en plural: los dux. También permanecen invariables
            #    los polisílabos agudos cuando se trata de voces compuestas cuyo segundo elemento es ya un plural:
            #    ciempiés, pl. ciempiés (no ciempieses); buscapiés, pl. buscapiés (no buscapieses),
            #    pasapurés, pl. pasapurés (no pasapureses).
            # OJO: lo de las palabras compuestas no parece aplicarse a burofax, telefax, bonobús...
            if palabra_singular.get_posicion_tonica() == -1:
                if len(palabra_singular.get_silabas()) == 1:
                    if forma_singular in [u'ex', u'dux', u'beis', u'siux']:
                        return [forma_singular]
                    return [Palabra(palabra_texto=forma_singular + u'es',
                                    calcula_alofonos=False,
                                    organiza_grafemas=True).ajusta_tildes()]  # Se quita la tilde a la vocal acentuada
                # Tenemos un problema, porque el diccionario de la RAE no da ninguna pista sobre si una palabra es
                # compuesta o no. La acepción de "compás" y la de "milpiés" no indica que haya ninguna diferencia en
                # este aspecto. Se ha revisado a mano.
                # En principio, si el lema tiene formas distintas para masculino y femenino, hay que añadir -es,
                if (not formas_expandidas or len(formas_expandidas) == 1) and\
                        forma_singular in [u'antiestrés', u'antigás', u'añás', u'arrastrapiés', u'avampiés', u'biribís', u'bisbís',
                                           u'calientapiés', u'champuses', u'chasís', u'chischís', u'ciempiés',
                                           u'cientopiés', u'corps', u'correverás', u'corriverás', u'cortapiés', u'cuscús',
                                           u'demás', u'después', u'entrés', u'estriptís', u'milpiés', u'buscapiés',
                                           u'guardapiés', u'moisés', u'moradux', u'pasapurés', u'pesabebés',
                                           u'portabebés', u'quesiqués', u'rapapiés', u'relax', u'reposapiés', u'reps',
                                           u'tapapiés', u'trastrás', u'unisex', u'ziszás']:
                    return [forma_singular]  # Invariante por ser palabra compuesta
                forma_plural = Palabra(palabra_texto=forma_singular + u'es',
                                       calcula_alofonos=False,
                                       organiza_grafemas=True).ajusta_tildes()  # Se quita la tilde si procede
                # print(forma_singular, u'->', forma_plural, u'(pensamos que añade -es)' + (u' doble forma' if formas_expandidas and len(formas_expandidas) > 1 else u''))
                return [forma_plural]  # Se quita la tilde a la vocal acentuada
            else:
                return [forma_singular]  # Invariante porque no es agudo (ni monosílabo)
        elif ultimo_caracter in u'lrndzj':
            # g) Sustantivos y adjetivos terminados en -l, -r, -n, -d, -z, -j. Si no van precedidas de otra
            #    consonante (→ j), forman el plural con -es: dócil, pl. dóciles; color, pl. colores;
            #    pan, pl. panes; césped, pl. céspedes; cáliz, pl. cálices; reloj, pl. relojes.
            #    Los extranjerismos que terminen en estas consonantes deben seguir esta misma regla:
            #    píxel, pl. píxeles; máster, pl. másteres; pin, pl. pines; interfaz, pl. interfaces; sij, pl. sijes.
            #    Son excepción las palabras esdrújulas, que permanecen invariables en plural:
            #    polisíndeton, pl. (los) polisíndeton; trávelin, pl. (los) trávelin; cáterin, pl. (los) cáterin.
            #    Excepcionalmente, el plural de hipérbaton es hipérbatos.
            if forma_singular in [u'espécimen', u'régimen', u'carácter']:
                return [u'especímenes' if forma_singular == u'espécimen' else
                        u'regímenes' if forma_singular == u'régimen' else u'caracteres']
            elif forma_singular in [u'hipérbaton', u'oxímoron']:
                return [forma_singular[:-1] + u's']
            elif forma_singular in [u'cualquier', u'quienquier']:
                return [forma_singular[:-5] + u'esquier']
            elif forma_singular in [u'algún', u'algund', u'anticorrosión', u'anticorrupción', u'buen',
                                  u'cataplum', u'cataplún', u'catapum', u'catapún', u'confer', u'confíteor',
                                  u'execuátur', u'exequatur', u'fástener', u'fuer', u'híper', u'imprimátur',
                                  u'malhumor', u'mánager', u'minisúper', u'súper', u'germán', u'gram', u'gran',
                                  u'grill', u'jimén', u'man', u'merchán', u'mostén', u'ningún', u'parisién',
                                  u'paternoster', u'pedrojiménez', u'perojiménez', u'perojimén', u'pómez', u'postrer',
                                  u'postrimer', u'primer',
                                  u'quid', u'rabicán', u'recién', u'recodán', u'recodín', u'recotán', u'recotín',
                                  u'rodríguez', u'san', u'súper', u'ter', u'tercer', u'val', u'veintiún', u'vivalavirgen']:
                return [forma_singular]
            elif forma_singular in [u'mod', u'pidgin']:
                return [forma_singular + u's']
            elif forma_singular in [u'bustrófedon']:
                return [u'bustrofedones']
            elif palabra_singular.get_posicion_tonica() == -3:
                return [forma_singular]  # Invariable por esdrújula
            # La tilde (o su inexistencia) permanece invariable en algunos casos:
            # - Si la forma es esdrújula: mantiene la tilde, así que simplemente añadimos -es.
            # - Si la forma es llana y no acaba en -n, tiene tilde y la mantiene: añadimos -es.
            # - Si es aguda no acabada en -n, no tiene tilde ni la tendrá: añadimos -es.
            # Pero hay un caso, quizá dos, en los que hay cambios:
            # - Si es llana y acaba en -n (¿existen), aparece tilde: dilan-dílanes
            # - Si es aguda acabada en -n, tiene tilde y desaparece: tapón-tapones.
            # Para cubrir todos los casos a la vez, creamos la última sílaba átona (última consonante (z->c) + "es"),
            # quitamos la coda a la palabra y unimos sílabas, ajustando tildes al final
            ultima_silaba = Palabra(palabra_texto=(u'c' if forma_singular[-1] == u'z' else forma_singular[-1]) + u'es',
                                    calcula_alofonos=False, organiza_grafemas=True).get_silabas()[-1]
            ultima_silaba.set_tonica(False)
            tilde_diacritica = copy.deepcopy(palabra_singular).ajusta_tildes() != forma_singular
            if tilde_diacritica:
                return [Palabra(silabas=palabra_singular.reset_coda().get_silabas() + [ultima_silaba],
                                calcula_alofonos=False,
                                organiza_grafemas=True).set_tilde(con_tilde=True)]  # Se deja la tilde diacrítica
            else:
                return [Palabra(silabas=palabra_singular.reset_coda().get_silabas() + [ultima_silaba],
                                calcula_alofonos=False,
                                organiza_grafemas=True).ajusta_tildes()]  # Se ajusta la tilde según quede
        elif forma_singular[-2:] == u'ch':
            # i) Sustantivos y adjetivos terminados en -ch. Procedentes todos ellos de otras lenguas,
            #    o bien se mantienen invariables en plural: (los) crómlech, (los) zarévich, (los) pech,
            #    o bien hacen el plural en -es: sándwich, pl. sándwiches; maquech, pl. maqueches.
            # Como la norma es ambigua, hay problemas porque no podemos diferenciar sándwich de crómlech.
            if forma_singular in [u'capararoch', u'crómlech', u'crónlech', u'mach', u'pech', u'poch', u'zarévich']:
                return [forma_singular]
            if forma_singular in [u'sándwich', u'maquech']:
                return [forma_singular + u'es']
            print(u'Hemos decidido sin rigor alguno, que el plural de', forma_singular, u'es', forma_singular + u'es')
            return [forma_singular + u'es']
        elif ultimo_caracter in u'bcfghkmñpqtvwz':
            # h) Sustantivos y adjetivos terminados en consonantes distintas de -l, -r, -n, -d, -z, -j, -s, -x, -ch.
            #    Se trate de onomatopeyas o de voces procedentes de otras lenguas, hacen el plural en -s:
            #    crac, pl. cracs; zigzag, pl. zigzags; esnob, pl. esnobs; chip, pl. chips; mamut, pl. mamuts;
            #    cómic, pl. cómics. Se exceptúa de esta regla la palabra club, que admite dos plurales, clubs y clubes
            #    (→ club). También son excepciones el arabismo imam (→ imán), cuyo plural asentado es imames,
            #    y el latinismo álbum (→ álbum), cuyo plural asentado es álbumes.
            if forma_singular[-4:] == u'club':  # videoclub, aeroclub, cineclub...
                return [forma_singular + u's', forma_singular + u'es']
            if forma_singular in [u'imam', u'álbum', u'almotazaf', u'almutazaf', u'nolit']:
                return [forma_singular + u'es']
            if forma_singular in [u'almanac', u'bambuc', u'baurac']:
                return [forma_singular[:-1] + u'ques']
            if forma_singular in [u'abc', u'grant', u'idem', u'ídem', u'molotov', u'sant', u'summum']:
                return [forma_singular]
            if forma_singular == u'pénsum':
                return [u'pensa']
            return [forma_singular + u's']

        print(u'No sé hacer el plural de', forma_singular)

    @staticmethod
    def testea_flexionador(lemario_elegido=u'rae', testea_formas=True, testea_etiquetas=True,
                           actualiza_modelos=False, imprime_flexiones=False):
        directorio_trabajo = os.path.dirname(os.path.realpath(__file__)) + u'/archivos_de_datos/' + lemario_elegido + u'/lemario/'
        nombre_archivo_lemario = directorio_trabajo + u'lemario_' + lemario_elegido + u'.pkl.bz2'
        if not os.path.exists(nombre_archivo_lemario):
            print(u'Falta el archivo', nombre_archivo_lemario + u'. Es necesario crear el lemario.')
            return
        with bz2.BZ2File(nombre_archivo_lemario, 'rb') as entrada:
            lemario = pickle.load(entrada)

        # Reducimos el lemario a las formas del canon
        verbos_no_pronominales = {palabra: lemario[palabra] for palabra in CANON_VERBOS if palabra in lemario}
        verbos_pronominales = {palabra + u'se': lemario[palabra + u'se']
                               for palabra in CANON_VERBOS if palabra + u'se' in lemario}
        verbos = verbos_no_pronominales
        verbos.update(verbos_pronominales)
        adjetivos = {palabra: lemario[palabra] for palabra in CANON_ADJETIVOS if palabra in lemario}
        sustantivos = {palabra: lemario[palabra] for palabra in CANON_SUSTANTIVOS if palabra in lemario}
        adverbios = {palabra: lemario[palabra] for palabra in CANON_ADVERBIOS if palabra in lemario}
        pronombres = {palabra: lemario[palabra] for palabra in CANON_PRONOMBRES if palabra in lemario}
        determinantes = {palabra: lemario[palabra] for palabra in CANON_DETERMINANTES if palabra in lemario}
        conjunciones = {palabra: lemario[palabra] for palabra in CANON_CONJUNCIONES if palabra in lemario}
        if True:
            lemario = copy.deepcopy(sustantivos)
            lemario.update(adjetivos)
            lemario.update(verbos)
            lemario.update(adverbios)  # Los del Wikcionario están mejor categorizados
            lemario.update(pronombres)
            lemario.update(determinantes)
            lemario.update(conjunciones)
        elif False:
            lemario = copy.deepcopy(verbos)
            # lemario = copy.deepcopy(adjetivos)
            # lemario.update(determinantes)
        else:
            # Trapis de momento para que solo testee una parte
            lemario = {u'cuclillas': lemario[u'cuclillas']}
        # El canon_conjugado es un dict cuyas claves son los lemas que se testean, y los valores son las formas
        # flexionadas (otro dict cuyas claves son las etiquetas y los valores una lista de formas).
        canon_conjugado = {}
        for lema_txt, lema in sorted(lemario.items()):
            if lemario_elegido == u'rae':
                canon_conjugado[lema_txt] = Flexionador.flexiona_lema_rae(lema, ajusta_lema=True, incluye_cliticos=True)
            else:
                canon_conjugado[lema_txt] = Flexionador.flexiona_lema_wik(lema, ajusta_lema=True, incluye_cliticos=True)
            continue

        if actualiza_modelos:
            directorio_modelos_nuevos = directorio_trabajo.replace(u'lemario', u'modelos_nuevos')
            if not os.path.exists(directorio_modelos_nuevos):
                os.makedirs(directorio_modelos_nuevos)
            print(u'\n---------------')
            print(u'GUARDANDO ' + str(len(canon_conjugado)) + u' modelos de flexión en .../' +\
                  u'/'.join(directorio_modelos_nuevos.split(u'/')[-5:]))

            for (lema_txt, flexion_modelo) in sorted(canon_conjugado.items(), key=lambda tupla: tupla[0]):
                nombre_archivo_modelo = directorio_modelos_nuevos + lema_txt + u'.json'
                nombre_archivo_txt = nombre_archivo_modelo[:-5] + u'.txt'
                try:
                    os.remove(nombre_archivo_modelo)
                except OSError:
                    pass
                try:
                    os.remove(nombre_archivo_txt)
                except OSError:
                    pass
                with file(nombre_archivo_modelo, 'wb') as archivo_modelo:
                    ujson.dump(flexion_modelo, archivo_modelo, ensure_ascii=False, escape_forward_slashes=False)
                with codecs.open(nombre_archivo_txt, "w", encoding='utf-8') as archivo_texto:
                    archivo_texto.write(Flexionador.flexion_a_txt(flexion_modelo, lema_txt, imprime=imprime_flexiones))

        directorio_modelos_previos = directorio_trabajo.replace(u'lemario', u'modelos_conjugacion')
        if not os.path.exists(directorio_modelos_previos):
            print(u'Faltan los modelos de conjugación para poder testear. Crea los modelos antes de testear.')
            return
        print(u'\n---------------')
        print(u'TESTEANDO ' + str(len(canon_conjugado)) + u' lemas escogidos según los modelos en .../' +\
              u'/'.join(directorio_modelos_previos.split(u'/')[-5:]))
        fallos = 0
        faltas = 0
        n_formas_total = 0
        for lema_txt in sorted(canon_conjugado):
            # TODO: borra esto
            # canon_conjugado[lema_txt] = {tag[:12]: value for tag, value in canon_conjugado[lema_txt].items()}
            canon_recortado = {}
            for tag, value in canon_conjugado[lema_txt].items():
                tag = tag[:12]
                if tag not in canon_recortado:
                    canon_recortado[tag] = value
                else:
                    for forma_txt, fuentes in value.items():
                        if forma_txt not in canon_recortado[tag]:
                            canon_recortado[tag][forma_txt] = fuentes
                        else:
                            canon_recortado[tag][forma_txt] = sorted(canon_recortado[tag][forma_txt] + fuentes)
            canon_conjugado[lema_txt] = canon_recortado



            nombre_archivo_modelo = directorio_modelos_previos + lema_txt + u'.json'
            if not isfile(nombre_archivo_modelo) and canon_conjugado[lema_txt].keys() and\
                    canon_conjugado[lema_txt].keys()[0][0] == VERBO and\
                    lema_txt[-1] != u'r':
                # Como metemos los verbos reflexivos a cascoporro, puede ser que alguno no exista en su versión
                # pronominal o incluso en su versión no pronominal. Como al flexionar no hacemos distinciones,
                # en caso de no existir, testeamos con la versión pronominal/no pronominal que sí que exista.
                # La forma no pronominal siempre aparece en los modelos.
                nombre_archivo_modelo = directorio_modelos_previos + lema_txt[:-2] + u'.json'
            if not os.path.exists(nombre_archivo_modelo):
                print(u'ERROR. ' + lema_txt + u' Falta el archivo modelo .../' +\
                    u'/'.join(nombre_archivo_modelo.split(u'/')[-5:]))
                faltas += 1
                continue
            with file(nombre_archivo_modelo, 'rb') as archivo_modelo:
                conjugacion_modelo = ujson.load(archivo_modelo)
                # TODO: borra esto
                # conjugacion_modelo = {tag[:12]: value for tag, value in conjugacion_modelo.items()}
                conjugacion_recortada = {}
                for tag, value in conjugacion_modelo.items():
                    tag = tag[:12]
                    if tag not in conjugacion_recortada:
                        conjugacion_recortada[tag] = value
                    else:
                        for forma_txt, fuentes in value.items():
                            if forma_txt not in conjugacion_recortada[tag]:
                                conjugacion_recortada[tag][forma_txt] = fuentes
                            else:
                                conjugacion_recortada[tag][forma_txt] = sorted(conjugacion_recortada[tag][forma_txt] + fuentes)
                conjugacion_modelo = conjugacion_recortada




            formas_totales_modelo = sorted([(forma, tag)
                                            for tag, formas in conjugacion_modelo.items()
                                            for forma, fuentes in formas.items()],
                                           key=lambda tupla: tupla[1])
            formas_distintas_modelo = set([forma for forma, tag in formas_totales_modelo])
            formas_totales_canon = sorted([(forma, tag)
                                           for tag, formas in canon_conjugado[lema_txt].items()
                                           for forma, fuentes in formas.items()],
                                          key=lambda tupla: tupla[1])
            formas_distintas_canon = set([forma for forma, tag in formas_totales_canon])
            n_formas_total += len(formas_totales_modelo)
            texto_error = u'ERROR. ' + lema_txt + u' (Antes: ' + str(len(formas_totales_modelo)) + u' formas, ' +\
                str(len(formas_distintas_modelo)) + u' distintas, ' + str(len(conjugacion_modelo.keys())) +\
                u' etiquetas; Ahora: ' + str(len(formas_totales_canon)) + u' formas, ' +\
                str(len(formas_distintas_canon)) + u' distintas, ' + str(len(canon_conjugado[lema_txt].keys())) +\
                u' etiquetas)'
            fallo = False
            if testea_formas and testea_etiquetas:
                for etiqueta, formas in sorted(canon_conjugado[lema_txt].items(), key=lambda tupla: tupla[0]):
                    for forma_txt, fuentes in formas.items():
                        if etiqueta not in conjugacion_modelo or forma_txt not in conjugacion_modelo[etiqueta]:
                            if not fallo:
                                print(texto_error, end=u' ')
                            print(u'\n\tforma extra', etiqueta, forma_txt, u'(' + u'), ('.join(fuentes) + u')', end=u' ')
                            fallo = True
                for etiqueta, formas in conjugacion_modelo.items():
                    for forma_txt, fuentes in formas.items():
                        if etiqueta not in canon_conjugado[lema_txt] or\
                                forma_txt not in canon_conjugado[lema_txt][etiqueta]:
                            if not fallo:
                                print(texto_error, end=u' ')
                            print(u'\n\tforma que falta', etiqueta, forma_txt, u'(' + u'), ('.join(fuentes) + u')', end=u' ')
                            fallo = True
            elif testea_formas and not testea_etiquetas:
                if len(formas_totales_modelo) != len(formas_totales_canon) or\
                        len(formas_distintas_modelo) != len(formas_distintas_canon):
                    if not fallo:
                        print(texto_error, end=u' ')
                    print(u'fallo en número de formas. Antes:', len(formas_totales_modelo), u'-', len(formas_distintas_modelo),
                        u', Ahora:', len(formas_totales_canon), u'-', len(formas_distintas_canon), end=u' ')
                    fallo = True
                for forma_canon, tag_canon in formas_totales_canon:
                    if forma_canon not in formas_distintas_modelo:
                        if not fallo:
                            print(texto_error, end=u' ')
                        print(u'\n\tforma que falta', tag_canon, forma_canon, u'(' +\
                            u'), ('.join(canon_conjugado[lema_txt][tag_canon][forma_canon]) + u')', end=u' ')
                        fallo = True
                for forma_modelo, tag_modelo in formas_totales_modelo:
                    if forma_modelo not in formas_distintas_canon:
                        if not fallo:
                            print(texto_error, end=u' ')
                        print(u'\n\tforma extra', tag_modelo, forma_modelo, u'(' +\
                            u'), ('.join(conjugacion_modelo[tag_modelo][forma_modelo]) + u')', end=u' ')
                        fallo = True
            elif not testea_formas and testea_etiquetas:
                if len(conjugacion_modelo) != len(canon_conjugado[lema_txt]):
                    if not fallo:
                        print(texto_error, end=u' ')
                    print(u'fallo en número de etiquetas. Modelo:', len(conjugacion_modelo),
                        u', Test:', len(canon_conjugado[lema_txt]), end=u' ')
                    fallo = True
                for tag_canon, formas_canon in canon_conjugado[lema_txt].items():
                    if tag_canon not in conjugacion_modelo:
                        if not fallo:
                            print(texto_error, end=u' ')
                        print(u'\n\tetiqueta que falta', tag_canon, u'(' + u'), ('.join(formas_canon.keys()) + u')', end=u' ')
                        fallo = True
                for tag_modelo, formas_modelo in conjugacion_modelo.items():
                    if tag_modelo not in canon_conjugado[lema_txt]:
                        if not fallo:
                            print(texto_error, end=u' ')
                        print(u'\n\tetiqueta_extra', tag_modelo, u'(' + u'), ('.join(formas_modelo.keys()) + u')', end=u' ')
                        fallo = True

            if not fallo:
                print(u'OK. ' + lema_txt + u' (' + str(len(formas_totales_modelo)) + u' formas, ' +\
                    str(len(formas_distintas_modelo)) + u' distintas, ' + str(len(conjugacion_modelo.keys())) +\
                    u' etiquetas)' + (u' <-- ESTO TIENE QUE CAMBIAR' if len(formas_totales_modelo) == 0 else u''))
            else:
                print(u'')
                fallos += 1
        print(u'\nRESUMEN DEL TESTEO DE', len(canon_conjugado), u'LEMAS.\n\t-', fallos, u'lemas fallidos.\n\t-',
            faltas, u'lemas sin modelo.\n\t-', len(canon_conjugado) - fallos - faltas, u'lemas correctos.\n')
        if fallos + faltas == 0:
            print(u'TODO CORRECTO. Impresionante. Y eso que eran', n_formas_total, u'formas distintas.')
        else:
            print(fallos + faltas, u'FALLOS. CORRÍGELOS. MADAFAKA.')
            beep(200, 300)
            beep(200, 300)
            beep(200, 500)
            beep(150, 1000)


if __name__ == '__main__':
    # print(u', '.join(Flexionador.pluraliza(u'que')))
    # Flexionador.crea_diminutivo(u'buz')
    Flexionador.testea_flexionador(lemario_elegido=u'rae', testea_formas=True, testea_etiquetas=True,
                                   actualiza_modelos=False, imprime_flexiones=False)

