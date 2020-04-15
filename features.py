# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import random
class BacFeature:
    #bacteria feature
    '''
    bio_regulation=0
    carbonhydrate_util=0
    carbon_util=0
    growth=0
    developmental_process=0
    metabolic_process=0
    negative_regulation_of_bio_process=0
    nitrogen_util=0
    phosphorus_util=0
    positive_regulation_of_bio_process=0
    reproduction=0
    reproductive_process=0
    binding=0
    molecular_function_regulator=0
    negative_function_of_molecular_function=0
    nutrient_reservoir_activity=0
    positive_regulation_of_molecular_function=0
    transcription_regulation_activity=0
    transition_regulation_activity=0
    feature=np.array((0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
    '''
    def __init__(self,feature=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]):
        
        self.bio_regulation=feature[0]
        self.carbonhydrate_util=feature[1]
        self.carbon_util=feature[2]
        self.growth=feature[3]
        self.developmental_process=feature[4]
        self.metabolic_process=feature[5]
        self.negative_regulation_of_bio_process=feature[6]
        self.nitrogen_util=feature[7]
        self.phosphorus_util=feature[8]
        self.positive_regulation_of_bio_process=feature[9]
        self.reproduction=feature[10]
        self.reproductive_process=feature[11]
        self.binding=feature[12]
        self.molecular_function_regulator=feature[13]
        self.negative_function_of_molecular_function=feature[14]
        self.nutrient_reservoir_activity=feature[15]
        self.positive_regulation_of_molecular_function=feature[16]
        self.transcription_regulation_activity=feature[17]
        self.transition_regulation_activity=feature[18]
        self.feature=np.array(feature)

def constrained_sum_sample_pos(n, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""
    dividers = sorted(random.sample(range(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]
    
class MediaFeature:
    '''
    random_feature=constrained_sum_sample_pos(24,100) 
    Phytone_peptone=0 
    Trypticase_peptone=0
    L_Histidine=0 
    L_Serine=0 
    L_Glutamine=0 
    Glycine=0 
    KCl=0 
    NaCl=0 
    MgCl2=0 
    MgSO4=0
    CaCl2=0 
    KH2PO4=0 
    MgSO4x7H2O=0 
    NH42SO4=0
    Glucose=0 
    Distilled_Water=0 
    Yeast_extract=0 
    Tween80=0 
    Tryptone=0  
    Casein=0 
    L_Cysteine_HCl=0 
    VitaminB12=0 
    H3BO=0  
    Meat_extract=0
    feature=np.array(random_feature) #24
    '''
    def __init__(self,feature=[1,5,1,3,4,3,11,3,2,13,1,7,1,3,5,6,1,2,1,3,10,6,2,6]):
        
        self.Phytone_peptone=feature[0]
        self.Trypticase_peptone=feature[1]
        self.L_Histidine=feature[2]
        self.L_Serine=feature[3]
        self.L_Glutamine=feature[4]
        self.Glycine=feature[5]
        self.KCl=feature[6]
        self.NaCl=feature[7]
        self.MgCl2=feature[8]
        self.MgSO4=feature[9]
        self.CaCl2=feature[10]
        self.KH2PO4=feature[11]
        self.MgSO4x7H2O=feature[12]
        self.NH42SO4=feature[13]
        self.Glucose=feature[14]
        self.Distilled_Water=feature[15]
        self.Yeast_extract=feature[16]
        self.Tween80=feature[17]
        self.Tryptone=feature[18]
        self.Casein=feature[19]
        self.L_Cysteine_HCl=feature[20]
        self.VitaminB12=feature[21]
        self.H3BO=feature[22]
        self.Meat_extract=feature[23]
        self.feature=np.array(feature)

    
class InputFeature:
    def __init__(self,bac_feature,media_feature):  #accept bacfeature and mediafeature classes
        self.bac_feature=(bac_feature)   
        self.media_feature=(media_feature)
        
        self.feature=np.concatenate((bac_feature.feature,media_feature.feature))
        
    
def randombac():
    total_gene=random.randint(200,50000)
    random_feature=constrained_sum_sample_pos(19,total_gene)
    bac=BacFeature(random_feature)
    return bac

def randommedia():
    random_feature=constrained_sum_sample_pos(24,100)
    media=MediaFeature(random_feature)
    return media
        
        
        
        
        
        
        
        