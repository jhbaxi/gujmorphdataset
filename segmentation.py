import pandas as pd
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import os
import sys
import numpy as np

def split(word): 
    return [char for char in word]
    
def load_segmentation_data():
  pre = os.path.dirname(os.path.realpath(__file__))
  fname = 'seg_input_18_Aug.xlsx'
  path = os.path.join(pre, fname)
  Z = pd.read_excel(path)
  df=pd.read_excel(path,converters={'Label': lambda x: str(x)})
  words=df['Word'].values
  targets=df['Label'].values
  tokenizer = Tokenizer(num_words=200,char_level=True)
  tokenizer.fit_on_texts(words)
  sequences = tokenizer.texts_to_sequences(words)
  X = pad_sequences(sequences, maxlen=18)
  tmplist=[]
  for x in targets:
    tmplist.append(split(x))
  Y=pad_sequences(tmplist,maxlen=18)
  X_train, X_test, y_train, y_test = train_test_split(X, Y,test_size=0.2,random_state=42)
  return X_train, X_test, y_train, y_test