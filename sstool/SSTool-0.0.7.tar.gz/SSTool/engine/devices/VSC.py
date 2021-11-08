from control.matlab import *
import pandas as pd
import numpy as np
from engine.devices.auxiliaries import *


def create(df_VSC, w):
    """
    Form all VSCs classes

    :param df_VSC: full data of VSC, straight from the .xlsx file
    :param w: pulsation, in rad/s
    :return: it builds the state space with the corresponding names
    """

    class VSC_particular:
        """
        Class for a particular VSC

        :param df_VSC: row of the full VSC dataframe
        :param w: pulsation, in rad/s
        :param indx: index of the VSC, from 0 to n
        :return: the state space and the names, also stores the input values
        """


        class BP_outer:
            """
            Class for the active power outer loop

            :param indx: index of the VSC
            :param vcq0: equilibrium point for the q voltage
            :param vcd0: equilibrium point for the d voltage
            :param icq0: equilibrium point for the q current
            :param icd0: equilibrium point for the d current
            :param kp_f: proportional constant for the frequency control
            :param kp_p: proportional constant for the active power control
            :param ki_p: integral constant for the active power control
            :return: state space of the active power outer loop with the inputs, outputs, states
            """

            def __init__(self, indx, vcq0, vcd0, icq0, icd0, kp_f, kp_p, ki_p):
                # store variables in the structure
                self.indx = indx
                self.vcq0 = vcq0
                self.vcd0 = vcd0
                self.icq0 = icq0
                self.icd0 = icd0
                self.kp_f = kp_f
                self.kp_p = kp_p
                self.ki_p = ki_p

                # initialize dictionaries and get the index
                self.inputs = {}
                self.outputs = {}
                self.states = {}
                istr = str(self.indx)

                # Active power calculation
                self.inputs_p = ['vcq_'+istr+'_P', 'vcd_'+istr+'_P', 'icq_'+istr+'_P', 'icd_'+istr+'_P']
                self.outputs_p = 'AP_c_'+istr
                self.ss_p, self.inputs, self.outputs, self.states = FP_active(self.inputs_p, self.outputs_p, self.vcq0, self.vcd0, self.icq0, self.icd0, self.indx, self.inputs, self.outputs, self.states)

                # Sum of powers
                self.inputs_s2 = ['Ap_ref_'+istr, 'AP_c_'+istr]
                self.sign_s2 = [+1, -1]
                self.outputs_s2 = 'diff_AP_'+istr
                self.ss_s2, self.inputs, self.outputs, self.states = FSum(self.inputs_s2, self.sign_s2, self.outputs_s2, self.indx, self.inputs, self.outputs, self.states)

                # PI controller
                self.inputs_PI2 = 'diff_AP_'+istr
                self.outputs_PI2 = 'icq_ref_'+istr
                self.ss_PI2, self.inputs, self.outputs, self.states = FPI_controller(self.ki_p, self.kp_p, self.inputs_PI2, self.outputs_PI2, self.indx, self.inputs, self.outputs, self.states)


                # Merge
                self.ss_full = append(self.ss_p, self.ss_s2, self.ss_PI2)
                self.inputs_full = ['vcq_'+istr+'_P', 'vcd_'+istr+'_P', 'icq_'+istr+'_P', 'icd_'+istr+'_P', 'Ap_ref_'+istr]  # removed w_ref
                self.outputs_full = ['icq_ref_'+istr]
                self.Qq, self.indx_x, self.indx_in, self.indx_out, self.name_x, self.name_in, self.name_out = Qvec_builder_full(self.inputs_full, self.outputs_full, self.inputs, self.outputs, self.states)
                self.ss_final = connect(self.ss_full, self.Qq, self.indx_in, self.indx_out)

                # Refer inputs, outputs and states to index 1
                self.indx_in = [ll + 1 for ll in range(len(self.indx_in))]
                self.indx_out = [ll + 1 for ll in range(len(self.indx_out))]
                self.indx_x = [ll + 1 for ll in range(len(self.indx_x))]

                self.dicc_in = BuildDictionary(self.indx_in, self.name_in)
                self.dicc_out = BuildDictionary(self.indx_out, self.name_out)
                self.dicc_x = BuildDictionary(self.indx_x, self.name_x)


        class BQ_outer:
            """
            Class for the reactive power outer loop

            :param indx: index of the VSC
            :param vcq0: equilibrium point for the q voltage
            :param vcd0: equilibrium point for the d voltage
            :param icq0: equilibrium point for the q current
            :param icd0: equilibrium point for the d current
            :param kp_v: proportional constant for the voltage control
            :param ki_v: integral constant for the voltage control
            :param kp_q: proportional constant for the reactive power control
            :param ki_q: integral constant for the reactive power control
            :return: state space of the reactive power outer loop with the inputs, outputs, states
            """

            def __init__(self, indx, vcq0, vcd0, icq0, icd0, kp_v, ki_v, kp_q, ki_q):
                # store variables in the structure
                self.indx = indx
                self.vcq0 = vcq0
                self.vcd0 = vcd0
                self.icq0 = icq0
                self.icd0 = icd0
                self.kp_v = kp_v
                self.ki_v = ki_v
                self.kp_q = kp_q
                self.ki_q = ki_q

                # initialize dictionaries and get the index
                self.inputs = {}
                self.outputs = {}
                self.states = {}
                istr = str(self.indx)

                # Q active  calculation
                self.inputs_q = ['vcq_'+istr+'_Q', 'vcd_'+istr+'_Q', 'icq_'+istr+'_Q', 'icd_'+istr+'_Q']
                self.outputs_q = 'AQ_c_'+istr
                self.ss_q, self.inputs, self.outputs, self.states = FQ_active(self.inputs_q, self.outputs_q, self.vcq0, self.vcd0, self.icq0, self.icd0, self.indx, self.inputs, self.outputs, self.states)

                # sum on the Q control side
                self.inputs_s2 = ['Aq_ref_'+istr, 'AQ_c_'+istr]
                self.sign_s2 = [+1, -1]
                self.outputs_s2 = 'diff_AQ_'+istr
                self.ss_s2, self.inputs, self.outputs, self.states = FSum(self.inputs_s2, self.sign_s2, self.outputs_s2, self.indx, self.inputs, self.outputs, self.states)

                # proportional integral controller
                self.inputs_PI = 'diff_AQ_'+istr
                self.outputs_PI = 'icd_ref_'+istr
                self.ss_PI, self.inputs, self.outputs, self.states = FPI_controller(self.ki_q, self.kp_q, self.inputs_PI, self.outputs_PI, self.indx, self.inputs, self.outputs, self.states)

                # Merge
                self.ss_full = append(self.ss_q, self.ss_s2, self.ss_PI)  # removed v_ref loop
                self.inputs_full = ['vcq_'+istr+'_Q', 'vcd_'+istr+'_Q', 'icq_'+istr+'_Q', 'icd_'+istr+'_Q', 'Aq_ref_'+istr]  # removed v_ref
                self.outputs_full = ['icd_ref_'+istr]
                self.Qq, self.indx_x, self.indx_in, self.indx_out, self.name_x, self.name_in, self.name_out = Qvec_builder_full(self.inputs_full, self.outputs_full, self.inputs, self.outputs, self.states)
                self.ss_final = connect(self.ss_full, self.Qq, self.indx_in, self.indx_out)

                # Refer inputs, outputs and states to index 1
                self.indx_in = [ll + 1 for ll in range(len(self.indx_in))]
                self.indx_out = [ll + 1 for ll in range(len(self.indx_out))]
                self.indx_x = [ll + 1 for ll in range(len(self.indx_x))]

                self.dicc_in = BuildDictionary(self.indx_in, self.name_in)
                self.dicc_out = BuildDictionary(self.indx_out, self.name_out)
                self.dicc_x = BuildDictionary(self.indx_x, self.name_x)


        class BPLL:
            """
            Class for the PLL (the simple version, built directly)

            :param indx: index of the VSC
            :param kp_pll: proportional constant for the frequency tracking
            :param ki_pll: integral constant for the frequency tracking
            :return: state space of the PLL with the inputs, outputs, states
            """

            def __init__(self, indx, kp_pll, ki_pll):
                # store variables in the structure
                self.indx = indx
                self.kp_pll = kp_pll
                self.ki_pll = ki_pll

                # initialize dictionaries and get the index
                self.inputs = {}
                self.outputs = {}
                self.states = {}
                istr = str(self.indx)

                # directly obtained ss
                A = [[0, 1], [0, 0]]
                B = [[0], [1]]
                C = [[-self.ki_pll, -self.kp_pll]]
                D = [[0]]

                self.ss_full = ss(A, B, C, D)

                self.states['PLL_etheta1_'+istr] = 1
                self.states['PLL_etheta2_'+istr] = 2
                self.inputs['vmd_'+istr+'_PLL'] = 1
                self.outputs['ang_'+istr] = 1
                # self.outputs['w_c_'+istr] = 2

                # Merge
                self.inputs_full = ['vmd_'+istr+'_PLL']
                self.outputs_full = ['ang_'+istr]
                self.Qq, self.indx_x, self.indx_in, self.indx_out, self.name_x, self.name_in, self.name_out = Qvec_builder_full(self.inputs_full, self.outputs_full, self.inputs, self.outputs, self.states)
                self.ss_final = connect(self.ss_full, self.Qq, self.indx_in, self.indx_out)

                # Refer inputs, outputs and states to index 1
                self.indx_in = [ll + 1 for ll in range(len(self.indx_in))]
                self.indx_out = [ll + 1 for ll in range(len(self.indx_out))]
                self.indx_x = [ll + 1 for ll in range(len(self.indx_x))]

                self.dicc_in = BuildDictionary(self.indx_in, self.name_in)
                self.dicc_out = BuildDictionary(self.indx_out, self.name_out)
                self.dicc_x = BuildDictionary(self.indx_x, self.name_x)


        class BInnerCurrentLoop:
            """
            Class for the inner current control loop

            :param indx: index of the VSC
            :param w: pulsation in rad/s
            :param Lc: inductance value to be used in the decoupling
            :param kp_i: proportional parameter of the current loop controller
            :param ki_i: integral parameter of the current loop controller
            :return: state space of the inner current control loop with the inputs, outputs, states
            """

            def __init__(self, indx, w, Lc, kp_i, ki_i):
                # store variables in the structure
                self.indx = indx
                self.w = w
                self.Lc = Lc
                self.kp_i = kp_i
                self.ki_i = ki_i

                # initialize dictionaries and get the index
                self.inputs = {}
                self.outputs = {}
                self.states = {}
                istr = str(self.indx)

                # division of the q current
                self.inputs_n1 = 'icq_'+istr+'_curr'
                self.outputs_n1 = ['icq_v1_'+istr, 'icq_v2_'+istr]
                self.ss_n1, self.inputs, self.outputs, self.states = FNode(self.inputs_n1, self.outputs_n1, self.indx, self.inputs, self.outputs, self.states)

                # division of the d current
                self.inputs_n2 = 'icd_'+istr+'_curr'
                self.outputs_n2 = ['icd_v1_'+istr, 'icd_v2_'+istr]
                self.ss_n2, self.inputs, self.outputs, self.states = FNode(self.inputs_n2, self.outputs_n2, self.indx, self.inputs, self.outputs, self.states)

                # comparator of q currents
                self.inputs_s1 = ['icq_ref_'+istr, 'icq_v1_'+istr]
                self.sign_s1 = [+1, -1]
                self.outputs_s1 = 'err_icq_'+istr
                self.ss_s1, self.inputs, self.outputs, self.states = FSum(self.inputs_s1, self.sign_s1, self.outputs_s1, self.indx, self.inputs, self.outputs, self.states)

                # comparator of d currents
                self.inputs_s2 = ['icd_ref_'+istr, 'icd_v1_'+istr]
                self.sign_s2 = [+1, -1]
                self.outputs_s2 = 'err_icd_'+istr
                self.ss_s2, self.inputs, self.outputs, self.states = FSum(self.inputs_s2, self.sign_s2, self.outputs_s2, self.indx, self.inputs, self.outputs, self.states)

                # PI controller for the q currents
                self.inputs_PI1 = 'err_icq_'+istr
                self.outputs_PI1 = 'err_vcq_'+istr
                self.ss_PI1, self.inputs, self.outputs, self.states = FPI_controller(self.ki_i, self.kp_i, self.inputs_PI1, self.outputs_PI1, self.indx, self.inputs, self.outputs, self.states)

                # PI controller for the d currents
                self.inputs_PI2 = 'err_icd_'+istr
                self.outputs_PI2 = 'err_vcd_'+istr
                self.ss_PI2, self.inputs, self.outputs, self.states = FPI_controller(self.ki_i, self.kp_i, self.inputs_PI2, self.outputs_PI2, self.indx, self.inputs, self.outputs, self.states)

                # product q component in the decoupling
                self.inputs_X1 = 'icq_v2_'+istr
                self.outputs_X1 = 'ixcq_'+istr
                self.ct_val = w * Lc
                self.ss_X1, self.inputs, self.outputs, self.states = FProduct(self.inputs_X1, self.ct_val, self.outputs_X1, self.indx, self.inputs, self.outputs, self.states)

                # product d component in the decoupling
                self.inputs_X2 = 'icd_v2_'+istr
                self.outputs_X2 = 'ixcd_'+istr
                self.ct_val = w * Lc
                self.ss_X2, self.inputs, self.outputs, self.states = FProduct(self.inputs_X2, self.ct_val, self.outputs_X2, self.indx, self.inputs, self.outputs, self.states)

                # final addition q component
                self.inputs_s3 = ['vcq_'+istr+'_curr', 'err_vcq_'+istr, 'ixcd_'+istr]
                self.sign_s3 = [+1, -1, -1]
                self.outputs_s3 = 'vcq_ref_'+istr
                self.ss_s3, self.inputs, self.outputs, self.states = FSum(self.inputs_s3, self.sign_s3, self.outputs_s3, self.indx, self.inputs, self.outputs, self.states)

                # final addition d component
                self.inputs_s4 = ['vcd_'+istr+'_curr', 'err_vcd_'+istr, 'ixcq_'+istr]
                self.sign_s4 = [+1, -1, +1]
                self.outputs_s4 = 'vcd_ref_'+istr
                self.ss_s4, self.inputs, self.outputs, self.states = FSum(self.inputs_s4, self.sign_s4, self.outputs_s4, self.indx, self.inputs, self.outputs, self.states)


                # Merge
                self.ss_full = append(self.ss_n1, self.ss_n2, self.ss_s1, self.ss_s2, self.ss_PI1, self.ss_PI2, self.ss_X1, self.ss_X2, self.ss_s3, self.ss_s4)
                self.inputs_full = ['icq_'+istr+'_curr', 'icd_'+istr+'_curr', 'icq_ref_'+istr, 'icd_ref_'+istr, 'vcq_'+istr+'_curr', 'vcd_'+istr+'_curr']
                self.outputs_full = ['vcq_ref_'+istr, 'vcd_ref_'+istr]
                self.Qq, self.indx_x, self.indx_in, self.indx_out, self.name_x, self.name_in, self.name_out = Qvec_builder_full(self.inputs_full, self.outputs_full, self.inputs, self.outputs, self.states)
                self.ss_final = connect(self.ss_full, self.Qq, self.indx_in, self.indx_out)

                # Refer inputs, outputs and states to index 1
                self.indx_in = [ll + 1 for ll in range(len(self.indx_in))]
                self.indx_out = [ll + 1 for ll in range(len(self.indx_out))]
                self.indx_x = [ll + 1 for ll in range(len(self.indx_x))]

                self.dicc_in = BuildDictionary(self.indx_in, self.name_in)
                self.dicc_out = BuildDictionary(self.indx_out, self.name_out)
                self.dicc_x = BuildDictionary(self.indx_x, self.name_x)


        class BGd:
            """
            Class for the 1st order transfer function (the simple version, built directly)

            :param indx: index of the VSC
            :param k: k parameter of the transfer function
            :param tau: tau parameter of the transfer function
            :return: state space of the 1st order transfer cuntion with the inputs, outputs, states
            """

            def __init__(self, indx, k_gd, tau_gd):
                # store variables in the structure
                self.indx = indx
                self.k_gd = k_gd
                self.tau_gd = tau_gd

                # initialize dictionaries and get the index
                self.inputs = {}
                self.outputs = {}
                self.states = {}
                istr = str(self.indx)

                # directly obtained ss
                A = [[- 1 / self.tau_gd, 0], [0, - 1 / self.tau_gd]]
                B = [[self.k_gd / self.tau_gd, 0], [0, self.k_gd / self.tau_gd]]
                C = [[1, 0], [0, 1]]
                D = [[0, 0], [0, 0]]

                self.ss_full = ss(A, B, C, D)

                self.inputs['vcq_ref_'+istr] = 1
                self.inputs['vcd_ref_'+istr] = 2
                self.outputs['vccq_'+istr] = 1
                self.outputs['vccd_'+istr] = 2
                self.states['int_vccq_ref_'+istr] = 1
                self.states['int_vccd_ref_'+istr] = 2

                # Merge
                self.inputs_full = ['vcq_ref_'+istr, 'vcd_ref_'+istr]
                self.outputs_full = ['vccq_'+istr, 'vccd_'+istr]
                self.Qq, self.indx_x, self.indx_in, self.indx_out, self.name_x, self.name_in, self.name_out = Qvec_builder_full(self.inputs_full, self.outputs_full, self.inputs, self.outputs, self.states)
                self.ss_final = connect(self.ss_full, self.Qq, self.indx_in, self.indx_out)

                # Refer inputs, outputs and states to index 1
                self.indx_in = [ll + 1 for ll in range(len(self.indx_in))]
                self.indx_out = [ll + 1 for ll in range(len(self.indx_out))]
                self.indx_x = [ll + 1 for ll in range(len(self.indx_x))]

                self.dicc_in = BuildDictionary(self.indx_in, self.name_in)
                self.dicc_out = BuildDictionary(self.indx_out, self.name_out)
                self.dicc_x = BuildDictionary(self.indx_x, self.name_x)


        class BTv:
            """
            Park transformation for the voltages

            :param indx: index of the VSC
            :param xq0: equilibrium point for the q voltage
            :param xd0: equilibrium point for the d voltage
            :param ang0: equilibrium point for the angle
            :return: state space of the Park transformation for the voltages
            """

            def __init__(self, indx, xq0, xd0, ang0):
                # store variables in the structure
                self.indx = indx
                self.xq0 = xq0
                self.xd0 = xd0
                self.ang0 = ang0

                # initialize dictionaries and get the index
                self.inputs = {}
                self.outputs = {}
                self.states = {}
                istr = str(self.indx)

                A = [[]]
                B = [[]]
                C = [[]]
                D = [[np.cos(self.ang0), - np.sin(self.ang0), - self.xd0 * np.cos(self.ang0) - self.xq0 * np.sin(self.ang0)], [np.sin(self.ang0), np.cos(self.ang0), self.xq0 * np.cos(self.ang0) - self.xd0 * np.sin(self.ang0)], [np.sin(self.ang0), np.cos(self.ang0), self.xq0 * np.cos(self.ang0) - self.xd0 * np.sin(self.ang0)]]

                self.ss_full = ss(A, B, C, D)

                self.inputs['vmq_'+istr+'_Tv'] = 1
                self.inputs['vmd_'+istr+'_Tv'] = 2
                self.inputs['ang_'+istr+'_Tv'] = 3

                self.outputs['vcq_'+istr] = 1
                self.outputs['vcd_'+istr]= 2
                self.outputs['vmd_'+istr+'_PLL']= 3

                # self.states['dummy_Tv_'+istr] = 1
                self.states = {}

                # Merge
                self.inputs_full = ['vmq_'+istr+'_Tv', 'vmd_'+istr+'_Tv', 'ang_'+istr+'_Tv']
                self.outputs_full = ['vcq_'+istr, 'vcd_'+istr, 'vmd_'+istr+'_PLL']
                self.Qq, self.indx_x, self.indx_in, self.indx_out, self.name_x, self.name_in, self.name_out = Qvec_builder_full(self.inputs_full, self.outputs_full, self.inputs, self.outputs, self.states)
                self.ss_final = connect(self.ss_full, self.Qq, self.indx_in, self.indx_out)

                # Refer inputs, outputs and states to index 1
                self.indx_in = [ll + 1 for ll in range(len(self.indx_in))]
                self.indx_out = [ll + 1 for ll in range(len(self.indx_out))]
                self.indx_x = [ll + 1 for ll in range(len(self.indx_x))]

                self.dicc_in = BuildDictionary(self.indx_in, self.name_in)
                self.dicc_out = BuildDictionary(self.indx_out, self.name_out)
                self.dicc_x = BuildDictionary(self.indx_x, self.name_x)


        class BTi:
            """
            Park transformation for the currents

            :param indx: index of the VSC
            :param xq0: equilibrium point for the q current
            :param xd0: equilibrium point for the d current
            :param ang0: equilibrium point for the angle
            :return: state space of the Park transformation for the currents
            """

            def __init__(self, indx, xq0, xd0, ang0):
                # store variables in the structure
                self.indx = indx
                self.xq0 = xq0
                self.xd0 = xd0
                self.ang0 = ang0

                # initialize dictionaries and get the index
                self.inputs = {}
                self.outputs = {}
                self.states = {}
                istr = str(self.indx)

                A = [[]]
                B = [[]]
                C = [[]]
                D = [[np.cos(self.ang0), - np.sin(self.ang0), - self.xd0 * np.cos(self.ang0) - self.xq0 * np.sin(self.ang0)], [np.sin(self.ang0), np.cos(self.ang0), self.xq0 * np.cos(self.ang0) - self.xd0 * np.sin(self.ang0)]]

                self.ss_full = ss(A, B, C, D)

                self.inputs['iq_'+istr] = 1
                self.inputs['id_'+istr] = 2
                self.inputs['ang_'+istr+'_Ti'] = 3

                self.outputs['icq_'+istr] = 1
                self.outputs['icd_'+istr] = 2

                # self.states['dummy_Ti_'+istr] = 1
                self.states = {}

                # Merge
                self.inputs_full = ['iq_'+istr, 'id_'+istr, 'ang_'+istr+'_Ti']
                self.outputs_full = ['icq_'+istr, 'icd_'+istr]
                self.Qq, self.indx_x, self.indx_in, self.indx_out, self.name_x, self.name_in, self.name_out = Qvec_builder_full(self.inputs_full, self.outputs_full, self.inputs, self.outputs, self.states)
                self.ss_final = connect(self.ss_full, self.Qq, self.indx_in, self.indx_out)

                # Refer inputs, outputs and states to index 1
                self.indx_in = [ll + 1 for ll in range(len(self.indx_in))]
                self.indx_out = [ll + 1 for ll in range(len(self.indx_out))]
                self.indx_x = [ll + 1 for ll in range(len(self.indx_x))]

                self.dicc_in = BuildDictionary(self.indx_in, self.name_in)
                self.dicc_out = BuildDictionary(self.indx_out, self.name_out)
                self.dicc_x = BuildDictionary(self.indx_x, self.name_x)



        class BTvinv:
            """
            Inverse Park transformation for the voltages

            :param indx: index of the VSC
            :param xq0: equilibrium point for the q voltage
            :param xd0: equilibrium point for the d voltage
            :param ang0: equilibrium point for the angle
            :return: state space of the inverse Park transformation for the voltages
            """

            def __init__(self, indx, xq0, xd0, ang0):
                # store variables in the structure
                self.indx = indx
                self.xq0 = xq0
                self.xd0 = xd0
                self.ang0 = ang0

                # initialize dictionaries and get the index
                self.inputs = {}
                self.outputs = {}
                self.states = {}
                istr = str(self.indx)

                A = [[]]
                B = [[]]
                C = [[]]
                D = [[np.cos(self.ang0), np.sin(self.ang0), - self.xq0 * np.sin(self.ang0) + self.xd0 * np.cos(self.ang0)], [- np.sin(self.ang0), np.cos(self.ang0), - self.xq0 * np.cos(self.ang0) - self.xd0 * np.sin(self.ang0)]]

                self.ss_full = ss(A, B, C, D)

                self.inputs['vccq_'+istr] = 1
                self.inputs['vccd_'+istr] = 2
                self.inputs['ang_'+istr+'_Tvinv'] = 3

                self.outputs['vxq_'+istr] = 1
                self.outputs['vxd_'+istr]= 2

                # self.states['dummy_Tvinv_'+istr] = 1
                self.states = {}

                # Merge
                self.inputs_full = ['vccq_'+istr, 'vccd_'+istr, 'ang_'+istr+'_Tvinv']
                self.outputs_full = ['vxq_'+istr, 'vxd_'+istr]
                self.Qq, self.indx_x, self.indx_in, self.indx_out, self.name_x, self.name_in, self.name_out = Qvec_builder_full(self.inputs_full, self.outputs_full, self.inputs, self.outputs, self.states)
                self.ss_final = connect(self.ss_full, self.Qq, self.indx_in, self.indx_out)

                # Refer inputs, outputs and states to index 1
                self.indx_in = [ll + 1 for ll in range(len(self.indx_in))]
                self.indx_out = [ll + 1 for ll in range(len(self.indx_out))]
                self.indx_x = [ll + 1 for ll in range(len(self.indx_x))]

                self.dicc_in = BuildDictionary(self.indx_in, self.name_in)
                self.dicc_out = BuildDictionary(self.indx_out, self.name_out)
                self.dicc_x = BuildDictionary(self.indx_x, self.name_x)


        class BDivs:
            """
            Class for the divison of repeated variables

            :param indx: index of the VSC
            :return: state space of all variables' division
            """

            def __init__(self, indx, bus_ac):
                # store variables in the structure
                self.indx = indx
                self.bus_ac = bus_ac

                # initialize dictionaries and get the index
                self.inputs = {}
                self.outputs = {}
                self.states = {}
                istr = str(self.indx)
                bus_ac = str(self.bus_ac)


                # vcq divsion
                self.inputs_nAvq = 'vcq_'+istr
                self.outputs_nAvq = ['vcq_'+istr+'_curr', 'vcq_'+istr+'_P', 'vcq_'+istr+'_Q']
                self.ss_nAvq, self.inputs, self.outputs, self.states = FNode(self.inputs_nAvq, self.outputs_nAvq, self.indx, self.inputs, self.outputs, self.states)

                # vcd division
                self.inputs_nAvd = 'vcd_'+istr
                self.outputs_nAvd = ['vcd_'+istr+'_curr', 'vcd_'+istr+'_P', 'vcd_'+istr+'_Q']
                self.ss_nAvd, self.inputs, self.outputs, self.states = FNode(self.inputs_nAvd, self.outputs_nAvd, self.indx, self.inputs, self.outputs, self.states)

                # icq division
                self.inputs_nAiq = 'icq_'+istr
                self.outputs_nAiq = ['icq_'+istr+'_curr', 'icq_'+istr+'_P', 'icq_'+istr+'_Q']
                self.ss_nAiq, self.inputs, self.outputs, self.states = FNode(self.inputs_nAiq, self.outputs_nAiq, self.indx, self.inputs, self.outputs, self.states)

                # icd division
                self.inputs_nAid = 'icd_'+istr
                self.outputs_nAid = ['icd_'+istr+'_curr', 'icd_'+istr+'_P', 'icd_'+istr+'_Q']
                self.ss_nAid, self.inputs, self.outputs, self.states = FNode(self.inputs_nAid, self.outputs_nAid, self.indx, self.inputs, self.outputs, self.states)

                # angle division
                self.inputs_nAang = 'ang_'+istr
                self.outputs_nAang = ['ang_'+istr+'_Tv', 'ang_'+istr+'_Ti', 'ang_'+istr+'_Tvinv']
                self.ss_nAang, self.inputs, self.outputs, self.states = FNode(self.inputs_nAang, self.outputs_nAang, self.indx, self.inputs, self.outputs, self.states)

                # vd division
                self.inputs_nAvd_div = 'vmd_'+istr
                self.outputs_nAvd_div = ['vmd_'+istr+'_Tv']
                self.ss_nAvd_div, self.inputs, self.outputs, self.states = FNode(self.inputs_nAvd_div, self.outputs_nAvd_div, self.indx, self.inputs, self.outputs, self.states)

                # vq division
                self.inputs_nAvq_div = 'vmq_'+istr
                self.outputs_nAvq_div = ['vmq_'+istr+'_Tv']
                self.ss_nAvq_div, self.inputs, self.outputs, self.states = FNode(self.inputs_nAvq_div, self.outputs_nAvq_div, self.indx, self.inputs, self.outputs, self.states)


                # iqxx division
                self.inputs_nAiqxx_div = 'iqxx_'+bus_ac
                self.outputs_nAiqxx_div = ['iqxv_'+bus_ac, 'iq_'+istr]
                self.ss_nAiqxx_div, self.inputs, self.outputs, self.states = FNode(self.inputs_nAiqxx_div, self.outputs_nAiqxx_div, self.indx, self.inputs, self.outputs, self.states)

                # idxx division
                self.inputs_nAidxx_div = 'idxx_'+bus_ac
                self.outputs_nAidxx_div = ['idxv_'+bus_ac, 'id_'+istr]
                self.ss_nAidxx_div, self.inputs, self.outputs, self.states = FNode(self.inputs_nAidxx_div, self.outputs_nAidxx_div, self.indx, self.inputs, self.outputs, self.states)

                # Merge
                self.ss_full = append(self.ss_nAvq, self.ss_nAvd, self.ss_nAiq, self.ss_nAid, self.ss_nAang, self.ss_nAvd_div, self.ss_nAvq_div, self.ss_nAiqxx_div, self.ss_nAidxx_div)
                self.inputs_full = ['vcq_'+istr, 'vcd_'+istr, 'icq_'+istr, 'icd_'+istr, 'ang_'+istr, 'vmd_'+istr, 'vmq_'+istr, 'iqxx_'+bus_ac, 'idxx_'+bus_ac]
                self.outputs_full = ['vcq_'+istr+'_curr', 'vcq_'+istr+'_P', 'vcq_'+istr+'_Q',  'vcd_'+istr+'_curr', 'vcd_'+istr+'_P', 'vcd_'+istr+'_Q', 'icq_'+istr+'_curr', 'icq_'+istr+'_P', 'icq_'+istr+'_Q', 'icd_'+istr+'_curr', 'icd_'+istr+'_P', 'icd_'+istr+'_Q', 'ang_'+istr+'_Tv', 'ang_'+istr+'_Ti', 'ang_'+istr+'_Tvinv', 'vmd_'+istr+'_Tv', 'vmq_'+istr+'_Tv', 'iqxv_'+bus_ac, 'iq_'+istr, 'idxv_'+bus_ac, 'id_'+istr]  # had to add vmd_PLL!!!!


                self.Qq, self.indx_x, self.indx_in, self.indx_out, self.name_x, self.name_in, self.name_out = Qvec_builder_full(self.inputs_full, self.outputs_full, self.inputs, self.outputs, self.states)
                self.ss_final = connect(self.ss_full, self.Qq, self.indx_in, self.indx_out)

                # Refer inputs, outputs and states to index 1
                self.indx_in = [ll + 1 for ll in range(len(self.indx_in))]
                self.indx_out = [ll + 1 for ll in range(len(self.indx_out))]
                self.indx_x = [ll + 1 for ll in range(len(self.indx_x))]

                self.dicc_in = BuildDictionary(self.indx_in, self.name_in)
                self.dicc_out = BuildDictionary(self.indx_out, self.name_out)
                self.dicc_x = BuildDictionary(self.indx_x, self.name_x)


        class BTrafo_filter:
            """
            Trafo + filter state space

            :param indx: index of the VSC
            :param w: pulsation at the linealization point
            :param bus_ac: ac bus at which the trafo is connected
            :param Rc: filter resistance
            :param Lc: filter inductance
            :param Rg: grid resistance
            :param Lg: grid inductance
            :return: state space of the grid constituted by the filter and the transformer
            """

            def __init__(self, indx, w, bus_ac, Rc, Lc, Rg, Lg):
                # store variables in the structure
                self.indx = indx
                self.w = w
                self.bus_ac = bus_ac
                self.Rc = Rc
                self.Lc = Lc
                self.Rg = Rg
                self.Lg = Lg

                # initialize dictionaries and get the index
                self.inputs = {}
                self.outputs = {}
                self.states = {}
                istr = str(self.indx)
                bus_ac = str(self.bus_ac)


                # changing current sign??
                A = [[-(self.Rc + self.Rg) / (self.Lc + self.Lg), -self.w],
                     [self.w, -(self.Rc + self.Rg) / (self.Lc + self.Lg)]]
                B = [[1 / (self.Lc + self.Lg), 0, -1 / (self.Lc + self.Lg), 0],
                     [0, 1 / (self.Lc + self.Lg), 0, -1 / (self.Lc + self.Lg)]]
                C = [[(self.Lg * self.Rc - self.Lc * self.Rg) / (self.Lc + self.Lg), 0],
                     [0, (self.Lg * self.Rc - self.Lc * self.Rg) / (self.Lc + self.Lg)],
                     [1, 0],
                     [0, 1]]
                D = [[self.Lc / (self.Lc + self.Lg), 0, self.Lg / (self.Lc + self.Lg), 0],
                     [0, self.Lc / (self.Lc + self.Lg), 0, self.Lg / (self.Lc + self.Lg)],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]


                self.ss_full = ss(A, B, C, D)

                # change sign of the current?
                self.inputs['vq_'+bus_ac] = 1
                self.inputs['vd_'+bus_ac] = 2
                self.inputs['vxq_'+istr] = 3
                self.inputs['vxd_'+istr] = 4


                self.outputs['vmq_'+istr] = 1
                self.outputs['vmd_'+istr] = 2
                self.outputs['iqxx_'+bus_ac] = 3
                self.outputs['idxx_'+bus_ac] = 4

                self.states['iqxx_'+bus_ac] = 1
                self.states['idxx_'+bus_ac] = 2

                # Merge
                self.inputs_full = ['vxq_'+istr, 'vxd_'+istr, 'vq_'+bus_ac, 'vd_'+bus_ac]
                self.outputs_full = ['vmq_'+istr, 'vmd_'+istr, 'iqxx_'+bus_ac, 'idxx_'+bus_ac]
                self.Qq, self.indx_x, self.indx_in, self.indx_out, self.name_x, self.name_in, self.name_out = Qvec_builder_full(self.inputs_full, self.outputs_full, self.inputs, self.outputs, self.states)
                self.ss_final = connect(self.ss_full, self.Qq, self.indx_in, self.indx_out)

                # Refer inputs, outputs and states to index 1
                self.indx_in = [ll + 1 for ll in range(len(self.indx_in))]
                self.indx_out = [ll + 1 for ll in range(len(self.indx_out))]
                self.indx_x = [ll + 1 for ll in range(len(self.indx_x))]

                self.dicc_in = BuildDictionary(self.indx_in, self.name_in)
                self.dicc_out = BuildDictionary(self.indx_out, self.name_out)
                self.dicc_x = BuildDictionary(self.indx_x, self.name_x)


        def __init__(self, df_vsc, w, ll):
            self.w = w
            self.indx = ll
            self.name = df_vsc['name']
            self.bus_dc = df_vsc['bus DC']
            self.bus_ac = df_vsc['bus AC']
            self.Rc = df_vsc['Rc']
            self.Lc = df_vsc['Lc']
            self.Rg = df_vsc['Rg']
            self.Lg = df_vsc['Lg']
            self.kp_pll = df_vsc['kp_pll']
            self.ki_pll = df_vsc['ki_pll']
            self.kp_i = df_vsc['kp_i']
            self.ki_i = df_vsc['ki_i']
            self.vcq0 = df_vsc['vcq0']
            self.vcd0 = df_vsc['vcd0']
            self.icq0 = df_vsc['icq0']
            self.icd0 = df_vsc['icd0']
            self.kp_v = df_vsc['kp_v']
            self.ki_v = df_vsc['ki_v']
            self.kp_q = df_vsc['kp_q']
            self.ki_q = df_vsc['ki_q']
            self.kp_f = df_vsc['kp_f']
            self.kp_p = df_vsc['kp_p']
            self.ki_p = df_vsc['ki_p']
            self.k_gd = df_vsc['k_gd']
            self.tau_gd = df_vsc['tau_gd']
            self.vsq0 = df_vsc['vsq0']
            self.vsd0 = df_vsc['vsd0']
            self.isq0 = df_vsc['isq0']
            self.isd0 = df_vsc['isd0']
            self.ang0 = df_vsc['ang0']
            self.vmq0 = df_vsc['vmq0']
            self.vmd0 = df_vsc['vmd0']
            self.imq0 = df_vsc['imq0']
            self.imd0 = df_vsc['imd0']


            # add subblocks
            self.P_outer = self.BP_outer(self.indx, self.vmq0, self.vmd0, self.imq0, self.imd0, self.kp_f, self.kp_p, self.ki_p)
            self.Q_outer = self.BQ_outer(self.indx, self.vmq0, self.vmd0, self.imq0, self.imd0, self.kp_v, self.ki_v, self.kp_q, self.ki_q)
            self.PLL = self.BPLL(self.indx, self.kp_pll, self.ki_pll)
            self.Inner_current_loop = self.BInnerCurrentLoop(self.indx, self.w, self.Lc, self.kp_i, self.ki_i)
            self.Gd = self.BGd(self.indx, self.k_gd, self.tau_gd)
            self.Tv = self.BTv(self.indx, self.vsq0, self.vsd0, self.ang0)
            self.Ti = self.BTi(self.indx, self.isq0, self.isd0, self.ang0)
            self.Tvinv = self.BTvinv(self.indx, self.vcq0, self.vcd0, self.ang0)
            self.Divs = self.BDivs(self.indx, self.bus_ac)
            self.Trafo_filter = self.BTrafo_filter(self.indx, self.w, self.bus_ac, self.Rc, self.Lc, self.Rg, self.Lg)

            # mix all subblocks
            self.dicc_in_pre = {**self.P_outer.dicc_in, **self.Q_outer.dicc_in, **self.PLL.dicc_in, **self.Inner_current_loop.dicc_in, **self.Gd.dicc_in, **self.Tv.dicc_in, **self.Ti.dicc_in, **self.Tvinv.dicc_in, **self.Divs.dicc_in, **self.Trafo_filter.dicc_in}
            self.keys_dicc_in_pre = list(self.dicc_in_pre.keys())
            self.values_dicc_in_pre = [ll + 1 for ll in range(len(self.keys_dicc_in_pre))]

            self.dicc_out_pre = {**self.P_outer.dicc_out, **self.Q_outer.dicc_out, **self.PLL.dicc_out, **self.Inner_current_loop.dicc_out, **self.Gd.dicc_out, **self.Tv.dicc_out, **self.Ti.dicc_out, **self.Tvinv.dicc_out, **self.Divs.dicc_out, **self.Trafo_filter.dicc_out}
            self.keys_dicc_out_pre = list(self.dicc_out_pre.keys())
            self.values_dicc_out_pre = [ll + 1 for ll in range(len(self.keys_dicc_out_pre))]

            self.dicc_x_pre = {**self.P_outer.dicc_x, **self.Q_outer.dicc_x, **self.PLL.dicc_x, **self.Inner_current_loop.dicc_x, **self.Gd.dicc_x, **self.Tv.dicc_x, **self.Ti.dicc_x, **self.Tvinv.dicc_x, **self.Divs.dicc_x, **self.Trafo_filter.dicc_x}
            self.keys_dicc_x_pre = list(self.dicc_x_pre.keys())
            self.values_dicc_x_pre = [ll + 1 for ll in range(len(self.keys_dicc_x_pre))]

            self.dic_i = {}
            for ll in range(len(self.dicc_in_pre)):
                self.dic_i[self.keys_dicc_in_pre[ll]] = ll + 1

            self.dic_o = {}
            for ll in range(len(self.dicc_out_pre)):
                self.dic_o[self.keys_dicc_out_pre[ll]] = ll + 1

            self.dic_x = {}
            for ll in range(len(self.dicc_x_pre)):
                self.dic_x[self.keys_dicc_x_pre[ll]] = ll + 1

            # Build final ss, just trying now
            self.inputs = ['Ap_ref_'+str(self.indx), 'Aq_ref_'+str(self.indx), 'vq_'+str(self.bus_ac), 'vd_'+str(self.bus_ac)]
            self.outputs = ['iqxv_'+str(self.bus_ac), 'idxv_'+str(self.bus_ac)]

            self.ss_full = append(self.P_outer.ss_final, self.Q_outer.ss_final, self.PLL.ss_final, self.Inner_current_loop.ss_final, self.Gd.ss_final, self.Tv.ss_final, self.Ti.ss_final, self.Tvinv.ss_final, self.Divs.ss_final, self.Trafo_filter.ss_final)
            self.Qq, self.indx_x, self.indx_in, self.indx_out, self.name_x, self.name_in, self.name_out = Qvec_builder_full(self.inputs, self.outputs, self.dic_i, self.dic_o, self.dic_x)
            self.ssm = connect(self.ss_full, self.Qq, self.indx_in, self.indx_out)
            self.ss = self.ssm

            # FPrinter(self.ssm, self.name_x, self.name_in, self.name_out, prnt=False)

            self.states = self.name_x
            self.ext_inputs = ['Ap_ref_'+str(self.indx), 'Aq_ref_'+str(self.indx)]
            self.ext_outputs = ['iqxv_'+str(self.bus_ac), 'idxv_'+str(self.bus_ac)]


    VSCs = [VSC_particular(df_VSC.iloc[ll, :], w, ll) for ll in range(len(df_VSC))]


    def df_device(VSCs):
        """
        Store in a dataframe the info of each particular class

        :param VSCs: the list of classes of a device VSC
        :return: a full dataframe
        """

        data = []
        for ll in range(len(VSCs)):
            data.append([VSCs[ll].name, VSCs[ll].bus_dc, VSCs[ll].bus_ac, VSCs[ll].Rc, VSCs[ll].Lc, VSCs[ll].Rg, VSCs[ll].Lg, VSCs[ll].kp_pll, VSCs[ll].ki_pll, VSCs[ll].kp_i, VSCs[ll].ki_i, VSCs[ll].vcq0, VSCs[ll].vcd0, VSCs[ll].icq0, VSCs[ll].icd0, VSCs[ll].kp_v, VSCs[ll].ki_v, VSCs[ll].kp_q, VSCs[ll].ki_q, VSCs[ll].kp_f, VSCs[ll].kp_p, VSCs[ll].ki_p, VSCs[ll].k_gd, VSCs[ll].tau_gd, VSCs[ll].vsq0, VSCs[ll].vsd0, VSCs[ll].isq0, VSCs[ll].isd0, VSCs[ll].ang0, VSCs[ll].vmq0, VSCs[ll].vmd0, VSCs[ll].imq0, VSCs[ll].imd0, VSCs[ll].ext_inputs, VSCs[ll].ext_outputs, VSCs[ll].states, np.array(VSCs[ll].ss.A), np.array(VSCs[ll].ss.B), np.array(VSCs[ll].ss.C), np.array(VSCs[ll].ss.D)])


        dff = pd.DataFrame(data, columns=['name', 'bus_dc', 'bus_ac', 'Rc', 'Lc', 'Rg', 'Lg', 'kp_pll', 'ki_pll', 'kp_i', 'ki_i', 'vcq0', 'vcd0', 'icq0', 'icd0', 'kp_v', 'ki_v', 'kp_q', 'ki_q', 'kp_f', 'kp_p', 'ki_p', 'k_gd', 'tau_gd', 'vsq0', 'vsd0', 'isq0', 'isd0', 'ang0', 'vmq0', 'vmd0', 'imq0', 'imd0', 'inputs', 'outputs', 'states', 'A', 'B', 'C', 'D'])

        return dff


    dff = df_device(VSCs)


    return VSCs, dff




