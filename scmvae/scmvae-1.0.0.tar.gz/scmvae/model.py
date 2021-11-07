import warnings
warnings.filterwarnings('ignore')
import pickle
import numpy as np
import pandas as pd
import tensorflow as tf
from keras import backend as K
from keras.callbacks import EarlyStopping
from keras.layers import Lambda, Input, Dense, Layer, Concatenate
from keras.losses import mean_squared_logarithmic_error, mean_squared_error
from keras.models import Model
from keras import regularizers
from keras import initializers
from keras import optimizers

def sampling(args):
  z_mean, z_log_var = args
  batch = K.shape(z_mean)[0]
  dim = K.int_shape(z_mean)[1]

  epsilon = K.random_normal(shape=(batch, dim), mean=0., stddev=1.0)
  return z_mean + K.exp(0.5*z_log_var) * epsilon

def omicVAE_loss(omic_mean, omic_sigma, omic_label, omic_pred):
  reconstruction_loss_omic = K.mean(mean_squared_error(omic_label, omic_pred)) * int(omic_label.shape[1])
  kl_loss_omic = K.mean(-0.5 * K.sum(1 + omic_sigma - K.square(omic_mean) - K.exp(omic_sigma), axis=-1))
  omic_loss = reconstruction_loss_omic + kl_loss_omic

  return omic_loss

def build_omicVAE(input_dim_omic, net_dim_omic_list, net_dim_omic_mean, optimizer=None, seed=100):
  seed = seed
  omicVAE = None
  net_dim_omic_sigma = net_dim_omic_mean
  
  inikernel = initializers.glorot_uniform(seed=seed)
  # omic model
  input_omic = Input(shape=(input_dim_omic,), name='input_omic')
  h_omic_encoder = input_omic
  for net_dim_omic in net_dim_omic_list:
    h_omic_encoder = Dense(net_dim_omic, kernel_initializer=inikernel, activation="selu")(h_omic_encoder)
  h_omic_mean = Dense(net_dim_omic_mean, name='encoder_omic_mean', kernel_initializer=inikernel)(h_omic_encoder)
  h_omic_sigma = Dense(net_dim_omic_sigma, name='encoder_omic_sigma', kernel_initializer=inikernel)(h_omic_encoder)
  z_omic = Lambda(sampling, output_shape=(net_dim_omic_mean,), name='z_omic')([h_omic_mean, h_omic_sigma])
  h_omic_decoder_z = Dense(net_dim_omic_mean*2, name='decoder_omic_z', kernel_initializer=inikernel)(z_omic)
  
  h_omic_decoder = h_omic_decoder_z
  for net_dim_omic in net_dim_omic_list[::-1]:
    h_omic_decoder = Dense(net_dim_omic, kernel_initializer=inikernel, activation="selu")(h_omic_decoder)
  h_omic_decoder = Dense(input_dim_omic, name='decoder_omic', kernel_initializer=inikernel, activation="relu")(h_omic_decoder)
  output_omic = h_omic_decoder

  omicVAE = Model(inputs=input_omic, outputs=output_omic)

  omicVAE.add_loss(omicVAE_loss(h_omic_mean, h_omic_sigma, input_omic, output_omic))
  if optimizer is None:
    optimizer=tf.optimizers.Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.000001, amsgrad=False)

  omicVAE.compile(optimizer=optimizer)

  return omicVAE, h_omic_mean


def scMVAE_loss(rna_mean, rna_sigma, rna_label, rna_pred, pro_mean, pro_sigma, pro_label, pro_pred, mix_mean, mix_sigma, y_label1, y_pred1, y_label2, y_pred2):
  reconstruction_loss_rna = K.mean(mean_squared_error(rna_label, rna_pred)) * int(rna_label.shape[1])
  kl_loss_rna = K.mean(-0.5 * K.sum(1 + rna_sigma - K.square(rna_mean) - K.exp(rna_sigma), axis=-1))
  rna_loss = reconstruction_loss_rna + kl_loss_rna

  reconstruction_loss_pro = K.mean(mean_squared_error(pro_label, pro_pred)) * int(pro_label.shape[1])
  kl_loss_pro = K.mean(-0.5 * K.sum(1 + pro_sigma - K.square(pro_mean) - K.exp(pro_sigma), axis=-1))
  pro_loss = reconstruction_loss_pro + kl_loss_pro

  reconstruction_loss_mix1 = K.mean(mean_squared_error(y_label1, y_pred1)) * int(y_pred1.shape[1])
  reconstruction_loss_mix2 = K.mean(mean_squared_error(y_label2, y_pred2)) * int(y_pred2.shape[1])
  kl_loss_mix = K.mean(-0.5 * K.sum(1 + mix_sigma - K.square(mix_mean) - K.exp(mix_sigma), axis=-1))
  mix_loss = reconstruction_loss_mix1 + reconstruction_loss_mix2 + kl_loss_mix

  return rna_loss + pro_loss + mix_loss

def build_scMVAE(input_dim_rna, input_dim_pro, net_dim_rna_list, net_dim_pro_list, net_dim_rna_mean, net_dim_pro_mean, net_dim_mix, optimizer=None, seed = 100):
  seed = seed
  scMVAE = None

  inikernel = initializers.glorot_uniform(seed=seed)
  # rna model
  input_rna = Input(shape=(input_dim_rna,), name='input_rna')
  h_rna_encoder = input_rna
  for net_dim_rna in net_dim_rna_list:
    h_rna_encoder = Dense(net_dim_rna, kernel_initializer=inikernel, activation="selu")(h_rna_encoder)
  
  h_rna_mean = Dense(net_dim_rna_mean, name='encoder_rna_mean', kernel_initializer=inikernel)(h_rna_encoder)
  h_rna_sigma = Dense(net_dim_rna_sigma, name='encoder_rna_sigma', kernel_initializer=inikernel)(h_rna_encoder)
  z_rna = Lambda(sampling, output_shape=(net_dim_rna_mean,), name='z_rna')([h_rna_mean, h_rna_sigma])
  h_rna_decoder_z = Dense(net_dim_rna_mean*2, name='decoder_rna_z', kernel_initializer=inikernel)(z_rna)
  h_rna_decoder = h_rna_decoder_z
  for net_dim_rna in net_dim_rna_list[::-1]:
    h_rna_decoder = Dense(net_dim_rna, kernel_initializer=inikernel, activation="selu")(h_rna_decoder)
  
  h_rna_decoder = Dense(input_dim_rna, name='decoder_rna', kernel_initializer=inikernel, activation="relu")(h_rna_decoder)
  output_rna = h_rna_decoder
  # pro model
  input_pro = Input(shape=(input_dim_pro,), name='input_pro')
  h_pro_encoder = input_pro
  for net_dim_pro in net_dim_pro_list:
    h_pro_encoder = Dense(net_dim_pro, kernel_initializer=inikernel, activation="selu")(h_pro_encoder)
  
  h_pro_mean = Dense(net_dim_pro_mean, name='encoder_pro_mean', kernel_initializer=inikernel)(h_pro_encoder)
  h_pro_sigma = Dense(net_dim_pro_sigma, name='encoder_pro_sigma', kernel_initializer=inikernel)(h_pro_encoder)
  z_pro = Lambda(sampling, output_shape=(net_dim_pro_mean,), name='z_pro')([h_pro_mean, h_pro_sigma])
  h_pro_decoder_z = Dense(net_dim_pro_mean*2, name='decoder_pro_z', kernel_initializer=inikernel)(z_pro)

  h_pro_decoder = h_pro_decoder_z
  for net_dim_pro in net_dim_pro_list[::-1]:
    h_pro_decoder = Dense(net_dim_pro, kernel_initializer=inikernel, activation="selu")(h_pro_decoder)
  
  h_pro_decoder = Dense(input_dim_pro, name='decoder_pro', kernel_initializer=inikernel, activation="relu")(h_pro_decoder)
  output_pro = h_pro_decoder
  # mix model
  input_mix_rna_mean = h_rna_mean
  input_mix_pro_mean = h_pro_mean
  mix_mean = Concatenate()([input_mix_rna_mean, input_mix_pro_mean])
  mix_mean = Dense(net_dim_mix, name="mix_mean", kernel_initializer=inikernel)(mix_mean)

  input_mix_rna_sigma = h_rna_sigma
  input_mix_pro_sigma = h_pro_sigma
  mix_sigma = Concatenate()([input_mix_rna_sigma, input_mix_pro_sigma])
  mix_sigma = Dense(net_dim_mix, name="mix_sigma", kernel_initializer=inikernel)(mix_sigma)

  z_mix = Lambda(sampling, output_shape=(net_dim_mix,), name='z_mix')([mix_mean, mix_sigma])
  mix_docoder = Dense(net_dim_rna_mean+net_dim_pro_mean, name="mix_docoder", kernel_initializer=inikernel)(z_mix)
  mix_docoder_rna = Dense(net_dim_rna_mean, name="mix_docoder_rna", kernel_initializer=inikernel)(mix_docoder)
  mix_docoder_pro = Dense(net_dim_pro_mean, name="mix_docoder_pro", kernel_initializer=inikernel)(mix_docoder)

  scMVAE = Model(inputs=[input_rna, input_pro], outputs=[output_rna, output_pro])

  scMVAE.add_loss(scMVAE_loss(h_rna_mean, h_rna_sigma, input_rna, output_rna, h_pro_mean, h_pro_sigma, input_pro, output_pro, mix_mean, mix_sigma, z_rna, mix_docoder_rna, z_pro, mix_docoder_pro))
  
  if optimizer is None:
    optimizer=tf.optimizers.Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.000001, amsgrad=False)

  scMVAE.compile(optimizer=optimizer)

  return scMVAE, mix_mean, h_rna_mean, h_pro_mean
