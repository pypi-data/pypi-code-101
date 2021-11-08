from control.matlab import *
import pandas as pd
import numpy as np


def create(df_RL, df_RLC, w):
    """
    Form all RL classes

    :param df_RL: full data of RL, straight from the .xlsx file
    :param df_RLC: data of RLC pi models, to input their RL
    :param w: pulsation, in rad/s
    :return: it builds the state space with the corresponding names
    """

    class RL_particular:
        """
        Class for a particular RL, to be used in the RL_full class

        :param df_line: row of the full RL dataframe
        :param w: pulsation, in rad/s
        :return: the state space and the names, also stores the R and L values
        """

        def __init__(self, df_line, w):
            self.name = df_line['name']
            self.R = df_line['R']
            self.L = df_line['L']
            self.bus_i = str(df_line['bus i'])
            self.bus_j = str(df_line['bus j'])

            if self.bus_i == self.bus_j:  # if it is a load
                self.A = [[-self.R / self.L, -w], [w, -self.R / self.L]]
                self.B = [[1 / self.L, 0], [0, 1 / self.L]]
                self.C = [[1, 0], [0, 1]]
                self.D = [[0, 0], [0, 0]]
                self.ssm = ss(self.A, self.B, self.C, self.D)

                self.inputs = ['vq_'+self.bus_i, 'vd_'+self.bus_i]
                self.outputs = ['iq_'+self.bus_i+'_'+self.bus_j, 'id_'+self.bus_i+'_'+self.bus_j]
                self.states = ['iq_'+self.bus_i+'_'+self.bus_j, 'id_'+self.bus_i+'_'+self.bus_j]

            else:  # if it is not a load, but a line
                self.A = [[-self.R / self.L, -w], [w, -self.R / self.L]]
                self.B = [[1 / self.L, 0, -1 / self.L, 0], [0, 1 / self.L, 0, -1 / self.L]]
                self.C = [[1, 0], [0, 1]]
                self.D = [[0, 0, 0, 0], [0, 0, 0, 0]]
                self.ssm = ss(self.A, self.B, self.C, self.D)

                self.inputs = ['vq_'+self.bus_i, 'vd_' +
                    self.bus_i, 'vq_'+self.bus_j, 'vd_'+self.bus_j]
                self.outputs = ['iq_'+self.bus_i+'_' +
                    self.bus_j, 'id_'+self.bus_i+'_'+self.bus_j]
                self.states = ['iq_'+self.bus_i+'_' +
                    self.bus_j, 'id_'+self.bus_i+'_'+self.bus_j]

    RLs = [RL_particular(df_RL.iloc[ll, :], w) for ll in range(len(df_RL))]
    RLs += [RL_particular(df_RLC.iloc[ll, :], w) for ll in range(len(df_RLC))]

    def df_device(RLs):
        """
        Store in a dataframe the info of each particular class

        :param RLs: the list of classes of a device RL
        :return: a full dataframe
        """

        data = []
        for ll in range(len(RLs)):
            data.append([RLs[ll].name, RLs[ll].R, RLs[ll].L, RLs[ll].bus_i, RLs[ll].bus_j, RLs[ll].inputs, RLs[ll].outputs, RLs[ll].states, np.array(RLs[ll].A), np.array(RLs[ll].B), np.array(RLs[ll].C), np.array(RLs[ll].D)])

        dff = pd.DataFrame(data, columns=['name', 'R', 'L', 'bus_i', 'bus_j', 'inputs', 'outputs', 'states', 'A', 'B', 'C', 'D'])

        return dff


    dff = df_device(RLs)

    return RLs, dff


