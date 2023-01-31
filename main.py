import requests
import folium
from tkinter import *
import webbrowser as wb
import pyfiglet

name_img = pyfiglet.figlet_format("Firebrand")
print(name_img)

def get():
    ip = edit.get()
    try:
        req = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
            '[IP]': req.get('query'),
            '[Интернет провайдер]': req.get('isp'),
            '[Страна]': req.get('country'),
            '[Регион]': req.get('regionName'),
            '[Почтовый индекс]': req.get('zip'),
            '[Широта]': req.get('lat'),
            '[Долгота]': req.get('lon'),
        }

        for k, v in data.items():
            print(f'{k}: {v}')
        print(f'--------------------\n')
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
window.iconbitmap('d80f3480a0a42895570ec5c660263700 (1).ico')
window.title('Firebrand')
window.geometry('300x250')
window.wm_attributes('-alpha', 0.8)

title = Label(window, text='Введите IPv4')
title.pack()

edit = Entry(window,width=15)
edit.pack()

but = Button(text='Принять', command=get)
but.pack()

window.mainloop()

if __name__ == '__main__':
    pass
