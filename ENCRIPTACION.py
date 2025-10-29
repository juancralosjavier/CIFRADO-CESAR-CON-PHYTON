import time
import sys
from colorama import Fore, Style, init
import unicodedata

# Inicializar colorama
init(autoreset=True)

# Alfabeto español extendido
ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def limpiar_texto(texto):
    """Normaliza el texto eliminando acentos y convirtiendo a mayúsculas."""
    texto = texto.upper()
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    return texto

def cifrar(texto, desplazamiento):
    """Cifra el texto usando el cifrado César con alfabeto español."""
    texto = limpiar_texto(texto)
    resultado = ""
    for c in texto:
        if c in ALFABETO:
            nueva_pos = (ALFABETO.index(c) + desplazamiento) % len(ALFABETO)
            resultado += ALFABETO[nueva_pos]
        else:
            resultado += c
    return resultado

def descifrar(texto, desplazamiento):
    """Descifra el texto cifrado."""
    return cifrar(texto, -desplazamiento)

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
    print("║                  🔐 CIFRADO CÉSAR 2.0 🔐                  ║")
    print("║  Israel Ibañez Arteaga Juan Carlos Javier Padilla          ║")
    print("╚════════════════════════════════════════════════════════════╝\n")
    print(Style.RESET_ALL)

def main():
    banner()

    while True:
        print(Fore.YELLOW + "1. Cifrar texto")
        print("2. Descifrar texto")
        print("3. Salir\n")

        opcion = input(Fore.CYAN + "👉 Elige una opción (1-3): " + Style.RESET_ALL)

        if opcion == "3":
            escribir_lento("\n👋 Saliendo del programa... ¡Hasta pronto!\n", Fore.MAGENTA)
            break

        if opcion not in ["1", "2"]:
            print(Fore.RED + "❌ Opción no válida. Intenta nuevamente.\n")
            continue

        texto = input(Fore.WHITE + "\n📝 Escribe el texto: " + Style.RESET_ALL)
        try:
            desplazamiento = int(input(Fore.WHITE + "🔢 Desplazamiento (número): " + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + "❌ Error: Debes ingresar un número válido.\n")
            continue

        escribir_lento("\nProcesando", Fore.MAGENTA)
        for _ in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.4)
        print("\n")

        if opcion == "1":
            resultado = cifrar(texto, desplazamiento)
            print(Fore.GREEN + "🔐 Texto cifrado: " + Fore.WHITE + resultado + "\n")
        else:
            resultado = descifrar(texto, desplazamiento)
            print(Fore.BLUE + "🔓 Texto descifrado: " + Fore.WHITE + resultado + "\n")

if __name__ == "__main__":
    main()
