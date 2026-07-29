from tkinter import Menu, messagebox

LOC = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']

class menubar():
    def ver(self, window_context):
        import requests
        import json
        url = "https://ubiquitous-figolla-2037da.netlify.app/variable.json"

        response = requests.get(url, timeout=5)

        license_server = response.json()

        with open("license.json", "r") as license:
            license_read =  json.load(license)

        if license_read['user'] not in license_server['license']:
            messagebox.showerror("You are in some trouble", "Get out, dont even try to battle it.")
            window_context.destroy()
            exit
        else:
            return Menu(window_context)

verification = menubar()

