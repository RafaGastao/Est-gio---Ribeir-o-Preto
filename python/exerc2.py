def contar_letra_a(string):
    # Converte a string para minúsculas e conta a quantidade de 'a'
    contagem = string.lower().count('a')
    
    if contagem > 0:
        return f"A letra 'a' aparece {contagem} vezes na string."
    else:
        return "A letra 'a' não foi encontrada na string."


string = input("Informe uma string: ")  
print(contar_letra_a(string))


    