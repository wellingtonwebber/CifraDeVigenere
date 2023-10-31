import sys

# Verifica se a quantidade de argumentos está correta
if len(sys.argv) != 4:
    print("Uso: python script.py <arquivo.txt> <chave> <criptografar ou decriptografar>")
    sys.exit(1)  # Sai do script com código de erro 1

# Obtém os argumentos da linha de comando
nomeDoArquivo = sys.argv[1]
chave = sys.argv[2]
modo = sys.argv[3]

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWYZÁÉÍÓÚÃÂÊÔabcdefghijklmnopqrstuvwxyzáéíóúãâêô:.@#%&*()-à;,?!_-0123456789 "

letra_valor = dict(zip(alfabeto, range(len(alfabeto)))) #dicionario com letra como key
valor_letra = dict(zip(range(len(alfabeto)), alfabeto)) #dicionario com valor inteiro de cada letra como key

def criptografar(msg, key):

    msg_criptografada = ""
    split_message = [
        msg[i: i + len(key)] for i in range(0, len(msg), len(key)) #divide a linha com valores do mesmo tamanho da key
    ]

    for split in split_message:
        i = 0
        for letra in split:
            valor = (letra_valor[letra] + letra_valor[key[i]]) % len(alfabeto) #soma os valores das duas listas e faz módulo pelo comprimento do alfabeto utilizado
            msg_criptografada += valor_letra[valor]
            i += 1

    return msg_criptografada


def decriptografar(cifra, key): #basicamente a mesma funcao de criptografar só que agora diminuimos o valor da key
    msg_decriptografada = ""
    split_cifra = [
        cifra[i: i + len(key)] for i in range(0, len(cifra), len(key))
    ]

    for split in split_cifra:
        i = 0
        for letra in split:
            valor = (letra_valor[letra] - letra_valor[key[i]]) % len(alfabeto)
            msg_decriptografada += valor_letra[valor]
            i += 1

    return msg_decriptografada

def manipularArquivo(nomeArquivo, key, isCriptografado):

    if isCriptografado:
        try:
            with open(nomeArquivo, "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.readlines()

        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")
            sys.exit(1)

        else:
            for index in range(len(conteudo)):
                conteudo[index] = decriptografar(conteudo[index].rstrip('\n'), key)

            with open(nomeArquivo[:-10] + "decripto.txt", "w", encoding="utf-8") as arquivo:
                for linha in conteudo:
                    arquivo.write(linha + '\n')

    else:
        try:
            with open(nomeArquivo, "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.readlines()

        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")
            sys.exit(1)

        else:
            for index in range(len(conteudo)):
                conteudo[index] = criptografar(conteudo[index].rstrip('\n'), key)

        with open(nomeArquivo[:-4] + "_cripto.txt", "w", encoding="utf-8") as arquivo:
            for linha in conteudo:
                arquivo.write(linha + '\n')

    return 0
def main():

    if modo == "criptografar":
        manipularArquivo(nomeDoArquivo, chave, False)
        print("Arquivo criptografado com sucesso!")

    elif modo == "decriptografar":
        manipularArquivo(nomeDoArquivo, chave, True)
        print("Arquivo decriptografado com sucesso!")

    else:
        print("Modo inválido!")

main()
