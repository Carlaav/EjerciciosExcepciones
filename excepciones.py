import re
class usuario:
    def __innit__(self,correo,contraseña):
        self.correo=correo
        self.contraseña=contraseña
    def logIn(self):
        email=str(input("introduzca su direccion de correo:"))
    while True:
        try:
            if email=="":
             raise Exception(email,"Es una entrada incorrecta")
            elif re.search(". * @. * \ .. *", email) is None:
             raise Exception("Una dirección de correo electrónico debe tener el formato xxx@xxx.xx" )
            else:
                if email==self.correo:
                    print("Bienvenido", self.nombre)
                    break
                else:
                    raise Exception("Cuenta bloqueada a causa de un ataque")
        except Exception as e:
            print(str(e))
            if str(e)=="Cuenta bloquada a causa de un ataque":
                break
        email=str(input("Introduce su direccion de correo"))
            
user=usuario("pepe","pepe@gmail.com")
user.logIn()