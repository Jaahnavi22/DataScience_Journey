#Python provides a Built-in-module called Keywords.
import keyword
print(keyword.kwlist) #Display all the keywords.
print(len(keyword.kwlist)) #Count total keywords.
#Check whether the word is keyword or not.
print(keyword.iskeyword("if"))
print(keyword.iskeyword("Student"))