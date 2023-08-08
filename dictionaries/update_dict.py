def update_dictionary(a_dictionary, key, value):
    newGender = {key: value}
    a_dictionary.update(newGender)
    print(a_dictionary)

gender = {"Hirwa": "Male", "Keza": "Female", "shema": "Male"}
update_dictionary(gender, "Brian", "Male")