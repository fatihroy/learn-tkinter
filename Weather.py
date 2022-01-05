from tkinter import *
import json
import requests

window = Tk()
window.title("bikin weather app")
window.geometry("600x100")

# credit : i created using airnow API
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=61257&distance=5&API_KEY=22B63539-D31F-4D0B-94A6-48D392E0A65A


# zip lookup 
def ziplookup():
    # z.get()
    # z_lbl = Label(window, text=z.get())
    # z_lbl.grid(row=1, column=0, columnspan=2)

    # mencoba connect kewebsite, bila websitenya gak connect maka jalankan except
    try:
        api_requests = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + z.get() + "&distance=25&API_KEY=22B63539-D31F-4D0B-94A6-48D392E0A65A")
        api = json.loads(api_requests.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
    
        # perkondisisan misal apabila good maka berwarna hijau
        if category == 'Good':
            color = "#0C0"
        elif category == 'Moderate':
            color = "FFF00"
        elif category == 'Unhealthy for Sensitive Group':
            color = "#ff9900"
        elif category == 'Unhealthy':
            color = "#FF0000"
        elif category == 'Very Unhealthy':
            color = "#990066"  
        elif category == 'Hazardous':
            color = "#66000"   
    
        lbl = Label(window, text=city + " Air Quality " + str(quality) + " " + category, font=('Helvetica','15'),bg=color)
        lbl.grid(row=1, column=0, columnspan=2)
        window.configure(bg=color)

    
    except Exception as e:
        api="Errorrr...!!1"


z = Entry(window)
z.grid(row=0, column=0, sticky=W + E + N +S)

z_btn = Button(window, text="Lookup zip code", command=ziplookup)
z_btn.grid(row=0, column=1)

window.mainloop()