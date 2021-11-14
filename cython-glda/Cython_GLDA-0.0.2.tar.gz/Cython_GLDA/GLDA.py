import numpy as np
from numpy.linalg import slogdet, cholesky
from Cython_GLDA.cython_trainer._cython_trainer import GLDA_trainer
import os
"""
Gaussian LDA using Gibbs sampling.

Draws from Allen Riddell's LDA library https://github.com/ariddell/lda 

and Savvy Sherpa's SLDA library https://github.com/Savvysherpa/slda/
"""

class TopicModelBase():
    """
    Base class for topic models.
    """
    n_topics = None
    alpha = None
    beta = None
    theta = None   
    
    
    def __init__(self):
            raise NotImplementedError


    
    def fit(self):
        """
        Estimate the topic distributions per document (theta) and term
        distributions per topic (phi).
        Parameters
        ----------
        X : array-like, shape = (n_docs, n_terms)
            The document-term matrix
        """

        raise NotImplementedError
    
    def fit_transform(self, X):
        """
        Estimate the topic distributions per document (theta) and term
        distributions per topic (phi), then return theta.
        Parameters
        ----------
        X : array-like, shape = (n_docs, n_terms)
            The document-term matrix
        Returns
        _______
        theta : numpy array, shape = (n_docs, n_topics)
            The topic distribution of each document
        """

        self.fit(X)
        return self.theta
    


class GLDA(TopicModelBase):
    """
    Latent Dirichlet allocation, using collapsed Gibbs sampling implemented in
    Cython.
    Parameters
    ----------
    K : int
        Number of topics
    alpha : array-like, shape = (n_topics,)
        Dirichlet distribution parameter for each document's topic
        distribution.
    beta : array-like, shape = (n_terms,)
        Dirichlet distribution parameter for each topic's term distribution.
    n_iter : int, default=500
        Number of iterations of Gibbs sampler
    n_burn_in : int, default=10
        Number of iterations of Gibbs sampler between progress reports.
    random_state : int, optional
        Seed for random number generator
    """
    """
    
#30ms orignally

)
    """
    def __init__(self, n_topics, alpha, beta, kappa, docs,embedding_matrix, vocab, n_iter=30, n_burnin =0,
                 seed=None,model_name = None, progress = 1, perplexity = 0, thin=1, need_init = 1):
        self.K = n_topics
        self.alpha = alpha
        self.beta = beta
        self.kappa = kappa
        self.n_iter = n_iter
        self.n_burnin = n_burnin 
        self.seed = seed
        self._embedding_matrix = embedding_matrix
        self._docs = docs
        self._vocab = vocab
        self._model_name = model_name
        self.progress = progress #print progress
        self.perp = perplexity
        self.need_init = need_init
        self.thin = thin
        
    def initialize(self):
        '''
        read files
        '''
        mydir = os.path.dirname(__file__)
        os.chdir(mydir)
        with open(self._docs) as f:
            lines = f.readlines()
        li = [line[1:-1].split() for line in lines]
        self.docs = []
        for tmp in li:
            self.docs.append([int(x) for x in tmp])
        
        with open(self._vocab, encoding='UTF-8') as f:
            lines = f.readlines()
        li = [str(line.split()[0]) for line in lines]
        
        self.embedding_matrix = np.load(self._embedding_matrix)
        self.embedding_size = self.embedding_matrix.shape[0] 
        '''
        initialize 
        '''
        
        model_name = "/" +  str(self._model_name) + "_K" + str(self.K)      
        self.model_name = os.path.join(mydir, model_name) 
        

        self.token_count = 0
        for doc in self.docs:
            self.token_count += len(doc) 
        self.Nw = np.zeros(shape=self.token_count, dtype='int')
        self.Nd = np.zeros(shape=self.token_count, dtype='int')
        self.Nr = np.zeros(shape=self.token_count, dtype='int')
        token_index = 0
        for doc_idx, doc in enumerate(self.docs):
            for word_id in doc:
                self.Nw[token_index] = word_id
                self.Nd[token_index] = doc_idx
                token_index += 1
        
        self.W = len(set(self.Nw)) # size of vocabulary
        self.D = len(set(self.Nd)) # number of documents
        self.Nz = np.random.randint(low=0, high=self.K, size=self.token_count, dtype='int')
        self.nzw = np.zeros(shape=(self.K, self.W), dtype='int') # topic word count matrix
        self.ndz = np.zeros(shape=(self.D, self.K), dtype='int') # document topic count matrix
        # fill ndz and nzw
        for i in range(self.token_count):
            d = self.Nd[i]
            w = self.Nw[i] #vocabulary
            z = self.Nz[i]
            self.ndz[d, z] += 1 
            self.nzw[z, w] += 1
            
        self.prior_nu = self.embedding_size
        sigma_scale = 3*self.prior_nu
        
        sigma = np.identity(self.embedding_size) * sigma_scale
        #sigma = np.random.rand(embedding_size,embedding_size)
       
        #chol_sigma = np.linalg.cholesky(B/100)
        chol_sigma = np.linalg.cholesky(sigma)
        self.table_chol_sigmas=np.zeros((self.embedding_size, self.embedding_size, self.K), dtype=np.float64,order='F')

        
        for i in range(self.K):
            self.table_chol_sigmas[:,:,i] =self.chol_sigma.T.copy()

            
        self.table_means = np.zeros((self.K,self.embedding_size),dtype=np.float64)

        for i in range(self.K):
            self.table_means[i] = np.mean(self.embedding_matrix,axis=0,dtype=np.float64).copy()
        


        
               
    def fit(self):
        """
        Estimate the topic distributions per document (theta) and term
        distributions per topic (phi).
        Parameters
        ----------
        X : array-like, shape = (n_docs, n_terms)
            The document-term matrix
        """
       
        
        # iterate
        self.Nz, self.new_assign, self.pll, self.ll, self.lls_t = GLDA_trainer(
            iterations = self.n_iter,
            Nw_in = self.Nw, Nd_in = self.Nd, ndz_in = self.ndz, nzw_in = self.nzw,
            K = self.K, W= self.W, 
            alpha = self.alpha, beta = self.beta, kappa = self.kappa,
            nu = self.embedding_size, print_progress = self.progress, burnin = self.burnin, thin = self.thin,
            embedding_in=self.embedding_matrix,
            posterior_topic_mean_in= self.table_means,
            posterior_topic_cov_in =  self.table_chol_sigmas, need_init = self.need_init, model_name = self.model_name
            )


