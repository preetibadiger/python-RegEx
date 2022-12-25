#### Regular Expression  ####

import re
txt = "A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern."
x = re.search("^A.*pattern.$", txt)

if x:
  print("YES! We have a match the string in 'txts' !")
else:
  print("No match of string in 'txt' ")
  
  #RegEx Functions

 #findall() Function

txt2="black, blue and brown"
x=re.findall("bl",txt2)

print(x)

txt3="bachelors of computer applicaion"
x=re.findall("science", txt3)
print(x)

if (x):
    print("Yes there is at least one match")
else:
    print("No Match")


  #search() Function

txt4 = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 

 # split() Function
  
txt5 = "The split() function returns a list where the string has been split at each match"
x = re.split("\s", txt5)
print(x)
            
 # sub() Function

txt6 = "The sub() function replaces the matches with the text of your choice"
x = re.sub("\s", "5", txt6)
print(x)
