# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:16:00 2020

@author: msmsa
"""
import PFAS_SAT as ps
import PFAS_SAT_ProcessModels as pspm
import PFAS_SAT_InputData as psid


def test_project():
    InventoryObject = pspm.Inventory()

    CommonDataObject = psid.CommonData()

    InputFlow = pspm.IncomFlow()

    InputFlow.set_flow('FoodWaste', 1000)

    demo = ps.Project(InventoryObject, CommonDataObject, ProcessModels=None)
    ProcessSet = demo.get_process_set(InputFlow.Inc_flow)
    demo.set_process_set(ProcessSet[0])
    FlowParams = demo.get_flow_params()
    demo.set_flow_params(FlowParams)
    demo.setup_network()
    demo.Inventory.Inv

    demo.setup_MC(InputFlow)
    demo.MC_Next(True)
    demo.Inventory.Inv

    results = demo.MC_Run(100)

    MC_results = ps.MCResults(results)
    MC_results.to_df()
    MC_results.plot_corr(MC_results.results_df.columns[2])
    MC_results.plot_data(MC_results.results_df.columns[2], MC_results.results_df.columns[8])
    MC_results.plot_dist(param=MC_results.results_df.columns[2])
