from optimaldesign.interior_point_method import FunctionTarget, FunctionTargetSupp
import jax.numpy as np
import jax.scipy as sp
from jax import jit, ops
from functools import partial


class DCritWeights(FunctionTarget):
    def set_constants(self, linear_model, supp):
        self.linear_model = linear_model
        self.design = linear_model.design(supp)
        self.supp = supp

    @partial(jit, static_argnums=(0,))
    def compute(self, weights):
        fim = self.linear_model.fim(weights, self.supp)
        phi = np.dot(
            self.design,
            sp.linalg.lu_solve(sp.linalg.lu_factor(fim), self.design.T),
        )
        det = np.linalg.det(fim)
        value = -np.log(det)
        gradient = -np.diag(phi)
        hessian = phi ** 2
        return value, gradient, hessian


class DCritSupp(FunctionTargetSupp):
    def set_constants(self, linear_model, weights, supp):
        self.linear_model = linear_model
        self.fim = linear_model.fim(weights, supp)

    @partial(jit, static_argnums=(0,), backend="cpu")
    def compute(self, x):
        feature_vec = self.linear_model.feature_vec(x)
        inv_fim_design = sp.linalg.lu_solve(sp.linalg.lu_factor(self.fim), feature_vec)
        jac = self.linear_model.jac(x)
        value = -np.dot(feature_vec, inv_fim_design) + self.linear_model.feature_size
        gradient = -np.dot(jac.T, inv_fim_design)

        return value, gradient


class CCritWeights(FunctionTarget):
    def set_constants(self, linear_model, supp, m):
        self.linear_model = linear_model
        self.design = linear_model.design(supp)
        self.supp = supp
        self.m = m

    @partial(jit, static_argnums=(0,))
    def compute(self, weights):
        feat_size = self.linear_model.selected_feature_size
        fim = self.linear_model.fim(weights, self.supp)

        e_n = np.ones(feat_size)
        offset = feat_size - self.m
        e_n = ops.index_update(e_n, ops.index[:offset], 0)
        fim_e_n = sp.linalg.lu_solve(sp.linalg.lu_factor(fim), e_n)
        theta = np.dot(self.design, fim_e_n)
        phi = np.dot(e_n, fim_e_n)

        value = np.log(phi)
        gradient = -1.0 / phi * theta ** 2
        hessian = np.outer(gradient, gradient) + 2.0 / phi * np.multiply(
            np.dot(
                self.design, sp.linalg.lu_solve(sp.linalg.lu_factor(fim), self.design.T)
            ),
            np.outer(theta, theta),
        )

        return value, gradient, hessian


class CCritSupp(FunctionTargetSupp):
    def set_constants(self, linear_model, weights, supp, m):
        self.linear_model = linear_model
        self.fim = linear_model.fim(weights, supp)
        self.supp = supp
        self.m = m

    @partial(jit, static_argnums=(0,), backend="cpu")
    def compute(self, x):
        feat_size = self.linear_model.selected_feature_size

        e_n = np.ones(feat_size)
        offset = feat_size - self.m
        e_n = ops.index_update(e_n, ops.index[:offset], 0)

        feature_vec = self.linear_model.feature_vec(x)
        jac = self.linear_model.jac(x)
        fim_e_n = sp.linalg.lu_solve(sp.linalg.lu_factor(self.fim), e_n)
        theta = np.dot(feature_vec, fim_e_n)
        phi = np.dot(e_n, fim_e_n)
        jac_fim_e_n = np.dot(jac.T, fim_e_n)

        value = phi - theta ** 2
        gradient = -theta * jac_fim_e_n

        return value, gradient
