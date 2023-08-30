# --- Environment --- #

"""
Environment is a system of axioms.

Old system: Coeff defined by variables
New systems: Coeff defined in environment
"""

# Something IDK

# --- Base Class --- #

"""
The most used base class is the integer.
After that, there is the float.
Base classes will also have system for float and maybe complex
"""

class BaseIntegerEnvironment(object):
    def __init__(self):
        self.systemConstant = int  # CONSTANT PER DOCUMENTATION
        self.systemConstantName = "int"  # may become obsolete soon

        self.constants = {}  # replace "aaa" variable algorithm (WTF Algorithm)

        self.variables = {}  # these change, like x and y. constants are coeff.
        
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
            "(",  # Deal with these two later
            ")"  # Deal with these two later
        ]

        # I would define different templates and stuff but ehh i'm lazy

    def addConstant(self, arg, name):
        self.constants[name] = arg

    def addVariable(self, arg, name):
        self.variables[name] = arg
    
    # --- MIGRATION --- #
    # BEGIN MIGRATING EQUATIONS AND INTERPRETATION INTO ENVIRONMENTS


class FloatEnvironment(BaseIntegerEnvironment):
    def __init__(self):
        super(FloatEnvironment, self).__init__(())
        # get template from previous
        
        self.systemConstant = float
        self.systemConstantName = "float"
        

#--- Different Mathematical/Logical Systems --- #

class ComplexEnvironmentX(BaseIntegerEnvironment):
    pass

class ComplexEnvironmentXY(BaseIntegerEnvironment):  # heat map
    pass

class ModularEnvironment(BaseIntegerEnvironment):  # modular addition and stuf
    pass
