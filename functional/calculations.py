
# мат ожидание
# данные принимаются в виде строки, вероятность выпадения элемента рвно значна у всех
def M(X):
    count=len(X)
    if count==0:
        return 0
    result=0
    for i in X:
        result = result + i
    
    return result/count

# дисперсия
# данные принимаются в виде строки, вероятность выпадения элемента рвно значна у всех
def D(X):
    X2=[]
    for i in X:
        X2.append(i**2)
    return M(X2)-M(X)**2

# медиана
# данные принимаются в виде строки, вероятность выпадения элемента рвно значна у всех
def Me(X):
    X.sort()
    if len(X)==0:
        return 0
    if len(X)%2==0:
        return (X[len(X)//2]+X[len(X)//2-1])/2
    else:
        return X[len(X)//2]
    
# расчет всех возможных значений
# принимает карты фракции
def calculator(cards):
    result={}
    spells=[]
    troops=[]
    places=[]
    for i in cards.spells.items():
        spells.append(i[1])
    for i in cards.troops.items():
        troops.append(i[1])
    for i in cards.places.items():
        places.append(i[1])
    result["фракция"]=cards.name

    result["мат ожидание особой карты"]=M(spells)
    result["медиальное значение особой карты"]=Me(spells)
    result["дисперсия особой карты"]=D(spells)

    result["мат ожидание отряда"]=M(troops)
    result["медиальное значение отряда"]=Me(troops)
    result["дисперсия отряда"]=D(troops)

    result["мат ожидание артефакта"]=M(places)
    result["медиальное значение артефактов"]=Me(places)
    result["дисперсия артефакта"]=D(places)

    all=spells+troops+places
    result["мат ожидание общее"]=M(all)
    result["медиальное значение общее"]=Me(all)
    result["дисперсия общее"]=D(all)

    return result


    