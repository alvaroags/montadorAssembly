instrucoes = {
    "lb": {
        "opcode": "0000011",
        "funct3": "000",
        "formato": "I"
    }, 
    
    "sb": {
        "opcode": "0100011",
        "funct3": "000",
        "formato": "S"
    },

    "add": {
        "opcode": "0110011",
        "funct3": "000",
        "funct7": "0000000",
        "formato": "R"
    },

    "addi": {
        "opcode": "0010011",
        "funct3": "000",
        "formato": "I"
    },

    "and": {
        "opcode": "0110011",
        "funct3": "111",
        "funct7": "0000000",
        "formato": "R"
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

    "or": {
        "opcode": "0110011",
        "funct3": "110",
        "funct7": "0000000",
        "formato": "R"
    },

    "andi": {
        "opcode": "0010011",
        "funct3": "111",
        "formato": "I"
    }
}

def montar(instrucao):
    if(instrucoes[instrucao[0]]["formato"] == "R"):
        return montar_R(instrucao)
    elif(instrucoes[instrucao[0]]["formato"] == "I"):
        return montar_I(instrucao)
    elif(instrucoes[instrucao[0]]["formato"] == "S"):
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
    immediate = format(int(instrucao[3]), '012b') 

    palavra = immediate + rs1 + funct3 + rd + opcode
    return palavra  

def montar_S(instrucao):
    opcode = instrucoes[instrucao[0]]["opcode"]
    funct3 = instrucoes[instrucao[0]]["funct3"]

    rs1 = format(int(instrucao[1][1:]), '05b')
    rs2 = format(int(instrucao[2][1:]), '05b')
    immediate = format(int(instrucao[3]), '012b')

    palavra = immediate[0:7] + rs2 + rs1 + funct3 + immediate[7:12] + opcode
    return palavra

bits = ""
while True:
    instrucao = input("Digite um comando (ou 'fim' para encerrar): ")
    if instrucao == 'fim':
        break
    instrucao = instrucao.replace(',', '')
    elementos = instrucao.split(' ')
    if(elementos[0][0] == 'sb' or elementos[0][0] == 'lb'):
        offset, elementos[2] = elementos[2].replace(')', '').split('(')
        elementos.insert(3, offset)
    bits += (montar(elementos)) + "\n"
print(bits)






# def montar_R(instrucao):
#     opcode = instrucoes[instrucao[0]]["opcode"]
#     funct3 = instrucoes[instrucao[0]]["funct3"]
#     funct7 = instrucoes[instrucao[0]]["funct7"]

#     rd = format(int(instrucao[1][1:]), '05b')
#     rs1 = format(int(instrucao[2][2:]), '05b')
#     rs2 = format(int(instrucao[3][2:]), '05b')

#     palavra = funct7 + rs2 + rs1 + funct3+ rd + opcode
#     return palavra

# def montar_I(instrucao):
#     opcode = instrucoes[instrucao[0]]["opcode"]
#     funct3 = instrucoes[instrucao[0]]["funct3"]

#     rd = format(int(instrucao[1][1:]), '05b')
#     rs1 = format(int(instrucao[2][2:]), '05b')
#     immediate = format(int(instrucao[3]), '012b')

#     palavra = immediate + rs1 + funct3 + rd + opcode
#     return palavra

# def montar_S(instrucao):
#     opcode = instrucoes[instrucao[0]]["opcode"]
#     funct3 = instrucoes[instrucao[0]]["funct3"]

#     offset, origem = instrucao[2].split('(')
#     origem = origem.replace(")", "")
#     rs1 = format(int(origem[1:]), '05b')
#     rs2 = format(int(instrucao[1][2:]), '05b')
#     immediate = format(int(offset), '012b')

#     palavra = immediate + rs2 + rs1 + funct3 + opcode
#     return palavra

# def Qual_instrucao(instrucao):
#     if instrucao[0] == 'lb':
#         return lb
#     elif instrucao[0] == 'sb':
#         return sb
#     elif instrucao[0] == 'add':
#         return add
#     elif instrucao[0] == 'and':
#         return aand
#     elif instrucao[0] == 'ori':
#         return ori
#     elif instrucao[0] == 'or':
#         return oor
#     elif instrucao[0] == 'sll':
#         return sll
#     elif instrucao[0] == 'bne':
#         return bne
#     elif instrucao[0] == 'li':
#         return addi

# def lb(elementos):

#     opcode = "0000011"
#     funct3 = "000"

#     offset, origem = elementos[2].split('(')  
#     origem = origem.replace(")", "")
#     rs1 = format(int(origem[1:]), '05b')
#     immediate = format(int(offset), '012b')
#     rd = format(int(elementos[1][1:]), '05b')
#     palavra = immediate + rs1 + funct3 + rd + opcode

#     return palavra

# def sb(elementos):

#     opcode = "0100011"
#     funct3 = "000"

#     offset, origem = elementos[2].split('(')
#     origem = origem.replace(")", "")
#     rs1 = format(int(origem[1:]), '05b')
#     rs2 = format(int(elementos[1][1:]), '05b')
#     immediate = format(int(offset), '012b')

#     palavra = immediate[0:7] + rs2 + rs1 + funct3 + immediate[7:12] + opcode
    
#     return palavra

# def add(elementos):

#     opcode = "0110011"
#     funct3 = "000"
#     funct7 = "0000000"

#     rd = format(int(elementos[1][1:]), '05b')
#     rs1 = format(int(elementos[2][2:]), '05b')
#     rs2 = format(int(elementos[3][2:]), '05b')

#     palavra = funct7 + rs2 + rs1 + funct3+ rd + opcode
#     return palavra

# def addi(elementos):
    
#     if(elementos[0] == 'li'):
#         elementos[0] = 'addi'
#         elementos.insert(2, 'x0')

#     opcode = "0010011"
#     funct3 = "000"

#     rd = format(int(elementos[1][1:]), '05b')
#     # rs1 = format(int(elementos[2][2:]), '05b')  
#     rs1 = format(int(elementos[2][1:]), '05b')  
#     immediate = format(int(elementos[3]), '012b')
    
#     palavra = immediate + rs1 + funct3 + rd + opcode
#     return palavra
    
# def aand(elementos):

#     opcode = "0110011"
#     funct3 = "111"
#     funct7 = "0000000"

#     rd = format(int(elementos[1][1:]), '05b')
#     rs1 = format(int(elementos[2][2:]), '05b')
#     rs2 = format(int(elementos[3][2:]), '05b')

#     palavra = funct7 + rs2 + rs1 + funct3+ rd + opcode
#     return palavra

# def oor(elementos):

#     opcode = "0110011"
#     funct3 = "110"
#     funct7 = "0000000"

#     rd = format(int(elementos[1][1:]), '05b')
#     rs1 = format(int(elementos[2][2:]), '05b')
#     rs2 = format(int(elementos[3][2:]), '05b')

#     palavra = funct7 + rs2 + rs1 + funct3+ rd + opcode
#     return palavra


# def ori(elementos):

#     opcode = "0010011"
#     funct3 = "110"

#     rd = format(int(elementos[1][1:]), '05b')
#     rs1 = format(int(elementos[2][2:]), '05b')
#     immediate = format(int(elementos[3]), '012b')

#     palavra = immediate + rs1 + funct3 + rd + opcode
#     return palavra

# def sll(elementos):

#     opcode = "0110011"
#     funct3 = "001"
#     funct7 = "0000000"

#     rd = format(int(elementos[1][1:]), '05b')
#     rs1 = format(int(elementos[2][2:]), '05b')
#     rs2 = format(int(elementos[3][2:]), '05b')

#     palavra = funct7 + rs2 + rs1 + funct3+ rd + opcode
#     return palavra

# def bne(elementos):
    
#     opcode = "1100011"
#     funct3 = "001"

#     rd = format(int(elementos[1][1:]), '05b')
#     rs1 = format(int(elementos[2][1:]), '05b')
#     immediate = format(int(elementos[3]), '012b')
    
#     palavra = immediate + rs1 + funct3 + rd + opcode
#     return palavra


# instrucao = str(input())
# elementos = instrucao.split(',')
# print(elementos)
# primeiro, segundo = elementos[0].split(' ')
# elementos[0] = primeiro
# elementos.insert(1, segundo)
# print(elementos)
# print(instrucao)
# print(Qual_instrucao(elementos)(elementos))