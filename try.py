def getChange(amount,price):
    currency = [100,50,25,10,5,1]
    soln = [0,0,0,0,0,0]
    if amount > price:
        Rchange = amount - price
        for i in range(0,6):
            count = 0
            if Rchange >= currency[i]:
                while Rchange >= currency[i]:
                    Rchange = Rchange - currency[i]
                    count = count + 1
        
            soln[i] = count
        print(soln)

    elif amount < price:
        print('Your money is not enough for the purchase')

    else:
        print('You have no change')
    

getChange(10,10)
    