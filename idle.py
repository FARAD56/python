# x = 'Alice and bob'
# y = 'bob'
# z = x+y
# print(z)

# name = input('Enter your name')
# name = name + x
# print (len(name))

#LISTS AND TUPLES
arr=[1,'me',3,4,5]
arr1=[1,'me',3,4,5]

arr = arr + arr1


#slice
print(arr[0:6])


#index
print(arr1[1])
print(arr[9])


#FUNCTIONS
def div(num):
    if(num > 0):
        return num * div(num-1)
    else:
        return 1

print(div(4))
