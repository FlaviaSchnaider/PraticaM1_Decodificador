import sys

# R: operações entre registradores
# I: imediato
# S: store
# B: branch
# U: upper
# J: jump

# Mapeamento de opcode para tipo de instrução RISC-V
TIPO_OPCODE = {
    "0110011": "R",
    "0010011": "I",
    "0000011": "I",
    "1100111": "I",
    "0100011": "S",
    "1100011": "B",
    "0110111": "U",
    "0010111": "U",
    "1101111": "J",
    "1110011": "I"
}

def hex_para_binario(hex_str):
    """Converte uma string hexadecimal para binário (32 bits)"""
    return format(int(hex_str, 16), '032b')

def interpretar_instrucao(instr_bin):
    """Interpreta uma instrução binária RISC-V"""
    opcode = instr_bin[25:32]
    tipo = TIPO_OPCODE.get(opcode, "DESCONHECIDO")

    resultado = {"tipo": tipo, "opcode": opcode}

    if tipo == "R":
        resultado.update({
            "rd": int(instr_bin[20:25], 2),
            "funct3": int(instr_bin[17:20], 2),
            "rs1": int(instr_bin[12:17], 2),
            "rs2": int(instr_bin[7:12], 2),
            "funct7": int(instr_bin[0:7], 2)
        })

    elif tipo == "I":
        resultado.update({
            "rd": int(instr_bin[20:25], 2),
            "funct3": int(instr_bin[17:20], 2),
            "rs1": int(instr_bin[12:17], 2),
            "imm": int(instr_bin[0:12], 2)
        })

    elif tipo == "S":
        imediato = instr_bin[0:7] + instr_bin[20:25]
        resultado.update({
            "funct3": int(instr_bin[17:20], 2),
            "rs1": int(instr_bin[12:17], 2),
            "rs2": int(instr_bin[7:12], 2),
            "imm": int(imediato, 2)
        })

    elif tipo == "B":
        imediato = instr_bin[0] + instr_bin[24] + instr_bin[1:7] + instr_bin[20:24] + "0"
        resultado.update({
            "funct3": int(instr_bin[17:20], 2),
            "rs1": int(instr_bin[12:17], 2),
            "rs2": int(instr_bin[7:12], 2),
            "imm": int(imediato, 2)
        })

    elif tipo == "U":
        resultado.update({
            "rd": int(instr_bin[20:25], 2),
            "imm": int(instr_bin[0:20], 2)
        })

    elif tipo == "J":
        imediato = instr_bin[0] + instr_bin[12:20] + instr_bin[11] + instr_bin[1:11] + "0"
        resultado.update({
            "rd": int(instr_bin[20:25], 2),
            "imm": int(imediato, 2)
        })

    return resultado

def processar_arquivo(caminho_arquivo):
    """Lê e processa instruções de um arquivo"""
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas:
        linha = linha.strip()

        if not linha:
            continue

        # Detecta se é binário ou hexadecimal
        if all(c in '01' for c in linha):
            instr_bin = linha.zfill(32)
        else:
            instr_bin = hex_para_binario(linha.replace("0x", ""))

        resultado = interpretar_instrucao(instr_bin)
        print(f"{linha} -> {resultado}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("python riscv_parser.py <arquivo>")
    else:
        processar_arquivo(sys.argv[1])