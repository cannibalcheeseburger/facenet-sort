import os
import shutil
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.models import load_model

labels = ['Ben_Affleck','Elton_John','Jerry_Seinfeld','Madonna','Mindy_Kaling']

out_path = 'OUTPUT'
in_path = 'INPUT'


file_list= os.listdir(in_path)
#for label in labels :
 #   os.makedirs(os.path.join(out_path,label))

model = load_model('./new_model/model.h5')
model.load_weights('./new_model/model_weights.h5')
# Insert model and make classifier
predictions = []
for fil in file_list:
    test_image = image.load_img(os.path.join(in_path,fil), target_size = (160, 160))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    predictions.append(np.argmax(model.predict(test_image)))
print(predictions)
# copies files to folders based on classifier
for i in range(0,len(file_list)):
    shutil.copy(os.path.join(in_path,file_list[i]),os.path.join(os.path.join(out_path,labels[predictions[i]]),file_list[i]))