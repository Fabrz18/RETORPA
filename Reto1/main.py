from pywinauto import Application
import pyautogui, subprocess
import time

def espaciador():
    print("\n" + "-"*50 + "\n")

def abrir_notepad(message):
    # Start Notepad
    app = Application(backend="win32").start("notepad.exe")

    time.sleep(1)

    app.window(title_re="Sin título")

    pyautogui.write(message)
    pyautogui.hotkey('ctrl', 's')
    pyautogui.hotkey('enter')


def menu_notepad():
    print("1. Escribir mensaje en Notepad")
    print("2. Usar mensaje predefinido")
    choice = input("Seleccione una opción: ")
    if choice == "1":

        message = input("Ingrese el mensaje que desea escribir en Notepad > ")
        abrir_notepad(message)

    elif choice == "2":
        message = """
        Automatic tittle: "Hello world! This is a predefined message.
        You can edit this message in the code if you want to change it.
        Review my github: Fabrz18
        """
        abrir_notepad(message)
    else:
        print("Opción no válida. Intente de nuevo.")
        menu_notepad()

def abrir_chrome():
    subprocess.Popen(['start', 'chrome', "https://www.bitraid.lat/"], shell=True)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'a')

def menu():
    print("1. Abrir Notepad (Ejecuta automatización en notepad)")
    print("2. Abrir Chrome (Ejecuta automatización en chrome)")
    print("3. Salir \ Cerrar programa")
    choice = input("Seleccione una opción: ")
    if choice == "1":
        espaciador()
        menu_notepad()
    elif choice == "2":
        espaciador()
        abrir_chrome()
    elif choice == "3":
        print("Saliendo...")
    else:
        print("Opción no válida. Intente de nuevo.")
        menu()

if __name__ == "__main__":
    menu()
    