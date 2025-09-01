def inverter(palavra):
    if palavra == "":
        return ""
    else:
        return inverter(palavra[1:]) + palavra[0]
    
print(inverter("Python"))