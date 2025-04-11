import os
import glob
import sd 
from sd.tools import export
from sd.api.sdvaluefloat import SDValueFloat
from sd.api.sdproperty import SDPropertyCategory

# variables and paths
input_value = 0
min_value = 0
max_value = 1
difference = max_value-min_value
frames = 30
step = difference/frames
id = 'pan'
'''THIS WILL BE A LOCAL FILE PATH - BE AWARE OF OS'''
folder_path = '/Users/vn57u66/Documents/Adobe/Adobe Substance 3D Designer/Animations_Automation_Batch_Export/output'
file_name = 'SD_Anim_Frame'
file_type = '/*.png'

# Getting the graph
sd_context = sd.getContext()
sd_application = sd_context.getSDApplication()
sd_ui_mgr = sd_application.getUIMgr()
graph = sd_ui_mgr.getCurrentGraph()

#Getting the Properties
category = SDPropertyCategory.Input
label_property = graph.getPropertyFromId(id, category)

# Batch Exporter
for frame in range(frames):
    
    export.exportSDGraphOutputs(graph, folder_path, '{}.png'.format(str(frame)))

    input_value = round((input_value + step), 5)

    graph.setPropertyValue(label_property, SDValueFloat.sNew(input_value))

    files = glob.glob(folder_path + file_type) 
    if files:
        newest_file = max(files, key = os.path.getctime)
        new_name = '{0}_{1}.png'.format(file_name, str(frame))
        os.rename(newest_file, os.path.join(folder_path, new_name))
        print('frame {} exported'.format(str(frame)))
    else:
        print('No files found to rename for frame {}'.format(str(frame)))