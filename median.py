def find_median(data : list):
    data.sort()
    if len(data) == 0:
        return None
    elif len(data) % 2 == 0:
        return (data[len(data)//2]+data[(len(data)//2) - 1])/2
    else:
        return data[len(data)//2]
