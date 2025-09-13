palavra = ('agua','fogo','terra','ar')
def separar_vogais(palavra):
    vogais = "aeiou"
    vogais_encontrada = [char for char in palavra if char in vogais]
    return vogais_encontrada
for p in palavra :
    vogais = separar_vogais(p)
    print("A palavra {} possui {} vogais: {}".format(p,len(vogais),','.join(vogais)))
    
