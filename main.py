import requests
from bs4 import BeautifulSoup
from colorama import Fore

class Gtfobins:

    def __init__(self):
        self.url = f"https://gtfobins.github.io/gtfobins/"

    def Eploit(self ,  binarise):
        response = requests.get(self.url + binarise)
        if response.status_code == 200:
            response = response.text
            soup = BeautifulSoup(response, "html.parser")
            sections = soup.find_all("h2", id=True)

            for section in sections:
                title = section.get_text()
                description = section.find_next("p").get_text() if section.find_next("p") else "No description"
                code_examples = [code.get_text() for code in section.find_next("ul", class_="examples").find_all("code")]
                print(f"- {Fore.GREEN} {title} {Fore.WHITE}\n")
                print(f"> {Fore.RED}Description {Fore.WHITE}: \n{description}\n> {Fore.RED}Commands {Fore.WHITE}: ")
                for example in code_examples:
                    print(f"\n-{Fore.RED} {example.strip()}")
                print("\n" + "-"*40 + "\n")
        else:
            print(f"{Fore.RED}Error {Fore.WHITE}: {binarise} not found")

logo = fr"""{Fore.RED}
              ______________________________________ __________.__               
             /  _____/\__    ___/\_   _____/\_____  \\______   \__| ____   ______
            /   \  ___  |    |    |    __)   /   |   \|    |  _/  |/    \ /  ___/
            \    \_\  \ |    |    |     \   /    |    \    |   \  |   |  \\___ \ 
             \______  / |____|    \___  /   \_______  /______  /__|___|  /____  >
                    \/                \/            \/       \/        \/     \/ 
        
    {Fore.WHITE}< {Fore.BLUE}GTFOBins is a curated list of Unix binaries that can be used to bypass local security restrictions in misconfigured systems. >{Fore.WHITE}
    
"""
for _ in logo.splitlines():
    print(_)

while True:
    gtfo = Gtfobins()
    exploit = input(f"{Fore.WHITE}> Enter Binary for get Exploit ex:(python , bash , php , ... ) $ ")
    gtfo.Eploit(exploit)