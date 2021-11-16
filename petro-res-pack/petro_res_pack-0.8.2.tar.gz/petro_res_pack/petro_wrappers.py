import gym
import numpy as np

import petro_res_pack
from .sub_matrices_utils import get_sub_matrix
from .petro_env import preprocess_p


class KernelWrapper(gym.ObservationWrapper):
    def __init__(self, env: petro_res_pack.petro_env.PetroEnv, kernel_size):
        """
        Args:
            kernel_size: size of well vicinity
            env: environment to overwrite
        Returns: (1, -1) observation of environment. Environment observation is an vector (n_wells, k_size, k_size, 2)
            reshaped to (1, -1).
            Preprocess as in main env.
        """
        super().__init__(env)
        self.kernel_size = kernel_size
        # self.observation_space = gym.spaces.Box(0, 1, (self.n,))

    def observation(self, obs) -> np.ndarray:
        """
        returns (1, -1) observation of environment. Environment observation is an vector (n_wells, k_size, k_size, 2)
        reshaped to (1, -1).
        Preprocess as in main env.
        Args:
            obs:

        Returns:

        """
        new_obs = self.obs_as_kernel()
        return new_obs

    def obs_as_kernel(self) -> np.ndarray:
        """
        Returns:1, -1) observation of environment. Environment observation is an vector (n_wells, k_size, k_size, 2)
            reshaped to (1, -1).

        """

        s_o_sc = self.preprocess_s(self.s_o)
        p_sc = preprocess_p(self.p)

        sat_out = np.stack(self.extract_kernels(s_o_sc, pad_value=self.s_o.bound_v),
                           axis=2)
        pre_out = np.stack(self.extract_kernels(p_sc, pad_value=self.p.bound_v),
                           axis=2)
        out = np.stack([sat_out, pre_out], axis=3)
        out = out.reshape((self.kernel_size,
                           self.kernel_size,
                           self.get_n_wells(), 2))
        out = np.transpose(a=out, axes=(2, 0, 1, 3))
        out = out.reshape((self.get_n_wells(), -1))
        out = out.reshape((1, -1))
        return out

    def extract_kernels(self, state: np.ndarray, pad_value: float) -> list:
        """
        Extract list of sub matrices, placed in well positions
        Args:
            state: 1d array, as ResState.values
            pad_value: value for padding

        Returns: list of square sub matrices

        """
        state = state.reshape((self.prop.nx, self.prop.ny))
        sub_matrices = []
        for w_pos in self.pos_r:
            x_sm = get_sub_matrix(x=state, k_size=self.kernel_size,
                                  center=w_pos, pad_value=pad_value)
            sub_matrices.append(x_sm)
        return sub_matrices
