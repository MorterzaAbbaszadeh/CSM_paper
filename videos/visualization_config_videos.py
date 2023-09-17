

#%%
import matplotlib.pyplot as plt
import matplotlib.colors as color
import matplotlib.ticker as ticker
from matplotlib.collections import LineCollection
import seaborn as sns
import numpy as np

#initialize

#global
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stat
import warnings
warnings.simplefilter('ignore', category=DeprecationWarning)
#local
from include_package import Welcome_party
Welcome_party().initialize()





class visual_config():



    def __init__(self):
        
        '''             Visualization settings for the plots                            '''

        self.d1_cls = [ "#e74c3c", "#34495e" ]
        self.d2_cls = [  "#2ecc71", "#34495e"]
        
        ''''                   Housekeeping functions for the plots     '''

        self.label_font = {  'weight' : 'normal',
                                'size'   : 14           }

        self.title_font = {     'weight' : 'bold',
                                'size'   : 16           }

        self.tick_font = {     'weight' : 'normal',
                                'size'   : 10            }

        self.heatmap_font= 8



        self.legend={   'fontsize':10,
                        'title':None,
                        'fancybox':True, 
                        'edgecolor':None, 
                        'frameon':False}

        
    '''                   Housekeeping functions for the plots  '''     

    def forceAspect(self, ax,ratio):
        xleft, xright = ax.get_xlim()
        ybottom, ytop = ax.get_ylim()
        ax.set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)
        return ax , 

    

    def segment_colors(self, ax, t_srs, time, labels, recpt, lw=2): 

        '''
        produces segmented colors

        '''
        xy = np.array([time, t_srs]).T.reshape(-1, 1, 2)
        segments = np.hstack([xy[:-1], xy[1:]])
      

        if recpt=='d1':
            cm = dict(zip(range(0,2 ,1),self.d2_cls))
        elif recpt=='d2':
            cm = dict(zip(range(0,2 ,1),self.d1_cls))
    
        cls = list( map( cm.get , labels))
    
        lc = LineCollection(segments, colors=cls, linewidths=lw)
        ax.add_collection(lc)
        return ax 
    

    def segment_colors_3D(self, ax, t_srs, t_sts2, t_srs3, labels, recpt, lw=2): 

        '''
        #produces segmented colors

        '''
        xy = np.array([t_srs, t_sts2, t_srs3]).T.reshape(-1, 1, 3)
        segments = np.hstack([xy[:-1], xy[1:]])
        
    

        if recpt=='d1':
            cm = dict(zip(range(0,2 ,1),self.d2_cls))
        elif recpt=='d2':
            cm = dict(zip(range(0,2 ,1),self.d1_cls))
    
        cls = list( map( cm.get , labels))
    
        lc = LineCollection(segments, colors=cls, linewidths=lw)
        ax.add_collection(lc)
        return ax 



    ####################
    #frame base
    def visualize_ts(self, ax, anim, strt, fini, gap=50): #db > after get_anim

        ar=anim.main_ar()
        head_ang=anim.mid_head_angs_atan()

        #time=np.linspace(0,cut, cut)/fps

        #treat=anim.treatment
        label_loc=[-0.08, 0.5]


        ax[0].plot(ar[:fini], color='r', lw=2)
        ax[0].set_ylabel(r'R.', fontdict=self.label_font)
        ax[0].yaxis.set_label_coords(-.1, .5)
        ax[0].set_xlim(strt, fini+gap)
        ax[0].set_ylim(0, 100)
        ax[0].tick_params(bottom=False, top=False, left=True, right=False)
        ax[0].set_xticks([], [])
        ax[0].set_yticks([], [])
        ax[0].patch.set_visible(False)
        sns.despine(top=True, bottom=True, right=True, left=True, ax=ax[0])

        ax[1].plot(head_ang[:fini], color='r', lw=2)
        ax[1].set_ylabel(r'$\phi $', fontdict=self.label_font)
        ax[1].yaxis.set_label_coords(-.1, .5)
        ax[1].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[1].set_xlim(strt, fini+gap)
        ax[1].set_ylim(80, 120)
        ax[1].set_xlabel('')
        ax[1].set_xticks([], [])
        ax[1].set_yticks([], [])
        ax[1].patch.set_visible(False)
        sns.despine(top=True, right=True, left=True, bottom=True, ax=ax[1])



        return ax


    def visualize_phis(self, ax, anim, strt, fini, gap=50): #db > after get_anim

        head_ang=anim.mid_head_angs_atan()
        mid_ang_1=anim.mid_mid_angs_atan()
        mid_ang_2=anim.tail_mid_angs_atan()

        label_loc=[-0.08, 0.5]

        ax[0].plot(head_ang[strt:fini], color='r', lw=2)
        ax[0].set_ylabel(r'mid_head', fontdict=self.label_font)
        ax[0].yaxis.set_label_coords(-.1, .5)
        ax[0].set_xlim(strt, fini+gap)
        #ax[0].set_ylim(0, 100)
        ax[0].tick_params(bottom=False, top=False, left=True, right=False)
        ax[0].set_xticks([], [])
        ax[0].set_yticks([], [])
        ax[0].patch.set_visible(False)
        sns.despine(top=True, bottom=True, right=True, left=True, ax=ax[0])

        ax[1].plot(mid_ang_1[strt:fini], color='r', lw=2)
        ax[1].set_ylabel(r'mid-mid', fontdict=self.label_font)
        ax[1].yaxis.set_label_coords(-.1, .5)
        ax[1].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[1].set_xlim(strt, fini+gap)
        #ax[1].set_ylim(80, 120)
        ax[1].set_xlabel('')
        ax[1].set_xticks([], [])
        ax[1].set_yticks([], [])
        ax[1].patch.set_visible(False)
        sns.despine(top=True, right=True, left=True, bottom=True, ax=ax[1])
        
        ax[2].plot(mid_ang_2[strt:fini], color='r', lw=2)
        ax[2].set_ylabel(r'tail_mid', fontdict=self.label_font)
        ax[2].yaxis.set_label_coords(-.1, .5)
        ax[2].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[2].set_xlim(strt, fini+gap)
        #ax[2].set_ylim(80, 120)
        ax[2].set_xlabel('')
        ax[2].set_xticks([], [])
        ax[2].set_yticks([], [])
        ax[2].patch.set_visible(False)
        sns.despine(top=True, right=True, left=True, bottom=True, ax=ax[2])

        return ax

    def visualize_ars(self, ax, anim, strt, fini, gap=50): #db > after get_anim


        main_ar=anim.main_ar()
        mid_ar=anim.mid2_ar()
        mean_ar=anim.mean_ar()
        label_loc=[-0.08, 0.5]

        ax[0].plot(main_ar[:fini], color='r', lw=2)
        ax[0].set_ylabel(r'main R', fontdict=self.label_font)
        ax[0].yaxis.set_label_coords(-.1, .5)
        ax[0].set_xlim(strt, fini+gap)
        #ax[0].set_ylim(0, 100)
        ax[0].tick_params(bottom=False, top=False, left=True, right=False)
        ax[0].set_xticks([], [])
        ax[0].set_yticks([], [])
        ax[0].patch.set_visible(False)
        sns.despine(top=True, bottom=True, right=True, left=True, ax=ax[0])

        ax[1].plot(mean_ar[:fini], color='r', lw=2)
        ax[1].set_ylabel(r'mean R', fontdict=self.label_font)
        ax[1].yaxis.set_label_coords(-.1, .5)
        ax[1].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[1].set_xlim(strt, fini+gap)
        #ax[1].set_ylim(80, 120)
        ax[1].set_xlabel('')
        ax[1].set_xticks([], [])
        ax[1].set_yticks([], [])
        ax[1].patch.set_visible(False)
        sns.despine(top=True, right=True, left=True, bottom=True, ax=ax[1])

        ax[2].plot(mid_ar[:fini], color='r', lw=2)
        ax[2].set_ylabel(r'mid R', fontdict=self.label_font)
        ax[2].yaxis.set_label_coords(-.1, .5)
        ax[2].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[2].set_xlim(strt, fini+gap)
        #ax[1].set_ylim(80, 120)
        ax[2].set_xlabel('')
        ax[2].set_xticks([], [])
        ax[2].set_yticks([], [])
        ax[2].patch.set_visible(False)
        sns.despine(top=True, right=True, left=True, bottom=True, ax=ax[2])

        return ax



    def visualize_trans(self, ax, anim, strt, fini, gap=50): #db > after get_anim


        main_tr=anim.translation()
        mid_tr=anim.mid_translation()
        label_loc=[-0.08, 0.5]

        ax[0].plot(main_tr[:fini], color='r', lw=2)
        ax[0].set_ylabel(r'main Tr', fontdict=self.label_font)
        ax[0].yaxis.set_label_coords(-.1, .5)
        ax[0].set_xlim(strt, fini+gap)
        #ax[0].set_ylim(0, 100)
        ax[0].tick_params(bottom=False, top=False, left=True, right=False)
        ax[0].set_xticks([], [])
        ax[0].set_yticks([], [])
        ax[0].patch.set_visible(False)
        sns.despine(top=True, bottom=True, right=True, left=True, ax=ax[0])

        ax[1].plot(mid_tr[:fini], color='r', lw=2)
        ax[1].set_ylabel(r'mid Tr', fontdict=self.label_font)
        ax[1].yaxis.set_label_coords(-.1, .5)
        ax[1].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[1].set_xlim(strt, fini+gap)
        #ax[1].set_ylim(80, 120)
        ax[1].set_xlabel('')
        ax[1].set_xticks([], [])
        ax[1].set_yticks([], [])
        ax[1].patch.set_visible(False)
        sns.despine(top=True, right=True, left=True, bottom=True, ax=ax[1])
    

        return ax

    def visualize_rot_speed(self, ax, anim, strt, fini, gap=50): #db > after get_anim


        rot_speed=anim.rot_speed()
        head_rot_speed=anim.head_rot_speed()
        mid_rot_speed=anim.mid_rot_speed()
        label_loc=[-0.08, 0.5]

        ax[0].plot(rot_speed[:fini], color='r', lw=2)
        ax[0].set_ylabel(r'rot speed', fontdict=self.label_font)
        ax[0].yaxis.set_label_coords(-.1, .5)
        ax[0].set_xlim(strt, fini+gap)
        #ax[0].set_ylim(0, 100)
        ax[0].tick_params(bottom=False, top=False, left=True, right=False)
        ax[0].set_xticks([], [])
        ax[0].set_yticks([], [])
        ax[0].patch.set_visible(False)
        sns.despine(top=True, bottom=True, right=True, left=True, ax=ax[0])

        ax[1].plot(head_rot_speed[:fini], color='r', lw=2)
        ax[1].set_ylabel(r'head Rot speed', fontdict=self.label_font)
        ax[1].yaxis.set_label_coords(-.1, .5)
        ax[1].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[1].set_xlim(strt, fini+gap)
        #ax[1].set_ylim(80, 120)
        ax[1].set_xlabel('')
        ax[1].set_xticks([], [])
        ax[1].set_yticks([], [])
        ax[1].patch.set_visible(False)
        sns.despine(top=True, right=True, left=True, bottom=True, ax=ax[1])

        ax[2].plot(mid_rot_speed[:fini], color='r', lw=2)
        ax[2].set_ylabel(r'mid_rot_speed', fontdict=self.label_font)
        ax[2].yaxis.set_label_coords(-.1, .5)
        ax[2].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[2].set_xlim(strt, fini+gap)
        #ax[2].set_ylim(80, 120)
        ax[2].set_xlabel('')
        ax[2].set_xticks([], [])
        ax[2].set_yticks([], [])
        ax[2].patch.set_visible(False)
        sns.despine(top=True, right=True, left=True, bottom=True, ax=ax[2])

        return ax
