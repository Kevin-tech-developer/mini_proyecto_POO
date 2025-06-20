'''
Simula un inicio de sesión simple. El programa debe verificar un nombre de usuario y una contraseña.

Si ambos son correctos (usuario: "admin", contraseña: "12345"), imprime "Acceso concedido".
Si el nombre de usuario es correcto pero la contraseña no, imprime "Contraseña incorrecta".
Si el nombre de usuario es incorrecto, imprime "Usuario no encontrado".
'''
usuario = ["kevin", "brayan", "eimy"]
contraseña = [1234, 4325, 5839]

while(True):
    usuariodev = input("ingrese el usuario: ")
    contraseñadev = int(input("digite la contraseña: "))
    verda1 = False
    verda2 = False
    for i in usuario:
        if(i == usuariodev):
            verda1 = True
    if(verda1):
        for i in contraseña:
            if(i == contraseñadev):
                verda2 = True
        if(verda2):
            print("vienvenido al home de dev senior")
            break
        else:
            print("contraseña incorrecta") 
    else:
        print("usuario incorrecto")