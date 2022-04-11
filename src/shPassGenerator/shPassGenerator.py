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
    def __init__(self , length : int) -> None:
        """_summary_

        Args:
            length (int): Set The Length of your Password (Max Length is 174 Characters)
        """
        super(GeneratePass , self).__init__()
        
        self.length = length
        
    def __str__(self) -> str:
        super(GeneratePass , self).__str__()
        
        if (type(self.length) is int):
            return ''.join([str(password) for password in random.sample(fr"{self.LOWERCASE}{self.UPPERCASE}{self.CHARACTERS}{self.NUMERIC}{self.OCTALDIGITS}{self.HEXADIGITS}{self.SYMBOLS}" , self.length)])