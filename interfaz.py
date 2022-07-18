from CalculadoraBinaria import CalculadoraBinaria
from tkinter import *

def actualizar_variables():#Actualiza las variables necesarias para el cálculo
    global ordenador

    ordenador=CalculadoraBinaria(int(long_mantisa.get()),int(long_exp.get()))
    sesgo.set(str(ordenador.sesgo))
    maximo.set(str(ordenador.calcular_maximo()))
    minimo.set(str(ordenador.calcular_min()))
    epsilon.set(str(ordenador.calcular_epsilon()))

    delete_button.config(state=NORMAL)
    act_button.config(state=DISABLED)

    num_dec_entry.config(state=NORMAL)
    palabra_entry.config(state=NORMAL)
    convertir_a_IEEE.config(state=NORMAL)
    convertir_a_dec.config(state=NORMAL)

def borrar():#Borra las variables para crear un nuevo ordenador
    global ordenador
    ordenador=None
    sesgo.set("")
    maximo.set("")
    minimo.set("")
    epsilon.set("")
    dec.set("")
    pal.set("")
    palabraIEEE.set("")
    palabra_conv.set("")

    delete_button.config(state=DISABLED)
    act_button.config(state=NORMAL)

    num_dec_entry.config(state=DISABLED)
    palabra_entry.config(state=DISABLED)
    convertir_a_IEEE.config(state=DISABLED)
    convertir_a_dec.config(state=DISABLED)

def conv_IEEE():#convierte el numero decimal a formato IEEE
    num_a_convertir=float(dec.get())
    num_convertido=ordenador.convertir_formato_IEEE(num_a_convertir)
    palabraIEEE.set(num_convertido)

def conv_dec():#convierte la palabra a decimal
    pal_a_convertir=pal.get()
    num_convertido=ordenador.palabra_a_decimal(pal_a_convertir)
    palabra_conv.set(num_convertido)

ordenador=None
root = Tk()

#Variables para los cuadro de texto
long_mantisa=StringVar()
long_exp=StringVar()
sesgo=StringVar()
maximo=StringVar()
minimo=StringVar()
epsilon=StringVar()
dec=StringVar()
pal=StringVar()
palabraIEEE=StringVar()
palabra_conv=StringVar()

#SETUP
root.title("FORMATO IEEE")
root.geometry("400x600")
root.config(bg="gray")

#Cuadro Longitud de Mantisa
title1=Label(root, text="Long. Mantisa:")
title1.place(x=80,y=0)
mantisa_entry=Entry(root,textvariable=long_mantisa)
mantisa_entry.place(x=200,y=0)

#Cuadro Longitud de exponentes
title2=Label(root, text="Long. Exponente:")
title2.place(x=80,y=30)
exp_entry=Entry(root,textvariable=long_exp)
exp_entry.place(x=200,y=30)

#Boton para crear ordenador
act_button=Button(root,text="Crear ordenador",
                  command=actualizar_variables)
act_button.place(x=80,y=60)

#Boton para borrar el actual y crear uno nuevo
delete_button=Button(root,text="Eliminar Ordenador",
                     state=DISABLED
                     ,command=borrar)
delete_button.place(x=200,y=60)

#Cuadro sesgo
title5=Label(root, text="Sesgo")
title5.place(x=80,y=150)
ses_entry=Entry(root, justify=CENTER,state="readonly",textvariable=sesgo)
ses_entry.place(x=200,y=150)
#Cuadro valor máximo
title5=Label(root, text="Valor máximo")
title5.place(x=80,y=180)
max_entry=Entry(root, justify=CENTER,state="readonly",textvariable=maximo)
max_entry.place(x=200,y=180)

#Cuadro valor mínimo
title5=Label(root, text="Valor mínimo")
title5.place(x=80,y=210)
min_entry=Entry(root, justify=CENTER,state="readonly",textvariable=minimo)
min_entry.place(x=200,y=210)

#Cuadro epsilon
title5=Label(root, text="Epsilon")
title5.place(x=80,y=240)
eps_entry=Entry(root, justify=CENTER,state="readonly",textvariable=epsilon)
eps_entry.place(x=200,y=240)


#Cuadro decimal a convertir
title3=Label(root, text="Número decimal:")
title3.place(x=80,y=330)
num_dec_entry=Entry(root,textvariable=dec,state=DISABLED)
num_dec_entry.place(x=200,y=330)

#Cuadro palabra a convertir
title4=Label(root, text="Palabra:")
title4.place(x=90,y=420)
palabra_entry=Entry(root,textvariable=pal,state=DISABLED)
palabra_entry.place(x=200,y=420)


#Boton para convertir decimal a palabra IEEE
convertir_a_IEEE=Button(root, text="Convertir IEEE", command=conv_IEEE,state=DISABLED)
convertir_a_IEEE.place(x=80,y=360)

IEEE_entry=Entry(root, justify=CENTER,textvariable=palabraIEEE,state="readonly")
IEEE_entry.place(x=200,y=360)

#Boton para convertir palabra IEEE a decimal
convertir_a_dec=Button(root, text="Convertir a decimal", command=conv_dec,state=DISABLED)
convertir_a_dec.place(x=80,y=450)

dec_entry=Entry(root, justify=CENTER,textvariable=palabra_conv,state="readonly")
dec_entry.place(x=200,y=450)

# Finalmente bucle de la aplicación
root.mainloop()