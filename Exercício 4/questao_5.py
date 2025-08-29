def decrescente(num):
    if num == 0:
        print(0)
    else:
        print(num)
        return decrescente(num-1)
    
decrescente(5)