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

        self.constants = {}  # replace "aaa" variable algorithm (WTF Algorithm)

        self.variables = {}  # these change, like x and y. constants are coeff.
        
        # I would define different templates and stuff but ehh i'm lazy

#--- Different Mathematical/Logical Systems --- #
