"""
Author: Damien GUEHO
Copyright: Copyright (C) 2021 Damien GUEHO
License: Public Domain
Version: 19
Created: May 2021
Python: 3.7.7
"""


"""

"""



import numpy as np
import scipy.io
import numpy.linalg as LA
import matplotlib.pyplot as plt
from matplotlib import rc
import cvxpy as cp

colors = [(11/255, 36/255, 251/255),
          (27/255, 161/255, 252/255),
          (77/255, 254/255, 193/255),
          (224/255, 253/255, 63/255),
          (253/255, 127/255, 35/255),
          (221/255, 10/255, 22/255),
          (255/255, 0/255, 127/255),
          (127/255, 0/255, 255/255),
          (255/255, 0/255, 255/255),
          (145/255, 145/255, 145/255),
          (0, 0, 0)]

plt.rcParams.update({"text.usetex": True, "font.family": "sans-serif", "font.serif": ["Computer Modern Roman"]})
rc('text', usetex=True)

from SparseIDAlgorithms.GeneratePolynomialBasisFunctions import generatePolynomialBasisFunctions
from SparseIDAlgorithms.GeneratePolynomialIndex import generatePolynomialIndex


HyperData_1 = scipy.io.loadmat('HyperData_1.mat')
HyperData_1_Soln = scipy.io.loadmat('HyperData_1_Soln.mat')
HyperData_2 = scipy.io.loadmat('HyperData_2.mat')
HyperData_2_Soln = scipy.io.loadmat('HyperData_2_Soln.mat')
#
#
# ## Get CUT Points weights
# data_CUT_weights = HyperData_1['XW'][:, 3]
# XW = np.diag(data_CUT_weights)








#######################################################################################################################
#################                   Expansion of ToF and gamma_0 u(t)                        ##########################
#######################################################################################################################

#
# ## Get time of Flight (ToF)
# data_tof = np.concatenate(HyperData_1_Soln['data']['tof'][0], axis=1)[0]
#
#
# ## Get gamma_0
# data_gamma_0 = np.concatenate(HyperData_1_Soln['data']['gam0'][0], axis=1)[0]
#
#
# ## Get nu_h (ToF)
# data_nu_h = np.concatenate(HyperData_1_Soln['data']['nuH'][0], axis=1)[0]
#
#
# ## Get nu_theta
# data_nu_theta = np.concatenate(HyperData_1_Soln['data']['nuTHETA'][0], axis=1)[0]
#
#
# ## Get altitude_0
# data_alt_0 = HyperData_1['alt'][:, 0]
# data_alt_0_n = 2 * (data_alt_0 - data_alt_0.min()) / (data_alt_0.max() - data_alt_0.min()) - 1
#
#
# ## Get longitude_0
# data_longitude_0 = HyperData_1['long'][:, 0]
# data_longitude_0_n = 2 * (data_longitude_0 - data_longitude_0.min()) / (data_longitude_0.max() - data_longitude_0.min()) - 1
#
#
# ## Get longitude_tf
# data_longitude_tf = HyperData_1['longt'][:, 0]
# data_longitude_tf_n = 2 * (data_longitude_tf - data_longitude_tf.min()) / (data_longitude_tf.max() - data_longitude_tf.min()) - 1
#
#
# ## Parameters
# number_cut_points = len(data_CUT_weights)
# dimension = 3
# order = 6
# post_treatment = True
# max_order = order
# alpha = 2
# epsilon = 1e-15
# delta = 1e-10
# max_iterations = 20
#
#
# ## Generate basis functions
# index = generatePolynomialIndex(dimension, order, post_treatment, max_order=max_order)
# index_length, _ = index.shape
# basis_functions = generatePolynomialBasisFunctions(dimension, index)
#
#
# ## Generate Matrix of basis functions
# Phi = np.zeros([number_cut_points, index_length])
# for i in range(number_cut_points):
#     for j in range(index_length):
#         z = np.array([data_alt_0_n[i], data_longitude_0_n[i], data_longitude_tf_n[i]])
#         Phi[i, j] = basis_functions[j](z)
#
#
# ## LS Solution
# # data_tof_norm = np.matmul(LA.inv(XW), data_tof)
# data_tof_norm = data_nu_h
# # data_gamma_0_norm = np.matmul(LA.inv(XW), data_gamma_0)
# data_gamma_0_norm = data_nu_theta
# C_LS_tof = np.matmul(LA.pinv(Phi), data_tof_norm)
# C_LS_gamma_0 = np.matmul(LA.pinv(Phi), data_gamma_0_norm)
#
#
# # Sparse solution
# it = 0
# C_Sparse_history_tof = np.zeros([index_length, max_iterations])
# C_Sparse_history_gamma_0 = np.zeros([index_length, max_iterations])
# C_Sparse_tof = np.zeros(index_length)
# C_Sparse_gamma_0 = np.zeros(index_length)
#
# W_tof = np.diag(np.ones(Phi.shape[1]))
# W_gamma_0 = np.diag(np.ones(Phi.shape[1]))
# for i in range(Phi.shape[1]):
#     W_tof[i, i] = 1 / (np.abs(C_LS_tof[i]) + epsilon)
#     W_gamma_0[i, i] = 1 / (np.abs(C_LS_gamma_0[i]) + epsilon)
# W_tof = W_tof / (np.max(np.abs(np.diag(W_tof))) * 0.8 * 1e-1)
# W_gamma_0 = W_gamma_0 / (np.max(np.abs(np.diag(W_gamma_0))) * 0.8 * 1e-1)
#
# while it < max_iterations:
#     print('Iteration: ', it)
#     c_tof = cp.Variable(shape=Phi.shape[1])
#     c_gamma_0 = cp.Variable(shape=Phi.shape[1])
#     objective_tof = cp.Minimize(cp.norm(W_tof @ c_tof, 1))
#     objective_gamma_0 = cp.Minimize(cp.norm(W_gamma_0 @ c_gamma_0, 1))
#     constraints_tof = [cp.norm(data_tof_norm - Phi @ c_tof, 2) <= alpha * cp.norm(data_tof_norm - np.matmul(Phi, C_LS_tof), 2)]
#     constraints_gamma_0 = [cp.norm(data_gamma_0_norm - Phi @ c_gamma_0, 2) <= alpha * cp.norm(data_gamma_0_norm - np.matmul(Phi, C_LS_gamma_0), 2)]
#     prob_tof = cp.Problem(objective_tof, constraints_tof)
#     prob_gamma_0 = cp.Problem(objective_gamma_0, constraints_gamma_0)
#     prob_tof.solve(verbose=True)
#     prob_gamma_0.solve(verbose=True)
#     print('c_tof', c_tof.value)
#     print('c_gamma_0', c_gamma_0.value)
#     C_Sparse_history_tof[:, it] = c_tof.value
#     C_Sparse_history_gamma_0[:, it] = c_gamma_0.value
#
#     for i in range(Phi.shape[1]):
#         W_tof[i, i] = 1 / (np.abs(c_tof.value[i]) + epsilon)
#         W_gamma_0[i, i] = 1 / (np.abs(c_gamma_0.value[i]) + epsilon)
#     W_tof = W_tof / (np.max(np.abs(np.diag(W_tof))) * 0.8 * 1e-1)
#     W_gamma_0 = W_gamma_0 / (np.max(np.abs(np.diag(W_gamma_0))) * 0.8 * 1e-1)
#     #print('W', W)
#
#     it = it + 1
#
# index_non0_tof = []
# index_non0_gamma_0 = []
# for i in range(Phi.shape[1]):
#     index_non0_tof.append(i)
#     index_non0_gamma_0.append(i)
# index_0_tof = []
# index_0_gamma_0 = []
# ind_tof = []
# ind_gamma_0 = []
# w_tof = []
# w_gamma_0 = []
# for i in range(Phi.shape[1]):
#     if np.abs(c_tof.value[i]) < delta:
#         index_0_tof.append(index_non0_tof[i])
#         ind_tof.append(i)
#     if np.abs(c_tof.value[i]) >= delta:
#         w_tof.append(c_tof.value[i])
#     if np.abs(c_gamma_0.value[i]) < delta:
#         index_0_gamma_0.append(index_non0_gamma_0[i])
#         ind_gamma_0.append(i)
#     if np.abs(c_gamma_0.value[i]) >= delta:
#         w_gamma_0.append(c_gamma_0.value[i])
#
# ind_tof.reverse()
# ind_gamma_0.reverse()
# for i in range(len(ind_tof)):
#     del index_non0_tof[ind_tof[i]]
# for i in range(len(ind_gamma_0)):
#     del index_non0_gamma_0[ind_gamma_0[i]]
#
# print('index_non0_tof', index_non0_tof)
# print('index_non0_gamma_0', index_non0_gamma_0)
# print('index_0_tof', index_0_tof)
# print('index_0_gamma_0', index_0_gamma_0)
#
# Phi_sparse_tof = np.take(Phi, index_non0_tof, axis=1)
# Phi_sparse_gamma_0 = np.take(Phi, index_non0_gamma_0, axis=1)
# theta_sparse_tof = np.matmul(LA.pinv(Phi_sparse_tof), data_tof_norm)
# theta_sparse_gamma_0 = np.matmul(LA.pinv(Phi_sparse_gamma_0), data_gamma_0_norm)
#
# count_tof = 0
# for i in range(index_length):
#     if count_tof < len(index_non0_tof):
#         if index_non0_tof[count_tof] == i:
#             C_Sparse_tof[i] = theta_sparse_tof[count_tof]
#             count_tof = count_tof + 1
# count_gamma_0 = 0
# for i in range(index_length):
#     if count_gamma_0 < len(index_non0_gamma_0):
#         if index_non0_gamma_0[count_gamma_0] == i:
#             C_Sparse_gamma_0[i] = theta_sparse_gamma_0[count_gamma_0]
#             count_gamma_0 = count_gamma_0 + 1
#
#
# error_tof = np.zeros([number_cut_points, 2])
# error_tof[:, 0] = np.abs((data_tof_norm - np.matmul(Phi, C_LS_tof)) / data_tof_norm)
# error_tof[:, 1] = np.abs((data_tof_norm - np.matmul(Phi, C_Sparse_tof)) / data_tof_norm)
# error_gamma_0 = np.zeros([number_cut_points, 2])
# error_gamma_0[:, 0] = np.abs((data_gamma_0_norm - np.matmul(Phi, C_LS_gamma_0)) / data_gamma_0_norm)
# error_gamma_0[:, 1] = np.abs((data_gamma_0_norm - np.matmul(Phi, C_Sparse_gamma_0)) / data_gamma_0_norm)
#
#
#
# ## Plotting
# plt.figure(1, figsize=(4, 3))
# plt.semilogy(np.linspace(1, index_length, index_length), np.abs(C_LS_tof), '*', color=colors[6])
# plt.semilogy(np.linspace(1, index_length, index_length), np.abs(C_Sparse_tof), '.', color=colors[7])
# plt.legend(['Least-squares solution', 'Sparse solution'])
# plt.xlabel('Basis functions')
# plt.ylabel('Amplitude of coefficients')
#
# plt.tight_layout()
# # plt.savefig('TOF_coeff.eps', format='eps')
#
# plt.show()
#
# plt.figure(11, figsize=(4, 3))
# plt.semilogy(np.linspace(1, index_length, index_length), np.abs(C_LS_gamma_0), '*', color=colors[6])
# plt.semilogy(np.linspace(1, index_length, index_length), np.abs(C_Sparse_gamma_0), '.', color=colors[7])
# plt.legend(['Least-squares solution', 'Sparse solution'])
# plt.xlabel('Basis functions')
# plt.ylabel('Amplitude of coefficients')
#
# plt.tight_layout()
# # plt.savefig('Gamma0_coeff.eps', format='eps')
#
# plt.show()



# plt.figure(2, figsize=(9, 9))
# plt.subplot(3, 3, 1)
# plt.semilogy(np.linspace(1, index_length, index_length), np.abs(C_LS_tof), '*', color=colors[6])
# plt.ylabel('Amplitude of coefficients')
# plt.title('Least-squares solution')
# plt.subplot(3, 3, 2)
# plt.semilogy(np.linspace(1, index_length, index_length), np.abs(C_Sparse_history_tof[:, 0]), '.', color=colors[7])
# plt.title('Iteration 1')
# plt.subplot(3, 3, 3)
# plt.semilogy(np.linspace(1, index_length, index_length), np.abs(C_Sparse_history_tof[:, 1]), '.', color=colors[7])
# plt.title('Iteration 2')
# plt.subplot(3, 3, 4)
# plt.semilogy(np.linspace(1, index_length, index_length), np.abs(C_Sparse_history_tof[:, 2]), '.', color=colors[7])
# plt.title('Iteration 3')
# plt.ylabel('Amplitude of coefficients')
# plt.subplot(3, 3, 5)
# plt.semilogy(np.linspace(1, index_length, index_length), np.abs(C_Sparse_history_tof[:, 3]), '.', color=colors[7])
# plt.title('Iteration 4')
# plt.subplot(3, 3, 6)
# plt.semilogy(np.linspace(1, index_length, index_length), np.abs(C_Sparse_history_tof[:, 4]), '.', color=colors[7])
# plt.title('Iteration 5')
# plt.subplot(3, 3, 7)
# plt.semilogy(np.linspace(1, index_length, index_length), np.abs(C_Sparse_history_tof[:, 5]), '.', color=colors[7])
# plt.title('Iteration 6')
# plt.ylabel('Amplitude of coefficients')
# plt.xlabel('Basis Functions')
# plt.subplot(3, 3, 8)
# plt.semilogy(np.linspace(1, index_length, index_length), np.abs(C_Sparse_history_tof[:, 6]), '.', color=colors[7])
# plt.title('Iteration 7')
# plt.xlabel('Basis Functions')
# plt.subplot(3, 3, 9)
# plt.semilogy(np.linspace(1, index_length, index_length), np.abs(C_Sparse_history_tof[:, 7]), '.', color=colors[7])
# plt.title('Iteration 8')
# plt.xlabel('Basis Functions')
# plt.show()
#
#
#
# plt.figure(3, figsize=(9, 9))
# plt.subplot(3, 3, 1)
# plt.semilogy(np.linspace(1, index_length, index_length), np.abs(C_LS_gamma_0), '*', color=colors[6])
# plt.ylabel('Amplitude of coefficients')
# plt.title('Least-squares solution')
# plt.subplot(3, 3, 2)
# plt.semilogy(np.linspace(1, index_length, index_length), np.abs(C_Sparse_history_gamma_0[:, 0]), '.', color=colors[7])
# plt.title('Iteration 1')
# plt.subplot(3, 3, 3)
# plt.semilogy(np.linspace(1, index_length, index_length), np.abs(C_Sparse_history_gamma_0[:, 1]), '.', color=colors[7])
# plt.title('Iteration 2')
# plt.subplot(3, 3, 4)
# plt.semilogy(np.linspace(1, index_length, index_length), np.abs(C_Sparse_history_gamma_0[:, 2]), '.', color=colors[7])
# plt.title('Iteration 3')
# plt.ylabel('Amplitude of coefficients')
# plt.subplot(3, 3, 5)
# plt.semilogy(np.linspace(1, index_length, index_length), np.abs(C_Sparse_history_gamma_0[:, 3]), '.', color=colors[7])
# plt.title('Iteration 4')
# plt.subplot(3, 3, 6)
# plt.semilogy(np.linspace(1, index_length, index_length), np.abs(C_Sparse_history_gamma_0[:, 4]), '.', color=colors[7])
# plt.title('Iteration 5')
# plt.subplot(3, 3, 7)
# plt.semilogy(np.linspace(1, index_length, index_length), np.abs(C_Sparse_history_gamma_0[:, 5]), '.', color=colors[7])
# plt.title('Iteration 6')
# plt.ylabel('Amplitude of coefficients')
# plt.xlabel('Basis Functions')
# plt.subplot(3, 3, 8)
# plt.semilogy(np.linspace(1, index_length, index_length), np.abs(C_Sparse_history_gamma_0[:, 6]), '.', color=colors[7])
# plt.title('Iteration 7')
# plt.xlabel('Basis Functions')
# plt.subplot(3, 3, 9)
# plt.semilogy(np.linspace(1, index_length, index_length), np.abs(C_Sparse_history_gamma_0[:, 7]), '.', color=colors[7])
# plt.title('Iteration 8')
# plt.xlabel('Basis Functions')
# plt.show()


# mdic = {"C_LS_nu_h": C_LS_tof}
# scipy.io.savemat("C_LS_nu_h.mat", mdic)




########################################################################################################################
######################                   Expansion of Control u(t)                        ##############################
########################################################################################################################

# ## Get h
# data_h = np.concatenate(HyperData_1_Soln['data']['h'][0], axis=1)
#
#
# ## Get theta
# data_theta = np.concatenate(HyperData_1_Soln['data']['theta'][0], axis=1)
#
#
# ## Get v
# data_v = np.concatenate(HyperData_1_Soln['data']['v'][0], axis=1)
#
#
# ## Get gamma
# data_gamma = np.concatenate(HyperData_1_Soln['data']['gamma'][0], axis=1)
#
#
# ## Get nu_h
# data_nu_h = np.multiply(np.ones([100001, 59]), np.concatenate(HyperData_1_Soln['data']['nuH'][0], axis=1)[0])
#
#
# ## Get nu_theta
# data_nu_theta = np.multiply(np.ones([100001, 59]), np.concatenate(HyperData_1_Soln['data']['nuTHETA'][0], axis=1)[0])
#
#
# ## Get_lambda_gamma
# data_lambda_gamma = np.concatenate(HyperData_1_Soln['data']['lamGAM'][0], axis=1)
#
#
# ## Get lambda_v
# data_lambda_v = np.concatenate(HyperData_1_Soln['data']['lamV'][0], axis=1)
#
# ## Get alpha
# c_L = 1.5658
# c_D = 1.6537
# u = np.zeros([10001, 59])
# for i in range(59):
#     for k in range(10001):
#         u[k, i] = c_L * data_lambda_gamma[k, i] / (2 * c_D * data_v[k, i] * data_lambda_v[k, i])
#
#
#
# ## Normalize data
# data_h_n = np.zeros([10001, 59])
# data_theta_n = np.zeros([10001, 59])
# data_v_n = np.zeros([10001, 59])
# data_gamma_n = np.zeros([10001, 59])
# data_nu_h_n = np.zeros([10001, 59])
# data_nu_theta_n = np.zeros([10001, 59])
# for i in range(10001):
#     data_h_n[i, :] = 2 * (data_h[i, :] - data_h[i, :].min()) / (data_h[i, :].max() - data_h[i, :].min()) - 1
#     data_theta_n[i, :] = 2 * (data_theta[i, :] - data_theta[i, :].min()) / (data_theta[i, :].max() - data_theta[i, :].min()) - 1
#     if i == 0:
#         data_v_n[i, :] = data_v[i, :]
#     else:
#         data_v_n[i, :] = 2 * (data_v[i, :] - data_v[i, :].min()) / (data_v[i, :].max() - data_v[i, :].min()) - 1
#     data_gamma_n[i, :] = 2 * (data_gamma[i, :] - data_gamma[i, :].min()) / (data_gamma[i, :].max() - data_gamma[i, :].min()) - 1
#     data_nu_h_n[i, :] = 2 * (data_nu_h[i, :] - data_nu_h[i, :].min()) / (data_nu_h[i, :].max() - data_nu_h[i, :].min()) - 1
#     data_nu_theta_n[i, :] = 2 * (data_nu_theta[i, :] - data_nu_theta[i, :].min()) / (data_nu_theta[i, :].max() - data_nu_theta[i, :].min()) - 1
#
#
# ## Parameters
# number_cut_points = len(data_CUT_weights)
# dimension = 6
# order = 3
# post_treatment = True
# max_order = order
# alpha = 2
# epsilon = 1e-15
# delta = 1e-10
# max_iterations = 20
# max_time_step = 10001
#
#
# ## Generate basis functions
# index = generatePolynomialIndex(dimension, order, post_treatment, max_order=max_order)
# index_length, _ = index.shape
# basis_functions = generatePolynomialBasisFunctions(dimension, index)
#
#
# ## Generate Matrix of basis functions
# Psi_1 = np.zeros([number_cut_points, index_length, 10001])
# Psi_2 = np.zeros([number_cut_points, index_length, 10001])
# for i in range(number_cut_points):
#     for j in range(index_length):
#         for k in range(max_time_step):
#             z1 = np.array([data_h_n[k, i], data_theta_n[k, i], data_v_n[k, i], data_gamma_n[k, i], data_nu_h_n[k, i], data_nu_theta_n[k, i]])
#             Psi_1[i, j, k] = basis_functions[j](z1)
#             z2 = np.array([data_h_n[k, i], data_theta_n[k, i], data_v_n[k, i], data_gamma_n[k, i], data_h_n[-1, i], data_theta_n[-1, i]])
#             Psi_2[i, j, k] = basis_functions[j](z2)
#
#
# ## LS Solution
# C_LS_1 = np.zeros([10001, index_length])
# C_LS_2 = np.zeros([10001, index_length])
# for k in range(max_time_step):
#     C_LS_1[k, :] = np.matmul(LA.pinv(Psi_1[:, :, k]), u[k, :])
#     C_LS_2[k, :] = np.matmul(LA.pinv(Psi_2[:, :, k]), u[k, :])
#
#
# # Sparse solution
# C_Sparse_history_1 = np.zeros([10001, index_length, max_iterations])
# C_Sparse_history_2 = np.zeros([10001, index_length, max_iterations])
# C_Sparse_1 = np.zeros([10001, index_length])
# C_Sparse_2 = np.zeros([10001, index_length])
#
#
# for k in range(1, max_time_step):
#
#     it = 0
#
#     W_1 = np.diag(np.ones(Psi_1.shape[1]))
#     W_2 = np.diag(np.ones(Psi_2.shape[1]))
#     for i in range(Psi_1.shape[1]):
#         W_1[i, i] = 1 / (np.abs(C_LS_1[k, i]) + epsilon)
#         W_2[i, i] = 1 / (np.abs(C_LS_2[k, i]) + epsilon)
#     W_1 = W_1 / (np.max(np.abs(np.diag(W_1))) * 0.8 * 1e-1)
#     W_2 = W_2 / (np.max(np.abs(np.diag(W_2))) * 0.8 * 1e-1)
#
#     while it < max_iterations:
#         print('Iteration: ', it)
#         c_1 = cp.Variable(shape=Psi_1.shape[1])
#         c_2 = cp.Variable(shape=Psi_2.shape[1])
#         objective_1 = cp.Minimize(cp.norm(W_1 @ c_1, 1))
#         objective_2 = cp.Minimize(cp.norm(W_2 @ c_2, 1))
#         constraints_1 = [cp.norm(u[k, :] - Psi_1[:, :, k] @ c_1, 2) <= alpha * cp.norm(u[k, :] - np.matmul(Psi_1[:, :, k], C_LS_1[k, :]), 2)]
#         constraints_2 = [cp.norm(u[k, :] - Psi_2[:, :, k] @ c_2, 2) <= alpha * cp.norm(u[k, :] - np.matmul(Psi_2[:, :, k], C_LS_2[k, :]), 2)]
#         prob_1 = cp.Problem(objective_1, constraints_1)
#         prob_2 = cp.Problem(objective_2, constraints_2)
#         prob_1.solve(verbose=False)
#         prob_2.solve(verbose=False)
#         # print('c_1', c_1.value)
#         # print('c_2', c_2.value)
#         C_Sparse_history_1[k, :, it] = c_1.value
#         C_Sparse_history_2[k, :, it] = c_2.value
#
#         for i in range(Psi_1.shape[1]):
#             W_1[i, i] = 1 / (np.abs(c_1.value[i]) + epsilon)
#             W_2[i, i] = 1 / (np.abs(c_2.value[i]) + epsilon)
#         W_1 = W_1 / (np.max(np.abs(np.diag(W_1))) * 0.8 * 1e-1)
#         W_2 = W_2 / (np.max(np.abs(np.diag(W_2))) * 0.8 * 1e-1)
#
#         it = it + 1
#
#     index_non0_1 = []
#     index_non0_2 = []
#     for i in range(Psi_1.shape[1]):
#         index_non0_1.append(i)
#         index_non0_2.append(i)
#     index_0_1 = []
#     index_0_2 = []
#     ind_1 = []
#     ind_2 = []
#     w_1 = []
#     w_2 = []
#     for i in range(Psi_1.shape[1]):
#         if np.abs(c_1.value[i]) < delta:
#             index_0_1.append(index_non0_1[i])
#             ind_1.append(i)
#         if np.abs(c_1.value[i]) >= delta:
#             w_1.append(c_1.value[i])
#         if np.abs(c_2.value[i]) < delta:
#             index_0_2.append(index_non0_2[i])
#             ind_2.append(i)
#         if np.abs(c_2.value[i]) >= delta:
#             w_2.append(c_2.value[i])
#
#     ind_1.reverse()
#     ind_2.reverse()
#     for i in range(len(ind_1)):
#         del index_non0_1[ind_1[i]]
#     for i in range(len(ind_2)):
#         del index_non0_2[ind_2[i]]
#
#     print('index_non0_1', index_non0_1)
#     print('index_non0_2', index_non0_2)
#     print('index_0_1', index_0_1)
#     print('index_0_2', index_0_2)
#
#     Psi_sparse_1 = np.take(Psi_1[:, :, k], index_non0_1, axis=1)
#     Psi_sparse_2 = np.take(Psi_2[:, :, k], index_non0_2, axis=1)
#     theta_sparse_1 = np.matmul(LA.pinv(Psi_sparse_1), u[k, :])
#     theta_sparse_2 = np.matmul(LA.pinv(Psi_sparse_2), u[k, :])
#
#     count_1 = 0
#     for i in range(index_length):
#         if count_1 < len(index_non0_1):
#             if index_non0_1[count_1] == i:
#                 C_Sparse_1[k, i] = theta_sparse_1[count_1]
#                 count_1 = count_1 + 1
#     count_2 = 0
#     for i in range(index_length):
#         if count_2 < len(index_non0_2):
#             if index_non0_2[count_2] == i:
#                 C_Sparse_2[k, i] = theta_sparse_2[count_2]
#                 count_2 = count_2 + 1
#
#
# ## Errors
# error_1 = np.zeros([10001, number_cut_points, 2])
# error_2 = np.zeros([10001, number_cut_points, 2])
# error_1_mean = np.zeros([10001, 2])
# error_2_mean = np.zeros([10001, 2])
# for k in range(1, max_time_step):
#     error_1[k, :, 0] = np.abs((u[k, :] - np.matmul(Psi_1[:, :, k], C_LS_1[k, :])) / u[k, :])
#     error_1[k, :, 1] = np.abs((u[k, :] - np.matmul(Psi_1[:, :, k], C_Sparse_1[k, :])) / u[k, :])
#     error_1_mean[k, 0] = np.mean(error_1[k, :, 0])
#     error_1_mean[k, 1] = np.mean(error_1[k, :, 1])
#     error_2[k, :, 0] = np.abs((u[k, :] - np.matmul(Psi_2[:, :, k], C_LS_2[k, :])) / u[k, :])
#     error_2[k, :, 1] = np.abs((u[k, :] - np.matmul(Psi_2[:, :, k], C_Sparse_2[k, :])) / u[k, :])
#     error_2_mean[k, 0] = np.mean(error_2[k, :, 0])
#     error_2_mean[k, 1] = np.mean(error_2[k, :, 1])
#
#
## Plotting
# plt.figure(1, figsize=(10, 2.5))
# plt.imshow(np.log10(np.abs(C_Sparse_u_1[0:500, :].T)), cmap='plasma', interpolation='nearest')
# cbar = plt.colorbar(fraction=0.046, pad=0.04)
# cbar.set_label('log value of the coefficients')
# plt.ylabel('\# coefficient')
# plt.xlabel('Time (time steps)')
#
# plt.tight_layout()
# plt.savefig('U1_coeff.eps', format='eps', transparent=False)
#
# plt.show()
#
#
# plt.figure(2, figsize=(10, 2.5))
# plt.imshow(np.log10(np.abs(C_Sparse_u_2[0:500, :].T)), cmap='plasma', interpolation='nearest')
# cbar = plt.colorbar(fraction=0.046, pad=0.04)
# cbar.set_label('log value of the coefficients')
# plt.ylabel('\# coefficient')
# plt.xlabel('Time (time steps)')
#
# plt.tight_layout()
# plt.savefig('U2_coeff.eps', format='eps', transparent=False)
#
# plt.show()


# plt.figure(1, figsize=(10, 8))
# plt.subplot(2, 1, 1)
# plt.semilogy(np.linspace(0, max_time_step - 1, max_time_step), error_1_mean[0:max_time_step, 0], color=colors[6])
# plt.semilogy(np.linspace(0, max_time_step - 1, max_time_step), error_1_mean[0:max_time_step, 1], color=colors[7])
# plt.title('Formulation 1')
# plt.ylabel('Mean relative error')
# plt.xlabel('Time (time steps)')
# plt.legend(['Least-squares', 'Sparse'])
# plt.subplot(2, 1, 2)
# plt.semilogy(np.linspace(0, max_time_step - 1, max_time_step), error_2_mean[0:max_time_step, 0], color=colors[6])
# plt.semilogy(np.linspace(0, max_time_step - 1, max_time_step), error_2_mean[0:max_time_step, 1], color=colors[7])
# plt.title('Formulation 2')
# plt.ylabel('Mean relative error')
# plt.xlabel('Time (time steps)')
# plt.legend(['Least-squares', 'Sparse'])
# plt.show()










########################################################################################################################
#
#                                  Verification tof, gamma_0, nu_h, nu_theta
#
########################################################################################################################


# C_LS_tof = scipy.io.loadmat('Coefficients/C_LS_tof.mat')['C_LS_tof'][0]
# C_LS_gamma_0 = scipy.io.loadmat('Coefficients/C_LS_gamma_0.mat')['C_LS_gamma_0'][0]
# C_LS_nu_h = scipy.io.loadmat('Coefficients/C_LS_nu_h.mat')['C_LS_nu_h'][0]
# C_LS_nu_theta = scipy.io.loadmat('Coefficients/C_LS_nu_theta.mat')['C_LS_nu_theta'][0]
# C_Sparse_tof = scipy.io.loadmat('Coefficients/C_Sparse_tof.mat')['C_Sparse_tof'][0]
# C_Sparse_gamma_0 = scipy.io.loadmat('Coefficients/C_Sparse_gamma_0.mat')['C_Sparse_gamma_0'][0]
# C_Sparse_nu_h = scipy.io.loadmat('Coefficients/C_Sparse_nu_h.mat')['C_Sparse_nu_h'][0]
# C_Sparse_nu_theta = scipy.io.loadmat('Coefficients/C_Sparse_nu_theta.mat')['C_Sparse_nu_theta'][0]
#
#
#
# ## Get time of Flight (ToF)
# data_tof = np.concatenate(HyperData_2_Soln['data']['tof'][0], axis=1)[0]
#
#
# ## Get gamma_0
# data_gamma_0 = np.concatenate(HyperData_2_Soln['data']['gam0'][0], axis=1)[0]
#
#
# ## Get nu_h (ToF)
# data_nu_h = np.concatenate(HyperData_2_Soln['data']['nuH'][0], axis=1)[0]
#
#
# ## Get nu_theta
# data_nu_theta = np.concatenate(HyperData_2_Soln['data']['nuTHETA'][0], axis=1)[0]
#
#
# ## Get altitude_0
# data_alt_0_1 = HyperData_1['alt'][:, 0]
# data_alt_0_2 = HyperData_2['alt'][:, 0]
# data_alt_0_2n = 2 * (data_alt_0_2 - data_alt_0_1.min()) / (data_alt_0_1.max() - data_alt_0_1.min()) - 1
#
#
# ## Get longitude_0
# data_longitude_0_1 = HyperData_1['long'][:, 0]
# data_longitude_0_2 = HyperData_2['long'][:, 0]
# data_longitude_0_2n = 2 * (data_longitude_0_2 - data_longitude_0_1.min()) / (data_longitude_0_1.max() - data_longitude_0_1.min()) - 1
#
#
# ## Get longitude_tf
# data_longitude_tf_1 = HyperData_1['longt'][:, 0]
# data_longitude_tf_2 = HyperData_2['longt'][:, 0]
# data_longitude_tf_2n = 2 * (data_longitude_tf_2 - data_longitude_tf_1.min()) / (data_longitude_tf_1.max() - data_longitude_tf_1.min()) - 1
#
#
#
# ## Parameters
# number_cut_points = len(data_CUT_weights)
# dimension = 3
# order = 6
# post_treatment = True
# max_order = order
# alpha = 2
# epsilon = 1e-15
# delta = 1e-10
# max_iterations = 20
#
#
#
# ## Generate basis functions
# index = generatePolynomialIndex(dimension, order, post_treatment, max_order=max_order)
# index_length, _ = index.shape
# basis_functions = generatePolynomialBasisFunctions(dimension, index)
#
#
#
# ## Generate Matrix of basis functions
# N = 200
# Phi = np.zeros([N, index_length])
# for i in range(N):
#     for j in range(index_length):
#         z = np.array([data_alt_0_2n[i], data_longitude_0_2n[i], data_longitude_tf_2n[i]])
#         Phi[i, j] = basis_functions[j](z)
#
#
# # ## Normalization
# # data_tof_norm = np.matmul(LA.inv(XW), data_tof)
# # data_gamma_0_norm = np.matmul(LA.inv(XW), data_gamma_0)
# # data_nu_h_norm = np.matmul(LA.inv(XW), data_nu_h)
# # data_nu_theta_norm = np.matmul(LA.inv(XW), data_nu_theta)
#
#
#
## Error
# error_tof_verification = np.zeros([N, 2])
# error_tof_verification[:, 0] = np.abs((data_tof - np.matmul(Phi, C_LS_tof)) / data_tof)
# error_tof_verification[:, 1] = np.abs((data_tof - np.matmul(Phi, C_Sparse_tof)) / data_tof)
# error_gamma_0_verification = np.zeros([N, 2])
# error_gamma_0_verification[:, 0] = np.abs((data_gamma_0 - np.matmul(Phi, C_LS_gamma_0)) / data_gamma_0)
# error_gamma_0_verification[:, 1] = np.abs((data_gamma_0 - np.matmul(Phi, C_Sparse_gamma_0)) / data_gamma_0)
# error_nu_h_verification = np.zeros([N, 2])
# error_nu_h_verification[:, 0] = np.abs((data_nu_h - np.matmul(Phi, C_LS_nu_h)) / data_nu_h)
# error_nu_h_verification[:, 1] = np.abs((data_nu_h - np.matmul(Phi, C_Sparse_nu_h)) / data_nu_h)
# error_nu_theta_verification = np.zeros([N, 2])
# error_nu_theta_verification[:, 0] = np.abs((data_nu_theta - np.matmul(Phi, C_LS_nu_theta)) / data_nu_theta)
# error_nu_theta_verification[:, 1] = np.abs((data_nu_theta - np.matmul(Phi, C_Sparse_nu_theta)) / data_nu_theta)































########################################################################################################################
#
#                                  Verification u(t)
#
########################################################################################################################


max_time_step = 10001

C_LS_u_1 = scipy.io.loadmat('Coefficients/C_LS_u_1.mat')['data']
C_LS_u_2 = scipy.io.loadmat('Coefficients/C_LS_u_2.mat')['data']
C_Sparse_u_1 = scipy.io.loadmat('Coefficients/C_Sparse_u_1.mat')['data']
C_Sparse_u_2 = scipy.io.loadmat('Coefficients/C_Sparse_u_2.mat')['data']



## Get h
data_h1 = np.concatenate(HyperData_1_Soln['data']['h'][0], axis=1)
data_h2 = np.concatenate(HyperData_2_Soln['data']['h'][0], axis=1)


## Get theta
data_theta1 = np.concatenate(HyperData_1_Soln['data']['theta'][0], axis=1)
data_theta2 = np.concatenate(HyperData_2_Soln['data']['theta'][0], axis=1)


## Get v
data_v1 = np.concatenate(HyperData_1_Soln['data']['v'][0], axis=1)
data_v2 = np.concatenate(HyperData_2_Soln['data']['v'][0], axis=1)


## Get gamma
data_gamma1 = np.concatenate(HyperData_1_Soln['data']['gamma'][0], axis=1)
data_gamma2 = np.concatenate(HyperData_2_Soln['data']['gamma'][0], axis=1)


## Get nu_h
data_nu_h = np.multiply(np.ones([100001, 200]), np.concatenate(HyperData_2_Soln['data']['nuH'][0], axis=1)[0])


## Get nu_theta
data_nu_theta = np.multiply(np.ones([100001, 200]), np.concatenate(HyperData_2_Soln['data']['nuTHETA'][0], axis=1)[0])


## Get_lambda_gamma
data_lambda_gamma = np.concatenate(HyperData_2_Soln['data']['lamGAM'][0], axis=1)


## Get lambda_v
data_lambda_v = np.concatenate(HyperData_2_Soln['data']['lamV'][0], axis=1)


## Get alpha
c_L = 1.5658
c_D = 1.6537
u = np.zeros([10001, 200])
for i in range(200):
    for k in range(max_time_step):
        u[k, i] = c_L * data_lambda_gamma[k, i] / (2 * c_D * data_v2[k, i] * data_lambda_v[k, i])



# ## Normalize data
# data_h_n = np.zeros([10001, 200])
# data_theta_n = np.zeros([10001, 200])
# data_v_n = np.zeros([10001, 200])
# data_gamma_n = np.zeros([10001, 200])
# data_nu_h_n = np.zeros([10001, 200])
# data_nu_theta_n = np.zeros([10001, 200])
# for i in range(max_time_step):
#     data_h_n[i, :] = 2 * (data_h2[i, :] - data_h1[i, :].min()) / (data_h1[i, :].max() - data_h1[i, :].min()) - 1
#     data_theta_n[i, :] = 2 * (data_theta2[i, :] - data_theta1[i, :].min()) / (data_theta1[i, :].max() - data_theta1[i, :].min()) - 1
#     if i == 0:
#         data_v_n[i, :] = data_v2[i, :]
#     else:
#         data_v_n[i, :] = 2 * (data_v2[i, :] - data_v1[i, :].min()) / (data_v1[i, :].max() - data_v1[i, :].min()) - 1
#     data_gamma_n[i, :] = 2 * (data_gamma2[i, :] - data_gamma1[i, :].min()) / (data_gamma1[i, :].max() - data_gamma1[i, :].min()) - 1
#     data_nu_h_n[i, :] = 2 * (data_nu_h[i, :] - data_nu_h[i, :].min()) / (data_nu_h[i, :].max() - data_nu_h[i, :].min()) - 1
#     data_nu_theta_n[i, :] = 2 * (data_nu_theta[i, :] - data_nu_theta[i, :].min()) / (data_nu_theta[i, :].max() - data_nu_theta[i, :].min()) - 1
#
#
#
# ## Parameters
# number_cut_points = len(data_CUT_weights)
# dimension = 6
# order = 3
# post_treatment = True
# max_order = order
# alpha = 2
# epsilon = 1e-15
# delta = 1e-10
# max_iterations = 20
#
#
# ## Generate basis functions
# index = generatePolynomialIndex(dimension, order, post_treatment, max_order=max_order)
# index_length, _ = index.shape
# basis_functions = generatePolynomialBasisFunctions(dimension, index)
#
#
# ## Generate Matrix of basis functions
# Psi_1 = np.zeros([200, index_length, 10001])
# Psi_2 = np.zeros([200, index_length, 10001])
# for i in range(200):
#     for j in range(index_length):
#         for k in range(max_time_step):
#             z1 = np.array([data_h_n[k, i], data_theta_n[k, i], data_v_n[k, i], data_gamma_n[k, i], data_nu_h_n[k, i], data_nu_theta_n[k, i]])
#             Psi_1[i, j, k] = basis_functions[j](z1)
#             z2 = np.array([data_h_n[k, i], data_theta_n[k, i], data_v_n[k, i], data_gamma_n[k, i], data_h_n[-1, i], data_theta_n[-1, i]])
#             Psi_2[i, j, k] = basis_functions[j](z2)
#
#
#
#
# ## Errors
# error_1 = np.zeros([10001, 200, 2])
# error_2 = np.zeros([10001, 200, 2])
# error_1_mean = np.zeros([10001, 2])
# error_2_mean = np.zeros([10001, 2])
# for k in range(1, max_time_step):
#     error_1[k, :, 0] = np.abs((u[k, :] - np.matmul(Psi_1[:, :, k], C_LS_u_1[k, :])) / u[k, :])
#     error_1[k, :, 1] = np.abs((u[k, :] - np.matmul(Psi_1[:, :, k], C_Sparse_u_1[k, :])) / u[k, :])
#     error_1_mean[k, 0] = np.mean(error_1[k, :, 0])
#     error_1_mean[k, 1] = np.mean(error_1[k, :, 1])
#     error_2[k, :, 0] = np.abs((u[k, :] - np.matmul(Psi_2[:, :, k], C_LS_u_2[k, :])) / u[k, :])
#     error_2[k, :, 1] = np.abs((u[k, :] - np.matmul(Psi_2[:, :, k], C_Sparse_u_2[k, :])) / u[k, :])
#     error_2_mean[k, 0] = np.mean(error_2[k, :, 0])
#     error_2_mean[k, 1] = np.mean(error_2[k, :, 1])



























########################################################################################################################
#
#                                  Error ellipses
#
########################################################################################################################



from SystemIDAlgorithms.Integrate import integrate
from scipy.integrate import odeint
from scipy import interpolate

mu = 3.986e5*1e9
rho0 = 1.2
H = 7500
mass = 750/2.2046226
re = 6378000
Aref = np.pi*(24*.0254/2)**2
g0 = 9.81
Cd0 = 0.0612
Cda2 = 1.6537
Cla = 1.5658

sfh = re
sfv = np.sqrt(g0*re)
sft = sfh/sfv


def dynamics(x, ts, u):

    hs = x[0]
    theta = x[1]
    vs = x[2]
    gam = x[3]

    h = sfh * hs
    v = sfv * vs
    # t = sft * ts

    # h = hs
    # v = vs
    t = ts

    alpha = u(t)

    rho = rho0 * np.exp(-h / H)
    Cl = (Cla * alpha)
    Cd = (Cda2 * alpha ** 2 + Cd0)
    D = 0.5 * rho * v ** 2 * Cd * Aref
    L = 0.5 * rho * v ** 2 * Cl * Aref
    r = re + h

    hdot = (v * np.sin(gam))
    hsdots = sft / sfh * hdot
    thetadot = (v * np.cos(gam) / r)
    thetadots = sft * thetadot
    vdot = (-D / mass - mu * np.sin(gam) / r ** 2)
    vsdots = sft / sfv * vdot
    gamdot = (L / (mass * v) + (v / r - mu / (v * r ** 2)) * np.cos(gam))
    gamdots = sft * gamdot

    print(np.array([hsdots, thetadots, vsdots, gamdots]))

    return np.array([hsdots, thetadots, vsdots, gamdots])

# x0 = np.array([80000/sfh, 0*np.pi/180, 4000/sfv, 0])
x0 = np.array([data_h2[0, 0], data_theta2[0, 0], data_v2[0, 0], data_gamma2[0, 0]])

tspan = np.linspace(0, 10000, 10001)

alpha = interpolate.interp1d(tspan, u[:, 0], kind='linear')

tspan_int = np.linspace(0, 100, 101)
# sol = integrate(dynamics, x0, tspan_int, 1, args=(alpha,))
sol = odeint(dynamics, x0, tspan_int, args=(alpha,), rtol=1e-13, atol=1e-13)



plt.figure(1)
plt.plot(tspan, u[:, 0]*180/np.pi)
plt.plot(tspan, alpha(tspan)*180/np.pi)
plt.show()

