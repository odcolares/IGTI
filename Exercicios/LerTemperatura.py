temp = float(input('Qual a sua temperatura? '))
if temp >= 39:
    print(f'temperatura esta em {temp} oC, Vc esta com febre!')
elif 38.9 >= temp >= 37:
    print(f'temperatura esta em {temp} oC, vc esta febril!')
elif 36.9 >= temp >= 35:
    print(f'temperatura esta em {temp} oC, vc esta sem febre.')
else:
    print(f'temperatura esta em {temp} oC, vc esta morto.')