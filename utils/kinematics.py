import numpy as np
import scipy.signal as sgn




def angs(x1,y1,x2,y2): #rendering vectro angles from 0 to 360

    theta=np.zeros(len(x1))
    

    i=0
    while i<len(x1):

        if y2[i]-y1[i]>0:
            theta[i]=np.arccos((x2[i]-x1[i])/(np.sqrt((x2[i]-x1[i])**2+(y2[i]-y1[i])**2)))*57.32

        elif y2[i]-y1[i]<0:                     # if the vector falls in third or forth quarters add 180 degs to result
                theta[i]=180+(np.arccos((x1[i]-x2[i])/(np.sqrt((x2[i]-x1[i])**2+(y2[i]-y1[i])**2)))*57.32)
        i+=1


    return np.concatenate((theta, theta[-1:])) #compensates for size difference in differentiation



def ar(x1,y1,x2,y2):

    ar=np.sqrt(np.square(x2-x1)+np.square(y2-y1))

    ar=np.pad(ar, 50, 'edge')
    
    return sgn.savgol_filter(ar, 45, 4)[50:-50] 




def translation(x, y):                                #calculate the euclidian distance between positions of a point in two frames. 
    
    
    stp=np.zeros(len(x))

    i=0
    while i<len(x)-1:
        stp[i]=np.sqrt(np.square(x[i+1]-x[i])+np.square(y[i+1]-y[i]))
        i+=1

    #stp=np.concatenate((stp, stp[-1]))

    stp=np.pad(stp, 50, 'edge')                #pad the signal by its edge
    

    return sgn.savgol_filter(stp, 45, 4)[50:-50]




#def tot_dist(x, y):                                #calculate the euclidian distance between positions of a point in two frames. 

#    return translation(x, y).sum()


def pos_rots(self, x1,y1,x2,y2):

    angs=self.npy_rot_speed(x1,y1,x2,y2)


    pos_rot=0
    neg_rot=0

    c_ang=0


    for ang in angs[:3600]:
        c_ang=c_ang+ang
        if c_ang >= 365:
            pos_rot=pos_rot+1
            c_ang=0
        elif c_ang <= -365:
            neg_rot=neg_rot+1
            c_ang=0
            

    return (pos_rot/len(angs), neg_rot/len(angs))




def thet_head(x1,y1,x2,y2,x3,y3,x4,y4):         #1:tail, 2:mid_head, 3 HeadR, 4:HeadL
    
    
    u=np.array([x2-x1, y2-y1])                  #main body vector
    v=np.array([x4-x3, y4-y3])                  #head vector


    dotp=u[0]*v[0]+u[1]*v[1]                    #dot product


    si_u=np.sqrt(u[0]**2+u[1]**2)
    si_v=np.sqrt(v[0]**2+v[1]**2)



    thet_head=np.arccos(dotp/(si_u*si_v))*57.32   #(abs(dotp/(si_u*si_v)))*57.32 
    sm_head=np.pad(thet_head, 50, 'edge')                #pad the signal by its edge
        
    return sgn.savgol_filter(sm_head, 45, 4)[50:-50]

def null_dperiodic(theta):

    for i, tet in enumerate(theta):
        if tet > 180: theta[i]-=360
        elif tet <= -180: theta[i]+=360

    return theta


def thet_head_atan(x1,y1,x2,y2,x3,y3,x4,y4):         # 1:mid1, 2:mid_head, 3:rhead, 4:lhead
    
    
    xes=x2-x1                 #head
    yes=y2-y1
    
    xno=x4-x3
    yno=y4-y3                 #head vector


    thet_head=np.arctan2(xes, yes)*57.32    
    thet_should=np.arctan2(xno, yno)*57.32   #(abs(dotp/(si_u*si_v)))*57.32 
    thet=null_dperiodic(thet_should-thet_head)
    sm_head=np.pad(thet, 50, 'edge')                #pad the signal by its edge
        
    return thet #sgn.savgol_filter(sm_head, 45, 4)[50:-50]




def smooth_diff(theta): 

    diff=np.diff(theta)

    for i in range(0,len(diff)):
        if diff[i]>30 or diff[i]<-30 :
            diff[i]=diff[i-1]

    diff=np.append(diff,diff[-1])
    diff=np.pad(diff, 50, 'edge')                #pad the signal by its edge
    
    return sgn.savgol_filter(diff, 45, 4)[50:-50]  
