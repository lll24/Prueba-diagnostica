''' 2) Dado una cadena C, valide si C se encuentra en notación FEN (Forsyth-Edwards Notation), Forsyth
Edwards Notation. FEN (Wikipedia, 2025) '''

import re
import os

def validar_fen(cadena):
    # Esta es la "Super Regex" que valida los 6 campos de la notación FEN
    # 1. Piezas: 8 filas separadas por /
    # 2. Turno: w o b
    # 3. Enroque: KQkq o -
    # 4. Peón al paso: e3, b6 o -
    # 5. Reloj 50 reglas: número
    # 6. Número de jugada: número
    regex_fen = (
        r'^([pnbrqkPNBRQK1-8]{1,8}/){7}[pnbrqkPNBRQK1-8]{1,8}' # 1. Tablero
        r'\s+[wb]'                                            # 2. Turno
        r'\s+(([KQkq]{1,4})|(-))'                             # 3. Enroque
        r'\s+(([a-h][36])|(-))'                               # 4. Peón al paso
        r'\s+\d+'                                             # 5. Media jugada
        r'\s+\d+$'                                            # 6. Jugada completa
    )

    if re.match(regex_fen, cadena):
        return True, "Sintaxis correcta."
    else:
        return False, "Sintaxis inválida. No cumple con el estándar FEN (Wikipedia, 2025)."

def inicio():
    print("--- Validador de Notación FEN (UNEG 2026-1) ---")
    print("Ejemplo válido: rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1\n")
    
    c = input("Ingresa la cadena FEN a validar: ").strip()
    
    es_valida, mensaje = validar_fen(c)
    
    print("\n--- Resultado ---")
    if es_valida:
        print(f"LA CADENA ES FEN VÁLIDA.\nDetalle: {mensaje}")
    else:
        print(f"LA CADENA NO ES FEN.\nDetalle: {mensaje}")

if __name__ == "__main__":
    inicio()