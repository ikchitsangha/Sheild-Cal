## Here we are importing all the required libraries ## 
import math
from tkinter import *
import tkinter as tk
from tkinter import ttk
#################################



##############    we define a container "root" in which all of our graphical objects will be placed       ####################    
root=Tk()                                         
root.title("Primary Wall Shielding CALc")            ## giving title to our container  ##


	
def help():                 ## defining function "help" for displaying contact 
	helpW=Tk()              ## container defined ## 
	helpW.title("Help")     ## tittle given  ##
	msg=Label(helpW,text="\n contact:ikchitsangha@gmail.com")
	msg.pack()                        
	helpW.geometry("300x100+330+100") 



menubar = Menu(root,bg='grey')
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Help", command=help)
menubar.add_cascade(label="File", menu=filemenu)

'''editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="ASYMETRIC", command=asm)
menubar.add_cascade(label="JAWS", menu=editmenu)
'''

label1=Label(root,text='Workload (Gy/Wk)-->',bg='grey', fg='black',font=('Arial',11))
label1.place(x=1,y=10)											
Workload =Entry(root, fg='blue',width=6,font=('Arial',12,'bold'))           
Workload.place(x=140,y=10)

label2=Label(root,text='Distance(Meters) -->',bg='grey', fg='black',font=('Arial',11))
label2.place(x=210,y=10)										
Distance =Entry(root, fg='blue', width=6,font=('Arial',12,'bold'))
Distance.place(x=370,y=10)

 
label3=Label(root,text='Energy -->',bg='grey', fg='black',font=('Arial',11))
label3.place(x=440,y=10)									
Enr = {'none':1, '4 Mv':4, '6 Mv':6, '10 Mv':10 }   
selectedE = tk.StringVar()
Er = ttk.Combobox(root, textvariable=selectedE, width=8,font=('Arial',12,'bold'))
Er ['values'] = list(Enr.keys())
Er.current(0)
Er.place(x=550,y=10)

line=Label(root,text="  _________________________________________________________________________________________________________________________",bg='grey',font=('Arial',12,'bold'))
line.place(x=1,y=30)

label6=Label(root,text='Area Type -->',bg='grey', fg='black',font=('Arial',11))
label6.place(x=1,y=60)										



Perm = {'none':1, 'Controlled':0.0001, 'Uncontrolled':0.00002 } 
selectedP = tk.StringVar()
Pr = ttk.Combobox(root, textvariable=selectedP, width=8,font=('Arial',12,'bold'))
Pr ['values'] = list(Perm.keys())
Pr.current(0)
Pr.place(x=100,y=60)


label7=Label(root,text='Use Factor -->',bg='grey', fg='black',font=('Arial',11))
label7.place(x=210,y=60)	
								
Usef = {'none':1, 'Roof Wall':0.263, 'Lateral Wall':0.213, 'Floor Wall':0.31 }  
selectedU = tk.StringVar()
Uf = ttk.Combobox(root, textvariable=selectedU, width=8,font=('Arial',12,'bold'))
Uf ['values'] = list(Usef.keys())
Uf.current(0)
Uf.place(x=300,y=60)


label8=Label(root,text='Occupancy -->',bg='grey', fg='black',font=('Arial',11)) 	
label8.place(x=400,y=60)								
Occp = {'1':1, '1/2':0.5, '1/5':0.2, '1/8':0.125, '1/20': 0.05 , '1/40': 0.025 }
selectedO = tk.StringVar()
Op = ttk.Combobox(root, textvariable=selectedO,width=13,font=('Arial',12,'bold'))
Op ['values'] = list(Occp.keys())
Op.current(0)
Op.place(x=510,y=60)

line=Label(root,text="  __________________________________________________________________________________________________________________________",bg='grey',font=('Arial',12,'bold'))
line.place(x=1,y=90)
## output label defined here ##
label9=Label(root,text='Transmission factor (Primary) ==>',bg='grey', fg='blue',font=('Arial',12))
label9.place(x=10,y=120)
out=Label(root,text='               ',bg='black', fg='red',font=('Arial',13,'bold'))
out.place(x=270,y=120)

## info label defined here ##
info=Label(root,text='',bg='grey', fg='black',font=('Arial',12,'bold'))
info.place(x=10,y=135)


labelS=Label(root,text='Material ->',bg='grey', fg='blue',font=('Arial',12,'bold'))
labelS.place(x=420,y=120)
mtrl = {'Concrete':1,'Steel':2, 'Lead':3 }
selectedM = tk.StringVar()
Mat = ttk.Combobox(root, textvariable=selectedM, width=8,font=('Arial',12,'bold'))
Mat ['values'] = list(mtrl.keys())
Mat.current(0)
Mat.place(x=500,y=120)

TVL1_4 = {'Concrete': 35,'Steel': 9.9, 'Lead': 5.7 }
TVL1_6 = {'Concrete': 37,'Steel':  10, 'Lead':  5.7 }
TVL1_10 = {'Concrete': 41,'Steel': 11, 'Lead': 5.7 }

TVLe_4 = {'Concrete': 30,'Steel':  9.9, 'Lead': 5.7 }
TVLe_6 = {'Concrete': 33,'Steel':  10, 'Lead':  5.7 }
TVLe_10 = {'Concrete': 37,'Steel': 11, 'Lead': 5.7 }


line=Label(root,text="  __________________________________________________________________________________________________________________________________",bg='grey',font=('Arial',12,'bold'))
line.place(x=1,y=150)

label10=Label(root,text='Thickness required (cm) ==>',bg='grey', fg='blue',font=('Arial',12,'bold'))
label10.place(x=80,y=185)
#result =Entry(root, bg='black',fg='red', width=15,font=('Arial',12,'bold'))
#result.place(x=400,y=250)
res=Label(root,text='                ',bg='black', fg='red',font=('Arial',14,'bold'))
res.place(x=400,y=185)





line=Label(root,text="  ________________________________________________________________________________________________________________________________",bg='grey',font=('Arial',12,'bold'))
line.place(x=1,y=220)







#############################################
###main calculation done here#####
#############################################

def action(event):
	
	Factor=(Perm[Pr.get()]*float(Distance.get())*float(Distance.get()))/(float(Workload.get())*Occp[Op.get()]*Usef[Uf.get()])
	print(Factor)
	out.config(text=f"{round(Factor,8)}")
	
	n=-1*math.log10(Factor)
	print(n)
	
	TVL1=0
	TVLe=0
	if (Enr[Er.get()]==4):
		TVL1= TVL1_4[Mat.get()]
		TVLe= TVLe_4[Mat.get()]	
		print(TVL1,Enr[Er.get()])
	if (Enr[Er.get()]==6):
		TVL1= TVL1_6[Mat.get()]
		TVLe= TVLe_6[Mat.get()]	
		print(TVL1,Enr[Er.get()])
	if (Enr[Er.get()]==10):
		TVL1= TVL1_10[Mat.get()]
		TVLe= TVLe_10[Mat.get()]	
		print(TVL1,Enr[Er.get()])
	
	thickness=TVL1+(n-1)*TVLe
	res.config(text=f"{round(thickness,4)}")	
	
## this function cleared all display bellow for clear button 	
def clear():
	res.config(text=f"")
	out.config(text=f"")
	Pr.current(0)
	Op.current(0)
	Mat.current(0)
	Er.current(0)
	Uf.current(0)
	Workload.delete(0,"end")
	Distance.delete(0,"end")
	info.config(text="")
line=Label(root,text="  _______________________________________________________________________________________________________________________",bg='grey',font=('Arial',12,'bold'))
line.place(x=1,y=270)

label1=Label(root,text='Note: This GUI is only for Primary Wall Calculations',bg='grey', fg='green',font=('Arial',13))
label1.place(x=1,y=310)

label1=Label(root,text='Note: Refer Table B.1 of NCRP-151 for occupancy factor values',bg='grey', fg='green',font=('Arial',13))
label1.place(x=1,y=340)

#execution
button=Button(root,text='CALCULATE',fg='green',font=('Arial',12,'bold'))
button.bind('<Button>',action)
button.place(x=260,y=250)

#clear
CLRbutton=Button(root,text='Clear',command=clear,fg='red',font=('Arial',12,'bold'))
CLRbutton.place(x=80,y=250)


#exit button 
exitButton=Button(root,text='Exit program',command=root.destroy,fg='red',font=('Arial',12,'bold'))
exitButton.place(x=500,y=250)

'''
s1.bind('<<ComboboxSelected>>', action)
Tdose.bind('<Return>',action)
Fx.bind('<Return>',action)
field.bind('<Return>',action)
X.bind('<Return>',action)
Y.bind('<Return>',action)
depth.bind('<Return>',action)
button.bind('<Return>',action)

Tdose.bind('<KP_Enter>',action)
Fx.bind('<KP_Enter>',action)
field.bind('<KP_Enter>',action)
X.bind('<KP_Enter>',action)
Y.bind('<KP_Enter>',action)
depth.bind('<KP_Enter>',action)
button.bind('<KP_Enter>',action)
'''
#geometry
root.configure(bg='grey',menu=menubar)
#root.config(menu=menubar)
root.geometry("660x380+330+100")
root.mainloop()



