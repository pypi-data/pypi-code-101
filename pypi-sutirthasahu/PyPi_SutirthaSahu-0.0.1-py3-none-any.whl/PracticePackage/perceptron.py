import numpy as np
import logging
from tqdm import tqdm


class Perceptron:
  def __init__(self,eta, epochs):
    self.weights = np.random.randn(3) * 1e-4
    logging.info(f"initial weights before training : {self.weights}")
    self.eta = eta
    self.epochs = epochs


  def activationFunction(self,inputs,weights):
    z=np.dot(inputs, weights) # z = W1.x1 ..... = W * X
    return np.where(z > 0, 1, 0)

  def fit(self, X, y):
    self.X = X
    self.y = y

    X_with_bias = np.c_[self.X, -np.ones((len(self.X),1))]
    logging.info(f"X with bias : \n{X_with_bias}")

    for epoch in tqdm(range(self.epochs), total=self.epochs, desc="training the model"):
      logging.info("--"*10)
      logging.info(f"for epoch : {epoch}")
      logging.info("--"*10)

      y_hat = self.activationFunction(X_with_bias,self.weights)  # fwd propagation 
      logging.info(f"Predicted value after forward pass : \n{y_hat}")

      self.error = self.y - y_hat
      logging.info(f"error : {self.error}")

      self.weights = self.weights + self.eta * np.dot(X_with_bias.T, self.error) #backward propagation
      logging.info(f"updated weights after epochs : \n{epoch}/{self.epochs} : {self.weights}")
      logging.info("####"*10)


  def predict(self, X):
    X_with_bias = np.c_[X, -np.ones((len(X),1))]
    return self.activationFunction(X_with_bias, self.weights)


  def total_loss(self):
    total_loss = np.sum(self.error)
    logging.info(f"total loss : {total_loss}")
    return total_loss