''' 3) Escriba un código que verifique si se cumple la conjetura de collatz en enteros de un intervalo [p,q]. La 
conjetura indica que para cualquier número  entero positivo n se aplica:
Si n es par → n = n / 2,  Si n es impar → n = 3n + 1,
Ejemplo:  6 ≤ n  ≤ 8
n=6:  6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
n=7:   7 → 22 → 11 → 34 → 17 → 52 → 26 → 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
n=8:   8 → 4 → 2 → 1
Demostrado...
Regla q ≥ 100p para poder aplicar la demostración '''

import os
def demostrar_collatz(n):
    pasos = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2  # Regla: Si n es par -> n = n/2 [cite: 19]
        else:
            n = 3 * n + 1  # Regla: Si n es impar -> n = 3n + 1 [cite: 19]
        pasos.append(n)
    return pasos

def main():
    print("--- Verificación de la Conjetura de Collatz (UNEG) ---")
    
    try:
        p = int(input("Ingrese el inicio del intervalo (p): "))
        q = int(input("Ingrese el fin del intervalo (q): "))
        
        # Validación obligatoria: q >= 100p 
        if q < 100 * p:
            print(f"\n Error: No se cumple la regla q >= 100p.")
            print(f"Para p={p}, q debe ser al menos {100 * p}.")
            return

        print(f"\nVerificando el intervalo [{p}, {q}]...")
        print("-" * 30)
        
        for num in range(p, q + 1):
            secuencia = demostrar_collatz(num)
            # Aquí imprimimos TODA la lista de números
            proceso_str = " -> ".join(map(str, secuencia))
            print(f"n={num}: {proceso_str}\n\n")
            
        print("-" * 30)
        print("Conjetura demostrada para todo el intervalo.")
        
    except ValueError:
        print(" Error: Debe ingresar números enteros.")

if __name__ == "__main__":
    main()