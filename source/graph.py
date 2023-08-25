import tkinter
import customMath

# setup root
global root
root = tkinter.Tk()

root.title("Graphing Calculator")

# idk
global out
out = 0

# config
global method
method = 3

"""
General Notes:
future companies and others be looking at my code and see this mess I would get arrested LOL
hope certain group doesn't see this when considering this
anyways PEP8 standard lovers gonna burn me at the stake bye yall
"""

"""
Method Settings:
method = 2
Fastest current method
Third method soon to fix irrational graphing problem and approx

Method 1:
Go through each pixel and sees if pair fits (bro what)

Method 2:
Goes to each x value and gets the val 

Method 3: [EXPERIMENTAL KINDA WORKS]
Method 1 but also decimals are accounted for via a special version of rounding. Unit parameter is required
unit=5 seems to be a sweet spot for pConstant = 0.1
Current settings are good for method 3
"""

"""
Syntax is space seperated because im stupid
may change another day
but example:
2x+1
2 * x + 1
"""

def reset(dimensions, system, n, unit, environment):
    p = GraphingCalculator(dimensions, system, n, unit, environment)

# Normal Math Graphing Calculator #

class GraphingCalculator(object):
    def __init__(self, dimensions=300, system=int, n="int", unit=1, environment=customMath.BaseIntegerEnvironment):
        # primitive definitions
        self.equation = ""
        self.dim = dimensions
        self.stopFlag = False
        self.unit = unit
        self.environment = environment
        self.pConstant = 0.01 # i'll make this more customizable later

        # math def
        self.system = system
        self.n = n
        self.tokenEq = []
        self.acceptedChars = [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "x",
            "X",
            "+",
            "-",
            "/",
            "*",
            "^",
            " ",
            "",
            ".",
            "(", # Deal with these two later
            ")" # Deal with these two later
        ]

        # complex def
        self.canvas = tkinter.Canvas(root, bg="white", height=dimensions, width=dimensions)
        self.equationBox = tkinter.Text(root, height=1, width=dimensions//7)
        self.equationGo = tkinter.Button(root, text="Graph", command=self.graph)
        self.resetButton = tkinter.Button(root, text="Reset Graph", command=self.resetGraph)

        # Coord Plane
        xAxis = self.canvas.create_rectangle(1, dimensions//2, dimensions, dimensions//2, fill="black")
        yAxis = self.canvas.create_rectangle(dimensions//2, 1, dimensions//2, dimensions, fill="black")

        # packing
        self.equationBox.pack()
        self.equationGo.pack()
        self.resetButton.pack()
        self.canvas.pack()
        root.mainloop()

    def graph(self):
        global method
        x1, y1 = 0, 0

        self.equation = self.equationBox.get("1.0", "end-1c")

        # --- Method 1 --- #
        if method not in [1, 2, 3]:
            method = 1
        if method == 1:
            for i in range(self.dim):
                for j in range(self.dim):
                    x1, y1 = self.getCord(i, j)
                    if self.useEq(x1, self.getEquation()) == y1:
                        idk = self.canvas.create_rectangle(i, j, i, j, fill="red")
        if method == 2: # works now
            for i in range(1, self.dim+1):
                x1, y1 = self.getCord(i, i)
                x1, y1 = self.getCord(i, self.useEq(x1, self.getEquation())) # redundant but idc
                idk = self.canvas.create_rectangle(i, y1, i, y1, fill="red")
        if method == 3:
            for i in range(self.dim):
                for j in range(self.dim):
                    x1, y1 = self.getCord(i, j)
                    x1 /= self.unit
                    y1 /= self.unit
                    # print(x1, y1)
                    if self.useEq(x1, self.getEquation()) == y1:
                        idk = self.canvas.create_rectangle(i, j, i, j, fill="red")
                    elif abs(self.useEq(x1, self.getEquation()) - y1) <= self.pConstant:
                        # print("yes")
                        idk = self.canvas.create_rectangle(i, j, i, j, fill="red")


    def getEquation(self):
        self.stopFlag = False

        # -- Illegal Check -- #
        for i in range(len(self.equation)):
            if self.equation[i] not in self.acceptedChars:
                self.stopFlag = True
                return

        # -- Paren. Check -- #
        "Do Later"

        # -- Interpret -- #

        "Via the WTF algorithm"

        self.tokenEq = self.equation.split(" ")
        pEquation = self.equation.split(" ")
        varLength = 1
        retEq = []
        aLoc = dict()
        for i in range(len(self.tokenEq)):
            if self.tokenEq[i].isdigit():
                self.tokenEq[i] = self.system(pEquation[i])
                retEq.append("a" * varLength)
                aLoc[varLength] = i
                varLength += 1
                continue
            retEq.append(self.tokenEq[i])

        # -- Assemble -- #
        bgStatement = ""
        for i in range(1, varLength):
            if varLength == 1:
                break
            bgStatement += "a" * i + "=" + self.n + "(" + pEquation[aLoc[i]] + ");"

        retStatement = "global out;" + bgStatement + "out += " + "".join(retEq)
        return retStatement

    def useEq(self, x, eq): # worst code ever bruh
        global out
        out = 0

        try:
            exec(eq)
        except ZeroDivisionError:
            out = 0
        except TypeError:
            pass

        return out

    def getCord(self, x, y):
        return (x - self.dim // 2)/self.unit, (-y + self.dim // 2)/self.unit

    def resetGraph(self): # worst coding practice ever LOL
        global root

        root.destroy()

        root = tkinter.Tk()
        root.title("Graphing Calculator")

        reset(self.dim, self.system, self.n, self.unit, self.environment)

if __name__ == "__main__":
    e = GraphingCalculator(unit=10, system=float, dimensions=300)
