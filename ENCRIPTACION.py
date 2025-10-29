import time
import sys
from colorama import Fore, Style, init
import unicodedata

# Inicializar colorama
init(autoreset=True)

# Alfabeto español extendido
ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# ===================== FUNCIONES BASE ===================== #

def limpiar_texto(texto):
    """Normaliza el texto eliminando acentos y convirtiendo a mayúsculas."""
    texto = texto.upper()
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    return texto

def escribir_lento(texto, color=Fore.WHITE, velocidad=0.02):
    """Imprime texto con efecto de escritura lenta."""
    for letra in texto:
        sys.stdout.write(color + letra)
        sys.stdout.flush()
        time.sleep(velocidad)
    print(Style.RESET_ALL, end="")

def banner():
    """Muestra el banner inicial."""
    print(Fore.CYAN + Style.BRIGHT)
    print("╔════════════════════════════════════════════════════════════╗")
    print("║             🔐 SISTEMA DE CIFRADOS - VERSIÓN 3.0 🔐        ║")
    print("║  Israel Ibañez Arteaga  |  Juan Carlos Javier Padilla      ║")
    print("╚════════════════════════════════════════════════════════════╝\n")
    print(Style.RESET_ALL)

# ===================== CIFRADO CÉSAR ===================== #

def cifrar_cesar(texto, desplazamiento):
    texto = limpiar_texto(texto)
    resultado = ""
    for c in texto:
        if c in ALFABETO:
            nueva_pos = (ALFABETO.index(c) + desplazamiento) % len(ALFABETO)
            resultado += ALFABETO[nueva_pos]
        else:
            resultado += c
    return resultado

def descifrar_cesar(texto, desplazamiento):
    return cifrar_cesar(texto, -desplazamiento)

# ===================== CIFRADO VIGENÈRE ===================== #

def cifrar_vigenere(texto, clave):
    texto = limpiar_texto(texto)
    clave = limpiar_texto(clave)
    resultado = ""
    clave_repetida = (clave * (len(texto) // len(clave) + 1))[:len(texto)]
    for c, k in zip(texto, clave_repetida):
        if c in ALFABETO:
            nueva_pos = (ALFABETO.index(c) + ALFABETO.index(k)) % len(ALFABETO)
            resultado += ALFABETO[nueva_pos]
        else:
            resultado += c
    return resultado

def descifrar_vigenere(texto, clave):
    texto = limpiar_texto(texto)
    clave = limpiar_texto(clave)
    resultado = ""
    clave_repetida = (clave * (len(texto) // len(clave) + 1))[:len(texto)]
    for c, k in zip(texto, clave_repetida):
        if c in ALFABETO:
            nueva_pos = (ALFABETO.index(c) - ALFABETO.index(k)) % len(ALFABETO)
            resultado += ALFABETO[nueva_pos]
        else:
            resultado += c
    return resultado

# ===================== CIFRADO ATBASH ===================== #

def cifrar_atbash(texto):
    texto = limpiar_texto(texto)
    resultado = ""
    for c in texto:
        if c in ALFABETO:
            nueva_pos = len(ALFABETO) - 1 - ALFABETO.index(c)
            resultado += ALFABETO[nueva_pos]
        else:
            resultado += c
    return resultado

# ===================== MENÚ PRINCIPAL ===================== #

def main():
    banner()

    while True:
        print(Fore.YELLOW + "1. Cifrado César")
        print("2. Cifrado Vigenère")
        print("3. Cifrado Atbash")
        print("4. Salir\n")

        opcion = input(Fore.CYAN + "👉 Elige una opción (1-4): " + Style.RESET_ALL)

        if opcion == "4":
            escribir_lento("\n👋 Saliendo del programa... ¡Hasta pronto!\n", Fore.MAGENTA)
            break

        if opcion not in ["1", "2", "3"]:
            print(Fore.RED + "❌ Opción no válida. Intenta nuevamente.\n")
            continue

        texto = input(Fore.WHITE + "\n📝 Escribe el texto: " + Style.RESET_ALL)

        # ===== CIFRADO CÉSAR =====
        if opcion == "1":
            try:
                desplazamiento = int(input(Fore.WHITE + "🔢 Desplazamiento (número): " + Style.RESET_ALL))
            except ValueError:
                print(Fore.RED + "❌ Error: Debes ingresar un número válido.\n")
                continue

            modo = input(Fore.CYAN + "¿Deseas cifrar (C) o descifrar (D)? ").upper()
            escribir_lento("\nProcesando", Fore.MAGENTA)
            for _ in range(3):
                sys.stdout.write("."); sys.stdout.flush(); time.sleep(0.4)
            print("\n")

            if modo == "C":
                resultado = cifrar_cesar(texto, desplazamiento)
                print(Fore.GREEN + "🔐 Texto cifrado: " + Fore.WHITE + resultado + "\n")
            elif modo == "D":
                resultado = descifrar_cesar(texto, desplazamiento)
                print(Fore.BLUE + "🔓 Texto descifrado: " + Fore.WHITE + resultado + "\n")
            else:
                print(Fore.RED + "❌ Opción inválida.\n")

        # ===== CIFRADO VIGENÈRE =====
        elif opcion == "2":
            clave = input(Fore.WHITE + "🔑 Ingresa la clave (por ejemplo 'KEY'): " + Style.RESET_ALL)
            modo = input(Fore.CYAN + "¿Deseas cifrar (C) o descifrar (D)? ").upper()
            escribir_lento("\nProcesando", Fore.MAGENTA)
            for _ in range(3):
                sys.stdout.write("."); sys.stdout.flush(); time.sleep(0.4)
            print("\n")

            if modo == "C":
                resultado = cifrar_vigenere(texto, clave)
                print(Fore.GREEN + "🔐 Texto cifrado (Vigenère): " + Fore.WHITE + resultado + "\n")
            elif modo == "D":
                resultado = descifrar_vigenere(texto, clave)
                print(Fore.BLUE + "🔓 Texto descifrado (Vigenère): " + Fore.WHITE + resultado + "\n")
            else:
                print(Fore.RED + "❌ Opción inválida.\n")

        # ===== CIFRADO ATBASH =====
        elif opcion == "3":
            escribir_lento("\nProcesando", Fore.MAGENTA)
            for _ in range(3):
                sys.stdout.write("."); sys.stdout.flush(); time.sleep(0.4)
            print("\n")

            resultado = cifrar_atbash(texto)
            print(Fore.GREEN + "🔐 Texto cifrado/descifrado (Atbash): " + Fore.WHITE + resultado + "\n")

if __name__ == "__main__":
    main()
