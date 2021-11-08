from control.matlab import *
import pandas as pd
import numpy as np
from engine.devices.auxiliaries import *


def create(df_SG, w):
    """
    Form all SGs classes

    :param df_SG: full data of SG, straight from the .xlsx file
    :param w: pulsation, in rad/s
    :return: it builds the state space with the corresponding names
    """

    class SG_particular:
        """
        Class for a particular SG

        :param df_SG: row of the full SG dataframe
        :param w: pulsation, in rad/s
        :param indx: index of the SG, from 0 to n
        :return: the state space and the names, also stores the input values
        """


        class BExciter:
            """
            Class for the exciter

            :param indx: index of the SG
            :param vsq0: equilibrium point for the q voltage
            :param vsd0: equilibrium point for the d voltage
            :param Vbase: base voltage in kV
            :param Rfd_pu:
            :param Lmd_pu:
            :param NsNf:
            :param Ka: constant of the control of the exciter
            :param Ta: first time constant
            :param Tb: second time constant
            :param Tc: third time constant
            :param Vfbase: base voltage in kV

            :return: state space of the exciter loop with the inputs, outputs, states
            """

            def __init__(self, indx, vsq0, vsd0, Vbase, Rfd_pu, Lmd_pu, NsNf, Ka, Ta, Tb, Tc, Vfbase):
                # store variables in the structure
                self.indx = indx
                self.vsq0 = vsq0
                self.vsd0 = vsd0
                self.Vbase = Vbase
                self.Rfd_pu = Rfd_pu
                self.Lmd_pu = Lmd_pu
                self.NsNf = NsNf
                self.Ka = Ka
                self.Ta = Ta
                self.Tb = Tb
                self.Tc = Tc
                self.Vfbase = Vfbase

                # initialize dictionaries and get the index
                self.inputs = {}
                self.outputs = {}
                self.states = {}
                istr = str(self.indx)

                # absolute value of the voltage calculation
                self.inputs_fv = ['vsq_ac_'+istr, 'vsd_ac_'+istr]
                self.outputs_fv = 'vs_ac_'+istr
                self.ss_fv, self.inputs, self.outputs, self.states = FAC_voltage_SG(self.inputs_fv, self.outputs_fv, self.vsq0, self.vsd0, self.Vbase, self.indx, self.inputs, self.outputs, self.states)

                # voltage difference
                self.inputs_s1 = ['vs_ref_'+istr, 'vs_ac_'+istr]
                self.sign_s1 = [+1, -1]
                self.outputs_s1 = 'vs_err_'+istr
                self.ss_s1, self.inputs, self.outputs, self.states = FSum(self.inputs_s1, self.sign_s1, self.outputs_s1, self.indx, self.inputs, self.outputs, self.states)

                # G exciter control
                self.inputs_G = 'vs_err_'+istr
                self.outputs_G = 'vd_gf_'+istr
                self.states_G = ['xexc_1_'+istr, 'xexc_2_'+istr]
                self.ss_G, self.inputs, self.outputs, self.states = FG_exc(self.Rfd_pu, self.Lmd_pu, self.Vfbase, self.NsNf, self.Ka, self.Ta, self.Tb, self.Tc, self.inputs_G, self.outputs_G, self.states_G, self.indx, self.inputs, self.outputs, self.states)

                # Merge
                self.ss_full = append(self.ss_fv, self.ss_s1, self.ss_G)
                self.inputs_full = ['vsq_ac_'+istr, 'vsd_ac_'+istr, 'vs_ref_'+istr]
                self.outputs_full = ['vd_gf_'+istr]
                self.Qq, self.indx_x, self.indx_in, self.indx_out, self.name_x, self.name_in, self.name_out = Qvec_builder_full(self.inputs_full, self.outputs_full, self.inputs, self.outputs, self.states)
                self.ss_final = connect(self.ss_full, self.Qq, self.indx_in, self.indx_out)

                # Refer inputs, outputs and states to index 1
                self.indx_in = [ll + 1 for ll in range(len(self.indx_in))]
                self.indx_out = [ll + 1 for ll in range(len(self.indx_out))]
                self.indx_x = [ll + 1 for ll in range(len(self.indx_x))]

                self.dicc_in = BuildDictionary(self.indx_in, self.name_in)
                self.dicc_out = BuildDictionary(self.indx_out, self.name_out)
                self.dicc_x = BuildDictionary(self.indx_x, self.name_x)


        class BGovernor:
            """
            Class for the governor

            :param indx: index of the SG
            :param wb: base frequency
            :param R: the regulation constant

            :return: state space of the governor loop with the inputs, outputs, states
            """

            def __init__(self, indx, wb, R):
                # store variables in the structure
                self.indx = indx
                self.wb = wb
                self.R = R

                # initialize dictionaries and get the index
                self.inputs = {}
                self.outputs = {}
                self.states = {}
                istr = str(self.indx)

                # difference of frequencies
                self.inputs_s1 = ['w_ref_'+istr, 'w_g_'+istr]
                self.sign_s1 = [+1, -1]
                self.outputs_s1 = 'w_e_'+istr
                self.ss_s1, self.inputs, self.outputs, self.states = FSum(self.inputs_s1, self.sign_s1, self.outputs_s1, self.indx, self.inputs, self.outputs, self.states)

                # proportional control 1/(wb * R)
                self.inputs_kp1 = 'w_e_'+istr
                self.outputs_kp1 = 'w_err_'+istr
                self.ss_kp1, self.inputs, self.outputs, self.states = FP_controller(1 / (self.wb * self.R), self.inputs_kp1, self.outputs_kp1, self.indx, self.inputs, self.outputs, self.states)

                # difference of active powers
                self.inputs_s2 = ['p_ref_'+istr, 'w_err_'+istr]
                self.sign_s2 = [+1, +1]
                self.outputs_s2 = 'Ay_'+istr
                self.ss_s2, self.inputs, self.outputs, self.states = FSum(self.inputs_s2, self.sign_s2, self.outputs_s2, self.indx, self.inputs, self.outputs, self.states)

                # Merge
                self.ss_full = append(self.ss_s1, self.ss_kp1, self.ss_s2)
                self.inputs_full = ['w_ref_'+istr, 'w_g_'+istr, 'p_ref_'+istr]
                self.outputs_full = ['Ay_'+istr]
                self.Qq, self.indx_x, self.indx_in, self.indx_out, self.name_x, self.name_in, self.name_out = Qvec_builder_full(self.inputs_full, self.outputs_full, self.inputs, self.outputs, self.states)
                self.ss_final = connect(self.ss_full, self.Qq, self.indx_in, self.indx_out)

                # Refer inputs, outputs and states to index 1
                self.indx_in = [ll + 1 for ll in range(len(self.indx_in))]
                self.indx_out = [ll + 1 for ll in range(len(self.indx_out))]
                self.indx_x = [ll + 1 for ll in range(len(self.indx_x))]

                self.dicc_in = BuildDictionary(self.indx_in, self.name_in)
                self.dicc_out = BuildDictionary(self.indx_out, self.name_out)
                self.dicc_x = BuildDictionary(self.indx_x, self.name_x)


        class BTurbine:
            """
            Class for the turbine

            :param indx: index of the SG
            :param T5: time constant for the 5th turbine
            :param T4: time constant for the 4th turbine
            :param T3: time constant for the 3th turbine
            :param T2: time constant for the 2th turbine
            :param F5: time constant for the 5th turbine
            :param F4: time constant for the 4th turbine
            :param F3: time constant for the 3th turbine
            :param F2: time constant for the 2th turbine

            :return: state space of the turbine with the inputs, outputs, states
            """

            def __init__(self, indx, T5, T4, T3, T2, F5, F4, F3, F2):
                # store variables in the structure
                self.indx = indx
                self.T5 = T5
                self.T4 = T4
                self.T3 = T3
                self.T2 = T2
                self.F5 = F5
                self.F4 = F4
                self.F3 = F3
                self.F2 = F2


                # initialize dictionaries and get the index
                self.inputs = {}
                self.outputs = {}
                self.states = {}
                istr = str(self.indx)

                # stage number 5
                self.inputs_s5 = ['Ay_'+istr]
                self.outputs_s5 = ['Ay5_'+istr, 'AT5_'+istr]
                self.ss_s5, self.inputs, self.outputs, self.states = FPiFi_turbine(self.T5, self.F5, self.inputs_s5, self.outputs_s5, self.indx, self.inputs, self.outputs, self.states)

                # stage number 4
                self.inputs_s4 = ['Ay5_'+istr]
                self.outputs_s4 = ['Ay4_'+istr, 'AT4_'+istr]
                self.ss_s4, self.inputs, self.outputs, self.states = FPiFi_turbine(self.T4, self.F4, self.inputs_s4, self.outputs_s4, self.indx, self.inputs, self.outputs, self.states)

                # stage number 3
                self.inputs_s3 = ['Ay4_'+istr]
                self.outputs_s3 = ['Ay3_'+istr, 'AT3_'+istr]
                self.ss_s3, self.inputs, self.outputs, self.states = FPiFi_turbine(self.T3, self.F3, self.inputs_s3, self.outputs_s3, self.indx, self.inputs, self.outputs, self.states)

                # stage number 2
                self.inputs_s2 = ['Ay3_'+istr]
                self.outputs_s2 = ['AT2_'+istr]
                self.ss_s2, self.inputs, self.outputs, self.states = FPiF_turbine(self.T2, self.F2, self.inputs_s2, self.outputs_s2, self.indx, self.inputs, self.outputs, self.states)


                # Merge
                self.ss_full = append(self.ss_s5, self.ss_s4, self.ss_s3, self.ss_s2)
                self.inputs_full = ['Ay_'+istr]
                self.outputs_full = ['AT5_'+istr, 'AT4_'+istr, 'AT3_'+istr, 'AT2_'+istr]
                self.Qq, self.indx_x, self.indx_in, self.indx_out, self.name_x, self.name_in, self.name_out = Qvec_builder_full(self.inputs_full, self.outputs_full, self.inputs, self.outputs, self.states)
                self.ss_final = connect(self.ss_full, self.Qq, self.indx_in, self.indx_out)

                # Refer inputs, outputs and states to index 1
                self.indx_in = [ll + 1 for ll in range(len(self.indx_in))]
                self.indx_out = [ll + 1 for ll in range(len(self.indx_out))]
                self.indx_x = [ll + 1 for ll in range(len(self.indx_x))]

                self.dicc_in = BuildDictionary(self.indx_in, self.name_in)
                self.dicc_out = BuildDictionary(self.indx_out, self.name_out)
                self.dicc_x = BuildDictionary(self.indx_x, self.name_x)



        class BShaft:
            """
            Class for the multi-mass shaft

            :param indx: index of the SG
            :param wb: base pulsation in rad/s
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
            :return: state space of the shaft with the inputs, outputs, states
            """

            def __init__(self, indx, wb, Pn, D1, H1, K12, D2, H2, K23, D3, H3, K34, D4, H4, K45, D5, H5):
                # store variables in the structure
                self.indx = indx
                self.wb = wb
                self.Pn = Pn
                self.D1 = D1
                self.H1 = H1
                self.K12 = K12
                self.D2 = D2
                self.H2 = H2
                self.K23 = K23
                self.D3 = D3
                self.H3 = H3
                self.K34 = K34
                self.D4 = D4
                self.H4 = H4
                self.K45 = K45
                self.D5 = D5
                self.H5 = H5


                # initialize dictionaries and get the index
                self.inputs = {}
                self.outputs = {}
                self.states = {}
                istr = str(self.indx)

                # full shaft
                self.inputs_sh = ['ATe_'+istr, 'AT2_'+istr, 'AT3_'+istr, 'AT4_'+istr, 'AT5_'+istr]
                self.outputs_sh = ['we_'+istr]
                self.states_sh = ['xwpu_1_'+istr, 'xwpu_2_'+istr, 'xwpu_3_'+istr, 'xwpu_4_'+istr, 'xwpu_5_'+istr, 'xdelt_1_'+istr, 'xdelt_2_'+istr, 'xdelt_3_'+istr, 'xdelt_4_'+istr, 'xdelt_5_'+istr]
                self.ss_sh, self.inputs, self.outputs, self.states = FShaft(self.wb, self.Pn, self.D1, self.D2, self.D3, self.D4, self.D5, self.H1, self.H2, self.H3, self.H4, self.H5, self.K12, self.K23, self.K34, self.K45, self.inputs_sh, self.outputs_sh, self.states_sh, self.indx, self.inputs, self.outputs, self.states)


                # Merge
                self.ss_full = append(self.ss_sh)
                self.inputs_full = ['ATe_'+istr, 'AT2_'+istr, 'AT3_'+istr, 'AT4_'+istr, 'AT5_'+istr]
                self.outputs_full = ['we_'+istr]
                self.Qq, self.indx_x, self.indx_in, self.indx_out, self.name_x, self.name_in, self.name_out = Qvec_builder_full(self.inputs_full, self.outputs_full, self.inputs, self.outputs, self.states)
                self.ss_final = connect(self.ss_full, self.Qq, self.indx_in, self.indx_out)

                # Refer inputs, outputs and states to index 1
                self.indx_in = [ll + 1 for ll in range(len(self.indx_in))]
                self.indx_out = [ll + 1 for ll in range(len(self.indx_out))]
                self.indx_x = [ll + 1 for ll in range(len(self.indx_x))]

                self.dicc_in = BuildDictionary(self.indx_in, self.name_in)
                self.dicc_out = BuildDictionary(self.indx_out, self.name_out)
                self.dicc_x = BuildDictionary(self.indx_x, self.name_x)


        class BElectricCircuit:
            """
            Class for the electric circuit

            :param indx: index of the SG
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
            :return: state space of the full electric circuit with the inputs, outputs, states
            """

            def __init__(self, indx, Rs, Rkd, Rkq1, Rkq2, Rfd_pr, Lmd, Lmq, Ll, Llkd, Llkq1, Llkq2, Llfd_pr, we0, isq0, isd0, ik1q0, ik2q0, ifd0, ikd0):
                # store variables in the structure
                self.indx = indx
                self.Rs = Rs
                self.Rkd = Rkd
                self.Rkq1 = Rkq1
                self.Rkq2 = Rkq2
                self.Rfd_pr = Rfd_pr
                self.Lmd = Lmd
                self.Lmq = Lmq
                self.Ll = Ll
                self.Llkd = Llkd
                self.Llkq1 = Llkq1
                self.Llkq2 = Llkq2
                self.Llfd_pr = Llfd_pr
                self.we0 = we0
                self.isq0 = isq0
                self.isd0 = isd0
                self.ik1q0 = ik1q0
                self.ik2q0 = ik2q0
                self.ifd0 = ifd0
                self.ikd0 = ikd0


                # initialize dictionaries and get the index
                self.inputs = {}
                self.outputs = {}
                self.states = {}
                istr = str(self.indx)


                # full electric circuit
                # self.inputs_se = ['vd_x_'+istr, 'vkd_x_'+istr, 'vfd_x_'+istr, 'vq_x_'+istr, 'vk1q_x_'+istr, 'vk2q_x_'+istr, 'we_y_'+istr]
                self.inputs_se = ['vd_x_'+istr, 'vkd_x_'+istr, 'vd_gf_'+istr, 'vq_x_'+istr, 'vk1q_x_'+istr, 'vk2q_x_'+istr, 'we_y_'+istr]
                self.outputs_se = ['isd_x_'+istr, 'ikd_x_'+istr, 'ifd_x_'+istr, 'isq_x_'+istr, 'ik1q_x_'+istr, 'ik2q_x_'+istr, 'ATe_'+istr]
                self.states_se = ['xisd_'+istr, 'xikd_'+istr, 'xifd_'+istr, 'xisq_'+istr, 'xik1q_'+istr, 'xik2q_'+istr]
                self.ss_se, self.inputs, self.outputs, self.states = FElectricCircuit(self.Rs, self.Rkd, self.Rkq1, self.Rkq2, self.Rfd_pr, self.Lmd, self.Lmq, self.Ll, self.Llkd, self.Llkq1, self.Llkq2, self.Llfd_pr, self.we0, self.isq0, self.isd0, self.ik1q0, self.ik2q0, self.ifd0, self.ikd0, self.inputs_se, self.outputs_se, self.states_se, self.indx, self.inputs, self.outputs, self.states)


                # Merge
                self.ss_full = append(self.ss_se)
                # self.inputs_full = ['vd_x_'+istr, 'vkd_x_'+istr, 'vfd_x_'+istr, 'vq_x_'+istr, 'vk1q_x_'+istr, 'vk2q_x_'+istr, 'we_y_'+istr]
                self.inputs_full = ['vd_x_'+istr, 'vkd_x_'+istr, 'vd_gf_'+istr, 'vq_x_'+istr, 'vk1q_x_'+istr, 'vk2q_x_'+istr, 'we_y_'+istr]
                self.outputs_full = ['isd_x_'+istr, 'ikd_x_'+istr, 'ifd_x_'+istr, 'isq_x_'+istr, 'ik1q_x_'+istr, 'ik2q_x_'+istr, 'ATe_'+istr]
                self.Qq, self.indx_x, self.indx_in, self.indx_out, self.name_x, self.name_in, self.name_out = Qvec_builder_full(self.inputs_full, self.outputs_full, self.inputs, self.outputs, self.states)
                self.ss_final = connect(self.ss_full, self.Qq, self.indx_in, self.indx_out)

                # Refer inputs, outputs and states to index 1
                self.indx_in = [ll + 1 for ll in range(len(self.indx_in))]
                self.indx_out = [ll + 1 for ll in range(len(self.indx_out))]
                self.indx_x = [ll + 1 for ll in range(len(self.indx_x))]

                self.dicc_in = BuildDictionary(self.indx_in, self.name_in)
                self.dicc_out = BuildDictionary(self.indx_out, self.name_out)
                self.dicc_x = BuildDictionary(self.indx_x, self.name_x)


        class BTiinv:
            """
            Inverse Park transformation for the currents

            :param indx: index of the SG
            :param xq0: equilibrium point for the q current
            :param xd0: equilibrium point for the d current
            :param ang0: equilibrium point for the angle
            :return: state space of the inverse Park transformation for the currents
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

                # directly obtained ss
                A = [[]]
                B = [[]]
                C = [[]]
                D = [[np.cos(self.ang0), np.sin(self.ang0), - self.xq0 * np.sin(self.ang0) + self.xd0 * np.cos(self.ang0)], [- np.sin(self.ang0), np.cos(self.ang0), - self.xq0 * np.cos(self.ang0) - self.xd0 * np.sin(self.ang0)]]

                self.ss_full = ss(A, B, C, D)

                self.inputs['isq_x_'+istr] = 1
                self.inputs['isd_x_'+istr] = 2
                self.inputs['ang_'+istr+'_Tiinv'] = 3

                self.outputs['isq_'+istr] = 1
                self.outputs['isd_'+istr]= 2

                # self.states['dummy_Tvinv_'+istr] = 1
                self.states = {}

                # Merge
                self.inputs_full = ['isq_x_'+istr, 'isd_x_'+istr, 'ang_'+istr+'_Tiinv']
                self.outputs_full = ['isq_'+istr, 'isd_'+istr]
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

            :param indx: index of the SG
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

                # directly obtained ss
                A = [[]]
                B = [[]]
                C = [[]]
                D = [[np.cos(self.ang0), - np.sin(self.ang0), - self.xd0 * np.cos(self.ang0) - self.xq0 * np.sin(self.ang0)], [np.sin(self.ang0), np.cos(self.ang0), self.xq0 * np.cos(self.ang0) - self.xd0 * np.sin(self.ang0)]]

                self.ss_full = ss(A, B, C, D)

                self.inputs['vq_g_'+istr+'_Tv'] = 1
                self.inputs['vd_g_'+istr+'_Tv'] = 2
                self.inputs['ang_'+istr+'_Tv'] = 3

                self.outputs['vq_s_'+istr] = 1
                self.outputs['vd_s_'+istr]= 2

                # self.states['dummy_Tv_'+istr] = 1
                self.states = {}

                # Merge
                self.inputs_full = ['vq_g_'+istr+'_Tv', 'vd_g_'+istr+'_Tv', 'ang_'+istr+'_Tv']
                self.outputs_full = ['vq_s_'+istr, 'vd_s_'+istr]
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

            :param indx: index of the SG
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

                # vq divsion
                self.inputs_nAvq = 'vqx_'+istr
                self.outputs_nAvq = ['vq_x_'+istr, 'vsq_ac_'+istr, 'vq_out_'+istr]
                self.ss_nAvq, self.inputs, self.outputs, self.states = FNode(self.inputs_nAvq, self.outputs_nAvq, self.indx, self.inputs, self.outputs, self.states)

                # vd division
                self.inputs_nAvd = 'vdx_'+istr
                self.outputs_nAvd = ['vd_x_'+istr, 'vsd_ac_'+istr, 'vd_out_'+istr]
                self.ss_nAvd, self.inputs, self.outputs, self.states = FNode(self.inputs_nAvd, self.outputs_nAvd, self.indx, self.inputs, self.outputs, self.states)

                # iq division
                self.inputs_nAiq = 'isq_x_'+istr
                self.outputs_nAiq = ['isq_l_'+istr, 'isq_out_'+istr]
                self.ss_nAiq, self.inputs, self.outputs, self.states = FNode(self.inputs_nAiq, self.outputs_nAiq, self.indx, self.inputs, self.outputs, self.states)

                # id division
                self.inputs_nAid = 'isd_x_'+istr
                self.outputs_nAid = ['isd_l_'+istr, 'isd_out_'+istr]
                self.ss_nAid, self.inputs, self.outputs, self.states = FNode(self.inputs_nAid, self.outputs_nAid, self.indx, self.inputs, self.outputs, self.states)

                # w division
                self.inputs_nw = 'we_'+istr
                self.outputs_nw = ['w_g_'+istr, 'we_y_'+istr]
                self.ss_nw, self.inputs, self.outputs, self.states = FNode(self.inputs_nw, self.outputs_nw, self.indx, self.inputs, self.outputs, self.states)

                # Merge
                self.ss_full = append(self.ss_nAvq, self.ss_nAvd, self.ss_nAiq, self.ss_nAid, self.ss_nw)
                self.inputs_full = ['vqx_'+istr, 'vdx_'+istr, 'isq_x_'+istr, 'isd_x_'+istr, 'we_'+istr]
                self.outputs_full = ['vq_x_'+istr, 'vsq_ac_'+istr, 'vq_out_'+istr, 'vd_x_'+istr, 'vsd_ac_'+istr, 'vd_out_'+istr, 'isq_l_'+istr, 'isq_out_'+istr, 'isd_l_'+istr, 'isd_out_'+istr, 'w_g_'+istr, 'we_y_'+istr]

                self.Qq, self.indx_x, self.indx_in, self.indx_out, self.name_x, self.name_in, self.name_out = Qvec_builder_full(self.inputs_full, self.outputs_full, self.inputs, self.outputs, self.states)
                self.ss_final = connect(self.ss_full, self.Qq, self.indx_in, self.indx_out)

                # Refer inputs, outputs and states to index 1
                self.indx_in = [ll + 1 for ll in range(len(self.indx_in))]
                self.indx_out = [ll + 1 for ll in range(len(self.indx_out))]
                self.indx_x = [ll + 1 for ll in range(len(self.indx_x))]

                self.dicc_in = BuildDictionary(self.indx_in, self.name_in)
                self.dicc_out = BuildDictionary(self.indx_out, self.name_out)
                self.dicc_x = BuildDictionary(self.indx_x, self.name_x)


        class BRload:
            """
            Basic Rload to extract the voltage

            :param indx: index of the SG
            :param Rload: value of the load resistance
            :param isq0: linealization point for the q current
            :param isd0: linealization point for the d current
            :return: state space of the voltage drop on a resistance
            """

            def __init__(self, indx, Rload, isq0, isd0):
                # store variables in the structure
                self.indx = indx
                self.Rload = Rload
                self.isq0 = isq0
                self.isd0 = isd0

                # initialize dictionaries and get the index
                self.inputs = {}
                self.outputs = {}
                self.states = {}
                istr = str(self.indx)

                # directly obtained ss
                A = [[]]
                B = [[]]
                C = [[]]
                D = [[-Rload, 0, Rload, 0, self.isq0], [0, -Rload, 0, Rload, self.isd0]]

                self.ss_full = ss(A, B, C, D)

                self.inputs['iq_load_'+istr] = 1
                self.inputs['id_load_'+istr] = 2
                self.inputs['isq_l_'+istr] = 3
                self.inputs['isd_l_'+istr] = 4
                self.inputs['Rload_'+istr] = 5

                self.outputs['vqx_'+istr] = 1
                self.outputs['vdx_'+istr] = 2

                self.states = {}

                # Merge
                self.inputs_full = ['iq_load_'+istr, 'id_load_'+istr, 'isq_l_'+istr, 'isd_l_'+istr, 'Rload_'+istr]
                self.outputs_full = ['vqx_'+istr, 'vdx_'+istr]
                self.Qq, self.indx_x, self.indx_in, self.indx_out, self.name_x, self.name_in, self.name_out = Qvec_builder_full(self.inputs_full, self.outputs_full, self.inputs, self.outputs, self.states)
                self.ss_final = connect(self.ss_full, self.Qq, self.indx_in, self.indx_out)

                # Refer inputs, outputs and states to index 1
                self.indx_in = [ll + 1 for ll in range(len(self.indx_in))]
                self.indx_out = [ll + 1 for ll in range(len(self.indx_out))]
                self.indx_x = [ll + 1 for ll in range(len(self.indx_x))]

                self.dicc_in = BuildDictionary(self.indx_in, self.name_in)
                self.dicc_out = BuildDictionary(self.indx_out, self.name_out)
                self.dicc_x = BuildDictionary(self.indx_x, self.name_x)




        def __init__(self, df_sg, w, ll):
            self.w = w
            self.indx = ll
            self.name = df_sg['name']
            self.bus_ac = df_sg['bus AC']
            self.Vbase = df_sg['Vbase']
            self.wb = df_sg['wb']
            self.Ka = df_sg['Ka']
            self.Ta = df_sg['Ta']
            self.Tb = df_sg['Tb']
            self.Tc = df_sg['Tc']
            self.vsq0 = df_sg['vsq0']
            self.vsd0 = df_sg['vsd0']
            self.NsNf = df_sg['NsNf']
            self.Pn = df_sg['Pn']
            self.T5 = df_sg['T5']
            self.T4 = df_sg['T4']
            self.T3 = df_sg['T3']
            self.T2 = df_sg['T2']
            self.F5 = df_sg['F5']
            self.F4 = df_sg['F4']
            self.F3 = df_sg['F3']
            self.F2 = df_sg['F2']
            self.D1 = df_sg['D1']
            self.D2 = df_sg['D2']
            self.D3 = df_sg['D3']
            self.D4 = df_sg['D4']
            self.D5 = df_sg['D5']
            self.H1 = df_sg['H1']
            self.H2 = df_sg['H2']
            self.H3 = df_sg['H3']
            self.H4 = df_sg['H4']
            self.H5 = df_sg['H5']
            self.K12 = df_sg['K12']
            self.K23 = df_sg['K23']
            self.K34 = df_sg['K34']
            self.K45 = df_sg['K45']
            self.R = df_sg['R']
            self.Rfd = df_sg['Rfd']
            self.Rs = df_sg['Rs']
            self.Rkd = df_sg['Rkd']
            self.Rkq1 = df_sg['Rkq1']
            self.Rkq2 = df_sg['Rkq2']
            self.Rfd_pr = df_sg['Rfd_pr']
            self.Lmd = df_sg['Lmd']
            self.Lmq = df_sg['Lmq']
            self.Ll = df_sg['Ll']
            self.Llkd = df_sg['Llkd']
            self.Llkq1 = df_sg['Llkq1']
            self.Llkq2 = df_sg['Llkq2']
            self.Llfd_pr = df_sg['Llfd_pr']
            self.we0 = df_sg['we0']
            self.isq0 = df_sg['isq0']
            self.isd0 = df_sg['isd0']
            self.ik1q0 = df_sg['ik1q0']
            self.ik2q0 = df_sg['ik2q0']
            self.ifd0 = df_sg['ifd0']
            self.ikd0 = df_sg['ikd0']
            self.ang0 = df_sg['ang0']
            self.Rload = df_sg['Rload']
            self.Rfd_pu = df_sg['Rfd_pu']
            self.Lmd_pu = df_sg['Lmd_pu']
            self.Vfbase = df_sg['Vfbase']

            # add subblocks
            self.Exciter = self.BExciter(self.indx, self.vsq0, self.vsd0, self.Vbase, self.Rfd_pu, self.Lmd_pu, self.NsNf, self.Ka, self.Ta, self.Tb, self.Tc, self.Vfbase)
            self.Governor = self.BGovernor(self.indx, self.wb, self.R)
            self.Turbine = self.BTurbine(self.indx, self.T5, self.T4, self.T3, self.T2, self.F5, self.F4, self.F3, self.F2)
            self.Shaft = self.BShaft(self.indx, self.wb, self.Pn, self.D1, self.H1, self.K12, self.D2, self.H2, self.K23, self.D3, self.H3, self.K34, self.D4, self.H4, self.K45, self.D5, self.H5)
            self.ElectricCircuit = self.BElectricCircuit(self.indx, self.Rs, self.Rkd, self.Rkq1, self.Rkq2, self.Rfd_pr, self.Lmd, self.Lmq, self.Ll, self.Llkd, self.Llkq1, self.Llkq2, self.Llfd_pr, self.we0, self.isq0, self.isd0, self.ik1q0, self.ik2q0, self.ifd0, self.ikd0)
            self.RloadC = self.BRload(self.indx, self.Rload, self.isq0, self.isd0)
            self.Divs = self.BDivs(self.indx, self.bus_ac)

            # self.Tiinv = self.BTiinv(self.indx, self.isq0, self.isd0, self.ang0)
            # self.Tv = self.BTv(self.indx, self.vsq0, self.vsd0, self.ang0)



            # mix all subblocks
            self.dicc_in_pre = {**self.Exciter.dicc_in, **self.Governor.dicc_in, **self.Turbine.dicc_in, **self.Shaft.dicc_in, **self.ElectricCircuit.dicc_in, **self.RloadC.dicc_in, **self.Divs.dicc_in}
            self.keys_dicc_in_pre = list(self.dicc_in_pre.keys())
            self.values_dicc_in_pre = [ll + 1 for ll in range(len(self.keys_dicc_in_pre))]

            self.dicc_out_pre = {**self.Exciter.dicc_out, **self.Governor.dicc_out, **self.Turbine.dicc_out, **self.Shaft.dicc_out, **self.ElectricCircuit.dicc_out, **self.RloadC.dicc_out, **self.Divs.dicc_out}
            self.keys_dicc_out_pre = list(self.dicc_out_pre.keys())
            self.values_dicc_out_pre = [ll + 1 for ll in range(len(self.keys_dicc_out_pre))]

            self.dicc_x_pre = {**self.Exciter.dicc_x, **self.Governor.dicc_x, **self.Turbine.dicc_x, **self.Shaft.dicc_x, **self.ElectricCircuit.dicc_x, **self.RloadC.dicc_x, **self.Divs.dicc_x}
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

            # Build final ss
            # self.inputs = ['w_ref_'+str(self.indx), 'p_ref_'+str(self.indx), 'vs_ref_'+str(self.indx), 'iq_load_'+str(self.indx), 'id_load_'+str(self.indx), 'Rload_'+str(self.indx)]
            # self.outputs = ['vqx_'+str(self.indx), 'vdx_'+str(self.indx), 'isd_x_'+str(self.indx), 'ikd_x_'+str(self.indx), 'ifd_x_'+str(self.indx), 'isq_x_'+str(self.indx), 'ik1q_x_'+str(self.indx), 'ik2q_x_'+str(self.indx), 'ATe_'+str(self.indx)]

            # for the stability, voltage as input, try it
            self.inputs = ['vqx_'+str(self.indx), 'vdx_'+str(self.indx)]
            self.outputs = ['isq_x_'+str(self.indx), 'isd_x_'+str(self.indx)]


            self.ss_full = append(self.Exciter.ss_final, self.Governor.ss_final, self.Turbine.ss_final, self.Shaft.ss_final, self.ElectricCircuit.ss_final, self.RloadC.ss_final, self.Divs.ss_final)
            self.Qq, self.indx_x, self.indx_in, self.indx_out, self.name_x, self.name_in, self.name_out = Qvec_builder_full(self.inputs, self.outputs, self.dic_i, self.dic_o, self.dic_x)
            self.ssm = connect(self.ss_full, self.Qq, self.indx_in, self.indx_out)
            self.ss = self.ssm


    SGs = [SG_particular(df_SG.iloc[ll, :], w, ll) for ll in range(len(df_SG))]


    def df_device(SGs):
        """
        Store in a dataframe the info of each particular class

        :param SGs: the list of classes of a device SG
        :return: a full dataframe
        """

        data = []
        for ll in range(len(SGs)):

            data.append([SGs[ll].name, SGs[ll].bus_ac, SGs[ll].Vbase, SGs[ll].wb, SGs[ll].Ka, SGs[ll].Ta, SGs[ll].Tb, SGs[ll].Tc, SGs[ll].vsq0, SGs[ll].vsd0, SGs[ll].NsNf, SGs[ll].Pn, SGs[ll].T5, SGs[ll].T4, SGs[ll].T3, SGs[ll].T2, SGs[ll].F5, SGs[ll].F4, SGs[ll].F3, SGs[ll].F2, SGs[ll].D1, SGs[ll].D2, SGs[ll].D3, SGs[ll].D4, SGs[ll].D5, SGs[ll].H1, SGs[ll].H2, SGs[ll].H3, SGs[ll].H4, SGs[ll].H5, SGs[ll].K12, SGs[ll].K23, SGs[ll].K34, SGs[ll].K45, SGs[ll].R, SGs[ll].Rfd, SGs[ll].Rs, SGs[ll].Rkd, SGs[ll].Rkq1, SGs[ll].Rkq2, SGs[ll].Rfd_pr, SGs[ll].Lmd, SGs[ll].Lmq, SGs[ll].Ll, SGs[ll].Llkd, SGs[ll].Llkq1, SGs[ll].Llkq2, SGs[ll].Llfd_pr, SGs[ll].we0, SGs[ll].isq0, SGs[ll].isd0, SGs[ll].ik1q0, SGs[ll].ik2q0, SGs[ll].ifd0, SGs[ll].ikd0, SGs[ll].ang0, SGs[ll].Rload, SGs[ll].Rfd_pu, SGs[ll].Lmd_pu, SGs[ll].Vfbase, SGs[ll].inputs, SGs[ll].outputs, SGs[ll].states, np.array(SGs[ll].ss.A), np.array(SGs[ll].ss.B), np.array(SGs[ll].ss.C), np.array(SGs[ll].ss.D)])


        dff = pd.DataFrame(data, columns=['name', 'bus_ac', 'Vbase', 'wb', 'Ka', 'Ta', 'Tb', 'Tc', 'vsq0', 'vsd0', 'NsNf', 'Pn', 'T5', 'T4', 'T3', 'T2', 'F5', 'F4', 'F3', 'F2', 'D1', 'D2', 'D3', 'D4', 'D5', 'H1', 'H2', 'H3', 'H4', 'H5', 'K12', 'K23', 'K34', 'K45', 'R', 'Rfd', 'Rs', 'Rkd', 'Rkq1', 'Rkq2', 'Rfd_pr', 'Lmd', 'Lmq', 'Ll', 'Llkd', 'Llkq1', 'Llkq2', 'Llfd_pr', 'we0', 'isq0', 'isd0', 'ik1q0', 'ik2q0', 'ifd0', 'ikd0', 'ang0', 'Rload', 'Rfd_pu', 'Lmd_pu', 'Vfbase', 'inputs', 'outputs', 'states', 'A', 'B', 'C', 'D'])

        return dff


    dff = df_device(SGs)

    return SGs, dff



