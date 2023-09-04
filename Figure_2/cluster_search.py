

#%% initialize

import numpy as np
np.random.seed(2023)

import pandas as pd
import seaborn as sns
from sklearn.metrics import roc_auc_score
from itertools import combinations
from hmmlearn import hmm

#local
from include_package import Welcome_party
Welcome_party().initialize()

def get_name(ky, map,map_name='_'):
    for m_name in map:
        map_name=map_name+m_name
    return ky+map_name

def extract_state(features, n_com=2):

    model = hmm.GaussianHMM(n_components=n_com, n_iter=14500)
    model.fit(features)
    return model.predict(features)


obsrvs=['R','phi','Tr', 'theta']
mappings=list(combinations(obsrvs, 2))+list(combinations(obsrvs, 3))
print(mappings)

#%%
from dlc_iteration import dlc_db


#get states:
cut=7100
targs=['LID']
db=dlc_db()
db.select_treatment(targets=targs)
print(db.keys)


def get_states(db, ky, mappings, cut=7100):
    states={}

    
    for map in mappings:
        the_map=[]
        if 'R' in map:
            the_map.append(db.main_ar()[:cut])
        if 'phi' in map:
            the_map.append(db.mid_head_angs()[:cut])
        if  'Tr' in map:
            the_map.append(db.translation()[:cut])
        if 'theta' in map:
            the_map.append(db.main_ar()[:cut])

        feats=np.array(the_map).reshape(-1,len(map))
        print(feats.shape)
        map_name=get_name(ky, map)
        states[map_name]=extract_state(feats, n_com=2)

    return states


#filter states

def get_state_cnt(db,iter_lim=50):
    state_cnt=[]
    for ky in db.keys:
        db.get_animal(ky, '30')

        states=get_states(db, ky, mappings)
        states_ls=list(states.keys())
        state_cnt.append((len(states_ls), 1, ky))

        for itr in range(2,iter_lim): #silly but cant use while due to racing

            print(len(states_ls))
            comb=np.random.choice(len(states_ls), 2)
            roc_states= roc_auc_score(states[states_ls[comb[0]]],states[states_ls[comb[1]]])
            if roc_states<0.55:
                    states_ls.remove(states_ls[comb[1]])

            state_cnt.append((len(states_ls), itr, ky))
            itr=itr+1

    return state_cnt


            

# %%

cnt=get_state_cnt(db)


#%%
cnt_df=pd.DataFrame(cnt, columns=['n_states', 'n_iter', 'animal'])
sns.lineplot(x='n_iter', y='n_states', data=cnt_df)
# %%
ky=db.keys
states=get_states(db, ky,mappings, cut=7100)
# %%
