from control.matlab import *
import pandas as pd
import numpy as np


def create(df_RLC, w):
    """
    Form all C classes, to output the voltages only

    :param df_RLC: full data of RLC, straight from the .xlsx file
    :param w: pulsation, in rad/s
    :return: it builds the state space with the corresponding names
    """


    class C_particular:
        """
        Class for a particular capacitor to output its particular voltage

        :param df_line: row of the full RLC dataframe
        :param w: pulsation, in rad/s
        :param summed_C: value of the added capacitors at this bus
        :return: the state space and the names, also stores the C value
        """

        def __init__(self, bus, w, summed_C):
            self.bus = bus
            self.sumC = summed_C


            self.A = [
                [0, -w],
                [w, 0]
            ]
            self.B = [
                [1 / self.sumC, 0],
                [0, 1 / self.sumC]
            ]
            self.C = [
                [1, 0],
                [0, 1]
            ]
            self.D = [
                [0, 0],
                [0, 0]
            ]

            self.ssm = ss(self.A, self.B, self.C, self.D)

            self.inputs = ['iqx_'+str(self.bus), 'idx_'+str(self.bus)]
            self.outputs = ['vq_'+str(self.bus), 'vd_'+str(self.bus)]
            self.states = ['vq_'+str(self.bus), 'vd_'+str(self.bus)]



    def sum_C(df_RLC):
        """
        Adds all the capacitors placed in the same bus
        :param df_RLC: dataframe of the RLC sheet
        :return: dictionary bus : C value
        """

        summed_C = dict()
        for ll in range(len(df_RLC)):
            if df_RLC['bus i'][ll] in summed_C:
                summed_C[df_RLC['bus i'][ll]] += df_RLC['C'][ll]
            else:
                summed_C[df_RLC['bus i'][ll]] = df_RLC['C'][ll]

            if df_RLC['bus j'][ll] in summed_C:
                summed_C[df_RLC['bus j'][ll]] += df_RLC['C'][ll]
            else:
                summed_C[df_RLC['bus j'][ll]] = df_RLC['C'][ll]

        return summed_C


    def build_C(row, w, done_V, summed_C):
        """
        Builds the full Cs classes according to the already expressed as output voltages

        :param row: row of the form: df_RLC.iloc[ll, :]
        :param w: pulsation in rad/s
        :param done_V: vector that stores the index of the bus if it has been already used as an output
        :param summed_C: vector with sums of capacitors at each bus
        :return: row of the full class structure to append and updated done_V object
        """
        error = False
        if row['bus i'] not in done_V:
            RLC_row = C_particular(int(row['bus i']), w, summed_C[int(row['bus i'])])
            done_V.append(int(row['bus i']))
        elif row['bus j'] not in done_V:
            RLC_row = C_particular(int(row['bus j']), w, summed_C[int(row['bus j'])])
            done_V.append(int(row['bus j']))
        else:
            error = True

        return RLC_row, done_V, error


    summed_C = sum_C(df_RLC)
    done_V = []
    RLCs = []
    for ll in range(len(df_RLC)):
        RLC_row, done_V, error = build_C(df_RLC.iloc[ll, :], w, done_V, summed_C)
        if error is False:
            RLCs.append(RLC_row)


    def df_device(RLCs):
        """
        Store in a dataframe the info of each particular class

        :param RLCs: the list of classes of a device RLC
        :return: a full dataframe
        """

        data = []
        for ll in range(len(RLCs)):
            data.append([RLCs[ll].bus, RLCs[ll].sumC, RLCs[ll].inputs, RLCs[ll].outputs, RLCs[ll].states, RLCs[ll].A, RLCs[ll].B, RLCs[ll].C, RLCs[ll].D])

        dff = pd.DataFrame(data, columns=['bus', 'sumC', 'inputs', 'outputs', 'states', 'A', 'B', 'C', 'D'])

        return dff


    dff = df_device(RLCs)

    return RLCs, dff


