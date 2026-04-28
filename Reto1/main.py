from pywinauto import Application
import pyautogui
import time

def espaciador():
    print("\n" + "-"*50 + "\n")

def abrir_notepad(message):
    # Start Notepad
    app = Application(backend="win32").start("notepad.exe")

    time.sleep(1)

    app.window(title_re="Sin título")

    pyautogui.write(message)

def menu_notepad():
    print("1. Escribir mensaje en Notepad")
    print("2. Usar mensaje predefinido")
    choice = input("Seleccione una opción: ")
    if choice == "1":

        message = input("Ingrese el mensaje que desea escribir en Notepad > ")
        abrir_notepad(message)

    elif choice == "2":
        abrir_notepad("Hello world! This is a predefined message.")
    else:
        print("Opción no válida. Intente de nuevo.")
        menu_notepad()

def menu():
    print("1. Abrir Notepad (Ejecuta automatización en notepad)")
    print("2. Salir \ Cerrar programa")
    choice = input("Seleccione una opción: ")
    if choice == "1":
        espaciador()
        menu_notepad()
    elif choice == "2":
        print("Saliendo...")
    else:
        print("Opción no válida. Intente de nuevo.")
        menu()

if __name__ == "__main__":
    menu()
    