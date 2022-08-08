'''
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
	Programado por
		Domingo Vaca Nieves 
  		2022

*-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
'''

import os, platform, time
from colorama import Fore, Style, Back

class Functions:
    def __init__(self) -> None:
        self.Systems:tuple= ("Windows", "Linux", "MacOs")
        self.styles:tuple= ("Classic", "Commodore", "Basic", "Green")

        self.DecoreLine= lambda: print("*" * 64)
        self.CenterLine= lambda msg: print(" " * ((64 - len(msg))//2) + msg)
        self.Stop= lambda tm: time.sleep(tm)

        if platform.platform() == self.Systems[1] or self.styles[2]:
            self.Clear= lambda: os.system("clear")
            self.Pause= lambda: input("Press [Enter] to continue...")
            self.Title= lambda title: os.system(f"xtitle {title}")
        else:
            self.Clear= lambda: os.system("cls")
            self.Pause= lambda: os.system("pause")
            self.Title= lambda title: os.system(f"title {title}")

    def _Style(self, style:str) -> None:
        assert type(style) == str, print(f"{style} don't is a string")

        if style == self.styles[0]:
            print(Fore.WHITE, Back.BLACK)
            self.Clear()
        elif style == self.styles[1]:
            print(Fore.CYAN, Back.BLUE, Style.BRIGHT)
            self.Clear()
        elif style == self.styles[2]:
            print(Fore.YELLOW, Back.CYAN, Style.BRIGHT)
            self.Clear()
        elif style == self.styles[3]:
            print(Fore.GREEN, Back.BLACK)
            self.Clear()
        else:
            print(f"'{style}' don't is a style")

    def Mdl_Creator(self) -> str:
        self.Creador= "Domingo Vaca Nives"
        return self.Creador
    
    def Mdl_Version(self) -> str:
        self.Vercion = "v4.8"
        return self.Vercion

if __name__ == "__main__":
	funcion= Functions()

	funcion.Title("Module of Functions: " + funcion.Mdl_Creator())


	funcion.Clear()

	funcion.DecoreLine()
	funcion.CenterLine("All correct....")
	funcion.DecoreLine()

	print("About to module: ")

	print("Running in: ", Fore.BLUE + platform.platform(), Fore.RESET)


	print("Module version: ", Fore.CYAN + funcion.Mdl_Version(), Fore.RESET)
	print("Module creator: ", Fore.GREEN + funcion.Mdl_Creator(), Fore.RESET )
	funcion.Pause()
	funcion.Clear()