from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from time import *
import datetime


window = Tk()
window.title("Horloge Python")
window.iconbitmap("icone.ico")

temps = ""
isThereAlarm = False
tempsAlarme = ""
isHeureCreated = False



#Fonction qui incrémenter les secondes,minutes et heures de la variable temps 
#à chaque fois qu'elle est appellé
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

#fonction récursive
def time(): 
    global isThereAlarm
    global tempsAlarme
    global temps
    global isHeureCreated

    if isHeureCreated == False : 
        temps = datetime.datetime.now().strftime('%H:%M:%S')
        txtAffichage.config(text=temps)
        #vérifie si il y a une alarme et si le temps est égale à l'heure de l'alarme
        if isThereAlarm == True and tempsAlarme == temps:
            messagebox.showwarning(title="Alarme", message="Il est " + temps)
            isThereAlarm = False
        #équivalent de la fonction sleep mais qui re-appelle la fonction time
        txtAffichage.after(1000,time)
    elif isHeureCreated == True : 
        txtAffichage.config(text=temps)
        timeManuel()
        if isThereAlarm == True and tempsAlarme == temps:
            messagebox.showwarning(title="Alarme", message="Il est " + temps)
            isThereAlarm = False
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

#Fenêtre réglage
def reglage():
    def configComboBox(var):
        global isHeureCreated
        if var == 1 : 
            heure.config(state="disabled")
            minutes.config(state="disabled")
            secondes.config(state="disabled")
            isHeureCreated = False
        elif var == 2 : 
            heure.config(state="readonly")
            minutes.config(state="readonly")
            secondes.config(state="readonly")

    def newTime(): 
            global isHeureCreated
            global temps 

            isHeureCreated = True
            tupleHeure = (heure.get(),minutes.get(),secondes.get())
            newHeure = tupleHeure[0] + ":" + tupleHeure[1] + ":" + tupleHeure[2] 
            temps = str(newHeure)
            print(temps)
            reglage.destroy()
   
    def annuler(): 
        reglage.destroy()


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

    if isHeureCreated == False : 
        radioHeureSysteme.invoke()
    elif isHeureCreated == True: 
        radioHeureManuel.invoke()

    radioHeureSysteme.grid(row=1,column=0,padx=5)
    radioHeureManuel.grid(row=1,column=1,padx=5)
    heure.grid(row=2,column=0,padx=5)
    minutes.grid(row=2,column=1,padx=5)
    secondes.grid(row=2,column=2,padx=5)
    
    reglageButtonFrame = Frame(reglage)
    reglageButtonFrame.grid(row=2,column=1)
    btnOk = Button(reglageButtonFrame,text="Changer l'heure",command= lambda:newTime())
    btnAnnuler = Button(reglageButtonFrame,text="Annuler",command= lambda:annuler())
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


window.mainloop()