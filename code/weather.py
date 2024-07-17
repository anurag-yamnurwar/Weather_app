from tkinter import * 
from tkinter import ttk 
import requests 

# Function to get the weather data
def data_get(): 
    city = city_name.get() 
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=9429d0a9b187fc62729363d7c2e658fd").json()
    
    if response.get('cod') != 200:
        error_message = response.get('message', '')
        w_label1.config(text="N/A") 
        wb_label1.config(text=error_message)
        temp_label1.config(text="N/A") 
        pre_label1.config(text="N/A") 
    else:
        w_label1.config(text=response["weather"][0]["main"]) 
        wb_label1.config(text=response["weather"][0]["description"]) 
        temp_label1.config(text=int(response["main"]["temp"] - 273.15)) 
        pre_label1.config(text=response["main"]["pressure"])

win = Tk() 
win.title("Weather Forecast") 
win.config(bg="lightblue") 
win.geometry("500x600")

# Main Title of The app 
name_label = Label(win, text="Weather Forecast", font=("Time New Roman",30,"bold")) 
name_label.place(x=25, y=50, height=50, width=450) 
 
# Name of all states in India 
city_name = StringVar() 
list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"] 
 
com = ttk.Combobox(win, text="Weather Forecast", values=list_name, font=("Time New Roman",15,"bold"), textvariable=city_name) 
com.place(x=25, y=120, height=50, width=450)

# Main Climate of the City  
w_label = Label(win, text="Weather Climate", font=("Time New Roman",18)) 
w_label.place(x=25, y=260, height=50, width=210) 
 
w_label1 = Label(win, text="", font=("Time New Roman",18)) 
w_label1.place(x=250, y=260, height=50, width=210) 
 
# Weather Description of the City 
wb_label = Label(win, text="Weather Description", font=("Time New Roman",17)) 
wb_label.place(x=25, y=330, height=50, width=210) 
wb_label1 = Label(win, text="", font=("Time New Roman",17)) 
wb_label1.place(x=250, y=330, height=50, width=210) 
 
# Temperature of the City 
temp_label = Label(win, text="Temperature", font=("Time New Roman",18)) 
temp_label.place(x=25, y=400, height=50, width=210)
temp_label1 = Label(win, text="", font=("Time New Roman",18)) 
temp_label1.place(x=250, y=400, height=50, width=210) 
 
# Pressure of the City 
pre_label = Label(win, text="Pressure", font=("Time New Roman",18)) 
pre_label.place(x=25, y=470, height=50, width=210) 
pre_label1 = Label(win, text="", font=("Time New Roman",18)) 
pre_label1.place(x=250, y=470, height=50, width=210) 
 
# Search button 
done_button = Button(win, text="Search", font=("Time New Roman",15,"bold"), command=data_get) 
done_button.place(y=190, height=50, width=100, x=200) 
 
win.mainloop()
