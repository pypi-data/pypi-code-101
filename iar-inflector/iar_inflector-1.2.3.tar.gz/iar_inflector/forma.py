#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""
"""

from iar_inflector.acep_consts import VERBO, SUSTANTIVO, ADJETIVO, ADVERBIO, PRONOMBRE, CONJUNCION, PREPOSICION

__author__ = "Iván Arias Rodríguez"
__copyright__ = "Copyright 2017, Iván Arias Rodríguez"
__credits__ = [""]
__license__ = "GPL"  # No estoy seguro
__version__ = "1.0.1"
__maintainer__ = "Iván Arias Rodríguez"
__email__ = "ivan.arias.rodriguez@gmail.com"
__status__ = "Development"  # "Prototype", "Production"


# Clases auxiliares
class Forma:
    u"""

    """

    def __init__(self, etiqueta_eagles, forma_txt=u'', acepcion=None, lema_txt=u'', n_acepcion=-1):
        self._etiqueta_eagles = etiqueta_eagles
        self._categoria = etiqueta_eagles[0]
        if not isinstance(self, FormaInterjeccion):
            self._tipo = etiqueta_eagles[1]
        else:
            self._tipo = "0"
        self._forma_txt = forma_txt
        if acepcion:
            self._lema_txt = acepcion.get_lema_rae_txt()
            self._n_acepcion = acepcion.get_n_acepcion()
        else:
            self._lema_txt = lema_txt if lema_txt else self._forma_txt  # Si no hay valor de lema-> invariable
            self._n_acepcion = n_acepcion
        if not self._forma_txt:
            self._forma_txt = self._lema_txt  # Si no hay valor de forma, se considera invariable

    def get_etiqueta_eagles(self):
        return self._etiqueta_eagles

    def set_etiqueta_eagles(self, etiqueta_eagles):
        self._etiqueta_eagles = etiqueta_eagles

    def get_categoria(self):
        return self._categoria

    def set_categoria(self, categoria):
        self._categoria = categoria

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo):
        self._tipo = tipo

    def get_forma_txt(self):
        return self._forma_txt

    def set_forma_txt(self, forma_txt):
        self._forma_txt = forma_txt

    def get_lema_txt(self):
        return self._lema_txt

    def set_lema_txt(self, lema_txt):
        self._lema_txt = lema_txt

    def get_n_acepcion(self):
        return self._n_acepcion

    def set_n_acepcion(self, n_acepcion):
        self._n_acepcion = n_acepcion

    @staticmethod
    def crea_forma(etiqueta_eagles, forma_txt=u'', acepcion=None, lema_txt=u'', n_acepcion=-1):
        categoria = etiqueta_eagles[0]
        # TODO: Determinantes e interjecciones
        clases = {SUSTANTIVO: FormaSustantivo, ADJETIVO: FormaAdjetivo, VERBO: FormaVerbo,
                  ADVERBIO: FormaAdverbio, PREPOSICION: FormaPreposicion, CONJUNCION: FormaConjuncion,
                  PRONOMBRE: FormaPronombre, "X": Forma}
        if categoria in clases:
            return clases[categoria](etiqueta_eagles, forma_txt=forma_txt, acepcion=acepcion,
                                     lema_txt=lema_txt, n_acepcion=n_acepcion)
        else:
            return Forma(etiqueta_eagles, forma_txt=forma_txt, acepcion=acepcion,
                         lema_txt=lema_txt, n_acepcion=n_acepcion)


class FormaFlexionada(Forma):
    def __init__(self, etiqueta_eagles, forma_txt=u'', acepcion=None, lema_txt=u'', n_acepcion=-1):
        Forma.__init__(self, etiqueta_eagles, forma_txt, acepcion, lema_txt, n_acepcion)
        if isinstance(self, FormaVerbo):
            self._genero = etiqueta_eagles[6]
            self._numero = etiqueta_eagles[5]
        elif isinstance(self, FormaSustantivo) or isinstance(self, FormaPreposicion):
            self._genero = etiqueta_eagles[2]
            self._numero = etiqueta_eagles[3]
        # elif isinstance(self, FormaAdjetivo) or isinstance(self, FormaPronombre) or\
        #     isinstance(self, FormaDeterminante):
        else:
            self._genero = etiqueta_eagles[3]
            self._numero = etiqueta_eagles[4]

    def get_genero(self):
        return self._genero

    def set_genero(self, genero):
        self._genero = genero

    def get_numero(self):
        return self._numero

    def set_numero(self, numero):
        self._numero = numero


class FormaNominal(FormaFlexionada):
    def __init__(self, etiqueta_eagles, forma_txt=u'', acepcion=None, lema_txt=u'', n_acepcion=-1):
        FormaFlexionada.__init__(self, etiqueta_eagles, forma_txt, acepcion, lema_txt, n_acepcion)
        if isinstance(self, FormaSustantivo):
            self._grado = etiqueta_eagles[6]
            self._origen = etiqueta_eagles[7]
        else:  # elif isinstance(self, FormaAdjetivo):
            self._grado = etiqueta_eagles[2]
            self._origen = etiqueta_eagles[5]

    def get_grado(self):
        return self._grado

    def set_grado(self, grado):
        self._grado = grado

    def get_origen(self):
        return self._origen

    def set_origen(self, origen):
        self._origen = origen


class FormaPersonal(FormaFlexionada):
    def __init__(self, etiqueta_eagles, forma_txt=u'', acepcion=None, lema_txt=u'', n_acepcion=-1):
        FormaFlexionada.__init__(self, etiqueta_eagles, forma_txt, acepcion, lema_txt, n_acepcion)
        self._persona = etiqueta_eagles[2]
        if isinstance(self, FormaPronombre):
            self._poseedor = etiqueta_eagles[6]
        elif isinstance(self, FormaDeterminante):
            self._poseedor = etiqueta_eagles[5]
        else:  # elif isinstance(self, FormaVerbo):
            self._poseedor = "0"

    def get_persona(self):
        return self._persona

    def set_persona(self, persona):
        self._persona = persona

    def get_poseedor(self):
        return self._poseedor

    def set_poseedor(self, poseedor):
        self._poseedor = poseedor


# Etiquetas EAGLES (una versión de ellas): http://nlp.lsi.upc.edu/freeling-old/doc/tagsets/tagset-es.html
class FormaAdverbio(Forma):
    def __init__(self, etiqueta_eagles, forma_txt=u'', acepcion=None, lema_txt=u'', n_acepcion=-1):
        Forma.__init__(self, etiqueta_eagles, forma_txt, acepcion, lema_txt, n_acepcion)


class FormaConjuncion(Forma):
    def __init__(self, etiqueta_eagles, forma_txt=u'', acepcion=None, lema_txt=u'', n_acepcion=-1):
        Forma.__init__(self, etiqueta_eagles, forma_txt, acepcion, lema_txt, n_acepcion)


class FormaInterjeccion(Forma):
    def __init__(self, etiqueta_eagles, forma_txt=u'', acepcion=None, lema_txt=u'', n_acepcion=-1):
        Forma.__init__(self, etiqueta_eagles, forma_txt, acepcion, lema_txt, n_acepcion)


class FormaPreposicion(FormaFlexionada):
    def __init__(self, etiqueta_eagles, forma_txt=u'', acepcion=None, lema_txt=u'', n_acepcion=-1):
        Forma.__init__(self, etiqueta_eagles, forma_txt, acepcion, lema_txt, n_acepcion)
        self._forma = etiqueta_eagles[2]

    def get_forma(self):
        return self._forma

    def set_forma(self, forma):
        self._forma = forma


class FormaSustantivo(FormaNominal):
    # Etiqueta EAGLES para nombre: 7 caracteres (en paréntesis campos o valores inventados)
    # 0: Categoría = Nombre
    # 1: Tipo = Común, Propio
    # 2: Género = Masculino, Femenino, Común, Neutro
    # 3: Número = Singular, Plural, iNvariable
    # 4-5: Clasificación semántica = 00, SP (antropónimo), G0 (topónimo), O0 (organización), V0 (otros)
    # 6: Grado = 0, Aumentativo, Diminutivo
    # 7: (Origen) = 0, de Adjetivo, de Verbo, coMpuesto (carácter inventado)
    def __init__(self, etiqueta_eagles, forma_txt=u'', acepcion=None, lema_txt=u'', n_acepcion=-1):
        FormaNominal.__init__(self, etiqueta_eagles, forma_txt, acepcion, lema_txt, n_acepcion)
        self._clase_semantica = etiqueta_eagles[4:6]

    def get_clase_semantica(self):
        return self._clase_semantica

    def set_clase_semantica(self, clase_semantica):
        self._clase_semantica = clase_semantica


class FormaAdjetivo(FormaNominal):
    # Etiqueta EAGLES para adjetivo: 6 caracteres (en paréntesis campos o valores inventados)
    # 0: Categoría = Adjetivo
    # 1: Tipo = Qalificativo, Ordinal, (Cardinal, Gentilicio, superLativo, Posesivo, Demostrativo,
    #    sustaNtivado, F de padecimiento, de Sustantivo, de Verbo)
    # 2: Grado = 0, Comparativo, Superlativo
    # 3: Género = Masculino, Femenino, Común
    # 4: Número = Singular, Plural, iNvariable
    # 5: Función = 0, de Participio (renombrado como Origen, puesto que indica el origen del adjetivo)
    def __init__(self, etiqueta_eagles, forma_txt=u'', acepcion=None, lema_txt=u'', n_acepcion=-1):
        FormaNominal.__init__(self, etiqueta_eagles, forma_txt, acepcion, lema_txt, n_acepcion)


class FormaPronombre(FormaPersonal):
    def __init__(self, etiqueta_eagles, forma_txt=u'', acepcion=None, lema_txt=u'', n_acepcion=-1):
        FormaPersonal.__init__(self, etiqueta_eagles, forma_txt, acepcion, lema_txt, n_acepcion)
        self._caso = etiqueta_eagles[5]
        self._politeness = etiqueta_eagles[7]

    def get_caso(self):
        return self._caso

    def set_caso(self, caso):
        self._caso = caso

    def get_politeness(self):
        return self._politeness

    def set_politenes(self, politeness):
        self._politeness = politeness


class FormaVerbo(FormaPersonal):
    # Etiqueta EAGLES para verbo: 7 caracteres (+ 5 inventados)
    # 0: Categoría = Verbo
    # 1: Tipo = M (principal, modal), Auxiliar ("haber"), Semiauxiliar ("ser", y según mi criterio, "estar")
    # 2: Modo: Indicativo, Subjuntivo, iMperativo, iNfinitivo, Gerundio, Participio
    # 3: Tiempo: 0 (no aplicable), Presente, Imperfecto, Futuro, S (perfecto simple), Condicional
    # 4: Persona: 0 (no aplicable), 1 (primera), 2 (segunda), 3 (tercera)
    # 5: Número = 0 (no aplicable), Singular, Plural
    # 6: Género = 0 (no aplicable), Masculino, Femenino
    # 7: Pronominal = 0 (no), Pronominal (inventado, supuestamente siempre tienen este carácter a 0)
    # 8: Persona (de enclítico de OI): 0 (no aplicable), 1 (primera), 2 (segunda), 3 (tercera)
    # 9: Número (de enclítico de OI): 0 (no aplicable), Singular, Plural
    # 10: Género (de enclítico de OD): 0 (no aplicable), Masculino, Femenino
    # 11: Número (de enclítico de OD): 0 (no aplicable), Singular, Plural
    def __init__(self, etiqueta_eagles, forma_txt=u'', acepcion=None, lema_txt=u'', n_acepcion=-1):
        FormaFlexionada.__init__(self, etiqueta_eagles, forma_txt, acepcion, lema_txt, n_acepcion)
        self._modo = etiqueta_eagles[2]
        self._tiempo = etiqueta_eagles[3]
        self._pronominal = etiqueta_eagles[7]
        self._persona_oi = etiqueta_eagles[8]
        self._numero_oi = etiqueta_eagles[9]
        self._genero_od = etiqueta_eagles[10]
        self._numero_od = etiqueta_eagles[11]

    def get_modo(self):
        return self._modo

    def set_modo(self, modo):
        self._modo = modo

    def get_tiempo(self):
        return self._tiempo

    def set_tiempo(self, tiempo):
        self._tiempo = tiempo

    def get_pronominal(self):
        return self._pronominal

    def set_pronominal(self, pronominal):
        self._pronominal = pronominal

    def get_persona_oi(self):
        return self._persona_oi

    def set_persona_oi(self, persona_oi):
        self._persona_oi = persona_oi

    def get_numero_oi(self):
        return self._numero_oi

    def set_numero_oi(self, numero_oi):
        self._numero_oi = numero_oi

    def get_genero_od(self):
        return self._genero_od

    def set_genero_od(self, genero_od):
        self._genero_od = genero_od

    def get_numero_od(self):
        return self._numero_od

    def set_numero_od(self, numero_od):
        self._numero_od = numero_od


class FormaDeterminante(FormaPersonal):
    def __init__(self, etiqueta_eagles, forma_txt=u'', acepcion=None, lema_txt=u'', n_acepcion=-1):
        FormaPersonal.__init__(self, etiqueta_eagles, forma_txt, acepcion, lema_txt, n_acepcion)
