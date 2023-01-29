import win10toast###
from win10toast import ToastNotifier###
import requests
import folium
from tkinter import *###
import webbrowser as wb

def get_info_ip(ip):
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

def main():
    ip = (input('Введите ip-адрес:'))

    get_info_ip(ip=ip)

def message():
    message = win10toast.ToastNotifier()
    message.show_toast(title="OSINT", msg="Scan finished!", duration=10)

def window():
    window = Tk()
    window.title('Инфо')
    window.geometry('300x250')
    window.wm_attributes('-alpha', 0.7)
    title = Label(window,text='Введите ip')
    title.pack()
    window.mainloop()

if __name__ == '__main__':
    try:
        while True:
            main()
            #message()
    except:
        print()
