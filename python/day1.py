# # # # # print("hello world")
# # # # # name1="hello world"
# # # # # name2='hello world'# for string
# # # # # name3="""hello world"""#used for paragraph
# # # # # rupee= 2000
# # # # # print("i have " ,rupee ,"rupees")
# college= "      Raffles university neemrana    "
# # # # # print(college.lower())
# # # # # print(college.upper())
# # # # # print(len(college))
# # # # # print(college.count("f"))
# # # # # print(college.endswith('a'))
# # # # # a ='hello world'
# # # # # print(a.replace('h','j'))
# # # # # print(a.split('o'))
# print(college.strip())
# print(college.lstrip())
# print(college.rstrip())


# # # # # #indexing
# # # # # #o to 9
# # # # # #from back numbering is from -1 To -infinity
# # # # # print(college[0:4:2]) #start:end:skip
# print(college[:-6])
# # # # # print("'hello world'")
# # # # # x= "hello"
# # # # # y="world"
# # # # # c= x + y
# # # # # print(c)
# # # # # c= x+" "+y
# # # # # print(c)
# # # # # c= x + "*" +y 
# # # # # print(c)
# age =100
# text = "my name is x and i am " +age  
# print(text)
# text =f"my name is x i am  {age}"
# print(text)
# txt="we study in \"the\"  \"upflaire\" now"
# print(txt)
# ...........................................................
# _____________________________LIST___________________________
# .....................................................................
# /////////////////////////////////////////...
# # # # # tropical=["mango","pineapple"]
# mylist =["apple","Aac","Mango",'hello']
# # # # # print(mylist)
# # # # # print(type(mylist))
# # # # # print(len(mylist))
# # # # # print(mylist[1:3])
# # # # # mylist[2]='hi'
# # # # # print(mylist)
# # # # # mylist[0:1]=["a","namaste"]
# # # # # print(mylist)
# # # # # mylist[1:2]=["banana","cherry"]
# # # # # print(mylist)
# # # # # mylist[0:3]=["mangon"]
# # # # print(mylist)
# .......................................................
# _________________________________insert_________________
# .......................................................
# # # # # mylist.insert(2,"watemaleon")
# # # # # print(mylist)
# mylist.append("kiwi")
# # # # # tropical=["mango","pineapple"]
# # # # # mylist.extend(tropical)
# # # # # mylist.remove("mango")
# # # # # mylist.pop()# delete the last pop doent take any argument
# # # # # mylist.clear()
# mylist.sort()# sort in ascending order
# print(mylist)
# # # # # mylist.sort(reverse=True)# descending order
# # # # # mylist.sort()
# # # # # print(mylist)
# mylist.sort(key=str.lower)#aac kko pehle convert karega lower mein fir solver karega lower mein hi the original value show karega
# print(mylist)
# # # # # mylist.reverse()
# # # # # list1=["a","b","c"]
# # # # # list2=[1,2,3]
# # # # # list3 =list1+list2
# # # # # list1.extend(list2)

# # # # # print(list1)
# # # # # print(list3)
# print(mylist)
# ......................................................................
# ___________________________________tuple_______________________________
# ......................................................................
# # # # tuple is unchangable ,can contain duplicates and    
# # # # mytuple=("hello","mango","bana");
# # # # print(mytuple)
# # # # print(type(mytuple))
# # # # print(len(mytuple))
# # # # tp=("hello",)#single value can't be a tuple we must add comma for making it into tuple
# # # # tp= ("hello","hi","kolam",1)
# # # # tp=tuple(("hi","bye","hello"))
# # # x=("hello","hi","bankai")

# # # y =list(x)
# # # y.append("vroom")
# # # y[1]="ohio"
# # # x= tuple(y)
# # # print(x)
# # # # print(tp)
# # # # print(len(tp))
# # # # print(type(tp))

# # # a=("hi ","mango","baby")
# # # b=("ji",)
# # # a +=b
# # # print(a)
# .........................................................................................................
# ________________________________________________remove function___________________________________________
# ...........................................................................................................
# # #delete tuple
# # a=("hi")
# # del a
# # print(a)
# .......................................................................................................
# # ____________________________________multiply__________________________________________________________
# ........................................................................................................
# fruit =("mango",)
# mytuple=fruit*2
# print(mytuple)
# ...............................................................
# ________________________________dictionary_____________________
# ...............................................................
# dictionary is changable ,can contains duplicates and  
# dct={
#     "name":"tanmay",
#     "branch":"btech cse",
# # "year":"2",iski value overwrite hojayegi
# "year": 3
# }
# print(dct)
# print(type(dct))
# print(len(dct))
# thisdict =dict(name="tanmay",classs=1,year="2024")
# print(thisdict)
# print(type(thisdict))
# print(len(thisdict))
# car={
#     "brand":"ford",
#     "model":"mustang",
#     "year": 1996

# }
# x =car.keys()
# print(x) #before the change
# car["color"]="white"
# print(x) #after the change
# # x=thisdict["model"]
# # x=thisdict.get("model")
# # x=thisdict.keys()
# # print(x)
# y =car.values()
# print(y)
# x=car.values()
# print(x)
# car["model"]="bmw"
# print(x)

# x=car.items()
# print(x)
# car.update({"brand": "mahindra"})
# car.pop("model")
# del car["year"]
# car.clear()
# print(car)
# .........................................................................................
# ______________________________________SET________________________________________________
# .........................................................................................
# set is unchangable,contains no duplicates  
# set ={"hello","bankai","hard"}
# print(type(set))
# print(len(set))
# print(set)
# thisset =set(("hello",))
# set2 ={"thus","this","h"}
# set3=thisset+set2# set + set shows error.....................................
# print(set3)
# # thisset.update(set2)
# thisset.add(1)
# print(thisset)
# print(len(thisset))
# print(type(thisset))
# set1={"python","code"}
# set2={1,2,3}
# result=set1.union(set2)
# print(result)
# result =set1.intersection(set2)
# print(result)
# result=set1|set2
# __________________________________________________________________________________________
# ..........The | operator for sets in Python performs a union but 
#.............. does not automatically sort the elements. It combines the elements from both sets, 
# ............but the order of elements in a set is not guaranteed. Sets in 
# ..............Python are inherently unordered collections.
# ____________________________________________________________.
# print(result)

# # set1.remove("python")
# set1.pop()
# print(set1)
