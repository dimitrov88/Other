student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    # print(index)
    # print(row)
    #Access row.student or row.score
    # print(row.student)
    # print(row.score)


# Keyword Method with iterrows()
df = pandas.read_csv("nato_phonetic_alphabet.csv")
# for (k, v) in df.items():
    # print(k)
    # print(v)

#TODO 1. Create a dictionary in this format:
new_dict = {row.letter: row.code for (index, row) in df.iterrows()}
# print(new_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_line = input("Enter a word: ").upper()

result = [new_dict[val] for val in input_line]

print(result)