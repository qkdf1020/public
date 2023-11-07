# python 3.10.9 버전에서 실행 하였습니다.

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


def job_1(num_A, num_B) :
  df = pd.read_csv('./data/pokemon.csv')

  features = []
  img_paths = []

  img_dir = './data/images/'
  
  p_name_1 = df.loc[num_A].tolist()[0]
  p_name_2 = df.loc[num_B].tolist()[0]

  for i in (p_name_1, p_name_2) :
    try :
      image_path = img_dir + str(i)+ ".png"
      img_paths.append(image_path)

      # Extract Features
      feature = get_extract(images = Image.open(image_path))
      features.append(feature)

    except :
      image_path = img_dir + str(i) + ".jpg"
      img_paths.append(image_path)
      image_path_r = img_dir + str(i) + ".png"
      img_paths.remove(image_path_r)

      # Extract Features50
      feature = get_extract(images = Image.open(image_path))
      features.append(feature)

  print('img_paths :', len(img_paths))
  print('features :', len(features))

  Pokemon_names = [path.split('/')[-1] for path in img_paths]
  Pokemon_names = [path.split('.')[0] for path in Pokemon_names]

  print('Pokemon_names :', len(Pokemon_names))
 
  print(f'{num_A}번 포켓몬과 {num_B}번 포켓몬의 유사도는 :', dot(features[0], features[1]) / (norm(features[0]) * norm(features[1])), '이고,')
  print(f"{num_A}번 포켓몬의 이름은 : '{Pokemon_names[0]}'이고,")
  print(f"{num_B}번 포켓몬의 이름은 : '{Pokemon_names[1]}'입니다.")


def job_2(name_A, name_B) :
  df = pd.read_csv('./data/pokemon.csv').reset_index()

  features = []
  img_paths = []

  img_dir = './data/images/'
  

  for i in (name_A, name_B) :
    try :
      image_path = img_dir + str(i)+ ".png"
      img_paths.append(image_path)

      # Extract Features
      feature = get_extract(images = Image.open(image_path))
      features.append(feature)

    except :
      image_path = img_dir + str(i) + ".jpg"
      img_paths.append(image_path)
      image_path_r = img_dir + str(i) + ".png"
      img_paths.remove(image_path_r)

      # Extract Features
      feature = get_extract(images = Image.open(image_path))
      features.append(feature)

  print('img_paths :', len(img_paths))
  print('features :', len(features))

  Pokemon_names = [path.split('/')[-1] for path in img_paths]
  Pokemon_names = [path.split('.')[0] for path in Pokemon_names]

  print('Pokemon_names :', len(Pokemon_names))

  Pokemon = pd.DataFrame(Pokemon_names).reset_index()
  Pokemon = Pokemon.rename(columns = {0 : 'Name', 'index' : 'id'})
  Pokemon = Pokemon[['Name', 'id']]

  num_A = Pokemon.index[Pokemon['Name'] == name_A].tolist()[0]
  num_B = Pokemon.index[Pokemon['Name'] == name_B].tolist()[0]
  
  print(f"'{name_A}' 포켓몬과 '{name_B}' 포켓몬의 유사도는 :",
        dot(features[num_A], features[num_B]) / (norm(features[num_A]) * norm(features[num_B])),'입니다.')


def job_3(Pokemon) :
  df = pd.read_csv('./data/pokemon.csv')

  features = []
  img_paths = []

  img_dir = './data/images/'

  for i in df['Name'] :
    try :
      image_path = img_dir + str(i) + ".png"
      img_paths.append(image_path)

      # Extract Features
      feature = get_extract(images = Image.open(image_path))
      features.append(feature)

    except :
      image_path = img_dir + str(i) + ".jpg"
      img_paths.append(image_path)
      image_path_r = img_dir + str(i) + ".png"
      img_paths.remove(image_path_r)

      # Extract Features
      feature = get_extract(images = Image.open(image_path))
      features.append(feature)

  print('img_paths :', len(img_paths))
  print('features :', len(features))

  Pokemon_names = [path.split('/')[-1] for path in img_paths]
  Pokemon_names = [path.split('.')[0] for path in Pokemon_names]

  print('Pokemon_names :', len(Pokemon_names))
  
  # Insert the image query
 
  try :
      img = Image.open(img_dir + Pokemon + '.png')
  except :
      img = Image.open(img_dir + Pokemon + '.jpg')

  # Extract its features

  query = get_extract(img)

  # Calculate the similarity (distance) between images
  dists = np.linalg.norm(features - query, axis = 1)

  # Extract 30 images that have lowest distance
  ids = np.argsort(dists)[: 30]

  scores = [(dists[id], img_paths[id], id) for id in ids]
  # Visualize the result

  axes = []
  fig = plt.figure(figsize = (8, 8))
  for a in range(5 * 6) :
      score = scores[a]
      axes.append(fig.add_subplot(5, 6, a + 1))
      subplot_title = str(round(score[0], 2)) + "/m" + str(score[2])
      axes[-1].set_title(subplot_title)  
      plt.axis('off')
      plt.imshow(Image.open(score[1]))
  fig.tight_layout()
  plt.show()