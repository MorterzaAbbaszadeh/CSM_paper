
# %%
#imports and instansiations

#local
from include_package import Welcome_party
Welcome_party().initialize()
from hmm_access import machine_access
from acss_data_base import data_access
from kinematics import dlc_kinematics
from iteration import dlc_iter
import single_ts as ts


from visualization_config_videos import visual_config
import cv2
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from celluloid import Camera
from PIL import Image


import warnings
warnings.simplefilter('ignore', category=DeprecationWarning)

filename = "/home/morteza/dlc_projects/Analysis/Currencodes/csm/videos/stock/D2A275052.mp4"
animal_ID = 1
time_point = 50
strt = 3500
n_frames = 1000
fps = 110
# initiate modules

fetch = ts.dlc_ts()
kin = dlc_kinematics()
iter = dlc_iter()
machine = machine_access()
model_d1 = machine.get_hmm_d1()
model_d2 = machine.get_hmm_d2()
vs_vd = visual_config()
data_base = data_access()
evalu = ['D2A']  # evaluate treatment group LID
dct = data_base.get_dct(evalu)

cap = cv2.VideoCapture(filename)
cap.set(1, strt)


fig = plt.figure(figsize=(10,6))

spec2 = gridspec.GridSpec(ncols=5, nrows=5, figure=fig)
camera = Camera(fig)


i = 0
while i < n_frames:  # video frame by frame

    _, frame = cap.read()
    cv2_im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_fig = Image.fromarray(frame)
    ax_im = fig.add_axes([0, 0, 1, 1])
    ax_im.imshow(frame, aspect='equal')
    ax_im.axis('off')

    cut = i+strt
    strt_t =strt/fps
    fini_t=strt_t+(i/fps)+2
    ax0 = fig.add_axes([0.55, 0.1, 0.5, 0.1])
    ax1 = fig.add_axes([0.55, 0.4, 0.5, 0.1])
    [ax0, ax1] = vs_vd.visualize_ts_state_d1([ax0, ax1], dct,  animal_ID, time_point,
                                             strt_t, fini_t, fetch, model_d1, cut, fps)

    i = i+1
    print(i)
    
    camera.snap()


animation = camera.animate()
animation.save('annotation3.mp4', fps=20, dpi=360)
