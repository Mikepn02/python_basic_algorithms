# fruit='banana';

# # print(len(fruit))

# for letter in fruit:
#     count =0
#     if letter == 'a':
#         count = count + 1
#         print(count)
# s= 'From stephen.maruard@uct.ac.zaSat Jan 5 09:14:16 2008'
# year = s.find('2008')
# print(s[13:33] , s[49:54])


# name = 'peter'
# reversed_string = ""

# for char in name:
#     reversed_string = char + reversed_string

# print(reversed_string)

# word= "anna has two bananas"
# count= {}
# for letter in word:
#     if letter in count:
#         count[letter] = count[letter] + 1
#     else:
#         count[letter] = 1
# print (count.get('z','wayobye brooo'))


# counts = {'Gloria' : 84,'jackson': 100,'shema':98}
# lst = list(counts.keys())
# print(lst)
# lst.sort()
# for key in lst:
#     print(counts,counts[key])


# def print_list_integers(int_list):
#     reversed_list=  int_list[::-1]
#     for number in reversed_list:
#      print (number)

# my_array = [2,4,54,23,522,43245,62]
# print(print_list_integers(my_array))

#simple dictionary

# def update_dictionary(a_dictionary,key,value):
# gender = {"Hirwa": "Male","Keza":"Female","shema":"Male"}
# newGender = {"Brian" : "Male"}

# for i,val in enumerate(newGender):
#         gender[i] = val

#         print(gender)



# def update_dictionary(a_dictionary, key, value):
#     newGender = {key: value}
#     a_dictionary.update(newGender)
#     print(a_dictionary)

# gender = {"Hirwa": "Male", "Keza": "Female", "shema": "Male"}
# update_dictionary(gender, "Brian", "Male")

greet=open('greet.text')
count=0
for lines in greet:
    line = lines.rstrip()
    # if line.startswith('where'):
    print(line)