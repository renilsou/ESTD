def fat_duplo(num):
    if num == 1:
        return 1
    else:
        return num * fat_duplo(num-2)
    
print(fat_duplo(7))