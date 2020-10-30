from cryptography.fernet import Fernet
#import IO
# key=Fernet.generate_key()
# print("Esta es mi Key: ",key)

import base64
import os
import pickle
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import inutil

def dame_salt():
    salt1 = os.urandom(16)# CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
    return salt1

def dame_key(salt1,password):
    salt =salt1
    contra=password
    #contra.encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(contra)) # Can only use kdf once
    return key

def encripto(mensage,key):
    #from cryptography.fernet import Fernet
    message = mensage
    key1=key
    #print(message)
    #print(key1)

    try:
        message=message.encode()
    except:
        pass

    try:
        key1.encode()
    except:
        pass

    #print(type(message))
    #print(type(key1))

    #Çif type(message) != bytes:
    #Ç    message.encode()
    #encriptamos el usuario
    #encriptamos
    f = Fernet(key1)
    msg_encrypted = f.encrypt(message)
    #print("se ha cifrado")
    return msg_encrypted

def decifro(msg,key1):
    """
    #   deciframos
    #   from cryptography.fernet import Fernet
    """
    key=key1
    f=Fernet(key)
    msg_decrypted = f.decrypt(msg)
    return msg_decrypted

#necesito una salt, una contra para encriptar el mensaje, un mensaje, y luego el mensaje encrytado 
def dame_cifrado(contra1,msg_a_cifrar):
    contra=contra1#la paswword o contraseña
    #contra.encode()
    salt1=dame_salt()
    key1=dame_key(salt1,contra)
    msg_encrypted=encripto(msg_a_cifrar,key1)
    msg_decrypted=decifro(msg_encrypted,key1)

    #print("Esta es la password: ",contra)
    #print("Esta es la salt: ",salt1)
    #print("Esta es la key:",key1)
    #print("Esto es el mensage encryptado: ",msg_encrypted)
    #print("Esto es lo decifrado: ",msg_decrypted)
    retorno=[key1,msg_encrypted,salt1]
    return retorno
    
    # #escribimos
    # escribimos_key(key1)
    # print("Se escribio la key: ")
    # escribimos_msg(msg_encrypted)
    # print("Se escribio el mensaje: ")
    # escribimos_salt(salt1)
    # print("Se escribio la salt: ")

def escribimos_todo(todo1,todo2,todo3,todo4,text,de_archivo):
    #salt_msg=dame_salt()#esta es la salt que se usara para encriptar y decriptar los datos
    key1=[todo1[0],todo2[0],todo3[0],todo4[0],de_archivo[0]]
    msg_cifrado=[todo1[1],todo2[1],todo3[1],todo4[1]]
    salt1=[todo1[2],todo2[2],todo3[2],todo4[2],de_archivo[2]]
    #escribimos la key
    escribimos_(key1,text[0])
    #escribimos el dato encriptado
    escribimos_(msg_cifrado,text[1])
    #escribimos la salt
    escribimos_(salt1,text[2])

    
def escribimos_(msg,n_archivo):
    #escribimos la key
    if inutil.existe(n_archivo):
        inutil.ab_archivo(n_archivo,msg)
        #print("Archivo abierto. ")
    else:#si no esta creado lo crea y escribe    
        inutil.wb_archivo(msg,n_archivo)
        #print("Archivo abierto. ")
   
#tomara un usuario y una contraseña y los cifrara y comprobara
def contra_anbn(user,contra):
    #primera letra de user
    c1=user[0]
    #ultima letra de user
    cn1=user[-1]
    #primera letra de contra 
    c2=contra[0]
    #ultima letra de contra
    cn2=contra[-1]
    r=c1+cn2+cn1+c2    
    return r

def dame_datos(user_provide,password_provide,text):
    #print("-----------------------")
    #user_provide=input("Introduce usuario: ")
    #password_provided = input("Escribe la contraseña: ")# This is input in the form of a string
    #print("-----------------------")
    #guardamos datos para no perderlos
    user= user_provide.encode()
    contra = password_provide.encode() # Convert to type bytes

    # #primero ciframos el usuario con la contra
    user1=dame_cifrado(contra,user)
        #print("-----------------------")
    # #luego la contra con el usuario
    contra1=dame_cifrado(user,contra)
    #print("-----------------------")

    #luego ciframos el usuario con la contra modificada usando lo siguiente
    #la primera letra de usuario +
    #la ultima letra de contra +
    #la ultima letra de usuario +
    #la primera letra de contra
    #manu
    #patas
    #msup
    #msup
    #manumsup
    #patasmsup

    ncontra=contra_anbn(user.decode(),contra.decode())
    #print(ncontra)
    ncontra=ncontra.encode()
    #print(user+ncontra)
    #print(contra+ncontra)
    user2=dame_cifrado(ncontra,(user+ncontra))    
    #print("-----------------------")
    #luego ciframos la contraseña con la ncontra modificada
    contra2=dame_cifrado(ncontra,contra+ncontra)
    #print("-----------------------")

    #necesito otra key mas
    de_archivo=dame_cifrado(user,user)

    #print(user1)
    #print("-----------------------")
    #print(contra1)
    #print("-----------------------")
    #print(user2)
    #print("-----------------------")
    #print(user2)
    #print("-----------------------")

    #text=["user.txt","user.txt","usalt.txt"]

    escribimos_todo(user1,contra1,user2,contra2,text,de_archivo)
        # #escribimos
        # escribimos_key(key1)
        # print("Se escribio la key: ")
        # escribimos_msg(msg_encrypted)
        # print("Se escribio el mensaje: ")
        # escribimos_salt(salt1)
        # print("Se escribio la salt: ")

#dame_datos()