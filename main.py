def multiploDeNumero(numeroRecibido):
    if numeroRecibido % 3 == 0 and numeroRecibido % 5 == 0:
        fizzbuzz = "fizzbuzz"
        numeroRecibido = fizzbuzz
        return numeroRecibido
    if numeroRecibido % 3 == 0:
        fizz = "fizz"
        numeroRecibido = fizz
        return numeroRecibido
    if numeroRecibido % 5 == 0:
        buzz = "buzz"
        numeroRecibido = buzz
        return numeroRecibido
    return numeroRecibido

contador = 1
while contador <= 100:
    print(multiploDeNumero(contador))
    contador+=1