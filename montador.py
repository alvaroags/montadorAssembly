def Qual_instrucao(instrucao):
    if instrucao[0] == 'lb':
        return lb
    elif instrucao[0] == 'sb':
        return sb
    elif instrucao[0] == 'add':
        return add
    elif instrucao[0] == 'and':
        return aand
    elif instrucao[0] == 'ori':
        return ori
    elif instrucao[0] == 'or':
        return oor
    elif instrucao[0] == 'sll':
        return sll
    elif instrucao[0] == 'bne':
        return bne
    elif instrucao[0] == 'li':
        return addi

def lb(elementos):

    opcode = "0000011"
    funct3 = "000"

    offset, origem = elementos[2].split('(')  
    origem = origem.replace(")", "")
    rs1 = format(int(origem[1:]), '05b')
    immediate = format(int(offset), '012b')
    rd = format(int(elementos[1][1:]), '05b')
    palavra = immediate + rs1 + funct3 + rd + opcode

    return palavra

def sb(elementos):

    opcode = "0100011"
    funct3 = "000"

    offset, origem = elementos[2].split('(')
    origem = origem.replace(")", "")
    rs1 = format(int(origem[1:]), '05b')
    rs2 = format(int(elementos[1][1:]), '05b')
    immediate = format(int(offset), '012b')

    palavra = immediate[0:7] + rs2 + rs1 + funct3 + immediate[7:12] + opcode
    
    return palavra

def add(elementos):

    opcode = "0110011"
    funct3 = "000"
    funct7 = "0000000"

    rd = format(int(elementos[1][1:]), '05b')
    rs1 = format(int(elementos[2][2:]), '05b')
    rs2 = format(int(elementos[3][2:]), '05b')

    palavra = funct7 + rs2 + rs1 + funct3+ rd + opcode
    return palavra

def addi(elementos):
    
    if(elementos[0] == 'li'):
        elementos[0] = 'addi'
        elementos.insert(2, 'x0')

    opcode = "0010011"
    funct3 = "000"

    rd = format(int(elementos[1][1:]), '05b')
    # rs1 = format(int(elementos[2][2:]), '05b')  
    rs1 = format(int(elementos[2][1:]), '05b')  
    immediate = format(int(elementos[3]), '012b')
    
    palavra = immediate + rs1 + funct3 + rd + opcode
    return palavra
    
def aand(elementos):

    opcode = "0110011"
    funct3 = "111"
    funct7 = "0000000"

    rd = format(int(elementos[1][1:]), '05b')
    rs1 = format(int(elementos[2][2:]), '05b')
    rs2 = format(int(elementos[3][2:]), '05b')

    palavra = funct7 + rs2 + rs1 + funct3+ rd + opcode
    return palavra

def oor(elementos):

    opcode = "0110011"
    funct3 = "110"
    funct7 = "0000000"

    rd = format(int(elementos[1][1:]), '05b')
    rs1 = format(int(elementos[2][2:]), '05b')
    rs2 = format(int(elementos[3][2:]), '05b')

    palavra = funct7 + rs2 + rs1 + funct3+ rd + opcode
    return palavra


def ori(elementos):

    opcode = "0010011"
    funct3 = "110"

    rd = format(int(elementos[1][1:]), '05b')
    rs1 = format(int(elementos[2][2:]), '05b')
    immediate = format(int(elementos[3]), '012b')

    palavra = immediate + rs1 + funct3 + rd + opcode
    return palavra

def sll(elementos):

    opcode = "0110011"
    funct3 = "001"
    funct7 = "0000000"

    rd = format(int(elementos[1][1:]), '05b')
    rs1 = format(int(elementos[2][2:]), '05b')
    rs2 = format(int(elementos[3][2:]), '05b')

    palavra = funct7 + rs2 + rs1 + funct3+ rd + opcode
    return palavra

def bne(elementos):
    
    opcode = "1100011"
    funct3 = "001"

    rd = format(int(elementos[1][1:]), '05b')
    rs1 = format(int(elementos[2][1:]), '05b')
    immediate = format(int(elementos[3]), '012b')
    
    palavra = immediate + rs1 + funct3 + rd + opcode
    return palavra


# instrucao = str(input())
# elementos = instrucao.split(',')
# print(elementos)
# primeiro, segundo = elementos[0].split(' ')
# elementos[0] = primeiro
# elementos.insert(1, segundo)
# print(elementos)
# print(instrucao)
# print(Qual_instrucao(elementos)(elementos))

while True:
    instrucao = input("Digite um comando (ou 'fim' para encerrar): ")
    if instrucao == 'fim':
        break
    elementos = instrucao.split(',')
    primeiro, segundo = elementos[0].split(' ')
    elementos[0] = primeiro
    elementos.insert(1, segundo)
    print(Qual_instrucao(elementos)(elementos))
