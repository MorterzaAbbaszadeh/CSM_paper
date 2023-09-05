#%%

import numpy as np
import pandas as pd
from include_package import Welcome_party
Welcome_party().initialize()
from dlc_iteration import dlc_db


def feats(db, cut=7100):
    cut=np.amin([len(db.main_ar()), len(db.mid_head_angs()), len(db.rot_speed()), 
                len(db.translation())])
    
    return np.vstack((db.main_ar()[:cut], db.mid_head_angs()[:cut], db.rot_speed()[:cut], 
                db.translation()[:cut])).swapaxes(1,0)



def decode_time(db, model, m_type='d2'):

    features=feats(db, cut=7100)
    if m_type=='d1':
        labels=model.predict(features[:, 2:])
    elif m_type=='d2':
        labels=model.predict(features[:,:2])

    return len(labels[labels==0])/features.shape[0]



def decoded_ts(db, model, m_type='d2'):

    features=feats(db, cut=7100)
    if m_type=='d1':
        labels=model.predict(features[:, 2:])
    elif m_type=='d2':
        labels=model.predict(features[:,:2])


    return labels


def time_spent(db , model, m_type='d2'):

    characters=[]
    for the_ky in db.keys:
        
        i=0
        while i<len(db.t_ps):
            t_point=db.t_ps[i]
            
            
            try:
                db.get_animal(the_ky, db.t_ps[i])
                characters.append((decode_time(db, model, m_type),int(t_point), the_ky, db.treatment)) #could add self.ar0 here
            except:
                print(the_ky+'missing'+t_point)

            i+=1


    return characters


#%%
import pickle
def get_model(adrs):
    with open(adrs, "rb") as file: model=pickle.load(file)
    return model


db=dlc_db()
targs=['LID', 'SUM', 'SKF']
db.select_treatment(targets=targs)
adrs=r'/home/morteza/dlc_projects/Analysis/Currencodes/data_sets/5p_D2HMM.pkl_atan'
model=get_model(adrs)

times_df=time_spent(db , model, m_type='d2')
expression_df=pd.DataFrame(times_df, columns=['state_exp','time', 'animal', 'treatment'])
expression_df.replace({'treatment' : { 'SKF' : 'D1Ag',  'SUM' :'D2Ag',
                            'LID':'LD-3mg', 'D1A':'D1Ant', 'D2A':'D2Ant' }}, inplace=True)
expression_df.head()


#%%
import seaborn as sns
sns.pointplot(x='time',y='state_exp', hue='treatment', data=expression_df)



#%%

def inside_out(dct, model, kin, t_point):
    
    in_and_out=[]


    for ky in dct.keys():
        

        treatment=dct[ky]['treatment']


        features=kin.get_3Dembd_train(dct, ky, kin, t_point )
        labels=model.predict(features)
        

        inside= features[[labels==1][0],:]#[labels==1][0]
        outside= features[[labels==0][0],:]

        inside_ar, inside_absrot_speed,inside_head_ang =np.mean(inside[:,0]),np.mean(inside[:,1]), np.mean(inside[:,2])
        outside_ar,  outside_absrot_speed, outside_head_ang,=np.mean(outside[:,0]),np.mean(outside[:,1]), np.mean(outside[:,2])

        in_and_out.append((inside_ar, inside_head_ang, inside_absrot_speed,ky, treatment, 'inside'))
        in_and_out.append((outside_ar,outside_head_ang, outside_absrot_speed,ky, treatment, 'outside'))


    return in_and_out


