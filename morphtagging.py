import os
import sys
import numpy as np
import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split

def prepare_noun_tagging_data():
  df=pd.read_excel('/content/drive/MyDrive/PHD/data/input_n_mcml.xlsx')
  words=df['Word'].values
  labels_case = ["case_nominative", "case_genitive","case_locative","case_ergative","case_dative","case_ablative"]
  labels_gender = ["gender_male", "gender_female","gender_neutral"]
  labels_number = ["number_singular", "number_plural"]
  targets_case = df[labels_case].values
  targets_gender = df[labels_gender].values
  targets_number = df[labels_number].values
  tokenizer = Tokenizer(num_words=200,char_level=True)
  tokenizer.fit_on_texts(words)
  sequences = tokenizer.texts_to_sequences(words)
  print(tokenizer.word_index)
  X= pad_sequences(sequences, maxlen=20)
  #Gender
  X_train, X_test, y_train_gender, y_test_gender = train_test_split(X, targets_gender,test_size=0.20,random_state=42)
  #Number
  X_train, X_test, y_train_number, y_test_number = train_test_split(X, targets_number,test_size=0.20,random_state=42)
  #Case
  X_train, X_test, y_train_case, y_test_case = train_test_split(X, targets_case,test_size=0.20,random_state=42)
  return X_train,X_test,y_train_gender, y_train_number, y_train_case,y_test_gender,y_test_number,y_test_case
  
def prepare_verb_tagging_data():
  df=pd.read_excel('/content/drive/MyDrive/PHD/data/verb_onehot.xlsx')
  words=df['Verb Form'].values
  labels_person = ["person_1", "person_2","person_3","person_4"]
  labels_gender = ["gender_1", "gender_2","gender_3","gender_4"]
  labels_tense = ["tense_1", "tense_2","tense_3","tense_4"]
  labels_aspect = ["aspect_1", "aspect_2","aspect_3","aspect_4","aspect_5"]
  labels_number=["number_1","number_2","number_3"]
  targets_person = df[labels_person].values
  targets_gender = df[labels_gender].values
  targets_tense=df[labels_tense].values
  targets_aspect=df[labels_aspect].values
  targets_number = df[labels_number].values
  tokenizer = Tokenizer(num_words=200,char_level=True)
  tokenizer.fit_on_texts(words)
  sequences = tokenizer.texts_to_sequences(words)
  print(tokenizer.word_index)
  X= pad_sequences(sequences, maxlen=20)
  #Person
  X_train, X_test, y_train_person, y_test_person = train_test_split(X, targets_person,test_size=0.20,random_state=42)
  #Gender
  X_train, X_test, y_train_gender, y_test_gender = train_test_split(X, targets_gender,test_size=0.20,random_state=42)
  #Tense
  X_train, X_test, y_train_tense, y_test_tense = train_test_split(X, targets_tense,test_size=0.20,random_state=42)
  #Aspect
  X_train, X_test, y_train_aspect, y_test_aspect = train_test_split(X, targets_aspect,test_size=0.20,random_state=42)
  #Number
  X_train, X_test, y_train_number, y_test_number = train_test_split(X, targets_number,test_size=0.20,random_state=42)
  return X_train, X_test,y_train_person,y_train_gender,y_train_tense, y_train_aspect, y_train_number,y_test_person,y_test_gender,y_test_tense,y_test_aspect,y_test_number
  
def prepare_adjective_tagging_data():
  df=pd.read_excel('/content/drive/MyDrive/PHD/data/master_data_adjective_3347.xls')
  words=df['Word'].values
  labels_type = ["type_1", "type_2"]
  labels_gender = ["gender_1", "gender_2","gender_3","gender_4"]
  labels_number=["number_1","number_2","number_3"]
  targets_type = df[labels_type].values
  targets_gender = df[labels_gender].values
  targets_number = df[labels_number].values
  tokenizer = Tokenizer(num_words=200,char_level=True)
  tokenizer.fit_on_texts(words)
  sequences = tokenizer.texts_to_sequences(words)
  print(tokenizer.word_index)
  X= pad_sequences(sequences, maxlen=20)
  #Type
  X_train, X_test, y_train_type, y_test_type = train_test_split(X, targets_type,test_size=0.20,random_state=42)
  #Gender
  X_train, X_test, y_train_gender, y_test_gender = train_test_split(X, targets_gender,test_size=0.20,random_state=42)
  #Number
  X_train, X_test, y_train_number, y_test_number = train_test_split(X, targets_number,test_size=0.20,random_state=42)
  return X_train, X_test, y_train_type, y_train_gender, y_train_number, y_test_type, y_test_gender, y_test_number