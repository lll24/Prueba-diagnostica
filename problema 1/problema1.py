''' 1) Dado una cadena de expresión aritmética imprima cada componente según su clasificación 
( NUMERO, OPERADOR, PAREN_IZQ, PAREN_DER, OPERANDO, ERROR).
Reglas:
NUMERO: debe ser un entero o un real con el “.”,  como marcador de decimales, sin signo
OPERANDO: no debe tener espacios ni iniciar con un numero (VALOR, A, B, CONT)
OPERADOR: + - * /
Ejemplo de salida para "12+ 3 * (4)":
Salida:
NUMERO 12    OPERADOR +   NUMERO 3  OPERADOR *  PAREN_IZQ ( 
NUMERO 4      PAREN_DER )   PARÉNTESIS BALANCEADOS.   '''


import re

def analizador_interactivo():
    print("------------------------")
    print("Reglas: NUMERO (entero o real con su .), OPERANDO (letras, no inician con numero), OPERADOR (+-*/)")
    print("------------------------")
    
    cadena = input("\nIngresa la expresion a analizar: ")
    
    # Patrones según el PDF [cite: 11]
    especificaciones = [
        ('NUMERO',    r'\d+(\.\d+)?'),          
        ('OPERANDO',  r'[a-zA-Z_][a-zA-Z0-9_]*'), 
        ('OPERADOR',  r'[+\-*/]'),              
        ('PAREN_IZQ', r'\('),                    
        ('PAREN_DER', r'\)'),                    
        ('ESPACIO',   r'\s+'),                  
        ('ERROR',     r'.'),                    
    ]
    
    tok_regex = '|'.join(f'(?P<{name}>{pat})' for name, pat in especificaciones)
    
    resultado = []
    errores = []
    balance = 0
    
    for mo in re.finditer(tok_regex, cadena):
        tipo = mo.lastgroup
        valor = mo.group()
        
        if tipo == 'ESPACIO':
            continue
        elif tipo == 'PAREN_IZQ':
            balance += 1
        elif tipo == 'PAREN_DER':
            balance -= 1
        elif tipo == 'ERROR':
            errores.append(f"El caracter '{valor}' no esta permitido (solo se aceptan numeros, letras y +-*/).")
        
        resultado.append(f"{tipo} {valor}")

    # --- MOSTRAR RESULTADOS ---
    print("\n--- Resultado del Analisis ---")
    print(" ".join(resultado))
    
    # --- EXPLICACIÓN DE FALLOS ---
    print("\n--- Diagnostico ---")
    
    # 1. Verificación de Parentheses 
    if balance == 0:
        print(" PARENTESIS BALANCEADOS.")
    elif balance > 0:
        print(f" ERROR: Faltan {balance} parentesis de cierre ')'.")
    else:
        print(f" ERROR: Hay {abs(balance)} parentesis de cierre ')' de mas.")
        
    # 2. Verificación de caracteres inválidos 
    if errores:
        for err in errores:
            print(f" ERROR LEXICO: {err}")
    else:
        print("Todo bien")

if __name__ == "__main__":
    analizador_interactivo()