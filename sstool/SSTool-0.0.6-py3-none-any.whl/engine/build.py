# from SSTool.engine.devices import RL
# from SSTool.engine import parse
import pandas as pd
import os.path
from control.matlab import *
from engine import parse
from engine.devices import RL, C, VSC, SG, auxiliaries


def create_syst(excel_file):
    """
    Creates the full state space of a complete system

    :param excel_file: .xlsx file path with multiple sheets
    :return: the full data structure of the state space
    """

    class syst:
        def __init__(self, syst_RL, syst_C, syst_VSC, syst_SG, RLs, Cs, VSCs, SGs, ISum, Xdivs, ss_final, inputs, outputs, states):
            """
            Store all the initial information here

            :param syst_RL: dataframe about the info of RLs
            :param syst_C: dataframe about the info of Cs
            :param syst_VSC: dataframe about the info of VSCs
            :param syst_SG: dataframe about the info of SGs
            :param RLs: list of classes of RLs
            :param Cs: list of classes of Cs
            :param VSCs: list of classes of VSCs
            :param SGs: list of classes of SGs
            :param ISum: list of classes of ISum
            :param Xdivs: list of classes of Xdivs
            :param ss_final: final state space
            :param inputs: full external inputs
            :param outputs: full external outputs
            :param states: full states
            :return: nothing, just store
            """

            self.syst_RL = syst_RL
            self.syst_C = syst_C
            self.syst_VSC = syst_VSC
            self.syst_SG = syst_SG

            self.RLs = RLs
            self.Cs = Cs
            self.VSCs = VSCs
            self.SGs = SGs
            self.ISum = ISum
            self.Xdivs = Xdivs

            self.ss_final = ss_final
            self.inputs = inputs
            self.outputs = outputs
            self.states = states


    print('---------------------------------------')
    print('Running engine...')

    # 0. parse
    dfs, w, Sb = parse.parser(excel_file)

    # 1. build particular SS of each element
    RLs, syst_RL = RL.create(dfs['RL'], dfs['RLC'], w)
    Cs, syst_C = C.create(dfs['RLC'], w)
    VSCs, syst_VSC = VSC.create(dfs['VSC'], w)
    SGs, syst_SG = SG.create(dfs['SG'], w)

    # 2. build auxiliary SS
    ISum = auxiliaries.I_balance(RLs, VSCs)  # exclude RLCs or any class where current is an input
    full_inputs, full_outputs, full_states, Xdivs = auxiliaries.adapt_all_names(RLs, Cs, VSCs, SGs, ISum)

    # 3. prepare final connect
    all_classes = [RLs, Cs, VSCs, SGs, ISum, Xdivs]  # unify everything. Use the same order as before!
    ext_inputs, ext_outputs = auxiliaries.exterior_ins_outs(dfs['External_inputs'], dfs['External_outputs'], VSCs)
    ss_complete = auxiliaries.append_ss(all_classes)
    dic_inputs, dic_outputs, dic_states = auxiliaries.dics_in_out_sts(full_inputs, full_outputs, full_states)
    Qq, list_indx_x, list_indx_in, list_indx_out, list_name_x, list_name_in, list_name_out = auxiliaries.Qvec_builder_full(ext_inputs, ext_outputs, dic_inputs, dic_outputs, dic_states)

    # 4. final connect
    ss_final = connect(ss_complete, Qq, list_indx_in, list_indx_out)
    # dfA, dfB, dfC, dfD = auxiliaries.FPrinter(ss_final, list_name_x, list_name_in, list_name_out, prnt=False)  # to nicely print

    # 5. store all information
    full_syst = syst(syst_RL, syst_C, syst_VSC, syst_SG, RLs, Cs, VSCs, SGs, ISum, Xdivs, ss_final, list_name_in, list_name_out, list_name_x)

    print('Succesfully finished!')
    print('---------------------------------------')

    return full_syst


def store_info(data, name):
    """
    Store a dataframe of interest

    :param data: the dataframe from syst to store in a .xlsx file
    :param name: name of the .xlsx file to be stored in the results folder
    :return: nothing, just stores
    """

    dff = pd.DataFrame(data)
    dff.to_excel('results/'+name+'.xlsx', sheet_name=name)
