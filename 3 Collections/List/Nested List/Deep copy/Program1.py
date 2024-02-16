#Deep Copy - it will be work on both i.e nested or normal list
#jya list madhe change kela aahe tyach list madhe change hoto
#inport in compulsory

import copy as cp
lang=["CPP","Java", "Python",["Go","Rust", "Dart"]]
new_list=cp.deepcopy(lang)

print(lang)
print(new_list)

lang[3][1]="JavaScript"

print(lang)
print(new_list)