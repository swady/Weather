from tkinter import*
import requests, json
root = Tk()

canvas= Canvas(root, width=590, height=280)
canvas.pack()
myimg= PhotoImage(file='g://filehandling//background4.gif')
canvas.create_image(0,0, anchor= NW, image=myimg)

def clr():
    b=e1.delete(0,END)
    a=e2.delete(0,END)
    c=e3.delete(0,END)
    d=e4.delete(0,END)
    e=e5.delete(0,END)
def ex():
    root.destroy()
def sub():
    try:
        global city
        city=e2.get()
        weather()
    except:
        a=e2.delete(0,END)
        e2.insert(0,'Wrong city name or No internet connection')
    
def weather():
    api_address='http://api.openweathermap.org/data/2.5/weather?'
    api_address += 'appid=603ae1e03c8079fcd72993096c94ebb6'+'&q='
    url=api_address + city
    json_data=requests.get(url).json()
    temp=int(json_data['main']['temp']-273.15)  #temperature
    x = json_data
    y = x['main']
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    e1.insert(0,str(temp)+chr(176)+'C')
    e5.insert(0,str(current_pressure)+' hPa(hetropascal)')
    e3.insert(0,str(current_humidity)+' %')
    e4.insert(0,weather_description)



f10=Frame(root,bg='#031BB9',height=5)
f10.pack(side=TOP,expand=TRUE,fill=BOTH)

root.title('Weather Report')
root.wm_iconbitmap(r'G:\filehandling\weather.ico')

f3=Frame(root,bg='#031BB9')
f3.pack(side=TOP,expand=TRUE,fill=BOTH)
l3=Label(f3,width=30,text='Name of the city',bg='black',fg='yellow')
l3.pack(side=LEFT,fill=BOTH,padx=20)
e2=Entry(f3,width=50,bg='white')
e2.pack(side=RIGHT,padx=20)
f10=Frame(root,bg='#031BB9',height=5)
f10.pack(side=TOP,expand=TRUE,fill=BOTH)

f1=Frame(root,bg='#031BB9')
f1.pack(side=TOP,expand=TRUE,fill=BOTH)
l1=Label(f1,width=30,text='Current temperature',bg='#42D19D',fg='red')
l1.pack(side=LEFT,fill=BOTH,padx=20)
e1=Entry(f1,width=50,bg='#ECCFEE')
e1.pack(side=RIGHT,padx=20)
f10=Frame(root,bg='#031BB9',height=5)
f10.pack(side=TOP,expand=TRUE,fill=BOTH)

f1=Frame(root,bg='#031BB9')
f1.pack(side=TOP,expand=TRUE,fill=BOTH)
l1=Label(f1,width=30,text='Pressure',bg='#42D19D',fg='red')
l1.pack(side=LEFT,fill=BOTH,padx=20)
e5=Entry(f1,width=50,bg='#ECCFEE')
e5.pack(side=RIGHT,padx=20)
f10=Frame(root,bg='#031BB9',height=5)
f10.pack(side=TOP,expand=TRUE,fill=BOTH)


f1=Frame(root,bg='#031BB9')
f1.pack(side=TOP,expand=TRUE,fill=BOTH)
l1=Label(f1,width=30,text='Humidity',bg='#42D19D',fg='red')
l1.pack(side=LEFT,fill=BOTH,padx=20)
e3=Entry(f1,width=50,bg='#ECCFEE')
e3.pack(side=RIGHT,padx=20)
f10=Frame(root,bg='#031BB9',height=5)
f10.pack(side=TOP,expand=TRUE,fill=BOTH)


f1=Frame(root,bg='#031BB9')
f1.pack(side=TOP,expand=TRUE,fill=BOTH)
l1=Label(f1,width=30,text='Weather Description',bg='#42D19D',fg='red')
l1.pack(side=LEFT,fill=BOTH,padx=20)
e4=Entry(f1,width=50,bg='#ECCFEE')
e4.pack(side=RIGHT,padx=20)
f10=Frame(root,bg='#031BB9',height=5)
f10.pack(side=TOP,expand=TRUE,fill=BOTH)



f4=Frame(root,bg='#031BB9')
f4.pack(side=TOP,expand=TRUE,fill=BOTH)
b2=Button(f4,text='Submit',bg='yellow',fg='red',font=20,bd=5,command=sub)
b2.pack(side=LEFT,fill=BOTH,expand=TRUE,padx=20)

b4=Button(f4,text='Exit',bg='yellow',fg='red',font=20,bd=5,command=ex)
b4.pack(side=RIGHT,fill=BOTH,expand=TRUE,padx=20)

b3=Button(f4,text='Clear',bg='yellow',fg='red',font=20,bd=5,command=clr)
b3.pack(side=RIGHT,fill=BOTH,expand=TRUE,padx=20)


f10=Frame(root,bg='#031BB9',height=8)
f10.pack(side=TOP,expand=TRUE,fill=BOTH)


root.mainloop()
