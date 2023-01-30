import requests
import folium
from tkinter import *
import webbrowser as wb


def get():
    ip = edit.get()
    try:
        req = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
            '[IP]': req.get('query'),
            '[Int prov]': req.get('isp'),
            '[Country]': req.get('country'),
            '[Region]': req.get('regionName'),
            '[ZIP]': req.get('zip'),
            '[Lat]': req.get('lat'),
            '[Lon]': req.get('lon'),
        }

        for k, v in data.items():
            print(f'{k}: {v}')
        with open('info.txt', 'a') as f:
            for k, v in data.items():
                f.write(f'{k}: {v}\n')
            f.write(f'--------------------\n')
        area = folium.Map(location=[req.get('lat'), req.get('lon')])
        area.save(f'{req.get("query")}_{req.get("city")}.html')

        ip = req.get("query")
        city = req.get("city")
        wb.open(f'file:///C:/Users/Cooper/PycharmProjects/OSINT/{ip}_{city}.html')
    except:
        print()

window = Tk()
#window.iconbitmap('favpng_vector-graphics-royalty-free-stock-illustration-knight.ico')
window.title('Knight')
window.geometry('300x250')
window.wm_attributes('-alpha', 0.8)

title = Label(window, text='Введите ip')
title.pack()

edit = Entry(window)
edit.pack()

but = Button(text='Принять', command=get)
but.pack()

window.mainloop()

