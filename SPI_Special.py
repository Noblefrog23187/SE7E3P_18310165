import tkinter as tk
from tkinter import messagebox
import json

# Cargar o inicializar redes de inferencia
try:
    with open("redes_inferencia.json", "r") as file:
        redes_inferencia = json.load(file)
except FileNotFoundError:
    redes_inferencia = {}

# Funcion para guardar las redes de inferencia
def guardar_redes():
    with open("redes_inferencia.json", "w") as file:
        json.dump(redes_inferencia, file, indent=4)

# Funcion para mostrar detalles de una opcion
def mostrar_detalles(titulo, texto):
    detalles_ventana = tk.Toplevel(root)
    detalles_ventana.title(titulo)
    detalles_ventana.geometry("600x400")
    
    tk.Label(detalles_ventana, text=titulo, font=("Arial", 16, "bold"), pady=10).pack()
    texto_area = tk.Text(detalles_ventana, wrap=tk.WORD, font=("Arial", 12), padx=10, pady=10, height=15, width=70)
    texto_area.insert(tk.END, texto)
    texto_area.config(state=tk.DISABLED)
    texto_area.pack()
    tk.Button(detalles_ventana, text="Cerrar", command=detalles_ventana.destroy).pack(pady=10)

# Funcion para manejar opciones
current_menu = []
def mostrar_menu(titulo, opciones):
    global current_menu

    def manejar_seleccion(opcion):
        if opcion == "Volver":
            mostrar_menu(*current_menu[-1])
            current_menu.pop()
        elif opcion == "Salir":
            root.quit()
        elif opcion in redes_inferencia:
            current_menu.append((titulo, opciones))
            mostrar_menu(opcion, list(redes_inferencia[opcion].keys()))
        elif titulo in redes_inferencia and opcion in redes_inferencia[titulo]:
            mostrar_detalles(opcion, redes_inferencia[titulo][opcion])
        else:
            messagebox.showerror("Error", f"No se encontro informacion para {opcion}.")

    # Limpiar la ventana
    for widget in root.winfo_children():
        widget.destroy()

    # Titulo del menu
    tk.Label(root, text=titulo, font=("Arial", 16, "bold"), pady=10).pack()

    # Botones para las opciones
    for opcion in opciones:
        tk.Button(root, text=opcion, font=("Arial", 12), command=lambda o=opcion: manejar_seleccion(o)).pack(pady=5)

# Estructura inicial de la interfaz
def iniciar_diagnostico():
    mostrar_menu("Bienvenido al sistema de diagnostico de fallas", [
        "Horno Rational",
        "Elevador Modificado",
        "Lavadora Modificada",
        "Lavaloza Modificada",
        "Salir",
    ])

# Configuracion de la ventana principal
root = tk.Tk()
root.title("Sistema de Diagnostico de Fallas")
root.geometry("600x400")

# Inicializar el sistema
iniciar_diagnostico()

# Ejecutar la aplicacion
root.mainloop()

# Guardar las redes al cerrar
guardar_redes()
