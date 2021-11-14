from math import floor
from shutil import get_terminal_size


##### PROGRESS BAR #####
class ProgressBar:
    progress = 0
    ratio = 0
    sincelastdraw=999999999
    sincelastupdate=999999999
    def __init__(self, title, total, chunks=30, value=0, empty=" ", filled="\u25a0", leftbracket="[", rightbracket="]", callstoupdate=50000, callstoforceupdate=100000):
        self.title = title
        self.total = total
        self.chunks = chunks
        self.empty = empty
        self.filled = filled
        self.leftbracket = leftbracket
        self.rightbracket = rightbracket
        self.callstoupdate = callstoupdate
        self.callstoforceupdate = callstoforceupdate
        self.Draw()
        self.Update(value)


    def Draw(self):
        size = get_terminal_size((80, 24))
        string = f"{self.title} {self.leftbracket}{self.filled*self.progress}{self.empty*(self.chunks-self.progress)}{self.rightbracket} ({100*self.ratio:.1f}%)"
        if len(string) > size[0]:
            string = string[:size[0]-3] + " >>"
        print(string, end="\r")
        self.sincelastdraw = 0

    def Update(self, value):
        if self.sincelastupdate >= self.callstoupdate:
            value = max(min(value, self.total), 0)
            self.ratio = value/self.total
            newprogress = floor(self.chunks*self.ratio)

            if self.sincelastdraw >= self.callstoforceupdate or newprogress > self.progress:
                self.progress = newprogress
                self.Draw()
            self.sincelastupdate = 0
        self.sincelastdraw += 1
        self.sincelastupdate += 1

    def Complete(self):
        self.ratio = 1.0
        self.progress = self.chunks
        self.Draw()
        print()

##### SELECTION MENU #####
def PrintHelp(name, options):
    print(f"-- {name} help --")
    for option in options:
        print(f"{option['name']}: {option['desc']}")
        print(f"\t{option['aliases']}")

#the default options that are added to every selection menu
DEFAULTOPTIONS = [
            {"name": "Quit", "aliases": ["quit", "q"], "desc": "Quits this selection menu", "func":lambda args:-1},
            {"name": "Help", "aliases": ["help", "h", "?"], "desc": "Displays information about this selection menu", "func":PrintHelp}
        ]

def SelectionMenu(useroptions, name="Menu", prompt=">"):
    options = useroptions + DEFAULTOPTIONS
    checkres = SelectionMenu_CheckOptions(options)
    if checkres != 0:
        print(f"SelectionMenu Error: Invalid options; {checkres} is a collision")
    
    retval = None 
    while retval == None:
        cmd, *args = input(prompt).lower().split(" ")
        for option in options:
            if cmd in option["aliases"]:
                if option["name"] == "Help":
                    PrintHelp(name, options)
                else:
                    retval = option["func"](args)

def SelectionMenu_CheckOptions(options):
    # if there is a collision in names/aliases, this function returns the first collision it finds
    # if there are no collisions, it returns 0
    words = []
    validOptions = True
    for option in options:
        for alias in option["aliases"]:
            if alias in words:
                return alias
            else:
                words.append(alias)
    return 0

def test_ProgressBar():
    N=9999999
    import time
    nobarstart = time.perf_counter()
    n=N
    x=0
    while x<n:
        x+=1
    nobarend = time.perf_counter()
    print(f"nobar: {nobarend-nobarstart}")

    barstart = time.perf_counter()
    n=N
    pb = ProgressBar("Doing", n)
    x=0
    while x<n:
        x+=1
        pb.Update(x)
    pb.Complete()
    barend = time.perf_counter()
    print(f"bar: {barend-barstart}")

def test_SelectionMenu():
    def TestOption(args):
        print("test option's function is working")
    options = [
                {"name": "testoption", "desc": "this is a test option", "aliases": ["testoption","test","t","testop"], "func":TestOption}
            ]
    SelectionMenu(options)

def main():
    #test_ProgressBar()
    test_SelectionMenu()

if __name__ == "__main__":
    main()
