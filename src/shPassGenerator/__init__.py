from shPassGenerator import GeneratePass


print(f"This Password is Strong : {GeneratePass(length=16 , lowercase=True)}")
print(f"This Password is Strong too : {GeneratePass(length=50 , chars=True , symbols=True)}")