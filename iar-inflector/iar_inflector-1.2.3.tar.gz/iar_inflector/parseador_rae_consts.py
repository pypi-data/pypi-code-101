#!/usr/bin/env python2
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

TAG_ACEPCION = u'p'
TAG_N_ACEP = u'n_acep'
TAG_ABBR = u'abbr'


REGEXP_AMBITOS = u'(Acústica|Aeronáutica|Agricultura|Alquimia|Anatomía|Antropología|Arqueología|Arquitectura|' \
                 u'Astrología|Astronomía|Biología|Bioquímica|Botánica|Carpintería|Cinegética|Cinematografía|' \
                 u'Comercio|Construcción|Danza\.?|Deportes|Derecho|Ecdótica|Ecología|Economía|' \
                 u'Electricidad|Equitación|Escultura|Esgrima|' \
                 u'Estadística|Filosofía|Física|Fisiología|Fonética|Fórmula|Fotografía|Geografía|Geología|Geometría|' \
                 u'Gramática|Heráldica|Imprenta|Informática|Ingeniería|Lingüística|Marina|Matemáticas|Mecánica|Medicina|' \
                 u'Meteorología|Métrica|Milicia|Mitología|Música|Numismática|Óptica|Ortografía|Parapsicología|' \
                 u'Pintura|Psicología|Psiquiatría|Química|Religión|Retórica|Sociología|Tauromaquia|Teatro\.?|' \
                 u'Tecnologías|Telecomunicación|Televisión|Teoría literaria|Topografía|Transportes|Urbanismo|' \
                 u'Veterinaria|Zoología|' \
                 u'coloquial|despectivo|vulgar|jerga|peyorativo|culto|poético|' \
                 u'rural|infantil|festivo|eufemismo|irónico|afectivo|malsonante|popular|ponderativo|' \
                 u'persona|jurídico|litúrgico|figurado|positivo|aposición|composición|por antonomasia|' \
                 u'(masculino|femenino)( o femenino)? referido a especie|contextos negativos o irreales|' \
                 u'construcciones negativas|' \
                 u'enfático|científico|náutico|sociológico|favorable|moral|' \
                 u'negativo|marina|lengua escrita|arquitectura|artillería|biología|botánica|geología|farmacia|medicina|' \
                 u'volatería|milicia|minería|lengua general|pintura|amenaza|antífrasis|coloquial|insulto|vocativo|' \
                 u'plural como taxón|dialectal)' \
                 u'( |$)'

REGEXP_PAISES = u'(América( Central| Meridional)?|(algunos|muchos) lugares de (América|España)|' \
                u'(((?<=^)|(?<=\s))[Ll]as )?Antillas|(((?<=^)|(?<=\s))[Ll]a )?Argentina|'\
                u'Bolivia|Chile|Colombia|Costa Rica|Cuba|(((?<=^)|(?<=\s))[Ee]l )?Ecuador|(((?<=^)|(?<=\s))[Ee]l )?Salvador|Estados Unidos|'\
                u'Filipinas|Granada|Guatemala|Guinea( Ecuatorial)?|Honduras|México|Nicaragua|Panamá|' \
                u'(((?<=^)|(?<=\s))[Ee]l )?Paraguay|'\
                u'(((?<=^)|(?<=\s))[Ee]l )?Perú|Puerto Rico|(((?<=^)|(?<=\s))[Ll]a )?República Dominicana|Uruguay|Venezuela)' \
                u'( |$)'

REGEXP_REGIONES = u'((norte de )?España( occidental| oriental)?|'\
                  u'Álava|Albacete|Almería|Andalucía|(algunos lugares de )?((((?<=^)|(?<=\s))[Ee]l )? Alto )?Aragón|' \
                  u'Asturias|Ávila|Badajoz|' \
                  u'Bilbao|Burgos|'\
                  u'Cáceres|Cádiz|Canarias|Cantabria|'\
                  u'Cataluña|Ciudad Real|Córdoba|Cuenca|Extremadura|Galicia|Gran Canaria|'\
                  u'Guadalajara|Guipúzcoa|Huelva|Huesca|'\
                  u'Islas Baleares|Jaén|Castilla|(((?<=^)|(?<=\s))[Ll]a )?Mancha|(((?<=^)|(?<=\s))[Ll]a )?Rioja|' \
                  u'León|Málaga|Madrid|Murcia|Navarra|' \
                  u'Palencia|País Vasco|Salamanca|Segovia|Sevilla|'\
                  u'Soria|Teruel|Tierra de Campos|Toledo|Valencia|Valladolid|Vizcaya|Zamora|Zaragoza|' \
                  u'germanía)' \
                  u'( |$)'

REGEXP_MEDIDAS = u'(área\(s\)|cada segundo|centígramo\(s\)|' \
                 u'centigramo\(s\)|centilitro\(s\)|centímetro\(s\)|centímetro\(s\) cúbico\(s\)|cuadrado\(s\)|' \
                 u'cúbico\(s\)|' \
                 u'decigramo\(s\)|eufemismo eufemístico o eufemística|' \
                 u'grado\(s\)( centígrado\(s\))?|' \
                 u'gramo\(s\)|hora\(s\)|' \
                 u'kilogramo\(s\)( por metro cúbico)?|kilohercio\(s\)|kilómetros|' \
                 u'kilómetro\(s\)( por hora)?|litro\(s\)|metro\(s\)|metro\(s\) cuadrado\(s\)|' \
                 u'metro\(s\) cúbico\(s\)| metro\(s\) por segundo|metro\(s\) por segundo cada segundo|' \
                 u'miligramo\(s\)|mililitro\(s\)|milímetro\(s\)|minuto\(s\)|mol\(es\) por metro cúbico|' \
                 u'número atómico|por segundo|por segundo cada segundo|tonelada\(s\))' \
                 u'( |$)'

REGEXP_VARIOS = u'^(afectivo o afectiva|(antes|después) de Cristo|aplicado|Aplicado a persona|' \
                u'coloquial|culto|despectivo o despectiva|Don|etcétera|' \
                u'irónico o irónica|festivo o festiva|germanía|latín científico|' \
                u'malsonante|peyorativo o peyorativa|poético o poética|ponderativo o ponderativa|' \
                u'popular|por antonomasia|[Pp]or ejemplo|[Pp]or extensión|rural|Símbolo|usted|vulgar)' \
                u'( |$)'

REGEXP_CATEGORIAS = u'(adjetivo|adverbio|artículo|conjunción|contracción|elementos? compositivos?|interjección|' \
                    u'locución|nombre|onomatopeya|participio irregular|' \
                    u'prefijo|preposición|pronombre|sufijo|verbo)' \
                    u'( |$)'
