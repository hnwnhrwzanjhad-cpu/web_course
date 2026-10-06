###################  set A:Reverse Countdown list ##################
def countdown(i):
    list=[]
    for x in range(i,-1,-1):              #Task 1
        list.append(x)
    print (list)

countdown(5)

                  ###############################################################
def print_and_return(i):
    print(i[0])
    return(i[len(i)-1])                    #Task 2

print(print_and_return([1,2]))
                  ################################################################
def first_plus_length(i):
    total=i[0]+len(i)
    return total                           #Task 3

print(first_plus_length([1,2,3,4,5]))
                  #################################################################
def values_greater_than_second(lst):
    My_list=[x for x in lst if x >lst[1]]
    print(len(My_list))                    #Task 4
    return My_list
print(values_greater_than_second([5,2,3,2,1,4]))
                  ##################################################################
def length_and_value(len,value):
    return [value]*len                      #Task 5
print(length_and_value(4,7))


############################### Set B: List Manipulation###############################
def Biggie_Size(num):
        if num > 0:
             return "Big"
        else:                              #Task 1
             return num            
print(Biggie_Size(10))
print(Biggie_Size(-50))
                        ##################################################
def count_positive(num):
    total=0
    for i in range(len(num)):
        if num[i]>0:
              total+=num[i]             #Task 2
    num[len(num)-1]=total
    return num

print(count_positive([0,1,2,3,4,5,6,7,8]))
                        ###################################################
def sum_total(num):
    sum=0
    for i in range(len(num)):
          sum+=i                    #Task3
    return sum

print(sum_total([0,1,2,3,4,5,6,7,8]))
                         ####################################################
def Average(num):
    sum=0
    for i in range(len(num)):
        sum+=i                         #Task 4
    Average = sum /len(num)
    return Average
print(Average([0,1,2,3,4,5,6,7,8]))
                         ######################################################
def minimum(num):
    if num==[]:
         return False
    else:
         return min(num)                #Task 5
print(minimum([7,49,5,37,29,9]))
print(minimum([]))
########################### Set C: Python tricks & Sequences operations ##########################
def Greet(name="Guest",time_of_day="day"):
     print (time_of_day,name)               #Task 1
Greet(time_of_day="Good morning",name="nesma")

                            #################################################

def Grade_Check(score):
    return "pass" if score>=60  else  "failled"   #Task 2

print(Grade_Check(85))
                           ###################################################
fruits=["apple" ,"banana" ,"cherry"]
fruits[0],fruits[2]= fruits[2],fruits[0]    #Task 3
print(fruits)
                            ######################################################
string="coding is fun"
print(string[:6])
print(string[10:])                #Task 4
print(string[::-1]) 
                            #######################################################      
Data=[42,10,77,2,15]   
print(max(Data))                   #Task 5
print(sum(Data))
print(sorted(Data))
                            ########################################################


 
