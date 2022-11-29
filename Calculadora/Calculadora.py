from tkinter import *

ventana = Tk()

def btnClick(num):
    global operador
    operador = operador+str(num)
    input_text.set(operador)

def resultado():
    global operador
    try:
        opera = str(eval(operador))
        input_text.set(opera)
    except:
        input_text.set("Error")
    operador =""

def clear():
    global operador
    operador = ("")
    input_text.set("0")

input_text=StringVar()
operador = ""
#formato
ventana.title("Mi primer calculadora")
ventana.configure(background="gray1")
ventana.iconbitmap("cal.ico")


anchoBoton = 12
altoBoton  = 4
colorBoton = ("slateBlue1")
colornumero = ("#ffffff")
fon = ("arial",12,"bold")

display=Entry(font=("arial",20,"bold"),foreground="#ffffff",bd=20,insertwidth=7,bg="grey1",justify="right",textvariable=input_text)
display.grid(row=0,column=0,columnspan=5,sticky=(W,E))






 

Button(ventana,text="AC",font=fon,foreground="grey1",bg="#D4D4D2",width=anchoBoton,height=altoBoton,command=lambda:clear()).grid(row=1,column=0)
Button(ventana,text="+/-",font=fon,foreground="grey1",bg="#D4D4D2",width=anchoBoton,height=altoBoton,command=lambda:btnClick("+")).grid(row=1,column=1)
Button(ventana,text="%",font=fon,foreground="grey1",bg="#D4D4D2",width=anchoBoton,height=altoBoton,command=lambda:btnClick("+")).grid(row=1,column=2)
Button(ventana,text="/",font=fon,foreground=colornumero,bg="#FF9500",width=anchoBoton,height=altoBoton,command=lambda:btnClick("/")).grid(row=1,column=3)



Button(ventana,text=7,font=fon,foreground=colornumero,bg="#505050",width=anchoBoton,height=altoBoton,command=lambda:btnClick(7)).grid(row=2,column=0)
Button(ventana,text=8,font=fon,foreground=colornumero,bg="#505050",width=anchoBoton,height=altoBoton,command=lambda:btnClick(8)).grid(row=2,column=1)
Button(ventana,text=9,font=fon,foreground=colornumero,bg="#505050",width=anchoBoton,height=altoBoton,command=lambda:btnClick(9)).grid(row=2,column=2)
Button(ventana,text="x",font=fon,foreground=colornumero,bg="#FF9500",width=anchoBoton,height=altoBoton,command=lambda:btnClick("*")).grid(row=2,column=3)




Button(ventana,text=4,font=fon,foreground=colornumero,bg="#505050",width=anchoBoton,height=altoBoton,command=lambda:btnClick(4)).grid(row=3,column=0)
Button(ventana,text=5,font=fon,foreground=colornumero,bg="#505050",width=anchoBoton,height=altoBoton,command=lambda:btnClick(5)).grid(row=3,column=1)
Button(ventana,text=6,font=fon,foreground=colornumero,bg="#505050",width=anchoBoton,height=altoBoton,command=lambda:btnClick(6)).grid(row=3,column=2)
Button(ventana,text="-",font=fon,foreground=colornumero,bg="#FF9500",width=anchoBoton,height=altoBoton,command=lambda:btnClick("-")).grid(row=3,column=3)




Button(ventana,text=1,font=fon,foreground=colornumero,bg="#505050",width=anchoBoton,height=altoBoton,command=lambda:btnClick(1)).grid(row=4,column=0)
Button(ventana,text=2,font=fon,foreground=colornumero,bg="#505050",width=anchoBoton,height=altoBoton,command=lambda:btnClick(2)).grid(row=4,column=1)
Button(ventana,text=3,font=fon,foreground=colornumero,bg="#505050",width=anchoBoton,height=altoBoton,command=lambda:btnClick(3)).grid(row=4,column=2)
Button(ventana,text="+",font=fon,foreground=colornumero,bg="#FF9500",width=anchoBoton,height=altoBoton,command=lambda:btnClick("+")).grid(row=4,column=3)




Button(ventana,text=0,font=fon,foreground=colornumero,bg="#505050",width=anchoBoton,height=altoBoton,command=lambda:btnClick(0)).grid(row=5,column=0,columnspan=2,sticky=(W,E))
Button(ventana,text=".",font=fon,foreground=colornumero,bg="#505050",width=anchoBoton,height=altoBoton,command=lambda:btnClick(".")).grid(row=5,column=2)
Button(ventana,text="=",font=fon,foreground=colornumero,bg="#FF9500",width=anchoBoton,height=altoBoton,command=lambda:resultado()).grid(row=5,column=3)





ventana.mainloop()