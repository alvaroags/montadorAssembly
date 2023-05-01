import argparse

instrucoes = {
    "lb": {
        "opcode": "0000011",
        "funct3": "000",
        "formato": "I"
    }, 
    
    "lh": {
        "opcode": "0000011",
        "funct3": "001",
        "formato": "I"
    },

    "lw": {
        "opcode": "0000011",
        "funct3": "010",
        "formato": "I"
    },

    "sb": {
        "opcode": "0100011",
        "funct3": "000",
        "formato": "S"
    },

    "sh": {
        "opcode": "0100011",
        "funct3": "001",
        "formato": "S"
    },
    
    "sw": {
        "opcode": "0100011",
        "funct3": "010",
        "formato": "S"
    },

    "add": {
        "opcode": "0110011",
        "funct3": "000",
        "funct7": "0000000",
        "formato": "R"
    },

    "sub": {
        "opcode": "0110011",
        "funct3": "000",
        "funct7": "0100000",
        "formato": "R"
    },

    "and": {
        "opcode": "0110011",
        "funct3": "111",
        "funct7": "0000000",
        "formato": "R"
    },

    "or": {
        "opcode": "0110011",
        "funct3": "110",
        "funct7": "0000000",
        "formato": "R"
    },
    
    "xor": {
        "opcode": "0110011",
        "funct3": "100",
        "funct7": "0000000",
        "formato": "R"
    },

    "addi": {
        "opcode": "0010011",
        "funct3": "000",
        "formato": "I"
    },
    
    "li":{
        "opcode": "0010011",
        "funct3": "000",
        "formato": "I"
    },

    "mv":{
        "opcode": "0010011",
        "funct3": "000",
        "formato": "I"
    },
    
    "andi": {
        "opcode": "0010011",
        "funct3": "111",
        "formato": "I"
    },

    "ori": {
        "opcode": "0010011",
        "funct3": "110",
        "formato": "I"
    },

    "sll": {
        "opcode": "0110011",
        "funct3": "001",
        "funct7": "0000000",
        "formato": "R"
    },

    "srl": {
        "opcode": "0110011",
        "funct3": "101",
        "funct7": "0000000",
        "formato": "R"
    },

    "bne": {
        "opcode": "1100011",
        "funct3": "001",
        "formato": "SB"
    },

    "beq": {
        "opcode": "1100011",
        "funct3": "000",
        "formato": "SB"
    },

    "blt":{
        "opcode": "1100011",
        "funct3": "100",
        "formato": "SB"
    },
    
    "bge":{
        "opcode": "1100011",
        "funct3": "101",
        "formato": "SB"
    },

    "bnez":{
        "opcode": "1100011",
        "funct3": "001",
        "formato": "SB"
    },

    "beqz":{
        "opcode": "1100011",
        "funct3": "000",
        "formato": "SB"
    },

    "bltz":{
        "opcode": "1100011",
        "funct3": "100",
        "formato": "SB"
    },

    "bgez":{
        "opcode": "1100011",
        "funct3": "101",
        "formato": "SB"
    }
}


def montar(instrucao):
    if(instrucoes[instrucao[0]]["formato"] == "R"):
        return montar_R(instrucao)
    elif(instrucoes[instrucao[0]]["formato"] == "I"):
        return montar_I(instrucao)
    elif(instrucoes[instrucao[0]]["formato"] == "S"):
        return montar_S(instrucao)
    elif(instrucoes[instrucao[0]]["formato"] == "SB"):
        return montar_sb(instrucao)
    else:
        print("Instrução não reconhecida")

def montar_R(instrucao):
    opcode = instrucoes[instrucao[0]]["opcode"]
    funct3 = instrucoes[instrucao[0]]["funct3"]
    funct7 = instrucoes[instrucao[0]]["funct7"]

    rd = format(int(instrucao[1][1:]), '05b')
    rs1 = format(int(instrucao[2][1:]), '05b')
    rs2 = format(int(instrucao[3][1:]), '05b')

    palavra = funct7 + rs2 + rs1 + funct3+ rd + opcode
    return palavra


def montar_I(instrucao):
    opcode = instrucoes[instrucao[0]]["opcode"]
    funct3 = instrucoes[instrucao[0]]["funct3"]
    if(instrucao[0] == "li"):
        instrucao.insert(2, "x0")
    if(instrucao[0] == "mv"):
        instrucao.insert(3, "0")

    rd = format(int(instrucao[1][1:]), '05b')
    rs1 = format(int(instrucao[2][1:]), '05b')
    immediate = base(instrucao)

    palavra = immediate + rs1 + funct3 + rd + opcode
    return palavra  

def montar_S(instrucao):
    opcode = instrucoes[instrucao[0]]["opcode"]
    funct3 = instrucoes[instrucao[0]]["funct3"]

    rs1 = format(int(instrucao[2][1:]), '05b')
    rs2 = format(int(instrucao[1][1:]), '05b')
    immediate = base(instrucao)
    
    palavra = immediate[0:7] + rs2 + rs1 + funct3 + immediate[7:12] + opcode
    return palavra

def montar_sb(instrucao):
    opcode = instrucoes[instrucao[0]]["opcode"]
    funct3 = instrucoes[instrucao[0]]["funct3"]
    if(instrucao[0] == "bnez" or instrucao[0] == "beqz" or instrucao[0] == "bltz" or instrucao[0] == "bgez"):
        instrucao.insert(2, "x0")
    rs1 = format(int(instrucao[1][1:]), '05b')
    rs2 = format(int(instrucao[2][1:]), '05b')
    
    if(instrucao[3][0:2] == '0x' or instrucao[3][0:2] == '0b' or instrucao[3][0:2] == '0o'):
        instrucao[3] = base(instrucao)
        instrucao[3] = int(instrucao[3], base=2) // 2
    else: 
        instrucao[3] = int(instrucao[3], base=10) // 2
    
    instrucao[3] = str(instrucao[3])
    immediate = base(instrucao)
    palavra = immediate[0] + immediate[2:8] + rs2 + rs1 + funct3 + immediate[8:12] + immediate[1] + opcode
    return palavra

def base(instrucao):
    if(instrucao[3][0] == '-'):
        return format(complementoDeDois(int(instrucao[3])), '012b')
    if(instrucao[3][0:2] == '0b'):
        return format(int(instrucao[3][2:], base=2), '012b')
    elif(instrucao[3][0:2] == '0x'):
        return format(int(instrucao[3], base=16), '012b')
    elif(instrucao[3][0:2] == '0o'):
        return format(int(instrucao[3], base=8), '012b')
    else:
        return format(int(instrucao[3]), '012b')

def complementoDeDois(numero):
    binario = bin(numero)[3:]
    binario = binario.zfill(12)
    invertido = "".join(["0" if bit == "1" else "1" for bit in binario])
    return int(invertido, 2) + 1

# parser = argparse.ArgumentParser(description='Montador de código assembly para RISC-V')
# parser.add_argument('entrada', type=str, help='Arquivo de entrada')
# parser.add_argument('-o', '--saida', type=str, help='Arquivo de saída')
# args = parser.parse_args()
argsEntrada = ''
argsSaida = ''

print("Montador de código assembly para RISC-V\n")
esc = int(input("1 - Para fornecer um arquivo de entrada e um arquivo de saída\n2 - Para fornecer um arquivo de entrada e imprimir o resultado no terminal\n3 - Para digitar o código no terminal e imprimir o resultado no terminal\n"))
match esc:
    case 1:
        argsEntrada, argsSaida = input("Digite o nome do arquivo de entrada e do arquivo de saída: (informe as extensões) ").split(' ')
    case 2:
        argsEntrada = input("Digite o nome do arquivo de entrada (informe as extensões): ")
    case 3:
        while(True):
            entrada = input('Digite a instrução:').rstrip('\n')
            if(entrada == 'fim'):
                break
            argsEntrada += entrada + '\n'
    case _:
        print("Opção inválida! Tente novamente reiniciando o programa.")

bits = ""
# hexa = ""
contador = 0

if(esc == 1 or esc == 2):
    with open(argsEntrada, 'r') as arquivo:
        conteudo = arquivo.read()
        instrucao = conteudo.split('\n')
        tamanho = len(instrucao)
else:
    conteudo = argsEntrada
    instrucao = conteudo.split('\n')
    tamanho = len(instrucao) - 1

# print(f'\n{conteudo}\n')
while contador != tamanho:
    if instrucao == '\n' or instrucao == '':
        break

    instrucao[contador] = instrucao[contador].replace(',', '')
    elementos = instrucao[contador].split(' ')
    if(elementos[0] in ('sb', 'lb', 'sw', 'lw', 'sh', 'lh')):
        offset, elementos[2] = elementos[2].replace(')', '').split('(')
        elementos.insert(3, offset)
    bits += (montar(elementos)) + "\n"

    saida = bits.split('\n')
    # hexa += format(int(saida[contador], base=2), '08x') + "\n"
    contador += 1

if argsSaida:
    with open(argsSaida, 'w') as f:
        f.write(bits)
        # f.write(hexa)
else:
    print(bits)
    # print(hexa)

#entrada com cada uma das instruções
# lb x1, 0x10(x2)
# lh x1, 0x10(x2)
# lw x1, 0x10(x2)
# sb x1, 0x10(x2)
# sh x1, 0x10(x2)
# sw x1, 0x10(x2)
# add x1, x2, x3
# sub x1, x2, x3
# and x1, x2, x3
# or x1, x2, x3
# xor x1, x2, x3
# addi x1, x2, 0x10
# li x1, 0x10
# mv x1, x2
# andi x1, x2, 0x10
# ori x1, x2, 0x10
# sll x1, x2, x3
# srl x1, x2, x3
# bne x1, x2, 0x10
# beq x1, x2, 0x10
# blt x1, x2, 0x10
# bge x1, x2, 0x10
# bnez x1, 0x10
# beqz x1, 0x10
# bltz x1, 0x10
# bgez x1, 0x10