import numpy as np
import logging
import pyLDAvis.gensim
import json
import warnings
warnings.filterwarnings('ignore')  # To ignore all warnings that arise here to enhance clarity

from gensim.models.coherencemodel import CoherenceModel
from gensim.models.ldamodel import LdaModel
from gensim.corpora.dictionary import Dictionary
from numpy import array

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.debug("test")

# Set up corpus
texts = [['human', 'interface', 'computer'],
         ['survey', 'user', 'computer', 'system', 'response', 'time'],
         ['eps', 'user', 'interface', 'system'],
         ['system', 'human', 'system', 'eps'],
         ['user', 'response', 'time'],
         ['trees'],
         ['graph', 'trees'],
         ['graph', 'minors', 'trees'],
         ['graph', 'minors', 'survey']]  # len 9 sum 29
dictionary = Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]  # counter for every text

# Set up two topic models
goodLdaModel = LdaModel(corpus=corpus, id2word=dictionary, iterations=50, num_topics=2)
badLdaModel = LdaModel(corpus=corpus, id2word=dictionary, iterations=1, num_topics=2)

# Using U_Mass Coherence
goodcm = CoherenceModel(model=goodLdaModel, corpus=corpus, dictionary=dictionary, coherence='u_mass')
badcm = CoherenceModel(model=badLdaModel, corpus=corpus, dictionary=dictionary, coherence='u_mass')

# View the pipeline parameters for one coherence model
print(goodcm)

# Visualize topic models
# pyLDAvis.enable_notebook()
# pyLDAvis.gensim.prepare(goodLdaModel, corpus, dictionary)
# pyLDAvis.gensim.prepare(badLdaModel, corpus, dictionary)
print(goodcm.get_coherence())
print(badcm.get_coherence())


# Using C_V coherence
goodcm = CoherenceModel(model=goodLdaModel, texts=texts, dictionary=dictionary, coherence='c_v')
badcm = CoherenceModel(model=badLdaModel, texts=texts, dictionary=dictionary, coherence='c_v')

# Pipeline parameters for C_V coherence
print(goodcm)

# Print coherence values
print(goodcm.get_coherence())
print(badcm.get_coherence())
