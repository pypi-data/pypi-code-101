from control.matlab import *
import pandas as pd
import numpy as np
from collections import Counter


def Qvec_builder_full(name_in, name_out, dic_i, dic_o, dic_x):
    '''
    Generates the Qq array and the name of inputs and outputs. To be used just before the final connect

    :param name_in: list of the input names
    :param name_out: list of the otput names
    :param dic_i: dictionary of inputs
    :param dic_o: dictionary of outputs
    :param dic_x: dictionary of states
    :return: the final Qq array for the connect, and the lists of names and indices of states, inputs and outputs
    '''

    Qq = []
    list_indx_x = []
    list_indx_in = [dic_i[name_in[ll]] for ll in range(len(name_in))]
    list_indx_out = [dic_o[name_out[ll]] for ll in range(len(name_out))]
    list_name_x = []
    list_name_in = [name_in[ll] for ll in range(len(name_in))]
    list_name_out = [name_out[ll] for ll in range(len(name_out))]

    for ll in range(len(dic_i)):
        name_key_in = list(dic_i.keys())[ll]
        if name_key_in in list(dic_o.keys())[:]:
            vec_Q = [dic_i[name_key_in], dic_o[name_key_in]]
        else:
            vec_Q = [dic_i[name_key_in], 0]
        Qq.append(vec_Q)

    for ll in range(len(dic_x)):
        name_key_x = list(dic_x.keys())[ll]
        list_indx_x.append(dic_x[name_key_x])
        list_name_x.append(list(dic_x.keys())[ll])

    return Qq, list_indx_x, list_indx_in, list_indx_out, list_name_x, list_name_in, list_name_out


def adapt_all_names(*ss_class):
    """
    Edits the inputs and outputs if the names coincide

    :param ss_class: tuple of all classes
    :return: list of inputs, outputs, states and the Xdivs list of classes
    """

    full_inputs = [sub_cl.inputs for cl in ss_class for sub_cl in cl]
    full_outputs = [sub_cl.outputs for cl in ss_class for sub_cl in cl]
    full_states = [sub_cl.states for cl in ss_class for sub_cl in cl]

    full_inputs = [item for sublist in full_inputs for item in sublist]
    full_outputs = [item for sublist in full_outputs for item in sublist]
    full_states = [item for sublist in full_states for item in sublist]

    # append _Tx in the name of the repeated variables
    dic_occ = Counter(full_inputs)
    dic_repeated = {}
    for key in dic_occ:
        if dic_occ[key] > 1:
            dic_repeated[key] = 0

    for ll in range(len(full_inputs)):
        if full_inputs[ll] in dic_repeated.keys():
            dic_repeated[full_inputs[ll]] += 1
            full_inputs[ll] = full_inputs[ll]+'_T'+str(dic_repeated[full_inputs[ll]])

    # create ss classes
    class Xdiv_particular:
        """
        Class for a particular variable division object

        :param ssm: full state space previously created
        :param ins: names of the inputs
        :param outs: names of the outputs
        :param sts: names of the states
        :return: store the ss and its names in a structure
        """

        def __init__(self, ssm, ins, outs, sts):
            self.ssm = ssm
            self.inputs = ins
            self.outputs = outs
            self.states = sts

    Xdivs = []  # list of classes

    for key in dic_repeated:
        A = [[]]
        B = [[]]
        C = [[]]
        Dd = [[1]] * dic_repeated[key]
        ssm = ss(A, B, C, Dd)
        inputs = [key]
        outputs = []
        for ll in range(dic_repeated[key]):
            outputs.append(key+'_T'+str(ll + 1))
            full_outputs.append(outputs[-1])
        states = []
        full_inputs.append(key)
        Xdivs.append(Xdiv_particular(ssm, inputs, outputs, states))

    return full_inputs, full_outputs, full_states, Xdivs


def exterior_ins_outs(df_ext_inputs, df_ext_outputs, VSCs):
    """
    Converts the info in the dataframe to the right names for inputs and outputs

    :param df_ext_inputs: full dataframe of external inputs
    :param df_ext_outputs: full dataframe of external outputs
    :return: list of names of inputs and outputs
    """

    full_ext_inputs = []
    for ll in range(len(df_ext_inputs)):
        if df_ext_inputs['Magnitude'][ll] == 'I':
            full_ext_inputs.append('iqx_'+str(df_ext_inputs['Bus'][ll]))
            full_ext_inputs.append('idx_'+str(df_ext_inputs['Bus'][ll]))
        elif df_ext_inputs.iloc[ll, 0] == 'V':
            full_ext_inputs.append('vq_'+str(df_ext_inputs['Bus'][ll]))
            full_ext_inputs.append('vd_'+str(df_ext_inputs['Bus'][ll]))

    full_ext_outputs = []
    for ll in range(len(df_ext_outputs)):
        if df_ext_outputs['Magnitude'][ll] == 'I':
            full_ext_outputs.append('iq_'+str(df_ext_outputs['Bus'][ll]))
            full_ext_outputs.append('id_'+str(df_ext_outputs['Bus'][ll]))
        elif df_ext_outputs['Magnitude'][ll] == 'V':
            full_ext_outputs.append('vq_'+str(df_ext_outputs['Bus'][ll]))
            full_ext_outputs.append('vd_'+str(df_ext_outputs['Bus'][ll]))

    for ll in range(len(VSCs)):  # add external inputs from the VSC
        full_ext_inputs += VSCs[ll].ext_inputs
        full_ext_outputs += VSCs[ll].ext_outputs

    return full_ext_inputs, full_ext_outputs


def append_ss(all_classes):
    """
    Append all the state spaces of all classes

    :param all_classes: list of all classes
    :return: full state space
    """

    ss_complete = []
    for cl in all_classes:
        for sub_cl in cl:
            ss_complete = append(ss_complete, sub_cl.ssm)

    return ss_complete


def dics_in_out_sts(full_inputs, full_outputs, full_states):
    """
    Builds dictionaries for inputs, outputs and states, to pass to Qvec_builder_full

    :param full_inputs: full list of inputs
    :param full_outputs: full list of outputs
    :param full_states: full list of states
    :return: dictionaries for inputs, outputs and states
    """

    dic_inputs = {}
    for ll in range(len(full_inputs)):
        dic_inputs[full_inputs[ll]] = ll + 1

    dic_outputs = {}
    for ll in range(len(full_outputs)):
        dic_outputs[full_outputs[ll]] = ll + 1

    dic_states = {}
    for ll in range(len(full_states)):
        dic_states[full_states[ll]] = ll + 1

    return dic_inputs, dic_outputs, dic_states


def FPrinter(ss_all, list_name_x0, list_name_in0, list_name_out0, prnt):
    '''
    Print the state space with the names

    :param ss_all: full state space representation
    :param list_name_x0: list of states names
    :param list_name_in0: list of inputs names
    :param list_name_out0: list of outputs names
    :param prnt: boolean to print or not
    :return: nothing, only prints
    '''

    mA = ss_all.A
    mB = ss_all.B
    mC = ss_all.C
    mD = ss_all.D

    dfA = pd.DataFrame(mA)
    dfB = pd.DataFrame(mB)
    dfC = pd.DataFrame(mC)
    dfD = pd.DataFrame(mD)

    list_name_x = []
    list_name_in = []
    list_name_out = []

    for ll in range(len(list_name_x0)):
        list_name_x.append(list_name_x0[ll])

    for ll in range(len(list_name_in0)):
        list_name_in.append(list_name_in0[ll])

    for ll in range(len(list_name_out0)):
        list_name_out.append(list_name_out0[ll])

    dfA_row = pd.DataFrame(list_name_x).T
    dfA = dfA_row.append(dfA)

    dfB_row = pd.DataFrame(list_name_in).T
    dfB = dfB_row.append(dfB)

    dfC_row = pd.DataFrame(list_name_x).T
    dfC = dfC_row.append(dfC)

    dfD_row = pd.DataFrame(list_name_in).T
    dfD = dfD_row.append(dfD)

    list_name_xa = list_name_x
    list_name_xa.insert(0, 'Identifier')
    dfA.insert(loc=0, column='t', value=list_name_xa)

    list_name_xb = list_name_x
    dfB.insert(loc=0, column='t', value=list_name_xb)

    if len(list_name_x0) > 0:
        list_name_xc = list_name_out
        list_name_xc.insert(0, 'Identifier')
        dfC.insert(loc=0, column='t', value=list_name_xc)
    else:
        new_list = []
        # new_list.append('Identifier')
        for ll in range(len(list_name_out)):
            new_list.append(list_name_out[ll])
        dfC['Identifier'] = new_list


    if len(list_name_x0) > 0:
        list_name_xd = list_name_out
        dfD.insert(loc=0, column='t', value=list_name_xd)
    else:
        list_name_xd = list_name_out
        list_name_xd.insert(0, 'Identifier')
        dfD.insert(loc=0, column='t', value=list_name_xd)


    if prnt is True:
        print('\n')
        print('A:')
        print(dfA.to_string(index=False, header=False))
        print('\n')
        print('B:')
        print(dfB.to_string(index=False, header=False))
        print('\n')
        print('C:')
        print(dfC.to_string(index=False, header=False))
        print('\n')
        print('D:')
        print(dfD.to_string(index=False, header=False))

    # write in excel
    writer = pd.ExcelWriter('results/SS_solution.xlsx')
    dfA.to_excel(writer, 'A')
    dfB.to_excel(writer, 'B')
    dfC.to_excel(writer, 'C')
    dfD.to_excel(writer, 'D')
    writer.save()

    return dfA, dfB, dfC, dfD






# def all_names(*ss_class):
#     """
#     Creates a full string of inputs, outputs and states from all classes

#     :param ss_class: tuple of all classes
#     :return: list of inputs, outputs and states
#     """

#     full_inputs = [sub_cl.inputs for cl in ss_class for sub_cl in cl]
#     full_outputs = [sub_cl.outputs for cl in ss_class for sub_cl in cl]
#     full_states = [sub_cl.states for cl in ss_class for sub_cl in cl]

#     full_inputs = [item for sublist in full_inputs for item in sublist]
#     full_outputs = [item for sublist in full_outputs for item in sublist]
#     full_states = [item for sublist in full_states for item in sublist]

#     return full_inputs, full_outputs, full_states


# def adapt_in_outs(full_inputs, full_outputs):
#     """
#     Changes names of inputs and creates the associated ss of the division

#     :param full_inputs: list of all the input names
#     :param full_outputs: list of all the outputs names
#     :return: modified list of input names, full list of output names with the division additions and the class with the ss of the division
#     """

#     # append _Tx in the name of the repeated variables
#     dic_occ = Counter(full_inputs)
#     dic_repeated = {}
#     for key in dic_occ:
#         if dic_occ[key] > 1:
#             dic_repeated[key] = 0

#     for ll in range(len(full_inputs)):
#         if full_inputs[ll] in dic_repeated.keys():
#             dic_repeated[full_inputs[ll]] += 1
#             full_inputs[ll] = full_inputs[ll]+'_T'+str(dic_repeated[full_inputs[ll]])

#     # create ss classes
#     class Xdiv_particular:
#         """
#         Class for a particular variable division object

#         :param ssm: full state space previously created
#         :param ins: names of the inputs
#         :param outs: names of the outputs
#         :param sts: names of the states
#         :return: store the ss and its names in a structure
#         """

#         def __init__(self, ssm, ins, outs, sts):
#             self.ssm = ssm
#             self.inputs = ins
#             self.outputs = outs
#             self.states = sts

#     Xdivs = []  # list of classes

#     for key in dic_repeated:
#         A = [[]]
#         B = [[]]
#         C = [[]]
#         Dd = [[1]] * dic_repeated[key]
#         ssm = ss(A, B, C, Dd)
#         inputs = [key]
#         outputs = []
#         for ll in range(dic_repeated[key]):
#             outputs.append(key+'_T'+str(ll + 1))
#             full_outputs.append(outputs[-1])
#         states = []
#         full_inputs.append(key)
#         Xdivs.append(Xdiv_particular(ssm, inputs, outputs, states))

#     return full_inputs, full_outputs, Xdivs





def I_balance(RLs, VSCs):
    """
    Form the state space for the current balances in repeated buses

    :param RLs: class with all the information about RLs
    :param VSCs: class with all the information about VSCs
    :return: it builds the state space with the corresponding names
    """

    class Isum_particular:
        """
        Class for a particular current balance object

        :param ssm: full state space previously created
        :param ins: names of the inputs
        :param outs: names of the outputs
        :param sts: names of the states
        :return: store the ss and its names in a structure
        """

        def __init__(self, ssm, ins, outs, sts):
            self.ssm = ssm
            self.inputs = ins
            self.outputs = outs
            self.states = sts

    I_sum = []  # list of classes

    # analyze buses
    bus_i_list = []
    bus_j_list = []
    bus_vsc_list = []

    for ll in range(len(RLs)):
        bus_i_list.append(int(RLs[ll].bus_i))
        bus_j_list.append(int(RLs[ll].bus_j))

    for ll in range(len(VSCs)):
        bus_vsc_list.append(int(VSCs[ll].bus_ac))


    merged_list = [*bus_i_list, *bus_j_list, *bus_vsc_list]
    dic_occ = Counter(merged_list)  # dictionary of occurrences of each bus
    list_buses = list(dict.keys(dic_occ))

    buses_repeated = []
    for key in list_buses:
        if dic_occ[key] > 1:
            buses_repeated.append(key)


    # current balance
    for bus_x in buses_repeated:
        states_Isum = []
        inputs_Isum = []
        outputs_Isum = []
        D_array_q = []  # upper row
        D_array_d = []  # lower row
        # perform search to find pairs of buses where there is a repeated bus
        for kk in range(len(bus_i_list)):  # for RLs
            if bus_i_list[kk] == bus_x:
                D_array_q.append(-1)
                D_array_q.append(0)
                D_array_d.append(0)
                D_array_d.append(-1)
                inputs_Isum.append(['iq_'+str(bus_i_list[kk])+'_'+str(bus_j_list[kk]),
                               'id_'+str(bus_i_list[kk])+'_'+str(bus_j_list[kk])])
            elif bus_j_list[kk] == bus_x:
                D_array_q.append(+1)
                D_array_q.append(0)
                D_array_d.append(0)
                D_array_d.append(+1)
                inputs_Isum.append(['iq_'+str(bus_i_list[kk])+'_'+str(bus_j_list[kk]),
                               'id_'+str(bus_i_list[kk])+'_'+str(bus_j_list[kk])])
        for kk in range(len(bus_vsc_list)):  # for VSCs, current always entering
            if bus_vsc_list[kk] == bus_x:
                D_array_q.append(-1)
                D_array_q.append(0)
                D_array_d.append(0)
                D_array_d.append(-1)
                inputs_Isum.append(['iqxv_'+str(bus_vsc_list[kk]),
                                'idxv_'+str(bus_vsc_list[kk])])

        inputs_Isum = [item for sublist in inputs_Isum for item in sublist]


        D_array = [D_array_q, D_array_d]
        outputs_Isum.append(['iqx_'+str(bus_x), 'idx_'+str(bus_x)])
        outputs_Isum = [item for sublist in outputs_Isum for item in sublist]

        states_Isum = []

        A_Isum = [[]]
        B_Isum = [[]]
        C_Isum = [[]]
        D_Isum = D_array
        ss_Isum = ss(A_Isum, B_Isum, C_Isum, D_Isum)

        I_sum.append(Isum_particular(
            ss_Isum, inputs_Isum, outputs_Isum, states_Isum))


    return I_sum




# functions of subelements
def FP_active(name_input, name_output, vcqo, vcdo, icqo, icdo, indx, dic_i, dic_o, dic_x):
    '''
    Active power calculation state space subelement

    :param name_input: array with the names of the inputs
    :param name_output: name of the output reactive power
    :param vcqo: equilibrium point for the q voltage
    :param vcdo: equilibrium point for the d voltage
    :param icqo: equilibrium point for the q current
    :param icdo: equilibrium point for the d current
    :param indx: index to identify the block, usually set to indx_VSC
    :param dic_i: dictionary of inputs
    :param dic_o: dictionary of outputs
    :param dic_x: dictionary of states
    :return: the final state space and the dictionaries of inputs, outputs and states
    '''

    A = [[]]
    B = [[]]
    C = [[]]
    D = [[3 / 2 * icqo, 3 / 2 * icdo, 3 / 2 * vcqo, 3 / 2 * vcdo]]

    indx = str(indx)
    syst = ss(A, B, C, D)

    n_i = len(dic_i) + 1
    for ll in range(len(name_input)):
        dic_i[name_input[ll]] = n_i + ll

    n_o = len(dic_o) + 1
    dic_o[name_output] = n_o

    return syst, dic_i, dic_o, dic_x


def FSum(name_in, sign_in, name_out, indx, dic_i, dic_o, dic_x):
    '''
    Sum state space subelement

    :param name_in: name of the inputs
    :param sign_in: array of +1 or -1 elements to identify the sign
    :param name_out: name of the output
    :param indx: index to identify the sum, usually set to indx_VSC
    :param dic_i: dictionary of inputs
    :param dic_o: dictionary of outputs
    :param dic_x: dictionary of states
    :return: the final state space and the dictionaries of inputs, outputs and states
    '''

    n_inp = len(name_in)

    A = [[]]
    B = [[]*n_inp]
    C = [[]]
    D = [sign_in]

    indx = str(indx)
    syst = ss(A, B, C, D)

    n_i = len(dic_i) + 1
    for ll in range(n_inp):
        dic_i[name_in[ll]] = n_i + ll

    n_o = len(dic_o) + 1
    dic_o[name_out] = n_o

    return syst, dic_i, dic_o, dic_x


def FP_controller(kp, var_in_name, var_out_name, indx, dic_i, dic_o, dic_x):
    '''
    Proportional controller state space subelement

    :param kp: proportional parameter of the controller
    :param var_in_name: name of the input of the controller
    :param var_out_name: name of the otput of the controller
    :param indx: index to identify the controller, usually set to indx_VSC
    :param dic_i: dictionary of inputs
    :param dic_o: dictionary of outputs
    :param dic_x: dictionary of states
    :return: the final state space and the dictionaries of inputs, outputs and states
    '''

    A = [[]]
    B = [[]]
    C = [[]]
    D = [[kp]]

    indx = str(indx)
    syst = ss(A, B, C, D)

    n_i = len(dic_i) + 1
    dic_i[var_in_name] = n_i

    n_o = len(dic_o) + 1
    dic_o[var_out_name] = n_o

    return syst, dic_i, dic_o, dic_x


def FPI_controller(ki, kp, var_in_name, var_out_name, indx, dic_i, dic_o, dic_x):
    '''
    PI controller state space subelement

    :param ki: integral parameter of the controller
    :param kp: proportional parameter of the controller
    :param var_in_name: name of the input of the controller
    :param var_out_name: name of the otput of the controller
    :param indx: index to identify the controller, usually set to indx_VSC
    :param dic_i: dictionary of inputs
    :param dic_o: dictionary of outputs
    :param dic_x: dictionary of states
    :return: the final state space and the dictionaries of inputs, outputs and states
    '''

    A = [[0]]
    B = [[1]]
    C = [[ki]]
    D = [[kp]]

    indx = str(indx)
    syst = ss(A, B, C, D)

    n_i = len(dic_i) + 1
    dic_i[var_in_name] = n_i

    n_o = len(dic_o) + 1
    dic_o[var_out_name] = n_o

    n_x = len(dic_x) + 1
    dic_x['int_'+var_in_name] = n_x

    return syst, dic_i, dic_o, dic_x


def FPiFi_turbine(T, F, var_in_name, var_out_name, indx, dic_i, dic_o, dic_x):
    '''
    Repetitive block inside the turbine steps

    :param T: time constant
    :param F: proportional control
    :param var_in_name: name of the input of the controller
    :param var_out_name: name of the otput of the controller
    :param indx: index to identify the SG
    :param dic_i: dictionary of inputs
    :param dic_o: dictionary of outputs
    :param dic_x: dictionary of states
    :return: the final state space and the dictionaries of inputs, outputs and states
    '''

    A = [[-1 / T]]
    B = [[1]]
    C = [[1 / T], [F / T]]
    D = [[0], [0]]

    indx = str(indx)
    syst = ss(A, B, C, D)

    n_i = len(dic_i) + 1
    for ll in range(len(var_in_name)):
        dic_i[var_in_name[ll]] = n_i + ll

    n_o = len(dic_o) + 1
    for ll in range(len(var_out_name)):
        dic_o[var_out_name[ll]] = n_o + ll

    n_x = len(dic_x) + 1
    dic_x['int_'+var_in_name[0]] = n_x

    return syst, dic_i, dic_o, dic_x


def FPiF_turbine(T, F, var_in_name, var_out_name, indx, dic_i, dic_o, dic_x):
    '''
    Final block inside the turbine

    :param T: time constant
    :param F: proportional control
    :param var_in_name: name of the input of the controller
    :param var_out_name: name of the otput of the controller
    :param indx: index to identify the SG
    :param dic_i: dictionary of inputs
    :param dic_o: dictionary of outputs
    :param dic_x: dictionary of states
    :return: the final state space and the dictionaries of inputs, outputs and states
    '''

    A = [[-1 / T]]
    B = [[1]]
    C = [[F / T]]
    D = [[0]]

    indx = str(indx)
    syst = ss(A, B, C, D)

    n_i = len(dic_i) + 1
    for ll in range(len(var_in_name)):
        dic_i[var_in_name[ll]] = n_i + ll

    n_o = len(dic_o) + 1
    for ll in range(len(var_out_name)):
        dic_o[var_out_name[ll]] = n_o + ll

    n_x = len(dic_x) + 1
    dic_x['int_'+var_in_name[0]] = n_x

    return syst, dic_i, dic_o, dic_x



def FShaft(wb, Pn, D1, D2, D3, D4, D5, H1, H2, H3, H4, H5, K12, K23, K34, K45, var_in_name, var_out_name, var_x_name, indx, dic_i, dic_o, dic_x):
    '''
    Final block inside the turbine

    :param wb: base pulsation
    :param Pn: nominal power
    :param D1:
    :param D2:
    :param D3:
    :param D4:
    :param D5:
    :param H1:
    :param H2:
    :param H3:
    :param H4:
    :param H5:
    :param K12:
    :param K23:
    :param K34:
    :param K45:
    :param var_in_name: name of the input of the shaft block
    :param var_out_name: name of the output of the shaft block
    :param var_x_name: name of the state of the shaft block
    :param indx: index to identify the SG
    :param dic_i: dictionary of inputs
    :param dic_o: dictionary of outputs
    :param dic_x: dictionary of states
    :return: the final state space and the dictionaries of inputs, outputs and states
    '''

    # follow what Luis has, rather than the slides
    A = [[-D1 / (2 * H1), 0, 0, 0, 0, -K12 / (2 * H1), K12 / (2 * H1), 0, 0, 0],
         [0, -D2 / (2 * H2), 0, 0, 0, K12 / (2 * H2), -(K12 + K23) / H2, K23 / (2 * H2), 0, 0],
         [0, 0, -D3 / (2 * H3), 0, 0, 0, K23 / (2 * H3), -(K23 + K34) / H3, K34 / (2 * H3), 0],
         [0, 0, 0, -D4 / (2 * H4), 0, 0, 0, K34 / (2 * H4), -(K34 + K45) / H4, K45 / (2 * H4)],
         [0, 0, 0, 0, -D5 / (2 * H5), 0, 0, 0, K45 / (2 * H5), -K45 / (2 * H5)],
         [wb, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, wb, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, wb, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, wb, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, wb, 0, 0, 0, 0, 0]]
    B = [[-wb / (2 * H1 * Pn), 0, 0, 0, 0],
         [0, 1 / (2 * H2), 0, 0, 0],
         [0, 0, 1 / (2 * H3), 0, 0],
         [0, 0, 0, 1 / (2 * H4), 0],
         [0, 0, 0, 0, 1 / (2 * H5)],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]
    C = [[wb, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    D = [[0, 0, 0, 0, 0]]


    indx = str(indx)
    syst = ss(A, B, C, D)

    n_i = len(dic_i) + 1
    for ll in range(len(var_in_name)):
        dic_i[var_in_name[ll]] = n_i + ll

    n_o = len(dic_o) + 1
    for ll in range(len(var_out_name)):
        dic_o[var_out_name[ll]] = n_o + ll

    n_x = len(dic_x) + 1
    for ll in range(len(var_x_name)):
        dic_x[var_x_name[ll]] = n_x + ll

    return syst, dic_i, dic_o, dic_x


# self.ss_se, self.inputs, self.outputs, self.states = FElectricCircuit(self.Rs, self.Rkd, self.Rkq1, self.Rkq2, self.Rfd_pr, self.Lmd, self.Lmq, self.Ll, self.Llkd, self.Llkq1, self.Llkq2, self.Llfd_pr, self.we0, self.isq0, self.isd0, self.ik1q0, self.ik2q0, self.ifd0, self.ikd0, self.inputs_se, self.outputs_se, self.states_se, self.indx, self.inputs, self.outputs, self.states)
def FElectricCircuit(Rs, Rkd, Rkq1, Rkq2, Rfd_pr, Lmd, Lmq, Ll, Llkd, Llkq1, Llkq2, Llfd_pr, we0, isq0, isd0, ik1q0, ik2q0, ifd0, ikd0, var_in_name, var_out_name, var_x_name, indx, dic_i, dic_o, dic_x):
    '''
    Final block for the electric circuit of the turbine

    :param Rs:
    :param Rkd:
    :param Rkq1:
    :param Rkq2:
    :param Rfd_pr:
    :param Lmd:
    :param Lmq:
    :param Ll:
    :param Llkd:
    :param Llkq1:
    :param Llkq2:
    :param Llfd_pr:
    :param we0:
    :param isq0:
    :param isd0:
    :param ik1q0:
    :param ik2q0:
    :param ifd0:
    :param ikd0:
    :param var_in_name: name of the input of the electric circuit
    :param var_out_name: name of the output of the electric circuit
    :param var_x_name: name of the state of the electric circuit
    :param indx: index to identify the SG
    :param dic_i: dictionary of inputs
    :param dic_o: dictionary of outputs
    :param dic_x: dictionary of states
    :return: the final state space and the dictionaries of inputs, outputs and states
    '''

    # follow what Luis has, rather than the slides
    # define matrices

    Lmod = [[-(Lmd + Ll), Lmd, Lmd, 0, 0, 0],
            [-Lmd, (Llkd + Lmd), Lmd, 0, 0, 0],
            [-Lmd, Lmd, (Llfd_pr + Lmd), 0, 0, 0],
            [0, 0, 0, -(Lmq + Ll), Lmq, Lmq],
            [0, 0, 0, -Lmq, (Llkq1 + Lmq), Lmq],
            [0, 0, 0, -Lmq, Lmq, (Llkq2 + Lmq)]]
    R8 = [[-Rs, 0, 0, 0, 0, 0],
          [0, Rkd, 0, 0, 0, 0],
          [0, 0, Rfd_pr, 0, 0, 0],
          [0, 0, 0, -Rs, 0, 0],
          [0, 0, 0, 0, Rkq1, 0],
          [0, 0, 0, 0, 0, Rkq2]]
    wLT = [[0, 0, 0, we0 * (Lmq + Ll), -we0 * Lmq, -we0 * Lmq],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [-we0 * (Lmd + Ll), we0 * Lmd, we0 * Lmd, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]]
    IL1 = [[1, 0, 0, 0, 0, 0, -(isq0 * (Lmq + Ll) - Lmq * ik1q0 - Lmq * ik2q0)],
           [0, 1, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, -(-isd0 * (Lmd + Ll) + Lmd * ikd0 + Lmd * ifd0)],
           [0, 0, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 1, 0]]
    Anp = np.matmul(- np.linalg.inv(np.array(Lmod)), (np.array(R8) + np.array(wLT)))
    Bnp = np.matmul(np.linalg.inv(np.array(Lmod)), np.array(IL1))
    A = Anp.tolist()
    B = Bnp.tolist()
    C = [[1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 1],
         [3 / 2 * (isq0 * (-Lmd + Lmq) - Lmq * (ik1q0 + ik2q0)), 3 / 2 * Lmd * isq0, 3 / 2 * Lmd * isq0, 3 / 2 * (isd0 * (- Lmd + Lmq) + Lmd * (ikd0 + ifd0)), -3 / 2 * Lmq * isd0, -3 / 2 * Lmq * isd0]]
    D = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]


    # process
    indx = str(indx)
    syst = ss(A, B, C, D)

    n_i = len(dic_i) + 1
    for kk in range(len(var_in_name)):
        dic_i[var_in_name[kk]] = n_i + kk

    n_o = len(dic_o) + 1
    for kk in range(len(var_out_name)):
        dic_o[var_out_name[kk]] = n_o + kk

    n_x = len(dic_x) + 1
    for kk in range(len(var_x_name)):
        dic_x[var_x_name[kk]] = n_x + kk

    return syst, dic_i, dic_o, dic_x




def FNode(name_in, name_out, indx, dic_i, dic_o, dic_x):
    '''
    Node state space subelement, to have a duplicate variable

    :param name_in: name of the input
    :param name_out: name of the outputs
    :param indx: index to identify the node, usually set to indx_VSC
    :param dic_i: dictionary of inputs
    :param dic_o: dictionary of outputs
    :param dic_x: dictionary of states
    :return: the final state space and the dictionaries of inputs, outputs and states
    '''

    n_out = len(name_out)

    A = [[]]
    B = [[]]
    C = [[]]
    D = [[1]] * n_out

    indx = str(indx)
    syst = ss(A, B, C, D)

    n_i = len(dic_i) + 1
    dic_i[name_in] = n_i

    n_o = len(dic_o) + 1
    for ll in range(n_out):
        dic_o[name_out[ll]] = n_o + ll

    return syst, dic_i, dic_o, dic_x


def FAC_voltage(name_input, name_output, vcqo, vcdo, indx, dic_i, dic_o, dic_x):
    '''
    AC voltage absolute value calculation state space subelement

    :param name_input: array of the input names
    :param name_output: name of the output voltage
    :param vcqo: equilibrium point for the q voltage
    :param vcdo: equilibrium point for the d voltage
    :param indx: index to identify the block, usually set to indx_VSC
    :param dic_i: dictionary of inputs
    :param dic_o: dictionary of outputs
    :param dic_x: dictionary of states
    :return: the final state space and the dictionaries of inputs, outputs and states
    '''

    A = [[]]
    B = [[]]
    C = [[]]
    D = [[vcqo / np.sqrt(vcqo ** 2 + vcdo ** 2), vcdo / np.sqrt(vcqo ** 2 + vcdo ** 2)]]

    indx = str(indx)
    syst = ss(A, B, C, D)

    n_i = len(dic_i) + 1
    for ll in range(len(name_input)):
        dic_i[name_input[ll]] = n_i + ll

    n_o = len(dic_o) + 1
    dic_o[name_output] = n_o

    return syst, dic_i, dic_o, dic_x


def FAC_voltage_SG(name_input, name_output, vcqo, vcdo, Vbase, indx, dic_i, dic_o, dic_x):
    '''
    AC voltage absolute value calculation state space subelement, for the SG

    :param name_input: array of the input names
    :param name_output: name of the output voltage
    :param vcqo: equilibrium point for the q voltage
    :param vcdo: equilibrium point for the d voltage
    :param Vbase: base voltage, only used in the SG
    :param indx: index to identify the block, usually set to indx_VSC
    :param dic_i: dictionary of inputs
    :param dic_o: dictionary of outputs
    :param dic_x: dictionary of states
    :return: the final state space and the dictionaries of inputs, outputs and states
    '''

    A = [[]]
    B = [[]]
    C = [[]]
    D = [[vcqo / np.sqrt(vcqo ** 2 + vcdo ** 2), vcdo / np.sqrt(vcqo ** 2 + vcdo ** 2)]] * 1 / Vbase

    indx = str(indx)
    syst = ss(A, B, C, D)

    n_i = len(dic_i) + 1
    for ll in range(len(name_input)):
        dic_i[name_input[ll]] = n_i + ll

    n_o = len(dic_o) + 1
    dic_o[name_output] = n_o

    return syst, dic_i, dic_o, dic_x


def FG_exc(Rfd, Lmd, Vbase, NsNf, Ka, Ta, Tb, Tc, name_input, name_output, name_state, indx, dic_i, dic_o, dic_x):
    '''
    AC voltage absolute value calculation state space subelement, for the SG

    :param Rfd:
    :param Lmd:
    :param Vbase:
    :param NsNf:
    :param Ka: constant of the control of the exciter
    :param Ta: first time constant
    :param Tb: second time constant
    :param Tc: third time constant
    :param name_input: array of the input names
    :param name_output: name of the output voltage
    :param indx: index to identify the block, usually set to indx_SG
    :param dic_i: dictionary of inputs
    :param dic_o: dictionary of outputs
    :param dic_x: dictionary of states
    :return: the final state space and the dictionaries of inputs, outputs and states
    '''

    Ksg = Rfd / Lmd * Vbase * NsNf

    A = [[0, 1], [-1 / (Ta * Tb), -1 / Tb - 1 / Ta]]
    B = [[0], [1]]
    C = [[Ksg * Ka / (Ta * Tb), Ksg * Tc * Ka / (Ta * Tb)]]
    D = [[0]]

    indx = str(indx)
    syst = ss(A, B, C, D)

    n_i = len(dic_i) + 1
    dic_i[name_input] = n_i

    n_o = len(dic_o) + 1
    dic_o[name_output] = n_o

    n_x = len(dic_x) + 1
    dic_x[name_state[0]] = n_x
    dic_x[name_state[1]] = n_x + 1

    return syst, dic_i, dic_o, dic_x




def FQ_active(name_input, name_output, vcqo, vcdo, icqo, icdo, indx, dic_i, dic_o, dic_x):
    '''
    Reactive power calculation state space subelement

    :param name_input: array with the names of the inputs
    :param name_output: name of the output reactive power
    :param vcqo: equilibrium point for the q voltage
    :param vcdo: equilibrium point for the d voltage
    :param icqo: equilibrium point for the q current
    :param icdo: equilibrium point for the d current
    :param indx: index to identify the block, usually set to indx_VSC
    :param dic_i: dictionary of inputs
    :param dic_o: dictionary of outputs
    :param dic_x: dictionary of states
    :return: the final state space and the dictionaries of inputs, outputs and states
    '''

    A = [[]]
    B = [[]]
    C = [[]]
    D = [[3 / 2 * icdo, - 3 / 2 * icqo, - 3 / 2 * vcdo, 3 / 2 * vcqo]]

    indx = str(indx)
    syst = ss(A, B, C, D)

    n_i = len(dic_i) + 1
    for ll in range(len(name_input)):
        dic_i[name_input[ll]] = n_i + ll

    n_o = len(dic_o) + 1
    dic_o[name_output] = n_o

    return syst, dic_i, dic_o, dic_x


def BuildDictionary(list_indx, list_name):
    '''
    Create a dictionary from the list indices and names

    :param list_indx: array of indices, from 1 to n
    :param list_name: array of the names linked to the indices
    :return: dictionary with both lists merged
    '''

    dicc = {}
    len_indx = len(list_indx)
    len_name = len(list_name)
    if len_indx != len_name:
        print('Error, lengths do not match')
    else:
        for ll in range(len_indx):
            dicc[list_name[ll]] = list_indx[ll]

    return dicc


def FProduct(name_in, ct_val, name_out, indx, dic_i, dic_o, dic_x):
    '''
    Product state space subelement

    :param name_in: name of the input
    :param ct_val: constant value by which we multiply
    :param name_out: name of the output
    :param indx: index to identify the product, usually set to indx_VSC
    :param dic_i: dictionary of inputs
    :param dic_o: dictionary of outputs
    :param dic_x: dictionary of states
    :return: the final state space and the dictionaries of inputs, outputs and states
    '''

    A = [[]]
    B = [[]]
    C = [[]]
    D = [[ct_val]]

    indx = str(indx)
    syst = ss(A, B, C, D)

    n_i = len(dic_i) + 1
    if name_in not in dic_i:
        dic_i[name_in] = n_i

    n_o = len(dic_o) + 1
    dic_o[name_out] = n_o


    return syst, dic_i, dic_o, dic_x



