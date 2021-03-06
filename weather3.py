from tkinter import*                                               #import libraries
import requests, json
root = Tk()

#set an image for the GUI
canvas= Canvas(root, width=590, height=280)
canvas.pack()
myimg= PhotoImage(file='<path of the gif file>')                    #a gif file is required in this place
canvas.create_image(0,0, anchor= NW, image=myimg)


#set the icon of the frame
root.title('Weather Report')
root.wm_iconbitmap(r'<path of the icon>')

#clear function
def clr():
    b=e1.delete(0,END)
    a=e2.delete(0,END)
    c=e3.delete(0,END)
    d=e4.delete(0,END)
    e=e5.delete(0,END)

#exit function
def ex():
    root.destroy()

#submit function
def sub():
    try:                                          #check if the user has entered a correct city name
        global city
        city=e2.get()
        weather()
    except:
        a=e2.delete(0,END)
        e2.insert(0,'Wrong city name or No internet connection')      #if wrong city name or there is no internet connection show this messege



#weather function   
def weather():
    api_address='http://api.openweathermap.org/data/2.5/weather?'
    api_address += 'appid=<enter your api addredss>'+'&q='       #enter your api adderss here
    url=api_address + city
    json_data=requests.get(url).json()
    x = json_data
    y = x['main']
    current_temperature = y['temp']-273.15
    current_pressure = y['pressure']
    current_humidity = y["humidity"]
    z = x['weather']
    weather_description = z[0]['description']
    e1.insert(0,str(current_temperature)+chr(176)+'C')
    e3.insert(0,str(current_humidity)+' %')
    e4.insert(0,weather_description)
    e5.insert(0,str(current_pressure)+' hPa(hetropascal)')



f10=Frame(root,bg='#031BB9',height=5)
f10.pack(side=TOP,expand=TRUE,fill=BOTH)

#enter the name of the city
f3=Frame(root,bg='#031BB9')
f3.pack(side=TOP,expand=TRUE,fill=BOTH)
l3=Label(f3,width=30,text='Name of the city',bg='black',fg='yellow')
l3.pack(side=LEFT,fill=BOTH,padx=20)
e2=Entry(f3,width=50,bg='white')
e2.pack(side=RIGHT,padx=20)
f10=Frame(root,bg='#031BB9',height=5)
f10.pack(side=TOP,expand=TRUE,fill=BOTH)


#current temperature
f1=Frame(root,bg='#031BB9')
f1.pack(side=TOP,expand=TRUE,fill=BOTH)
l1=Label(f1,width=30,text='Current temperature',bg='#42D19D',fg='red')
l1.pack(side=LEFT,fill=BOTH,padx=20)
e1=Entry(f1,width=50,bg='#ECCFEE')
e1.pack(side=RIGHT,padx=20)
f10=Frame(root,bg='#031BB9',height=5)
f10.pack(side=TOP,expand=TRUE,fill=BOTH)



#pressure
f1=Frame(root,bg='#031BB9')
f1.pack(side=TOP,expand=TRUE,fill=BOTH)
l1=Label(f1,width=30,text='Pressure',bg='#42D19D',fg='red')
l1.pack(side=LEFT,fill=BOTH,padx=20)
e5=Entry(f1,width=50,bg='#ECCFEE')
e5.pack(side=RIGHT,padx=20)
f10=Frame(root,bg='#031BB9',height=5)
f10.pack(side=TOP,expand=TRUE,fill=BOTH)

#humidity
f1=Frame(root,bg='#031BB9')
f1.pack(side=TOP,expand=TRUE,fill=BOTH)
l1=Label(f1,width=30,text='Humidity',bg='#42D19D',fg='red')
l1.pack(side=LEFT,fill=BOTH,padx=20)
e3=Entry(f1,width=50,bg='#ECCFEE')
e3.pack(side=RIGHT,padx=20)
f10=Frame(root,bg='#031BB9',height=5)
f10.pack(side=TOP,expand=TRUE,fill=BOTH)



#weather description 
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

#submit Button
b2=Button(f4,text='Submit',bg='yellow',fg='red',font=20,bd=5,command=sub)
b2.pack(side=LEFT,fill=BOTH,expand=TRUE,padx=20)

#exit button
b4=Button(f4,text='Exit',bg='yellow',fg='red',font=20,bd=5,command=ex)
b4.pack(side=RIGHT,fill=BOTH,expand=TRUE,padx=20)

#clear button
b3=Button(f4,text='Clear',bg='yellow',fg='red',font=20,bd=5,command=clr)
b3.pack(side=RIGHT,fill=BOTH,expand=TRUE,padx=20)

f10=Frame(root,bg='#031BB9',height=8)
f10.pack(side=TOP,expand=TRUE,fill=BOTH)

root.mainloop()