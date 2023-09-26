#importar librerías
import tkinter as tk

def convertir_a_celsius():
    Far = float(entry1.get())
    Cel = (Far - 32) * 5.0/9.0
    entry2.delete(0,tk.END)
    entry2.insert(0,f"{Cel:.2f}")

def convertir_a_Farenheits():
    Cel = float(entry2.get())
    Far = (Cel*9/5)+ +32
    entry1.delete(0,tk.END)
    entry1.insert(0,f"{Far:.2f}")
def borrar():
    entry1.delete(0,tk.END)
    entry2.delete(0,tk.END)

#Creación de la ventana
ventana = tk.Tk()
ventana.title("Convertidor de Farenheits a Celsius y Celsius a Farenheits")

#Creación de Label Farenheits
label1 = tk.Label(ventana,text="Farenheits")
label1.grid(row=0,column=1)

#Creación de cuadro de texto de entrada Farenheits
entry1 = tk.Entry(ventana)
entry1.grid(row=0,column=2)

#Creación de botón calcular Celsius
button1 = tk.Button(ventana, text = "Convertir a Celsius", command= convertir_a_celsius)
button1.grid(row = 0, column = 3)

#Creación de Label Celsius
label2 = tk.Label(ventana,text="Celsius")
label2.grid(row=1,column=1)

#Creación cuadro de texto de entrada Celsius
entry2 = tk.Entry(ventana)
entry2.grid(row=1,column=2)

#Creación de botón calcular Farenheits
button2 = tk.Button(ventana, text = "Convertir a Farenheits", command = convertir_a_Farenheits)
button2.grid(row = 1, column = 3)

#Creación botón restablecer
#Creación de botón calcular Celsius
button3 = tk.Button(ventana, text = "Restablecer", command = borrar)
button3.grid(row = 2, column = 2)


ventana.mainloop()