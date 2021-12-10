r= 0b00100011
def En(T):
    a= int(T)
    if a>27.5:
        return "Tiene Fiebre"
    elif a<25 :
        return "Tiene Hipotermia"
    else:
        return "OK"