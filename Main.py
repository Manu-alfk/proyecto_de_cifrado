
"""
#"Etapas del proyecto
# 1.crear interfas grafica --h
# 2.crear los asets para crear un usuario y contraseña --h
# 3.encriptar dichos datos, revisar que no haya ninguno igual --h
#   *guardar estos datos en archivo bit encriptado,-h 
# 4.crear los asets para introducir usuario y contraseña --h
# 5.crear las segundas gui para cuando tenemos al usuario ingresado --h
# 6.crear asets para abrir y crear archivo archivo,  --h
#   *crear los gif y demas para dar a entender al usuario que sucede -h
# 7.trabajar con archivo bit ya creado  -h
#   *buscar manualmente,
#   *seleccionar manualmente,
#   *encontrar automatico,
#   *arbrir automatico 
# 8.crear asets para leer archivo bit, cerrarlo, borrarlo, modificarlo  -h
# 9.crear asets para crear archivo .txt, abrirlo, modificarlo, borrarlo  -h
# 10.crear asets para leer de archivo bit y eso escribir en archivo.txt -h 
# 11.dar la señal de que archivo.txt abierto y rellenado correctamente  -h
#   *cuando es primera vez, como no hay nada no se lee,--h
#   * ni escribe nada mas que una prueba "Hola Mundo"
# 12.crear asets para escribir en archivo.txt desde programa 
# 13.crear boton de guardado automatico con combinacion de teclas
# 14.escribir en archivo.txt desde programa y fuera de el,
#   *experimentar
# 15.encriptar datos introducidos a archivo.txt y mostrar todo los procesos --h
# 16.escribir en archivo bit  -h
# 17.borrar todo de archivo.txt --h
# 18.borrar archivo.txt   -h
# 19.gurdar datos de archivo bit  -h
# 20.crear otras dos copias desde cero, especificar las rutas la primera vez
# 21.cerrar todo  -h
# 22.automatizar todo si es posible  "
# salto de linea \n
# para los ajustes
#   *contraseña troll
#   *idiomas
#   *colores de las ventanas o paletas de colores preestablecidas 
"""


"""
msg_borrar="Se ha borrado archivo txt"
msg_escrito="Se ha escrito archivo"
msg_no_existe_contenido="No existe contenido"
msg_existe_contenido="Existe contenido"
msg_abierto="Se ha abierto el archivo"
msg_texto_de="Textos de "
msg_archivo_borrados="Se han borrado los archivos"
msg_archivo_existe="archivo ya existe"
msg_archivo_no_existe="Archivo no existe"
msg_puedes_ingresar_datos="puedes ingresar datos"

msg_user_invalido="Usuario invalido"
msg_user_valido="Usuario valido"
msg_contra_invalida="Cotraseña invalida"
msg_contra_valida="Cotraseña valida"
msg_contra_mayor="Contraseña debe de ser mayor  "
msg_hay_error="Ha ocurrido un error, "

msg_no_user="No existe ese usuario" 
msg_has_iniciado="Has iniciado secion correctamente"
msg_puedes_entrar="Puedes entrar"

msg_user_existe ="Ya existe un usuario con esos datos"
msg_puedes_registrarte="Puedes registrarte"
msg_te_registraste="Te has registrado correctamente"

msg_entraste="entraste"
msg_registrate="registarte"

t_bu_register="REGISTRARSE"
t_bu_ingresar="ENTRAR"
t_bu_ajustes="AJUSTES"

t_la_contra_troll="Contraseña"
t_msg_troll="patatas1patatas2patatas3patatas4patatas5patatas6"
t_troll_chkbu="Contraseña Troll"

t_la_idioma="Idioma"

t_v_user="SIN_ESPACIOS"
t_la_usuario="USUARIO"
t_la_contraseña="CONTRASEÑA"

t_bu_aceptar="ACEPTAR"
t_la_avisos="Avisos"

t_bu_crear_bin= " Cerar archivo "
t_bu_abrir_bin= " Abrir archivo "
t_bu_borrar_bin="Borrar archivo "

t_bu_cerrar="Cerrar cesión"
t_bu_abrir="Escribir archivo"
t_bu_borrar="Borrar archivo"
"""
from tkinter import *
import inutil, cifrado, decifra, sys
from threading import Timer

#capturar datos de textblock con boton
#state="disable" "active" para desavilitar 
#este es enrealidad la accion del boton pero necesita un mode,
#que se lo da uno de los botones fisico
#osea hay dos botones fisicos y estos llaman a esta misma funcion con un mode diferente
#boton registrar

def boton_register():
    #escribimos
    #print(msg_registrate)
    #llamamps a los botones de entrar 
    #true es register
    ingresar_ocultar()
    b_ingresar_mostrar(True)
    reescribir()
    #ocultar_into_register()

def boton_entrar():#boton entrar
    #escribimos
    #print(msg_entraste)
    #llamamos a los botones de entrar 
    #False es entrar
    ingresar_ocultar()
    b_ingresar_mostrar(False)   
    reescribir()
    #ocultar_into_register()

def ocultar_into_register():
    bu_ingresar.place_forget()
    bu_register.place_forget()
    bu_ajustes.place_forget()

def mostrar_buttons():
    bu_register.place(x="50",y="50")
    bu_ingresar.place(x="190",y="50")
    bu_ajustes.place(x="400",y="50")

def dame_datos_de_usuario():
    user=ent_usuario.get()
    contra=ent_contraseña.get()
    datos=[user,contra]
    #print("-_-_-_-_-_-_-_- - - - - - - ")
    #print(datos)
    return datos

def b_mode_aceptar(mode):
    #print("aceptar") #imprimir datos de prueba
    #user=ent_usuario.get()
    #contra=ent_contraseña.get()
    #datos=[user,contra]
    datos=dame_datos_de_usuario()
    #print("- - - - - - - - - - - - - - ")
    #print(datos) 
    user =datos[0]
    contra=datos[1]
    
    #si esta borrar todoy pedir los tados otra ves    
    #las variables de inicio
    user_1=t_v_user
    contra_1="123456"
    max_contra=6
    
    text=["zkey","zuser","zsalt"]
    #verificar que no sean datos iguales
    if user!=user_1:
                #print(msg_user_valido)
            if len(contra)>max_contra:
                if contra!=contra_1 :#and len(contra)>6
                    #print(msg_contra_valida)  
                    #cuando hemos cambiado los datos de inicio
                    #print("Es > a max_contra=6")

                    if mode:#true es register y no tiene que existir el archivo
                            #se puede crear
                            if inutil.existe(text[0]):
                                usuario=decifra.mientras_listas(datos,text)
                                if usuario[0]:
                                    #nos interesa que no exista ninguno
                                    #osea que si da True, no podemos registrarnos 
                                    #print(msg_user_existe)  
                                    la_avisos.config(text=msg_user_existe)                                  
                                    reescribir()
                                else:
                                    #osea si da false, es que no hay uno igual
                                    #y nos podemos registrar
                                    #print(msg_puedes_registrarte)
                                    #la_avisos.config(text="Te has registrado correctamente")                                               
                                    avisos2(msg_te_registraste)
                                    #reescribir()
                                    ingresar_ocultar()                                    
                                    m_opci_morado()
                                    ocultar_into_register()
                                    cifrado.dame_datos(user,contra,text)
                                    aviso_espera(5,avisos2_f)
                            else:
                                #si no existe lo creamos de una ves
                                #print(msg_puedes_registrarte)
                                #reescribir()
                                #la_avisos.config(text="Te has registrado correctamente")
                                avisos2(msg_te_registraste)
                                ingresar_ocultar()
                                ocultar_into_register()
                                m_opci_morado()
                                cifrado.dame_datos(user,contra,text)
                                aviso_espera(5,avisos2_f)

                    else:#False es entrar y tiene que existir el archivo
                        if inutil.existe(text[0]):
                            usuario=decifra.mientras_listas(datos,text)
                            if usuario[0]:
                                #nos interesa que exista uno
                                #osea que si da True si podemos entrar
                                #print(msg_puedes_entrar)
                                #la_avisos.config(text="Has entrado")
                                avisos2(msg_has_iniciado)
                                ingresar_ocultar()
                                m_opci_morado()
                                ocultar_into_register()
                                #reescribir()                               
                                aviso_espera(5,avisos2_f)
                            else:
                                #osea si da False no existe
                                #print(msg_no_user)
                                la_avisos.config(text=msg_no_user)
                                reescribir()
                        else:
                            #print(msg_hay_error+msg_archivo_no_existe)
                            la_avisos.config(text=msg_hay_error+msg_archivo_no_existe)
                            reescribir()

                        # if inutil.existe("ukey.txt"):#si existe leemos,
                        #     # esto nos dara True si existe o False si no existe
                        #     #decifra.mientras_listas([user,contra])
                        # else:#si no existe lo creamos, ok
                        #     #inutil.wb_archivo()
                        #     text=["zkey.txt","zuser.txt","zsalt.txt"]
                        #     cifrado.dame_datos(user,contra,text)
                        
                    user=""
                    contra=""

                else:
                    #print(msg_contra_invalida)
                    la_avisos.config(text=msg_contra_invalida)
                    reescribir()
            else:
                #print(msg_contra_mayor,max_contra)
                la_avisos.config(text=msg_contra_mayor+str(max_contra))
                reescribir()
                    
    else:
        #print(msg_user_invalido)
        la_avisos.config(text=msg_user_valido)
        reescribir()

def aviso_espera(point,funcion):#avisos2_f
    t=Timer(point,funcion,args=None, kwargs=None)  
    #print("")
    t.start()   

def avisos2_f():
    try:
        la_avisos2.place_forget()
    except:
        pass

def avisos2(textos=""):

    la_avisos2.place(x="300",y="75",anchor="center")
    la_avisos2.config(text=textos)

def b_ingresar_mostrar(mode):
    #escribimos 
    #print(msg_puedes_ingresar_datos)
    #mostramos datos y entramos a bucle
    global mostrar
    mostrar=True
    #posicionar para opciones
    la_usuario.place(anchor="center",x="100",y="75")
    ent_usuario.place(anchor="center",x="100",y="100")

    la_contraseña.place(anchor="center",x="100",y="135")
    ent_contraseña.place(anchor="center",x="100",y="160")
    
    if mode:#true es para registrar
        bu_aceptar1.place(anchor="center",x="100",y="215")
    else:
        bu_aceptar2.place(anchor="center",x="100",y="215")

    la_avisos.config(text="")
    la_avisos.place(x=("300"),y="175",anchor="center") 
    
    #escribe el mensaje de inicio
    reescribir()
    
    #m_abierto()
    m_cerrado()

def b_aceptar_register():
    b_mode_aceptar(True)

def b_aceptar_entrar():
    b_mode_aceptar(False)

def m_contra():
    #print("mostrar")
    pass

def o_contra():
    #print("ocultar")
    pass

def reescribir():
    
    ent_usuario.delete(0,100)       
    ent_usuario.insert(0,v_user)

    ent_contraseña.delete(0,100)
    ent_contraseña.insert(0,v_register) 
    #print("v_register",v_register)
    ent_contraseña_ns.delete(0,100)
    ent_contraseña_ns.insert(0,v_register2) 
    #print("v_register",v_register) 
    #print("contrases",ent_contraseña.get())
    #print("contrases_ns",ent_contraseña_ns.get())

def ingresar_ocultar():       
    #ocultar witgets
    la_usuario.place_forget()
    #ent_usuario.place_forget()
    la_contraseña.place_forget()
    #ent_contraseña.place_forget()
    bu_aceptar1.place_forget()
    bu_aceptar2.place_forget()

    la_avisos.place_forget()
    global mostrar
    mostrar = True 

def m_opci_morado():
    #posicionar para opciones
    la_fondo_morado1.place(x="130",y="50")
    la_fondo_morado1.config(width="20",height="20")
    la_fondo_morado2.place(x="330",y="50")
    la_fondo_morado2.config(width="20",height="20")
    bu_crear_bin.place(x="150",y="75")
    bu_abrir_bin.place(x="150",y="130")
    bu_borrar_bin.place(x="150",y="185")
    bu_cerrar.place(x="150",y="230")
    bu_abrir_txt.place(x="350",y="75")
    bu_borrar_txt.place(x="350",y="130")

def ocultar_opci_morado():
    la_fondo_morado1.place_forget()
    la_fondo_morado2.place_forget()
    bu_crear_bin.place_forget()
    bu_abrir_bin.place_forget()
    bu_borrar_bin.place_forget()
    bu_cerrar.place_forget()
    bu_borrar_txt.place_forget()
    bu_abrir_txt.place_forget()

def m_abierto():#pongo el abierto a cerrado 
    bu_cerrado.place(x=195,y=149)
    bu_abierto.place_forget()

    ent_contraseña_ns.place_forget()
    ent_contraseña.place(anchor="center",x="100",y="160")
    
    ent_contraseña_ns.delete(0,100)

def m_cerrado():#pongo  el cerrado a abierto y ell * a normal  
    bu_cerrado.place_forget() 
    bu_abierto.place(x=195,y=149)

    ent_contraseña_ns.place(anchor="center",x="100",y="160")
    ent_contraseña.place_forget()
    
    msg=ent_contraseña.get()
    ent_contraseña_ns.delete(0,100)
    ent_contraseña_ns.insert(0,msg)

    if no_troll==False:
        aviso_espera(5,m_abierto)
    else:
        troll_mostrar()

def troll_mostrar():#esto hara que se este reescribiendo en el entry
    #tenemos que obtener la variable y guardarla en otro entri

    global no_troll
    #print("esto es troll")
    global vs_troll
    try:    
        if no_troll:
            
            msg_normal=ent_contraseña_ns.get()
            nmsg_normal=msg_normal

            if len(msg_normal)==0:
                ent_contraseña.delete(0,100)
                    
            if vs_troll > 0 :# pylint: disable=E0601
                #cuando es 1 o mas entramos 
                if vs_troll < len(msg_normal):#entonces se ha agregado texto y 

                    ent_contraseña_ns.delete(0,(vs_troll))#borramos lo enterior y nos quedamos con lo nuevo
                    #n_msg=ent_contraseña_ns.get()
                    ent_contraseña.insert(vs_troll,ent_contraseña_ns.get())#insertamos lo nuevo
                    #ne_msg=ent_contraseña.get()
                    vs_troll=len(msg_normal)                             

                    #v_troll=len(msg_normal)
                else:#hemosquitado
                        vs_troll=len(msg_normal)
                        ent_contraseña.delete(vs_troll,100)
            else:#la primera vez escribimos tal cual
                #cuando es 1 escribimos tal cual
                vs_troll=len(msg_normal)
                ent_contraseña.delete(0,100)
                ent_contraseña.insert(0,msg_normal) 
            
            n_msg=ent_contraseña.get()
            ent_contraseña_ns.delete(0,100)
            ent_contraseña_ns.insert(0,nmsg_normal)

            try:
                #print("contraseñato",ent_contraseña.get())        
                if len(msg_normal)<=40:
                    if len(msg_normal)>0:
                        #ent_contraseña.delete(0,100)
                        #se tiene que escribir en contraseña la verdadera contraseña

                        msg_null=""
                        for a in range(len(msg_normal)):
                            msg_null=msg_null+str(msg_troll[a])

                        ent_contraseña_ns.delete(0,100)
                        ent_contraseña_ns.insert(0,msg_null)
                        ent_contraseña.delete(0,100)
                        ent_contraseña.insert(0,n_msg)                
                else:
                    ent_contraseña_ns.delete(40,100)
                    ent_contraseña.delete(40,100)
            except:            
                ent_contraseña_ns.delete(0,100)
                ent_contraseña.delete(0,100)
                #pass

            aviso_espera(0.3,troll_mostrar)
            #print("1")
    except:       
        r.quit()
        sys.exit()

        #r.destroy()

def troll_ocultar():
    re=ra.get()     
    global no_troll
    if re==0:
        no_troll = False
        # print(entra_troll)
        reescribir()
        
        config=inutil.ini_archivo("settings.ini")
        inutil.ini_set(config,"settings","troll","False")        
        inutil.ini_write(config,"settings.ini")
        # entra_normal.place(x=200,y=100,anchor="center")
        # entra_troll.place_forget()
        if mostrar:
            m_cerrado()   
    elif re==1:
        no_troll = True
        reescribir()     
        config=inutil.ini_archivo("settings.ini")   
        inutil.ini_set(config,"settings","troll","True")
        inutil.ini_write(config,"settings.ini")
        if mostrar:
            m_cerrado()    

def troll_invoke():
    config=inutil.ini_archivo("settings.ini")
    item=inutil.dame_items()
    return item[2]

def crear_new_archivo_bin(msg="",archivo="archivo"):
    #nos tiene que dar un nombre que por defecto sera archivo
    if inutil.existe(archivo) == False:
        #print(msg_archivo_existe)
        inutil.wb_archivo("",archivo) 
    
def borrar_archivo_bin(archivo1="archivo",archivo2="msg.txt",archivo3="num.txt"):
    #no tiene que dar el arcivo que por defecto sera archivo
    inutil.borra_varios([archivo1,archivo2,archivo3])
    #print(msg_archivo_borrados)   

def leer_archivo_bin(archivo="archivo"):
    #nos tiene que dar el nombre del archivo que por defecto sera archivo
    #leeremos el archivo y escribiremos todo lo que este en el en un archivo de txt plano
    if inutil.existe(archivo):       
        textos=inutil.rb_archivo(archivo)
        #debemos cerrar la ventana de pregunta
        #print(textos)
        if len(textos)>0:
                #print(msg_existe_contenido)
            #debemos consegir la posicion
            datos=dame_datos_de_usuario()
            #print(datos)
            
            text=["zkey","zuser","zsalt"]
            usuario=decifra.mientras_listas(datos,text)
            #print(usuario[1])#esta es la posicion

            #debemos consegir la salt
            key=decifra.dame_key_pos4(usuario[1],text)
            #print(key)
            #al tener la key podemos decifrar o cifrar
            texto=decifra.dame_a_decifrar([key],0,[textos],msg_texto_de+"--archivo.txt--")
            #al tener el texto decifrado tenemos que escribirlo en el msg.txt            
            inutil.w_archivo(texto,"msg.txt")
            #despues hay que escribir un numero que indique la cantidad de texto que hay en el
            textlen=len(texto)
            inutil.w_archivo(textlen,"num.txt")
            #print(msg_abierto)

        else:
            #print(msg_no_existe_contenido)
            #no exixte nada entonces solo creamos el msg
            inutil.w_archivo()
            numlen=inutil.r_archivo("msg.txt") 
            textlen=len(numlen)
            inutil.w_archivo(textlen,"num.txt")

def escribir_archivo_bin(archivo1="msg.txt",archivo2="archivo"):
    #nos tiene que dar el nombre que por defecto sera archivo
    #leeremos lo que este en  msg lo encrictaremos, y lo cambiaremos a archivo 

    if inutil.existe(archivo1):
        #tenemos que averiguar si hemos modificado el archivo
        numlen=inutil.r_archivo("msg.txt") 
        textlen=len(numlen)
        inutil.w_archivo(textlen,"num.txt")
        numlen=inutil.r_archivo("num.txt")  
        if int(numlen) > 0:
            #aqui pedimos la fecha y la escribimos
            fecha=inutil.dame_fecha()
            inutil.a_archivo(fecha,"msg.txt")
            
            textos=inutil.r_archivo(archivo1)
            #print(textos)
            #hay que encriptar
            datos=dame_datos_de_usuario()
            #print(datos)
            
            text=["zkey","zuser","zsalt"]
            usuario=decifra.mientras_listas(datos,text)
            #print(usuario[1])#esta es la posicion

            key=decifra.dame_key_pos4(usuario[1],text)
            #print(key)
            
            texto=cifrado.encripto(textos,key)

            inutil.wb_archivo(texto,archivo2)
            
            numlen=inutil.r_archivo("msg.txt") 
            textlen=len(numlen)
            inutil.w_archivo(textlen,"num.txt")
            #print(msg_escrito)

def borrar_archivo_txt(archivo="msg.txt"):
    #con eto borramos el archivo txt
    if inutil.existe(archivo):
        inutil.borar_archivo(archivo)  
    #print(msg_borrar)
    
def idiomas():
    archivo1="settings.ini"
    idioma="idiomas"
    ra=re.get()
    lista=inutil.dame_items (archivo1,idioma)
    num_i=lista[0]-1
    if ra==0 and ra !=num_i :#modificaremos a español
        #print("Español")
        inutil.m_idioma(archivo1,"Espain","1")
        #despues tengo que llamara al idioma
        dame_idiomas()
        #despues tengo que actualizar todas las variables al nuevo lenguaje
        actualiza()

    elif ra==1 and ra != num_i:#modificaresmos a español
        #print("English")
        inutil.m_idioma(archivo1,"English","2")
        #despues tengo que llamara al idioma
        dame_idiomas()
        #despues tengo que actualizar todas las variables al nuevo lenguaje
        actualiza()

    elif ra==2 and ra != num_i:
        #print("Italiano")
        inutil.m_idioma(archivo1,"Italiano","3")
        #despues tengo que llamara al idioma
        dame_idiomas()
        #despues tengo que actualizar todas las variables al nuevo lenguaje
        actualiza()

    elif ra==3 and ra != num_i:
        #print("Portuges")
        inutil.m_idioma(archivo1,"Portuges","4")
        #despues tengo que llamara al idioma
        dame_idiomas()
        #despues tengo que actualizar todas las variables al nuevo lenguaje
        actualiza()
    
def acerca_de():
    pass

def cerrar():
    #debemos de salir y dejar todo como al principio
    #if inutil.existe("msg.txt"):
    #inutil.borar_archivo("msg.txt")
    ocultar_opci_morado()
    mostrar_buttons()
    reescribir()

def ajustes():
    fr_ajustes.grid(row=0,column=9,rowspan=8,columnspan=4)
    bu_ajustes_ocultar.place(x=100,y=470,anchor="center")
    la_troll.place(x=5,y=5)
    la_contra_troll.place(x=100,y=20,anchor="center")
    #m_rb.place(x=10,y=35)
    #q_rb.place(x=10,y=55)
    troll_chkbu.place(x=10,y=35)
    #fr_ajustes.grid_forget()
    la_idioma.place(x=100,y=85,anchor="center")
    #chk_espain.place(x=10,y=90)
    #chk_english.place(x=10,y=120)
    #chk_italiano.place(x=10,y=150)
    #chk_portuges.place(x=10,y=180)
    rb_espain.place(x=10,y=100)
    rb_english.place(x=10,y=130)
    rb_italiano.place(x=10,y=160)
    rb_portuges.place(x=10,y=190)
    
    la_color.place(x=100,y=250,anchor="center")
    rb_oscuro.place(x=10,y=270)
    rb_fuego.place(x=10,y=300)
    rb_nieve.place(x=10,y=330)

def ocultar_ajustes():
    fr_ajustes.grid_forget()

def ver_select():
    item=inutil.dame_items()
    
    if item[0]==1:
        rb_espain.select()
    elif item[0]==2: 
        rb_english.select()
    elif item[0]==3:
        rb_italiano.select() 
    elif item[0]==4:
        rb_portuges.select() 
    global no_troll
    if item[2]:
        troll_chkbu.select()
        no_troll=True
    else:
        troll_chkbu.deselect()
        no_troll=False

    if item[3]==0:
        rb_oscuro.select()
    elif item[3]==1:
        rb_fuego.select() 
    elif item[3]==2:
        rb_nieve.select() 

def ac_colores():
    archivo1="settings.ini"

    ra=ro.get()
    listas=inutil.dame_items (archivo1,items=["paleta","num_paleta"])
    num_i=listas[0]
    if ra==0 and ra !=num_i :
        #print("Oscuro")
        inutil.m_idioma(archivo1,"paleta_oscuro","0",opcion=["paleta","num_paleta"])
        colorea()
    if ra==1 and ra !=num_i :
        #print("Fuego")
        inutil.m_idioma(archivo1,"paleta_fuego","1",opcion=["paleta","num_paleta"])
        colorea()
    if ra==2 and ra !=num_i :
        #print("Nieve")
        inutil.m_idioma(archivo1,"paleta_nieve","2",opcion=["paleta","num_paleta"])
        colorea()

def colorea():
    lista=inutil.ini_dame_items()
    #print(lista)
    colores()
    wid=dame_wid_color()
    actuliza_colores(wid,lista)

def actualiza():
    #tengo que ingresar a los config de cada uno de los widgets
    lengua =inutil.dame_idioma()
    lista=dame_wid()
    for a in range(24,42):#esto contiene todo el idioma
        #tengo que tener en algun lado una lista con todos los widgets
        try:
            lista[a-24].config(text=lengua[a])
        except:
            #print("no se pudo actualizar")
            pass
        #tengo que escribir en bu aceptar2
        bu_aceptar2.config(text=lengua[34])

def dame_wid():
    #aqui pondre todos los widgets
    lista=[]
    lista.append(bu_register )
    lista.append(bu_ingresar )
    lista.append(bu_ajustes )

    lista.append(la_contra_troll )
    lista.append(msg_troll )
    lista.append(troll_chkbu )

    lista.append(la_idioma )

    lista.append(v_user )

    lista.append(la_usuario )
    lista.append(la_contraseña )

    lista.append(bu_aceptar1 )
    lista.append(la_avisos )
    
    lista.append(bu_crear_bin )
    lista.append(bu_abrir_bin )
    lista.append(bu_borrar_bin )

    lista.append(bu_cerrar )
    lista.append(bu_abrir_txt )
    lista.append(bu_borrar_txt )

    return lista

#aqui recibiremos todos los datos del lenguaje
def dame_idiomas():
    global msg_borrar 
    global msg_escrito 
    global msg_no_existe_contenido 
    global msg_existe_contenido 
    global msg_abierto 
    global msg_texto_de 
    global msg_archivo_borrados 
    global msg_archivo_existe 
    global msg_archivo_no_existe 
    global msg_puedes_ingresar_datos 

    global msg_user_invalido 
    global msg_user_valido 
    global msg_contra_invalida 
    global msg_contra_valida 
    global msg_contra_mayor 
    global msg_hay_error 

    global msg_no_user 
    global msg_has_iniciado 
    global msg_puedes_entrar 

    global msg_user_existe  
    global msg_puedes_registrarte 
    global msg_te_registraste 

    global msg_entraste 
    global msg_registrate 

    global t_bu_register 
    global t_bu_ingresar 
    global t_bu_ajustes 

    global t_la_contra_troll 
    global t_msg_troll 
    global t_troll_chkbu 

    global t_la_idioma 

    global t_v_user 
    global t_la_usuario 
    global t_la_contraseña 

    global t_bu_aceptar 
    global t_la_avisos 

    global t_bu_crear_bin 
    global t_bu_abrir_bin 
    global t_bu_borrar_bin 

    global t_bu_cerrar 
    global t_bu_abrir 
    global t_bu_borrar 
    
    lengua=inutil.dame_idioma()

    msg_borrar=lengua[0]
    msg_escrito=lengua[1]
    msg_no_existe_contenido=lengua[2]
    msg_existe_contenido=lengua[3]
    msg_abierto=lengua[4]
    msg_texto_de=lengua[5]
    msg_archivo_borrados=lengua[6]
    msg_archivo_existe=lengua[7]
    msg_archivo_no_existe=lengua[8]
    msg_puedes_ingresar_datos=lengua[9]

    msg_user_invalido=lengua[10]
    msg_user_valido=lengua[11]
    msg_contra_invalida=lengua[12]
    msg_contra_valida=lengua[13]
    msg_contra_mayor=lengua[14]
    msg_hay_error=lengua[15]

    msg_no_user=lengua[16]
    msg_has_iniciado=lengua[17]
    msg_puedes_entrar=lengua[18]

    msg_user_existe =lengua[19]
    msg_puedes_registrarte=lengua[20]
    msg_te_registraste=lengua[21]

    msg_entraste=lengua[22]
    msg_registrate=lengua[23]

    t_bu_register=lengua[24]
    t_bu_ingresar=lengua[25]
    t_bu_ajustes=lengua[26]

    t_la_contra_troll=lengua[27]
    t_msg_troll=lengua[28]
    t_troll_chkbu=lengua[29]

    t_la_idioma=lengua[30]

    t_v_user=lengua[31]
    t_la_usuario=lengua[32]
    t_la_contraseña=lengua[33]

    t_bu_aceptar=lengua[34]
    t_la_avisos=lengua[35]

    t_bu_crear_bin=lengua[36]
    t_bu_abrir_bin=lengua[37]
    t_bu_borrar_bin=lengua[38]

    t_bu_cerrar=lengua[39]
    t_bu_abrir=lengua[40]
    t_bu_borrar=lengua[41]

def dame_wid_color():
    lista=[]
    relista=[]
    rerelista=[]

    lista.append(fr_datos )
    lista.append(fr_usuario )
    lista.append(fr_register )
    lista.append(la_troll )

    relista.append(fr_ajustes )
    relista.append(bu_ajustes_ocultar )
    relista.append(la_contra_troll )
    relista.append(troll_chkbu )
    relista.append(la_idioma )
    relista.append(rb_espain )
    relista.append(rb_english )
    relista.append(rb_italiano )
    relista.append(rb_portuges )
    relista.append(la_color )
    lista.append(relista)    
    relista=[]

    relista.append(la_fondo_morado1 )
    relista.append(la_fondo_morado2 )
    lista.append(relista)
    relista=[]
    
    relista.append(bu_register )
    relista.append(bu_ingresar )
    relista.append(bu_ajustes )
    relista.append(bu_crear_bin )
    relista.append(bu_abrir_bin )
    relista.append(bu_borrar_bin )
    relista.append(bu_cerrar )
    relista.append(bu_abrir_txt )
    relista.append(bu_borrar_txt )
    lista.append(relista)
    relista=[]

    relista.append(la_usuario )
    relista.append(la_contraseña )
    relista.append(bu_aceptar1 )
    relista.append(bu_aceptar2 )
    lista.append(relista)
    relista=[]

    relista.append(ent_usuario )
    relista.append(ent_contraseña )
    relista.append(ent_contraseña_ns )
    lista.append(relista)
    relista=[]

    rerelista.append(la_usuario )
    rerelista.append(la_contraseña )
    rerelista.append(bu_aceptar1 )
    rerelista.append(bu_aceptar2 )
    relista.append(rerelista)
    lista.append(relista)
    relista=[]    
    rerelista=[]

    rerelista.append(ent_usuario )
    rerelista.append(ent_contraseña )
    rerelista.append(ent_contraseña_ns )
    relista.append(rerelista)
    lista.append(relista)
    relista=[]    
    rerelista=[]

    return lista

def actuliza_colores(lista_w,lista_c):
    for x in range(len(lista_c)):
        b=lista_w[x]
        i=lista_c[x]
        if type(b)==list:
            for c in b:
                if type(c)==list:
                    for d in c:
                        #print("*        ",d," : ",i)
                        d.config(fg=i)
                else:
                    #print("#    ",c," : ",i) 
                    c.config(bg=i)
        else:
            #print("! ",b," : ",i)
            b.config(bg=i)
        #print("")   

def colores():
    #pañeta de colores
    global color_fr_datos 
    global color_fr_usuario 
    global color_fr_register 

    global color_fr_ajustes 

    global color_la_troll 
    global color_la_fondo_m1 

    global color_green 
    global color_black 
    global color_white 
    
    global color_gray
    global color_purple 
    
    p=inutil.ini_dame_items()

    color_fr_datos=p[0]
    color_fr_usuario=p[1]
    color_fr_register=p[2]

    color_la_troll=p[3]
    color_fr_ajustes= p[4]
    color_la_fondo_m1=p[5]
    
    color_green=p[6]
    color_black=p[7]
    color_white=p[8]

    color_gray=p[9]
    color_purple=p[10]

def cerrando():
    #r.wait_window()
    try:
        global no_troll
        no_troll=False
        sys.exit()
        r.quit()
        
    except:
        sys.exit()
        pass

dame_idiomas()
colores()
#colorea()

r = Tk()
r.protocol("WM_DELETE_WINDOW",cerrando)
usuario=""
#gris para ingresar datos de usuario nuevo o existente
fr_datos=Frame(r)
fr_datos.config(width="225", height="500",bg=color_fr_datos)#gris
fr_datos.grid(row=0,column=0,rowspan=8,columnspan=4)
fr_datos.grid_propagate(False) #para que el frame quede con el tamaño que yo quiero

#morado para opciones de usuario unico
fr_usuario=Frame(r)
fr_usuario.grid(row=0,column=4,rowspan=4,columnspan=4)
fr_usuario.config(width="600", height="350",bg=color_fr_usuario)  #morado
fr_usuario.grid_propagate(False)

#negro para opciones de entrar/registar /ajustes
fr_register=Frame(r) 
fr_register.grid(row=4,column=4,rowspan=4,columnspan=4)
fr_register.config(width="600", height="150",bg=color_fr_register) #negro
fr_register.grid_propagate(False)

#labels para opciones
bu_register=Button(fr_register,command=boton_register,text=t_bu_register,bg=color_green,font="20")
bu_ingresar=Button(fr_register,command=boton_entrar,text=t_bu_ingresar,bg=color_green,font="20")
bu_ajustes=Button (fr_register,command=ajustes,text=t_bu_ajustes,bg=color_green,font="20")
#posicionar buttons
mostrar_buttons()
#para ajustes
fr_ajustes=Frame(r)
fr_ajustes.config(width=200,height=500,bg=color_fr_ajustes)#celeste
fr_ajustes.grid(row=0,column=9,rowspan=8,columnspan=4)
fr_ajustes.grid_propagate(False)
fr_ajustes.grid_forget()
#para ocultar ajustes t_la_contra_troll="Contraseña"
la_troll=Label(fr_ajustes,bg=color_la_troll,width=25,height=32)
bu_ajustes_ocultar=Button(fr_ajustes,command=ocultar_ajustes,text=" X ",bg=color_fr_ajustes,font="40")

la_contra_troll=Label(fr_ajustes,bg=color_fr_ajustes,text=t_la_contra_troll)
#para ocutar lo de mensaje troll
ra=IntVar()
msg_troll=t_msg_troll#"patataspatataspatataspatataspatataspatatas" 
troll_chkbu=Checkbutton(fr_ajustes,text=t_troll_chkbu,bg=color_fr_ajustes,variable=ra,onvalue=1,offvalue=0,command=troll_ocultar)
#troll_chkbu.invoke()
#troll_chkbu.select()
#no_troll=troll_invoke()
vs_troll=IntVar()
vs_troll=0
mostrar=False
#para idiomas
la_idioma=Label(fr_ajustes,bg=color_fr_ajustes,text=t_la_idioma)
re=IntVar()
rb_espain=Radiobutton(fr_ajustes,text="Español",bg=color_fr_ajustes,variable=re,value=0,command=idiomas)
rb_english=Radiobutton(fr_ajustes,text="English",bg=color_fr_ajustes,variable=re,value=1,command=idiomas)
rb_italiano=Radiobutton(fr_ajustes,text="Italiano",bg=color_fr_ajustes,variable=re,value=2,command=idiomas)
rb_portuges=Radiobutton(fr_ajustes,text="Portuges",bg=color_fr_ajustes,variable=re,value=3,command=idiomas)

ro=IntVar()
rb_oscuro=Radiobutton(fr_ajustes,text="Oscuro",bg="#1A237E",variable=ro,value=0,command=ac_colores,fg="gray")
rb_fuego=Radiobutton(fr_ajustes,text="Fuego",bg="#E67E22",variable=ro,value=1,command=ac_colores)
rb_nieve=Radiobutton(fr_ajustes,text="Nieve",bg="#BBDEFB",variable=ro,value=2,command=ac_colores)
#rb_oscuro.select()
la_color=Label(fr_ajustes,text="Colors",bg=color_fr_ajustes)
 
#chk_espain=Checkbutton(fr_ajustes,text="Español",bg=color_fr_ajustes,variable=re,onvalue=1,offvalue=0,command=idiomas)
#chk_english=Checkbutton(fr_ajustes,text="English",bg=color_fr_ajustes,variable=re,onvalue=2,offvalue=0,command=idiomas)
#chk_italiano=Checkbutton(fr_ajustes,text="Italiano",bg=color_fr_ajustes,variable=re,onvalue=3,offvalue=0,command=idiomas) 
#chk_portuges=Checkbutton(fr_ajustes,text="Portuges",bg=color_fr_ajustes,variable=re,onvalue=4,offvalue=0,command=idiomas)
#chk_espain.select()
#rb_espain.select()
#varibles para opciones
v_user=StringVar()
v_register=StringVar()
v_register2=StringVar()

v_user=t_v_user #"SIN_ESPACIOS"
v_register ="123456"
v_register2="123456"
#labels para opciones
la_usuario=Label(fr_datos,text=t_la_usuario,bg=color_black,fg=color_gray,font="20")
la_contraseña=Label(fr_datos,text=t_la_contraseña,bg=color_black,fg=color_gray,font="20")
#ENTRY para opciones 2
ent_usuario=Entry(fr_datos,textvariable=v_user,bg=color_white,fg=color_purple,font="15",width="20")
ent_contraseña=Entry(fr_datos,textvariable=v_register,bg=color_white,fg=color_purple,show="F",font="20")
ent_contraseña_ns=Entry(fr_datos,textvariable=v_register2,bg=color_white,fg=color_purple,font="20")
#imagenes para otones
ima_cerrado=PhotoImage(file="ojo_cerrado.png")
ima_abierto=PhotoImage(file="ojo_abierto.png")
#botones de ver contraseña
bu_abierto=Button(fr_datos,image=ima_abierto,command=m_abierto)
bu_cerrado=Button(fr_datos,image=ima_cerrado,command=m_cerrado)
#boton para opciones 
bu_aceptar1=Button(fr_datos,command=b_aceptar_register,text=t_bu_aceptar,font="20",bg=color_black,fg=color_gray)
bu_aceptar2=Button(fr_datos,command=b_aceptar_entrar,text=t_bu_aceptar,font="20",bg=color_black,fg=color_gray)
#label abajo del boton aceptar
la_avisos=Label(fr_usuario,text=t_la_avisos,font="30")
la_avisos2=Label(fr_register,text=t_la_avisos,font="30")
#boton para mostrar u ocultar la contraseña
bu_mcontra=Button(fr_datos,command=m_contra)
ingresar_ocultar()
la_fondo_morado1=Label(fr_usuario,bg=color_la_fondo_m1)
la_fondo_morado2=Label(fr_usuario,bg=color_la_fondo_m1)

bu_crear_bin=Button(fr_usuario,command=crear_new_archivo_bin,text= t_bu_crear_bin,bg=color_green,font=20)
bu_abrir_bin=Button(fr_usuario,command=leer_archivo_bin,text=t_bu_abrir_bin,bg=color_green,font=20)
bu_borrar_bin=Button(fr_usuario,command=borrar_archivo_bin,text=t_bu_borrar_bin,bg=color_green,font=20)

bu_cerrar=Button(fr_usuario,command=cerrar,text=t_bu_cerrar ,bg=color_green,font=20)

bu_abrir_txt=Button(fr_usuario,command=escribir_archivo_bin,text=t_bu_abrir ,bg=color_green,font=20)
bu_borrar_txt=Button(fr_usuario,command=borrar_archivo_txt,text =t_bu_borrar ,bg=color_green,font=20)

#bu_crear_txt=Button(fr_usuario,command=crear_new_archivo_bin,text=  "Crear archivo ",bg="green",font=20)
#para ocultar estos widget
ocultar_opci_morado()
ver_select()
#t=Timer(5,avisos2("",True),args=None, kwargs=None)

# menu_opc=Menu(r,bg="#212121",bd="40",activebackground="green",fg="green")
# menu_opc.add_command(label="Opciones",command=acerca_de)
# menu_opc.add_command(label="Acerca de...",command=acerca_de)
# #menu_opc.config(bg="#212121",bd="40",fg="green")
# r.config(menu=menu_opc)

#print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
try:
    r.mainloop()
except:
    print("Hay un error")
    sys.exit()
    r.quit()
    #pass
#print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")



