#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""
"""

from __future__ import print_function
from iar_inflector.acep_consts import FORMA, VERBO, SUSTANTIVO, ADJETIVO, ADVERBIO, PRONOMBRE, PREPOSICION,\
    CONTRAIDA, ABREVIATURA,\
    INTERJECCION, EXPRESION,\
    DETERMINADO, INDETERMINADO, ARTICULO_D, ARTICULO_I, ONOMATOPEYA,\
    FEMENINO, MASCULINO, AMBIGUO, SINGULAR, PLURAL,\
    SIGLA, SUFIJO, FLEXIVO, INTERROGATIVO, PERSONAL, RELATIVO, RELATIVO_POSESIVO, EXCLAMATIVO,\
    CARDINAL, DE_PADECIMIENTO, DE_SUSTANTIVO, DE_VERBO, INDEFINIDO, DEMOSTRATIVO, ORDINAL, POSESIVO,\
    CALIFICATIVO, COMPARATIVO, SUPERLATIVO,\
    GENTILICIO, SUSTANTIVADO, PARTICIPIO, AFIRMATIVO, CUANTITATIVO, DUBITATIVO, PRINCIPAL, NEGATIVO,\
    TEMPORAL, DISTRIBUTIVO,\
    LOCATIVO, GERUNDIO, INFINITIVO, PREFIJO, NEUTRO, DE_ADJETIVO, COLECTIVO, COMPUESTO, PROPIO,\
    SIMBOLO, ATONO, DESCONOCIDA, DIMINUTIVO, AUMENTATIVO, DETERMINANTE,\
    CONJUNCION, COPULATIVA, DISYUNTIVA, DISTRIBUTIVA, ADVERSATIVA,\
    CAUSAL, FINAL, CONCESIVA, ILATIVA,\
    ELEMENTO_COMPOSITIVO, SIGNO

from iar_transcriber.palabra import Palabra
from iar_transcriber.fon_consts import ANTE, MEDI, POST
from iar_inflector.flex_consts import NEXOS_AOU, NEXOS_IE, CARDINALES, ORDINALES
from iar_inflector.parseador_rae_consts import REGEXP_AMBITOS, REGEXP_PAISES, REGEXP_REGIONES, \
    REGEXP_MEDIDAS, REGEXP_CATEGORIAS, REGEXP_VARIOS

import re
import copy

__author__ = "Iván Arias Rodríguez"
__copyright__ = "Copyright 2017, Iván Arias Rodríguez"
__credits__ = [""]
__license__ = "GPL"  # No estoy seguro
__version__ = "1.0.1"
__maintainer__ = "Iván Arias Rodríguez"
__email__ = "ivan.arias.rodriguez@gmail.com"
__status__ = "Development"  # "Prototype", "Production"


class Acepcion:
    u"""

    """

    def __init__(self, acepcion_dict, origen, n_entrada, n_acepcion, verboso=True):
        self._n_entrada = n_entrada
        self._n_acepcion = n_acepcion
        self._origen = origen
        # Como cada tipo de acepción puede tener datos distintos, se meten en un diccionario según
        # se vayan encontrando y se manejan siempre con las funciones de este método y no directamente
        self._datos = {}

    def get_n_entrada(self):
        return self._n_entrada

    def set_n_entrada(self, n_entrada):
        self._n_entrada = n_entrada

    def get_n_acepcion(self):
        return self._n_acepcion

    def set_n_acepcion(self, n_acepcion):
        self._n_acepcion = n_acepcion

    def get_origen(self):
        return self._origen

    def set_origen(self, origen):
        self._origen = origen

    def get_datos(self):
        return self._datos

    def set_datos(self, datos):
        self._datos = datos

    def get_categoria(self):
        return self._datos["categoria"] if "categoria" in self._datos else ""

    def set_categoria(self, categoria, verboso=True):
        if isinstance(self, AcepcionRae) or "categoria" not in self._datos or self._datos["categoria"] == categoria:
            self._datos["categoria"] = categoria
        # TODO: esto es un apaño, pero realmente sólo hay 6-7 palabras a las que les ocurre esto
        elif self._datos["categoria"] == FORMA or categoria == ADJETIVO and self._datos["categoria"] == SUSTANTIVO:
            # Teníamos categoría de forma conjugada, y entra algo, o éramos sustantivo y entra adjetivo (más flexión)
            self._datos["categoria"] = categoria
        elif verboso and categoria != FORMA:
            print(self._lema_rae_txt, u'tiene dos categorías: primero', self._datos["categoria"], u', segundo', categoria)

    def get_conjs(self):
        return self._datos["conjs"] if "conjs" in self._datos else []

    def set_conjs(self, conjs):
        self._datos["conjs"] = conjs

    def append_conj(self, etiqueta_conj):
        if "conjs" not in self._datos:
            self._datos["conjs"] = [etiqueta_conj]
        elif etiqueta_conj not in self._datos["conjs"]:
            self._datos["conjs"].append(etiqueta_conj)

    def get_tipos(self):
        return self._datos["tipos"] if "tipos" in self._datos else []

    def append_tipo(self, tipo):
        if "tipos" not in self._datos:
            self._datos["tipos"] = [tipo]
        elif tipo not in self._datos["tipos"]:
            self._datos["tipos"].append(tipo)

    def set_tipos(self, tipos):
        self._datos["tipos"] = tipos

    def get_numero(self):
        return self._datos["numero"] if "numero" in self._datos else SINGULAR

    def set_numero(self, numero):
        self._datos["numero"] = numero

    def set_numeros_disponibles(self, numeros_disponibles):
        self._datos["numeros_disponibles"] = numeros_disponibles

    def get_numeros_disponibles(self):
        return self._datos["numeros_disponibles"] if "numeros_disponibles" in self._datos else []

    def append_numero_disponible(self, numero_disponible):
        # En la RAE hay un tratamiento de los números distinto. Se añaden los códigos de los números que tiene
        # el lema. Más adelante, según este valor y el lema RAE, se extraerán las formas según los números.
        self._datos.setdefault("numeros_disponibles", []).append(numero_disponible)

    def get_persona(self):
        return self._datos["persona"] if "persona" in self._datos else "0"

    def set_persona(self, persona):
        self._datos["persona"] = persona

    def get_genero(self):
        return self._datos["genero"] if "genero" in self._datos else ""

    def set_genero(self, genero):
        # El género (para nombres) puede ser masculino (el coche/los coches), femenino (la bola/las bolas),
        # ambiguo (el mar/la mar/los mares/las mares) o neutro (algún pronombre).
        # Básicamente género ambiguo significa masculino y femenino, y género neutro significa ni masculino ni femenino
        if "genero" not in self._datos or genero == AMBIGUO:
            # No teníamos género asignado o entra un género ambiguo que machaca lo que hubiera (tiene máxima inflexión)
            self._datos["genero"] = genero
        elif self._datos["genero"] not in [AMBIGUO, genero] and genero != NEUTRO:
            # Ya teníamos un género asignado, que no era ambiguo ni neutro (es decir, era masculino o femenino), y
            # entra algo que es distinto de lo que había (y no es ambiguo ni neutro). Es decir, teníamos masculino y
            # entra femenino, o teníamos femenino y entra masculino. Nos hemos convertido en ambiguo.
            self._datos["genero"] = AMBIGUO
        else:
            # El género que entra es neutro y ya teníamos algo (así que nada que hacer), o bien es del mismo tipo
            # del que ya teníamos (lo dejamos igual, nada que hacer).
            pass

    def set_generos_disponibles(self, generos_disponibles):
        self._datos["generos_disponibles"] = generos_disponibles

    def get_generos_disponibles(self):
        return self._datos["generos_disponibles"] if "generos_disponibles" in self._datos else []

    def append_genero_disponible(self, genero_disponible):
        # En la RAE hay un tratamiento de los géneros distinto. Se añaden los códigos de los géneros que tiene
        # el lema. Más adelante, según este valor y el lema RAE, se extraerán las formas según los géneros.
        self._datos.setdefault("generos_disponibles", []).append(genero_disponible)

    def remove_genero_disponible(self, genero_disponible):
        if genero_disponible in self._datos["generos_disponibles"]:
            self._datos["generos_disponibles"].remove(genero_disponible)

    def get_es_antroponimo(self):
        return self._datos["es_antroponimo"] if "es_antroponimo" in self._datos else False

    def set_es_antroponimo(self, es_antroponimo):
        self._datos["es_antroponimo"] = es_antroponimo

    def get_es_toponimo(self):
        return self._datos["es_toponimo"] if "es_toponimo" in self._datos else False

    def set_es_toponimo(self, es_toponimo):
        self._datos["es_toponimo"] = es_toponimo

    def get_es_auxiliar(self):
        return self._datos["es_auxiliar"] if "es_auxiliar" in self._datos else False

    def set_es_auxiliar(self, es_auxiliar):
        self._datos["es_auxiliar"] = es_auxiliar

    def get_es_impersonal(self):
        return self._datos["es_impersonal"] if "es_impersonal" in self._datos else False

    def set_es_impersonal(self, es_impersonal):
        self._datos["es_impersonal"] = es_impersonal

    def get_es_copulativo(self):
        return self._datos["es_copulativo"] if "es_copulativo" in self._datos else False

    def set_es_copulativo(self, es_copulativo):
        self._datos["es_copulativo"] = es_copulativo

    def get_es_desusado(self):
        return self._datos["es_desusado"] if "es_desusado" in self._datos else False

    def set_es_desusado(self, es_desusado):
        self._datos["es_desusado"] = es_desusado

    def get_es_poco_usado(self):
        return self._datos["es_poco_usado"] if "es_poco_usado" in self._datos else False

    def set_es_poco_usado(self, es_poco_usado):
        self._datos["es_poco_usado"] = es_poco_usado

    def get_es_transitivo(self):
        return self._datos["es_transitivo"] if "es_transitivo" in self._datos else False

    def set_es_transitivo(self, es_transitivo):
        self._datos["es_transitivo"] = es_transitivo

    def get_es_intransitivo(self):
        return self._datos["es_intransitivo"] if "es_intransitivo" in self._datos else False

    def set_es_intransitivo(self, es_intransitivo):
        self._datos["es_intransitivo"] = es_intransitivo

    def get_es_pronominal(self):
        return self._datos["es_pronominal"] if "es_pronominal" in self._datos else False

    def set_es_pronominal(self, es_pronominal):
        self._datos["es_pronominal"] = es_pronominal

    def get_es_defectivo(self):
        return self._datos["es_defectivo"] if "es_defectivo" in self._datos else False

    def set_es_defectivo(self, es_defectivo):
        self._datos["es_defectivo"] = es_defectivo

    def get_es_reflexivo(self):
        return self._datos["es_reflexivo"] if "es_reflexivo" in self._datos else False

    def set_es_reflexivo(self, es_reflexivo):
        self._datos["es_reflexivo"] = es_reflexivo

    def get_lema_base(self):
        return self._datos["lema_base"] if "lema_base" in self._datos else u''

    def set_lema_base(self, lema_base):
        self._datos["lema_base"] = lema_base

    def get_es_latina(self):
        return self._datos["es_latina"] if "es_latina" in self._datos else False

    def set_es_latina(self, es_latina):
        self._datos["es_latina"] = es_latina

    def get_grado(self):
        return self._datos["grado"] if "grado" in self._datos else "0"

    def set_grado(self, grado):
        self._datos["grado"] = grado

    def get_es_impropia(self):
        return self._datos["es_impropia"] if "es_impropia" in self._datos else False

    def set_es_impropia(self, es_impropia):
        self._datos["es_impropia"] = es_impropia

    def get_es_enclitico(self):
        return self._datos["es_enclitico"] if "es_enclitico" in self._datos else None

    def set_es_enclitico(self, es_enclitico):
        self._datos["es_enclitico"] = es_enclitico

    def get_de_participio(self):
        return self._datos["de_participio"] if "de_participio" in self._datos else "0"

    def set_de_participio(self, de_participio):
        self._datos["de_participio"] = de_participio

    def get_apocope_txt(self):
        return self._datos["apocope_txt"] if "apocope_txt" in self._datos else u''

    def set_apocope_txt(self, apocope_txt):
        self._datos["apocope_txt"] = apocope_txt

    def reset_apocope_txt(self):
        del self._datos["apocope_txt"]

    def get_apocope_plural_txt(self):
        return self._datos["apocope_plural_txt"] if "apocope_plural_txt" in self._datos else u''

    def set_apocope_plural_txt(self, apocope_plural_txt):
        self._datos["apocope_plural_txt"] = apocope_plural_txt

    def reset_apocope_plural_txt(self):
        del self._datos["apocope_plural_txt"]

    def get_neutro_txt(self):
        return self._datos["neutro_txt"] if "neutro_txt" in self._datos else u''

    def set_neutro_txt(self, neutro_txt):
        self._datos["neutro_txt"] = neutro_txt

    def get_comparativo_txt(self):
        return self._datos["comparativo_txt"] if "comparativo_txt" in self._datos else u''

    def set_comparativo_txt(self, comparativo_txt):
        self._datos["comparativo_txt"] = comparativo_txt

    def get_formas_plural(self):
        return self._datos["formas_plural"] if "formas_plural" in self._datos else []

    def set_formas_plural(self, formas_plural):
        self._datos["formas_plural"] = formas_plural

    def get_masculino_ambiguo(self):
        return self._datos["masculino_ambiguo"] if "masculino_ambiguo" in self._datos else False

    def set_masculino_ambiguo(self, masculino_ambiguo):
        self._datos["masculino_ambiguo"] = masculino_ambiguo

    def get_tambien_superlativo_regular(self):
        return self._datos["tambien_superlativo_regular"] if "tambien_superlativo_regular" in self._datos else False

    def set_tambien_superlativo_regular(self, tambien_superlativo_regular):
        self._datos["tambien_superlativo_regular"] = tambien_superlativo_regular

    def get_superlativos_txt(self):
        return self._datos["superlativos_txt"] if "superlativos_txt" in self._datos else []

    def set_superlativos_txt(self, superlativos_txt):
        self._datos["superlativos_txt"] = superlativos_txt

    def get_aumentativos(self):
        return self._datos.setdefault("aumentativos", [])

    def set_aumentativos(self, aumentativos):
        self._datos["aumentativos"] = aumentativos

    def get_diminutivos(self):
        return self._datos.setdefault("diminutivos", [])

    def set_diminutivos(self, diminutivos):
        self._datos["diminutivos"] = diminutivos

    def get_formas_atonas_txt(self):
        return self._datos["formas_atonas_txt"] if "formas_atonas_txt" in self._datos else []

    def set_formas_atonas_txt(self, formas_atonas_txt):
        self._datos["formas_atonas_txt"] = formas_atonas_txt

    def get_forma_tonica_txt(self):
        return self._datos["forma_tonica_txt"] if "forma_tonica_txt" in self._datos else u''

    def set_forma_tonica_txt(self, forma_tonica_txt):
        self._datos["forma_tonica_txt"] = forma_tonica_txt

    def get_forma_amalgamada_txt(self):
        return self._datos["forma_amalgamada_txt"] if "forma_amalgamada_txt" in self._datos else u''

    def set_forma_amalgamada_txt(self, forma_amalgamada_txt):
        self._datos["forma_amalgamada_txt"] = forma_amalgamada_txt

    def get_es_locucion(self):
        return self._datos["es_locucion"] if "es_locucion" in self._datos else False

    def set_es_locucion(self, es_locucion):
        self._datos["es_locucion"] = es_locucion

    # def get_es_contraccion(self):
    #     return self._datos["es_contraccion"] if "es_contraccion" in self._datos else False

    # def set_es_contraccion(self, es_contraccion):
    #     self._datos["es_contraccion"] = es_contraccion

    def get_palabras_contraidas(self):
        return self._datos["palabras_contraidas"] if "palabras_contraidas" in self._datos else []

    def set_palabras_contraidas(self, palabras_contraidas):
        self._datos["palabras_contraidas"] = palabras_contraidas

    def get_es_apocope(self):
        return self._datos["es_apocope"] if "es_apocope" in self._datos else False

    def set_es_apocope(self, es_apocope):
        self._datos["es_apocope"] = es_apocope

    def get_es_forma_atona(self):
        return self._datos["es_forma_atona"] if "es_forma_atona" in self._datos else False

    def set_es_forma_atona(self, es_forma_atona):
        self._datos["es_forma_atona"] = es_forma_atona

    def get_es_forma_tonica(self):
        return self._datos["es_forma_tonica"] if "es_forma_tonica" in self._datos else False

    def set_es_forma_tonica(self, es_forma_tonica):
        self._datos["es_forma_tonica"] = es_forma_tonica

    def get_es_superlativo(self):
        return self._datos["es_superlativo"] if "es_superlativo" in self._datos else False

    def set_es_superlativo(self, es_superlativo):
        self._datos["es_superlativo"] = es_superlativo

    def get_es_pronombre_amalgamado(self):
        return self._datos["es_pronombre_amalgamado"] if "es_pronombre_amalgamado" in self._datos else False

    def set_es_pronombre_amalgamado(self, es_pronombre_amalgamado):
        self._datos["es_pronombre_amalgamado"] = es_pronombre_amalgamado

    def get_es_comparativo(self):
        return self._datos["es_comparativo"] if "es_comparativo" in self._datos else False

    def set_es_comparativo(self, es_comparativo):
        self._datos["es_comparativo"] = es_comparativo

    """
    def reset_info_uso(self):
        self._datos.pop("info_uso", None)

    def set_info_uso(self, clave, valor):
        if "info_uso" not in self._datos:
            self._datos["info_uso"] = {}
        if False and clave in self._datos["info_uso"]:
            print(u'¿Es esto un problema? Hay más de un', clave, u'en info_uso de', self._lema_rae_txt, u'.',\
                u'Teníamos', self._datos["info_uso"], u'. Ahora entra:', valor)
        self._datos["info_uso"][clave] = valor

    def get_info_uso(self, clave):
        if "info_uso" in self._datos and clave in self._datos["info_uso"]:
            return self._datos["info_uso"][clave]
        # elif clave == "categoria_alternativa":
        #     return self.get_categoria()
        return None
    """


class AcepcionWik(Acepcion):
    def __init__(self, acepcion_wik, origen, n_entrada, n_acepcion, verboso=True):
        Acepcion.__init__(self, acepcion_wik, origen, n_entrada, n_acepcion, verboso)
        self._lema_txt = acepcion_wik["lema"]
        # Vamos a procesar la etiqueta de categoría y todas las informaciones de forma similar
        etiquetas_de_acepcion = [acepcion_wik["cat"]] + acepcion_wik["infos"]
        for etiqueta_completa in etiquetas_de_acepcion:
            # Para homegeneizar, quitamos los prefijos raros de las etiquetas de conjungación.
            etiqueta_completa = etiqueta_completa.replace(u'W.es.v.', u'v.'). \
                replace(u'w.es.v.', u'v.').replace(u'es.v.', u'v.')
            # Dentro de la etiqueta tenemos la propia etiqueta en sí, seguida de parámetros, separados por |,
            # del estilo de {{inflect.es.sust.ad-lib|formasingular|formaplural|link=s}} o {{enclítico|dejar|me}}
            # Los pronombres son un poco un infierno, porque es común ver etiquetas que usan la plantilla de pronombre:
            # === {{pronombre|es|demostrativo}} ===. En el procesado previo hemos quitado el |es, pero se nos quedan
            # cosas como |demostrativo como si fueran parámetros, así que eliminamos los |. Además, se marcan de forma
            # errónea como pronombres posesivos lo que deberían ser adjetivos posesivos.
            if re.match(u'pronombre', etiqueta_completa, re.IGNORECASE):
                etiqueta = etiqueta_completa.replace(u'|', u' ').strip()
                if re.match(u'pronombre posesivo', etiqueta, re.IGNORECASE):
                    # En realidad, los posesivos son adjetivos, no pronombres.
                    etiqueta = u'adjetivo' + etiqueta[9:]
                parametros = []
            else:
                etiqueta = etiqueta_completa.split(u'|')[0].strip()
                parametros = [parametro.strip() for parametro in etiqueta_completa.split(u'|')[1:]]
            # Usualmente los parámetros tienen un orden, lo que les da su significado. Pero se puede indicar
            # el orden del parámetro de la forma {{inflect.es.sust.í|2=s}}.
            # Se suele usar cuando los otros parámetros tienen sus valores por defecto.
            parametros_sin_igual = [parametro for parametro in parametros if u'=' not in parametro]
            # Vamos a procesar las etiquetas según el texto que haya al inicio.
            if re.match(u'f\.', etiqueta) or re.match(u'forma', etiqueta, re.IGNORECASE):
                # Tenemos una etiqueta de una forma flexionada
                # Puede ser f.v (forma verbal), f.s.p (forma sustantivo plural), y muchas otras
                # f.s.p: https://es.wiktionary.org/wiki/Plantilla:forma_sustantivo_plural
                # f.adj2: https://es.wiktionary.org/wiki/Plantilla:forma_adjetivo_2
                #  f.adj2|perecosísimo|pl|grado=sup|adj=perecoso
                # f.v: https://es.wiktionary.org/wiki/Plantilla:forma_verbo
                # TODO: De aquí se podrían extraer formas verbales irregulares, aunque las importantes,
                # como participios (irregulares) vienen etiquetados aparte.
                self.set_categoria(FORMA)  # TODO: Quizá podríamos especificar el tipo
                if parametros_sin_igual:
                    self.set_lema_base(parametros_sin_igual[0])
                # TODO: las formas interesantes son quizá el participio y el gerundio, pero aparecen en sus
                # respectivos verbos.
                continue
            elif re.match(u'locución', etiqueta, re.IGNORECASE):
                # Es una locución. Puede ser de muchos tipos. Si es una locución latina lo anotamos aparte, pero
                # si no, lo procesamos como si fuera una única palabra (es decir, una locución adjetiva se trata
                # como un adjetivo). Transformamos la propia etiqueta para que se procese como si hubiera llegado
                # así.
                self.set_es_locucion(True)
                if etiqueta == u'locución':  # Si hay algo más
                    continue
                elif u'latina' in etiqueta:
                    self.set_es_latina(True)
                    continue
                # Si no es solo locución (lo que sería un error) y no es latina, modificamos la etiqueta para
                # tratarlo como si solo fuera una palabra y no una locución
                etiqueta = etiqueta.replace(u'adjetiva', u'adjetivo').replace(u'adverbial', u'adverbio'). \
                    replace(u'conjuntiva', u'conjunción').replace(u'interjectiva', u'interjección'). \
                    replace(u'preposicional', u'preposición').replace(u'sustantiva', u'sustantivo'). \
                    replace(u'verbal', u'verbo').replace(u'interrogativa', u'interrogativo'). \
                    replace(u'modal', u'de modo').replace(u'temporal', u'de tiempo'). \
                    replace(u'masculina', u'masculino').replace(u'masclunino', u'masculino'). \
                    replace(u'femenina', u'femenino').replace(u'propia', u'propio'). \
                    replace(u'transitiva', u'transitivo')
                etiqueta = etiqueta.replace(u'locución', u'').strip()

            # Nos quedamos con la palabra clave, que es la primera palabra que define qué etiqueta es.
            # Si es una etiqueta de categoría, se marcará, y si es de información anexa, también
            keyword = etiqueta.split(u'|')[0].strip().split(u'#')[0].strip().split()[0].strip().lower()
            if re.match(u'v\.conj', etiqueta):
                if self._lema_txt in [u'ir', u'irse']:
                    # TODO: esto es bastante horroroso. Pero es que para el verbo "irse" se utiliza la plantilla
                    # es.v.conj, que demasiado genérica. Esta plantilla es como una plantilla "raw" con un listado
                    # de formas en orden y no tiene etiquetas de tiempos como otras. Mucho lío para parsearlo.
                    # Así que lo mejor es imponer la etiqueta correcta y no hacer procesados específicos.
                    etiqueta_completa = u'v.conj.ir|'
                    etiqueta_completa += u'|irregular=sí' + \
                                         (u'|pronominal=s' if self._lema_txt[-2:] == u'se' else u'') + \
                                         u'|ger=yendo' \
                                         u'|i.p.1s=voy|i.p.2s=vas|i.p.2s2=vas|i.p.3s=va' \
                                         u'|i.p.1p=vamos|i.p.2p=vais|i.p.3p=van' \
                                         u'|i.pi.1s=iba|i.pi.2s=ibas|i.pi.3s=iba' \
                                         u'|i.pi.1p=íbamos|i.pi.2p=ibais|i.pi.3p=iban' \
                                         u'|i.pp.1s=fui|i.pp.2s=fuiste|i.pp.3s=fue' \
                                         u'|i.pp.1p=fuimos|i.pp.2p=fuisteis|i.pp.3p=fueron' \
                                         u'|s.p.1s=vaya|s.p.2s=vayas|s.p.2s2=vayás|s.p.3s=vaya' \
                                         u'|s.p.1p=vayamos|s.p.2p=vayáis|s.p.3p=vayan' \
                                         u'|s.pi.1s=fuera|s.pi.2s=fueras|s.pi.3s=fuera' \
                                         u'|s.pi.1p=fuéramos|s.pi.2p=fuerais|s.pi.3p=fueran' \
                                         u'|s.pi2.1s=fuese|s.pi2.2s=fueses|s.pi2.3s=fuese' \
                                         u'|s.pi2.1p=fuésemos|s.pi2.2p=fueseis|s.pi2.3p=fuesen' \
                                         u'|s.f.1s=fuere|s.f.2s=fueres|s.f.3s=fuere' \
                                         u'|s.f.1p=fuéremos|s.f.2p=fuereis|s.f.3p=fueren' \
                                         u'|im.2s=ve|im.2s2=andá'
                    etiqueta_completa += u'|gerpron=yéndose|imppron2s=vete|imppron2s2=andate|imppron3s=váyase' \
                                         u'|imppron1p=vámonos o vayámonos|imppron2p=idos|imppron3p=váyanse'
                self.append_conj(etiqueta_completa.replace(u'\n', u''))  # Con los parámetros
            elif re.match(u'inflect\.', etiqueta):
                self.append_inflect(etiqueta_completa)  # Con los parámetros
            elif keyword == u'abreviatura':  # {{abreviatura|es}}
                self.set_categoria(ABREVIATURA)
            elif keyword == u'adjetivo':  # {{adjetivo...}}
                # Es un adjetivo (quizá locución adjetival). Veremos de qué tipo.
                self.set_categoria(ADJETIVO)
                if etiqueta != u'adjetivo':  # Si pone algo más que "adjetivo"
                    if u'cardinal' in etiqueta:  # {{adjetivo cardinal|es}}
                        self.append_tipo(CARDINAL)
                    elif u'de padecimiento' in etiqueta:  # {{adjetivo de padecimiento|carcoma|consunción}}
                        self.append_tipo(DE_PADECIMIENTO)
                    elif u'de sustantivo' in etiqueta.replace(u'_', u' '):
                        # {{adjetivo de sustantivo|[[nihilismo]]|al}}
                        self.append_tipo(DE_SUSTANTIVO)
                    elif u'de verbo' in etiqueta:  # {{adjetivo de verbo|abstraer|abstrae}}
                        self.append_tipo(DE_VERBO)
                    elif u'demostrativo' in etiqueta:
                        self.append_tipo(DEMOSTRATIVO)
                    elif u'ordinal' in etiqueta:
                        self.append_tipo(ORDINAL)
                    elif u'posesivo' in etiqueta:
                        # Algunas formas de adjetivos posesivos aparecen como pronombres posesivos pero se
                        # modifican para que se traten aquí.
                        self.append_tipo(POSESIVO)
                    elif u'indefinido' in etiqueta:
                        self.append_tipo(INDEFINIDO)
                    elif u'calificativo' in etiqueta:
                        self.append_tipo(CALIFICATIVO)
                    elif u'gentilicio' in etiqueta:
                        self.append_tipo(GENTILICIO)
                    elif u'invariable' in etiqueta:
                        # A veces aparece como información en el encabezado, === {{adjetivo|es}} invariable ===
                        # y entonces suelen echar en falta una etiqueta de inflexión. La creamos.
                        self.append_inflect(u'inflect.es.adj.invariante')  # No tiene parámetros
                    elif u'superlativo' in etiqueta:  # === {{adjetivo|es}} superlativo ===
                        self.set_grado(SUPERLATIVO)
                    elif u'sustantivado' in etiqueta:
                        self.append_tipo(SUSTANTIVADO)
                    elif u'participio' in etiqueta:
                        # Suele aparecer como === {{adjetivo|es}} y participio ===. En realidad, que derive de un
                        # participio no nos aporta información relevante, ya que el lema del verbo lo contendrá.
                        # La única información perdida es la de saber que este adjetivo proviene de un participio,
                        # pero eso se puede comprobar directamente en el lexicón, si existen más formas iguales
                        # con etiqueta de participio. Pero se añade esta información
                        self.set_de_participio(PARTICIPIO)
                    elif verboso:
                        print(u'La etiqueta {{' + etiqueta + u'}} no se procesa bien. Lema:', self._lema_txt)

            elif keyword == u'adverbio':
                self.set_categoria(ADVERBIO)
                if etiqueta != u'adverbio':  # Si pone algo más que "adverbio"
                    if u'de afirmación' in etiqueta:
                        self.append_tipo(AFIRMATIVO)
                    elif u'de cantidad' in etiqueta.replace(u'_', u''):
                        self.append_tipo(CUANTITATIVO)
                    elif u'de duda' in etiqueta:
                        self.append_tipo(DUBITATIVO)
                    elif u'de modo' in etiqueta:
                        self.append_tipo(PRINCIPAL)
                    elif u'de negación' in etiqueta:
                        self.append_tipo(NEGATIVO)
                    elif u'de orden' in etiqueta:
                        self.append_tipo(ORDINAL)
                    elif u'de tiempo' in etiqueta:
                        self.append_tipo(TEMPORAL)
                    elif u'interrogativo' in etiqueta:
                        self.append_tipo(INTERROGATIVO)
                    elif u'relativo' in etiqueta:
                        self.append_tipo(RELATIVO)

                    if u'comparativo' in etiqueta:  # Puede ser relativo y comparativo, o sólo comparativo
                        self.append_tipo(COMPARATIVO)
                    elif u'lugar' in etiqueta or u'locativo' in etiqueta:  # Puede ser de tiempo y lugar
                        self.append_tipo(LOCATIVO)
                    if not self.get_tipos() and verboso:  # No hemos encontrado el tipo, y había algo más
                        print(u'La etiqueta {{' + etiqueta + u'}} no se procesa bien. Lema:', self._lema_txt)
            elif keyword in [u'antropónimo', u'apellido']:
                self.set_categoria(SUSTANTIVO)
                self.set_es_antroponimo(True)
                if keyword == u'antropónimo':
                    # Metemos además el género
                    self.set_genero(MASCULINO if u'masculino' in etiqueta else FEMENINO)
            elif keyword in [u'ciudades', u'regiones', u'países', u'islas', u'lagos', u'mares',
                             u'penínsulas', u'planetas', u'ríos', u'topónimos']:
                self.set_es_toponimo(True)
            elif keyword == u'artículo':
                print(u'Esto se tiene que mirar mejor:', self._lema_txt)
                self.set_categoria(DETERMINANTE)
                self.append_tipo(ARTICULO_D)
                if etiqueta != u'artículo':  # Si contiene algo más
                    if u'determinado' in etiqueta:
                        self.append_tipo(DETERMINADO)
                    elif u'indeterminado' in etiqueta.replace(u'_', u''):
                        self.append_tipo(INDETERMINADO)
                    elif verboso:
                        print(u'La etiqueta {{' + etiqueta + u'}} no se procesa bien. Lema:', self._lema_txt)
            elif keyword == u'conjunción':
                self.set_categoria(CONJUNCION)
                if etiqueta != u'conjunción':  # Si contiene algo más
                    if u'distributiva' in etiqueta:
                        self.append_tipo(DISTRIBUTIVA)
                    elif u'adversativa':
                        self.append_tipo(ADVERSATIVA)
                    elif u'causal':
                        self.append_tipo(CAUSAL)
                    elif u'final':
                        self.append_tipo(FINAL)
                    elif verboso:
                        print(u'La etiqueta {{' + etiqueta + u'}} no se procesa bien. Lema:', self._lema_txt)
            elif keyword == u'contracción':
                self.set_categoria(CONTRAIDA)
            elif keyword in [u'diminutivo', u'aumentativo', u'superlativo', u'comparativo']:
                self.set_grado({u'diminutivo': DIMINUTIVO, u'aumentativo': AUMENTATIVO,
                                u'superlativo': SUPERLATIVO, u'comparativo': COMPARATIVO})
                self.set_grado(DIMINUTIVO if keyword == u'diminutivo'
                               else AUMENTATIVO if keyword == u'aumentativo' else SUPERLATIVO)
                if parametros_sin_igual:
                    # Azadón -> {{aumentativo|azada|tipo=sustantivo}}, Peor -> {{comparativo|irreg=sí|mal}}
                    self.set_lema_base(parametros_sin_igual[0])
            elif keyword == u'enclítico':
                self.set_es_enclitico(True)
            elif keyword in [u'gentilicio', u'gentilicios', u'gentilicio1', u'gentilicio2', u'gentilicio3']:
                self.append_tipo(GENTILICIO)
            elif keyword == u'impropia':  # En realidad "impropia" significa que es gramatical
                self.set_es_impropia(True)
            elif keyword == u'infinitivo':
                self.append_tipo(INFINITIVO)  # La categoría será la de forma verbal
                # https://es.wiktionary.org/wiki/Plantilla:infinitivo
                # Usualmente indica el inf sin el -se de un verbo que es sólo pronominal. El -se es separable.
                if parametros_sin_igual:
                    self.set_lema_base(parametros_sin_igual[0])  # El primer parámetro es el lema de la forma
            elif keyword == u'gerundio':  # Ahora las formas se eliminan, así que aquí no llegamos
                self.append_tipo(GERUNDIO)  # La categoría será la de forma verbal
                # https://es.wiktionary.org/wiki/Plantilla:gerundio
                # Usualmente indica el gerundio sin el -se de un verbo que es sólo pronominal. El -se es separable.
                if parametros_sin_igual:
                    self.set_lema_base(parametros_sin_igual[0])  # El primer parámetro es el lema de la forma
            elif keyword == u'participio':  # Ahora las formas se eliminan, así que aquí no llegamos
                self.append_tipo(PARTICIPIO)  # La categoría será la de forma verbal
                # https://es.wiktionary.org/wiki/Plantilla:participio
                # Usualmente indica el part sin el -se de un verbo que es sólo pronominal. El -se es separable.
                if parametros_sin_igual:
                    self.set_lema_base(parametros_sin_igual[0])  # El primer parámetro es el lema de la forma
            elif keyword == u'interjección':
                self.set_categoria(INTERJECCION)
            elif keyword in [u'dígrafo', u'letra']:  # Es una letra, es decir, un nombre común femenino
                self.set_categoria(SUSTANTIVO)
                self.set_genero(FEMENINO)
            elif keyword == u'onomatopeya':
                self.set_categoria(ONOMATOPEYA)
            elif keyword == u'plural':
                self.set_categoria(FORMA)
                self.set_numero(PLURAL)
                # https: // es.wiktionary.org / wiki / Plantilla:forma_sustantivo_plural
                if parametros_sin_igual:
                    self.set_lema_base(parametros_sin_igual[0])
            elif keyword == u'prefijo':
                self.set_categoria(PREFIJO)
            elif keyword == u'preposición':
                self.set_categoria(PREPOSICION)
            elif keyword == u'pronombre':
                self.set_categoria(PRONOMBRE)
                if etiqueta != u'pronombre':  # Si incluye algo más
                    if u'demostrativo' in etiqueta:
                        self.append_tipo(DEMOSTRATIVO)
                        if u'masculino' in etiqueta:
                            self.set_genero(MASCULINO)
                        elif u'femenino' in etiqueta:
                            self.set_genero(FEMENINO)
                        elif u'neutro' in etiqueta:
                            self.set_genero(NEUTRO)
                    elif u'interrogativo' in etiqueta:
                        self.append_tipo(INTERROGATIVO)
                    elif u'personal' in etiqueta:
                        self.append_tipo(PERSONAL)
                        if u'átono' in etiqueta:
                            print(self._lema_txt, u'es un pronombre personal átono')
                            self.append_tipo(ATONO)
                    elif u'relativo' in etiqueta:
                        self.append_tipo(RELATIVO)
                    elif u'exclamativo' in etiqueta:
                        self.append_tipo(EXCLAMATIVO)
                    elif u'indeterminado' in etiqueta:
                        self.append_tipo(INDETERMINADO)
                        print(self._lema_txt, u'es un pronombre indeterminado (LQQQES)')
                    elif u'indefinido' in etiqueta:
                        self.append_tipo(INDEFINIDO)
                    elif verboso:
                        print(u'La etiqueta {{' + etiqueta + u'}} no se procesa bien. Lema:', self._lema_txt)
            elif keyword == u'refrán':  # De un lema normal, se da un ejemplo de refrán donde aparece.
                pass
            elif keyword == u'sigla':
                self.set_categoria(SIGLA)
            elif keyword == u'sufijo':
                self.set_categoria(SUFIJO)
                if u'flexivo' in etiqueta:
                    self.append_tipo(FLEXIVO)
            elif keyword == u'sustantivo':
                self.set_categoria(SUSTANTIVO)
                if etiqueta != u'sustantivo':  # Si incluye algo más
                    if u'de adjetivo' in etiqueta:
                        self.append_tipo(DE_ADJETIVO)
                    elif u'de verbo' in etiqueta:
                        self.append_tipo(DE_VERBO)
                    if u'colectivo' in etiqueta:  # Hay poquísimos. Los más básicos, no están
                        self.append_tipo(COLECTIVO)
                    if u'compuesto' in etiqueta:
                        self.append_tipo(COMPUESTO)
                    if u'propio' in etiqueta or self._lema_txt != self._lema_txt.lower():
                        self.append_tipo(PROPIO)

                    if u'ambiguo' in etiqueta:
                        self.set_genero(AMBIGUO)
                    else:
                        if u'masculino' in etiqueta:
                            self.set_genero(MASCULINO)
                        # Puede ser "masculino o femenino"
                        if u'femenino' in etiqueta:
                            self.set_genero(FEMENINO)
                    if u'plural' in etiqueta:
                        self.set_numero(PLURAL)
                    if verboso and not self.get_tipos() and not self.get_genero() and self.get_numero() == SINGULAR:
                        print(u'La etiqueta {{' + etiqueta + u'}} no se procesa bien. Lema:', self._lema_txt)
            elif keyword == u'símbolo':
                self.set_categoria(SIMBOLO)
            elif keyword == u'verbo':
                self.set_categoria(VERBO)
                if etiqueta != u'verbo':  # Si incluye algo más
                    if u'auxiliar' in etiqueta:
                        self.set_es_auxiliar(True)  # Sólo para el verbo "haber"
                    if u'impersonal' in etiqueta:
                        self.set_es_impersonal(True)
                    if u'intransitivo' in etiqueta:
                        self.set_es_intransitivo(True)
                    elif u'transitivo' in etiqueta:
                        self.set_es_transitivo(True)
                    if u'pronominal' in etiqueta:
                        self.set_es_pronominal(True)
                    if u'defectivo' in etiqueta:
                        self.set_es_defectivo(True)
                    if u'reflexivo' in etiqueta:
                        self.set_es_reflexivo(True)
            elif keyword == u'desconocida':
                # No hemos encontrado una etiqueta de categoría válida.
                self.set_categoria(DESCONOCIDA)
                print(u'El lema', self._lema_txt, u'tiene una categoría desconocida')
            elif verboso:
                print(u'la etiqueta', etiqueta, u'es rarííííssssima. Lema:', self._lema_txt)
        if self.get_categoria() == VERBO and not self.get_conjs():
            for etiqueta_conj in AcepcionWik.infiere_conjs(self._lema_txt, normativa=True, diptonguiza=False,
                                                           hiatiza=False, cierra=False, impersonal=False):
                self.append_conj(etiqueta_conj)
        if self.get_categoria() == SUSTANTIVO:
            if self.get_es_antroponimo() or self.get_es_toponimo() or self._lema_txt != self._lema_txt.lower():
                self.append_tipo(PROPIO)
            elif not self.get_genero():
                self.set_genero(AcepcionWik.infiere_genero(self._lema_txt))

        if self.get_categoria() in [SUSTANTIVO, ADJETIVO] and not self.get_inflects():
            for etiqueta_inflect in AcepcionWik.infiere_inflect(self._lema_txt, self.get_categoria(),
                                                                PROPIO in self.get_tipos()):
                # En realidad solo hay uno
                self.append_inflect(etiqueta_inflect)

    def get_inflects(self):
        return self._datos["inflects"] if "inflects" in self._datos else []

    def append_inflect(self, etiqueta_inflect):
        # Este método solo se usa para las acepciones del Wikcionario
        etiqueta_inflect = AcepcionWik.limpia_etiqueta_flexion(etiqueta_inflect)
        if "inflects" not in self._datos:
            self._datos["inflects"] = [etiqueta_inflect]
        elif etiqueta_inflect not in self._datos["inflects"]:
            self._datos["inflects"].append(etiqueta_inflect)

    def append_conj(self, etiqueta_conj):
        etiqueta_conj = AcepcionWik.limpia_etiqueta_flexion(etiqueta_conj)
        Acepcion.append_conj(self, etiqueta_conj)

    @staticmethod
    def infiere_genero(lema_txt):
        # TODO: esto es un boceto. Habría que ver según la terminación.
        # En realidad, esto procesa algunas excepciones, y con esto nos vale para ellas.
        if lema_txt[-1] in u'aá':
            return FEMENINO
        else:
            return MASCULINO

    @staticmethod
    def infiere_conjs(lema_txt, normativa=True, diptonguiza=True, hiatiza=True, cierra=True, impersonal=False):
        # OJO: aunque está algo currado, en realidad es un coladero y puede hacer cosas mal. No obstante,
        # la mayor parte de los verbos ya tiene el valor de conjugación apropiado y esto es solo para las
        # excepciones fuera del Wikci.
        pronominal = False
        if lema_txt[-2:] == u'se':
            lema_txt = lema_txt[:-2]
            pronominal = True

        silabas = Palabra(palabra_texto=lema_txt, calcula_alofonos=False, organiza_grafemas=True).get_silabas()

        etiquetas_conj = []
        if len(lema_txt) >= 8:
            if lema_txt[-8:] in [u'bendecir', u'maldecir']:
                etiquetas_conj.append(u'v.conj.benmal.decir|' + lema_txt[:-5])
                diptonguiza = False
        if not etiquetas_conj and len(lema_txt) >= 6:
            if lema_txt[-6:] in [u'querer', u'seguir']:
                etiquetas_conj.append(u'v.conj.' + lema_txt[-6:] + (u'|' + lema_txt[:-6] if lema_txt[:-6] else u''))
                diptonguiza = False
        if not etiquetas_conj and len(lema_txt) >= 5:
            if lema_txt[-5:] in [u'andar', u'decir', u'valer', u'venir', u'yacer', u'tener', u'traer', u'saber',
                                 u'salir', u'poner']:
                etiquetas_conj.append(u'v.conj.' + lema_txt[-5:] + (u'|' + lema_txt[:-5] if lema_txt[:-5] else u''))
                diptonguiza = False
            elif lema_txt[-5:] in [u'hacer']:
                etiquetas_conj.append(u'v.conj.hacer|' + lema_txt[:-4])
                if len(lema_txt) > 5 and lema_txt[-6] in u'eao':
                    etiquetas_conj[0] += u'|i=í'  # Para "rehíce" o similares con prefijo acabado en vocal fuerte
            elif lema_txt[-5:] in [u'ducir']:
                etiquetas_conj.append(u'v.conj.ducir|' + lema_txt[:-3])
            elif lema_txt[-5:] in [u'aizar', u'eizar', u'oizar']:
                etiquetas_conj.append(u'v.conj.izar|' + lema_txt[:-4])
        if not etiquetas_conj and len(lema_txt) >= 4:
            if lema_txt[-4:] in [u'caer', u'cuar', u'eñir', u'guar', u'roer']:
                etiquetas_conj.append(u'v.conj.' + lema_txt[-4:] + (u'|' + lema_txt[:-4] if lema_txt[:-4] else u''))
                diptonguiza = False
            elif lema_txt[-4:] in [u'ucir']:
                etiquetas_conj.append(u'v.conj.zc.cir|' + lema_txt[:-3])
            elif lema_txt[-4:] in [u'ecer', u'ocer', u'acer']:
                etiquetas_conj.append(u'v.conj.zc.cer|' + lema_txt[:-3])
                if lema_txt[-4:] in [u'ecer']:
                    diptonguiza = False
            elif lema_txt[-4:] in [u'ller']:
                etiquetas_conj.append(u'v.conj.ñer|' + lema_txt[:-2])
                diptonguiza = False
            elif lema_txt[-4:] in [u'llir']:
                etiquetas_conj.append(u'v.conj.llir|' + lema_txt[:-2])
                diptonguiza = False
        if not etiquetas_conj and len(lema_txt) >= 3:
            if lema_txt[-3:] in [u'car', u'cer', u'cir', u'dar', u'eír', u'gar', u'ger', u'gir', u'üir', u'zar']:
                etiquetas_conj.append(u'v.conj.' + lema_txt[-3:] + (u'|' + lema_txt[:-3] if lema_txt[:-3] else u''))
            elif lema_txt[-3:] in [u'eer', u'oír']:
                etiquetas_conj.append(u'v.conj.' + lema_txt[-3:] + u'|' + lema_txt[:-2] +
                                      (u'|part2=' + lema_txt[:-3] + u'isto' if lema_txt[-4:] == u'veer' else u''))
                diptonguiza = False
            elif lema_txt[-3:] in [u'ñer', u'ñir']:
                etiquetas_conj.append(u'v.conj.' + lema_txt[-3:] + u'|' + lema_txt[:-2])
                diptonguiza = False
            elif lema_txt[-3:] in [u'ver'] and lema_txt[-6:] != u'volver':
                etiquetas_conj.append(u'v.conj.' + lema_txt[-3:] + u'|' + lema_txt[:-2])
                diptonguiza = False
            elif lema_txt[-3:] in [u'uir'] and len(lema_txt) > 3 and lema_txt[-4] not in u'gq':
                etiquetas_conj.append(u'v.conj.' + lema_txt[-3:] + u'|' + lema_txt[:-2])
                diptonguiza = False
            elif lema_txt[-3:] in [u'iar', u'uar']:
                if hiatiza:
                    # Repatriar, actuar
                    etiquetas_conj.append(u'v.conj.2.ar|' + lema_txt[:-2] +
                                          u'|' + lema_txt[:-3] + {u'i': u'í', u'u': u'ú'}[lema_txt[-3]])
                if normativa or not hiatiza:
                    etiquetas_conj.append(u'v.conj.ar|' + lema_txt[:-2])  # Diluviar, menguar
                diptonguiza = False
            else:
                if lema_txt[-2:] in [u'ar']:
                    # Hay conjugación específica para -car, -gar, -zar
                    caracteres_nexo = 0  # Sólo hay nexo con -car, -gar, -zar -> qu, gu, c (y ya se capturaron arriba).
                    if hiatiza and len(silabas) > 1 and silabas[-2].get_fonema_semivocal():
                        # Enraizar
                        etiquetas_conj.append(u'v.conj.2.ar|' + lema_txt[:-2])
                    if normativa or not hiatiza:
                        etiquetas_conj.append(u'v.conj.ar|' + lema_txt[:-2])
                elif lema_txt[-2:] in [u'er']:
                    # No hay conjugaciones específicas para -guer, -quer, pero sí para -ger, -cer (ya tratadas)
                    caracteres_nexo = 2 if lema_txt[:-2][-2:] in [u'gu', u'qu'] else 0
                    etiquetas_conj.append(u'v.conj.er|' + lema_txt[:-2 - caracteres_nexo])
                elif lema_txt[-2:] in [u'ir']:
                    if len(silabas) > 1 and silabas[-2].get_fonema_semivocal() and lema_txt[:-2] == u're':
                        # Reunir, rehundir
                        caracteres_nexo = 2 if lema_txt[:-2][-2:] in [u'gu', u'qu']\
                            else 1 if lema_txt[:-2][-1] in u'cg' else 0
                        etiquetas_conj.append(u'v.conj.ir.hiato|' + lema_txt[:-2 - caracteres_nexo])
                        silabas_hiato = silabas[:-1]
                        grafemas_coda = silabas[-1].get_grafemas_coda()
                        silabas_hiato[-1].reset_grafemas_coda()
                        forma_hiato = Palabra(silabas=silabas_hiato, calcula_alofonos=False, organiza_grafemas=True).\
                            transcribe_ortograficamente_palabra(separador=u'', apertura=u'', cierre=u'')
                        forma_hiato = forma_hiato[:-1] + {u'i': u'í', u'u': u'ú'}[forma_hiato[-1]]
                        for grafema_coda in grafemas_coda:
                            forma_hiato += grafema_coda.get_grafema_txt()
                        etiquetas_conj[0] += u'|' + forma_hiato[:-2 - caracteres_nexo]
                    else:
                        # No hay conjugaciones específicas para -guir, -quir, pero sí para -gir, -cir (ya tratadas)
                        caracteres_nexo = 2 if lema_txt[:-2][-2:] in [u'gu', u'qu'] else 0
                        etiquetas_conj.append(u'v.conj.ir|' + lema_txt[:-2 - caracteres_nexo])
                else:  # elif lema[-2:] in [u'ír']:
                    caracteres_nexo = 2 if lema_txt[:-2][-2:] in [u'gu', u'qu']\
                        else 1 if lema_txt[:-2][-1] in u'cg' else 0
                    etiquetas_conj.append(u'v.conj.ir|' + lema_txt[:-2 - caracteres_nexo])

                if caracteres_nexo > 0:
                    etiquetas_conj[-1] += u'|nexo=' + lema_txt[:-2][-caracteres_nexo:]
        if not etiquetas_conj and len(lema_txt) == 2:
            # Sólo puede ser el verbo 'ir'
            etiquetas_conj.append(u'v.conj.ir|irregular=sí' + (u'|pronominal=s' if lema_txt[-2:] == u'se' else u'') +
                                  u'|ger=yendo'
                                  u'|i.p.1s=voy|i.p.2s=vas|i.p.2s2=vas|i.p.3s=va|i.p.1p=vamos|i.p.2p=vais|i.p.3p=van'
                                  u'|i.pi.1s=iba|i.pi.2s=ibas|i.pi.3s=iba|i.pi.1p=íbamos|i.pi.2p=ibais|i.pi.3p=iban'
                                  u'|i.pp.1s=fui|i.pp.2s=fuiste|i.pp.3s=fue'
                                  u'|i.pp.1p=fuimos|i.pp.2p=fuisteis|i.pp.3p=fueron'
                                  u'|s.p.1s=vaya|s.p.2s=vayas|s.p.2s2=vayás|s.p.3s=vaya'
                                  u'|s.p.1p=vayamos|s.p.2p=vayáis|s.p.3p=vayan'
                                  u'|s.pi.1s=fuera|s.pi.2s=fueras|s.pi.3s=fuera'
                                  u'|s.pi.1p=fuéramos|s.pi.2p=fuerais|s.pi.3p=fueran'
                                  u'|s.pi2.1s=fuese|s.pi2.2s=fueses|s.pi2.3s=fuese'
                                  u'|s.pi2.1p=fuésemos|s.pi2.2p=fueseis|s.pi2.3p=fuesen'
                                  u'|s.f.1s=fuere|s.f.2s=fueres|s.f.3s=fuere'
                                  u'|s.f.1p=fuéremos|s.f.2p=fuereis|s.f.3p=fueren'
                                  u'|im.2s=ve|im.2s2=andá'
                                  u'|gerpron=yéndose|imppron2s=vete|imppron2s2=andate|imppron3s=váyase'
                                  u'|imppron1p=vámonos|imppron2p=idos|imppron3p=váyanse')

        # AÑADIMOS FORMAS DIPTONGADAS (o cerrada) SI HACE FALTA
        if (diptonguiza or cierra) and not silabas[-1].get_fonema_semiconsonante() and len(silabas) > 1 \
                and not silabas[-2].get_fonema_semiconsonante() and not silabas[-2].get_fonema_semivocal():
            caracteres_nexo = 0
            # Pensar, contar, jugar
            if lema_txt[-2:] in [u'ar'] and (silabas[-2].get_fonema_vocal().get_abertura() == MEDI or
                                             silabas[-2].get_fonema_vocal().get_localizacion() == POST):
                if not normativa:
                    etiquetas_conj = []
                if lema_txt[-3:] in [u'gar', u'zar']:  # Hay conjugaciones específicas, pero no para -car
                    etiquetas_conj.append(u'v.conj.-ie-ue-.' + lema_txt[-3:] + u'|' + lema_txt[:-3])
                    if silabas[-2].get_fonema_vocal().get_localizacion() == ANTE:
                        forma_diptongo = u'ie'.join(lema_txt[:-3].rsplit(u'e', 1))
                    else:
                        vocal = u'o' if silabas[-2].get_fonema_vocal().get_abertura() == MEDI else u'u'
                        if len(silabas[-2].get_grafemas_ataque()) == 1 and\
                                silabas[-2].transcribe_ortograficamente_silaba(False)[0] == u'g':
                            forma_diptongo = u'güe'.join(lema_txt[:-3].rsplit(u'g' + vocal, 1))
                        else:
                            forma_diptongo = u'ue'.join(lema_txt[:-3].rsplit(vocal, 1))
                else:
                    caracteres_nexo = 1 if lema_txt[:-2][-1] in u'c' else 0  # -gar y -zar caen arriba
                    etiquetas_conj.append(u'v.conj.-ie-ue-.ar|' + lema_txt[:-2 - caracteres_nexo])
                    if silabas[-2].get_fonema_vocal().get_localizacion() == ANTE:
                        forma_diptongo = u'ie'.join(lema_txt[:-2 - caracteres_nexo].rsplit(u'e', 1))
                    else:
                        vocal = u'o' if silabas[-2].get_fonema_vocal().get_abertura() == MEDI else u'u'
                        if len(silabas[-2].get_grafemas_ataque()) == 1 and \
                                silabas[-2].transcribe_ortograficamente_silaba(False)[0] == u'g':
                            forma_diptongo = u'güe'.join(lema_txt[:-2 - caracteres_nexo].rsplit(u'g' + vocal, 1))
                        else:
                            forma_diptongo = u'ue'.join(lema_txt[:-2 - caracteres_nexo].rsplit(vocal, 1))
                etiquetas_conj[-1] += u'|' + forma_diptongo
            # Entender, mover
            elif lema_txt[-2:] in [u'er'] and silabas[-2].get_fonema_vocal().get_abertura() == MEDI:
                if not normativa:
                    etiquetas_conj = []
                caracteres_nexo = 2 if lema_txt[:-2][-2:] in [u'gu', u'qu'] else 1 if lema_txt[:-2][-1] in u'cg' else 0
                etiquetas_conj.append(u'v.conj.-ie-ue-.er|' + lema_txt[:-2 - caracteres_nexo])
                if silabas[-2].get_fonema_vocal().get_localizacion() == ANTE:
                    forma_diptongo = u'ie'.join(lema_txt[:-2 - caracteres_nexo].rsplit(u'e', 1))
                else:
                    if len(silabas[-2].get_grafemas_ataque()) == 1 and \
                            silabas[-2].transcribe_ortograficamente_silaba(False)[0] == u'g':
                        forma_diptongo = u'güe'.join(lema_txt[:-2 - caracteres_nexo].rsplit(u'go', 1))
                    else:
                        forma_diptongo = u'ue'.join(lema_txt[:-2 - caracteres_nexo].rsplit(u'o', 1))
                etiquetas_conj[-1] += u'|' + forma_diptongo
            elif lema_txt[-2:] in [u'ir'] and silabas[-2].get_fonema_vocal().get_abertura() == MEDI:  # Sentir, dormir.
                #  OJO: con la variable 'cierra' a True es como pedir, elegir.
                if not normativa:
                    etiquetas_conj = []
                caracteres_nexo = 2 if lema_txt[:-2][-2:] in [u'gu', u'qu'] else 1 if lema_txt[:-2][-1] in u'cg' else 0
                etiquetas_conj.append(u'v.conj.-ie-i-ue-u-.ir|' + lema_txt[:-2 - caracteres_nexo])
                if silabas[-2].get_fonema_vocal().get_localizacion() == ANTE:
                    forma_diptongo = u'ie'.join(lema_txt[:-2 - caracteres_nexo].rsplit(u'e', 1))
                    forma_cerrada = u'i'.join(lema_txt[:-2 - caracteres_nexo].rsplit(u'e', 1))
                else:
                    if len(silabas[-2].get_grafemas_ataque()) == 1 and \
                            silabas[-2].transcribe_ortograficamente_silaba(False)[0] == u'g':
                        forma_diptongo = u'güe'.join(lema_txt[:-2 - caracteres_nexo].rsplit(u'go', 1))
                    else:
                        forma_diptongo = u'ue'.join(lema_txt[:-2 - caracteres_nexo].rsplit(u'o', 1))
                    forma_cerrada = u'u'.join(lema_txt[:-2 - caracteres_nexo].rsplit(u'o', 1))
                etiquetas_conj[-1] += u'|' + (forma_diptongo if diptonguiza else forma_cerrada) +\
                                      (u'|' + forma_cerrada if cierra else u'')

            if caracteres_nexo > 0:  # OJO: -gar y -zar no caen aquí
                etiquetas_conj[-1] += u'|nexo=' + lema_txt[:-2][-caracteres_nexo:]
            pass

        if pronominal:
            # Deberíamos añadir la etiqueta pronominal=s y además meter la forma tónica.
            # Pero más adelante se vacían estos huecos y se calcula la forma tónica y demás.
            # Así que no hace falta hacer nada porque se hace después.
            # etiqueta_conj += u'|pronominal=s'
            pass

        if len(silabas) == 1:
            for orden_etiqueta, etiqueta_conj in enumerate(etiquetas_conj):
                etiquetas_conj[orden_etiqueta] += u'|mono=s'

        if impersonal:
            for orden_etiqueta, etiqueta_conj in enumerate(etiquetas_conj):
                etiquetas_conj[orden_etiqueta] += u'|impersonal=plural'

        # print(lema_txt, u'no tenía etiqueta de conjugación. Le hemos asignado', etiquetas_conj)
        return etiquetas_conj

    @staticmethod
    def infiere_inflect(lema_txt, categoria, propio=False):
        inflects = []
        if categoria in [SUSTANTIVO, ADJETIVO]:
            if categoria == SUSTANTIVO and propio:
                inflects = [u'inflect.sust.invariante']
            else:  # No es nombre propio
                if categoria == SUSTANTIVO:
                    tag_categoria = u'sust.'
                    if lema_txt[-1] in u'aáeéoóiu':
                        inflects = [u'inflect.es.' + tag_categoria + u'reg|' + lema_txt]
                else:  # ADJETIVO
                    tag_categoria = u'adj.'
                    if lema_txt[-1] in u'aáeéiu':
                        inflects = [u'inflect.es.' + tag_categoria + u'no-género']
                    elif lema_txt[-1] in u'oó':
                        inflects = [u'inflect.es.' + tag_categoria + u'reg|' + lema_txt[:-1]]
                if not inflects:
                    # Parte común
                    if lema_txt[-1] in u'íú':
                        inflects = [u'inflect.es.' + tag_categoria + u'í']
                    elif lema_txt[-1] in u'n':
                        palabra = Palabra(palabra_texto=lema_txt, calcula_alofonos=False, organiza_grafemas=True)
                        if len(palabra.get_silabas()) == 1:  # Es monosílabo, tipo "truhan", o "guion"
                            inflects = [u'inflect.es.' + tag_categoria + u'reg-cons']
                        elif palabra.get_posicion_tonica() == -1:  # Es aguda polisílaba
                            # Si no tiene semivocal, podemos usar el inflect agudo-cons tipo rev|é|s
                            if not palabra.get_silabas()[-1].get_fonema_semivocal():
                                inflects = [u'inflect.es.' + tag_categoria + u'agudo-cons|' + lema_txt[:-2] + u'|' +
                                            {u'á': u'a', u'é': u'e', u'í': u'i', u'ó': u'o', u'ú': u'u'}[lema_txt[-2]] +
                                            u'|' + lema_txt[-1]]
                            else:
                                # La cosa se complica. Las palabras así son rarísimas, nombres propios,
                                # de otras lenguas o casi inventadas, tipo arriquitáun, Espáin, Andoáin...
                                # La plantilla agudo-cons no admite esto. Lo hacemos a mano.
                                forma_atona = palabra.set_tilde(con_tilde=False)
                                inflects = [u'inflect.es.' + tag_categoria + u'ad-lib|' + lema_txt +
                                            u'|' + forma_atona + u'es' +
                                            ((u'|' + forma_atona + u'a' +
                                              u'|' + forma_atona + u'as') if categoria == ADJETIVO else u'')]
                        else:
                            # Se producen cambios en las tildes (pasa de llana a esdrújula).
                            forma_acentuada = palabra.set_tilde(con_tilde=True)
                            inflects = [u'inflect.es.' + tag_categoria + u'ad-lib|' + lema_txt +
                                        u'|' + forma_acentuada + u'es' +
                                        ((u'|' + forma_acentuada + u'a' +
                                          u'|' + forma_acentuada + u'as') if categoria == ADJETIVO else u'')]
                    elif lema_txt[-1] in u'sx':
                        # Alguno en -s debería ser más bien pluralia tantum, pero son poquísimas
                        inflects = [u'inflect.es.' + tag_categoria + u'invariante']
                    elif lema_txt[-1] in u'z':
                        inflects = [u'inflect.es.' + tag_categoria + u'ad-lib|' + lema_txt +
                                    u'|' + lema_txt[:-1] + u'ces']
                    elif lema_txt[-1] in u'rldb':
                        inflects = [u'inflect.es.' + tag_categoria + u'reg-cons']
                    else:
                        # Son palabras por lo general extranjeras tipo slip, short, confort, notebook...
                        inflects = [u'inflect.es.' + tag_categoria + u'reg|' + lema_txt]

        elif categoria == PRONOMBRE:
            inflects = [u'inflect.desconocida']
        elif categoria == DETERMINANTE:
            inflects = [u'inflect.desconocida']
        else:
            print(u'¡Qué demonios!')
        return inflects

    @staticmethod
    def limpia_etiqueta_flexion(etiqueta):
        etiqueta = etiqueta.replace(u"'", u'').replace(u'*', u'').replace(u'(', u'').replace(u')', u'')\
            .replace(u'¿', u'').replace(u'?', u'')
        # Quitamos las macros para que marque las irregularidades en negrita en la web
        regex = u'\{\{(resaltar|marcar sin referencias|l.?\|[a-z]{1,2})\|[^}]+\}\}'
        inicio = 0
        while True:
            hay_cambios = False
            while True:
                extremos = re.search(regex, etiqueta[inicio:], re.IGNORECASE)
                if not extremos:
                    # Hemos llegado al final. Salimos del bucle.
                    break
                fin = extremos.end() + inicio
                inicio += extremos.start()
                texto = etiqueta[inicio + etiqueta[inicio:fin].rfind(u'|') + 1:fin - 2]
                hay_cambios = True
                etiqueta = etiqueta[:inicio] + texto + etiqueta[fin:]

            if not hay_cambios:
                break
            else:
                inicio = 0

        # Algunas etiquetas de conjugación contienen texto wiki, enlaces del tipo [[enlace|enlace]]
        regex = u'\[\[(([^[])|(\[(?!\[)))*?\]\]'
        inicio = 0
        while True:
            hay_cambios = False
            while True:
                extremos = re.search(regex, etiqueta[inicio:], re.IGNORECASE)
                if not extremos:
                    # Hemos llegado al final. Salimos del bucle.
                    break
                fin = extremos.end() + inicio
                inicio += extremos.start()
                texto = etiqueta[inicio:fin]
                texto_sin_tag = etiqueta[inicio + 2:fin - 2]
                hay_cambios = True
                separacion_enlace_texto = texto_sin_tag.rfind(u'|')
                if separacion_enlace_texto != -1:
                    # enlace = texto_sin_tag[:separacion_enlace_texto]
                    texto = texto_sin_tag[separacion_enlace_texto + 1:]
                else:
                    texto = texto_sin_tag
                etiqueta = etiqueta[:inicio] + texto + etiqueta[fin:]
            if not hay_cambios:
                break
            else:
                inicio = 0

        return etiqueta

    def procesa_etiquetas_conj(self):
        datos_etiquetas_conj = []
        for etiqueta_conj in self.get_conjs():
            datos_etiquetas_conj.append(AcepcionWik.procesa_etiqueta_conj(self._lema_txt, etiqueta_conj))
        return datos_etiquetas_conj

    @staticmethod
    def procesa_etiqueta_conj(lema_txt, etiqueta_conj):
        u"""Se toma la etiqueta de la plantilla conj del Wikcionario y se extraen una serie de parámetros

        :param lema_txt:
        :param etiqueta_conj:
        :return:
        """
        paradigma = 1 if lema_txt[-2:] == u'ar' else 2 if lema_txt[-2:] == u'er' else 3  # -ir, -ír
        # TODO: cambiar la siguiente línea da grima, porque va bien pero realmente machacamos parámetros vacíos.
        # No se debería hacer ese replace de las dobles barras pero así parece funcionar bien siempre.
        # A veces salen parámetros vacíos, tipo ...||...|...|
        if u'||' in etiqueta_conj:
            pass
        partes_etiqueta = etiqueta_conj.replace(u'||', u'|').split(u'|')
        # El texto previo al primer | es siempre el de tipo de flexión. El resto son parámetros.
        plantilla_conj = partes_etiqueta[0]
        mono = len(Palabra(palabra_texto=lema_txt, calcula_alofonos=False).get_silabas()) == 1
        datos_conj = {"paradigma": paradigma, "plantilla_conj": plantilla_conj, "lema": lema_txt,
                      "raices": [], "nexos": {"a": u'', "i": u''}, "mono": mono, "formas": {}, "pronominal": False,
                      "palatal": False}
        parametros = [param.strip() for param in partes_etiqueta[1:]]
        for parametro in parametros:
            if u'=' not in parametro:
                if parametro.strip() != u'':
                    datos_conj["raices"].append(parametro.strip())
                continue
            if parametro.count(u'=') != 1:
                # Debe de haber algún error con el parámetro. Tendrá un = en un [http://asf=asfas=...
                continue
            etiqueta_partida = parametro.split(u'=')
            codigo = etiqueta_partida[0].strip().lower()
            valor = etiqueta_partida[1].strip() if len(etiqueta_partida) > 1 else u''

            if codigo.lower() in [u'pronominal', u'impersonal', u'irregular', u'i']:  # u'i' es parámetro de "hacer"
                #
                datos_conj[codigo] = valor
            elif codigo.lower() == u'nexo':
                if paradigma == 1:
                    datos_conj["nexos"] = {"a": valor, "i": NEXOS_IE[valor]}
                else:
                    datos_conj["nexos"] = {"a": NEXOS_AOU[valor], "i": valor}
            elif codigo.lower() in [u'notas', u'resaltar', u'conjugacion', u'mono', u'gerreg', u'gerundio regular']:
                # No nos interesan estos parámetros. Los de resaltar, gerreg y gerundio regular sólo valen para poner
                # en negrita las formas en la página del wikcionario. Las de mono y conjugacion se extraen ya sin
                # problemas del propio lema, y las notas no interesan
                continue
            else:
                # Es una etiqueta de una forma verbal concreta
                datos_conj["formas"][codigo] = valor
        if len(datos_conj["raices"]) == 0:
            datos_conj["raices"] = [u'']  # Hay tags conj que no necesitan parámetros: traer, dar...

        # IDENTIFICACIÓN DE RAÍCES: átona, diptongada, cerrada y tónica
        raices = {"ato": datos_conj["raices"][0]}
        if datos_conj["pronominal"]:
            # La raíz acentuada siempre es la última
            raices["ton"] = datos_conj["raices"][-1]
            # Si no hay un único dato de raíz (en cuyo caso todas las raíces son iguales), no se quita, pero si
            # hay más, se borra la raíz que acabamos de tomar. Esto se hace para que la lógica posterior funcione.
            if len(datos_conj["raices"]) > 1:
                datos_conj["raices"] = datos_conj["raices"][:-1]
        if len(datos_conj["raices"]) > 1:
            raices["dip"] = datos_conj["raices"][1]
        else:
            raices["dip"] = datos_conj["raices"][0]
        if len(datos_conj["raices"]) > 2:
            raices["cerr"] = datos_conj["raices"][2]
        else:
            raices["cerr"] = datos_conj["raices"][0]
        # Ponemos los valores procesados de las raíces y machacamos los valores iniciales extraídos de la etiqueta
        datos_conj["raices"] = raices
        if not datos_conj["pronominal"]:
            # Si no nos han dado la forma pronominal, "nos la inventamos". La raíz tónica se usa exclusivamente para las
            # formas con clíticos (incluyendo las de reflexivo) y también se usa en v.conj.2.ar donde debia usarse "dip"
            # porque hay hiato acentuado (en el fondo, "ton" es lo que reemplaza a "dip" cuando necesita tilde).
            # Ponemos este valor de momento, aunque en realidad en los modelos de conjugación que presuponen alguna
            # consonante final previa al -ar/er/-ir/-ír, se tendrá que recalcular cuando recalculemos el resto de
            # raíces o los nexos).
            AcepcionWik.calcula_raiz_tonica(datos_conj)
        return datos_conj

    @staticmethod
    def calcula_raiz_tonica(datos_conj):
        forma_atona = datos_conj["raices"]["dip"]  # Partimos de la forma diptongada
        forma_atona += (datos_conj["nexos"]["a"] + u'a') if datos_conj["paradigma"] == 1\
            else (datos_conj["nexos"]["i"] + u'e')
        palabra = Palabra(palabra_texto=forma_atona, calcula_alofonos=False, organiza_grafemas=True)
        datos_conj["raices"]["ton"] = palabra.set_tilde(con_tilde=True)[:len(datos_conj["raices"]["dip"]) -
                                                                        len(forma_atona)]

    def procesa_etiquetas_inflect(self):
        datos_etiquetas_inflect = []
        for etiqueta_inflect in self.get_inflects():
            datos_etiquetas_inflect.append(AcepcionWik.procesa_etiqueta_inflect(self._lema_txt, etiqueta_inflect))
        return datos_etiquetas_inflect

    @staticmethod
    def procesa_etiqueta_inflect(lema_txt, etiqueta_inflect):
        partes_etiqueta = etiqueta_inflect.split(u'|')
        plantilla_inflect = partes_etiqueta[0]  # El primer parámetro es siempre el de flexión. El resto son infos.
        categoria_implicita = ADJETIVO if u'adj.' in plantilla_inflect else SUSTANTIVO
        plantilla_inflect = plantilla_inflect.replace(u'inflect.', u'').replace(u'es.', u'').replace(u'sust.', u'') \
            .replace(u'adj.', u'')
        parametros = [] if len(partes_etiqueta) == 1 else [param.strip() for param in partes_etiqueta[1:]]
        datos_inflect = {"plantilla_inflect": plantilla_inflect, "lema": lema_txt,
                         "raiz": parametros[0] if parametros and u'=' not in parametros[0] else lema_txt,
                         "categoria_implicita": categoria_implicita, "tiene_singular": True,
                         "parametros": [], "parametros_numericos": {}, "superlativos": []}
        # EXTRACCIÓN DE PARÁMETROS "NUMÉRICOS"
        # A veces, se antepone un código numérico al parámetro, que indica la posición de este parámetro.
        # Su valor depende del tipo de conjugación, por ahora los extraemos.
        orden_parametro = len(parametros) - 1
        while orden_parametro >= 0:
            # Los parámetros numéricos tipo 2=... a veces se quedan en un simple 2 cuando es un parámetro de sí/no
            if u'=' in parametros[orden_parametro] or\
                    (parametros[orden_parametro] and parametros[orden_parametro][0] in u'1234'):
                codigo_parametro = parametros[orden_parametro].split(u'=')[0].strip()
                if codigo_parametro in [u'1', u'2', u'3', u'4']:
                    partes_parametro = parametros[orden_parametro].split(u'=')
                    datos_inflect["parametros_numericos"][codigo_parametro] = partes_parametro[1].strip() \
                        if len(partes_parametro) > 1 else u''
                elif codigo_parametro in [u'sup', u'sup2']:
                    # Es una etiqueta de superlativo (habitualmente vacía)
                    if parametros[orden_parametro].replace(u'sup=', u'').replace(u'sup2=', u''):
                        datos_inflect["superlativos"] += parametros[orden_parametro].split(u'=')[1:]
                elif codigo_parametro in [u'singular']:
                    # Es un parámetro que indica que no existen formas singulares, el propio lema es plural ya.
                    if parametros[orden_parametro].replace(u'singular=', u'') and\
                            parametros[orden_parametro].split(u'=')[1] == u'no':
                        datos_inflect["tiene_singular"] = False
                elif codigo_parametro in [u'plural']:
                    # Es un parámetro que indica que no existen formas plurales
                    if parametros[orden_parametro].replace(u'plural=', u'') and\
                            parametros[orden_parametro].split(u'=')[1] == u'no':
                        datos_inflect["tiene_plural"] = False
                elif codigo_parametro in [u'link']:
                    pass
                parametros = parametros[:orden_parametro] + parametros[orden_parametro + 1:]
            orden_parametro -= 1
        datos_inflect["parametros"] = parametros
        return datos_inflect

    def get_lema_txt(self):
        return self._lema_txt

    def set_lema_txt(self, lema_txt):
        self._lema_txt = lema_txt


class AcepcionRae(Acepcion):
    def __init__(self, acepcion_rae, entrada_rae, verboso=True):
        n_acepcion = acepcion_rae["n_acepcion"]
        n_entrada = entrada_rae["n_entrada"]
        Acepcion.__init__(self, acepcion_rae, "rae", n_entrada, n_acepcion, verboso)
        self._lema_rae_txt = acepcion_rae["lema_rae_txt"]  # Es el "lema" de la RAE: "niño, ña"
        self._formas_expandidas = acepcion_rae["formas_expandidas"]
        self._definicion = acepcion_rae["definicion"]
        self._definicion_post = acepcion_rae["definicion_post"]
        self._ejemplos = acepcion_rae["ejemplos"]
        self._ejemplos_post = acepcion_rae["ejemplos_post"]
        # self._datos["ambitos_uso"] = []
        # self._datos["paises_uso"] = []
        # self._datos["regiones_uso"] = []

        self._acepciones_derivadas = []

        # BORRABLES
        ambitos_total = set()
        paises_total = set()
        regiones_total = set()
        desconocidas = set()
        todas = set()
        if self._lema_rae_txt in [u'le', u'lo']:
            pass
        for tipo_info, datos_info in entrada_rae["morfo"].items():
            if tipo_info == "tambien_superlativo_regular":
                self.set_tambien_superlativo_regular(datos_info)
            elif tipo_info == "masculino_ambiguo":
                self.set_masculino_ambiguo(datos_info)
            elif tipo_info == "superlativos_txt":
                self.set_superlativos_txt(datos_info)
            elif tipo_info == "apocope_txt":
                # Tratamos los apócopes un poco mal. Muchos solo se aplican a ciertas acepciones de la entrada, pero
                # tal y como hemos creado la estructura de datos, no hemos extraído en qué acepciones se usa (cuando
                # esta información aparece en la morfología) o directamente no lo dice (cuando se extrae de otro lema
                # que apunta al "lema padre").
                # En general, usamos el apócope para esta acepción si no es un nombre, o si lo es pero la primera
                # acepción de la entrada es de nombre (que puede ser esta misma). De momento lo ponemos pero puede ser
                # que más adelante lo borremos.
                self.set_apocope_txt(datos_info)
            elif tipo_info == "apocope_plural_txt":
                self.set_apocope_plural_txt(datos_info)
            elif tipo_info == "aumentativos":
                self.set_aumentativos(datos_info)
            elif tipo_info == "diminutivos":
                self.set_diminutivos(datos_info)
            elif tipo_info == "formas_atonas_txt":
                self.set_formas_atonas_txt(datos_info)
            elif tipo_info == "forma_tonica_txt":
                self.set_forma_tonica_txt(datos_info)
            elif tipo_info == "formas_plural":
                self.set_formas_plural(datos_info)
            elif tipo_info == "neutro_txt":
                self.set_neutro_txt(datos_info)
            elif tipo_info == "forma_amalgamada_txt":
                self.set_forma_amalgamada_txt(datos_info)
            elif tipo_info == "comparativo_txt":
                self.set_comparativo_txt(datos_info)
            elif tipo_info == "ids_conjugacion":
                self.set_conjs(datos_info)
            # elif tipo_info == "es_contraccion":
            #     self.set_es_contraccion(True)
            elif tipo_info in ["id_del_que_es_apocope", "id_del_que_es_apocope_plural", "es_apocope"]:
                self.set_es_apocope(True)
            elif tipo_info == "id_del_que_es_forma_atona":
                self.set_es_forma_atona(True)
            elif tipo_info == "id_del_que_es_forma_tonica":
                self.set_es_forma_tonica(True)
            elif tipo_info == "id_del_que_es_superlativo":
                self.set_es_superlativo(True)
            elif tipo_info == "es_pronombre_amalgamado":
                self.set_es_pronombre_amalgamado(True)
            elif tipo_info == "lemas_de_los_que_es_comparativo":
                self.set_es_comparativo(True)
            elif tipo_info in ["ids_superlativos", "id_apocope", "id_apocope_plural", "id_plural", "id_neutro",
                               "ids_formas_casos", "id_comparativo"]:
                pass  # De momento, no nos interesan
            else:
                print(u'Información morfológica no procesada para el lema', self._lema_rae_txt, u':', tipo_info, datos_info)

        for abreviatura in acepcion_rae["abrs_morfo"]:
            # Estas abreviaturas nos informan sobre la categoría de la palabra y de algunos otros aspectos
            abreviatura = re.sub(u' y | o |, | de | persona ', u' ', abreviatura).replace(u'poco usado', u'pocousado')
            keyword = abreviatura.split()[0].lower()
            terminos = abreviatura.split()[1:]
            if keyword == u'locución':
                self.set_es_locucion(True)
                for termino in terminos:
                    if termino == u'adjetiva':
                        self.set_categoria(ADJETIVO)
                        self.append_tipo(CALIFICATIVO)
                    elif termino == u'adverbial':
                        self.set_categoria(ADVERBIO)
                    elif termino == u'sustantiva':
                        self.set_categoria(SUSTANTIVO)
                    elif termino == u'interjectiva':
                        self.set_categoria(INTERJECCION)
                    elif termino == u'desusada':
                        self.set_es_desusado(True)
                    elif termino == u'coloquial':
                        self.append_ambito_uso(u'Coloquial')
                    else:
                        print(u'Locución con tipo extraño:', termino + u':', self._lema_rae_txt +\
                            u' (' + str(n_entrada) + u'|' + str(n_acepcion) + u') ->', abreviatura)
            elif keyword == u'adjetivo':
                # En la RAE se etiqueta como adjetivo muchos lemas que nosotros trataremos como determinantes.
                # Según el tipo del adjetivo, nosotros lo etiquetaremos como adjetivo o como determinante.

                # Los ordinales y cardinales aparecen etiquetados en la RAE simplemente como adjetivos, sin
                # ningún tipo.
                # Añadimos el tipo y después los ordinales y cardinales se etiquetarán como determinantes.
                # Además, en las propias definiciones de la RAE, los cardinales se usan también como
                # pronombres (tienen el "Usado también como pronombre" o directamente una acepción como
                # pronombre).
                if self._formas_expandidas[0] in CARDINALES:
                    # Los números cardinales (salvo "uno" y "cero") son adjetivos/(pro)nombres especiales para
                    # el número (para el género son normales, salvo el tema de apócopes), aunque la RAE no los
                    # distinga del resto.
                    # Cuando son adjs/prons son en sí mismos formas plurales y carecen de singular: seis aves,
                    # dame doce.
                    # Si son nombres masculinos, tienen variación normal de número: saqué un diez, me gustan
                    # los dieces.
                    # Si son nombres femeninos (para las horas, hasta las 23), también tienen valor únicamente
                    # plural.
                    # Por su parte el "cero" en invariante en número: cero euros, cero interés
                    self.append_tipo(CARDINAL)
                    if self._formas_expandidas[0] != u'uno':
                        # Los lemas tipo dos/tres/... + cientos varían en género y tienen formas distintas.
                        self.set_formas_plural([[forma] for forma in self._formas_expandidas])
                        if self._formas_expandidas[0] != u'cero':
                            self.set_numeros_disponibles([PLURAL])
                elif self._formas_expandidas[0] in ORDINALES:
                    self.append_tipo(ORDINAL)

                for termino in terminos:
                    if termino == u'indefinido':
                        # "muchos", "ambos", "cualquiera"...
                        self.append_tipo(INDEFINIDO)
                        if self._lema_rae_txt == u'cada':
                            # "cada" es válido para singular (cada mes) o plural (cada 2 meses), pero la RAE
                            # no lo especifica. Para evitar que cree "cadas", metemos la forma plural.
                            self.set_formas_plural([[u'cada']])
                    elif termino == u'demostrativo':
                        # Las 3 distancias (este, ese, aquel), con neutros y arcaicismos, y "tal", "tan".
                        self.append_tipo(DEMOSTRATIVO)
                    elif termino == u'posesivo':
                        # Los típicos, apocopados o no, de las 3 personas y 2 números: mi, mis, mío, míos...
                        # Además aparecen desusados, como "voso", "nueso"... y también "cuyo", que es también
                        # relativo, con abreviatura "adjetivo relativo posesivo" (con lo que el término
                        # "relativo" ya se ha procesado).
                        # Para la RAE no hay pronombres posesivos, solo adjetivos, lo cual tiene sentido,
                        # porque algo tal que "vuestro" no sustituye nunca a un nombre, lo califica.
                        # Aun cuando se tenga algo como "el vuestro", claramente "el" determina a "vuestro",
                        # igual que si digo "el azul".
                        # Nosotros lo categorizamos como determinante.
                        self.append_tipo(POSESIVO)
                        self.set_persona("1" if u'primera' in abreviatura
                                         else "2" if u'segunda' in abreviatura else "3")
                        # No hay nada más que procesar en la abreviatura, al flexionar deduciremos el resto de
                        # datos (la abreviatura no da todos los datos, como por ejemplo, el número).
                        break
                    elif termino == u'interrogativo':
                        # "qué", "cuál" y "cuánto" ("cuán")
                        self.append_tipo(INTERROGATIVO)
                        if self._lema_rae_txt == u'qué':
                            self.set_formas_plural([[u'qué']])
                    elif termino == u'exclamativo':
                        # "vaya", "qué" y "cuánto" ("cuán")
                        self.append_tipo(EXCLAMATIVO)
                        if self._lema_rae_txt in [u'qué', u'vaya']:
                            self.set_formas_plural([[self._lema_rae_txt]])
                    elif termino == u'relativo':
                        # "cuyo" y "cuanto" ("cuan")
                        if u'posesivo' in abreviatura:
                            # Se trata de "cuyo"
                            self.append_tipo(RELATIVO_POSESIVO)
                            break  # No procesamos otra vez el término "posesivo"
                        self.append_tipo(RELATIVO)
                    elif termino == u'comparativo':
                        # "más", "menos" y "tanto" ("tan")
                        self.append_tipo(COMPARATIVO)
                    elif termino == u'coloquial':
                        self.append_ambito_uso(u'Coloquial')
                    elif termino == u'desusado':
                        self.set_es_desusado(True)
                    elif termino == u'pocousado':
                        self.set_es_poco_usado(True)
                    else:
                        print(termino + u':', self._lema_rae_txt + u' (' + str(n_entrada) + u'|' + str(n_acepcion) + \
                                              u') ->', abreviatura, u'DESCONOCIDA')
                if not self.get_tipos():
                    self.append_tipo(CALIFICATIVO)
                    if self._lema_rae_txt == u'bien':
                        self.set_formas_plural([[u'bien']])
                tipo = self.get_tipos()[0]
                if tipo in [CALIFICATIVO, COMPARATIVO]:  # Etiquetamos como ADJETIVO
                    self.set_categoria(ADJETIVO)
                else:  # Etiquetamos como DETERMINANTE aunque en la RAE vengan como ADJETIVO
                    self.set_categoria(DETERMINANTE)

            elif keyword == u'nombre':  # Son "nombre" aquí pero "sustantivo" en las abreviaturas post
                self.set_categoria(SUSTANTIVO)
                if self._formas_expandidas[0] in CARDINALES and self._formas_expandidas[0] != u'uno' and\
                        u'femenino' in terminos:
                    # Los números cardinales (salvo "uno" y "cero") son adjetivos/(pro)nombres especiales para el número
                    # (para el género son normales, salvo el tema de apócopes), aunque la RAE no los distinga del resto.
                    # Cuando son adjs/prons son en sí mismos formas plurales y carecen de singular: seis mesas, dame 3.
                    # Si son nombres masculinos, tienen variación normal de número: saqué un diez, me gustan los dieces.
                    # Sin son nombres femeninos (para las horas, hasta las 23), también tienen valor únicamente plural.
                    # (en este caso, la RAE ya indica que van en plural).
                    # Por su parte el "cero" en invariante en número: cero euros, cero interés
                    self.set_formas_plural([[forma] for forma in self._formas_expandidas])
                for termino in terminos:
                    if termino == u'masculino':  # Existe "masculino o femenino"
                        self.append_genero_disponible(MASCULINO)
                    elif termino == u'femenino':
                        self.append_genero_disponible(FEMENINO)
                    elif termino == u'plural':
                        self.append_numero_disponible(PLURAL)
                    elif termino == u'coloquial':
                        self.append_ambito_uso(u'Coloquial')
                    elif termino == u'desusado':
                        self.set_es_desusado(True)
                    elif termino == u'pocousado':
                        self.set_es_poco_usado(True)
                    else:
                        print(termino + u':', self._lema_rae_txt + u' (' + str(n_entrada) + u'|' + str(n_acepcion) + \
                                              u') ->', abreviatura, u'DESCONOCIDA')
                # Borramos el apócope si no corresponde
                if self.get_apocope_txt() and u'nombre' not in entrada_rae["acepciones"][0]["abrs_morfo"][0]:
                    # Los apócopes solo se aplican a nombres cuando la primera acepción de la entrada es nombre.
                    # print(u'Borramos el apócope del lema', self._lema_rae_txt,\
                    #     u'(' + str(n_entrada) + u'|' + str(n_acepcion) + u') ->', self.get_apocope_txt())
                    self.reset_apocope_txt()
                    if self._lema_rae_txt == u'cualquiera':
                        # El lema "cualquiera" es muy raro en cuanto al plural. Para empezar, tiene un plural raro
                        # (cualesquiera), además de tener un plural apocopado (cualesquier) y otro plural "regular"
                        # que solo se usa cuando es sustantivo (cualquieras, de "son unas cualquieras").
                        self.set_formas_plural([[u'cualquieras']])
                        self.reset_apocope_plural_txt()

            elif keyword == u'verbo':
                self.set_categoria(VERBO)
                for termino in terminos:
                    if termino == u'transitivo':
                        self.set_es_transitivo(True)
                    elif termino == u'intransitivo':
                        self.set_es_intransitivo(True)
                    # Cuando la abreviatura principal de un verbo indica que es impersonal, siempre se indica si es
                    # transitivo, intransitivo o impersonal, y si no, es implícitamente intransitivo.
                    # Verbos pronominales, auxiliares y copulativos, en ausencia de información que diga lo contrario
                    # son intransitivos implícitamente.
                    # Pero no los marcamos porque luego diferenciamos entre los que son explícitamente transitivos y
                    # el resto, para formar los clíticos. De hecho, los verbos pronominales son generalmente
                    # intransitivos. Hay muy pocos que sean transitivos. Incluso aunque la acepción principal sea
                    # transitiva: estresar (algo) -> estresarse, cansar -> cansarse, doblar -> doblarse...
                    elif termino == u'impersonal':
                        # Si aparece en la abreviatura inicial, siempre se indica que es intransitivo, pronominal o aux
                        # print(self._lema_rae_txt, u'es un verbo', termino, u'de primeras:', u'; '.join(acepcion_rae["abrs_morfo"]) + u' (' + str(n_entrada) + u'|' + str(n_acepcion) + u')')
                        self.set_es_impersonal(True)
                    elif termino == u'pronominal':
                        # Si aparece en la abreviatura inicial, implícitamente es intransitivo.
                        # print(self._lema_rae_txt, u'es un verbo', termino, u'de primeras:', u'; '.join(acepcion_rae["abrs_morfo"]) + u' (' + str(n_entrada) + u'|' + str(n_acepcion) + u')')
                        self.set_es_pronominal(True)
                    elif termino == u'auxiliar':  # Haber y ser
                        # Si aparece en la abreviatura inicial, implícitamente es intransitivo.
                        # print(self._lema_rae_txt, u'es un verbo', termino, u'de primeras:', u'; '.join(acepcion_rae["abrs_morfo"]) + u' (' + str(n_entrada) + u'|' + str(n_acepcion) + u')')
                        self.set_es_auxiliar(True)
                    elif termino == u'copulativo':  # "ser", "estar" y "parecer", y formas antiguas, "seer", "eser"
                        # Si aparece en la abreviatura inicial, implícitamente es intransitivo.
                        # print(self._lema_rae_txt, u'es un verbo', termino, u'de primeras:', u'; '.join(acepcion_rae["abrs_morfo"]) + u' (' + str(n_entrada) + u'|' + str(n_acepcion) + u')')
                        self.set_es_copulativo(True)
                    elif termino in u'desusado':
                        self.set_es_desusado(True)
                    elif termino == u'pocousado':
                        self.set_es_poco_usado(True)
                    else:
                        print(termino + u':', self._lema_rae_txt + u' (' + str(n_entrada) + u'|' + str(n_acepcion) + \
                                              u') ->', abreviatura, u'DESCONOCIDA')
            elif keyword == u'adverbio':
                self.set_categoria(ADVERBIO)
                for termino in terminos:
                    if termino == u'indefinido':
                        # "bastante", "demasiado", "dondequiera"...
                        self.append_tipo(INDEFINIDO)
                    elif termino == u'relativo':
                        # "donde", "según", "como", "cuan", "do"...
                        self.append_tipo(RELATIVO)
                    elif termino == u'interrogativo':
                        # "dónde", "cuán(to)", "cuándo", "cómo", "do".
                        self.append_tipo(INTERROGATIVO)
                    elif termino == u'exclamativo':
                        # "dónde", "cuán(to)", "cuándo", "cómo", "do", "qué", "cuál"
                        self.append_tipo(EXCLAMATIVO)
                    elif termino == u'demostrativo':
                        # Son deícticos: "ayer", "tanto", "aquí", "ahora"...
                        self.append_tipo(DEMOSTRATIVO)
                    elif termino == u'comparativo':
                        # "más", "tanto", "menos", "tan"
                        self.append_tipo(COMPARATIVO)
                    elif termino == u'distributivo':
                        # Únicamente "cuándo"
                        self.append_tipo(DISTRIBUTIVO)
                    elif termino in u'desusado':
                        self.set_es_desusado(True)
                    elif termino == u'pocousado':
                        self.set_es_poco_usado(True)
                    else:
                        print(termino + u':', self._lema_rae_txt + u' (' + str(n_entrada) + u'|' + str(n_acepcion) + \
                                              u') ->', abreviatura, u'DESCONOCIDA')
            elif keyword == u'pronombre':
                self.set_categoria(PRONOMBRE)
                for termino in terminos:
                    if termino == u'indefinido':
                        # "cada", "bastante", "nada", "alguien", "vario", "mucho"...
                        self.append_tipo(INDEFINIDO)
                        if self._lema_rae_txt == u'cada':
                            # "cada" es válido para singular (cada mes) o plural (cada 2 meses), pero la RAE no lo
                            # especifica. Para evitar que cree "cadas", metemos la forma plural.
                            self.set_formas_plural([[u'cada']])
                    elif termino == u'relativo':
                        # "que", "quien", "cuanto", "qui", "cual".
                        self.append_tipo(RELATIVO)
                    elif termino == u'interrogativo':
                        # "qué", "cuál", "quién", "cuánto".
                        self.append_tipo(INTERROGATIVO)
                    elif termino == u'masculino':
                        self.append_genero_disponible(MASCULINO)
                    elif termino == u'femenino':
                        self.append_genero_disponible(FEMENINO)
                    elif termino == u'neutro':
                        self.append_genero_disponible(NEUTRO)
                    elif termino == u'personal':
                        self.append_tipo(PERSONAL)
                    elif termino in [u'primera', u'segunda', u'2.ª', u'tercera']:
                        self.set_persona("1" if termino == u'primera' else "3" if termino == u'tercera' else "2")
                    elif termino == u'singular':
                        self.append_numero_disponible(SINGULAR)
                    elif termino == u'plural':
                        self.append_numero_disponible(PLURAL)
                    elif termino == u'exclamativo':
                        # "qué", "quién", "cuánto".
                        self.append_tipo(EXCLAMATIVO)
                    elif termino == u'demostrativo':
                        # "este", "ese", "aquel", "tanto", "estotro", "esotro", "tal".
                        self.append_tipo(DEMOSTRATIVO)
                    elif termino == u'comparativo':
                        # "más", "tanto" y "menos".
                        self.append_tipo(COMPARATIVO)
                    else:
                        print(termino + u':', self._lema_rae_txt + u' (' + str(n_entrada) + u'|' + str(n_acepcion) + \
                            u') ->', abreviatura, u'DESCONOCIDA')
            elif keyword == u'artículo':
                self.set_categoria(DETERMINANTE)  # Todos los demás determinantes aparecen en la RAE como adjetivos
                for termino in terminos:
                    if termino == u'determinado':
                        # "el"
                        self.append_tipo(ARTICULO_D)
                    elif termino == u'indeterminado':
                        # "un"
                        self.append_tipo(ARTICULO_I)
                    elif termino == u'masculino':
                        self.append_genero_disponible(MASCULINO)
                    elif termino == u'femenino':
                        self.append_genero_disponible(FEMENINO)
                    elif termino == u'neutro':
                        self.append_genero_disponible(NEUTRO)
                    else:
                        print(termino + u':', self._lema_rae_txt + u' (' + str(n_entrada) + u'|' + str(n_acepcion) + \
                            u') ->', abreviatura, u'DESCONOCIDA')
            elif keyword == u'contracción':
                self.set_categoria(PREPOSICION)  # No tiene términos
                palabras_contraidas = self._definicion.lower().split(u'.')[0].split(u';')[0].split()
                self.set_palabras_contraidas(palabras_contraidas)
            elif keyword == u'preposición':
                self.set_categoria(PREPOSICION)  # No tiene términos
            elif keyword == u'conjunción':
                self.set_categoria(CONJUNCION)
                for termino in terminos:
                    if termino == u'adversativa':
                        # "antes", "aunque", "mas", "pero", "empero", "sino"
                        self.append_tipo(ADVERSATIVA)
                    elif termino == u'distributiva':
                        # "siquiera", "agora", "quier", "ora", "bien", "ahora"
                        self.append_tipo(DISTRIBUTIVA)
                    elif termino == u'copulativa':
                        # "y", "e", "ni"
                        self.append_tipo(COPULATIVA)
                    elif termino == u'causal':
                        # "ca", "car", "onde", "porque"
                        self.append_tipo(CAUSAL)
                    elif termino == u'temporal':
                        # "mientras"
                        self.append_tipo(TEMPORAL)
                    elif termino == u'ilativa':
                        # "conque", "luego"
                        self.append_tipo(ILATIVA)
                    elif termino == u'disyuntiva':
                        # "o", "u"
                        self.append_tipo(DISYUNTIVA)
                    elif termino == u'final':
                        # "porque"
                        self.append_tipo(FINAL)
                    elif termino == u'concesiva':
                        # "siquiera", "aunque", "maguer", "maguera"
                        self.append_tipo(CONCESIVA)
                    else:
                        print(termino + u':', self._lema_rae_txt + u' (' + str(n_entrada) + u'|' +
                              str(n_acepcion) + u') ->', abreviatura, u'DESCONOCIDA')
            elif keyword == u'interjección':
                self.set_categoria(INTERJECCION)  # No tiene términos
            elif keyword == u'onomatopeya':
                self.set_categoria(ONOMATOPEYA)  # No tiene términos
            elif keyword == u'prefijo':
                self.set_categoria(PREFIJO)  # No tiene términos
            elif keyword == u'sufijo':
                self.set_categoria(SUFIJO)  # No tiene términos
            elif abreviatura.lower() in [u'elemento compositivo', u'elementos compositivos']:
                # Viene a ser lo mismo que un prefijo/sufijo, pero con "mayor" valor léxico que gramatical.
                # No siempre, pero suelen ser partículas griegas que se anteponen o postponen:
                # clepto-, mega-, xero-, morfo- -morfo, ‒́grado...
                self.set_categoria(ELEMENTO_COMPOSITIVO)
            elif keyword == u'expresión':
                self.set_categoria(EXPRESION)
            elif keyword == u'plural':
                self.append_numero_disponible(PLURAL)  # No tiene términos
            elif keyword == u'singular':
                self.append_numero_disponible(SINGULAR)  # No tiene términos
            elif keyword == u'desusado':
                self.set_es_desusado(True)
            elif keyword == u'pocousado':
                self.set_es_poco_usado(True)
            elif keyword == u'signo':
                self.set_categoria(SIGNO)
            else:
                print(u'Abreviatura desconocida:', abreviatura, u'para el lema', self._lema_rae_txt)
                desconocidas |= {abreviatura}

        for abreviatura in acepcion_rae["abrs_ambito"]:
            abreviatura = re.sub(u'([Uu]sado )?[En]n ((lenguaje|sentido) )?', u'', abreviatura)
            abreviatura = re.sub(u'((?<=^)|(?<=\s))(Aplicado a |[eE]l |[lL]as? )', u'', abreviatura)
            abreviatura = re.sub(u', | y ', u' ', abreviatura).replace(u'.', u'')
            paises = [ab[0].strip()[0].upper() + ab[0].strip()[1:]
                      for ab in re.findall(REGEXP_PAISES, abreviatura)]
            if paises:
                self._datos["paises_uso"] = self._datos.setdefault("paises_uso", []) + paises
                abreviatura = re.sub(REGEXP_PAISES, u'', abreviatura)

            regiones = [ab[0].strip()[0].upper() + ab[0].strip()[1:]
                        for ab in re.findall(REGEXP_REGIONES, abreviatura)]
            if regiones:
                self._datos["regiones_uso"] = self._datos.setdefault("regiones_uso", []) + regiones
                abreviatura = re.sub(REGEXP_REGIONES, u'', abreviatura)

            ambitos = [ab[0].strip()[0].upper() + ab[0].strip()[1:]
                       for ab in re.findall(REGEXP_AMBITOS, abreviatura)]
            if ambitos:
                self._datos["ambitos_uso"] = self._datos.setdefault("ambitos_uso", []) + ambitos
                abreviatura = re.sub(REGEXP_AMBITOS, u'', abreviatura)

        for abreviatura in acepcion_rae["abrs_post"]:
            # Variables auxiliares para separar partes geográficas/ámbitos de categorías alternativas
            ambitos = []
            paises = []
            regiones = []

            abreviatura_original = abreviatura
            abreviatura = re.sub(u'[Uu]sad[oa]s?((,| o)? usad[oa]s?){0,3}', u'usado', abreviatura)
            abreviatura = abreviatura[0].upper() + abreviatura[1:]
            abreviatura = re.sub(u'([Uu]sado )(actualmente |especialmente |frecuentemente )', u'\\1', abreviatura)
            abreviatura = abreviatura.replace(u'filosófico', u'Filosofía').replace(u'comercial', u'Comercio').\
                replace(u'deportivo', u'Deportes').replace(u'religioso', u'Religión').\
                replace(u'Fonética, fonología', u'Fonética').replace(u'Electricidad, electrónica', u'Electricidad')

            # GEOGRAFÍA Y ÁMBITOS
            parte_geografia = re.match(u'((^En ([A-Z]|algunos|muchos|el|la).+, (?=usado))|'
                                       u'(^(Era )?[Uu]sado (más |también )?en ([A-Z]|algunos|muchos|el|las? A).+))',
                                       abreviatura)
            if parte_geografia:
                # Es una etiqueta geográfica del tipo "En Colombia, Cuba y México, usado también...".
                # Extraemos los valores de geografía y los eliminamos de la etiqueta
                # TODO: si tiene parte de geografía, todos los ámbitos y demás abreviaturas se refieren
                # a una segunda acepción alternativa, y no son de esta acepción.
                texto_geografia = parte_geografia.group(0)
                abreviatura = abreviatura[len(texto_geografia):]
                if abreviatura:
                    abreviatura = abreviatura[0].upper() + abreviatura[1:]
                texto_geografia = texto_geografia.replace(u'el panocho murciano', u'Murcia')
                texto_geografia = re.sub(u'((?<=^)|(?<=\s))([Ee]l |[Ll]as? )', u'', texto_geografia)
                texto_geografia = re.sub(u', | y ', u' ', texto_geografia)
                paises = [ab[0].strip()[0].upper() + ab[0].strip()[1:]
                          for ab in re.findall(REGEXP_PAISES, texto_geografia)]
                texto_geografia = re.sub(REGEXP_PAISES, u'', texto_geografia)
                regiones = [ab[0].strip()[0].upper() + ab[0].strip()[1:]
                            for ab in re.findall(REGEXP_REGIONES, texto_geografia)]
                texto_geografia = re.sub(REGEXP_REGIONES, u'', texto_geografia)
                ambitos = [ab[0].strip()[0].upper() + ab[0].strip()[1:]
                           for ab in re.findall(REGEXP_AMBITOS, texto_geografia)]
                texto_geografia = re.sub(REGEXP_AMBITOS, u'', texto_geografia)
                if not re.match(u'(^(Era )?[Uu]sado (más |también )?en)|En', texto_geografia):
                    desconocidas |= {abreviatura + u' -> ' + abreviatura_original}
                if not abreviatura and not (ambitos and (paises or regiones)):
                    # La abreviatura no dice más, y tenemos solo ámbito o solo geografía (o nada), así que se añade esta
                    # información a la acepción principal.
                    # En caso de que la abreviatura diga más cosas o que haya a la vez ámbito y geografía, esos datos
                    # van a una acepción derivada
                    if ambitos:
                        self._datos["ambitos_uso"] = self._datos.setdefault("ambitos_uso", []) + ambitos
                    if paises:
                        self._datos["paises_uso"] = self._datos.setdefault("paises_uso", []) + paises
                    if regiones:
                        self._datos["regiones_uso"] = self._datos.setdefault("regiones_uso", []) + regiones
                    ambitos = []
                    paises = []
                    regiones = []

            # ÁMBITOS
            if re.match(u'^(Era )?([Uu]sado )?(más |también )?[Ee]n (sentido|lenguaje) ', abreviatura):
                abreviatura = re.sub(u'^(Era )?([Uu]sado )?(más |también )?[Ee]n (sentido|lenguaje) ', u'', abreviatura)
                abreviatura = re.sub(u' y (como )?| o |, ', u' ', abreviatura)
                ambitos += [ab[0].strip()[0].upper() + ab[0].strip()[1:]
                            for ab in re.findall(REGEXP_AMBITOS, abreviatura)]
                abreviatura = re.sub(REGEXP_AMBITOS, u'', abreviatura)
                if not abreviatura and not (ambitos and (paises or regiones)):
                    # La abreviatura no es relativa a una región geográfica, ni puede tenerla, así que no hay una
                    # acepción derivada y se aplica a la propia acepción.
                    self._datos["ambitos_uso"] = self._datos.setdefault("ambitos_uso", []) + ambitos
                    ambitos = []

            if re.match(u'^(Era )?[Uu]sado (más |también )?(en |como )(la )?', abreviatura):
                abreviatura_previa = abreviatura
                abreviatura = re.sub(u'^(Era )?[Uu]sado (más |también )?(en |como )(la )?', u'', abreviatura)
                # El split es por "Usado más en la volatería, referido a las aves"
                abreviatura = re.sub(u' y (en )?', u' ', abreviatura).split(u', ')[0].replace(u'jergal', u'jerga')
                ambitos += [ab[0].strip()[0].upper() + ab[0].strip()[1:]
                            for ab in re.findall(REGEXP_AMBITOS, abreviatura, re.IGNORECASE)]
                abreviatura = re.sub(REGEXP_AMBITOS, u'', abreviatura)
                if abreviatura.strip():
                    # Aunque la abreviatura parecía del tipo indicado para ámbito, tiene información morfológica:
                    # "Usado en femenino"
                    abreviatura = abreviatura_previa
                if not abreviatura and not (ambitos and (paises or regiones)):
                    self._datos["ambitos_uso"] = self._datos.setdefault("ambitos_uso", []) + ambitos
                    ambitos = []

            if re.match(u'^(Era )?[Uu]sado (más |también )?en (singular|plural|femenino)', abreviatura):
                # Se dice que se usa más en plural, o singular, o que tienen el mismo significado.
                # No es importante, porque no limita, y el número está ya incluido, o si no, como en
                # anal1, es un era usado que es mejor no tener en Cuenca.
                abreviatura = u''
                # Como habrá capturado la parte geográfica ("En América, usado también en plural con el mismo
                # significado que en singular"), lo quitamos para que no cree una acepción derivada de esto.
                paises = []
                regiones = []

            if re.match(u'^(Era )?[Uu]sado (más |también )?(seguido |ante |antepuesto |con |pospuesto|precedido '
                        u'|repetid[ao])', abreviatura):
                # Hay bastantes abreviaturas de este tipo pero no aportan prácticamente nada "computable". Que si
                # se usa más antepuesto al sustantivo, o con el verbo en subjuntivo o lo que sea, pero lo ignoramos,
                # salvo por un par de abreviaturas con información de ámbitos
                if u'despectiva' in abreviatura:
                    self.append_ambito_uso(u'Despectivo')
                if u'festiva' in abreviatura:
                    self.append_ambito_uso(u'Festivo')
                abreviatura = u''
                # Como habrá capturado la parte geográfica ("En América, usado también antepuesto al verbo en forma
                # conjugada"), lo quitamos para que no cree una acepción derivada de esto.
                paises = []
                regiones = []

            if re.match(u'^En (plural|voces compuestas),', abreviatura):
                # En 3-4 entradas, dice que la forma plural es peyorativa. Lo ignoramos. También, que en voces
                # compuestas, se usa como prefijo ("tras"). Sólo interesa "En plural, usado también como adverbio",
                # para "horror", pero complica el tema.
                abreviatura = u''

            if abreviatura == u'Aplicado a persona':
                # print(self._lema_rae_txt, u'tiene lo de persona')
                self.append_ambito_uso(u'Persona')
                abreviatura = u''

            # CATEGORÍA ALTERNATIVA
            parte_alternativo = re.match(u'^(Era )?[Uu]sado (a veces |más |también |menos |solo )?(como |en |el )',
                                         abreviatura)
            if parte_alternativo:
                # Es la abreviatura típica de una doble categoría/género/tipo verbo...
                if re.match(u'Era usado ', abreviatura):
                    era_usado = True
                    abreviatura = abreviatura[10:]  # Quitamos "Era usado "
                else:
                    era_usado = False
                    abreviatura = abreviatura[6:]  # Quitamos "Usado "
                parte_modificador = re.match(u'a veces |más |también |menos |solo ', abreviatura)
                if parte_modificador:
                    modificador = parte_modificador.group(0)[:-1]  # Quitamos el espacio
                    abreviatura = abreviatura[len(modificador) + 1:]  # Quitamos el modificador
                else:
                    modificador = u''
                abreviatura = re.sub(u'^(como |en |el )', u'', abreviatura)  # Quitamos el "como ..."
                abreviatura = abreviatura.replace(u',', u'').replace(u'la ', u'')

                acepcion_derivada = {}
                # La acepción principal tendrá sus propios valores de ámbito/país/región de uso. Se entiende que la
                # acepción derivada hereda dichos valores salvo que tenga valores propios. Las acepciones derivadas
                # están "incrustadas" en las acepciones principales, y son equivalentes a la estructura _datos.
                if paises:
                    acepcion_derivada["paises_uso"] = paises
                if regiones:
                    acepcion_derivada["regiones_uso"] = regiones
                if ambitos:
                    acepcion_derivada["ambitos_uso"] = ambitos
                if era_usado or self.get_es_desusado() or self.get_es_poco_usado():
                    acepcion_derivada["es_desusado" if era_usado or self.get_es_desusado() else "es_poco_usado"] = True

                keyword = abreviatura.split()[0].lower()
                if keyword == u'sustantivo':  # En las abreviaturas morfológicas, se denomina como "nombre"
                    # Si se nos habla de que es más frecuente en un género/número, no limitamos el otro.
                    if re.findall(u'especialmente en |frecuentemente |generalmente (en )?|y más en ',
                                  abreviatura):
                        abreviatura =\
                            re.sub(u'(especialmente en |frecuentemente |generalmente (en )?|y más en ).*',
                                   u'', abreviatura)
                    acepcion_derivada["categoria"] = SUSTANTIVO
                    if re.search(u'( y era usado)? en plural como taxón', abreviatura):
                        acepcion_derivada["ambitos_uso"] = [u'Plural como taxón']
                        abreviatura = re.sub(u'( y era usado)? en plural como taxón', u'', abreviatura)
                    abreviatura = re.sub(u' (y|o)(( más| a veces) en plural)?', u'', abreviatura)
                    terminos = abreviatura.split()[1:]
                    for termino in terminos:
                        if termino == u'femenino':
                            acepcion_derivada.setdefault("generos_disponibles", []).append(FEMENINO)
                        elif termino == u'masculino':
                            acepcion_derivada.setdefault("generos_disponibles", []).append(MASCULINO)
                        elif termino == u'plural':
                            acepcion_derivada.setdefault("numeros_disponibles", []).append(PLURAL)
                        else:
                            desconocidas |= {abreviatura + u' -> ' + abreviatura_original + u' ¿' + termino + u'?'}
                    if self.get_categoria() != ADJETIVO and "generos_disponibles" not in acepcion_derivada:
                        # Hay algunas onomatopeyas de las que derivan nombres, pero todas, menos "alirón", indican
                        # el género (y en "alirón" es masculino)
                        acepcion_derivada["generos_disponibles"] = [MASCULINO]
                    # Como derivan de adjetivos y onomatopeyas principalmente, no tienen información de género,
                    # pero quizá sí que la tengan de número
                    if "numeros_disponibles" not in acepcion_derivada:
                        acepcion_derivada["numeros_disponibles"] = self.get_numeros_disponibles()
                    if self.get_categoria() == SUSTANTIVO and\
                            (acepcion_derivada["generos_disponibles"] == self.get_generos_disponibles() or
                             (acepcion_derivada["generos_disponibles"][0] in self.get_generos_disponibles() and
                              acepcion_derivada["generos_disponibles"][-1] in self.get_generos_disponibles())) and\
                            (acepcion_derivada["numeros_disponibles"] == self.get_numeros_disponibles() or
                             (acepcion_derivada["numeros_disponibles"][0] in self.get_numeros_disponibles() and
                              acepcion_derivada["numeros_disponibles"][-1] in self.get_numeros_disponibles())):
                        # Hay veces que aparece un nombre y pone un "usado más en masculino" y cosas así, que quizá
                        # podríamos usar para cambiar la etiqueta de uso, pero en realidad nos la suda un poco y lo
                        # que acemos es borrar la acepción derivada.
                        acepcion_derivada = {}
                elif keyword in [u'masculino', u'femenino']:
                    acepcion_derivada["categoria"] = SUSTANTIVO
                    acepcion_derivada["generos_disponibles"] = [MASCULINO if keyword == u'masculino' else FEMENINO]
                    abreviatura = re.sub(u'y (en América como )?', u'', abreviatura)
                    if u'plural como taxón' in abreviatura:  # Para "simio, a"
                        acepcion_derivada.setdefault("ambitos_uso", []).append(u'Plural como taxón')
                        abreviatura = abreviatura.replace(u' como taxón', u'')  # Dejamos el "plural"
                    terminos = abreviatura.split()[1:]
                    for termino in terminos:
                        if termino in [u'masculino', u'femenino']:  # Los hay "masculino y femenino"
                            acepcion_derivada.setdefault("generos_disponibles", []).append(MASCULINO if keyword == MASCULINO else FEMENINO)
                        elif termino == u'plural':
                            acepcion_derivada["numeros_disponibles"] = [PLURAL]
                        else:
                            desconocidas |= {abreviatura + u' -> ' + abreviatura_original + u' ¿' + termino + u'?'}
                    if modificador == u'más':
                        if len(acepcion_derivada["generos_disponibles"]) > 1:
                            # Se dice que se usa un género más en un sitio, y otro más en otro. En concreto, para "tac",
                            # "tanga" y "tiroides": "En España, usado más como masculino y en América como femenino".
                            # Pero la acepción ya dice que es masculino y femenino. Lo dejamos así.
                            acepcion_derivada = {}
                        elif ("paises_uso" not in acepcion_derivada) and ("regiones_uso" not in acepcion_derivada) and \
                                ("ambitos_uso" not in acepcion_derivada):
                            # El género indicado es más usado, y el otro es poco usado.
                            # No hay casos de acepciones desusadas o poco usadas con esta abreviatura.
                            self.remove_genero_disponible(acepcion_derivada["generos_disponibles"][0])
                            self.set_es_poco_usado(True)
                    elif modificador == u'menos':
                        if len(acepcion_derivada["generos_disponibles"]) > 1:
                            acepcion_derivada = {}
                            print(u'joder la leche')
                        elif ("paises_uso" not in acepcion_derivada) and ("regiones_uso" not in acepcion_derivada) and \
                                ("ambitos_uso" not in acepcion_derivada):
                            # El género indicado es poco usado, y el otro es como lo tuviera
                            # No hay casos de acepciones desusadas o poco usadas con esta abreviatura.
                            # Solo para "mancebo, ba" hay una etiqueta en acepción que es adjetivo, que tiene otra
                            # etiqueta de categoría alternativa de sustantivo, sin especificar género
                            if self.get_categoria() == SUSTANTIVO:
                                self.remove_genero_disponible(acepcion_derivada["generos_disponibles"][0])
                                self.set_es_poco_usado(True)
                            else:
                                # En "mancebo" se dice que se usa menos el femenino. Lo ignoramos
                                acepcion_derivada["generos_disponibles"] = [MASCULINO, FEMENINO]
                    if acepcion_derivada and "numeros_disponibles" not in acepcion_derivada:
                        acepcion_derivada["numeros_disponibles"] = self.get_numeros_disponibles()
                elif keyword == u'adjetivo':
                    # Cuando hay una acepción "Usada también como adjetivo", la categoría "propia" es siempre
                    # sustantivo salvo en tres casos que son pronombres: "cual", "esotro" y "estotro".
                    # En estos tres casos debemos meter el tipo, y en los dos últimos casos además tenemos que
                    # etiquetarlo como DETERMINANTE
                    acepcion_derivada["categoria"] = ADJETIVO if self.get_categoria() == SUSTANTIVO or\
                        self.get_tipos()[0] in [CALIFICATIVO, COMPARATIVO] else DETERMINANTE
                    if self.get_categoria() == PRONOMBRE:  # Son todos sustantivos, y tres pronombres
                        # Pasa con "cual", "esotro" y "estotro"
                        acepcion_derivada["tipos"] = self.get_tipos()
                    else:
                        acepcion_derivada["tipos"] = [CALIFICATIVO]
                elif keyword in [u'pronominal', u'transitivo', u'intransitivo', u'impersonal', u'auxiliar']:
                    acepcion_derivada["categoria"] = VERBO
                    acepcion_derivada["conjs"] = self.get_conjs()
                    acepcion_derivada["es_" + keyword] = True
                    # En estos casos, 3797 veces de 3800 es un verbo pronominal, que adquiere la transitividad de su
                    # acepción principal. El resto son poner, seer y eser, que básicamente son implícitamente
                    # intransitivos.
                    if keyword in [u'pronominal', u'impersonal', u'auxiliar']:
                        # Se toma la pronominalidad de la acepción principal. Siempre aparece tras verbos que expresan
                        # explícitamente que son (in)transitivos, o que son copulativos (y por tanto intransitivos).
                        # print(self._lema_rae_txt, u'es un verbo', keyword, u'de segundas:', u'; '.join(acepcion_rae["abrs_morfo"]) + u' (' + str(n_entrada) + u'|' + str(n_acepcion) + u')')
                        if self.get_es_transitivo():
                            acepcion_derivada["es_transitivo"] = self.get_es_transitivo()
                        if self.get_es_intransitivo():
                            acepcion_derivada["es_intransitivo"] = self.get_es_transitivo()
                    if modificador == u'más':
                        if not self.get_es_desusado():
                            self.set_es_poco_usado(True)
                    elif modificador == u'menos':
                        acepcion_derivada["es_poco_usado"] = True
                    if keyword in [u'transitivo', u'intransitivo'] and u'pronominal' in abreviatura:
                        # En "alargar": Usado también como intransitivo y más como pronominal
                        # En "argumentar": Usado también como transitivo y menos como pronominal
                        self._acepciones_derivadas.append(acepcion_derivada)
                        acepcion_derivada = copy.deepcopy(acepcion_derivada)
                        acepcion_derivada["es_pronominal"] = True
                        if u'y más como' in abreviatura:
                            if "es_desusado" not in self._acepciones_derivadas[0]:
                                self._acepciones_derivadas[0]["es_poco_usado"] = True
                        elif u'y menos como' in abreviatura:
                            if not self.get_es_desusado():
                                acepcion_derivada["es_poco_usado"] = True
                    elif keyword == u'pronominal' and u' transitivo' in abreviatura:
                        # En "apechugar" hay "Usado también como pronominal y menos como transitivo"
                        self._acepciones_derivadas.append(acepcion_derivada)
                        acepcion_derivada = copy.deepcopy(acepcion_derivada)
                        acepcion_derivada.pop("es_pronominal")
                        acepcion_derivada.pop("es_intransitivo")
                        acepcion_derivada["es_transitivo"] = True
                        acepcion_derivada["es_poco_usado"] = True  # (... y menos como transitivo...)
                    elif keyword == u'auxiliar' and u'intransitivo' in abreviatura:
                        # En "eser" tenemos: Era usado también como auxiliar e intransitivo
                        self._acepciones_derivadas.append(acepcion_derivada)
                        acepcion_derivada = copy.deepcopy(acepcion_derivada)
                        acepcion_derivada.pop("es_auxiliar")
                        acepcion_derivada["es_intransitivo"] = True
                elif keyword == u'adverbio':
                    acepcion_derivada["categoria"] = ADVERBIO
                elif keyword == u'interjección':
                    acepcion_derivada["categoria"] = INTERJECCION
                elif keyword == u'acusativo':
                    # Es para "le", por el tema del leísmo, que vale también como si fuera "lo". Como ya está metido
                    # como forma átona, y al flexionar pronombres se meten estos valores manualmente, no hace falta.
                    acepcion_derivada = {}
                elif keyword == u'pronombre':
                    # Son adjetivos que tienen también uso como pronombre. Están los numerales y otros.
                    # "entrambos" tiene "Usado también como pronombre indefinido", pero la acepción es adjetivo
                    # indefinido, así que no hace falta procesar términos.
                    acepcion_derivada = copy.deepcopy(self.get_datos())
                    acepcion_derivada["categoria"] = PRONOMBRE
                    # Lo demás queda igual pero quitamos los valores innecesarios
                    for info in ["ambitos_uso", "paises_uso", "regiones_uso", "apocope_txt", "apocope_plural_txt"]:
                        if info in acepcion_derivada:
                            acepcion_derivada.pop(info)
                elif keyword == u'locución':
                    acepcion_derivada["es_locucion"] = True
                    terminos = abreviatura.split()[1:]
                    for termino in terminos:
                        if termino == u'adjetiva':
                            acepcion_derivada["categoria"] = ADJETIVO
                            acepcion_derivada["tipos"] = [CALIFICATIVO]
                        elif termino == u'adverbial':
                            acepcion_derivada["categoria"] = ADVERBIO
                        elif termino == u'sustantiva':
                            acepcion_derivada["categoria"] = SUSTANTIVO
                        elif termino == u'masculina':
                            acepcion_derivada.setdefault("generos_disponibles", []).append(MASCULINO)
                        else:
                            print(u'Esto es malo')
                elif keyword in [u'singular', u'plural']:
                    # Son abreviaturas de tipo "Usado solo en plural". Modificamos los números disponibles.
                    if ambitos or paises or regiones:
                        acepcion_derivada["categoria"] = self.get_categoria()
                        acepcion_derivada["generos_disponibles"] = self.get_generos_disponibles()
                        acepcion_derivada.setdefault("numeros_disponibles", []).append(SINGULAR
                                                                                       if keyword == u'singular'
                                                                                       else PLURAL)
                    else:
                        self.set_numeros_disponibles([SINGULAR if keyword == u'singular' else PLURAL])
                elif keyword in [u'participio', u'imperativo', u'diminutivo', u'aumentativo', u'superlativo']:
                    # Un verbo como meritar, en el que se dice que se usa más en participio, o como en "listo", que
                    # se dice que se usa más en diminutivo. Podríamos hacer algo complejo, pero lo ignoramos sin más
                    acepcion_derivada = {}
                elif keyword in [u'voz', u'formas', u'locuciones', u'primera']:
                    # Usado solo en la voz pasiva, Usado más en formas no conjugadas,
                    # Usado más en primera persona plural,Usado también en locuciones adverbiales
                    acepcion_derivada = {}
                else:
                    if abreviatura:
                        desconocidas |= {abreviatura + u' -> ' + abreviatura_original + u': ' + self._lema_rae_txt}
                    acepcion_derivada = {}
                if acepcion_derivada:
                    if "categoria" not in acepcion_derivada:
                        print(u'No tenemos categoría!!!!', self._lema_rae_txt, abreviatura)
                    self._acepciones_derivadas.append(acepcion_derivada)
                abreviatura = u''
            elif ambitos or paises or regiones:
                # La etiqueta no incluye datos de categorías/géneros/números... alternativos, pero sí de ámbito.
                # Creamos una acepción derivada que sólo se diferenciará en los ámbitos y la geografía de la principal.
                if not ambitos or not (paises or regiones):
                    print(self._lema_rae_txt, u'Houston, problema con las etiquetas:', abreviatura_original)
                acepcion_derivada = copy.deepcopy(self.get_datos())
                if paises:
                    acepcion_derivada["paises_uso"] = paises
                if regiones:
                    acepcion_derivada["regiones_uso"] = regiones
                if ambitos:
                    acepcion_derivada["ambitos_uso"] = ambitos
                self._acepciones_derivadas.append(acepcion_derivada)

            if abreviatura.strip():
                desconocidas |= {abreviatura + u' -> ' + abreviatura_original}
                todas |= {abreviatura}
                print(self._lema_rae_txt, u'tiene una abreviatura extraña (' + abreviatura.strip() + u')')

            ambitos_uso = (self._datos["ambitos_uso"] if "ambitos_uso" in self._datos else []) +\
                [amb for acp in self.get_acepciones_derivadas() if "ambitos_uso" in acp for amb in acp["ambitos_uso"]]
            for ambito_uso in ambitos_uso:
                ambitos_total |= {ambito_uso}
            paises_uso = (self._datos["paises_uso"] if "paises_uso" in self._datos else []) +\
                [amb for acp in self.get_acepciones_derivadas() if "paises_uso" in acp for amb in acp["paises_uso"]]
            for pais_uso in paises_uso:
                paises_total |= {pais_uso}
            regiones_uso = (self._datos["regiones_uso"] if "regiones_uso" in self._datos else []) +\
                [amb for acp in self.get_acepciones_derivadas() if "regiones_uso" in acp for amb in acp["regiones_uso"]]
            for region_uso in regiones_uso:
                regiones_total |= {region_uso}
        if False:
            self._borrame = {"todas": todas,
                             "desconocidas": desconocidas,
                             "paises": paises_total,
                             "regiones": regiones_total,
                             "ambitos": ambitos_total}

    def get_formas_expandidas(self):
        return self._formas_expandidas

    def set_formas_expandidas(self, formas_expandidas):
        self._formas_expandidas = formas_expandidas

    def get_lema_rae_txt(self):
        return self._lema_rae_txt

    def set_lema_rae_txt(self, lema_rae_txt):
        self._lema_rae_txt = lema_rae_txt

    def get_ambitos_uso(self):
        return self._datos["ambitos_uso"]

    def append_ambito_uso(self, ambito_uso):
        self._datos.setdefault("ambitos_uso", []).append(ambito_uso)

    def set_ambitos_uso(self, ambitos_uso):
        self._datos["ambitos_uso"] = ambitos_uso

    def get_acepciones_derivadas(self):
        return self._acepciones_derivadas

    def reset_acepciones_derivadas(self):
        self._acepciones_derivadas = []

    def get_definicion(self):
        return self._definicion

    def get_definicion_post(self):
        return self._definicion_post

    def get_ejemplos(self):
        return self._ejemplos

    def get_ejemplos_post(self):
        return self._ejemplos_post
