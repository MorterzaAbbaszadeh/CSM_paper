#%%

import numpy as np
import pandas as pd
import sklearn.metrics as metrics
from hmmlearn import hmm
import pickle

from include_package import Welcome_party
Welcome_party().initialize()

from dlc_iteration import dlc_db
db=dlc_db()


np.random.seed(2023)
t_p='30'
eval_group=['LID']
dim=4 #training dimension
n_com=2 #number of HMM states


def stack_feats(db, cut=7100):
    return np.vstack((db.main_ar()[:cut], db.mid_head_angs_atan()[:cut], db.rot_speed()[:cut], 
                db.translation()[:cut])).swapaxes(1,0)

def get_hmm_features(db, t_p):
    features=np.empty((0,dim))

    for ky in db.keys:
        db.get_animal(ky, t_p)
        features=np.vstack((features,stack_feats(db)))

    return features


def train_d1_hmm(features, n_com=2):

    model = hmm.GaussianHMM(n_components=n_com, n_iter=14500)
    model.fit(features[:,2:]) #rot_speed and translate
    return model

def train_d2_hmm(features   , n_com=2):

    model = hmm.GaussianHMM(n_components=n_com, n_iter=14500)
    model.fit(features[:,:2]) #rot_speed and translate
    return model

#%% train and save D1model


db=dlc_db()
targs=['LID']
db.select_treatment(targets=targs)
feats=get_hmm_features(db, t_p)


#%%
d1_model=train_d1_hmm(feats, n_com=2)
with open("5p_D1HMM_atan.pkl", "wb") as file: pickle.dump(d1_model, file)



# %% train and save D2model
d2_model=train_d2_hmm(feats, n_com=2)
with open("5p_D2HMM.pkl_atan", "wb") as file: pickle.dump(d2_model, file) 

# %%
