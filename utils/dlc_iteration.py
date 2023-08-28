import numpy as np
import scipy.signal as sgn
import kinematics as kin

class dlc_db():

    def __init__(self):

        self.pth=r'C:\MachineShop\CSM_paper\data\5p_d_base.npy'
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

    def main_ar(self):
        return kin.ar(self.x_tail, self.y_tail, self.xm_head, self.ym_head)
    
    def rot_angs(self):
        return kin.angs(self.xm_head, self.ym_head, self.x_tail, self.y_tail)
    
    def rot_speed(self):
        return kin.smooth_diff(self.rot_angs())
    
    def translation(self):
        return kin.translation(self.xm_head, self.ym_head)