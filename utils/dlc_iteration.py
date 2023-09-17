import numpy as np
import scipy.signal as sgn
import kinematics as kin

class dlc_db():

    def __init__(self):

        self.pth=r'/home/morteza/dlc_projects/Analysis/Currencodes/data_sets/5p_d_base.npy'
        self.t_ps= ['10','20','30','40','50','60','70', '80']
        with open(self.pth, 'rb') as f:
            self.db=np.load(f, allow_pickle=True)[()]

        self.keys=list(self.db.keys())

    def select_treatment(self, targets):
        self.__init__() # make sure everything is there

        for ky in list(self.db.keys()):
            if not self.db[ky]['treatment'] in targets:
                self.db.pop(ky)
        self.keys=list(self.db.keys())


    def get_animal(self, ky, t_p):    

        self.ky=ky  

        self.treatment=self.db[self.ky]['treatment']
        self.id=self.db[self.ky]['id']

        self.x_rhead=self.db[self.ky]['traces'][t_p]['headR']
        self.y_rhead=self.db[self.ky]['traces'][t_p]['headR.1']

        self.x_lhead=self.db[self.ky]['traces'][t_p]['headL']
        self.y_lhead=self.db[self.ky]['traces'][t_p]['headL.1']

        self.x_mid1=self.db[self.ky]['traces'][t_p]['mid1']
        self.y_mid1=self.db[self.ky]['traces'][t_p]['mid1.1']

        self.x_mid2=self.db[self.ky]['traces'][t_p]['mid2']
        self.y_mid2=self.db[self.ky]['traces'][t_p]['mid2.1']

        self.x_tail=self.db[self.ky]['traces'][t_p]['tail']
        self.y_tail=self.db[self.ky]['traces'][t_p]['tail.1']

        self.xm_head=(self.x_lhead+self.x_rhead)/2
        self.ym_head=(self.y_lhead+self.y_rhead)/2


    
    def tail_head_angs(self):
        return kin.thet_head(self.x_tail, self.y_tail, self.xm_head, self.ym_head,
                             self.x_rhead,self.y_rhead, self.x_lhead, self.y_lhead)

    def mid_head_angs(self):
        return kin.thet_head(self.x_mid1, self.y_mid1, self.xm_head, self.ym_head,
                             self.x_rhead,self.y_rhead, self.x_lhead, self.y_lhead)

    def mid_head_angs_atan(self):
        return kin.thet_head_atan(self.x_mid1, self.y_mid1, self.xm_head, self.ym_head,
                             self.x_rhead,self.y_rhead, self.x_lhead, self.y_lhead)-90
    
    def mid_head_angs(self):
        return kin.thet_head(self.x_mid1, self.y_mid1, self.xm_head, self.ym_head,
                             self.x_rhead,self.y_rhead, self.x_lhead, self.y_lhead)-90


    def mid_mid_angs_atan(self):
        return kin.thet_head_atan(self.x_mid2, self.y_mid2, self.x_mid1, self.y_mid1,
                                self.x_mid1, self.y_mid1, self.xm_head, self.ym_head)

    def tail_mid_angs_atan(self):
        return kin.thet_head_atan(self.x_tail, self.y_tail,self.x_mid2, self.y_mid2, 
                                self.x_mid2, self.y_mid2, self.x_mid1, self.y_mid1)



    
    def rot_speed(self):
        return kin.smooth_diff(kin.angs(self.xm_head, self.ym_head, self.x_tail, self.y_tail))
    
    def head_rot_speed(self):
        return kin.smooth_diff(kin.angs(self.x_lhead, self.y_lhead,self.x_rhead, self.y_rhead))

    def mid_rot_speed(self):
        return kin.smooth_diff(kin.angs(self.x_mid1, self.y_mid1,self.x_mid2, self.y_mid2))




    def main_ar(self):
        return kin.ar(self.x_tail, self.y_tail, self.xm_head, self.ym_head)

    def mid_ar(self):
        return kin.ar(self.x_mid1, self.y_mid1, self.xm_head, self.ym_head)

    def mid2_ar(self):
        return kin.ar(self.x_mid2, self.y_mid2, self.x_mid1, self.y_mid1)

    def mean_ar(self):
        ar1=kin.ar(self.x_mid2, self.y_mid2, self.x_mid1, self.y_mid1)
        ar2=kin.ar(self.x_mid1, self.y_mid1, self.xm_head, self.ym_head)
        ar3=kin.ar(self.x_tail, self.y_tail, self.xm_head, self.ym_head)
        ar4=kin.ar(self.x_mid2, self.y_mid2, self.xm_head, self.ym_head)
        return np.mean([ar1,ar2,ar3,ar4], axis=0)



    def translation(self):
        return kin.translation(self.xm_head, self.ym_head)

    def mid_translation(self):
        return kin.translation(self.x_mid1, self.y_mid1)