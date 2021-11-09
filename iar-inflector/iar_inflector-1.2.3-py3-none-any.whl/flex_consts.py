#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""

"""

from iar_inflector.acep_consts import VERBO, PRINCIPAL, INFINITIVO, GERUNDIO, PARTICIPIO,\
    INDICATIVO, SUBJUNTIVO, IMPERATIVO, PRESENTE, IMPERFECTO, FUTURO, PERFECTO, CONDICIONAL,\
    NA, PRONOMINAL, SINGULAR, PLURAL, MASCULINO, FEMENINO, PRIMERA, SEGUNDA, VOS, TERCERA

__author__ = "Iván Arias Rodríguez"
__copyright__ = "Copyright 2017, Iván Arias Rodríguez"
__credits__ = [""]
__license__ = "GPL"  # No estoy seguro
__version__ = "1.0.1"
__maintainer__ = "Iván Arias Rodríguez"
__email__ = "ivan.arias.rodriguez@gmail.com"
__status__ = "Development"  # "Prototype", "Production"


NOMBRES_TIEMPOS = {PRESENTE: u'Presente',
                   IMPERFECTO: u'Pretérito imperfecto',
                   PERFECTO: u'Pretérito perfecto',
                   FUTURO: u'Futuro',
                   CONDICIONAL: u'Condicional'}
NOMBRES_MODOS = {INDICATIVO: u'Indicativo',
                 SUBJUNTIVO: u'Subjuntivo',
                 IMPERATIVO: u'Imperativo'}
CODIGOS_PERSONAS = [PRIMERA + SINGULAR, SEGUNDA + SINGULAR, SEGUNDA + VOS, TERCERA + SINGULAR,
                    PRIMERA + PLURAL, SEGUNDA + PLURAL, TERCERA + PLURAL]
NOMBRES_PERSONAS = {PRIMERA + SINGULAR: u'Yo',
                    SEGUNDA + SINGULAR: u'Tú',
                    SEGUNDA + VOS: u'Vos',
                    TERCERA + SINGULAR: u'Él/usted',
                    PRIMERA + PLURAL: u'Nosotros',
                    SEGUNDA + PLURAL: u'Vosotros',
                    TERCERA + PLURAL: u'Ellos/utds.'}

PRONOMINALES = {NA: u'', PRONOMINAL: u'se'}
REFLEXIVOS = {PRIMERA + SINGULAR: u'me',
              SEGUNDA + SINGULAR: u'te',
              SEGUNDA + VOS: u'te',
              TERCERA + SINGULAR: u'se',
              PRIMERA + PLURAL: u'nos',
              SEGUNDA + PLURAL: u'os',
              TERCERA + PLURAL: u'se'}
OBJETOS_INDIRECTOS = {NA + NA: u'',
                      PRIMERA + SINGULAR: u'me',
                      SEGUNDA + SINGULAR: u'te',
                      TERCERA + SINGULAR: u'le',
                      PRIMERA + PLURAL: u'nos',
                      SEGUNDA + PLURAL: u'os',
                      TERCERA + PLURAL: u'les'}
OBJETOS_DIRECTOS = {NA + NA: u'',
                    MASCULINO + SINGULAR: u'lo',
                    MASCULINO + PLURAL: u'los',
                    FEMENINO + SINGULAR: u'la',
                    FEMENINO + PLURAL: u'las'}

# Partiendo de un nexo de vocal abierta, da el nexo para vocal cerrada
NEXOS_IE = {u'': u'', u'c': u'qu', u'g': u'gu', u'gu': u'gü', u'z': u'c'}
# Partiendo de un nexo de vocal cerrada, da el nexo para vocal abierta
NEXOS_AOU = {u'': u'', u'c': u'z', u'g': u'j', u'gu': u'g', u'gü': u'gu', u'qu': u'c'}

# https://es.wikipedia.org/wiki/Conjunci%C3%B3n_(gram%C3%A1tica)
# Hay muchísimas que están compuestas por varias palabras, y no sé qué hacer con ellas.
# Coordinadas
CONJS_COPULATIVAS = [u'y', u'e', u'ni', u'que']
CONJS_DISYUNTIVAS = [u'o', u'u']
CONJS_DISTRIBUTIVAS = [u'bien', u'sea', u'ya', u'ora']
CONJS_ADVERSATIVAS = [u'mas', u'pero', u'aunque', u'sino', u'empero', u'sin embargo', u'no obstante']
CONJS_EXPLICATIVAS = []
CONJS_COORDINADAS = CONJS_COPULATIVAS + CONJS_DISYUNTIVAS + CONJS_DISTRIBUTIVAS + CONJS_ADVERSATIVAS + \
                    CONJS_EXPLICATIVAS
# Subordinadas
CONJS_CONSECUTIVAS = [u'conque', u'luego']
CONJS_CAUSALES = [u'porque', u'como', u'pues']
CONJS_FINALES = []
CONJS_CONCESIVAS = [u'aunque']
CONJS_TEMPORALES = []
CONJS_CONDICIONALES = [u'si', u'como', u'cuando']
CONJS_SUBORDINADAS = CONJS_CONSECUTIVAS + CONJS_CAUSALES + CONJS_FINALES + CONJS_CONCESIVAS +\
                     CONJS_TEMPORALES + CONJS_CONDICIONALES

# Se usa el estándar de EAGLES para español: http://nlp.lsi.upc.edu/freeling-old/doc/tagsets/tagset-es.html
# He añadido algunas cosas... Debería hacer un compendio aquí arriba de esos cambios.
# - Los nombres propios pueden tener género (¿y número?)
# - Hay muchos más tipos de adjetivos
# - Tiempos verbales con reflexivo llevan una P extra al final. Además están las marcas de formas enclíticas
INF = VERBO + PRINCIPAL + INFINITIVO + (NA * 9)  # VMN000000000
INF_P = INF[:7] + PRONOMINAL + (NA * 4)  # VMN0000P0000
GER = VERBO + PRINCIPAL + GERUNDIO + (NA * 9)  # VMG000000000
GER_P = GER[:7] + PRONOMINAL + (NA * 4)  # VMG0000P0000
PAR_SM = VERBO + PRINCIPAL + PARTICIPIO + (NA * 2) + SINGULAR + MASCULINO + (NA * 5)  # VMP00SM00000
PAR_SF = VERBO + PRINCIPAL + PARTICIPIO + (NA * 2) + SINGULAR + FEMENINO + (NA * 5)  # VMP00SF00000
PAR_PM = VERBO + PRINCIPAL + PARTICIPIO + (NA * 2) + PLURAL + MASCULINO + (NA * 5)  # VMP00PM00000
PAR_PF = VERBO + PRINCIPAL + PARTICIPIO + (NA * 2) + PLURAL + FEMENINO + (NA * 5)  # VMP00PF00000

IP1S = VERBO + PRINCIPAL + INDICATIVO + PRESENTE + PRIMERA + SINGULAR + (NA * 6)  # VMIP1S000000
IP2S = VERBO + PRINCIPAL + INDICATIVO + PRESENTE + SEGUNDA + SINGULAR + (NA * 6)  # VMIP2S000000
IP2V = VERBO + PRINCIPAL + INDICATIVO + PRESENTE + SEGUNDA + VOS + (NA * 6)  # VMIP2V000000
IP3S = VERBO + PRINCIPAL + INDICATIVO + PRESENTE + TERCERA + SINGULAR + (NA * 6)  # VMIP3S000000
IP1P = VERBO + PRINCIPAL + INDICATIVO + PRESENTE + PRIMERA + PLURAL + (NA * 6)  # VMIP1P000000
IP2P = VERBO + PRINCIPAL + INDICATIVO + PRESENTE + SEGUNDA + PLURAL + (NA * 6)  # VMIP2P000000
IP3P = VERBO + PRINCIPAL + INDICATIVO + PRESENTE + TERCERA + PLURAL + (NA * 6)  # VMIP3P000000

II1S = VERBO + PRINCIPAL + INDICATIVO + IMPERFECTO + PRIMERA + SINGULAR + (NA * 6)  # VMII1S000000
II2S = VERBO + PRINCIPAL + INDICATIVO + IMPERFECTO + SEGUNDA + SINGULAR + (NA * 6)  # VMII2S000000
II3S = VERBO + PRINCIPAL + INDICATIVO + IMPERFECTO + TERCERA + SINGULAR + (NA * 6)  # VMII3S000000
II1P = VERBO + PRINCIPAL + INDICATIVO + IMPERFECTO + PRIMERA + PLURAL + (NA * 6)  # VMII1P000000
II2P = VERBO + PRINCIPAL + INDICATIVO + IMPERFECTO + SEGUNDA + PLURAL + (NA * 6)  # VMII2P000000
II3P = VERBO + PRINCIPAL + INDICATIVO + IMPERFECTO + TERCERA + PLURAL + (NA * 6)  # VMII3P000000

IS1S = VERBO + PRINCIPAL + INDICATIVO + PERFECTO + PRIMERA + SINGULAR + (NA * 6)  # VMIS1S000000
IS2S = VERBO + PRINCIPAL + INDICATIVO + PERFECTO + SEGUNDA + SINGULAR + (NA * 6)  # VMIS2S000000
IS3S = VERBO + PRINCIPAL + INDICATIVO + PERFECTO + TERCERA + SINGULAR + (NA * 6)  # VMIS3S000000
IS1P = VERBO + PRINCIPAL + INDICATIVO + PERFECTO + PRIMERA + PLURAL + (NA * 6)  # VMIS1P000000
IS2P = VERBO + PRINCIPAL + INDICATIVO + PERFECTO + SEGUNDA + PLURAL + (NA * 6)  # VMIS2P000000
IS3P = VERBO + PRINCIPAL + INDICATIVO + PERFECTO + TERCERA + PLURAL + (NA * 6)  # VMIS3P000000

IF1S = VERBO + PRINCIPAL + INDICATIVO + FUTURO + PRIMERA + SINGULAR + (NA * 6)  # VMIF1S000000
IF2S = VERBO + PRINCIPAL + INDICATIVO + FUTURO + SEGUNDA + SINGULAR + (NA * 6)  # VMIF2S000000
IF3S = VERBO + PRINCIPAL + INDICATIVO + FUTURO + TERCERA + SINGULAR + (NA * 6)  # VMIF3S000000
IF1P = VERBO + PRINCIPAL + INDICATIVO + FUTURO + PRIMERA + PLURAL + (NA * 6)  # VMIF1P000000
IF2P = VERBO + PRINCIPAL + INDICATIVO + FUTURO + SEGUNDA + PLURAL + (NA * 6)  # VMIF2P000000
IF3P = VERBO + PRINCIPAL + INDICATIVO + FUTURO + TERCERA + PLURAL + (NA * 6)  # VMIF3P000000

IC1S = VERBO + PRINCIPAL + INDICATIVO + CONDICIONAL + PRIMERA + SINGULAR + (NA * 6)  # VMIC1S000000
IC2S = VERBO + PRINCIPAL + INDICATIVO + CONDICIONAL + SEGUNDA + SINGULAR + (NA * 6)  # VMIC2S000000
IC3S = VERBO + PRINCIPAL + INDICATIVO + CONDICIONAL + TERCERA + SINGULAR + (NA * 6)  # VMIC3S000000
IC1P = VERBO + PRINCIPAL + INDICATIVO + CONDICIONAL + PRIMERA + PLURAL + (NA * 6)  # VMIC1P000000
IC2P = VERBO + PRINCIPAL + INDICATIVO + CONDICIONAL + SEGUNDA + PLURAL + (NA * 6)  # VMIC2P000000
IC3P = VERBO + PRINCIPAL + INDICATIVO + CONDICIONAL + TERCERA + PLURAL + (NA * 6)  # VMIC3P000000

SP1S = VERBO + PRINCIPAL + SUBJUNTIVO + PRESENTE + PRIMERA + SINGULAR + (NA * 6)  # VMSP1S000000
SP2S = VERBO + PRINCIPAL + SUBJUNTIVO + PRESENTE + SEGUNDA + SINGULAR + (NA * 6)  # VMSP2S000000
SP2V = VERBO + PRINCIPAL + SUBJUNTIVO + PRESENTE + SEGUNDA + VOS + (NA * 6)  # VMSP2V000000
SP3S = VERBO + PRINCIPAL + SUBJUNTIVO + PRESENTE + TERCERA + SINGULAR + (NA * 6)  # VMSP3S000000
SP1P = VERBO + PRINCIPAL + SUBJUNTIVO + PRESENTE + PRIMERA + PLURAL + (NA * 6)  # VMSP1P000000
SP2P = VERBO + PRINCIPAL + SUBJUNTIVO + PRESENTE + SEGUNDA + PLURAL + (NA * 6)  # VMSP2P000000
SP3P = VERBO + PRINCIPAL + SUBJUNTIVO + PRESENTE + TERCERA + PLURAL + (NA * 6)  # VMSP3P000000

SI1S = VERBO + PRINCIPAL + SUBJUNTIVO + IMPERFECTO + PRIMERA + SINGULAR + (NA * 6)  # VMSI1S000000
SI2S = VERBO + PRINCIPAL + SUBJUNTIVO + IMPERFECTO + SEGUNDA + SINGULAR + (NA * 6)  # VMSI2S000000
SI3S = VERBO + PRINCIPAL + SUBJUNTIVO + IMPERFECTO + TERCERA + SINGULAR + (NA * 6)  # VMSI3S000000
SI1P = VERBO + PRINCIPAL + SUBJUNTIVO + IMPERFECTO + PRIMERA + PLURAL + (NA * 6)  # VMSI1P000000
SI2P = VERBO + PRINCIPAL + SUBJUNTIVO + IMPERFECTO + SEGUNDA + PLURAL + (NA * 6)  # VMSI2P000000
SI3P = VERBO + PRINCIPAL + SUBJUNTIVO + IMPERFECTO + TERCERA + PLURAL + (NA * 6)  # VMSI3P000000

SF1S = VERBO + PRINCIPAL + SUBJUNTIVO + FUTURO + PRIMERA + SINGULAR + (NA * 6)  # VMSF1S000000
SF2S = VERBO + PRINCIPAL + SUBJUNTIVO + FUTURO + SEGUNDA + SINGULAR + (NA * 6)  # VMSF2S000000
SF3S = VERBO + PRINCIPAL + SUBJUNTIVO + FUTURO + TERCERA + SINGULAR + (NA * 6)  # VMSF3S000000
SF1P = VERBO + PRINCIPAL + SUBJUNTIVO + FUTURO + PRIMERA + PLURAL + (NA * 6)  # VMSF1P000000
SF2P = VERBO + PRINCIPAL + SUBJUNTIVO + FUTURO + SEGUNDA + PLURAL + (NA * 6)  # VMSF2P000000
SF3P = VERBO + PRINCIPAL + SUBJUNTIVO + FUTURO + TERCERA + PLURAL + (NA * 6)  # VMSF3P000000

MP2S = VERBO + PRINCIPAL + IMPERATIVO + PRESENTE + SEGUNDA + SINGULAR + (NA * 6)  # VMMP2S000000
MP2V = VERBO + PRINCIPAL + IMPERATIVO + PRESENTE + SEGUNDA + VOS + (NA * 6)  # VMMP2V000000
MP3S = VERBO + PRINCIPAL + IMPERATIVO + PRESENTE + TERCERA + SINGULAR + (NA * 6)  # VMMP3S000000
MP1P = VERBO + PRINCIPAL + IMPERATIVO + PRESENTE + PRIMERA + PLURAL + (NA * 6)  # VMMP1P000000
MP2P = VERBO + PRINCIPAL + IMPERATIVO + PRESENTE + SEGUNDA + PLURAL + (NA * 6)  # VMMP2P000000
MP3P = VERBO + PRINCIPAL + IMPERATIVO + PRESENTE + TERCERA + PLURAL + (NA * 6)  # VMMP3P000000

MP2S_P = VERBO + PRINCIPAL + IMPERATIVO + PRESENTE + SEGUNDA + SINGULAR + NA + PRONOMINAL + (NA * 4)  # VMMP2S0P0000
MP2V_P = VERBO + PRINCIPAL + IMPERATIVO + PRESENTE + SEGUNDA + VOS + NA + PRONOMINAL + (NA * 4)  # VMMP2V0P0000
MP3S_P = VERBO + PRINCIPAL + IMPERATIVO + PRESENTE + TERCERA + SINGULAR + NA + PRONOMINAL + (NA * 4)  # VMMP3S0P0000
MP1P_P = VERBO + PRINCIPAL + IMPERATIVO + PRESENTE + PRIMERA + PLURAL + NA + PRONOMINAL + (NA * 4)  # VMMP1P0P0000
MP2P_P = VERBO + PRINCIPAL + IMPERATIVO + PRESENTE + SEGUNDA + PLURAL + NA + PRONOMINAL + (NA * 4)  # VMMP2P0P0000
MP3P_P = VERBO + PRINCIPAL + IMPERATIVO + PRESENTE + TERCERA + PLURAL + NA + PRONOMINAL + (NA * 4)  # VMMP3P0P0000


CATALOGO_ETIQUETAS = [INF, INF_P, GER, GER_P, PAR_SM, PAR_SF, PAR_PM, PAR_PF,
                      IP1S, IP2S, IP2V, IP3S, IP1P, IP2P, IP3P,
                      II1S, II2S, II3S, II1P, II2P, II3P,
                      IS1S, IS2S, IS3S, IS1P, IS2P, IS3P,
                      IF1S, IF2S, IF3S, IF1P, IF2P, IF3P,
                      IC1S, IC2S, IC3S, IC1P, IC2P, IC3P,
                      SP1S, SP2S, SP2V, SP3S, SP1P, SP2P, SP3P,
                      SI1S, SI2S, SI3S, SI1P, SI2P, SI3P,
                      SF1S, SF2S, SF3S, SF1P, SF2P, SF3P,
                      MP2S, MP2V, MP3S, MP1P, MP2P, MP3P,
                      MP2S_P, MP2V_P, MP3S_P, MP1P_P, MP2P_P, MP3P_P]

# Para identificar la posición de ciertos tiempos verbales en las tablas de conjugación de la RAE
POSICION_CONJUGACION = [([II1S, II2S, II3S, II1P, II2P, II3P], 7, 4)]  # imperfecto de indicativo
POSICION_CONJUGACION += [([IS1S, IS2S, IS3S, IS1P, IS2P, IS3P], 16, 3)]  # pretérito perfecto simple
POSICION_CONJUGACION += [([IF1S, IF2S, IF3S, IF1P, IF2P, IF3P], 16, 4)]  # futuro de indicativo
POSICION_CONJUGACION += [([IC1S, IC2S, IC3S, IC1P, IC2P, IC3P], 25, 3)]  # condicional
POSICION_CONJUGACION += [([SP1S, SP2S, SP3S, SP1P, SP2P, SP3P], 35, 3)]  # presente de subjuntivo
POSICION_CONJUGACION += [([SF1S, SF2S, SF3S, SF1P, SF2P, SF3P], 35, 4)]  # futuro de subjuntivo
POSICION_CONJUGACION += [([SI1S, SI2S, SI3S, SI1P, SI2P, SI3P], 44, 3)]  # imperfecto de subjuntivo

CANON_VERBOS = [u'ir']  # v.conj
CANON_VERBOS += [u'repatriar', u'garuar', u'desvirtuar']  # v.conj.2.ar
CANON_VERBOS += [u'andar', u'desandar']  # v.conj.andar
CANON_VERBOS += [u'estar', u'encovar', u'evacuar', u'antojar', u'colar', u'diluviar', u'amar']  # v.conj.ar
CANON_VERBOS += [u'lisiar', u'penar']  # v.conj.arse
CANON_VERBOS += [u'bendecir', u'maldecir']  # v.conj.benmal.decir
CANON_VERBOS += [u'caer', u'decaer']  # v.conj.caer
CANON_VERBOS += [u'enrocar', u'complicar', u'cascar']  # v.conj.car
CANON_VERBOS += [u'mecer', u'convencer']  # v.conj.cer
CANON_VERBOS += [u'uncir', u'esperdecir']  # v.conj.cir
CANON_VERBOS += [u'licuar', u'adecuar']  # v.conj.cuar
CANON_VERBOS += [u'dar']  # v.conj.dar
CANON_VERBOS += [u'decir', u'desdecir']  # v.conj.decir
CANON_VERBOS += [u'reducir', u'producir', u'introducir', u'conducir']  # v.conj.ducir
CANON_VERBOS += [u'poseer', u'creer', u'desproveer']  # v.conj.eer
CANON_VERBOS += [u'reír', u'refreír', u'freír']  # v.conj.eír
CANON_VERBOS += [u'ceñir', u'constreñir']  # v.conj.eñir
CANON_VERBOS += [u'haber', u'ser', u'raer', u'vender', u'caber']  # v.conj.er
CANON_VERBOS += [u'propagar', u'cagar', u'cargar', u'descargar', u'descuajaringar', u'abrigar']  # v.conj.gar
CANON_VERBOS += [u'coger', u'proteger']  # v.conj.ger
CANON_VERBOS += [u'fingir', u'afligir']  # v.conj.gir
CANON_VERBOS += [u'aguar', u'desaguar']  # v.conj.guar
CANON_VERBOS += [u'hacer', u'rehacer']  # v.conj.hacer
CANON_VERBOS += [u'dormir', u'entredormir', u'elegir', u'henchir', u'discernir',
                 u'concernir', u'adquirir', u'hendir']  # v.conj.-ie-i-ue-u-.ir
CANON_VERBOS += [u'aforar', u'asolar', u'errar', u'follar', u'empezar']  # v.conj.-ie-ue-.ar
CANON_VERBOS += [u'cocer', u'devolver', u'extender', u'oler']  # v.conj.-ie-ue-.er
CANON_VERBOS += [u'jugar', u'descolgar', u'renegar', u'fregar']  # v.conj.-ie-ue-.gar
CANON_VERBOS += [u'forzar', u'avergonzar', u'comenzar']  # v.conj.-ie-ue-.zar
CANON_VERBOS += [u'asir', u'desvaír', u'inscribir', u'rehuir', u'extinguir']  # v.conj.ir
CANON_VERBOS += [u'reunir', u'prohibir', u'desprohibir']  # v.conj.ir.hiato
CANON_VERBOS += [u'enraizar', u'raizar']  # v.conj.izar
CANON_VERBOS += [u'desmullir']  # v.conj.llir
CANON_VERBOS += [u'atañer', u'empeller']  # v.conj.ñer
CANON_VERBOS += [u'plañir', u'mullir', u'zambullir']  # v.conj.ñir
CANON_VERBOS += [u'oír', u'desoír']  # v.conj.oír
CANON_VERBOS += [u'poner', u'indisponer']  # v.conj.poner
CANON_VERBOS += [u'querer', u'bienquerer']  # v.conj.querer
CANON_VERBOS += [u'roer', u'corroer']  # v.conj.roer
CANON_VERBOS += [u'saber', u'resaber']  # v.conj.saber
CANON_VERBOS += [u'salir', u'sobresalir']  # v.conj.salir
CANON_VERBOS += [u'seguir', u'proseguir']  # v.conj.seguir
CANON_VERBOS += [u'tener', u'sostener']  # v.conj.tener
CANON_VERBOS += [u'traer', u'atraer']  # v.conj.traer
CANON_VERBOS += [u'destruir', u'huir']  # v.conj.uir
CANON_VERBOS += [u'argüir', u'redargüir']  # v.conj.üir
CANON_VERBOS += [u'valer', u'equivaler']  # v.conj.valer
CANON_VERBOS += [u'venir', u'sobrevenir']  # v.conj.venir
CANON_VERBOS += [u'ver', u'entrever']  # v.conj.ver
CANON_VERBOS += [u'yacer', u'subyacer']  # v.conj.yacer
CANON_VERBOS += [u'granizar', u'izar']  # v.conj.zar
CANON_VERBOS += [u'anochecer', u'acontecer', u'agradecer', u'crecer']  # v.conj.zc.cer
CANON_VERBOS += [u'lucir', u'translucir']  # v.conj.zc.cir

CANON_ADJETIVOS = [u'japonés', u'común', u'honesto', u'limpio', u'verde',
                   u'gris', u'locuaz', u'huevón', u'fácil',  # inflect.es.adj.ad-lib
                   u'pachón', u'lisbonés', u'danzarín', u'solterón',  # inflect.es.adj.agudo-cons
                   u'tres', u'veintiuno', u'gilipollas', u'antiarrugas', u'pagafantas',  # inflect.es.adj.invariante
                   u'amante', u'decente', u'moscovita', u'fucsia', u'suave',  # inflect.es.adj.no-género
                   u'inicial', u'estéril', u'modular', u'cruel', u'uvular',  # inflect.es.adj.no-género-cons
                   u'amigo', u'castellano', u'ñoño', u'lúdico', u'húngaro',  # inflect.es.adj.reg
                   u'actor', u'español', u'dios', u'jugador',  # inflect.es.adj.reg-cons
                   u'adquirible', u'truhan', u'quichicientos', u'segundo', u'undécimo', u'bueno', u'malo', u'gay',
                   u'madrileño', u'tanto']
CANON_SUSTANTIVOS = [u'universidad', u'mes', u'flor', u'luz',
                     u'sacristán', u'alféizar',  # inflect.es.sust.ad-lib
                     u'sanción', u'bodegón', u'delfín',  # inflect.es.sust.agudo-cons
                     u'ubicación', u'ladrón', u'limón',  # inflect.es.sust.-ón
                     u'oasis', u'unisex', u'martes', u'virus',  # inflect.es.sust.invariante
                     u'gayumbos', u'fimosis', u'cuclillas',  # inflect.es.sust.plur.tantum
                     u'ojo', u'mano', u'página', u'día', u'bosque', u'llave'  # inflect.es.sust.reg
                     u'señal', u'mujer', u'uréter', u'edad', u'girasol', u'miel', u'arroz',  # inflect.es.sust.reg-cons
                     u'luchador',  # inflect.es.adj.reg-cons
                     u'dinero', u'superávit', u'internet', u'semen', u'rugby',  # inflect.es.sust.sing.tantum
                     u'gurú', u'marroquí', u'rubí', u'pedigrí', u'ajonjolí',  # inflect.es.sust.í
                     u'guion', u'león', u'zayn', u'convoy', u'Javier', u'Finlandia', u'torero', u'zar', u'príncipe', u'emperador']
CANON_SUSTANTIVOS += [u'saludes', u'bacanal', u'arribes', u'foto', u'mapa', u'pajarito', u'Buenos Aires']

CANON_ADVERBIOS = [u'también', u'sí', u'bastante', u'poco', u'muchísimo', u'muy', u'casi', u'igual', u'antes',
                   u'lejos', u'así', u'activamente', u'pero', u'tampoco', u'no', u'posteriormente', u'como', u'ahora',
                   u'inmediatamente', u'hoy']

CANON_PRONOMBRES = [u'yo', u'comigo', u'tú', u'vos', u'él', u'ge', u'lle', u'usted', u'vusted', u'voacé',
                    u'nosotros', u'connosco', u'vosotros', u'convusco', u'vusco', u'quienquiera']

CANON_DETERMINANTES = [u'algotro', u'algund', u'alguno', u'ambos', u'amos', u'aquel', u'aquele', u'aquese', u'aqueste',
                       u'bastante', u'cada', u'catorce', u'cero', u'cien', u'ciento', u'cinco', u'cincuenta',
                       u'cualque', u'cualquiera', u'cuarenta', u'cuatro', u'cuatrocientos', u'cuyo', u'cuál', u'cuánto',
                       u'demasiado', u'diecinueve', u'dieciocho', u'diecisiete', u'dieciséis', u'diez', u'doce', u'dos',
                       u'doscientos', u'el', u'entrambos', u'entramos', u'ese', u'esotro', u'este', u'estotro',
                       u'harto', u'menos', u'mil', u'mucho', u'muncho', u'más', u'mío', u'ninguno', u'novecientos',
                       u'noventa', u'nueso', u'nuestro', u'nueve', u'ochenta', u'ocho', u'ochocientos', u'once',
                       u'poco', u'quince', u'quinientos', u'qué', u'seis', u'seiscientos', u'sesenta', u'setecientos',
                       u'setenta', u'siete', u'so', u'suyo', u'tal', u'tantico', u'tanto', u'todo', u'trece',
                       u'treinta', u'tres', u'trescientos', u'tropecientos', u'tuyo', u'uno', u'vario', u'vaya',
                       u'veinte', u'veinticinco', u'veinticuatro', u'veintidós', u'veintinueve', u'veintiocho',
                       u'veintisiete', u'veintiséis', u'veintitrés', u'veintiuno', u'voso', u'vueso', u'vuestro']

CANON_CONJUNCIONES = [u'agora', u'ahora', u'antes', u'así', u'aunque', u'bien', u'ca', u'car', u'como', u'conque',
                      u'cuando', u'cuanto', u'deque', u'desque', u'e', u'ecepto', u'empero', u'ergo', u'et', u'excepto',
                      u'luego', u'maguer', u'maguera', u'mas', u'menos', u'mientras', u'más', u'ne', u'nen', u'ni',
                      u'nin', u'o', u'onde', u'ora', u'pero', u'porque', u'pues', u'que', u'quier', u'salvo', u'si',
                      u'sino', u'siquiera', u'tanto', u'u', u'y']



# OJO: el "cero" y también el "uno" tienen tratamiento especial
CARDINALES = [u'cero', u'uno', u'dos', u'tres', u'cuatro', u'cinco', u'seis', u'siete', u'ocho', u'nueve', u'diez',
              u'once', u'doce', u'trece', u'catorce', u'quince', u'dieciséis', u'diecisiete', u'dieciocho',
              u'diecinueve', u'veinte', u'veintiuno', u'veintidós', u'veintitrés', u'veinticuatro',
              u'veinticinco', u'veintiséis', u'veintisiete', u'veintiocho', u'veintinueve', u'treinta',
              u'cuarenta', u'cincuenta', u'sesenta', u'setenta', u'ochenta', u'noventa', u'cien', u'ciento',
              u'doscientos', u'trescientos', u'cuatrocientos', u'quinientos', u'seiscientos', u'setecientos',
              u'ochocientos', u'novecientos', u'mil', u'tropecientos']
ORDINALES = [u'primero', u'segundo', u'tercero', u'cuarto', u'quinto', u'sexto', u'séptimo', u'séptimo', u'octavo',
             u'noveno', u'nono', u'décimo', u'undécimo', u'decimoprimero', u'duodécimo', u'decimosegundo',
             u'decimotercero', u'decimocuarto', u'decimoquinto', u'decimosexto', u'decimoséptimo',
             u'decimoctavo', u'decimonoveno', u'vigésimo', u'trigésimo', u'cuadragésimo', u'quincuagésimo',
             u'sexagésimo', u'septuagésimo', u'octogésimo', u'nonagésico', u'centésimo', u'ducentésimo',
             u'tricentésimo', u'cuadringentésimo', u'quingentésimo', u'sexcentésimo', u'septingentésimo',
             u'octingentésimo', u'noningentésico', u'milésimo', u'millonésimo', u'milmillonésimo', u'billonésimo',
             u'milbillonésimo', u'trillonésimo', u'miltrillonésimo', u'cuatrillonésimo']
