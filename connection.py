from tkinter import Menu, messagebox # importing the framework to return the Menu(vistas) when legally gotten

class menubar():
    def ver(self, window_context):
        import requests # importing requests for getting the legal licenses from the server
        import json # importing json to get the license
        url = "https://ubiquitous-figolla-2037da.netlify.app/variable.json" # the server, you need to replace it with your own

        response = requests.get(url, timeout=5) # getting the response from the server

        license_server = response.json() # getting the json out of the server

        with open("license.json", "r") as license: # opening the entered license
            license_read =  json.load(license) # getting the users license

        if license_read['user'] not in license_server['license']: # if user doesnt have a real license
            messagebox.showerror("You are in some trouble", "Get out, dont even try to battle it.") # show them an error message
            window_context.destroy() # destroy the vistas
        else: # if user has a real license
            return Menu(window_context) # return vistas so the app wont crash

verification = menubar() # tech stuff

