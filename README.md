# Montador RISC-V

O projeto Montador RISC-V é um software que tem como objetivo converter instruções RISC-V para linguagem de máquina. Ele foi desenvolvido como parte da disciplina de Organização de Computadores 1 e tem como propósito ajudar os alunos a desenvolver habilidades em RISC-V.

## Funcionalidades

O Montador RISC-V é capaz de:

- Converter instruções RISC-V para binário
- Utilizar um dicionário contendo opcode, funct3, funct7, rd e rs1

## Dependências

Para utilizar o Montador RISC-V, basta executar o código em um terminal Python. Não é necessário instalar nenhuma dependência adicional.

## Contribuidores

O projeto foi desenvolvido com a contribuição de Álvaro Gomes e Esdras Araújo.

## Como usar

1. Abra um terminal e acesse a pasta do projeto.
2. Execute o arquivo `montador.py` com o comando `python montador.py`.
3. Digite as instruções RISC-V que deseja converter para binário.
4. O Montador RISC-V exibirá o resultado em formato binário.

## Exemplo

$ python montador.py
Digite as instruções RISC-V a serem convertidas para binário:
add x1, x2, x3
0010011 00011 00010 000 001 00100 0110011

## Licença

O Montador RISC-V é um software livre e está disponível sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.
