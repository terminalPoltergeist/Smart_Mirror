
# xrandr --output HDMI1 --rotate right
# rotate screen for mirror?

import tkinter as tk
from time import strftime
import datetime
from datetime import timedelta
import requests
import time
import PIL as p
import PIL.ImageTk as ptk
import pprint
import threading


def currenttime():
    global current_time
    x = datetime.datetime.now()
    current_time = x.strftime('%-I')


ptk

currenttime()


def tim():
    string = strftime('%-I:%M')
    x = str(strftime('%p'))
    x = x.lower()
    timlab.config(text=string)
    timlab.after(1000, tim)
    amplab.config(text=x)


def dat():
    global datestring
    x = datetime.datetime.today()
    datestring = x.strftime('%A, %b %d')


HEIGHT = 1100
WIDTH = 2000


def riseset():
    from datetime import datetime
    global rise
    global sett
    import pytz
    url = 'https://api.sunrise-sunset.org/json'
    lat = '44.708679'
    lon = '-96.276489'
    params = {'lat': lat, 'lng': lon}
    response = requests.get(url, params=params)
    weather = response.json()
    riseutc = (weather['results']['sunrise'])
    setutc = (weather['results']['sunset'])
    riseutc = datetime.strptime(riseutc, '%H:%M:%S %p')
    tz = pytz.timezone('US/Central')
    rise = riseutc.replace(tzinfo=pytz.utc).astimezone(tz)
    rise = rise.strftime('%H')
    setutc = datetime.strptime(setutc, '%H:%M:%S %p')
    tz = pytz.timezone('US/Central')
    sett = setutc.replace(tzinfo=pytz.utc).astimezone(tz)
    sett = sett.strftime('%H')


riseset()

# d398dcd6c9b4f8e1b99abb8ff330f1a7
# 56a7ec2ba43650bc82ad9341c871162a
# api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={your api key}


def weth():
    global descrip
    global des
    weather_key = 'd398dcd6c9b4f8e1b99abb8ff330f1a7'
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    lat = '44.708679'
    lon = '-96.276489'
    params = {'APPID': weather_key, 'lat': lat,
              'lon': lon, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()
    city = (weather['name'])
    descrip = (weather['weather'][0]['description'])
    des = (weather['weather'][0]['main'])
    temp = int(weather['main']['temp'])
    weatherstring = '%s \n%s \n%s°' % (city, descrip, temp)


weth()


def forc():
    global des1
    global des2
    global des3
    weather_key = '2ad58f62c12b4b83aa0d17da61322572'
    url = 'https://api.weatherbit.io/v2.0/forecast/hourly'
    lat = '44.708679'
    lon = '-96.276489'
    params = {'key': weather_key, 'lat': lat,
              'lon': lon, 'units': 'I', 'hours': 12}
    response = requests.get(url, params=params)
    forecast = response.json()
    descrip1 = (forecast['data'][2]['weather']['description'])
    des1 = (forecast['data'][2]['weather']['code'])
    temp1 = int(forecast['data'][2]['temp'])
    descrip2 = (forecast['data'][5]['weather']['description'])
    des2 = (forecast['data'][5]['weather']['code'])
    temp2 = int(forecast['data'][5]['temp'])
    descrip3 = (forecast['data'][8]['weather']['description'])
    des3 = (forecast['data'][8]['weather']['code'])
    temp3 = int(forecast['data'][11]['temp'])
    f1 = '%s°' % (temp1)
    f2 = '%s°' % (temp2)
    f3 = '%s°' % (temp3)
# 2ad58f62c12b4b83aa0d17da61322572


cloud = "/Users/jacknemitz/Desktop/Smart Mirror/weather icons/cloudy.png"
sun = "/Users/jacknemitz/Desktop/Smart Mirror/weather icons/sunny.png"
fewcloud = "/Users/jacknemitz/Desktop/Smart Mirror/weather icons/partlycloudy.png"
storm = "/Users/jacknemitz/Desktop/Smart Mirror/weather icons/storm.png"
driz = "/Users/jacknemitz/Desktop/Smart Mirror/weather icons/drizzle.png"
rain = "/Users/jacknemitz/Desktop/Smart Mirror/weather icons/rain.png"
heavyrain = "/Users/jacknemitz/Desktop/Smart Mirror/weather icons/heavyrain.png"
clearnight = "/Users/jacknemitz/Desktop/Smart Mirror/weather icons/clearnight.png"
cloudnight = "/Users/jacknemitz/Desktop/Smart Mirror/weather icons/cloudynight.png"


def forcicopick1():
    global fico1
    time1 = datetime.datetime.now() + timedelta(hours=3)
    tim1 = time1.strftime('%H')
    time1 = int(tim1)
    t = time1
    r = int(rise)
    s = int(sett)
    xx = s >= t >= r
    if int(str(des1)[:1]) == 2:
        fico1 = storm
    elif int(str(des1)[:1]) == 3:
        fico1 = driz
    elif int(str(des1)[:3]) == 502:
        fico1 = heavyrain
    elif int(str(des1)[:3]) == 501:
        fico1 = heavyrain
    elif int(str(des1)[:1]) == 5:
        fico1 = rain
    elif int(str(des1)[:3]) == 800:
        if xx == True:
            fico1 = sun
        else:
            fico1 = clearnight
    elif int(str(des1)[:3]) == 801:
        if xx == True:
            fico1 = fewcloud
        else:
            fico1 = cloudnight
    elif int(str(des1)[:3]) == 802:
        if xx == True:
            fico1 = fewcloud
        else:
            fico1 = cloudnight
    elif int(str(des1)[:3]) == 803:
        if xx == True:
            fico1 = cloud
        else:
            fico1 = cloudnight
    elif int(str(des1)[:3]) == 804:
        if xx == True:
            fico1 = cloud
        else:
            fico1 = cloudnight
    else:
        fico1 = sun


def forcicopick2():
    global fico2
    time2 = datetime.datetime.now() + timedelta(hours=6)
    tim2 = time2.strftime('%H')
    time2 = int(tim2)
    t = time2
    r = int(rise)
    s = int(sett)
    xx = s >= t >= r
    if int(str(des2)[:1]) == 2:
        fico2 = storm
    elif int(str(des2)[:1]) == 3:
        fico2 = driz
    elif int(str(des2)[:3]) == 502:
        fico2 = heavyrain
    elif int(str(des2)[:3]) == 501:
        fico2 = heavyrain
    elif int(str(des2)[:1]) == 5:
        fico2 = rain
    elif int(str(des2)[:3]) == 800:
        if xx == True:
            fico2 = sun
        else:
            fico2 = clearnight
    elif int(str(des2)[:3]) == 801:
        if xx == True:
            fico2 = fewcloud
        else:
            fico2 = cloudnight
    elif int(str(des2)[:3]) == 802:
        if xx == True:
            fico2 = fewcloud
        else:
            fico2 = cloudnight
    elif int(str(des2)[:3]) == 803:
        if xx == True:
            fico2 = cloud
        else:
            fico2 = cloudnight
    elif int(str(des2)[:3]) == 804:
        if xx == True:
            fico2 = cloud
        else:
            fico2 = cloudnight
    else:
        fico2 = sun


def forcicopick3():
    global fico3
    time3 = datetime.datetime.now() + timedelta(hours=9)
    tim3 = time3.strftime('%H')
    time3 = int(tim3)
    t = time3
    r = int(rise)
    s = int(sett)
    xx = s >= t >= r
    if int(str(des3)[:1]) == 2:
        fico3 = storm
    elif int(str(des3)[:1]) == 3:
        fico3 = driz
    elif int(str(des3)[:3]) == 502:
        fico3 = heavyrain
    elif int(str(des3)[:3]) == 501:
        fico3 = heavyrain
    elif int(str(des3)[:1]) == 5:
        fico3 = rain
    elif int(str(des3)[:3]) == 800:
        if xx == True:
            fico3 = sun
        else:
            fico3 = clearnight
    elif int(str(des3)[:3]) == 801:
        if xx == True:
            fico3 = fewcloud
        else:
            fico3 = cloudnight
    elif int(str(des3)[:3]) == 802:
        if xx == True:
            fico3 = fewcloud
        else:
            fico3 = cloudnight
    elif int(str(des3)[:3]) == 803:
        if xx == True:
            fico3 = cloud
        else:
            fico3 = cloudnight
    elif int(str(des3)[:3]) == 804:
        if xx == True:
            fico3 = cloud
        else:
            fico3 = cloudnight
    else:
        fico3 = sun


def forctime1():
    global time1
    time1 = datetime.datetime.now() + timedelta(hours=3)
    tim1 = time1.strftime('%-I')
    ap = str(time1.strftime('%p'))
    ap = ap.lower()
    forctimlab1.config(text=tim1)
    aplab1.config(text=ap)
    forctimlab1.after(60000, forctime1)


def forctime2():
    global time2
    time2 = datetime.datetime.now() + timedelta(hours=6)
    tim2 = time2.strftime('%-I')
    ap = str(time2.strftime('%p'))
    ap = ap.lower()
    forctimlab2.config(text=tim2)
    aplab2.config(text=ap)
    forctimlab2.after(60000, forctime2)


def forctime3():
    global time3
    time3 = datetime.datetime.now() + timedelta(hours=9)
    tim3 = time3.strftime('%-I')
    ap = str(time3.strftime('%p'))
    ap = ap.lower()
    forctimlab3.config(text=tim3)
    aplab3.config(text=ap)
    forctimlab3.after(60000, forctime3)


def icopick():
    global ico
    time = datetime.datetime.now()
    tim = time.strftime('%H')
    time = int(tim)
    t = time
    r = int(rise)
    s = int(sett)
    xx = s >= t >= r
    if des == "Clouds":
        if xx == True:
            ico = cloud
        else:
            ico = cloudnight
    elif descrip == "few clouds":
        ico = fewcloud
    elif descrip == "scattered clouds":
        ico = fewcloud
    elif des == "Clear":
        if xx == True:
            ico = sun
        else:
            ico = clearnight
    elif des == "Rain":
        ico = heavyrain
    elif descrip == "light rain":
        ico = rain
    elif descrip == "moderate rain":
        ico = rain
    elif descrip == "light intensity shower rain":
        ico = rain
    elif des == "Drizzle":
        ico = driz
    elif des == "Thunderstorm":
        ico = storm
    else:
        ico = sun


# 547398a7d3d84096aa4e160daa586abd
# news api key

def x():
    global x
    x = 0


x()


def add():
    global x
    while True:
        x += 0.001
        time.sleep(0.08)


def defkey():
    global key
    key = 0


defkey()


def addkey():
    global key
    key += 1


def getnews():
    global key
    global news
    url = ('http://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=547398a7d3d84096aa4e160daa586abd')
    response = requests.get(url)
    data = response.json()
    news = (data['articles'][key]['description'])


getnews()


root = tk.Tk()
root.wm_attributes('-fullscreen', 'false')  # set to true to hide title bar
root.configure(background='black')
root.title('')


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH,
                   bg='black', highlightthickness=0)
canvas.pack()

dattim_frame = tk.Frame(canvas, bg='black')
dattim_frame.place(relx=0.2, rely=0.1, relwidth=0.3,
                   relheight=0.15, anchor='n')

weth_frame = tk.Frame(canvas, bg='black')
weth_frame.place(relx=0.7, rely=0.1, relwidth=0.4,
                 relheight=0.2, anchor='n')

forc_frame = tk.Frame(canvas, bg='black')
forc_frame.place(relx=0.72, rely=0.28, relwidth=0.45,
                 relheight=0.16, anchor='n')

n_frame = tk.Frame(canvas, bg='black')
n_frame.place(relx=0.55, rely=0.8, relwidth=0.8,
              relheight=0.1, anchor='center')

attribution_frame = tk.Frame(canvas, bg='black')
attribution_frame.place(relx=0.89, rely=0.94, relwidth=0.1, relheight=0.05)

timlab = tk.Label(dattim_frame, font=(
    'Courier New', 70, 'bold'), bg='black', fg='white', justify='right')
timlab.pack(anchor='center')
amplab = tk.Label(dattim_frame, font=('Courier New', 45),
                  bg='black', fg='white', justify='left')
amplab.place(relx=0.71, rely=0.14)
tim()

datlab = tk.Label(dattim_frame, font=(
    'Courier New', 30, 'italic'), bg='black', fg='white', justify='left')
datlab.place(relx=0.27, rely=0.53)
dat()
datlab.config(text=datestring)
datlab.after(86400000, dat())

wethlab = tk.Label(weth_frame, font=(
    'Courier New', 40), bg='black', fg='white', anchor='n', justify='left')
wethlab.place(relx=0.45, rely=0)
wethlab.config(text=weatherstring)
wethlab.after(1800000, weth())


icopick()
pic = p.Image.open(ico)
pic = pic.resize((150, 150))
photo = ptk.PhotoImage(pic)

iconlab = tk.Label(weth_frame, image=photo, bg='black')
iconlab.place(relx=0.15, rely=0)
iconlab.after(1800000, icopick)

forclab1 = tk.Label(forc_frame, font=(
    'Courier New', 27, 'bold'), bg='black', fg='white', anchor='n', justify='center')
forclab1.place(relx=0.25, rely=0.7)

forclab2 = tk.Label(forc_frame, font=(
    'Courier New', 27, 'bold'), bg='black', fg='white', anchor='n', justify='center')
forclab2.place(relx=0.5, rely=0.7)

forclab3 = tk.Label(forc_frame, font=(
    'Courier New', 27, 'bold'), bg='black', fg='white', anchor='n', justify='center')
forclab3.place(relx=0.75, rely=0.7)
forc()
forclab1.config(text=f1)
forclab1.after(3600000, forc)
forclab2.config(text=f2)
forclab2.after(3600000, forc)
forclab3.config(text=f3)
forclab3.after(3600000, forc)

forcicopick1()
fi1 = p.Image.open(fico1)
fi1 = fi1.resize((50, 50))
ficon1 = ptk.PhotoImage(fi1)

ficonlab1 = tk.Label(forc_frame, image=ficon1, bg='black')
ficonlab1.place(relx=0.25, rely=0.3)
ficonlab1.after(3600000, icopick)


forcicopick2()
fi2 = p.Image.open(fico2)
fi2 = fi2.resize((50, 50))
ficon2 = ptk.PhotoImage(fi2)

ficonlab2 = tk.Label(forc_frame, image=ficon2, bg='black')
ficonlab2.place(relx=0.5, rely=0.3)
ficonlab2.after(3600000, icopick)

forcicopick3()
fi3 = p.Image.open(fico3)
fi3 = fi3.resize((50, 50))
ficon3 = ptk.PhotoImage(fi3)

ficonlab3 = tk.Label(forc_frame, image=ficon3, bg='black')
ficonlab3.place(relx=0.75, rely=0.3)
ficonlab3.after(3600000, icopick)

forctimlab1 = tk.Label(forc_frame, font=(
    'Courier New', 20, 'bold', 'italic'), bg='black', fg='white', anchor='center', justify='center')
forctimlab1.place(relx=0.24, rely=0.05)
aplab1 = tk.Label(forc_frame, font=('Courier New', 20, 'italic'),
                  bg='black', fg='white')
aplab1.place(relx=0.295, rely=0.08)
forctime1()

forctimlab2 = tk.Label(forc_frame, font=(
    'Courier New', 20, 'bold', 'italic'), bg='black', fg='white', justify='center')
forctimlab2.place(relx=0.5, rely=0.05)
aplab2 = tk.Label(forc_frame, font=('Courier New', 20, 'italic'),
                  bg='black', fg='white')
aplab2.place(relx=0.55, rely=0.08)
forctime2()

forctimlab3 = tk.Label(forc_frame, font=(
    'Courier New', 20, 'bold', 'italic'), bg='black', fg='white', justify='center')
forctimlab3.place(relx=0.74, rely=0.05)
aplab3 = tk.Label(forc_frame, font=('Courier New', 20, 'italic'),
                  bg='black', fg='white')
aplab3.place(relx=0.79, rely=0.08)
forctime3()


nlab = tk.Label(n_frame, font=(
    'Courier New', 20, 'bold', 'italic'), bg='black', fg='white', anchor='e', justify='left')
nlab.after(30000, addkey(), getnews())
nlab.config(text=news)

t1 = threading.Thread(target=add)
t1.start()


def newsmove():
    nlab.place(relx=x, rely=0.5)
    nlab.after(30, newsmove)


newsmove()


def newsstop():
    global key
    global x
    while True:
        if x > 1:
            x = -0.3
            if 0 > x > 0.99:
                key += 1
                getnews()
            else:
                continue
        else:
            continue


t2 = threading.Thread(target=newsstop)
t2.start()


attlab = tk.Label(attribution_frame, text=("Powered by:\n News API"), font=(
    'Courier New', 15, 'italic'), bg='black', fg='white', justify='center')
attlab.place(relx=0.1, rely=0.1)

root.mainloop()
