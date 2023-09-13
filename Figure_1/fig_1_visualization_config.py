
#a class that stores visualization settings and functions for matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as color
import matplotlib.ticker as ticker
import seaborn as sns
import numpy as np

class visual_config():



    def __init__(self):
        
        '''             Visualization settings for the plots                            '''
        #color set

        self.tretament_pal=sns.color_palette("tab10")
        self.treatment_color_list=self.tretament_pal.as_hex() #round_1colors


        self.treatments=['LD-3mg','D1Ag','D2Ag','D1Ant','D2Ant','D2K', 'Vehicle']

        self.treatment_cols=['darkviolet', 'cyan' , 'darkgrey', 'limegreen', 'orangered', 'chocolate', 'black']
       
       
        def treat_cls(slef):
            cls_dct={}
            for i,j in enumerate(self.treatments):
                    cls_dct[self.treatments[i]]=self.treatment_cols[i] 
            return cls_dct
            

        
        self.treatment_colors=treat_cls(self)  #sefl hotfix, fix later




        self.compare_colors_sr = ["#95a5a6", "#e74c3c", 
                                  "#34495e", "#2ecc71"]
        self.compare_colors=sns.set_palette(sns.color_palette(self.compare_colors_sr))

        self.compare_colors_sr2 = [ "#3498db","#9b59b6",
                                     "#95a5a6", "#e74c3c", 
                                    "#34495e", "#2ecc71"]
        self.compare_colors2=sns.set_palette(sns.color_palette(self.compare_colors_sr2))


                                #palette=palette

        self.heatmap_cmp= sns.cubehelix_palette(light=1.05, as_cmap=True)
        self.gradient_colors=sns.color_palette("RdPu", 10)       
       



        #fonts

        self.label_font = {  'weight' : 'normal',
                                'size'   : 16           }

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



    #messy with alot of constants
    def head_polar_plot(self,ax, head_ang, ar,lower_cut, upper_cut, treatment, alph=0.1 ):
        
        
        
        ax.plot( head_ang[lower_cut:upper_cut],ar[lower_cut:upper_cut],
                            
                                ls='', marker='o',color=self.treatment_colors[treatment], alpha=alph)


        ax.grid(linewidth=1, ls='--')

        ax.set_xticklabels(['270', '', '0', '', '90', '', '180', ''])
        ax.set_ylim(0,1.5) #normalized body
   
        ax.set_rticks([0, 0.5, 1, 1.5])
       
        ax.spines['polar'].set_visible(False)

        

        return ax


    def presence_heat_maps(self, axs,cent_x,cent_y, lower_cut, upper_cut ):



        cbar_kws = {'format':'%.1e'}


        axs.plot(cent_x[lower_cut:upper_cut],cent_y[lower_cut:upper_cut],linewidth=0.3, color='k', alpha=0.5)#,cumulative=True,
    
        arena=plt.Circle((320, 320),320, fill=False, linestyle='--', linewidth=0.5)
        axs.add_patch(arena)
        axs.set_xlim(0, 640)
        axs.set_ylim(0, 640)
        sns.despine(top=True, bottom=True, left=True, right=True)
        axs.set_xticks([],[])
        axs.set_yticks([],[])
        axs.set_aspect(1)

        sns.kdeplot(x=cent_x[lower_cut:upper_cut],y=cent_y[lower_cut:upper_cut],shade=True, 
                    cmap=self.heatmap_cmp, cbar=True, cbar_kws = cbar_kws, ax=axs)#,cumulative=True,
       
        return axs
    

    def sns_plots(self, ax, xlabel, ylabel, legend=False):
    
        
        
        ax.set_xlabel(xlabel, fontdict=self.label_font)
        ax.set_ylabel(ylabel, fontdict=self.label_font)


        sns.despine(ax=ax)
        
        if isinstance(legend, dict):
            plt.legend(**legend)
        else:
            ax.legend([],[], frameon=False, fontsize=self.tick_font['size'])

         #make this local

            
        return ax
    

    '''                        Time series                                 '''


    def visualize_phis(self, anim, strt, fini, cut, fps, treat): #db > after get_anim

        _, ax = plt.subplots(3)
        head_ang=anim.mid_head_angs_atan()[:cut]
        mid_ang_1=anim.mid_mid_angs_atan()[:cut]
        mid_ang_2=anim.tail_mid_angs_atan()[:cut]

        time=np.linspace(0,cut, cut)/fps

        #treat=anim.treatment
        label_loc=[-0.08, 0.5]

        ax[0].plot(time, head_ang, linewidth=0.9, color=self.treatment_colors[treat])
        ax[0].set_ylabel(r'$\phi$', fontdict=self.label_font)
        ax[0].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[0].set_xlim(strt, fini)
        ax[0].tick_params(bottom=False, top=False, left=True, right=False)
        ax[0].set_xticklabels([])
        sns.despine(top=True, bottom=True, right=True, ax=ax[0])

        ax[1].plot(time, mid_ang_1, linewidth=0.9, color=self.treatment_colors[treat])
        ax[1].set_ylabel(r'$\phi$ mid1', fontdict=self.label_font)
        ax[1].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[1].set_xlim(strt, fini)
        ax[1].tick_params(bottom=False, top=False, left=True, right=False)
        ax[1].set_xticklabels([])
        sns.despine(top=True, bottom=True, right=True, ax=ax[1])

        ax[2].plot(time, mid_ang_2, linewidth=0.9, color=self.treatment_colors[treat])
        ax[2].set_ylabel(r'$\phi$ mid2', fontdict=self.label_font)
        ax[2].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[2].set_xlim(strt, fini)
        ax[2].tick_params(bottom=False, top=False, left=True, right=False)
        ax[2].set_xlabel('Time (sec)', fontdict=self.label_font)
        sns.despine(top=True, right=True, ax=ax[2])




        return ax

    def visualize_ars(self, anim, strt, fini, cut, fps, treat): #db > after get_anim

        _, ax = plt.subplots(2)
        main_ar=anim.main_ar()[:cut]
        mean_ar=anim.mean_ar()[:cut]

        time=np.linspace(0,cut, cut)/fps

        #treat=anim.treatment
        label_loc=[-0.08, 0.5]

        ax[0].plot(time, main_ar, linewidth=0.9, color=self.treatment_colors[treat])
        ax[0].set_ylabel(r'ar', fontdict=self.label_font)
        ax[0].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[0].set_xlim(strt, fini)
        ax[0].tick_params(bottom=False, top=False, left=True, right=False)
        ax[0].set_xticklabels([])
        sns.despine(top=True, bottom=True, right=True, ax=ax[0])

        ax[1].plot(time, mean_ar, linewidth=0.9, color=self.treatment_colors[treat])
        ax[1].set_ylabel(r'mean ar', fontdict=self.label_font)
        ax[1].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[1].set_xlim(strt, fini)
        ax[1].tick_params(bottom=False, top=False, left=True, right=False)
        ax[1].set_xlabel('Time (sec)', fontdict=self.label_font)
        sns.despine(top=True, right=True, ax=ax[1])




        return ax


    def visualize_trans(self, anim, strt, fini, cut, fps, treat): #db > after get_anim

        _, ax = plt.subplots(2)
        main_tr=anim.translation()[:cut]
        mid_tr=anim.mid_translation()[:cut]

        time=np.linspace(0,cut, cut)/fps

        #treat=anim.treatment
        label_loc=[-0.08, 0.5]

        ax[0].plot(time, main_tr, linewidth=0.9, color=self.treatment_colors[treat])
        ax[0].set_ylabel(r'Tr.', fontdict=self.label_font)
        ax[0].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[0].set_xlim(strt, fini)
        ax[0].tick_params(bottom=False, top=False, left=True, right=False)
        ax[0].set_xticklabels([])
        sns.despine(top=True, bottom=True, right=True, ax=ax[0])


        ax[1].plot(time, mid_tr, linewidth=0.9, color=self.treatment_colors[treat])
        ax[1].set_ylabel(r'Mid Tr.', fontdict=self.label_font)
        ax[1].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[1].set_xlim(strt, fini)
        ax[1].tick_params(bottom=False, top=False, left=True, right=False)
        ax[1].set_xlabel('Time (sec)', fontdict=self.label_font)
        sns.despine(top=True, right=True, ax=ax[1])




        return ax

    def visualize_rot_speed(self, anim, strt, fini, cut, fps, treat): #db > after get_anim

        _, ax = plt.subplots(3)
        rot_speed=anim.rot_speed()[:cut]
        head_rot_speed=anim.head_rot_speed()[:cut]
        mid_rot_speed=anim.mid_rot_speed()[:cut]

        time=np.linspace(0,cut, cut)/fps

        #treat=anim.treatment
        label_loc=[-0.08, 0.5]

        ax[0].plot(time, rot_speed, linewidth=0.9, color=self.treatment_colors[treat])
        ax[0].set_ylabel(r'rot_speed', fontdict=self.label_font)
        ax[0].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[0].set_xlim(strt, fini)
        ax[0].tick_params(bottom=False, top=False, left=True, right=False)
        ax[0].set_xticklabels([])
        sns.despine(top=True, bottom=True, right=True, ax=ax[0])

        ax[1].plot(time, mid_rot_speed, linewidth=0.9, color=self.treatment_colors[treat])
        ax[1].set_ylabel(r'mid_rot', fontdict=self.label_font)
        ax[1].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[1].set_xlim(strt, fini)
        ax[1].tick_params(bottom=False, top=False, left=True, right=False)
        ax[1].set_xticklabels([])
        sns.despine(top=True, bottom=True, right=True, ax=ax[1])

        ax[2].plot(time, head_rot_speed, linewidth=0.9, color=self.treatment_colors[treat])
        ax[2].set_ylabel(r'head Rot', fontdict=self.label_font)
        ax[2].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[2].set_xlim(strt, fini)
        ax[2].tick_params(bottom=False, top=False, left=True, right=False)
        ax[2].set_xlabel('Time (sec)', fontdict=self.label_font)
        sns.despine(top=True, right=True, ax=ax[2])




        return ax


    def visualize_ts(self, anim, strt, fini, cut, fps, treat): #db > after get_anim

        _, ax = plt.subplots(4)
        ar=anim.main_ar()[:cut]
        head_ang=anim.mid_head_angs_atan()[:cut]
        rot_speed=anim.rot_speed()[:cut]
        translate=anim.translation()[:cut]

        time=np.linspace(0,cut, cut)/fps

        #treat=anim.treatment
        label_loc=[-0.08, 0.5]

        ax[0].plot(time, head_ang, linewidth=0.9, color=self.treatment_colors[treat])
        ax[0].set_ylabel(r'$\phi $', fontdict=self.label_font)
        ax[0].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[0].set_xlim(strt, fini)
        ax[0].tick_params(bottom=False, top=False, left=True, right=False)
        ax[0].set_xticklabels([])
        sns.despine(top=True, bottom=True, right=True, ax=ax[0])


        ax[1].plot(time, ar, linewidth=0.9, color=self.treatment_colors[treat])
        ax[1].set_ylabel(r'R', fontdict=self.label_font)
        ax[1].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[1].set_xlim(strt, fini)
        ax[1].tick_params(bottom=False, top=False, left=True, right=False)
        ax[1].set_xticklabels([])
        sns.despine(top=True, bottom=True, right=True, ax=ax[1])

        ax[2].plot(time, rot_speed, linewidth=0.9, color=self.treatment_colors[treat])
        ax[2].set_ylabel(r'd$\theta$/dt', fontdict=self.label_font)
        ax[2].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[2].set_xlim(strt, fini)
        ax[2].tick_params(bottom=False, top=False, left=True, right=False)
        ax[2].set_xticklabels([])
        sns.despine(top=True, bottom=True, right=True, ax=ax[2])

        ax[3].plot(time, translate, linewidth=0.9, color=self.treatment_colors[treat])
        ax[3].set_ylabel(r'Tr.', fontdict=self.label_font)
        ax[3].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[3].set_xlim(strt, fini)
        ax[3].set_xlabel('Time (sec)', fontdict=self.label_font)
        sns.despine(top=True, right=True, ax=ax[3])


        

        return ax

    

