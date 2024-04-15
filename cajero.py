### **Cajero Automático**

'''Diseñar un simulador de cajero automático, el mismo debe permitir ingresar dinero,
retirar dinero, consultar saldo, hacer transferencia, y debe contener más de una cuenta 
permitiendo seleccionar desde cual se desea retirar. 
El mismo debe poseer una contraseña de acceso pedida al 
usuario al momento de iniciar el programa.'''

usuarios = { 
            'usuario1':{'contraseña': 'pasword1', 'saldo': 1000},
            'usuario2':{'contrasena': 'pasword2', 'saldo': 2000},
            'usuario3':{'contrasena': 'pasword3', 'saldo': 3000}
}
"""Verifica si el usuario y la contraseña son correctos."""
def verificar_usuario(usuario, contraseña):
    return usuario in usuarios and usuarios[usuario]['contraseña'] == contraseña


"""Consulta el saldo de un usuario."""
def consultar_saldo(usuario):
    return usuarios[usuario]['saldo']

"""Retira dinero de la cuenta de un usuario."""
def retirar_dinero(usuario, cantidad):
    if cantidad > usuarios[usuario]['saldo']:
        return "Saldo insuficiente"
    usuarios[usuario]['saldo'] -= cantidad
    return f"Retiro exitoso. Saldo restante: {usuarios[usuario]['saldo']}"

"""Deposita fondos en la cuenta de un usuario."""
def depositar_fondos(usuario, cantidad):
    usuarios[usuario]['saldo'] += cantidad
    return f"Depósito exitoso. Saldo actual: {usuarios[usuario]['saldo']}"

def cajero_automatico():
    '''Simulamos el cajero'''
    print('Bienvenido al cajero Automatico')
    usuario = input('Ingrese su usuario: ')
    contraseña = input('Ingrese su contraseña: ')
    
    if verificar_usuario(usuario, contraseña):
        print('Inicio de sesion exitoso')
        
        while True:
            print('\n OPCIONES:')
            print('1. Consultar saldo:')
            print('2. Retirar dinero:')
            print('3. Depositar fondos:')
            print('4. Salir:')    
            
            opcion = input('Seleccione una opcion: ')
        
            if opcion == '1':
                print(f'Saldo actual: {consultar_saldo(usuario)}')
            elif opcion == '2':
                cantidad = float(input('Ingrese la cantidad a retirar: '))
                print(retirar_dinero(usuario, cantidad))
            elif opcion == '3':
                cantidad = float(input('Ingrese la cantidad a depositar: '))
                print(depositar_fondos(usuario, cantidad))    
            elif opcion == '4':
                print('Gracias por usar nuestro cajero automatico. Hasta luego.')
                break
            else:
                print('OPCION NO VALIDA. POR FAVOR SELECCIONE UNA OPCION CORRECTA')
    else:
        print('Usuario o contraseña incorrectos')
        
cajero_automatico()
