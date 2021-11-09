#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""
"""

__author__ = "Iván Arias Rodríguez"
__copyright__ = "Copyright 2017, Iván Arias Rodríguez"
__credits__ = [""]
__license__ = "GPL"  # No estoy seguro
__version__ = "1.0.1"
__maintainer__ = "Iván Arias Rodríguez"
__email__ = "ivan.arias.rodriguez@gmail.com"
__status__ = "Development"  # "Prototype", "Production"

# TODO: El tema de las contracciones es muy raro, supongo que hay que cambiarlo
# TODO: el tema de los afijos hay que cambiarlo y además se tiene que usar en el Wikcionario
# TODO: hay etiquetas al final que quizá deban eliminarse.


'''#########################################
# Etiquetas GENERALES de varias categorías #
#########################################'''
''' POR DEFECTO / NO APLICABLE'''
NA = "0"
''' GÉNERO '''
MASCULINO = "M"
FEMENINO = "F"
NEUTRO = "0"  # Sin género asignado, por ejemplo: ello, dello, lo...
AMBIGUO = "C"  # Misma forma para masculino o femenino, por ejemplo: verde, pianista, tú...
''' NÚMERO '''
SINGULAR = "S"
VOS = "V"  # Para verbos en 2ª persona: singular, vos, plural
PLURAL = "P"
INVARIABLE = "N"  # Misma forma para singular o plural, por ejemplo: bilis, se...
''' PERSONA '''
PRIMERA = "1"
SEGUNDA = "2"
TERCERA = "3"
''' SUFIJACIÓN '''
AUMENTATIVO = "A"
DIMINUTIVO = "D"
APOCOPE = "P"
''' USO '''
DESUSADO = "D"
POCO_USADO = "P"


'''################################
# Etiquetas propias de SUSTANTIVO #
################################'''
# Etiqueta EAGLES para nombre: 7 caracteres + 2 inventados
# 0: Categoría = Nombre
# 1: Tipo = Común, Propio
# 2: Género = Masculino, Femenino, Común, 0 (neutro)
# 3: Número = Singular, Plural, iNvariable
# 4-5: Clasificación semántica = 00, SP (antropónimo), G0 (topónimo), O0 (organización), V0 (otros)
# 6: Sufijación (era Grado) = 0, Aumentativo, Diminutivo, aPócope (carácter modificado)
# 7: Origen = 0, de Adjetivo, de Verbo, coMpuesto (carácter inventado)
# 8: Uso = 0 (normal), Desusado, Poco usado (carácter inventado)
SUSTANTIVO = "N"
''' TIPO '''
COMUN = "C"
PROPIO = "P"
''' OTROS TIPOS (usados como tipo en lemario, pero no en el lexicón) '''
COLECTIVO = "L"
''' ORIGEN '''
DE_ADJETIVO = "A"
DE_VERBO = "V"
COMPUESTO = "M"


'''##############################
# Etiquetas propias de ADJETIVO #
##############################'''
##############################################################################################################
# *Se han eliminado los ordinales. En general, todos los adjetivos "gramaticales" se consideran determinantes.
##############################################################################################################
# Etiqueta EAGLES para adjetivo: 6 caracteres + 2 inventados
# 0: Categoría = Adjetivo
# 1: Tipo = Q (calificativo), (eliminado Ordinal). Yo he añadido los siguientes:
#    Gentilicio, N (sustantivado), de Padecimiento, de Sustantivo, de Verbo, Comparativo
# 2: Grado = 0, Comparativo, Superlativo
# 3: Género = Masculino, Femenino, Común, 0 (neutro)
# 4: Número = Singular, Plural, iNvariable
# 5: Función = 0, Participio
# 6: Sufijación = 0, Aumentativo, Diminutivo, aPócope (carácter inventado)
# 7: Uso = 0 (normal), Desusado, Poco usado (carácter inventado)
ADJETIVO = "A"
''' TIPO '''
CALIFICATIVO = "Q"
GENTILICIO = "G"
SUSTANTIVADO = "N"
DE_PADECIMIENTO = "P"
DE_SUSTANTIVO = "S"
# DE_VERBO = "V"
COMPARATIVO = "C"  # Más, menos... (usados como adjetivo)
''' GRADO '''
# COMPARATIVO = "C"
SUPERLATIVO = "S"
''' FUNCIÓN '''
PARTICIPIO = "P"  # Solo se usa en el Wikcionario y en pocos casos. No se borra porque aparece en EAGLES


'''###################################
# Etiquetas propias de DETERMINANTE* #
###################################'''
##############################################################################################################
# *Los determinantes no se tratan como tal en la RAE: allí son siempre adjetivos y a veces también pronombres,
# según el caso. En el Wikcionario el tratamiento es dispar: aparecen a veces como adjetivo y pronombre, a
# veces solo como pronombre... Los artículos aparecen como tal en ambas fuentes.
# El estándar EAGLES etiqueta los determinantes/artículos como determinantes o pronombres. Así que seguimos la
# norma de no meter dentro de los adjetivos a los determinantes (aunque debería ser así) porque es lo que se
# hace en EAGLES y además viene mejor a la hora de hacer un análisis sintáctico de la oración.
##############################################################################################################
# Etiqueta EAGLES para determinante: 6 caracteres + 2 inventados
# 0: Categoría = Determinante
# 1: Tipo = Demostrativo, Posesivo, inTerrogativo, Exclamativo, Indefinido, Artículo determinado.
#    Yo he añadido: Ordinal, cardiNal, U (artículo indeterminado), Relativo, Y (relativo y posesivo)
# 2: Persona = 0 (no aplicable), 1, 2, 3
# 3: Género = Masculino, Femenino, Común, 0 (neutro)
# 4: Número = Singular, Plural, N (impersonal/invariable)
# 5: Poseedor = 0 (no aplicable), Singular, Plural, iNvariable
# 6: Sufijación = 0, aPócope (carácter inventado)
# 7: Uso = 0 (normal), Desusado, Poco usado (carácter inventado)
DETERMINANTE = "D"
''' TIPO '''
DEMOSTRATIVO = "D"
POSESIVO = "P"
INTERROGATIVO = "T"
EXCLAMATIVO = "E"
INDEFINIDO = "I"
ARTICULO_D = "A"  # para el determinado
ORDINAL = "O"
CARDINAL = "N"
ARTICULO_I = "U"  # para el indeterminado
RELATIVO = "R"  # Únicamente "cual", "cuanto" (usados como adjetivo)
RELATIVO_POSESIVO = "Y"  # Solo para "cuyo": adjetivo relativo posesivo -> determinante


'''###############################
# Etiquetas propias de PRONOMBRE #
###############################'''
##############################################################################################################
# *Se han añadido 2 caracteres para tratar mejor los pronombres personales y hacer más fácil el análisis
# sintáctico:
# El carácter Preposicional, indica si dicho pronombre necesita ir precedido de preposición (mí, sí...), si no
# puede llevarla (yo, tú...), si la lleva amalgamada (conmigo...) o si puede o no llevarla ((con) nosotros...)
# El carácter de Reflexividad indica si el pronombre puede hacer referencia a la misma persona que el sujeto.
# Existen formas únicamente reflexivas (sí y se reflexivo), formas nunca reflexivas (yo, contigo...) y formas
# que pueden o no ser reflexivas (me, nosotras).
# Por último, el carácter Polite sólo tiene valor distinto de 0 para usted/ustedes, pero también para el vos
# de segunda persona del plural: vos sabéis bien que os amo.
# Así pues, un pronombre puede:
# - Ser sujeto sii su caso es Nominativo.
# - Ser CD sii Caso == Acusativo o Reflexividad != 0 (o si es "ello")
# - Ser CI sii Caso == Dativo, o Reflexividad == Indistinto o Preposición == Preposicional.
# - Ser CC sii Preposicional != 0
# Los datos de etiquetado aparecen en el archivo pronombres personales.xlsx
##############################################################################################################
# Etiqueta EAGLES para pronombre: 10 caracteres (1 carácter eliminado, 3 caracteres añadido)
# 0: Categoría = Pronombre
# 1: Tipo = Personal, Demostrativo, Indefinido, inTerrogativo, Relativo, Exclamativo (eliminado Posesivo (X)).
#    Yo he añadido: cardiNal, Comparativo
# 2: Persona = 1, 2, 3
# 3: Género = Masculino, Femenino, Común, 0 (neutro)
# 4: Número = Singular, Plural, N (impersonal/invariable)
# 5: Caso = Nominativo, Acusativo, Dativo, Oblicuo, 0 (no es pronombre personal)
# -: (eliminado Poseedor = Singular, Plural)
# 6: Preposicionalidad = 0 (no preposicional), Preposicional, Amalgamado, Indistinto
# 7: Politeness = Polite (para usted/ustedes/vos), 0 (resto)
# 8: Reflexividad = 0 (no reflexivo), Reflexivo, Indistinto
# 9: Uso = 0 (normal), Desusado, Poco usado (carácter inventado)
PRONOMBRE = "P"
''' TIPO '''
PERSONAL = "P"
# DEMOSTRATIVO = "D"
# INDEFINIDO = "I"
# INTERROGATIVO = "T"
# RELATIVO = "R"
# EXCLAMATIVO = "E"
# CARDINAL = "N"  # OJO: los ordinales (5º) son adjetivos y los cardinales determinantes/pronombres (5)
# COMPARATIVO = "C"  # Tanto...
''' CASO '''
NOMINATIVO = "N"
ACUSATIVO = "A"
DATIVO = "D"
OBLICUO = "O"
''' PREPOSICIONALIDAD '''
PREPOSICIONAL = "P"
AMALGAMADO = "A"
INDISTINTO = "I"
''' POLITENESS '''
POLITE = "P"
''' REFLEXIVIDAD '''
REFLEXIVO = "R"
# INDISTINTO = "I"


'''###########################
# Etiquetas propias de VERBO #
###########################'''
########################################################################################################################
# En el estándar EAGLES solo "haber" tiene tipo Auxiliar (también Principal (M), en existenciales: hay cuatro gatos), y solo
# "ser" tiene tipo Semiauxiliar. Nosotros, hacemos unos cambios:
# - También etiquetamos "haber" como principal o como auxiliar. Esto no cambia.
# - "ser" puede ser Semiauxiliar (uso copulativo), Auxiliar (uso pasivo) o Principal (M) (ocurrir, pertenecer...: Son las dos,
#   eso es de Juan).
# - "estar" y "parecer" pueden ser Semiauxiliar (copulativo) o Principal.
# y existen otros verbos no principales:
# - "seer" y "eser" puede ser Semiauxiliares (copulativos) o Principales. Ambos están desusados.
# Sobre los caracteres 7-11 que indican los enclíticos:
# - Si el verbo no está marcado como transitivo:
#   - Los caracteres 10-11 son 00 (no hay clíticos l[oa]s?).
#   - Los caracteres 8-9 marcan la persona y nº del oi.
#   - El carácter 7 marca si hay clítico reflexivo. Si lo hay, siempre es de la misma persona y número que la forma
#     imperativa, o "se" en las formas impersonales. Funciones:
#       - Si es el único clítico, puede ser de od u oi ("lávate" vs "lavarse las manos").
#       - Si existe clítico de oi, entonces no tiene función ("antojárseles", "discúlpatenos", "hudírsenos").
# - Si el verbo está marcado como transitivo:
#   - Los caracteres 10-11 marcan la persona y nº del od.
#   - Los caracteres 8-9 marcan la persona y nº del oi cuando es de 3ª (le/les/se), o indistintamente el od/oi si
#     es de 1ª o 2ª ("quiere entregarme/te/nos/os" vs. quiere "entregarme/te/nos/os una carta"). Se marca como etiqueta
#     de oi pero como vemos, podría ser od.
#   - Los caracteres 8-9 marcan:
#       - La persona y nº del oi cuando es de 3ª (le/les/se) o cuando existe od ("dármelas", "cuéntamelas").
#       - La persona y nº del od/oi cuando es de 1ª o 2ª y no hay od: "muérete", "lávate"
#
#
# , o indistintamente el od/oi si
#     es de 1ª o 2ª ("quiere entregarme/te/nos/os" vs. quiere "entregarme/te/nos/os una carta"). Se marca como etiqueta
#     de oi pero como vemos, podría ser od.
#   - El carácter 7 marca si hay clítico reflexivo. Si lo hay, siempre es de la misma persona y número que la forma
#     imperativa, o "se" en las formas impersonales. Funciones:
#       - Si es el único clítico, puede ser de od u oi ("lávate" vs "lavarse las manos").
#       - Si existe clítico de od, entonces es siempre oi ("lávatelas", "lavárselas").
#       - Si existe clítico de oi, pero no de od, entonces es od si el verbo es transitivo (ESO CREO),
#         o no tiene función si es intransitivo ("antojárseles", "discúlpatenos", "agárresenos").
#       - Si existe clítico de od, pero no de oi, entonces es oi ("comérselo", "apréndetelo", "húndamelos") (ESO CREO)
#       - Si existen los tres clíticos, es un dativo ético: "cómetemela", "cuídatemela".
#
#   Además si el carácter 7 es Pronominal, entonces se tiene la marca de pronominal para la persona que indiquen los
#   caracteres 4-5 (o "se" si es infinitivo o gerundio): diríjasenos
#       - Si el carácter 7 es no Pronominal,
#   de pronominal
########################################################################################################################
# Etiqueta EAGLES para verbo: 7 caracteres (+ 9 inventados)
# 0: Categoría = Verbo
# 1: Tipo = M (principal), Auxiliar ("haber", "ser"), Semiauxiliar/copulativo
#    (ser, eser, seer, estar, parecer) (carácter inventado)
# 2: Modo: Indicativo, Subjuntivo, iMperativo, iNfinitivo, Gerundio, Participio
# 3: Tiempo: 0 (no aplicable), Presente, Imperfecto, Futuro, S (perfecto simple), Condicional
# 4: Persona: 0 (no aplicable), 1 (primera), 2 (segunda), 3 (tercera)
# 5: Número = 0 (no aplicable), Singular, Plural, Voseo
# 6: Género = 0 (no aplicable), Masculino, Femenino
# 7: Pronominal = 0 (no), Pronominal (tiene clíticos pegados) (carácter inventado)
# 8: Persona (de enclítico de OI/OD): 0 (no aplicable), 1 (1ª), 2 (2ª), 3 (3ª) (carácter inventado)
# 9: Número (de enclítico de OI/OD): 0 (no aplicable), Singular, Plural, iNvariable (carácter inventado)
# 10: Género (de enclítico de OD): 0 (no aplicable), Masculino, Femenino (carácter inventado)
# 11: Número (de enclítico de OD): 0 (no aplicable), Singular, Plural (carácter inventado)
# 12: Transitividad: 0, Transitivo, Intransitivo (carácter inventado)
# 13: Impersonalidad: 0 (personal), Impersonal (carácter inventado)
# 14: Pronominalidad: 0 (no pronominal), Pronominal (carácter inventado)
# 15: Uso = 0 (normal), Desusado, Poco usado (carácter inventado)
VERBO = "V"
''' TIPO '''
PRINCIPAL = "M"  # Verbo "normal"
AUXILIAR = "A"
COPULATIVO = "S"  # Semiauxiliar/copulativo
''' MODO '''
INFINITIVO = "N"
GERUNDIO = "G"
# PARTICIPIO = "P"
INDICATIVO = "I"
SUBJUNTIVO = "S"
IMPERATIVO = "M"
''' TIEMPO '''
PRESENTE = "P"
IMPERFECTO = "I"
FUTURO = "F"
PERFECTO = "S"
CONDICIONAL = "C"
''' TRANSITIVIDAD '''
TRANSITIVO = "T"
INTRANSITIVO = "I"
''' IMPERSONALIDAD '''
IMPERSONAL = "I"
''' PRONOMINALIDAD '''
PRONOMINAL = "P"


'''##############################
# Etiquetas propias de ADVERBIO #
##############################'''
# Etiqueta EAGLES para adverbio: 2 caracteres + 2 inventados
# 0: Categoría = R (adverbio)
# 1: Tipo = General, Negativo. Además yo he añadido: Comparativo, Afirmativo, Q (cuantitativo), dUbitativo,
#           Locativo, Modal, Ordinal, temPoral, inTerrogativo, Relativo, Demostrativo, Indefinido,
#           Exclamativo, distriButivo
# 2: Grado = 0 (positivo), Comparativo, Superlativo (carácter inventado)
# 3: Uso = 0 (normal), Desusado, Poco usado (carácter inventado)
# Además, EAGLES reserva el tipo Negativo únicamente para "no". Yo también lo pongo en: apenas, tampoco y pero
# (hay un "pero" que es adverbio, usado un poco a la italiana, con significado de "pese a lo precedente").
ADVERBIO = "R"
''' TIPO '''
GENERAL = "G"
NEGATIVO = "N"
# COMPARATIVO = "C"  # Mayormente, mejor, peor
# SUPERLATIVO = "S"  # Pésimamente
AFIRMATIVO = "A"
CUANTITATIVO = "Q"
DUBITATIVO = "U"
LOCATIVO = "L"
# PRINCIPAL = "M"
# ORDINAL = "O"
TEMPORAL = "P"
# INTERROGATIVO = "T"
# RELATIVO = "R"
# DEMOSTRATIVO = "D"
# INDEFINIDO = "I"
# EXCLAMATIVO = "E"
DISTRIBUTIVO = "B"


'''################################
# Etiquetas propias de CONJUNCIÓN #
################################'''
# Etiqueta EAGLES para conjuncion: 2 caracteres + 2 inventados
# 0: Categoría = Conjución
# 1: Tipo = 0 (desconocido), Coordinada, Subordinada
# 2: Subtipo (inventado) = 0, -coordinadas- Y (copulativa), O (disyuntiva), Distributiva, Adversativa, Explicativa,
#                             -subordinadas- conSecutiva, Causal (X), Final, conZesiva, temPoral, Condicional, Ilativa
# 3: Uso = 0 (normal), Desusado, Poco usado (carácter inventado)
CONJUNCION = "C"
''' TIPO '''
COORDINADA = "C"
SUBORDINADA = "S"
''' SUBTIPO '''
COPULATIVA = "Y"
DISYUNTIVA = "O"
DISTRIBUTIVA = "D"
ADVERSATIVA = "A"
EXPLICATIVA = "E"
CONSECUTIVA = "S"
CAUSAL = "X"
FINAL = "F"
CONCESIVA = "Z"
# TEMPORAL = "P"
# CONDICIONAL = "C"
ILATIVA = "I"


'''#################################
# Etiquetas propias de PREPOSICIÓN #
#################################'''
# Etiqueta EAGLES para preposiciones: 5 caracteres + 1 inventado (1 carácter eliminado, 1 carácter añadido)
# 0: Categoria = S (adposición)
# -: (eliminado Tipo = Preposición)
# 1: Tipo (era Forma) = Simple, Contraída
# 2: Género = 0 (no aplicable), Masculino (para "al" y "del"), Femenino (para desusadas como desas)
# 3: Número = 0 (no aplicable), Singular, Plural (para desusadas como dentrambos)
# 4: Uso = 0 (normal), Desusado, Poco usado (carácter inventado)
PREPOSICION = "S"
''' TIPO '''
SIMPLE = "S"
CONTRAIDA = "C"


'''############################
# Etiquetas propias de NÚMERO #
############################'''
# Etiqueta EAGLES para número: 1 carácter (1 carácter eliminado, 1 carácter añadido)
# 0: Categoria = Z (número)
# -: (eliminado Tipo = partitivo, moneda, porcentaje, unidad)
# 1: Uso = 0 (normal), Desusado, Poco usado (carácter inventado)
NUMERO = "Z"


'''############################
# Etiquetas propias de AFIJOS #
############################'''
# Etiqueta EAGLES para sufijo: 3 caracteres (categoría inventada)
# 0: Categoría = - (afijo)
# 1: Tipo = > (prefijo), < (sufijo)
# 2: Subtipo = sufijo Flexivo, Elemento compositivo, 0
# 3: Género = Masculino, Femenino, Común, 0 (neutro)
# 4: Número = Singular, Plural, iNvariable
# 5: Uso = 0 (normal), Desusado, Poco usado
AFIJO = "-"
''' TIPO '''
PREFIJO = ">"
SUFIJO = "<"
''' SUBTIPO '''
FLEXIVO = "F"  # Para los sufijos flexivos
ELEMENTO_COMPOSITIVO = "E"


'''##########################################
# Etiquetas propias de SIGNOS DE PUNTUACIÓN #
##########################################'''
# Etiqueta EAGLES para signo de puntuación: 3 caracteres
##############################################################################################################
# Hay muchas diferencias: https://talp-upc.gitbooks.io/freeling-4-0-user-manual/content/tagsets/tagset-es.html
##############################################################################################################
# 0: Categoría = F (signo de puntuación)
# 1: Tipo = Dos puntos, Coma, Llave, s (etc), Admiración, Guion, Z (puntuación), paréNtesis, Tanto por
#           ciento, Punto, Interrogación, R (comillas), X (punto y coma), H (barra), K (corchete)
# 2: Posición = Apertura, Cierre, 0 (sin variantes)
# 3: Uso = 0 (normal)
SIGNO = "F"
''' TIPO '''
DOS_PUNTOS = "D"
COMA = "C"
LLAVE = "L"
ETC = "S"
ADMIRACION = "A"
GUION = "G"
PUNTUACION = "Z"  # Otro signo desconocido.
PARENTESIS = "N"
TANTO_POR_CIENTO = "T"
PUNTO = "P"
INTERROGACION = "I"
COMILLAS = "R"
PUNTO_Y_COMA = "X"
BARRA = "H"
CORCHETE = "K"
PUNTOS_SUSPENSIVOS = "V"
COMPARADOR = "M"
COMILLA = "Y"
''' POSICIÓN '''
APERTURA = "A"
CIERRE = "C"


'''#########################################
# Etiquetas propias de FORMAS DESCONOCIDAS #
#########################################'''
# TODO: Esto ha cambiado
# Etiqueta EAGLES para formas desconocidas: 2 caracteres (categoría inventada)
##############################################################################################################
# 0: Categoría = ? (forma desconocida)
# 1: Tipo = Número, Mayúscula inicial, Común
# 2: Uso = 0 (normal)
DESCONOCIDA = "?"
''' TIPO '''
# NUMERO = "N"  # Cualquier string que se reconozca como número.
# PROPIO = "P"  # Cualquier forma que comience por mayúscula y resto en minúscula (¿nombre propio?)
# SIGLA = "G"  # Cualquier forma que comience por mayúscula y tenga alguna otra mayúscula (¿acronimo?)
# COMUN = "C"  # Cualquier forma no numérica enteramente escrita con minúsculas


'''######################################
# Etiquetas propias de OTRAS CATEGORÍAS #
######################################'''
INTERJECCION = "I"
ONOMATOPEYA = "O"
EXPRESION = "X"  # Son básicamente locuciones (o no) latinas: mea culpa, requiescat in pace, vide...
ABREVIATURA = "B"
SIGLA = "G"  # Salen en el Wikcionario. Algunas salen en la RAE (ADN, ADSL) como nombres (casi siempre masculinos)
SIMBOLO = "M"  # Muchas veces son abreviaturas de unidades de media y cosas así


'''###########################################
# Etiquetas propias de CATEGORÍAS AUXILIARES #
###########################################'''
FORMA = "F"


CATEGORIAS_A_TXT = {SUSTANTIVO: u'Sustantivo', ADJETIVO: u'Adjetivo', DETERMINANTE: u'Determinante',
                    PRONOMBRE: u'Pronombre', VERBO: u'Verbo', ADVERBIO: u'Adverbio',
                    PREPOSICION: u'Preposición', CONJUNCION: u'Conjunción', INTERJECCION: u'Interjección',
                    EXPRESION: u'Expresión', ONOMATOPEYA: u'Onomatopeya', AFIJO: u'Afijo',
                    PREFIJO: u'Prefijo', SUFIJO: u'Sufijo', ELEMENTO_COMPOSITIVO: u'Afijoide',
                    SIGNO: u'Signo', DESCONOCIDA: u'Desconocida'}

TIPOS_VERBO_A_TXT = {PRINCIPAL: u'Principal', COPULATIVO: u'Copulativo', AUXILIAR: u'Auxiliar'}

# INVESTIGA ESTAS ETIQUETAS. Seguramente hay que borrarlas o algo así.
ATONO = "A"
DETERMINADO = "D"
INDETERMINADO = "I"


