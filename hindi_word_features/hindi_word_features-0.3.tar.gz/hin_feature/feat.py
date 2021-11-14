#!/usr/bin/env python
# coding: utf-8

# In[251]:


import pandas as pd
import numpy as np
import epitran as epi
from wordfreq import word_frequency, zipf_frequency, tokenize


# In[285]:


#getting IPA tranformation

def get_IPA(word):
    """Converts the input Hindi 'word' to corresponding IPA (International Phonetic Alphabet) notation"""
    epit = epi.Epitran('hin-Deva')
    IPA = epit.trans_list(word)
    return (IPA)
    


# In[253]:


#getting frequency based features

def get_FRQ(word):
    """Counts the frequency of input Hindi 'word' based on occurances in multiple datasets"""
    FRQ = (word_frequency(word, 'hi', wordlist='best', minimum=0.0))*1000000
    return(FRQ)

def get_ZPF(word):
    """Calculates the Zipf value of input Hindi 'word' based on occurances in multiple datasets"""
    ZPF = int(zipf_frequency(word, 'hi', wordlist='best', minimum=0.0))
    return (ZPF)


# In[254]:


#Glyphs

swara = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ए', 'ऐ', 'ओ', 'औ', 'अं', 'ऋ']
vyanjana = ['क', 'ख', 'ग', 'घ', 'ङ',  
            'च', 'छ', 'ज','झ', 'ञ',
            'ट', 'ठ', 'ड', 'ढ', 'ण',
            'त', 'थ', 'द', 'ध', 'न',
            'प', 'फ', 'ब', 'भ', 'म', 
            'य', 'र', 'ल', 'व', 'श',
            'ष', 'स', 'ह', 'क्ष', 'त्र', 'ज्ञ', 'ळ', 'ऑ']
matra = ['े', 'ं', 'ै', 'ा', 'ी', 'ौ', 'ो', 'ि', 'ू', 'ु', 'ँ', 'ॉ', 'ृ', 'ः', 'ॅ']
halant = '्'


# In[255]:


#Phones

vowels = ['ə', 'ə̃', 'a','aː', 'a:', 'ã', 'ɪ', 'i', 'iː','ĩ', 'i:', 'ʊ', 'ũ', 'uː', 'u','u:', 'ɻ̩', 'e','e:', 'ẽ',  'ɛ','ɛ:', 'o', 'o:', 'ɔ', 'ɔ:','ɔː','ɔ̃ː','æ','æː','ॅ','ऑ']
last = ['ə']
long = ['ː']
schwa = ['ə']


# In[256]:


#Anuswar and anunasik presence

def get_ANU(word):
    """Checks the prsence of Anuswar or Anunasik in input Hindi 'word' 
    0: None present
    1: Either present
    2:Both present"""
    
    y = word
    nasik = ['ं','ँ' ]
    y = [i for i in y if i in nasik]
    if (nasik[0] in y and nasik[1] in y):
        y1 = 2
    elif (nasik[0] in y or nasik[1] in y):
        y1 = 1
    else:
        y1 = 0
    return (y1)


# In[257]:


#Consonant Cluster count

def get_CCL(IPA):
    """Counts the number of consonant clusters (yukt-akshar) in input Hindi 'word'
    takes IPA as input run get_IPA(word) or help(get_IPA)"""
    y = IPA
    y = [j for j in y if j not in long]   
    c = 0
    j=0
    k=1
    while j<len(y):
        b = 0    
        l = 1
        while k<len(y):
            if (y[j] not in vowels and y[k] not in vowels):
                if (b==0):
                    b=1
                    l += 1
                    c = c+1
                k +=1
                
            else:
                l = 1
                j = k
                k +=1
                b=0
               
        j+=1
        
    return(c)


# In[258]:


#Syllable count

def get_SYB(IPA):
    """Counts the number of syllables in input Hindi 'word' 
    run get_IPA(word) first or help(get_IPA)"""
    
    y = IPA
    #y = eval(y)
    y = [j for j in y if j not in long]   
    if (y[len(y)-1] in last):
        y.pop()
        
    for i in y:
        if (i in schwa):
            x = y.index(i)
            if (x != 1):
                if (x+1<len(y) and y[x+1] not in vowels):
                    if (x+2<len(y) and y[x+2] in vowels):
                        del y[x]
                
    
    if (y[len(y)-1] not in vowels):
        if(len(y)-2>=0):
            if (len(y)-3>=0):
                if (y[len(y)-2] not in vowels and y[len(y)-3] in vowels):
                    y = [i for i in y if i in vowels]
                    c = len(y)
                elif (y[len(y)-2] in vowels):
                    y = [i for i in y if i in vowels]
                    c = len(y)
                else:
                    y = [i for i in y if i in vowels]
                    c = len(y)+1
            else:
                if (y[len(y)-2] in vowels):
                    y = [i for i in y if i in vowels]
                    c = len(y)
                else:
                    y = [i for i in y if i in vowels]
                    c = len(y)+1
        else:
            y = [i for i in y if i in vowels]
            c = len(y)+1
    else:
        y = [i for i in y if i in vowels]
        c = len(y)
    return(c)
    


# In[259]:


#Articulatory phonetics

swara = ['ə', 'ə̃', 'a','aː', 'a:', 'ã', 'ɪ', 'i', 'iː','ĩ', 'i:', 'ʊ', 'ũ', 'uː', 'u','u:', 'ɻ̩', 'e','e:', 'ẽ',  'ɛ','ɛ:', 'o', 'o:', 'ɔ', 'ɔ:','ɔː','ɔ̃ː','æ','æː','ॅ','ऑ'] 
last = ['ə']
long = ['ː','्']
schwa = ['ə']

retroflex = ['ɳ','ʈ','ʈʰ','ɖ','ɖʱ','ɽ','ɽʱ','ʂ','ɖ̤','ɽ̥','ळ']
dental = ['n','t','tʰ','d','dʱ','r','s','z','l','d̤']
bilabial = ['m','p','pʰ','b','bʱ','f','ʋ','v','b̤']
palatal = ['ɲ','tʃ','tʃʰ','dʒ','dʒʱ','ʃ','ʒ','j', 'd͡ʒ', 't͡ʃ','t͡ʃʰ','r̩','d͡ʒ̤']
velar = ['ŋ','k','q','kʰ','ɡ','ɡʱ','x','ɣ','ɡ̤']
glottal = ['ɦ', 'h']


# In[260]:


#Articulatory position change count 

def get_TPC(IPA):
    """Counts the number of articulatory position changes in articulation of input Hindi 'word' 
    run get_IPA(word) first or help(get_IPA)"""
    
    y = IPA
    #y = eval(y)
    y = [j for j in y if j not in long]   
    if (y[len(y)-1] in last):
        y.pop()
        
    for i in y:
        if (i in schwa):
            x = y.index(i)
            if (x != 1):
                if (x+1<len(y) and y[x+1] not in swara):
                    if (x+2<len(y) and y[x+2] in swara):
                        del y[x]
    for i in y:
        if (i in swara):
            x = y.index(i)
            del y[x]
    c = 0
    j=0
    k=1
    while k<len(y):
        b = 0
        if (y[j] in velar and y[k] not in velar):
            if (b==0):
                b=1
                if(y[k] not in swara):
                    c = c+1
            
        elif (y[j] in swara and y[k] not in swara):
            if (b==0):
                b=1
              
        elif (y[j] in palatal and y[k] not in palatal):
            if (b==0):
                b=1
                if(y[k] not in swara):
                    c = c+1            
                
        elif (y[j] in retroflex and y[k] not in retroflex):
            if (b==0):
                b=1
                if(y[k] not in swara):
                    c = c+1                

                
        elif (y[j] in dental and y[k] not in dental):
            if (b==0):
                b=1
                if(y[k] not in swara):
                    c = c+1
      
                
        elif (y[j] in bilabial and y[k] not in bilabial):
            if (b==0):
                b =1
                if(y[k] not in swara):
                    c = c+1            
           
            
        elif (y[j] in glottal and y[k] not in glottal):
            if (b==0):
                b=1
                if(y[k] not in swara):
                    c = c+1
        k+=1       
        j+=1
        
    return(c)
   


# In[261]:


#Ascender and descender marks

asc = ['े', 'ं', 'ै', 'ी', 'ौ', 'ो', 'ि', 'ँ', 'ॉ', 'ई', 'ऐ', 'ओ', 'औ']
rasc = 'र्'

des = [ 'ू', 'ु', 'ृ', '़']
rdes = '्र'
vdes = 'क्व'
ndes = 'न्न'
thdes = 'ठ्ठ'
ttdes = 'ट्ट'
tthdes = 'ट्ठ'
dgdes = 'द्ग'
ddhdes = 'द्ध'
dbhdes = 'द्भ'
dmdes = 'द्म'
dvdes = 'द्व'
dddes = 'ड्ड'
gndes = 'ग्न'
ghndes = 'घ्न'
hmdes = 'ह्म'
hldes = 'ह्ल'
hvdes = 'ह्व'
hndes = 'ह्न'
hydes = 'ह्य'

AD = [rdes, vdes, ndes, ttdes, tthdes, thdes, dgdes, ddhdes, dbhdes, dmdes, dvdes, dddes, gndes, ghndes, hmdes, hldes, hvdes, hndes, hydes]


# In[262]:


#Presence of Ascender and Descender

def get_PAD(word):
    """Counts the presence of top or bottom diacrictis (matra) and/or half characters in input Hindi 'word' 
    0: None present
    1: Either present
    2: Both present"""
    
    y = word
    l = 0
    a = 0
    d = 0
    if (rasc in y):
        a = a+1
    for i in AD:
        if (i in y):
            d = d+1
    for j in y:
        if (j in asc):
            a = a + 1
        elif (j in des):
            d = d + 1
    if (a>0 and d>0):
        l = 2
    elif (a>0 or d>0):
        l = 1
    return(l)


# In[263]:


#Left and right oriented vowel signs

left = [ 'ि', 'ु']
right = [ 'ा', 'ी', 'ौ', 'ो', 'ी', 'ू', 'ॉ', 'ृ', 'ः' ]


# In[264]:


#Bidirectionality

def get_BID(word):
    """Counts the presence of left or right diacritics (matra) in input Hindi 'word' 
    0: None present
    1: Either present
    2: Both present"""
    
    y = word
    o = 0
    l = 0
    r = 0
    for j in y:
        if (j in left):
            l = l+1
        if (j in right):
            r = r+1
    if (l>0 and r>0):
        o = 2
    elif (l>0 or r>0):
        o = 1
    
    return(o)


# In[265]:


#Conjunct consonants

halant = '्'
ksh = 'क्ष'
sr = 'श्र'
dy = 'द्य'
gy = 'ज्ञ'
tr = 'त्र'

cld = [ksh, sr, dy, gy, tr]


# In[266]:


#Half-character count

def get_HAL(word):
    """Counts the number of half-characters (with halant) in input Hindi 'word' """
    
    y = word
    y1 = [i for i in y if i in halant]
    z = len(y1)
    for j in cld:
        if (j in y):
            z = z-y.count(j)
    
    return(z)


# In[267]:


#morphologic length

def get_LEN(word):
    """Counts the number of all characters (excluding halant) and,
    calculates the morphological length of the input Hindi 'word' """
    
    y = word
    y = list(y)
    y = [i for i in y if i not in halant]
    return(len(y))


# In[268]:


#All features

def get_all_features(word):
    """Calculates the feature set (10 features) for the input Hindi 'word' 
    If you just need phonetic features try get_phonetic_features(word) or help(get_phonetic_features)
    If you just need orthographic features try get_orthographic_features(word) or help(get_orthographic_features)
    If you just need frequency based features try get_frequency_features(word) or help(get_frequency_features)
    If you just need single feature try get_this_feature(word, feature) or help(get_this_feature)
    """
    
    IPA = get_IPA(word)
    FRQ = get_FRQ(word)
    ZPF = get_ZPF(word)
    LEN = get_LEN(word)
    HAL = get_HAL(word)
    BID = get_BID(word)
    PAD = get_PAD(word)
    ANU = get_ANU(word)
    CCL = get_CCL(IPA)
    SYB = get_SYB(IPA)
    TPC = get_TPC(IPA)
    dict = {'Frequency':FRQ, 'Zipf value':ZPF, 'Morphological length':LEN,
           'Half character count':HAL, 'Bidirectionality':BID, 'Presence of Ascender/Decender':PAD, 
            'Presence of Anuswar/Anunasik':ANU, 'Consonant cluster count':CCL, 'Number of Syllables':SYB, 
            'Articulatory position changes':TPC}
    return(dict)


# In[276]:


#single particular feature

def get_this_feature(word, feature):
    """Calculate particular 'feature' for the input Hindi 'word'
    The input 'feature' must be one of the following-
    'Frequency': run help(get_FRQ)
    'Zipf': run help(get_ZPF)
    'Length': run help(get_LEN)
    'Halant': run help(get_HAL)
    'TopDown': run help(get_PAD)
    'LeftRight': run help(get_BID)
    'Anu': run help(get_ANU)
    'Cluster': run help(get_CCL)
    'Syllable': run help(get_SYB)
    'Position': run help(get_TPC)
    """
    
    if (feature == 'Frequency'):
        a = get_FRQ(word)
    elif (feature == 'Zipf'):
        a = get_ZPF(word)
    elif (feature == 'Length'):
        a = get_LEN(word)
    elif (feature == 'Halant'):
        a = get_HAL(word)
    elif (feature == 'TopDown'):
        a = get_PAD(word)
    elif (feature == 'LeftRight'):
        a = get_BID(word)
    elif (feature == 'Anu'):
        a = get_ANU(word)
    elif (feature == 'Cluster'):
        IPA = get_IPA(word)
        a = get_CCL(IPA)
    elif (feature == 'Syllable'):
        IPA = get_IPA(word)
        a = get_SYB(IPA)
    elif (feature == 'Position'):
        IPA = get_IPA(word)
        a = get_TPC(IPA)
    else:
        a = help(get_this_feature)
    return (a)


# In[277]:


#phonetic features

def get_phonetic_features(word):
    """Calculates the phonetic feature set (4 features) for the input Hindi 'word' 
    If you need all features try get_all_features(word) or help(get_all_features)
    If you just need orthographic features try get_orthographic_features(word) or help(get_orthographic_features)
    If you just need frequency based features try get_frequency_features(word) or help(get_frequency_features)
    If you just need single feature try get_this_feature(word, feature) or help(get_this_feature)
    """
    IPA = get_IPA(word)
    ANU = get_ANU(word)
    CCL = get_CCL(IPA)
    SYB = get_SYB(IPA)
    TPC = get_TPC(IPA)
    dict = {'Presence of Anuswar/Anunasik':ANU, 'Consonant cluster count':CCL, 'Number of Syllables':SYB, 
            'Articulatory position changes':TPC}
    return(dict)


# In[278]:


#orthographic features

def get_orthographic_features(word):
    """Calculates the orthographic feature set (4 features) for the input Hindi 'word' 
    If you need all features try get_all_features(word) or help(get_all_features)
    If you just need phonetic features try get_phonetic_features(word) or help(get_phonetic_features)
    If you just need frequency based features try get_frequency_features(word) or help(get_frequency_features)
    If you just need single feature try get_this_feature(word, feature) or help(get_this_feature)
    """
    LEN = get_LEN(word)
    HAL = get_HAL(word)
    BID = get_BID(word)
    PAD = get_PAD(word)
    
    dict = {'Morphological length':LEN, 'Half character count':HAL, 
            'Bidirectionality':BID, 'Presence of Ascender/Decender':PAD}
    return(dict)


# In[279]:


#frequency-based features

def get_frequency_features(word):
    """Calculates the frewuency based feature set (2 features) for the input Hindi 'word' 
    If you just need phonetic features try get_phonetic_features(word) or help(get_phonetic_features)
    If you just need orthographic features try get_orthographic_features(word) or help(get_orthographic_features)
    If you all features try get_all_features(word) or help(get_all_features)
    If you just need single feature try get_this_feature(word, feature) or help(get_this_feature)
    """
    FRQ = get_FRQ(word)
    ZPF = get_ZPF(word)
    dict = {'Frequency':FRQ, 'Zipf value':ZPF}
    return(dict)


# In[280]:


#features for text

def get_features(text, k='all'):
    """
    Calculates the 'k' features for the given Hindi 'text'
    'text' is combination of words (sentence, passage, etc.)
    
    the input 'k' features must be one of following-
    'all' : run help(get_all_features)
    'phonetic' : run help(get_phonetic_features)
    'orthographic' : run help(get_orthographic_features)
    'frequency' : run help(get_frequency_feature)
    
    If you need a particular feature of a particular 'word' run help(get_this_feature)
    """
    words = tokenize(text, 'hi')
    dict = {}
    k_list = ['all', 'phonetic', 'orthographic', 'frequency']
    if(k not in k_list):
        print ("Please select the apropriate feature set or run help(get_features)")
        return
    for word in words:
        print (word)
        if k=='all':
            ft = get_all_features(word)
            print(ft)
            dict.update({word:ft})
        
        elif k=='phonetic':
            ft = get_phonetic_features(word)
            print(ft)
            dict.update({word:ft})
        
        elif k=='orthographic':
            ft = get_orthographic_features(word)
            print(ft)
            dict.update({word:ft})
        
        elif k=='frequency':
            ft = get_frequency_features(word)
            print(ft)
            dict.update({word:ft})
    return (dict)
    








