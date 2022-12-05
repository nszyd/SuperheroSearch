from os import system
from re import search
import requests
from IPython.display import display
import pandas as pd
from tkinter import *
from tkinter.ttk import * 
import json
from PIL import ImageTk, Image
import urllib.request


def newWindow(charName, charRace, charStrength, charIntelligence, charSpeed, charCombat, pImage):
	root = Tk()
	root.geometry("300x500")
	root.title("Superhero Search")
	frame = Frame(root)
	frame.pack()
	charNameLabel = Label(frame, text = "Character Name: ")
	charNameLabel.pack()
	superName = Label(frame, text = charName)
	superName.pack()
	charRaceLabel = Label(frame, text = "Character Race: ")
	charRaceLabel.pack()
	superRace = Label(frame, text = charRace)
	superRace.pack()
	charStrengthLabel = Label(frame, text = "Character Strength: ")
	charStrengthLabel.pack()
	superStrength = Label(frame, text = charStrength)
	superStrength.pack()
	charIntelligenceLabel = Label(frame, text = "Character Intelligence: ")
	charIntelligenceLabel.pack()
	superIntelligence = Label(frame, text = charIntelligence)
	superIntelligence.pack()
	charSpeedLabel = Label(frame, text = "Character Speed: ")
	charSpeedLabel.pack()
	superSpeed = Label(frame, text = charSpeed)
	superSpeed.pack()
	charCombatLabel = Label(frame, text = "Character Combat: ")
	charCombatLabel.pack()
	superCombat = Label(frame, text=charCombat)
	superCombat.pack()
	python_image = ImageTk.PhotoImage(pImage)#Convert Image from JPG to correct form -- I think
	superImageLabel = Label(frame, image=python_image)#Display the Image
	superImageLabel.pack()
	root.mainloop()



def storeInfo():
	system('cls')
	print("Superhero Search V1.0")
	searchTerm = input("Enter the Hero's Name: ")
	url = "https://superhero-search.p.rapidapi.com/api/"
	querystring = {"hero":f"{searchTerm}"}
	headers = {
	"X-RapidAPI-Key": "API KEY HERE",
	"X-RapidAPI-Host": "superhero-search.p.rapidapi.com"
	}
	response = requests.request("GET", url, headers=headers, params=querystring)
	properties_dict = response.json()['appearance']

	charName = response.json()['name']
	charRace = response.json()['appearance']['race']
	charStrength = response.json()['powerstats']['strength']
	charIntelligence = response.json()['powerstats']['intelligence']
	charSpeed = response.json()['powerstats']['speed']
	charCombat = response.json()['powerstats']['combat']
	charImage = response.json()['images']['sm'] #Store Image URL
	pImage = Image.open(requests.get(charImage, stream=True).raw)  #Open URL using Pillow, Create an image from it 
	newWindow(charName, charRace, charStrength, charIntelligence, charSpeed, charCombat, pImage)



storeInfo()
