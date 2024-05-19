'''
FILE    leer_xml.py, funciones.py
FUNCION Generar archivos (salida a dw powerbuilder, salida a PE mainframe)
AUTOR   Antonio Araujo
FECHA   Set/Oct 2.022 - 
'''
# -*- utf -8 -*-
import os
import time
from funciones import *
# import zipfile
import sys

def clear():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")

def terminar(argumento):
    # escribe archivo LOG con informacion del proceso
    lineas = ''
    final = time.strftime("%Y%m%d%H%M%S")
    if argumento==0:
        error = '00'
        errtext = 'PYTHON. OK.'
    if argumento==1:
        error = '01'
        errtext = 'FALTA ARCHIVO PARAMETROS_PYTHON.INI'
    if argumento==2:
        error = '01'    
        errtext = 'FALTA ARCHIVO PREMIUM-WORLD-CHECK.XML PARA IMPORTAR'
    if argumento==3:
        error = '01'
        errtext = 'ARCHIVO PREMIUM-WORLD-CHECK.XML SIN DATOS'
    # escribe archivo testigo
    archivo = 'TESTIGO_' + time.strftime("%Y%m%d") + '.TXT'
    fil_testigo = open(archivo,'w',encoding='utf-8')
    fil_testigo.write(errtext+'\n')
    fil_testigo.close()
    # escribe log  
    fil_sal_log = open('LOG.txt','w',encoding='utf-8')
    fil_sal_log.write(left(inicio,8)+'-1-'+inicio+'-'+final+'-'+right(str(1000000000+lazo),9)+'-'+right(str(1000000000+lazo1),9)+'-'+right(str(1000000000+lazo5),9)+'-'+right(str(1000000000+lazo2),9)+'-'+right(str(1000000000+lazo3),9)+'-'+right(str(1000000000+lazo4),9)+'-'+error+'-'+errtext+'\n')
    fil_sal_log.close()
    # sale de la aplicacion
    sys.exit()

clear()

# variables a usar
error = '00'
errtext = 'PYTHON. OK.'
lineas = ''
lazo = lazo1 = lazo2 = lazo3 = lazo4 = lazo5 = 0

# determina la fecha de inicio del proceso
inicio = time.strftime("%Y%m%d%H%M%S")

# verifica si existe el archivo de parametros
if not(os.path.isfile("parametros_python.ini")):
    terminar(2)
else:
    #abre archivo de entrada
    fil_ent = open("parametros_python.ini",'r',encoding='utf-8')
    lineas = fil_ent.readline()
    lineas = fil_ent.readline()
    camino = mid(lineas,8,len(lineas)-8)
    if right(camino,1)!=chr(92):
        camino = camino + chr(92)
    destino = os.getcwd() + chr(92)
    lineas = fil_ent.readline()    
    archivo = mid(lineas,9,len(lineas)-9)
    can_linea = 0
    # verifica si no existe el archivo
    if not(os.path.isfile(camino+archivo)):
        terminar(2)
    else:
        #abre archivo de entrada
        fil_ent = open(camino+archivo,'r',encoding='utf-8')
        # analiza si tiene filas que leer. Si no tiene cancela y cierra, sino prosigue con el resto
        if len(fil_ent.readlines())<=2:
            terminar(3)
        #crea archivo salida datos unicos
        fil_sal_datos_unicos = open(destino + "datos_unicos.txt",'w',encoding='utf-8')
        fil_sal_datos_unicos.write("<?xml  version='1.0' encoding='UTF-8'?>"+'\n'+"<d_worldcheck>"+'\n'+"<d_worldcheck_row>"+'\n')
        #crea archivo salida individuos
        fil_sal_individuos = open(destino + "individuos.txt",'w',encoding='utf-8')
        fil_sal_individuos.write("<?xml  version='1.0' encoding='UTF-8'?>"+'\n'+"<d_individuo>"+'\n'+"<d_individuo_row>"+'\n')
        #crea archivo salida alias
        fil_sal_alias = open(destino + "alias.txt",'w',encoding='utf-8')
        fil_sal_alias.write("<?xml  version='1.0' encoding='UTF-8'?>"+'\n'+"<d_alias>"+'\n'+"<d_alias_row>"+'\n')
        #crea archivo salida sanciones
        fil_sal_keyword = open(destino + "keyword.txt",'w',encoding='utf-8')
        fil_sal_keyword.write("<?xml  version='1.0' encoding='UTF-8'?>"+'\n'+"<d_sanciones>"+'\n'+"<d_sanciones_row>"+'\n')
        #crea archivo salida linked
        fil_sal_linked = open(destino + "linked.txt",'w',encoding='utf-8')
        fil_sal_linked.write("<?xml  version='1.0' encoding='UTF-8'?>"+'\n'+"<d_linkedto>"+'\n'+"<d_linkedto_row>"+'\n')
        # lineas = fil_ent.readlines()
        lineas = fil_ent.readline()
        fil_ent.seek(0)
        posini = posfin = longitud = 0
        mark1 = mark2 = mark3 = mark4 = 0
        xcad = xuid = xemp = xdob = xpob = xtit = xpos = ''
        xei = '<ei>E</ei>'
        marcat = marcei = marnom = marape = maralias = mardob = marpob = marcoun = 0
        for cadena in fil_ent:
            lazo += 1
            cadena = cadena.strip()
            # descarta los siguientes tags
            if  ('<?xml' in cadena) or ('<records' in cadena) or ('<deceased' in cadena) or ('</agedata>' in cadena) or ('<further_information>' in cadena or len(cadena)==1):
                continue
            # filtra la cadena para eliminar caracteres
            cadena = filtrar(cadena)
            #categoria
            if ("<record category=" in cadena):
                if (mark1>0 or mark2>0 or mark3>0 or mark4>=0):
                    if (xei!='<ei>E</ei>'):
                        if (mark1==0):
                            xdob = '<dob>NONE</dob>'
                        if (mark2==0):
                            xpob = '<place_of_birth>NONE</place_of_birth>'        
                        if (mark3==0):
                            xtit = '<title>NONE</title>'
                        if (mark4==0):
                            xpos = '<position>NONE</position>'
                        fil_sal_individuos.write(xuid + xdob + xpob + xtit + xpos + '\n')
                        lazo5 += 1
                        mark1 = mark2 = mark3 = mark4 = 0  
                #category
                xcategory = f_leer(cadena,'category=','editor=')
                #entered
                xentered = f_leer(cadena,'entered=','updatecategory=')
                #updatecategory
                xupdatecategory = f_leer(cadena,'updatecategory=','sub-category=')
                #sub-category
                xsubcat = f_leer(cadena,'sub-category=','uid=')
                #uid
                xuid = f_leer(cadena,'uid=','updated=')
                #updated
                xupdated = f_leer(cadena,'updated=','')                
                marcat = 1
                lazo1 += 1
                continue
            #e-i
            if ("e-i=" in cadena):
                xei = f_leer(cadena,'e-i=','')
                marcei = 1
                continue
            #last_name
            if ("<last_name>" in cadena):
                xape = f_leer(cadena,'<last_name>','</last_name>')                                
                marape = 1
                continue
            #first_name
            if ("<first_name" in cadena):
                if ('<first_name/>' in cadena):
                    xnom = ' '
                    marnom = 1
                if ('<first_name>' in cadena):
                    x= cadena.index('<first_name')
                    y = cadena.index("</first_name>")
                    xnom = cadena[(x+12):y]
                    xnom = '<first_name>' + xnom.strip() + '</first_name>'
                    xnom = xnom.replace("'","")
                    marnom = 1
            #alias
            if ("<alias>" in cadena):
                xalias = f_leer(cadena,'<alias>','</alias>')                
                fil_sal_alias.write(xuid + xalias + '\n')
                lazo2 += 1
                continue
            #keyword
            if ("<keyword>" in cadena):
                xkey = f_leer(cadena,'<keyword>','</keyword>')
                fil_sal_keyword.write(xuid + xkey + '\n')
                lazo3 += 1
                continue
            #linked
            if ("<uid>" in cadena):
                xlink = f_leer(cadena,'<uid>','</uid>')
                fil_sal_linked.write(xuid + xlink + '\n')
                lazo4 += 1
                continue
            #country
            if ("<country>" in cadena):
                x = cadena.index('<country>')
                y = cadena.index("</country")
                xcoun = cadena[(x+9):y]
                xpais = buscar_pais(xcoun)
                xpais = '<codigo_pais>' + xpais + '</codigo_pais>'
                xcoun = '<country>' + xcoun.strip() + '</country>'
                xcoun = xcoun.replace("'","")
                marcoun = 1
                continue
            #individuos
            if ("<dob>" in cadena):
                xdob = f_leer(cadena,'<dob>','</dob')
                mark1 = 1
                continue
            # lugar nacimiento
            if ("<place_of_birth>" in cadena):
                xpob = f_leer(cadena,'<place_of_birth>','</place_of_birth>')
                mark2 = 1
                continue
            # titulo
            if ("<title>" in cadena):
                xtit = f_leer(cadena,'<title>','</title')
                # x = cadena.index('<title>')
                # y = cadena.index("</title")
                # xtit = cadena[(x+7):y]
                # xtit = '<title>' + xtit + '</title>'
                # xtit = xtit.replace("'","")
                mark3 = 1
                continue
            # posicion/cargo
            if ("<position>" in cadena):
                xpos = f_leer(cadena,'<position>','</position')
                mark4 = 1
                continue        
            # escribe registro datos unicos
            if (marcat==1 and marcei==1 and marnom==1 and marape==1 and marcoun==1):
                fil_sal_datos_unicos.write(xuid + xei + xape + xnom + xcategory + xentered + xsubcat + xupdatecategory + xupdated + xcoun + xpais + "\n")
                marcat = marcei = marnom = marape = marcoun = 0
        # cierra archivo origen
        fil_ent.close
        # cierra datos unicos
        fil_sal_datos_unicos.write("</d_worldcheck_row>"+'\n'+"</d_worldcheck>"+'\n')
        fil_sal_datos_unicos.close()
        # cieraa individuos
        fil_sal_individuos.write("</d_individuo_row>"+'\n'+"</d_individuo>"+'\n')
        fil_sal_individuos.close()
        # cierra alias
        fil_sal_alias.write("</d_alias_row>"+'\n'+"</d_alias>"+'\n')
        fil_sal_alias.close()
        # cierra keyword
        fil_sal_keyword.write("</d_sanciones_row>"+'\n'+"</d_sanciones>"+'\n')
        fil_sal_keyword.close()
        # cierra linked
        fil_sal_linked.write("</d_linkedto_row>"+'\n'+"</d_linkedto>"+'\n')
        fil_sal_linked.close()
# finaliza proceso
terminar(0)

# comprimir archivo. Quito el respaldo ya que RPA hace una copia del mismo en carpeta
# file_zip = "wlc_" + str(final) + ".zip"
# wlc_zip = zipfile.ZipFile(file_zip, 'w', allowZip64=True)
# archivo = camino + archivo
# wlc_zip.write(archivo, compress_type=zipfile.ZIP_DEFLATED)
# wlc_zip.close()
