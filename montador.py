# def montar_I(instrucao):
#     opcode = instrucoes[instrucao[0]]["opcode"]
#     funct3 = instrucoes[instrucao[0]]["funct3"]

#     rd = format(int(instrucao[1][1:]), '05b')
#     rs1 = format(int(instrucao[2][1:]), '05b')
#     immediate = format(int(instrucao[3]), '012b') 

#     palavra = immediate + rs1 + funct3 + rd + opcode
#     return palavra  

# def montar_S(instrucao):
#     opcode = instrucoes[instrucao[0]]["opcode"]
#     funct3 = instrucoes[instrucao[0]]["funct3"]

#     rs1 = format(int(instrucao[1][1:]), '05b')
#     rs2 = format(int(instrucao[2][1:]), '05b')
#     immediate = format(int(instrucao[3]), '012b')

#     palavra = immediate[0:7] + rs2 + rs1 + funct3 + immediate[7:12] + opcode
#     return palavra

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
}


def montar(instrucao):
    if(instrucoes[instrucao[0]]["formato"] == "R"):
        return montar_R(instrucao)
    elif(instrucoes[instrucao[0]]["formato"] == "I"):
        return montar_I(instrucao)
    elif(instrucoes[instrucao[0]]["formato"] == "S"):
        return montar_S(instrucao)
    elif(instrucoes[instrucao[0]]["formato"] == "SB"):
        return montar_S(instrucao)
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

    rd = format(int(instrucao[1][1:]), '05b')
    rs1 = format(int(instrucao[2][1:]), '05b')
    immediate = base(instrucao)

    palavra = immediate + rs1 + funct3 + rd + opcode
    return palavra  

def montar_S(instrucao):
    opcode = instrucoes[instrucao[0]]["opcode"]
    funct3 = instrucoes[instrucao[0]]["funct3"]

    rs1 = format(int(instrucao[1][1:]), '05b')
    rs2 = format(int(instrucao[2][1:]), '05b')
    immediate = base(instrucao)

    palavra = immediate[0:7] + rs2 + rs1 + funct3 + immediate[7:12] + opcode
    return palavra

def montar_sb(instrucao):
    opcode = instrucoes[instrucao[0]]["opcode"]
    funct3 = instrucoes[instrucao[0]]["funct3"]

    rs1 = format(int(instrucao[1][1:]), '05b')
    rs2 = format(int(instrucao[2][1:]), '05b')

    immediate = base(instrucao)

    palavra = immediate[0] + immediate[1:7] + rs2 + rs1 + funct3 + immediate[7:11] + immediate[11] + opcode

    return palavra

def base(instrucao):
    if(instrucao[3][0:2] == '0b'):
        return format(int(instrucao[3][2:], base=2), '012b')
    elif(instrucao[3][0:2] == '0x'):
        return format(int(instrucao[3], base=16), '012b')
    elif(instrucao[3][0:2] == '0o'):
        return format(int(instrucao[3], base=8), '012b')
    else:
        return format(int(instrucao[3]), '012b')


bits = ""
# while True:
#     instrucao = input("Digite um comando (ou 'fim' para encerrar): ")
#     if instrucao == 'fim':
#         break
#     instrucao = instrucao.replace(',', '')
#     elementos = instrucao.split(' ')
#     if(elementos[0] == 'sb' or elementos[0] == 'lb'):
#         offset, elementos[2] = elementos[2].replace(')', '').split('(')
#         elementos.insert(3, offset)
#     bits += (montar(elementos)) + "\n"
# print(bits)

contador = 0

with open('teste.ams', 'r') as arquivo:
    conteudo = arquivo.read()
    instrucao = conteudo.split('\n')
    tamanho = len(instrucao)
print(f'\n{conteudo}\n')
while contador != tamanho:

    if instrucao == 'fim':
        break

    instrucao[contador] = instrucao[contador].replace(',', '')
    elementos = instrucao[contador].split(' ')
    if(elementos[0] in ('sb', 'lb', 'sw', 'lw', 'sh', 'lh')):
        offset, elementos[2] = elementos[2].replace(')', '').split('(')
        elementos.insert(3, offset)
    #bits += (montar(elementos)) + "\n"
    bits += format(int(montar(elementos), 2), '08x') + "\n"
    contador += 1

print(bits)

with open('saida.txt', 'w') as f:
    f.write(bits)
