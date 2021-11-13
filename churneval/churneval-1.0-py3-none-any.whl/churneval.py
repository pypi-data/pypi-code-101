# -*- coding: utf-8 -*-
"""
@author: Soumi De
"""
import pandas as pd
from sklearn.metrics import confusion_matrix, roc_auc_score
from sklearn import metrics

def get_performance_metrics(model_name, true_class, predicted_class, predicted_probs):
    
    test_index = true_class.index
    conf_mat = confusion_matrix(predicted_class, true_class, labels=[1,0])
    tdl = pd.concat([pd.DataFrame(predicted_probs,index=test_index, columns=['predicted_probs']),
                        pd.DataFrame(predicted_class,index=test_index, columns=['predicted_class']),
                        pd.DataFrame(true_class,index=test_index)], 
                    axis = 1, ignore_index=False).sort_values('predicted_probs', ascending = False)

    a = tdl.head(round(0.10*tdl.shape[0]))

    tdl_metric_num = a.query('predicted_class == 1 and y == 1')['y'].sum()/a.shape[0]
    tdl_metric_den = sum(conf_mat[:,0])/conf_mat.sum()
    tdl = tdl_metric_num/tdl_metric_den

    roc_value = roc_auc_score(true_class, predicted_probs) 
    accuracy = metrics.accuracy_score(true_class, predicted_class)
    precision = metrics.precision_score(true_class, predicted_class)
    sensitivity = metrics.recall_score(true_class, predicted_class)
    specificity = conf_mat[1,1]/sum(conf_mat[:,1])
    f1_score = metrics.f1_score(true_class, predicted_class)
    perf = pd.DataFrame()
    perf = perf.append({'Model_Name': model_name, 'Accuracy': accuracy, 'Confusion Matrix': conf_mat,
                        'Precision': precision, 'Sensitivity': sensitivity, 
                        'Specificity': specificity, 'F1-score': f1_score,'ROC_score':roc_value,
                        "Top_dec_lift":tdl}, ignore_index=True)
    
    return(perf)
