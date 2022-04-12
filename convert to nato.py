# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
# Access index and row
# Access row.student or row.score

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Create a dictionary in this format:
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic)


# Create a list of the phonetic code words from a word that the user inputs.
def generate_nato():
    word = input("Enter a word: ").upper()
    try:
        output = [phonetic[letter] for letter in word]
    except KeyError:
        print("sorry only letter from nato alphabet")
        generate_nato()
    else:
        print(output)


generate_nato()
