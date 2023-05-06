
from tkinter import *
from tkinter import messagebox

ventana_principal = Tk()

ventana_principal.title("Academico y Medico")
ventana_principal.geometry("900x900")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="medium turquoise")


#FRAME ACADEMICO
frame_academico = Frame(ventana_principal)
frame_academico.config(bg="alice blue", width=400, height=880)
frame_academico.place(x=10, y=10)


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

lb_TD = Label(frame_DRA, text ="Digite las notas de las siguientes asignaturas")
lb_TD.config(bg="alice blue", fg="black", font=("Times New Roman", 15))
lb_TD.place(x=5, y=10)

#CAJA DE TEXTO PARA INGRESAR LOS DATOS
entry_nota_materia = Entry(frame_DRA)
entry_nota_materia.config(bg="medium turquoise", fg="black", font=("Times New Roman", 18), width=10)
entry_nota_materia.focus_set()
entry_nota_materia.place(x=115,y=70)

ventana_principal.mainloop()