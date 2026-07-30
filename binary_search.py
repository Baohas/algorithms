#бинарный поиск в упорядоченном массиве
def binary_search(arr, target):
    lo = 0 #нижний индекс
    hi = len(arr)-1 #верхний индекс
    while lo <= hi: #пока верх и низ не сошлись
        mid = (lo+hi)//2 #ищем центр
        if target < arr[mid]:
            hi = mid-1
        elif target > arr[mid]:
            lo = mid+1
        else:
            return mid #возврат индекса таргета
    return lo #возврат индекса где мог бы стоять таргет (если его необходимо занести в этот массив)

print(binary_search([1,2,2,5,6], 4))
