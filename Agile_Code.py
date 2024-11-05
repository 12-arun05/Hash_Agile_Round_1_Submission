def func(arr):
     count,elem = 0,None
     for i in range(len(arr)):
        if count == 0:
            count = 1
            elem = arr[i]
        elif elem == arr[i]:
            count += 1
        else:
            count -= 1
            check_count = 0
     for i in range(len(arr)):
        if arr[i] == elem:
            check_count += 1
     return elem if check_count > (len(arr)//2) else -1
arr =[3,3,4,2,4,4,2,4,4]
print(func(arr))