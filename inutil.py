import os
import pickle
from datetime import datetime, date
from configparser import ConfigParser
import decifra

def m_idioma(archivo,idioma="Espain",lengua="1",items=[False],section="settings",opcion=["idioma","lengua"]):
    items=[idioma,lengua]

    config=ini_archivo(archivo)

    ini_set(config,section,opcion[0],idioma)
    ini_set(config,section,opcion[1],lengua)
    #config.set(section,opcion[0],idioma)
    #config.set(section,opcion[1],lengua)
    
    ini_write(config,archivo)

    #datos=open(archivo, "w")
    #config.write(datos)

def dame_idioma():
    archivo1="settings.ini"
    idioma="idiomas"

    lista=dame_items(archivo1,idioma)
    nun_idioma= lista[0]
    name_idioma= lista[1]

    return dame_idiomas(idioma,nun_idioma,name_idioma)

def dame_items(archivo1="settings.ini",archivo2="idiomas",section="settings",items=["idioma","lengua","troll","num_paleta"]):
    
    if existe(archivo2):
        #print("Archivo existe. ")
        config1=ini_archivo(archivo1)

    name=config1.get(section,items[0])
    nun=config1.getint(section,items[1])
    try:
        troll=config1.getboolean(section,items[2])
    except:
        troll=False
    try:
        paleta=config1.getint(section,items[3])
    except:
        paleta=0

    return [nun,name,troll,paleta]

def dame_idiomas(idioma,nun_idioma,name_idioma):
    listo=decifra.dame_listas(idioma)
    key=listo[0]
    lengua=decifra.dame_de_listas_la_key(listo,nun_idioma)
    retorno=[]
    for a in range(len(lengua)):
        b=decifra.dame_a_decifrar([key],a,lengua,name_idioma,0)
        retorno.append(b)
    return retorno

def rb_archivo(archivo):
    datos_archivo=open(archivo,"rb")
    #pickle.dump("esto es una prueba de archico existente",datos_archivo)
    datos = pickle.load(datos_archivo)
    #print(pickle.load(datos_archivo))
    datos_archivo.close()
    del(datos_archivo)

    return datos

def r_archivo(archivo):
    
    if existe(archivo):
        datos_archivo=open(archivo,"r")
        #pickle.dump("esto es una prueba de archico existente",datos_archivo)
        datos = datos_archivo.read()
        #print(pickle.load(datos_archivo))
        datos_archivo.close()
        del(datos_archivo)
    else:
        datos ="0"
    return datos

def a_archivo(msg,archivo = "msg.txt" ):#esto abre el archivo en append osea agregar mas
    datos_archivo=open(archivo,"a") 
    for a in msg:
        datos_archivo.write(str(a))
    #datos=pickle.load(datos_archivo)
    #return datos
    datos_archivo.close()
    del(datos_archivo)

def ab_archivo(archivo,msg):#esto abre el archivo en modo append y agrega mas
    datos_archivo=open(archivo,"ab")
    pickle.dump(msg,datos_archivo)
    #datos=pickle.load(datos_archivo)
    #return datos
    datos_archivo.close()
    del(datos_archivo)

def wb_archivo(msg,archivo="archivo"):#esto abre el archivo en modo escritura y borra todo
    datos_archivo=open(archivo,"wb")
    pickle.dump(msg,datos_archivo)
    datos_archivo.close()
    del(datos_archivo)

def w_archivo(msg="",archivo="msg.txt"):
    datos_archivo=open(archivo,"w")
    datos_archivo.write(str(msg))
    datos_archivo.close()
    del(datos_archivo)

def existe(archivo):
    if os.path.isfile(archivo):
        #print("archivo existe")    
        return True
    else:
        #print("no archivo")       
        return False 

def borar_archivo(archivo="msg.txt"):
    #if input("Quieres borra archivo: y/n: ")=="y":
    if(existe(archivo)):
            os.remove(archivo)#borrar este archivo no lo envia a la papelera de reciclaje

def borra_varios(archivo=["zkey","zsalt","zuser","archivo","msg.txt"]):
    for a in archivo:
        if(existe(a)):
                os.remove(a)#borrar este archivo no lo envia a la papelera de reciclaje

def dame_dia():
    #dia actual
    day=date.today()
    #print("- - - - - - - - - - ")
    now_dia=[day.day,day.month,day.year]
    return now_dia

def dame_fecha():
    #fecha
    fecha= datetime.now()
    now_fecha=["\n",fecha.day,"/",fecha.month,"/",fecha.year," ",fecha.hour,":",fecha.minute,":",fecha.second,"\n"]
    return now_fecha

def ini_cifra(archivo1="archivo.ini",archivo2="settings.ini"):#tenemos que cifrar
    #config1=ini_archivo(archivo1)#tenemos el config
    #config2=ini_archivo(archivo2)#tenemos el config
    pass

def ini_add_section(config,section):
    config.add_section(section)

def ini_set(config,section,item,valor):
    config.set(section,item,valor)

def ini_write(config,archivo):
    if existe(archivo):
        datos=open(archivo, "w")
        config.write(datos)

def ini_archivo(archivo="archivo.ini"):
    #esto debuelve una lista de los textos traducidos
    if existe(archivo):
        #lo abrimos
        config=ConfigParser()
        config.read(archivo)
    else:#lo creamos
        w_archivo("",archivo)        
        config=ConfigParser()
        config.read(archivo)

    return config
    
def ini_items(archivo="settings.ini",section="paleta_de_colores"):
    
    config=ini_archivo(archivo)

    tt=config.options(section)
    ta=[]
    for a in tt:
        ta.append(config.get(section,a))
    
    #print(ta)
    return ta

def ini_dame_items(section="paleta_de_colores",num="num_paleta",name="paleta"):
    con=ini_items(section=section)

    items=dame_items(items=[name,num])
    #print(items)

    pale=ini_items(section=con[items[0]])
    return pale

#archivo1="settings.ini"
#m_idioma(archivo1,"Espain","1")
#borra_varios()