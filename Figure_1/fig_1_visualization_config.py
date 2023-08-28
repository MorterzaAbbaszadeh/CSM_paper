
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






    '''                    Kinematic Plots                           


    def kinematic_box(self, ax, xlabel, ylabel, legend=False):
        

        ax.set_xlim(-0.5, 8.5)
        
        ax.set_xlabel(xlabel, fontdict=self.label_font)
        ax.set_ylabel(ylabel, fontdict=self.label_font)


        sns.despine(ax=ax)
        
        
        if isinstance(legend, dict):
            plt.legend(**legend)
        else:
            ax.legend([],[], frameon=False, fontsize=self.tick_font['size'])

         #make this local
    
        return ax


    def kinematic_lines(self, ax, xlabel, ylabel, legend=False):
        

        ax.set_xlim(-0.5, 8.5)
        
        ax.set_xlabel(xlabel, fontdict=self.label_font)
        ax.set_ylabel(ylabel, fontdict=self.label_font)


        sns.despine(ax=ax)
        
        
        if isinstance(legend, dict):
            plt.legend(**legend)
        else:
            ax.legend([],[], frameon=False, fontsize=self.tick_font['size'])

         #make this local

        sns.set_palette(self.compare_colors_sr2)
            
        return ax



    '''

    '''                        HMM Plots                                     



    def hmm_plots(self, ax, xlabel, ylabel, xlim_right=8.5, legend=False):
        

        ax.set_xlim(-0.5, xlim_right)
        
        ax.set_xlabel(xlabel, fontdict=self.label_font)
        ax.set_ylabel(ylabel, fontdict=self.label_font)


        sns.despine(ax=ax)
        
        if isinstance(legend, dict):
            plt.legend(**legend)
        else:
            ax.legend([],[], frameon=False, fontsize=self.tick_font['size'])

         #make this local

            
        return ax



    def barplots(self, ax, xlabel, ylabel, legend=False):
    

        ax.set_xlim(-0.5, 8.5)
        
        ax.set_xlabel(xlabel, fontdict=self.label_font)
        ax.set_ylabel(ylabel, fontdict=self.label_font)


        sns.despine(ax=ax)
        
        if isinstance(legend, dict):
            plt.legend(**legend)
        else:
            ax.legend([],[], frameon=False, fontsize=self.tick_font['size'])

            #make this local

            
            return ax

    '''

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



    '''                       Time Series Plots                            



    def visualize_ts(self, ax, dct,  ID_n, time_point,strt, fini, fetch, model, cut, fps, treat ):


        
        head_ang, ar, rot_speed, translate=fetch.time_srs(dct, ID_n,  time_point)
        features=np.vstack(([ar[:cut], rot_speed[:cut], head_ang[:cut], translate[:cut]])).swapaxes(1,0)
        

        time=np.linspace(0,cut, cut)/fps


        
        ar=features[:,0]
        rot_speed=features[:,1]
        head_ang=features[:,2]
        translate=features[:,3]

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






    def visualize_ts_state(self, ax, dct,  ID_n, time_point,strt, fini, fetch, model, cut, fps):


        
        head_ang, ar, rot_speed, translate=fetch.time_srs(dct, ID_n,  time_point)
        features=np.vstack(([ar[:cut], rot_speed[:cut], head_ang[:cut]])).swapaxes(1,0)
        labels=model.predict(features)

        time=np.linspace(0,cut, cut)/fps



        ar=features[:,0]
        rot_speed=features[:,1]
        head_ang=features[:,2]

        label_loc=[-0.08, 0.5]

        circle_size=1.7
        inside_lable=1

        ax[0].plot(time, head_ang, linewidth=0.5)
        ax[0].scatter(time[labels==inside_lable], head_ang[labels==inside_lable],
                     color=self.compare_colors_sr2[3], s=circle_size, label='in-state')
        ax[0].scatter(time[labels!=inside_lable], head_ang[labels!=inside_lable], 
                            color=self.compare_colors_sr2[4], s=circle_size, label='in-state')

        ax[0].set_ylabel(r'$\phi $', fontdict=self.label_font)
        ax[0].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[0].set_xlim(strt, fini)
        ax[0].tick_params(bottom=False, top=False, left=True, right=False)
        ax[0].set_xticklabels([])
        sns.despine(top=True, bottom=True, right=True, ax=ax[0])


        ax[1].plot(time, ar, linewidth=0.5)
        ax[1].scatter(time[labels==inside_lable], ar[labels==inside_lable],
                     color=self.compare_colors_sr2[3], s=circle_size, label='in-state')
        ax[1].scatter(time[labels!=inside_lable], ar[labels!=inside_lable], 
                            color=self.compare_colors_sr2[4], s=circle_size, label='in-state')
        
        ax[1].set_ylabel(r'R', fontdict=self.label_font)
        ax[1].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[1].set_xlim(strt, fini)
        ax[1].tick_params(bottom=False, top=False, left=True, right=False)
        ax[1].set_xticklabels([])
        sns.despine(top=True, bottom=True, right=True, ax=ax[1])


        ax[2].plot(time, rot_speed, linewidth=0.5)
        ax[2].scatter(time[labels==inside_lable], rot_speed[labels==inside_lable],
                     color=self.compare_colors_sr2[3], s=circle_size, label='in-state')
        ax[2].scatter(time[labels!=inside_lable], rot_speed[labels!=inside_lable], 
                            color=self.compare_colors_sr2[4], s=circle_size, label='in-state')
      
        ax[2].set_ylabel(r'd$\theta$/dt', fontdict=self.label_font)
        ax[2].yaxis.set_label_coords(label_loc[0], label_loc[1])
        ax[2].set_xlim(strt, fini)
        ax[2].set_xlabel('Time (sec)', fontdict=self.label_font)
        sns.despine(top=True, right=True, ax=ax[2])


        

        return ax




                            

    def state_polar(self, ax, dct,  ID_n, time_point, fetch, model, cut, state, alph):


        
        head_ang, ar, rot_speed, translate=fetch.time_srs(dct, ID_n,  time_point)
        features=np.vstack(([ar[:cut], rot_speed[:cut], head_ang[:cut]])).swapaxes(1,0)
        labels=model.predict(features)



        inside_lable=1
        ar=features[:,0]
        rot_speed=features[:,1]
        head_ang=features[:,2]
        head_orientation=(head_ang/57.32)



        if state==inside_lable:
            cl=self.compare_colors_sr2[3]
        else: 
            cl=self.compare_colors_sr2[4]

        ax.plot( head_orientation[labels==state],ar[labels==state],
                        ls='', marker='o',color=cl, alpha=alph)


        ax.grid(linewidth=1, ls='--')

        ax.set_xticklabels(['270', '', '0', '', '90', '', '180', ''])
        ax.set_ylim(0,1) #normalized body
   
        ax.set_rticks([0, 0.5, 1])
       
        ax.spines['polar'].set_visible(False)

        return ax

    



    def cluster_bar_plots(self,ax, characters, params):
        for i in range(len(ax)):
            param=list(params.keys())[i]
            sns.barplot(x='Type', y=param,data=characters, palette=self.compare_colors_sr2[3:], errcolor='darkgrey' ,ax=ax[i], ci=95)
            ax[i].set_xlim(-1, 2)
            ax[i].set_xticklabels(['in', 'out'],  rotation = 45, fontdict=self.label_font)
            ax[i].set_ylabel(params[param], fontdict=self.label_font)
            ax[i].set_xlabel('')
            if i==1: #specific to cluster vis
                ax[i].plot([-1, 2], [0, 0], color='k', linestyle='--', alpha=0.5)
            
            sns.despine(right=True, top=True, ax=ax[i])
            plt.tight_layout()

        return ax
    

     '''
    

    def visualize_ts(self, anim, strt, fini, cut, fps, treat): #db > after get_anim

        _, ax = plt.subplots(4)
        ar=anim.main_ar()[:cut]
        head_ang=anim.mid_head_angs()[:cut]
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

    

