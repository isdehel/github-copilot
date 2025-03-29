import random
import string

def generar_contraseña(longitud=12):
    """
    Genera una contraseña aleatoria de la longitud especificada.
    
    :param longitud: Longitud de la contraseña (por defecto es 12).
    :return: Contraseña generada.
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

# Ejemplo de uso
if __name__ == "__main__":
    print("Contraseña generada:", generar_contraseña())
