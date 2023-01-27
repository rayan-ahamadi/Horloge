from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from time import *
import datetime


window = Tk()
window.title("Horloge Python")
window.iconbitmap("")

temps = ""
isThereAlarm = False
tempsAlarme = ""
isHeureManuel = False
isHeureCreated = False



#fonction récursive
def timeManuel(): 
    global temps
    timeSplit = temps.split(":")
    heure = int(timeSplit[0])
    minute = int(timeSplit[1])
    seconde = int(timeSplit[2])
    seconde +=1

    if seconde == 60 : 
        seconde = "0"
        minute+=1

    if minute == 60 : 
        minute = "0"
        heure+=1

    if heure == 24 : 
        heure = "0"

    if int(heure) < 10 :
        heure = "0" + str(heure)
    elif int(minute) < 10  : 
        minute = "0" + str(minute)
    elif int(seconde) < 10 : 
        seconde = "0" + str(seconde)

    timeUpdate = str(heure) + ":" + str(minute) + ":" + str(seconde)
    temps = timeUpdate


def time(): 
    global isThereAlarm
    global tempsAlarme
    global isHeureManuel
    global temps

    if isHeureManuel == False : 
        temps = datetime.datetime.now().strftime('%H:%M:%S')
        txtAffichage.config(text=temps)
        #vérifie si il y a une alarme et si le temps est égale à l'heure de l'alarme
        if isThereAlarm == True and tempsAlarme == temps:
            messagebox.showwarning(title="Alarme", message="Il est " + temps)
            isThereAlarm = False
        #équivalent de la fonction sleep mais qui appelle la fonction time
        txtAffichage.after(1000,time)
    elif isHeureManuel and isHeureCreated : 
        txtAffichage.config(text=temps)
        timeManuel()
        #vérifie si il y a une alarme et si le temps est égale à l'heure de l'alarme
        if isThereAlarm == True and tempsAlarme == temps:
            messagebox.showwarning(title="Alarme", message="Il est " + temps)
            isThereAlarm = False
        #équivalent de la fonction sleep mais qui appelle la fonction time
        txtAffichage.after(1000,time)

    
    


#Fenêtre d'alarme
def alarme():
    global isThereAlarm
    isThereAlarm = False
    def initialiserAlarme():
        global isThereAlarm
        global tempsAlarme

        tuple = (heure.get(),minutes.get(),secondes.get())
        tempsAlarme = tuple[0] + ":" + tuple[1] + ":" + tuple[2]
        print(tempsAlarme)
        isThereAlarm = True
        alarm.destroy()


    alarm = Toplevel(window)

    Label(alarm, text="Alarme",font=("Arial",15)).grid(row=0,column=1,pady=5)

    comboBoxFrame = Frame(alarm)
    comboBoxFrame.grid(row=1,column=1)

    valueHeure = []
    valueMinutes= []
    valueSecondes= []

    for i in range(0,24): 
        if i < 10 : 
            valueHeure.append("0" + str(i))
        else:
            valueHeure.append(i)

    for i in range(0,61):
        if i < 10 : 
            valueMinutes.append("0" + str(i))
        else:
            valueMinutes.append(i)
    
    for i in range(0,61):
        if i < 10 : 
            valueSecondes.append("0" + str(i))
        else:
            valueSecondes.append(i)

    heure = ttk.Combobox(comboBoxFrame,values=valueHeure,state='readonly')
    minutes = ttk.Combobox(comboBoxFrame,values=valueMinutes,state='readonly')
    secondes = ttk.Combobox(comboBoxFrame,values=valueSecondes,state='readonly')
    
    heure.grid(row=1,column=0,padx=5)
    minutes.grid(row=1,column=1,padx=5)
    secondes.grid(row=1,column=2,padx=5)

    alarmButtonFrame = Frame(alarm)
    alarmButtonFrame.grid(row=2,column=1)
    btnOk = Button(alarmButtonFrame,text="Initialiser l'alarme",command=initialiserAlarme)
    btnAnnuler = Button(alarmButtonFrame,text="Annuler")
    btnOk.grid(row=2,column=0,pady=5,padx=5)
    btnAnnuler.grid(row=2,column=1,pady=5,padx=5)

def modeAffichage():
    formatWindow = Toplevel(window)
    Label(formatWindow,text="Mode d'affichage",font=("Arial",15)).grid(row=0,column=1,pady=5)
    frameFormat = Frame(formatWindow)
    frameFormat.grid(row=1,column=1)
    btn12heure = Button(frameFormat,text="format 12 heures")
    btn24heure = Button(frameFormat,text="format 24 heures")
    btn12heure.grid(row=1,column=0,padx=5,pady=5)
    btn24heure.grid(row=1,column=1,padx=5,pady=5)


def reglage():
    global isHeureManuel
    #Fonctions de la fenêtre
    def configComboBox(var):
        global isHeureManuel 
        if var == 1 : 
            heure.config(state="disabled")
            minutes.config(state="disabled")
            secondes.config(state="disabled")
            isHeureManuel = False 
        elif var == 2 : 
            heure.config(state="readonly")
            minutes.config(state="readonly")
            secondes.config(state="readonly")
            isHeureManuel = False

    def newTime(): 
            global isHeureCreated
            global isHeureManuel
            global temps 

            isHeureCreated = True
            isHeureManuel = True
            tupleHeure = (heure.get(),minutes.get(),secondes.get())
            newHeure = tupleHeure[0] + ":" + tupleHeure[1] + ":" + tupleHeure[2] 
            temps = str(newHeure)
            print(temps)
            reglage.destroy()
   


    ####################################



    reglage = Toplevel(window)
    Label(reglage, text="Réglage",font=("Arial",15)).grid(row=0,column=1,pady=5)

    comboBoxFrame = Frame(reglage)
    comboBoxFrame.grid(row=1,column=1)

    valueHeure = []
    valueMinutes= []
    valueSecondes=[]

    for i in range(0,24): 
        if i < 10 : 
            valueHeure.append("0" + str(i))
        else:
            valueHeure.append(i)

    for i in range(0,61):
        if i < 10 : 
            valueMinutes.append("0" + str(i))
        else:
            valueMinutes.append(i)
    
    for i in range(0,61):
        if i < 10 : 
            valueSecondes.append("0" + str(i))
        else:
            valueSecondes.append(i)

    
        
    heure = ttk.Combobox(comboBoxFrame,values=valueHeure)
    minutes = ttk.Combobox(comboBoxFrame,values=valueMinutes)
    secondes = ttk.Combobox(comboBoxFrame,values=valueSecondes)

    var = IntVar()
    radioHeureSysteme = Radiobutton(comboBoxFrame,variable=var,text="Heure du système",value=1,command= lambda : configComboBox(1))
    radioHeureManuel = Radiobutton(comboBoxFrame,variable=var,text="Heure Manuel",value=2,command=lambda : configComboBox(2))

    if isHeureManuel == False : 
        radioHeureSysteme.invoke()
    else: 
        radioHeureManuel.invoke()

    radioHeureSysteme.grid(row=1,column=0,padx=5)
    radioHeureManuel.grid(row=1,column=1,padx=5)
    heure.grid(row=2,column=0,padx=5)
    minutes.grid(row=2,column=1,padx=5)
    secondes.grid(row=2,column=2,padx=5)
    
    reglageButtonFrame = Frame(reglage)
    reglageButtonFrame.grid(row=2,column=1)
    btnOk = Button(reglageButtonFrame,text="Changer l'heure",command= lambda:newTime())
    btnAnnuler = Button(reglageButtonFrame,text="Annuler")
    btnOk.grid(row=2,column=0,pady=5,padx=5)
    btnAnnuler.grid(row=2,column=1,pady=5,padx=5)



txtAffichage = Label(window,font=('Arial',90),foreground="black",bg="cyan")
txtAffichage.grid(row=0)
time()

btnFrame = Frame(window)
btnFrame.grid(row=1)
btnAlarme = Button(btnFrame, text="Alarme",command= alarme)
btnAlarme.grid(row=1, column=0,padx=25,pady=10,ipady=10,ipadx=5)

btnReglage = Button(btnFrame,text="Reglage",command=reglage)
btnReglage.grid(row=1, column=1,padx=25,pady=10,ipady=10,ipadx=5)

btnAffichage = Button(btnFrame, text="Format d'affichage",command=modeAffichage)
btnAffichage.grid(row=1, column=2,padx=25,pady=10,ipady=10,ipadx=5)


window.mainloop()
