# ==================================================
# CS361 - Sprint 4
# Name: Theresa Phan
# Date: February 13, 2021
# Population Generator Project
# ==================================================
import tkinter as tk
from tkinter import *
import requests
import sys
import csv
import rpyc

class myService(rpyc.Service):
    # A connection is created
    # (to init the service, if needed)
    def on_connect(self,conn):
        print("Connection Received!")
        pass
    
    # The connection has already closed
    # (Finalize the service)
    def on_disconnect(self, conn):
        print("Disconnected!")
        pass
    
    # Exponsed method
    def exposed_get_population(self, state, year):

        return get_population(state, year)
    
# Height and width of canvas defined
HEIGHT = 400
WIDTH = 500

# Data from https://www.census.gov/data/developers/data-sets/acs-1year.html
# api.census.gov/data/2010/acs/acs1?get=NAME,B01001_001E&for=state:*&key=YOUR_KEY_GOES_HERE

def test_function(state, year):
    print("This is the state:", state)
    print("This is the year:", year)

def format_response(population):
    population_number = population[1][1]

    return str(population_number)
    
def get_population(state, year):
    population_key = 'f69a542f9018e3d6b4cbeea4fd06bba2d83e3fa1'
    base_url = 'http://api.census.gov/data/'
    data_set = '/acs/acs1?get=NAME,'
    variable = "B01003_001E"

    fips = states_dic[state]
    url = str(base_url + year + data_set + variable + '&for=state:' + fips + '&key=' + population_key)
    response = requests.get(url)
    population = response.json()

    return format_response(population) 

def set_population(state,year):
     population = get_population(state,year)
     label['text'] = population

root = tk.Tk()

# Source: https://www.youtube.com/watch?v=D8-snVfekto&t=3455s
# Canvas
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#f4eada')
frame.place(relx=.2, rely=.3, relwidth=.6, relheight=.6)

#Drop Down Boxes

states_dic = {
    "AL": "01",
    "AK": "02",
    "AZ": "04",
    "AR": "05",
    "CA": "06",
    "CO": "08",
    "CT": "09",
    "DE": "10",
    "FL": "12",
    "GA": "13",
    "HI": "15",
    "ID": "16",
    "IL": "17",
    "IN": "18",
    "IA": "19",
    "KS": "20",
    "KY": "21",
    "LA": "22",
    "ME": "23",
    "MD": "24",
    "MA": "25",
    "MI": "26",
    "MN": "27",
    "MS": "28",
    "MO": "29",
    "MT": "30",
    "NE": "31",
    "NV": "32",
    "NH": "33",
    "NJ": "34",
    "NM": "35",
    "NY": "36",
    "NC": "37",
    "ND": "38",
    "OH": "39",
    "OK": "40",
    "OR": "41",
    "PA": "42",
    "RI": "44",
    "SC": "45",
    "SD": "46",
    "TN": "47",
    "TX": "48",
    "UT": "49",
    "VT": "50",
    "VA": "51",
    "WA": "53",
    "WV": "54",
    "WI": "55",
    "WY": "56"
}

clicked1 = StringVar()

state = OptionMenu(root, clicked1, *states_dic)
state.place(relx=".2", rely=".2")
# drop.pack()
clicked1.set(list(states_dic.keys())[0]) # Set the first object in the list.

years_dic = [
    "2005",
    "2006",
    "2007",
    "2008",
    "2009",
    "2010",
    "2011",
    "2012",
    "2013",
    "2014",
    "2015",
    "2016",
    "2016",
    "2017",
    "2018",
    "2019"
]

clicked2 = StringVar()
clicked2.set(years_dic[0])

year = OptionMenu(root, clicked2, *years_dic)
year.place(relx=".4", rely=".2")

# Button
# Source: https://stackoverflow.com/questions/49816795/tkinter-optionmenu-cant-use-get-in-a-function
button1 = tk.Button(root, text="Get Population Size", command=lambda: set_population(clicked1.get(), clicked2.get()))
button1.place(relx=".6", rely=".2")

label = tk.Label(frame, bg='#ccccff', font=('Modern', 15))
label.place(relwidth=1, relheight=1)

titleLabel = tk.Label(canvas, font=('Modern', 20))
titleLabel['text'] = "Population Generator"
titleLabel.place(relx=".3", rely=".08")

# If there is a command line arguments, GUI does not open
if(len(sys.argv) == 2):

    # Argument for starting rpyc server
    if(sys.argv[-1] == "-server"):
        from rpyc.utils.server import ThreadedServer
        t = ThreadedServer(myService, port=3495)
        t.start()

    # Argument of input.csv
    else:
        arr = []
        
        with open('input.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                arr.append(row)
        
        population = get_population(arr[1][0], arr[1][1])

        with open('output.csv', 'w', newline='') as new_file:
            csv_writer = csv.writer(new_file, delimiter=',')
            csv_writer.writerow(["input_year", "input_state", "output_population_size"])
            csv_writer.writerow([arr[1][0], arr[1][1], population])

# If there is no command line argument, GUI opens
else:
    root.mainloop()