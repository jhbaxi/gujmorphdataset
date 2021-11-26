

Package Name : Segmentation

Methods :

- load_segmentation_data()

Description : This method will read the excel file which contains list of inflected words along with their root word encoding. The encoding is in binary format in which character '1' indictes morpheme segmentation boundary.
Character based tokenization is applied and each word is converted into sequence of integers where each integer represents one character. The root word encoding part is considered as labels for the classification problem. 
Dataset is splitted for training and testing in 80:20 ratio and the corresponding lists are returned.

Below lists are returned by the function :

The function returns 4 lists :
 
1. X_train - The data for training a model. Shape - ( # of words in training set, maximum possible wordlength)
2. y_train - The labels for training a model. - ( # of words in training set, maximum possible wordlength)
3. X_test - The data for testing a model. - ( # of words in test set, maximum possible wordlength)
4. y_test - The labels for testing a model. - ( # of words in test set, maximum possible wordlength)


Package Name : morphtagging

For all the methods in this package, first the data file is loaded which contains inflected word along with the binary encoded labels. For noun, verb and adjective, different methods are provided to prepare the tagging dataset.

Methods :

- prepare_noun_tagging_data 

Description :For noun category, there are 3 features. Gender, number and case. Labels are created as per the possible values each feature can take. The details of the classification labels are as below :

Gender : 3 labels - gender_male, gender_female and gender_neutral

Number : 2 labels - number_singular and number_plural

Case : 6 labels - case_nominative, case_genitive, case_locative, case_ergative, case_dative and case_ablative


The character based tokenizer is applied to convert a word into sequence of characters. Dataset is splitted for training and testing in 80:20 ratio and the corresponding lists are returned.

Below lists are returned by the function :

1. X_train - Training data for common for all the features - Shape - ( # of words in training set, maximum possible wordlength)  
2. X_test - Testing data for common for all the features - Shape - ( # of words in test set, maximum possible wordlength)  
3. y_train_gender - Labels for training gender classifier - Shape - ( # of words in training set, 3)  
4. y_train_number - Labels for training number classifier - Shape - ( # of words in training set, 2)  
5. y_train_case - Labels for training case classifier - Shape - ( # of words in training set, 6)  
6. y_test_gender - Labels for testing gender classifier - Shape - ( # of words in testing set, 3)  
7. y_test_number - Labels for testing number classifier - Shape - ( # of words in testing set, 2)  
8. y_test_case - Labels for testing case classifier - Shape - ( # of words in testing set, 6)  


- prepare_verb_tagging_data : For verb category, there are 5 features. Person, gender, tense, aspect and number. Labels are created as per the possible values each feature can take. The details of the classification labels are as below :
Person : 4 labels ( person_1, person_2, person_3, person_4)

Gender : 4 labels ( gender_1, gender_2, gender_3, gender_4)

Tense : 4 labels ( tense_1, tense_2, tense_3, tense_4)

Aspect : 5 labels ( aspect_1,aspect_2,aspect_3,aspect_4,aspect_5)

Number : 3 labels ( number_1, number_2, number_3)

The character based tokenizer is applied to convert a word into sequence of characters. Dataset is splitted for training and testing in 80:20 ratio and the corresponding lists are returned.

Below lists are returned by the function :

1.X_train - Training data for common for all the features - Shape - ( # of words in training set, maximum possible wordlength)</br>
2.X_test - Testing data for common for all the features - Shape - ( # of words in test set, maximum possible wordlength)</br>
3.y_train_person - Labels for training person classifier - Shape - ( # of words in training set, 4)</br>
4.y_train_gender - Labels for training gender classifier - Shape - ( # of words in training set, 4)</br>
5.y_train_tense - Labels for training tense classifier - Shape - ( # of words in training set, 4)</br>
6.y_train_aspect - Labels for training aspect classifier - Shape - ( # of words in training set, 5)</br>
7.y_train_number - Labels for training number classifier - Shape - ( # of words in training set, 3)</br>
8.y_test_person - Labels for testing person classifier - Shape - ( # of words in testing set, 4)</br>
9.y_test_gender - Labels for testing gender classifier - Shape - ( # of words in testing set, 4)</br>
10.y_test_tense  - Labels for testing tense classifier - Shape - ( # of words in testing set, 4)</br>
11.y_test_aspect - Labels for testing aspect classifier - Shape - ( # of words in testing set, 5)</br>
12.y_test_number - Labels for testing number classifier - Shape - ( # of words in testing set, 3)</br>

- prepare_adjective_tagging_data : For adjective category, there are 3 features. Type, gender and number. Labels are created as per the possible values each feature can take. The details of the classification labels are as below :</br>
Type - 2 labels (type_1, type_2)

Gender - 4 labels ( gender_1, gender_2, gender_3, gender_4)

Number - 3 labels ( number_1, number_2, number_3)

The character based tokenizer is applied to convert a word into sequence of characters. Dataset is splitted for training and testing in 80:20 ratio and the corresponding lists are returned.</br>

Below lists are returned by the function :</br>

1.X_train - Training data for common for all the features - Shape - ( # of words in training set, maximum possible wordlength)</br>
2.X_test - Testing data for common for all the features - Shape - ( # of words in test set, maximum possible wordlength)</br>
3.y_train_type - Labels for training type classifier - Shape - ( # of words in training set, 2)</br>
4.y_train_gender - Labels for training gender classifier - Shape - ( # of words in training set, 4)</br>
5.y_train_number - Labels for training number classifier - Shape - ( # of words in training set, 3)</br>
6.y_test_type - Labels for testing type classifier - Shape - ( # of words in training set, 2)</br>
7.y_test_gender - Labels for testing gender classifier - Shape - ( # of words in training set, 4)</br>
8.y_test_number - Labels for testing number classifier - Shape - ( # of words in training set, 3)</br>
