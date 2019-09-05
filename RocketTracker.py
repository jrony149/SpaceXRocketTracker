from mpl_toolkits.mplot3d import axes3d
#matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import urllib
import urllib.parse
import urllib.request
import re
import webbrowser
import requests
import json
import csv
from tkinter import *
from tkinter.messagebox import *
import os

global array, array2, array3, array4

array, array2, array3, array4 = [], [], [], []

for x in range(15000):

    array.append(None)

    array2.append(None)

    array3.append(None)

    array4.append(None)


def hashFunction(key):

    return int(key % 15000)

def insertElementAltFirstStage(time, Altitude): 

    for x in range(len(time)):

        key = int(time[x])

        array[hashFunction(key)] = Altitude[x]

def insertElementVelFirstStage(time, Velocity):

    for x in range(len(time)):

        key = int(time[x])

        array2[hashFunction(key)] = Velocity[x]

def searchValueAltFirstStage():

    val = int(keyEntry.get())

    key = hashFunction(val)

    altitudeOtpt.insert(END, array[key])

def searchValueVelFirstStage():

    val = int(keyEntry.get())

    key = hashFunction(val)

    velocityOtpt.insert(END, array2[key])

def insertElementAltSecondStage(time, Altitude): 

    for x in range(len(time)):

        key = int(time[x])

        array3[hashFunction(key)] = Altitude[x]

def insertElementVelSecondStage(time, Velocity):

    for x in range(len(time)):

        key = int(time[x])

        array4[hashFunction(key)] = Velocity[x]

def searchValueAltSecondStage():

    val = int(keyEntry2.get())

    key = hashFunction(val)

    altitudeOtpt2ndStage.insert(END, array3[key])

def searchValueVelSecondStage():

    val = int(keyEntry2.get())

    key = hashFunction(val)

    velocityOtpt2ndStage.insert(END, array4[key])

    
def DataSearch():

    flightNum2 = str(flightNumInput.get())

    mainAPI = "https://api.spacexdata.com/v2/launches?flight_number=" + flightNum2

    data = requests.get(mainAPI).json()

    rocketName = data[0]['rocket']['rocket_name']
    launchDate = data[0]['launch_date_local']
    details = data[0]['details']
    flightTelem = data[0]['telemetry']['flight_club']

    rocketNameOutput.insert(0, rocketName)
    launchDateOutput.insert(0, launchDate)
    detailsOutput.insert(END, details)

    if flightNumInput.get() == '56':

        mainAPI2 = "https://www.flightclub.io:8443/FlightClub/api/v1/simulator/results/7bda1de3-2d2c-495c-a4ba-da64034d0237" #api call to flightclub's json profile on
                                                                                                                            #CRS-12 launch.
        data2 = requests.get(mainAPI2).json()

        #firstStageTelem = data2['data'][0]['files'][0]['url']#navigates to the telemetry data file for the first stage in the json profile.

        #secondStageTelem = data2['data'][0]['files'][2]['url']#navigates to the telemetry data file for the second stage in the json profile.
        
        #webbrowser.open(firstStageTelem) #opens the telemetry data file for the first stage.

        #webbrowser.open(secondStageTelem) #opens the telemetry data file for the second stage.

        #Altitude graph, 1st Stage

        fig = plt.Figure(figsize = (2.7, 2.7), dpi = 100)
        ax = fig.add_subplot(111, projection = '3d')

        X, Y, Z = [], [], []

        with open('7bda1de3-2d2c-495c-a4ba-da64034d0237_0.dat', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=';')

            next(plots)
            
            for x in plots:
                
                X.append(float(x[0])) #time
                Y.append(0)
                Z.append(float(x[4])) #altitude

        insertElementAltFirstStage(X, Z)

        ax.set_xlabel("Time (seconds)")
        ax.set_zlabel("Altitude (km)")

        ax.plot(X,Y,Z)

        global canvas
        canvas = FigureCanvasTkAgg(fig, lowerRightFrame)
        canvas.draw()
        canvas.get_tk_widget().grid()
        ax.mouse_init()

        #Velocity graph, 1st Stage

        fig2 = plt.Figure(figsize = (2.7, 2.7), dpi = 100)
        ax = fig2.add_subplot(111, projection = '3d')

        Q, R, S = [], [], []

        with open('7bda1de3-2d2c-495c-a4ba-da64034d0237_0.dat', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter = ';')

            next(plots)
            
            for x in plots:

                Q.append(float(x[0]))
                R.append(0)
                S.append(float(x[5]))

            insertElementVelFirstStage(Q, S)
                
            ax.set_xlabel("Time\n(seconds)")
            ax.set_zlabel("Velocity (mps)")

            ax.plot(Q,R,S)

            global canvas2
            canvas2 = FigureCanvasTkAgg(fig2, lowerRightMostFrame)
            canvas2.draw()
            canvas2.get_tk_widget().grid()
            ax.mouse_init()

        #Altitude graph, 2nd Stage
    
        fig = plt.Figure(figsize = (2.7, 2.7), dpi = 100)
        ax = fig.add_subplot(111, projection = '3d')

        A, B, C = [], [], []

        with open('7bda1de3-2d2c-495c-a4ba-da64034d0237_1.dat', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=';')

            next(plots)
            
            for x in plots:
                
                A.append(float(x[0]))
                B.append(0)
                C.append(float(x[4]))

        insertElementAltSecondStage(A, C)

        ax.set_xlabel("Time (seconds)")
        ax.set_zlabel("Altitude (km)")

        ax.plot(A,B,C)

        global canvas3
        canvas3 = FigureCanvasTkAgg(fig, lowestRightFrame)
        canvas3.draw()
        canvas3.get_tk_widget().grid()
        ax.mouse_init()

        #Velocity graph, 2nd Stage

        fig2 = plt.Figure(figsize = (2.7, 2.7), dpi = 100)
        ax = fig2.add_subplot(111, projection = '3d')

        T, U, V = [], [], []

        with open('7bda1de3-2d2c-495c-a4ba-da64034d0237_1.dat', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter = ';')

            next(plots)
            
            for x in plots:
                T.append(float(x[0]))
                U.append(0)
                V.append(float(x[5]))

            insertElementVelSecondStage(T, V)
                
            ax.set_xlabel("Time (seconds)")
            ax.set_zlabel("Velocity (mps)")

            ax.plot(T,U,V)

            global canvas4
            canvas4 = FigureCanvasTkAgg(fig2, lowestRightMostFrame)
            canvas4.draw()
            canvas4.get_tk_widget().grid()
            ax.mouse_init()

    if flightNumInput.get() == '57':

        mainAPI2 = "https://www.flightclub.io:8443/FlightClub/api/v1/simulator/results/30964ffc-a1c9-4afc-b06e-8aacdfc7b9bd" #api call to flightclub's json profile on
                                                                                                                            #CRS-12 launch.
        data2 = requests.get(mainAPI2).json()

        #firstStageTelem = data2['data'][0]['files'][0]['url']#navigates to the telemetry data file for the first stage in the json profile.

        #secondStageTelem = data2['data'][0]['files'][2]['url']#navigates to the telemetry data file for the seconds stage in the json profile.
        
        #webbrowser.open(firstStageTelem) #opens the telemetry data file for the first stage.

        #webbrowser.open(secondStageTelem) #opens the telemetry data file for the seconds stage.

        #Altitude graph, 1st Stage
    
        fig = plt.Figure(figsize = (2.7, 2.7), dpi = 100)
        ax = fig.add_subplot(111, projection = '3d')

        X, Y, Z = [], [], []

        with open('30964ffc-a1c9-4afc-b06e-8aacdfc7b9bd_0.dat', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=';')

            next(plots)
            
            for x in plots:
                
                X.append(float(x[0]))
                Y.append(0)
                Z.append(float(x[4]))

        insertElementAltFirstStage(X, Z)

        ax.set_xlabel("Time (seconds)")
        ax.set_zlabel("Altitude (km)")

        ax.plot(X,Y,Z)

        canvas = FigureCanvasTkAgg(fig, lowerRightFrame)
        canvas.draw()
        canvas.get_tk_widget().grid()
        ax.mouse_init()

        #Velocity graph, 1st Stage

        fig2 = plt.Figure(figsize = (2.7, 2.7), dpi = 100)
        ax = fig2.add_subplot(111, projection = '3d')

        Q, R, S = [], [], []

        with open('30964ffc-a1c9-4afc-b06e-8aacdfc7b9bd_0.dat', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter = ';')

            next(plots)
            
            for x in plots:
                Q.append(float(x[0]))
                R.append(0)
                S.append(float(x[5]))

            insertElementVelFirstStage(Q, S)
                
            ax.set_xlabel("Time (seconds)")
            ax.set_zlabel("Velocity (mps)")

            ax.plot(Q,R,S)

            canvas2 = FigureCanvasTkAgg(fig2, lowerRightMostFrame)
            canvas2.draw()
            canvas2.get_tk_widget().grid()
            ax.mouse_init()

        #Altitude graph, 2nd Stage
    
        fig = plt.Figure(figsize = (2.7, 2.7), dpi = 100)
        ax = fig.add_subplot(111, projection = '3d')

        A, B, C = [], [], []

        with open('30964ffc-a1c9-4afc-b06e-8aacdfc7b9bd_1.dat', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=';')

            next(plots)
            
            for x in plots:
                
                A.append(float(x[0]))
                B.append(0)
                C.append(float(x[4]))

        insertElementAltSecondStage(A, C)

        ax.set_xlabel("Time (seconds)")
        ax.set_zlabel("Altitude (km)")

        ax.plot(A,B,C)

        canvas3 = FigureCanvasTkAgg(fig, lowestRightFrame)
        canvas3.draw()
        canvas3.get_tk_widget().grid()
        ax.mouse_init()

        #Velocity graph, 2nd Stage

        fig2 = plt.Figure(figsize = (2.7, 2.7), dpi = 100)
        ax = fig2.add_subplot(111, projection = '3d')

        T, U, V = [], [], []

        with open('30964ffc-a1c9-4afc-b06e-8aacdfc7b9bd_1.dat', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter = ';')

            next(plots)
            
            for x in plots:
                T.append(float(x[0]))
                U.append(0)
                V.append(float(x[5]))

        insertElementVelSecondStage(T, V)
                
        ax.set_xlabel("Time (seconds)")
        ax.set_zlabel("Velocity (mps)")

        ax.plot(T,U,V)

        canvas4 = FigureCanvasTkAgg(fig2, lowestRightMostFrame)
        canvas4.draw()
        canvas4.get_tk_widget().grid()
        ax.mouse_init()

    if flightNumInput.get() == '58':

        mainAPI2 = "https://www.flightclub.io:8443/FlightClub/api/v1/simulator/results/9f298ebd-f2d3-41d3-b687-5463baf40199" #api call to flightclub's json profile on
                                                                                                                            #CRS-12 launch.
        data2 = requests.get(mainAPI2).json()

        #firstStageTelem = data2['data'][0]['files'][0]['url']#navigates to the telemetry data file for the first stage in the json profile.

        #secondStageTelem = data2['data'][0]['files'][2]['url']#navigates to the telemetry data file for the seconds stage in the json profile.
        
        #webbrowser.open(firstStageTelem) #opens the telemetry data file for the first stage.

        #webbrowser.open(secondStageTelem) #opens the telemetry data file for the seconds stage.

        #Altitude graph, 1st Stage
    
        fig = plt.Figure(figsize = (2.7, 2.7), dpi = 100)
        ax = fig.add_subplot(111, projection = '3d')

        X, Y, Z = [], [], []

        with open('9f298ebd-f2d3-41d3-b687-5463baf40199_0.dat', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=';')

            next(plots)
            
            for x in plots:
                
                X.append(float(x[0]))
                Y.append(0)
                Z.append(float(x[4]))

        insertElementAltFirstStage(X, Z)

        ax.set_xlabel("Time (seconds)")
        ax.set_zlabel("Altitude (km)")

        ax.plot(X,Y,Z)

        canvas = FigureCanvasTkAgg(fig, lowerRightFrame)
        canvas.draw()
        canvas.get_tk_widget().grid()
        ax.mouse_init()

        #Velocity graph, 1st Stage

        fig2 = plt.Figure(figsize = (2.7, 2.7), dpi = 100)
        ax = fig2.add_subplot(111, projection = '3d')

        Q, R, S = [], [], []

        with open('9f298ebd-f2d3-41d3-b687-5463baf40199_0.dat', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter = ';')

            next(plots)
            
            for x in plots:
                Q.append(float(x[0]))
                R.append(0)
                S.append(float(x[5]))

        insertElementVelFirstStage(Q, S)
                
        ax.set_xlabel("Time (seconds)")
        ax.set_zlabel("Velocity (mps)")

        ax.plot(Q,R,S)

        canvas2 = FigureCanvasTkAgg(fig2, lowerRightMostFrame)
        canvas2.draw()
        canvas2.get_tk_widget().grid()
        ax.mouse_init()

        #Altitude graph, 2nd Stage
    
        fig = plt.Figure(figsize = (2.7, 2.7), dpi = 100)
        ax = fig.add_subplot(111, projection = '3d')

        A, B, C = [], [], []

        with open('9f298ebd-f2d3-41d3-b687-5463baf40199_1.dat', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=';')

            next(plots)
            
            for x in plots:
                
                A.append(float(x[0]))
                B.append(0)
                C.append(float(x[4]))

        insertElementAltSecondStage(A, C)

        ax.set_xlabel("Time (seconds)")
        ax.set_zlabel("Altitude (km)")

        ax.plot(A,B,C)

        canvas3 = FigureCanvasTkAgg(fig, lowestRightFrame)
        canvas3.draw()
        canvas3.get_tk_widget().grid()
        ax.mouse_init()

        #Velocity graph, 2nd Stage

        fig2 = plt.Figure(figsize = (2.7, 2.7), dpi = 100)
        ax = fig2.add_subplot(111, projection = '3d')

        T, U, V = [], [], []

        with open('9f298ebd-f2d3-41d3-b687-5463baf40199_1.dat', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter = ';')

            next(plots)
            
            for x in plots:
                T.append(float(x[0]))
                U.append(0)
                V.append(float(x[5]))

        insertElementVelSecondStage(T, V)
                
        ax.set_xlabel("Time (seconds)")
        ax.set_zlabel("Velocity (mps)")

        ax.plot(T,U,V)

        canvas4 = FigureCanvasTkAgg(fig2, lowestRightMostFrame)
        canvas4.draw()
        canvas4.get_tk_widget().grid()
        ax.mouse_init()

    if flightNumInput.get() == '59':

        mainAPI2 = "https://www.flightclub.io:8443/FlightClub/api/v1/simulator/results/d62f12c8-f3a9-44f7-818e-df4a602a8a2f" #api call to flightclub's json profile on
                                                                                                                            #CRS-12 launch.
        data2 = requests.get(mainAPI2).json()

        firstStageTelem = data2['data'][0]['files'][0]['url']#navigates to the telemetry data file for the first stage in the json profile.

        secondStageTelem = data2['data'][0]['files'][2]['url']#navigates to the telemetry data file for the seconds stage in the json profile.
        
        #webbrowser.open(firstStageTelem) #opens the telemetry data file for the first stage.

        #webbrowser.open(secondStageTelem) #opens the telemetry data file for the seconds stage.

        #Altitude graph, 1st Stage
    
        fig = plt.Figure(figsize = (2.7, 2.7), dpi = 100)
        ax = fig.add_subplot(111, projection = '3d')

        X, Y, Z = [], [], []

        with open('d62f12c8-f3a9-44f7-818e-df4a602a8a2f_0.dat', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=';')

            next(plots)
            
            for x in plots:
                
                X.append(float(x[0]))
                Y.append(0)
                Z.append(float(x[4]))

        insertElementAltFirstStage(X, Z)

        ax.set_xlabel("Time (seconds)")
        ax.set_zlabel("Altitude (km)")

        ax.plot(X,Y,Z)

        canvas = FigureCanvasTkAgg(fig, lowerRightFrame)
        canvas.draw()
        canvas.get_tk_widget().grid()
        ax.mouse_init()

        #Velocity graph, 1st Stage

        fig2 = plt.Figure(figsize = (2.7, 2.7), dpi = 100)
        ax = fig2.add_subplot(111, projection = '3d')

        Q, R, S = [], [], []

        with open('d62f12c8-f3a9-44f7-818e-df4a602a8a2f_0.dat', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter = ';')

            next(plots)
            
            for x in plots:
                Q.append(float(x[0]))
                R.append(0)
                S.append(float(x[5]))

        insertElementVelFirstStage(Q, S)
                
        ax.set_xlabel("Time (seconds)")
        ax.set_zlabel("Velocity (mps)")

        ax.plot(Q,R,S)

        canvas2 = FigureCanvasTkAgg(fig2, lowerRightMostFrame)
        canvas2.draw()
        canvas2.get_tk_widget().grid()
        ax.mouse_init()

        #Altitude graph, 2nd Stage
    
        fig = plt.Figure(figsize = (2.7, 2.7), dpi = 100)
        ax = fig.add_subplot(111, projection = '3d')

        A, B, C = [], [], []

        with open('d62f12c8-f3a9-44f7-818e-df4a602a8a2f_1.dat', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=';')

            next(plots)
            
            for x in plots:
                
                A.append(float(x[0]))
                B.append(0)
                C.append(float(x[4]))

        insertElementAltSecondStage(A, C)

        ax.set_xlabel("Time (seconds)")
        ax.set_zlabel("Altitude (km)")

        ax.plot(A,B,C)

        canvas3 = FigureCanvasTkAgg(fig, lowestRightFrame)
        canvas3.draw()
        canvas3.get_tk_widget().grid()
        ax.mouse_init()

        #Velocity graph, 2nd Stage

        fig2 = plt.Figure(figsize = (2.7, 2.7), dpi = 100)
        ax = fig2.add_subplot(111, projection = '3d')

        T, U, V = [], [], []

        with open('d62f12c8-f3a9-44f7-818e-df4a602a8a2f_1.dat', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter = ';')

            next(plots)
            
            for x in plots:
                T.append(float(x[0]))
                U.append(0)
                V.append(float(x[5]))

        insertElementVelSecondStage(T, V)
                
        ax.set_xlabel("Time (seconds)")
        ax.set_zlabel("Velocity (mps)")

        ax.plot(T,U,V)

        canvas4 = FigureCanvasTkAgg(fig2, lowestRightMostFrame)
        canvas4.draw()
        canvas4.get_tk_widget().grid()
        ax.mouse_init()

    if flightNumInput.get() == '60':
        
        mainAPI2 = "https://www.flightclub.io:8443/FlightClub/api/v1/simulator/results/212c569a-88fe-484d-879b-649f83ce7246" #api call to flightclub's json profile on
                                                                                                                            #CRS-12 launch.
        data2 = requests.get(mainAPI2).json()

        firstStageTelem = data2['data'][0]['files'][0]['url']#navigates to the telemetry data file for the first stage in the json profile.

        secondStageTelem = data2['data'][0]['files'][2]['url']#navigates to the telemetry data file for the seconds stage in the json profile.
        
        #webbrowser.open(firstStageTelem) #opens the telemetry data file for the first stage.

        #webbrowser.open(secondStageTelem) #opens the telemetry data file for the seconds stage.

        #Altitude graph, 1st Stage
    
        fig = plt.Figure(figsize = (2.7, 2.7), dpi = 100)
        ax = fig.add_subplot(111, projection = '3d')

        X, Y, Z = [], [], []

        with open('212c569a-88fe-484d-879b-649f83ce7246_0.dat', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=';')

            next(plots)
            
            for x in plots:
                
                X.append(float(x[0]))
                Y.append(0)
                Z.append(float(x[4]))

        insertElementAltFirstStage(X, Z)

        ax.set_xlabel("Time (seconds)")
        ax.set_zlabel("Altitude (km)")

        ax.plot(X,Y,Z)

        canvas = FigureCanvasTkAgg(fig, lowerRightFrame)
        canvas.draw()
        canvas.get_tk_widget().grid()
        ax.mouse_init()

        #Velocity graph, 1st Stage

        fig2 = plt.Figure(figsize = (2.7, 2.7), dpi = 100)
        ax = fig2.add_subplot(111, projection = '3d')

        Q, R, S = [], [], []

        with open('212c569a-88fe-484d-879b-649f83ce7246_0.dat', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter = ';')

            next(plots)
            
            for x in plots:
                Q.append(float(x[0]))
                R.append(0)
                S.append(float(x[5]))

        insertElementVelFirstStage(Q, S)
                
        ax.set_xlabel("Time (seconds)")
        ax.set_zlabel("Velocity (mps)")

        ax.plot(Q,R,S)

        canvas2 = FigureCanvasTkAgg(fig2, lowerRightMostFrame)
        canvas2.draw()
        canvas2.get_tk_widget().grid()
        ax.mouse_init()

        #Altitude graph, 2nd Stage
    
        fig = plt.Figure(figsize = (2.7, 2.7), dpi = 100)
        ax = fig.add_subplot(111, projection = '3d')

        A, B, C = [], [], []

        with open('212c569a-88fe-484d-879b-649f83ce7246_1.dat', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=';')

            next(plots)
            
            for x in plots:
                
                A.append(float(x[0]))
                B.append(0)
                C.append(float(x[4]))

        insertElementAltSecondStage(A, C)

        ax.set_xlabel("Time (seconds)")
        ax.set_zlabel("Altitude (km)")

        ax.plot(A,B,C)

        canvas3 = FigureCanvasTkAgg(fig, lowestRightFrame)
        canvas3.draw()
        canvas3.get_tk_widget().grid()
        ax.mouse_init()
    
        #Velocity graph, 2nd Stage

        fig2 = plt.Figure(figsize = (2.7, 2.7), dpi = 100)
        ax = fig2.add_subplot(111, projection = '3d')

        T, U, V = [], [], []

        with open('212c569a-88fe-484d-879b-649f83ce7246_1.dat', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter = ';')

            next(plots)
            
            for x in plots:
                T.append(float(x[0]))
                U.append(0)
                V.append(float(x[5]))

        insertElementVelSecondStage(T, V)
                
        ax.set_xlabel("Time (seconds)")
        ax.set_zlabel("Velocity (mps)")

        ax.plot(T,U,V)

        canvas4 = FigureCanvasTkAgg(fig2, lowestRightMostFrame)
        canvas4.draw()
        canvas4.get_tk_widget().grid()
        ax.mouse_init()

def clearData():

    rocketNameOutput.delete(0, END)
    launchDateOutput.delete(0, END)    
    flightNumInput.delete(0, END)
    detailsOutput.delete(1.0, END)
    canvas.get_tk_widget().destroy()
    canvas2.get_tk_widget().destroy()
    canvas3.get_tk_widget().destroy()
    canvas4.get_tk_widget().destroy()
    altitudeOtpt.delete(0, END)
    keyEntry.delete(0, END)
    velocityOtpt.delete(0, END)
    keyEntry2.delete(0, END)
    altitudeOtpt2ndStage.delete(0, END)
    velocityOtpt2ndStage.delete(0, END)


    

     ###############################################################################################################       

   

#GUI Code            

root = Tk()
root.geometry("1000x700")
root.resizable(0,0)

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label = "Flights with Full Data Available", menu = subMenu)
subMenu.add_command(label = "Flight 56 (PAZ & Microsat -2a, -2b)")
subMenu.add_command(label = "Flight 57 (Hispasat 30W-6)")
subMenu.add_command(label = "Flight 58 (Iridium NEXT-5)")
subMenu.add_command(label = "Flight 59 (CRS-14)")
subMenu.add_command(label = "Flight 60 (TESS)")
subMenu.add_separator()


#Title frame
topl = Frame(root, width = 995, height = 60, bd = 5, relief = "raise")
topl.grid()
topl.grid_propagate(False)

topLabel = Label(topl, text = "ROCKETS AND DATA AND DATA AND ROCKETS", font = ("helvetica", 30, "bold"))
topLabel.grid()

#API Data:

lowerLeftFrame = Frame(root, width = 55, height = 700, bd = 5, relief = "raise")
lowerLeftFrame.grid()
lowerLeftFrame.place(relx = 0.001, rely = 0.085)

lowestLeftFrame = Frame(root, width = 415, height = 125, bd = 5, relief = "raise")
lowestLeftFrame.grid()
lowestLeftFrame.grid_propagate(False)
lowestLeftFrame.place(relx = 0.001, rely = 0.82)

flightNumLabel = Label(lowerLeftFrame, text = "Enter flight number!", font = ("helvetica", 12))
flightNumLabel.grid()

flightNumInput = Entry(lowerLeftFrame, width = 5)
flightNumInput.grid()

retrieveData = Button(lowerLeftFrame, text = "Retrieve Data", command = DataSearch)
retrieveData.grid()

rocketName = Label(lowerLeftFrame, text = "Rocket Name:", font =("helvetica", 11))
rocketName.grid()

rocketNameOutput = Entry(lowerLeftFrame, width = 30)
rocketNameOutput.grid()

launchDate = Label(lowerLeftFrame, text = "Launch Date:", font = ("helvetica", 11))
launchDate.grid()

launchDateOutput = Entry(lowerLeftFrame, width = 30)
launchDateOutput.grid()

details = Label(lowerLeftFrame, text = "Mission Details:", font = ("helvetica", 11))
details.grid()

detailsOutput = Text(lowerLeftFrame, width = 50, height = 20, state = 'normal', wrap = WORD)
detailsOutput.grid()

#Hash Table GUI Section

lowestLeftFrame = Frame(root, width = 415, height = 125, bd = 5, relief = "raise")
lowestLeftFrame.grid()
lowestLeftFrame.grid_propagate(False)
lowestLeftFrame.place(relx = 0.001, rely = 0.82)

keyLabel = Label(lowestLeftFrame, text = "Enter a time in seconds, and get an altitude or velocity for 1st stage!", font = ("helvetica", 9))
keyLabel.grid()

keyEntryLabelAlt = Label(lowestLeftFrame, text = "Enter time:", font = ("helvetica", 7))
keyEntryLabelAlt.grid()
keyEntryLabelAlt.place(relx = 0.01, rely = 0.2)
 
keyEntry = Entry(lowestLeftFrame, width = 5)
keyEntry.grid()
keyEntry.place(relx = 0.14, rely = 0.2)

altRetrieve = Button(lowestLeftFrame, text = "Get Altitude", font = ("helvetica", 7), command = searchValueAltFirstStage)
altRetrieve.grid()
altRetrieve.place(relx = 0.21, rely = 0.2)

altitudeLabel = Label(lowestLeftFrame, text = "Altitude:", font = ("helvetica", 7))
altitudeLabel.grid()
altitudeLabel.place(relx = 0.35, rely = 0.2)

altitudeOtpt = Entry(lowestLeftFrame, width = 7)
altitudeOtpt.grid()
altitudeOtpt.place(relx = 0.45, rely = 0.2)

velRetrieve = Button(lowestLeftFrame, text = "Get Velocity", font = ("helvetica", 7), command = searchValueVelFirstStage)
velRetrieve.grid()
velRetrieve.place(relx = 0.57, rely = 0.2)

velocityLabel = Label(lowestLeftFrame, text = "Velocity:", font = ("helvetica", 7))
velocityLabel.grid()
velocityLabel.place(relx = 0.72, rely = 0.2)

velocityOtpt = Entry(lowestLeftFrame, width = 7)
velocityOtpt.grid()
velocityOtpt.place(relx = 0.82, rely = 0.2)

keyLabel2 = Label(lowestLeftFrame, text = "Enter a time in seconds, and get an altitude or velocity for 2nd stage!", font = ("helvetica", 9))
keyLabel2.grid()
keyLabel2.place(relx = 0, rely = 0.4)

keyEntry2Label = Label(lowestLeftFrame, text = "Enter time:", font = ("helvetica", 7))
keyEntry2Label.grid()
keyEntry2Label.place(relx = 0.01, rely = 0.6)

keyEntry2 = Entry(lowestLeftFrame, width = 5)
keyEntry2.grid()
keyEntry2.place(relx = 0.14, rely = 0.6)

altRetrieve2ndStage = Button(lowestLeftFrame, text = "Get Altitude", font = ("helvetica", 7), command = searchValueAltSecondStage)
altRetrieve2ndStage.grid()
altRetrieve2ndStage.place(relx = 0.21, rely = 0.6)

altitudeLabel2ndStage = Label(lowestLeftFrame, text = "Altitude:", font = ("helvetica", 7))
altitudeLabel2ndStage.grid()
altitudeLabel2ndStage.place(relx = 0.35, rely = 0.6)

altitudeOtpt2ndStage = Entry(lowestLeftFrame, width = 7)
altitudeOtpt2ndStage.grid()
altitudeOtpt2ndStage.place(relx = 0.45, rely = 0.6)

velRetrieve2ndStage = Button(lowestLeftFrame, text = "Get Velocity", font = ("helvetica", 7), command = searchValueVelSecondStage)
velRetrieve2ndStage.grid()
velRetrieve2ndStage.place(relx = 0.57, rely = 0.6)

velocityLabel2ndStage = Label(lowestLeftFrame, text = "Velocity:", font = ("helvetica", 7))
velocityLabel2ndStage.grid()
velocityLabel2ndStage.place(relx = 0.72, rely = 0.6)

velocityOtpt2ndStage = Entry(lowestLeftFrame, width = 7)
velocityOtpt2ndStage.grid()
velocityOtpt2ndStage.place(relx = 0.82, rely = 0.6)


#File Data:

firstStageLabel = Label(root, text = "First Stage Data", font = ("helvetica", 12))
firstStageLabel.grid()
firstStageLabel.place(relx = 0.42, rely = 0.085)

lowerRightFrame = Frame(root, width = 281, height = 285, bd = 5, relief = "raise")
lowerRightFrame.grid()
lowerRightFrame.place(relx = 0.42, rely = 0.125)

lowerRightMostFrame = Frame(root, width = 281, height = 285, bd = 5, relief = "raise")
lowerRightMostFrame.grid()
lowerRightMostFrame.place(relx = 0.712, rely = 0.125)

secondStageLabel = Label(root, text = "Second Stage Data", font = ("helvetica", 12))
secondStageLabel.grid()
secondStageLabel.place(relx = 0.42, rely = 0.545)

deleteData = Button(root, text = "Clear Data", command = clearData)
deleteData.grid()
deleteData.place(relx = 0.67, rely = 0.545)

lowestRightFrame = Frame(root, width = 281, height = 285, bd = 5, relief = "raise")
lowestRightFrame.grid()
lowestRightFrame.place(relx = 0.42, rely = 0.590)

lowestRightMostFrame = Frame(root, width = 281, height = 285, bd = 5, relief = "raise")
lowestRightMostFrame.grid()
lowestRightMostFrame.place(relx = 0.712, rely = 0.590)

root.mainloop()
