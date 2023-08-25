# --- Environment --- #

"""
Environment is a system of axioms.

Old system: Coeff defined by variables
New systems: Coeff defined in environment
"""

# --- Base Class --- #

"""
The most used base class is the integer.
After that, there is the float.
Base classes will also have system for float and maybe complex
"""

class BaseIntegerEnvironment(object):
    def __init__(self):
        self.systemConstant = int  # CONSTANT PER DOCUMENTATION
        
        self.variables = {}  # replace "aaa" variable algorithm

#--- Different Mathematical/Logical Systems --- #
