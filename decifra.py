import pickle,os,inutil

#deciframos
from cryptography.fernet import Fernet

def dame_listas(n_archivo):#dato es el archivo "usalt.txt" "ukey.txt" "user.txt"
    if inutil.existe(n_archivo):#si el archivo existe lo abrimos como rb
        #print("Archivo existe. ")
        archivo=open(n_archivo,"rb")
        
        listas=[]
        while True:
            try:
                listas.append(pickle.load(archivo))
            except:
                #print("no hay mas listas") 
                #print("------------")
                break   

        archivo.close()
        del(archivo)
        #print(listas)
        
        # print("------------")
        return listas

    else:
        #print("Ha ocurrido un ERROR... ")
        #print("Archivo NO existe... ")
        pass

def dame_de_listas_la_key(listas,pos):
    lista=[]  
    for a in listas[pos]:    
        
        lista.append(a)
        #print(c)
    
    #print(lista)
    #print("------------")

    #print("Esto es la lista: ")
    #print(lista[0])
    return lista

    # for a in lista_key:
    #     print(a)

    #print("Esto es el user encryptado: ")
    #print("Esto es la salt")

def dame_a_decifrar(lista_key,pos,lista_user,msg,pos2=1):
    if pos2 == 1:
        pos2=pos
    key=lista_key[pos2]
    f = Fernet(key) 
    user_encrypted=lista_user[pos]
    user_decrypted = f.decrypt(user_encrypted)
    decifrado=user_decrypted.decode()
    #print("Esto es ",msg," decifrado: ",decifrado)

    return decifrado

#def dame_datos():
#    #despues de terner los primeros dos decriptados hay que comparar si son correptos
#    #user1=input("Introduce el usuario: ")
#    #contra1=input("Introduce la contraseña ")
#    datos_send=[user1,contra1]
#    return datos_send

def compara_datos(datos_send,datos_decryto,anbn):
    #Datos dados por el usuario
    user1=datos_send[0]
    contra1=datos_send[1]
    #Datos decifrados
    de_user1=datos_decryto[0]
    de_contra1=datos_decryto[1]
    #datos decifrados mas anbn 
    de_user2=datos_decryto[2]
    de_contra2=datos_decryto[3]
    #datos dados por usuario mas anbn
    an_user=anbn[0]
    an_contra=anbn[1]

    if(user1==de_user1 and contra1==de_contra1 and de_user2==an_user and de_contra2==an_contra):
        #print("Usuario y contraseña son correptos")
        return True
    else:
        #print("Usuario o contraseña son incorreptos, intentelo de nuevo")
        return False

def anbn(datos):
    user=datos[0]
    contra=datos[1]
    #primera letra de user
    c1=user[0]
    #ultima letra de user
    cn1=user[-1]
    #primera letra de contra 
    c2=contra[0]
    #ultima letra de contra
    cn2=contra[-1]
    r=c1+cn2+cn1+c2 

    user2=user+r
    contra2=contra+r
    r=[user2,contra2]   
    
    return r

def dame_key_pos4(pos,text):
    listas=dame_listas(text[0])
    lista=dame_de_listas_la_key(listas,pos)
    de_key=lista[4]
    return de_key

def decifra(pos,datos,text):
    listas_key=dame_listas(text[0])#estos son los archivos donde se guardan los datos
    listas_user=dame_listas(text[1])

    lista_key=dame_de_listas_la_key(listas_key,pos)
    lista_user=dame_de_listas_la_key(listas_user,pos)

    de_user=dame_a_decifrar(lista_key,0,lista_user,"el usuario")
    de_contra=dame_a_decifrar(lista_key,1,lista_user,"la contraseña")
    de_user2=dame_a_decifrar(lista_key,2,lista_user,"el usuario+anbn")
    de_contra2=dame_a_decifrar(lista_key,3,lista_user,"la contraseña+anbn")
    #de_salt_msg=lista_key[4]
    de_datos=[de_user,de_contra,de_user2,de_contra2]

    #datos=dame_datos()
    d_anbn=anbn(datos)

    return compara_datos(datos,de_datos,d_anbn)

def mientras_listas(datos,text):
    indice=0
    while True:
        try:#mientras la lista sea mas grande 
            #print("Todavia hay para revisar: ",indice)
            if decifra(indice,datos,text):
                return [True,indice]
                #el break y el return funcionan igual rompen en bucle y pornerlos juntos es 
                #break

            indice=indice+1
        except:#cuando la lista de un error
            #print("Ya no hay mas de donde revisar")
            indice=indice-1
            #depende de si estamos ingresando o registrandonos
            #si estamos registrandonos, nos interesa que no exista ninguna igual
            #si estamos ingresando si nos interesa que exista una igual
            #nos interesara uno de los dos resultados
            return [False,indice]
            #el break y el return funcionan igual rompen en bucle y pornerlos juntos es 
            #break
