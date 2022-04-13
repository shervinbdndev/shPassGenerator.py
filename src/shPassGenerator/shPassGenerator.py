try:
    import io
    import os
    import random
    
except:
    import sys;\
    sys.exit(0)
    





class Version:
    def __init__(self) -> None:
        super(Version , self).__init__()
        
        self.version = r""
        with io.open(file=os.path.join(os.path.abspath('.') , 'version.txt') , mode='r+' , encoding='utf-8' , errors=None) as temp:
            self.version = temp.readline()
                
    def __str__(self) -> str:
        return self.version






class Utils:
    LOWERCASE = r"abcdefghijklmnopqrstuvwxyz"
    UPPERCASE = r"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    CHARACTERS = fr"{LOWERCASE}{UPPERCASE}"
    NUMERIC = r"0123456789"
    OCTALDIGITS = r"01234567"
    HEXADIGITS = fr"{NUMERIC}abcdefABCDEF"
    SYMBOLS = r"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"





class GeneratePass(Utils):
    def __init__(self , length=None , chars=None , lowercase=None , uppercase=None , numbers=None , symbols=None , octal=None , hexa=None) -> None:
        """_summary_

        Args:
            length (int): Set The Length of your Password (Max Length is Unlimited)
            chars (bool): Use Lowercase & Uppercase Characters in Your Password
            lowercase (bool): Use Lowercase Characters in Your Password
            uppercase (bool): Use Uppercase Characters in Your Password
            numbers (bool): Use Numbers in Your Password
            symbols (bool): Use Symbols in Your Password
            octal (bool): Use Octal Characters in Your Password
            hexa (bool): Use Hexa Characters in Your Password
        """
        super(GeneratePass , self).__init__()
        
        self.length : int = length
        self.chars : bool = chars
        self.lowercase : bool = lowercase
        self.uppercase : bool = uppercase
        self.numbers : bool = numbers
        self.symbols : bool = symbols
        self.octal : bool = octal
        self.hexa : bool = hexa
        self.password : str = r""
        
    def __str__(self) -> str:
        super(GeneratePass , self).__str__()
        
        if (type(self.length) is int):
            if (self.chars is True):
                self.password += self.CHARACTERS
                if (self.lowercase is True):
                    self.password += self.LOWERCASE
                elif (self.uppercase is True):
                    self.password += self.UPPERCASE
                elif (self.numbers is True):
                    self.password += self.NUMERIC
                elif (self.symbols is True):
                    self.password += self.SYMBOLS
                elif (self.octal is True):
                    self.password += self.OCTALDIGITS
                elif (self.hexa is True):
                    self.password += self.HEXADIGITS
            elif (self.lowercase is True):
                self.password += self.LOWERCASE
                if (self.chars is True):
                    self.password += self.CHARACTERS
                elif (self.uppercase is True):
                    self.password += self.UPPERCASE
                elif (self.numbers is True):
                    self.password += self.NUMERIC
                elif (self.symbols is True):
                    self.password += self.SYMBOLS
                elif (self.octal is True):
                    self.password += self.OCTALDIGITS
                elif (self.hexa is True):
                    self.password += self.HEXADIGITS
            elif (self.uppercase is True):
                self.password += self.UPPERCASE
                if (self.chars is True):
                    self.password += self.CHARACTERS
                elif (self.lowercase is True):
                    self.password += self.LOWERCASE
                elif (self.numbers is True):
                    self.password += self.NUMERIC
                elif (self.symbols is True):
                    self.password += self.SYMBOLS
                elif (self.octal is True):
                    self.password += self.OCTALDIGITS
                elif (self.hexa is True):
                    self.password += self.HEXADIGITS
            elif (self.numbers is True):
                self.password += self.NUMERIC
                if (self.chars is True):
                    self.password += self.CHARACTERS
                elif (self.lowercase is True):
                    self.password += self.LOWERCASE
                elif (self.uppercase is True):
                    self.password += self.UPPERCASE
                elif (self.symbols is True):
                    self.password += self.SYMBOLS
                elif (self.octal is True):
                    self.password += self.OCTALDIGITS
                elif (self.hexa is True):
                    self.password += self.HEXADIGITS
            elif (self.symbols is True):
                self.password += self.SYMBOLS
                if (self.chars is True):
                    self.password += self.CHARACTERS
                elif (self.lowercase is True):
                    self.password += self.LOWERCASE
                elif (self.uppercase is True):
                    self.password += self.UPPERCASE
                elif (self.numbers is True):
                    self.password += self.NUMERIC
                elif (self.octal is True):
                    self.password += self.OCTALDIGITS
                elif (self.hexa is True):
                    self.password += self.HEXADIGITS
            elif (self.octal is True):
                self.password += self.OCTALDIGITS
                if (self.chars is True):
                    self.password += self.CHARACTERS
                elif (self.lowercase is True):
                    self.password += self.LOWERCASE
                elif (self.uppercase is True):
                    self.password += self.UPPERCASE
                elif (self.numbers is True):
                    self.password += self.NUMERIC
                elif (self.symbols is True):
                    self.password += self.SYMBOLS
                elif (self.hexa is True):
                    self.password += self.HEXADIGITS
            elif (self.hexa is True):
                self.password += self.HEXADIGITS
                if (self.chars is True):
                    self.password += self.CHARACTERS
                elif (self.lowercase is True):
                    self.password += self.LOWERCASE
                elif (self.uppercase is True):
                    self.password += self.UPPERCASE
                elif (self.numbers is True):
                    self.password += self.NUMERIC
                elif (self.symbols is True):
                    self.password += self.SYMBOLS
                elif (self.octal is True):
                    self.password += self.OCTALDIGITS
            else:
                raise None
            return r''.join([str(password) for password in random.sample(population=[random.choice(seq=self.password) for inner_password in range(self.length)] , k=self.length)])