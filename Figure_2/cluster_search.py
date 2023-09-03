
#%% initialize

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#local
from include_package import Welcome_party
Welcome_party().initialize()

#%%

from dlc_iteration import dlc_db
from fig_1_visualization_config import visual_config

vis_config=visual_config()
targs=['LID']
db=dlc_db()
db.select_treatment(targets=targs)
print(db.keys)
db.get_animal(db.keys[2], '30')

ax=vis_config.visualize_ts(db, 10, 30, 7000, 50, 'LD-3mg')