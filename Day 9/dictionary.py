programming_dictionary = {
 "Bug": "An error in a program that prevents a program from running.",
 "Function":"A piece of code that you can easily call over and over again"
 }


#print(programming_dictionary["Bug"])

#Adding new items to the dictionary
programming_dictionary["Loop"]= "The action of doing something again and again "
#print(programming_dictionary)

#creating new empty dictionary
empty_dictionary = {}

#wiping the contents of dictionary
#programming_dictionary = {}
#print(programming_dictionary)

#edit an item in dictionary
programming_dictionary["Bug"] = "A moth in a program."
##print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])