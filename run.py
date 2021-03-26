from scipy.spatial.distance import cosine
import numpy as np
import cv2
import mtcnn
from keras.models import load_model
from utils import get_face, plt_show, get_encode, load_pickle, l2_normalizer
import shutil
import os 

encoder_model = 'model/facenet_keras.h5'
people_dir = 'data/train'
encodings_path = 'encodings/encodings.pkl'

in_dir = 'INPUT/'
out_dir = 'OUTPUT/'
recognition_t = 0.3
required_size = (160, 160)

encoding_dict = load_pickle(encodings_path)
face_detector = mtcnn.MTCNN()
face_encoder = load_model(encoder_model)


for im in os.listdir(in_dir):
    img = cv2.imread(in_dir+im)
    # plt_show(img)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_detector.detect_faces(img_rgb)
    for res in results:
        face, pt_1, pt_2 = get_face(img_rgb, res['box'])
        encode = get_encode(face_encoder, face, required_size)
        encode = l2_normalizer.transform(np.expand_dims(encode, axis=0))[0]

        name = 'unknown'
        distance = float("inf")

        for db_name, db_encode in encoding_dict.items():
            dist = cosine(db_encode, encode)
            if dist < recognition_t and dist < distance:
                name = db_name
                distance = dist
        print(in_dir+im+' Copying to:'+name)

        shutil.copy(in_dir+im,out_dir+name+'/'+im)

