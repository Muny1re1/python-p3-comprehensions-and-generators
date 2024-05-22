def return_evens(num_list):
    even = [n for n in num_list if (n % 2) == 0]
    print(even)
    return even

def make_exclamation(sentence_list):
    exclamation_list = [sentence + '!' for sentence in sentence_list]
    print(exclamation_list)
    return exclamation_list