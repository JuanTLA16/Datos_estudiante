
from tkinter import *
from tkinter import messagebox


def calcular_promedio():
    messagebox.showinfo("ACADEMICO", "SU PROMEDIO SERÁ CALCULADO")
    quimica = float(entry_quimica.get())
    calculo = float(entry_calculo.get())
    algebra = float(entry_algebra.get())
    programacion = float(entry_programacion.get())

    notas_materia = quimica + calculo + algebra + programacion
    promedio = notas_materia / 4

    if promedio < 3.0:
        t_resultados.insert(INSERT,f"Tu promedio es de " + str(promedio) + " vas perdiendo.")
    else:
        t_resultados.insert(INSERT,f"Tu promedio es de " + str(promedio) + " vas pasando.")

def calcular_IMC():
    messagebox.showinfo("MEDICO","SU IMC SERÁ CALCULADO")
    peso = float(entry_peso.get())
    altura = float(entry_altura.get())

    imc = peso / altura ** 2
     
    if ( imc  < 16):
        t_resultados_IMC.insert(INSERT,f" Criterio de ingreso en el hospital ")
    elif ( 16 < imc  < 17 ):
        t_resultados_IMC.insert(INSERT,f"  INFRAPESO ")
    elif ( 17 < imc  < 18):
        t_resultados_IMC.insert(INSERT,f"  BAJO PESO")
    elif ( 18 < imc  < 25):
        t_resultados_IMC.insert(INSERT,f" SALUDABLE")
    elif ( 25 < imc < 30):
        t_resultados_IMC.insert(INSERT,f" OBESIDAD GRADO I")
    elif ( 30 < imc < 35):
        t_resultados_IMC.insert(INSERT,f" OBESIDAD GRADO II")
    elif ( 35 < imc  < 40):
        t_resultados_IMC.insert(INSERT,f" OBESIDAD GRADO III")
    elif ( imc  > 40):
        t_resultados_IMC.insert(INSERT,f" OBESIDAD GRADO IV")   
    

def borrar_datos():
    entry_quimica.delete(0, END)
    entry_calculo.delete(0, END)
    entry_algebra.delete(0, END)
    entry_programacion.delete(0, END)
    entry_peso.delete(0, END)
    entry_altura.delete(0, END)
    t_resultados.delete('1.0', END)
    t_resultados_IMC.delete('1.0', END)
   
        
ventana_principal = Tk()



ventana_principal.title("Academico y Medico")
ventana_principal.geometry("900x900")
ventana_principal.config(bg="medium turquoise")
ventana_principal.resizable(0,0)


#VARIABLE
var = StringVar()

##############FRAME ACADEMICO####################
frame_academico = Frame(ventana_principal)
frame_academico.config(bg="alice blue", width=400, height=880)
frame_academico.place(x=15, y=10)


#FRAME TITULO ACADEMICO
frame_titulo_academico = Frame(frame_academico)
frame_titulo_academico.config(bg="alice blue", width=400, height=60)
frame_titulo_academico.place(x=10, y=10)

lb_academico = Label(frame_academico, text ="              ACADEMICO")
lb_academico.config(bg="alice blue", fg="black", font=("Times New Roman", 20))
lb_academico.place(x=10, y=10)

#FRAME DATOS Y RESULTADOS ACADEMICOS
frame_DRA = Frame(frame_academico)
frame_DRA.config(bg="sky blue", width=360, height=800)
frame_DRA.place(x=20, y=60)

lb_DRA = Label(frame_academico, text ="")
lb_DRA.config(bg="white", fg="black", font=("Times New Roman", 20))
lb_DRA.place(x=200, y=800)

#FRAME TITULO DATOS 
frame_TD= Frame(frame_DRA)
frame_TD.config(bg="alice blue", width=1, height=10)
frame_TD.place(x=10, y=10)

lb_TD = Label(frame_DRA, text ="NOTAS")
lb_TD.config(bg="alice blue", fg="black", font=("Times New Roman", 15))
lb_TD.place(x=145, y=10)

#CAJA DE TEXTO PARA INGRESAR LOS DATOS
entry_quimica = Entry(frame_DRA)
entry_quimica.config(bg="medium turquoise", fg="black", font=("Times New Roman", 18), width=10)
entry_quimica.focus_set()
entry_quimica.place(x=115,y=100)

entry_calculo = Entry(frame_DRA)
entry_calculo.config(bg="medium turquoise", fg="black", font=("Times New Roman", 18), width=10)
entry_calculo.focus_set()
entry_calculo.place(x=115,y=190)

entry_algebra = Entry(frame_DRA)
entry_algebra.config(bg="medium turquoise", fg="black", font=("Times New Roman", 18), width=10)
entry_algebra.focus_set()
entry_algebra.place(x=115,y=280)

entry_programacion = Entry(frame_DRA)
entry_programacion.config(bg="medium turquoise", fg="black", font=("Times New Roman", 18), width=10)
entry_programacion.focus_set()
entry_programacion.place(x=115,y=370)



#FRAME TITULO QUIMICA
frame_TD= Frame(frame_DRA)
frame_TD.config(bg="sky blue", width=1, height=10)
frame_TD.place(x=10, y=10)

lb_TD = Label(frame_DRA, text ="QUIMICA")
lb_TD.config(bg="sky blue", fg="black", font=("Times New Roman", 15))
lb_TD.place(x=135, y=60)


#FRAME TITULO CALCULO I
frame_TD= Frame(frame_DRA)
frame_TD.config(bg="sky blue", width=1, height=10)
frame_TD.place(x=10, y=10)

lb_TD = Label(frame_DRA, text ="CALCULO I")
lb_TD.config(bg="sky blue", fg="black", font=("Times New Roman", 15))
lb_TD.place(x=125, y=150)

#FRAME TITULO ALGEBRA LINEAL
frame_TD= Frame(frame_DRA)
frame_TD.config(bg="sky blue", width=1, height=10)
frame_TD.place(x=10, y=10)

lb_TD = Label(frame_DRA, text ="ALGEBRA LINEAL")
lb_TD.config(bg="sky blue", fg="black", font=("Times New Roman", 15))
lb_TD.place(x=90, y=240)

#FRAME TITULO PROGRAMACION
frame_TD= Frame(frame_DRA)
frame_TD.config(bg="sky blue", width=1, height=10)
frame_TD.place(x=10, y=10)

lb_TD = Label(frame_DRA, text ="PROGRAMACION")
lb_TD.config(bg="sky blue", fg="black", font=("Times New Roman", 15))
lb_TD.place(x=90, y=330)

#FRAME RESULTADOS




t_resultados = Text(frame_DRA)
t_resultados.config(bg="white", fg="black", font=("Times New Roman", 12))
t_resultados.place(x=60,y=480,width=240,height=50)




#BOTON CALCULAR ACADEMICO
boton_calcular = Button(frame_DRA, text="CALCULAR", command=calcular_promedio)
boton_calcular.config(bg="white", fg="black", font=("Times New Roman", 10))
boton_calcular.place(x=90,y=420)





#################FRAME MEDICO##################
frame_medico= Frame(ventana_principal)
frame_medico.config(bg="alice blue", width=430, height=880)
frame_medico.place(x=450, y=10)

#FRAME TITULO MEDICO
frame_titulo_medico = Frame(frame_medico)
frame_titulo_medico.config(bg="alice blue", width=400, height=60)
frame_titulo_medico.place(x=10, y=10)

lb_medico = Label(frame_medico, text ="                       MEDICO")
lb_medico.config(bg="alice blue", fg="black", font=("Times New Roman", 20))
lb_medico.place(x=10, y=10)

#FRAME DATOS Y RESULTADOS MEDICO
frame_DRAM = Frame(frame_medico)
frame_DRAM.config(bg="sky blue", width=390, height=800)
frame_DRAM.place(x=20, y=60)

lb_DRAM = Label(frame_academico, text ="")
lb_DRAM.config(bg="white", fg="black", font=("Times New Roman", 20))
lb_DRAM.place(x=200, y=800)

#FRAME TITULO DATOS 
frame_TD= Frame(frame_DRAM)
frame_TD.config(bg="alice blue", width=1, height=10)
frame_TD.place(x=10, y=10)

lb_TD = Label(frame_DRAM, text ="DIGITE SU PESO EN (KG)")
lb_TD.config(bg="alice blue", fg="black", font=("Times New Roman", 15))
lb_TD.place(x=85, y=20)

frame_TD= Frame(frame_DRAM)
frame_TD.config(bg="alice blue", width=1, height=10)
frame_TD.place(x=10, y=10)

lb_TD = Label(frame_DRAM, text ="DIGITE SU ALTURA EN (M))")
lb_TD.config(bg="alice blue", fg="black", font=("Times New Roman", 15))
lb_TD.place(x=70, y=120) 


#ETIQUETA IMAGENES IMC

IMC_img = PhotoImage(file="img/IMC.png")
lb_IMC_img= Label(frame_DRAM, image=IMC_img, bg="white", width=160, height=150)
lb_IMC_img.place(x=110, y=240)

#CAJA DE TEXTO PARA INGRESAR LOS DATOS
entry_peso = Entry(frame_DRAM)
entry_peso.config(bg="medium turquoise", fg="black", font=("Times New Roman", 18), width=20)
entry_peso.focus_set()
entry_peso.place(x=80,y=60)

entry_altura = Entry(frame_DRAM)
entry_altura.config(bg="medium turquoise", fg="black", font=("Times New Roman", 18), width=20)
entry_altura.focus_set()
entry_altura.place(x=80,y=170)


#FRAME RESULTADOS
t_resultados_IMC = Text(frame_DRAM)
t_resultados_IMC.config(bg="white", fg="black", font=("Times New Roman", 12))
t_resultados_IMC.place(x=70,y=480,width=240,height=50)


#BOTON CALCULAR MEDICO
bt_calcular_IMC = Button(frame_DRAM, text="Calcular IMC", command=calcular_IMC)
bt_calcular_IMC.config(bg="white", fg="black", font=("Times New Roman", 10))
bt_calcular_IMC.place(x=90, y=420)



bt_BORRAR_IMC = Button(frame_DRAM, text="REINICIAR", command=borrar_datos)
bt_BORRAR_IMC.config(bg="white", fg="black", font=("Times New Roman", 10))
bt_BORRAR_IMC.place(x=210, y=420)

bt_BORRAR_DATOS = Button(frame_DRA, text="REINICIAR" , command=borrar_datos)
bt_BORRAR_DATOS.config(bg="white", fg="black", font=("Times New Roman", 10))
bt_BORRAR_DATOS.place(x=180, y=420)

ventana_principal.mainloop()