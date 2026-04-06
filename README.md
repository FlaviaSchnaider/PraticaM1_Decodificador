# Pratica M1 - Decodificador
Este projeto foi desenvolvido como parte da disciplina de Organização de Computadores, com foco na compreensão prática do funcionamento interno da ISA RISC-V.

<br>

# Objetivo
O objetivo principal é interpretar instruções em formato hexadecimal ou binário, identificando:
- O tipo da instrução (R, I, S, B, U ou J)
- O opcode
- Registradores (rd, rs1, rs2)
- Campos funcionais (funct3, funct7)
- Valores imediatos (imm)

<br>

# Funcionalidade
1. Leitura de arquivos contendo instruções em:
    - Hexadecimal (ex: 0x00500413)
    - Binário (32 bits)
2. Classificação automática das instruções:
    - Tipo R
    - Tipo I
    - Tipo S
    - Tipo B
    - Tipo U
    - Tipo J
3. Extração correta dos campos conforme o formato
4. Suporte às instruções base do padrão RV32I
5. Saída organizada com todos os campos decodificados

<br>

# Como Funciona
O programa analisa os 7 bits menos significativos (opcode) de cada instrução para determinar seu tipo. A partir disso, os demais bits são interpretados de acordo com o formato específico da instrução.

- Exemplo: 0x00500413 
<br>
Tipo: I; rd = 8; funct3 = 0; rs1 = 0; imm = 5

<br>

# Tecnologias Utilizadas
- Python
- Arquitetura RISC-V

<br>

# Como rodar
- python riscv_parser.py instrucoes.txt

<br>

# Autores
- Flávia Schnaider
- Gregori da Luz Maciel