contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print(6)
        continue
    
    if contador >= 10 and contador <= 27:
        print(contador)
        continue
    
    print(contador)
    
    if contador == 48:
        break
    
    print('acabou')