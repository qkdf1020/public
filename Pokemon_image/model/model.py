import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model

from PIL import Image

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy import dot
from numpy.linalg import norm



base_model = VGG16(weights = 'imagenet')
model = Model(inputs = base_model.input, outputs = base_model.get_layer('fc1').output)


def get_extract(images):
    images = images.resize((224, 224))
    images = images.convert('RGB')

    x = image.img_to_array(images)
    x = np.expand_dims(x, axis = 0)
    x = preprocess_input(x)
    feature = model.predict(x)[0]

    return feature / norm(feature)


def twe(num_A, num_B) :
  df = pd.read_csv('C:/Users/qkdf1/Documents/public/Pokemon_image/data/pokemon.csv').reset_index()

  features = []
  img_paths = []

  cur_dir = 'C:/Users/qkdf1/Documents/public/Pokemon_image/data/images/'
  
  p_name_1 = df.loc[num_A].tolist()[1]
  p_name_2 = df.loc[num_A].tolist()[1]

  for i in (p_name_1, p_name_2) :
    try :
      image_path = cur_dir + str(i)+ ".png"
      img_paths.append(image_path)

      # Extract Features
      feature = get_extract(images = Image.open(image_path))
      features.append(feature)

    except :
      image_path = cur_dir + str(i) + ".jpg"
      img_paths.append(image_path)
      image_path_r = cur_dir + str(i) + ".png"
      img_paths.remove(image_path_r)

      # Extract Features
      feature = get_extract(images = Image.open(image_path))
      features.append(feature)

  print('img_paths :', len(img_paths))
  print('features :', len(features))

  Pokemon_names = [path.split('/')[-1] for path in img_paths]
  Pokemon_names = [path.split('.')[0] for path in Pokemon_names]

  print('Pokemon_names :', len(Pokemon_names))


def all() :
  df = pd.read_csv('C:/Users/qkdf1/Documents/public/Pokemon_image/data/pokemon.csv')

  features = []
  img_paths = []

  cur_dir = 'C:/Users/qkdf1/Documents/public/Pokemon_image/data/images/'

  for i in df['Name'] :
    try :
      image_path = cur_dir + str(i) + ".png"
      img_paths.append(image_path)

      # Extract Features
      feature = get_extract(images = Image.open(image_path))
      features.append(feature)

    except :
      image_path = cur_dir + str(i) + ".jpg"
      img_paths.append(image_path)
      image_path_r = cur_dir + str(i) + ".png"
      img_paths.remove(image_path_r)

      # Extract Features
      feature = get_extract(images = Image.open(image_path))
      features.append(feature)

  print('img_paths :', len(img_paths))
  print('features :', len(features))

  Pokemon_names = [path.split('/')[-1] for path in img_paths]
  Pokemon_names = [path.split('.')[0] for path in Pokemon_names]

  print('Pokemon_names :', len(Pokemon_names))


def Pokemon(name):
  Pokemon = pd.DataFrame(Pokemon_names).reset_index()
  Pokemon = Pokemon.rename(columns = {0 : 'Name', 'index' : 'id'})
  Pokemon = Pokemon[['Name', 'id']]
  return Pokemon.index[df['Name'] == name].tolist()[0]


def features_find_num(num_A : int, num_B : int) :
    print(f'{num_A}번 포켓몬과 {num_B}번 포켓몬의 유사도는 :', dot(features[num_A], features[num_B]) / (norm(features[num_A]) * norm(features[num_B])), '이고,')
    print(f"{num_A}번 포켓몬의 이름은 : '{Pokemon_names[num_A]}'이고,")
    print(f"{num_B}번 포켓몬의 이름은 : '{Pokemon_names[num_B]}'입니다.")
    
    
def features_find_name(num_A : int, num_B : int, name_A : str, name_B : str) :
    print(f"'{name_A}' 포켓몬과 '{name_B}' 포켓몬의 유사도는 :", dot(features[num_A], features[num_B]) / (norm(features[num_A]) * norm(features[num_B])),'입니다.')
    
    
