def num(p):
    result = []
    while True:
        if not (p % 2) :
            p = p // 2
            result.append(2)
        else:
            break
    for val in range(3,int(p**1//2)+1,2):
        while True:
            if not (p % val):
                p = p // val
                result.append(val)
            else:
                break
    if p > 2: 
        result.append(p)
    return result
          