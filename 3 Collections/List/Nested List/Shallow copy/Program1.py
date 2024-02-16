#Shallow Copy
#Shallow copy works on only nested list
#shallow copy change both list element 
#if you change duplicate list he internally change original list

lang=["CPP","Java", "Python",["Go","Rust", "Dart"]]
new_list=lang.copy()

print(lang)
print(new_list)

lang[3][1]="Javascript"
print(lang) #it change rust to javascript
print(new_list) # it will also change by javasript