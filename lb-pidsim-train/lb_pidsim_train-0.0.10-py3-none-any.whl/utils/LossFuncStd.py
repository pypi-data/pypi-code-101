#from __future__ import annotations

import tensorflow as tf
from tensorflow.keras.metrics import Metric

from keras import backend
from keras.utils import metrics_utils
from keras.utils import losses_utils


class LossFuncStd (Metric):   # docs to add
  """description
  
  See Also
  --------
  tf.keras.metrics :
    ...
  """
  def __init__ (self, name = "loss_std", **kwargs) -> None:
    super(LossFuncStd, self) . __init__ (name = name, **kwargs)
    self.std = self.add_weight (name = "std", initializer = "zeros")

  def update_state (self, values) -> None:
    values = tf.cast (values, self.dtype)
    self.std.assign_add ( tf.math.reduce_std(values) )
    
  def result (self) -> None:
    return self.std
