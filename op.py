def findstem(arr): 
    res, s, l  = "", arr[0], len(arr[0])
    for i in range(l) :
        for j in range( i + 1, l + 1) :
            k, stem = 1, s[i:j] 
            for k in range(1, len(arr)) :
                if stem not in arr[k]: 
                    break
            if (k + 1 == len(arr) and len(res) < len(stem)) :
                res = stem
    return res

arr = ["awmfe", "ame", "tame"]
common_substr = findstem(arr) 
if len(common_substr)>1:
    print(common_substr)
else:
    print("No the substring is not greater than 1")
    def subarraySum(arr)