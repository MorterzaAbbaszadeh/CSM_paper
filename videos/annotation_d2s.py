
# %%
#imports and instansiations

import warnings
from PIL import Image
from celluloid import Camera
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import cv2
from visualization_config_videos import visual_config
vs_config=visual_config()

from include_package import Welcome_party
Welcome_party().initialize()


warnings.simplefilter('ignore', category=DeprecationWarning)


from dlc_iteration import dlc_db
n_frames=700
strt=500



targs=['LID']
db=dlc_db()
db.select_treatment(targets=targs)
db.get_animal(db.keys[6], '40')
print(db.keys[2])



video_path='/home/morteza/Desktop/per_cont/LID264042160720.mp4'
cap = cv2.VideoCapture(video_path)
cap.set(1, strt)




# %% phis 3 axes


fig = plt.figure(figsize=(10, 6))
#spec2 = gridspec.GridSpec(ncols=5, nrows=5, figure=fig)
camera = Camera(fig)


i = 0
while i < n_frames:  # video frame by frame

    _, frame = cap.read()
    cv2_im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_fig = Image.fromarray(frame)
    ax_im = fig.add_axes([0, 0, 1, 1])
    ax_im.imshow(frame, aspect='equal')
    ax_im.axis('off')

    
    fini=strt+i

    ax0 = fig.add_axes([0.45, 0.1, 0.3, 0.1])
    ax1 = fig.add_axes([0.45, 0.4, 0.3, 0.1])
    ax2 = fig.add_axes([0.45, 0.7, 0.3, 0.1])
    [ax0, ax1, ax2] = vs_config.visualize_phis([ax0, ax1, ax2], db, strt, fini)
    i = i+1

    camera.snap()


animation = camera.animate()
animation.save('phi_LID_21_40.mp4', fps=10, dpi=360)



# %% ars 3 axes

fig = plt.figure(figsize=(10, 6))
#spec2 = gridspec.GridSpec(ncols=5, nrows=5, figure=fig)
camera = Camera(fig)


i = 0
while i < n_frames:  # video frame by frame

    _, frame = cap.read()
    cv2_im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_fig = Image.fromarray(frame)
    ax_im = fig.add_axes([0, 0, 1, 1])
    ax_im.imshow(frame, aspect='equal')
    ax_im.axis('off')

    
    fini=strt+i

    ax0 = fig.add_axes([0.45, 0.1, 0.3, 0.1])
    ax1 = fig.add_axes([0.45, 0.4, 0.3, 0.1])
    ax2 = fig.add_axes([0.45, 0.7, 0.3, 0.1])
    [ax0, ax1, ax2] = vs_config.visualize_ars([ax0, ax1, ax2], db, strt, fini)
    i = i+1

    camera.snap()


animation = camera.animate()
animation.save('ar_LID_21_40.mp4', fps=10, dpi=360)


# %% Trans


fig = plt.figure(figsize=(10, 6))
#spec2 = gridspec.GridSpec(ncols=5, nrows=5, figure=fig)
camera = Camera(fig)


i = 0
while i < n_frames:  # video frame by frame

    _, frame = cap.read()
    cv2_im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_fig = Image.fromarray(frame)
    ax_im = fig.add_axes([0, 0, 1, 1])
    ax_im.imshow(frame, aspect='equal')
    ax_im.axis('off')

    
    fini=strt+i

    ax0 = fig.add_axes([0.45, 0.1, 0.5, 0.1])
    ax1 = fig.add_axes([0.45, 0.4, 0.5, 0.1])
    [ax0, ax1] = vs_config.visualize_trans([ax0, ax1], db, strt, fini)
    i = i+1

    camera.snap()


animation = camera.animate()
animation.save('Tr_LID_21_40.mp4', fps=10, dpi=360)


# %% Rot speed



fig = plt.figure(figsize=(10, 6))
#spec2 = gridspec.GridSpec(ncols=5, nrows=5, figure=fig)
camera = Camera(fig)


i = 0
while i < n_frames:  # video frame by frame

    _, frame = cap.read()
    cv2_im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_fig = Image.fromarray(frame)
    ax_im = fig.add_axes([0, 0, 1, 1])
    ax_im.imshow(frame, aspect='equal')
    ax_im.axis('off')

    
    fini=strt+i

    ax0 = fig.add_axes([0.45, 0.1, 0.3, 0.1])
    ax1 = fig.add_axes([0.45, 0.4, 0.3, 0.1])
    ax2 = fig.add_axes([0.45, 0.7, 0.3, 0.1])
    [ax0, ax1, ax2] = vs_config.visualize_rot_speed([ax0, ax1, ax2], db, strt, fini)
    i = i+1

    camera.snap()


animation = camera.animate()
animation.save('rot_speed_LID_21_40.mp4', fps=10, dpi=360)


# %%
