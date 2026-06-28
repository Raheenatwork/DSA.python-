def inttostr(i):
    dig = '0123456789'
    if i==0 :
        return '0'
    result = ''
    while i>0 :
        result  = dig[i%10]+result
        i=i//10
        return result
    print(inttostr(123))