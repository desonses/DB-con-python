#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 00:18:05 2019

@author: fredy marin

uaem

desonses@gmail.com
"""
import psycopg2
import time
import os
from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return db

#+++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++
"""
Func que realiza el calculo de votos realizados en casillas Rural y Urbana en las elecciones
a Presidente, recibe un estado de la republica ingresado por el usuario. El resultado se muestra en pantalla
"""
def cand_box_rural_urb(estado):# Ingresar estado (mostrar candidato ganador en casillas rurales y urbanas)
    conn = None
    try:
        # read the connection parameters
        params = config()
        
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
################
### CODIGO BEGIN

        #estado="AGUASCALIENTES"
        casilla=["Rural","Urbana"]
    
        for box in casilla:
            cur.execute("SELECT SUM(presidencia_votos.PAN),SUM(presidencia_votos.PRI), SUM(presidencia_votos.PRD),SUM(presidencia_votos.PVEM),SUM(presidencia_votos.PT),SUM(presidencia_votos.MOVIMIENTO_CIUDADANO), SUM(presidencia_votos.NUEVA_ALIANZA), SUM(presidencia_votos.MORENA), SUM(presidencia_votos.ENCUENTRO_SOCIAL), SUM(presidencia_votos.PAN_PRD_MC), SUM(presidencia_votos.PAN_PRD), SUM(presidencia_votos.PAN_MC) , SUM(presidencia_votos.PRD_MC) , SUM(presidencia_votos.PRI_PVEM_NA) , 	SUM(presidencia_votos.PRI_PVEM) , SUM(presidencia_votos.PRI_NA) , SUM(presidencia_votos.PVEM_NA) , SUM(presidencia_votos.PT_MORENA_PES) , SUM(presidencia_votos.PT_MORENA) ,SUM(presidencia_votos.PT_PES) , SUM(presidencia_votos.MORENA_PES) ,SUM(presidencia_votos.CAND_IND_01) , SUM(presidencia_votos.CAND_IND_02) FROM presidencia_votos WHERE presidencia_votos.casilla="+"'"+box+"'"+"and presidencia_votos.nombre_estado="+"'"+estado+"'"+";")       
            rows = cur.fetchall()
            for row in rows:
                PAN=row[0]
                PRI=row[1]
                PRD=row[2]
                PVEM=row[3]
                PT=row[4]
                MOVIMIENTO_CIUDADANO=row[5]
                NUEVA_ALIANZA=row[6]
                MORENA=row[7]
                ENCUENTRO_SOCIAL=row[8]
                PAN_PRD_MC=row[9]
                PAN_PRD=row[10]
                PAN_MC=row[11]
                PRD_MC=row[12]
                PRI_PVEM_NA=row[13]
                PRI_PVEM=row[14]
                PRI_NA=row[15]
                PVEM_NA=row[16]
                PT_MORENA_PES=row[17]
                PT_MORENA=row[18]
                PT_PES=row[19]
                MORENA_PES=row[20]
                CAND_IND_01=row[21]
                CAND_IND_02=row[22]
                
                maximo=max( PAN,PRI,PRD,PVEM,PT,MOVIMIENTO_CIUDADANO,NUEVA_ALIANZA,MORENA,ENCUENTRO_SOCIAL,PAN_PRD_MC,PAN_PRD,PAN_MC,PRD_MC,PRI_PVEM_NA,PRI_PVEM,PRI_NA,PVEM_NA,PT_MORENA_PES,PT_MORENA,PT_PES,MORENA_PES, CAND_IND_01,CAND_IND_02)
                
                if(maximo==PAN):
                    partido="PAN"
                if(maximo==PRI):
                    partido="PRI"
                if(maximo==PRD):
                    partido="PRD"
                if(maximo==PVEM):
                    partido="PVEM"
                if(maximo==PT):
                    partido="PT"
                if(maximo==MOVIMIENTO_CIUDADANO):
                    partido="MOVIMIENTO_CIUDADANO"
                if(maximo==NUEVA_ALIANZA):
                    partido="NUEVA_ALIANZA"
                if(maximo==MORENA):
                    partido="MORENA"
                if(maximo==ENCUENTRO_SOCIAL):
                    partido="ENCUENTRO_SOCIAL"
                if(maximo==PAN_PRD_MC):
                    partido="PAN_PRD_MC"
                if(maximo==PAN_PRD):
                    partido="PAN_PRD"
                if(maximo==PRD_MC):
                    partido="PRD_MC"
                if(maximo==PRI_PVEM_NA):
                    partido="PRI_PVEM_NA"
                if(maximo==PRI_PVEM):
                    partido="PRI_PVEM"
                if(maximo==PRI_NA):
                    partido="PRI_NA"
                if(maximo==PVEM_NA):
                    partido="PVEM_NA"
                if(maximo==PT_MORENA_PES):
                    partido="PT_MORENA_PES"
                if(maximo==PT_MORENA):
                    partido="PT_MORENA"
                if(maximo==PT_PES):
                    partido="PT_PES"
                if(maximo==MORENA_PES):
                    partido="MORENA_PES"
                if(maximo==CAND_IND_01):
                    partido="CAND_IND_O1"
                if(maximo==CAND_IND_02):  
                    partido="CAND_IND_02"
                    
                print('\n')
                print("Partido", partido,"con mayoria de votos en ",estado ,"con ",maximo,"votos en casillas", box)
                    
                cur.execute("SELECT candidatos.partido_ci, candidatos.candidato_a, candidatos.candidatura_propietaria FROM candidatos WHERE candidatos.partido_ci="+"'"+partido+"'"+"and candidatos.candidato_a='Presidente';")
                rows = cur.fetchall()
                for row in rows:
                    partido=row[0]
                    candidato_a=row[1]
                    propietario=row[2]
                print('\n')
                print("Partido ganador: ",partido)
                print("Candidato a: " ,candidato_a)
                print("Candidato: " ,propietario)
            
        print("Operation successfully...")
        
### CODIGO END
##############

        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()    

#+++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++

"""
Func que calcula el candidato ganador a la Presidencia por estado, no recibe un estado, los resultados
se generan directamente consultando a la bd por estado y realizando el conteo de votos.
El resultado se muestra en pantalla
"""
def cand_by_state():# Mostrar candidato ganador por estado
    conn = None
    try:
        # read the connection parameters
        params = config()
        
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

################
### CODIGO BEGIN
    
        estado=["AGUASCALIENTES","BAJA CALIFORNIA","BAJA CALIFORNIA SUR","CAMPECHE","COAHUILA","COLIMA","CHIAPAS","CHIHUAHUA","CIUDAD DE MÉXICO","DURANGO","GUANAJUATO","GUERRERO","HIDALGO","JALISCO","MÉXICO","MICHOACÁN","MORELOS","NAYARIT","NUEVO LEÓN","OAXACA","PUEBLA","QUERÉTARO","QUINTANA ROO","SAN LUIS POTOSÍ","SINALOA","SONORA","TABASCO","TAMAULIPAS","TLAXCALA","VERACRUZ","YUCATÁN","ZACATECAS"]
    
        for state in estado:
            cur.execute("SELECT SUM(presidencia_votos.PAN),SUM(presidencia_votos.PRI),SUM(presidencia_votos.PRD),SUM(presidencia_votos.PVEM),SUM(presidencia_votos.PT),	SUM(presidencia_votos.MOVIMIENTO_CIUDADANO), SUM(presidencia_votos.NUEVA_ALIANZA) , SUM(presidencia_votos.MORENA), SUM(presidencia_votos.ENCUENTRO_SOCIAL), SUM(presidencia_votos.PAN_PRD_MC),SUM(presidencia_votos.PAN_PRD), SUM(presidencia_votos.PAN_MC), SUM(presidencia_votos.PRD_MC), SUM(presidencia_votos.PRI_PVEM_NA), SUM(presidencia_votos.PRI_PVEM), SUM(presidencia_votos.PRI_NA), SUM(presidencia_votos.PVEM_NA), SUM(presidencia_votos.PT_MORENA_PES), 	SUM(presidencia_votos.PT_MORENA), 	SUM(presidencia_votos.PT_PES), SUM(presidencia_votos.MORENA_PES), 	SUM(presidencia_votos.CAND_IND_01), SUM(presidencia_votos.CAND_IND_02) FROM presidencia_votos WHERE presidencia_votos.NOMBRE_ESTADO="+"'"+state+"'"+";")
            rows = cur.fetchall()
            for row in rows:    
                PAN=row[0]
                PRI=row[1]
                PRD=row[2]
                PVEM=row[3]
                PT=row[4]
                MOVIMIENTO_CIUDADANO=row[5]
                NUEVA_ALIANZA=row[6]
                MORENA=row[7]
                ENCUENTRO_SOCIAL=row[8]
                PAN_PRD_MC=row[9]
                PAN_PRD=row[10]
                PAN_MC=row[11]
                PRD_MC=row[12]
                PRI_PVEM_NA=row[13]
                PRI_PVEM=row[14]
                PRI_NA=row[15]
                PVEM_NA=row[16]
                PT_MORENA_PES=row[17]
                PT_MORENA=row[18]
                PT_PES=row[19]
                MORENA_PES=row[20]
                CAND_IND_01=row[21]
                CAND_IND_02=row[22]
                         
                maximo=max(PAN,PRI,PRD,PVEM, PT,MOVIMIENTO_CIUDADANO,NUEVA_ALIANZA,MORENA,ENCUENTRO_SOCIAL, PAN_PRD_MC,PAN_PRD, PAN_MC,PRD_MC, PRI_PVEM_NA, PRI_PVEM,PRI_NA,PVEM_NA,PT_MORENA_PES,PT_MORENA,PT_PES, MORENA_PES,CAND_IND_01,CAND_IND_02)
    
                if(maximo==PAN):
                    partido="PAN"
                if(maximo==PRI):
                    partido="PRI"
                if(maximo==PRD):
                    partido="PRD"
                if(maximo==PVEM):
                    partido="PVEM"
                if(maximo==PT):
                    partido="PT"
                if(maximo==MOVIMIENTO_CIUDADANO):
                    partido="MOVIMIENTO_CIUDADANO"
                if(maximo==NUEVA_ALIANZA):
                    partido="NUEVA ALIANZA"
                if(maximo==MORENA):
                    partido="MORENA"
                if(maximo==ENCUENTRO_SOCIAL):
                    partido="ENCUENTRO_SOCIAL"
                if(maximo==PAN_PRD_MC):
                    partido="PAN_PRD_MC"
                if(maximo==PAN_PRD):
                    partido="PAN_PRD"
                if(maximo==PAN_MC):
                    partido="PAN_MC"
                if(maximo==PRD_MC):
                    partido="PRD_MC"
                if(maximo==PRI_PVEM_NA):
                    partido="PRI_PVEM_NA"
                if(maximo==PRI_PVEM):
                    partido="PRI_PVEM"
                if(maximo==PRI_NA):
                    partido="PRI_NA"
                if(maximo==PVEM_NA):
                    partido="PVEM_NA"
                if(maximo==PT_MORENA_PES):
                    partido="PT_MORENA_PES"
                if(maximo==PT_MORENA):
                    partido="PT_MORENA"
                if(maximo==PT_PES):
                    partido="PT_PES"
                if(maximo==MORENA_PES):
                    partido="MORENA_PES"
                if(maximo==CAND_IND_01):
                    partido="CAND_IND_01"
                if(maximo==CAND_IND_02):
                    partido="CAND_IND_02"
                
                print('\n')
                print("Partido",partido ,"con mayoria de votos en",state," con", maximo,"votos")
            
                cur.execute("SELECT candidatos.partido_ci, candidatos.candidato_a, candidatos.candidatura_propietaria FROM candidatos WHERE candidatos.partido_ci="+"'" +partido+"'"+"and candidatos.candidato_a='Presidente';")
                rows = cur.fetchall()
                for row in rows:
                    partido=row[0]
                    candidato_a=row[1]
                    propietario=row[2]
                print('\n')
                print("Partido ganador: ",partido)
                print("Candidato a:" ,candidato_a)
                print("Candidato: " ,propietario)
                print("--------------------------------------------")
    
        print("Operation successfully...")
### CODIGO END
##############

        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()   


#+++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++
"""
Func que realiza el resumen de elecciones para las tres elecciones disponibles
Presidencia, Senaduria y diputacion, genera un archivo de salida txt de acuerdo a la eleccion
elegida por el usuario
"""
def summary(elecciones):
    
    conn = None
    try:
        # read the connection parameters
        params = config()
        
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
      
################      
### CODIGO BEGIN 
        hora=time.strftime("%H:%M:%S")
        fecha=time.strftime("%d/%m/%y")
        
        estados=["AGUASCALIENTES","BAJA CALIFORNIA","BAJA CALIFORNIA SUR","CAMPECHE","COAHUILA","COLIMA","CHIAPAS","CHIHUAHUA","CIUDAD DE MÉXICO","DURANGO","GUANAJUATO","GUERRERO","HIDALGO","JALISCO","MÉXICO","MICHOACÁN","MORELOS","NAYARIT","NUEVO LEÓN","OAXACA","PUEBLA","QUERÉTARO","QUINTANA ROO","SAN LUIS POTOSÍ","SINALOA","SONORA","TABASCO","TAMAULIPAS","TLAXCALA","VERACRUZ","YUCATÁN","ZACATECAS"]

        for state in estados:
            
            if(elecciones=="Senador"):
                #msg=" Elecciones a Senador:"
                summary_senadores = open("senadores.txt","a")
                #summary_senadores.write(hora+" "+fecha+'\n\n')
                consulta1="select distinct senadurias_votos.id_distrito,senadurias_votos.nombre_distrito FROM senadurias_votos WHERE senadurias_votos.nombre_estado="+"'"+state+"'"+"order by senadurias_votos.id_distrito;"

            if(elecciones=="Diputado"):
                #msg=" Elecciones a Diputado:"
                summary_diputados = open("diputados.txt","a")
                consulta1="select distinct diputaciones_votos.id_distrito, diputaciones_votos.nombre_distrito FROM diputaciones_votos WHERE diputaciones_votos.nombre_estado="+"'"+state+"'"+"order by diputaciones_votos.id_distrito;"

            if(elecciones=="Presidente"):
                #msg=" Elecciones a Presidente:"
                summary_presidente = open("presidente.txt","a")
                consulta1="select distinct presidencia_votos.id_distrito,presidencia_votos.nombre_distrito FROM presidencia_votos WHERE presidencia_votos.nombre_estado="+"'"+state+"'"+"order by presidencia_votos.id_distrito;"
                
            cur.execute(consulta1)
            rows = cur.fetchall()

            #print('\n')
            #print("################################################")
            #print('\n')
            #print("Estado de", state + msg+'\n')
            #print("################################################")
            for row in rows:
                distrito=row[0]
                nombre_distrito=row[1]
                
                if(elecciones=="Senador"):
                    consulta2="select senadurias_votos.id_distrito, senadurias_votos.nombre_estado,SUM(senadurias_votos.PAN),SUM(senadurias_votos.PRI),SUM(senadurias_votos.PRD),SUM(senadurias_votos.PVEM), SUM(senadurias_votos.PT),SUM(senadurias_votos.MOVIMIENTO_CIUDADANO), SUM(senadurias_votos.NUEVA_ALIANZA), SUM(senadurias_votos.MORENA), SUM(senadurias_votos.ENCUENTRO_SOCIAL), SUM(senadurias_votos.PAN_PRD_MC), SUM(senadurias_votos.PAN_PRD), SUM(senadurias_votos.PAN_MC), SUM(senadurias_votos.PRD_MC), SUM(senadurias_votos.PRI_PVEM_NA), SUM(senadurias_votos.PRI_PVEM), SUM(senadurias_votos.PRI_NA), SUM(senadurias_votos.PVEM_NA), SUM(senadurias_votos.PT_MORENA_PES), SUM(senadurias_votos.PT_MORENA), SUM(senadurias_votos.PT_PES), SUM(senadurias_votos.MORENA_PES), SUM(senadurias_votos.CAND_IND_01), SUM(senadurias_votos.CAND_IND_02) from senadurias_votos WHERE senadurias_votos.nombre_estado="+"'"+state+"'"+"and senadurias_votos.id_distrito="+str(int(distrito))+"group by senadurias_votos.id_distrito, senadurias_votos.nombre_estado;"
                if(elecciones=="Diputado"):
                    consulta2="select diputaciones_votos.id_distrito, diputaciones_votos.nombre_estado,SUM(diputaciones_votos.PAN),SUM(diputaciones_votos.PRI),SUM(diputaciones_votos.PRD),SUM(diputaciones_votos.PVEM), SUM(diputaciones_votos.PT),SUM(diputaciones_votos.MOVIMIENTO_CIUDADANO), SUM(diputaciones_votos.NUEVA_ALIANZA), SUM(diputaciones_votos.MORENA), SUM(diputaciones_votos.ENCUENTRO_SOCIAL), SUM(diputaciones_votos.PAN_PRD_MC), SUM(diputaciones_votos.PAN_PRD), SUM(diputaciones_votos.PAN_MC), SUM(diputaciones_votos.PRD_MC), SUM(diputaciones_votos.PRI_PVEM_NA), SUM(diputaciones_votos.PRI_PVEM), SUM(diputaciones_votos.PRI_NA), SUM(diputaciones_votos.PVEM_NA), SUM(diputaciones_votos.PT_MORENA_PES), SUM(diputaciones_votos.PT_MORENA), SUM(diputaciones_votos.PT_PES), SUM(diputaciones_votos.MORENA_PES), SUM(diputaciones_votos.CAND_IND_01), SUM(diputaciones_votos.CAND_IND_02) from diputaciones_votos WHERE diputaciones_votos.nombre_estado="+"'"+state+"'"+"and diputaciones_votos.id_distrito="+str(int(distrito))+"group by diputaciones_votos.id_distrito, diputaciones_votos.nombre_estado;"
                if(elecciones=="Presidente"):
                    consulta2="select presidencia_votos.id_distrito, presidencia_votos.nombre_estado,SUM(presidencia_votos.PAN),SUM(presidencia_votos.PRI),SUM(presidencia_votos.PRD),SUM(presidencia_votos.PVEM), SUM(presidencia_votos.PT),SUM(presidencia_votos.MOVIMIENTO_CIUDADANO), SUM(presidencia_votos.NUEVA_ALIANZA), SUM(presidencia_votos.MORENA), SUM(presidencia_votos.ENCUENTRO_SOCIAL), SUM(presidencia_votos.PAN_PRD_MC), SUM(presidencia_votos.PAN_PRD), SUM(presidencia_votos.PAN_MC), SUM(presidencia_votos.PRD_MC), SUM(presidencia_votos.PRI_PVEM_NA), SUM(presidencia_votos.PRI_PVEM), SUM(presidencia_votos.PRI_NA), SUM(presidencia_votos.PVEM_NA), SUM(presidencia_votos.PT_MORENA_PES), SUM(presidencia_votos.PT_MORENA), SUM(presidencia_votos.PT_PES), SUM(presidencia_votos.MORENA_PES), SUM(presidencia_votos.CAND_IND_01), SUM(presidencia_votos.CAND_IND_02) from presidencia_votos WHERE presidencia_votos.nombre_estado="+"'"+state+"'"+"and presidencia_votos.id_distrito="+str(int(distrito))+"group by presidencia_votos.id_distrito, presidencia_votos.nombre_estado;"
                    
                cur.execute(consulta2)
                rows2 = cur.fetchall()
                
                for row2 in rows2:
                    id_distrito=row2[0]
                    #nombre_estado=row2[1]
                    PAN=row2[2]
                    PRI=row2[3]
                    PRD=row2[4]
                    PVEM=row2[5]
                    PT=row2[6]
                    MOVIMIENTO_CIUDADANO=row2[7]
                    NUEVA_ALIANZA=row2[8]
                    MORENA=row2[9]
                    ENCUENTRO_SOCIAL=row2[10]
                    PAN_PRD_MC=row2[11]
                    PAN_PRD=row2[12]
                    PAN_MC=row2[13]
                    PRD_MC=row2[14]
                    PRI_PVEM_NA=row2[15]
                    PRI_PVEM=row2[16]
                    PRI_NA=row2[17]
                    PVEM_NA=row2[18]
                    PT_MORENA_PES=row2[19]
                    PT_MORENA=row2[20]
                    PT_PES=row2[21]
                    MORENA_PES=row2[22]
                    CAND_IND_01=row2[23]
                    CAND_IND_02=row2[24]
                    maximo=max(PAN,PRI,PRD,PVEM,PT,MOVIMIENTO_CIUDADANO,NUEVA_ALIANZA,MORENA,ENCUENTRO_SOCIAL,PAN_PRD_MC,PAN_PRD,PAN_MC,PRD_MC,PRI_PVEM_NA,PRI_PVEM,PRI_NA,PVEM_NA,PT_MORENA_PES,PT_MORENA,PT_PES,MORENA_PES ,CAND_IND_01 ,CAND_IND_02)
                    if (maximo==PAN):
                        partido="PAN"
                    if (maximo==PRI):
                        partido="PRI"
                    if (maximo==PRD):
                        partido="PRD"
                    if (maximo==PVEM):
                        partido="PVEM"
                    if (maximo==PT):
                        partido="PT"
                    if (maximo==MOVIMIENTO_CIUDADANO):
                        partido="MOVIMIENTO_CIUDADANO"
                    if (maximo==NUEVA_ALIANZA):
                        partido="NUEVA_ALIANZA"
                    if (maximo==MORENA):
                        partido="MORENA"
                    if (maximo==ENCUENTRO_SOCIAL):
                        partido="ENCUENTRO_SOCIAL"
                    if (maximo==PAN_PRD_MC):
                        partido="PAN_PRD_MC"
                    if (maximo==PAN_PRD):
                        partido="PAN_PRD"
                    if (maximo==PAN_MC):
                        partido="PAN_MC"
                    if (maximo==PRD_MC):
                        partido="PRD_MC"
                    if (maximo==PRI_PVEM_NA):
                        partido="PRI_PVEM_NA"
                    if (maximo==PRI_PVEM):
                        partido="PRI_PVEM"
                    if (maximo==PRI_NA):
                        partido="PRI_NA"
                    if (maximo==PVEM_NA):
                        partido="PVEM_NA"
                    if (maximo==PT_MORENA_PES):
                        partido="PT_MORENA_PES"
                    if (maximo==PT_MORENA):
                        partido="PT_MORENA"
                    if (maximo==PT_PES):
                        partido="PT_PES"
                    if (maximo==MORENA_PES):
                        partido="MORENA_PES"
                    if (maximo==CAND_IND_01): 
                        partido="CAND_IND_01"
                    if (maximo==CAND_IND_02):
                        partido="CAND_IND_02"
                        
                    #print(PAN,PRI,PRD,PVEM,PT,MOVIMIENTO_CIUDADANO,NUEVA_ALIANZA,MORENA,ENCUENTRO_SOCIAL,PAN_PRD_MC,PAN_PRD,PAN_MC,PRD_MC,PRI_PVEM_NA,PRI_PVEM,PRI_NA,PVEM_NA,PT_MORENA_PES,PT_MORENA,PT_PES,MORENA_PES ,CAND_IND_01 ,CAND_IND_02)
                    #rint("maximo:", maximo)
                    #print("Partido ganador",partido, " con ",maximo," votos en el distrito ",id_distrito,nombre_distrito+'\n')
                    
                    if(elecciones=="Senador"):
                        consulta3="SELECT DISTINCT candidatos.candidatura_propietaria, candidatos.candidatura_suplente, candidatos.candidato_a, candidatos.partido_ci FROM candidatos WHERE candidatos.partido_ci="+"'"+partido+"'"+"and candidatos.candidato_a="+"'"+elecciones+"'"+"and candidatos.nombre_estado="+"'"+state+"'"+"and candidatos.id_distrito="+str(int(distrito))+";"
                    if(elecciones=="Diputado"):
                        consulta3="SELECT DISTINCT candidatos.candidatura_propietaria, candidatos.candidatura_suplente, candidatos.candidato_a, candidatos.partido_ci FROM candidatos WHERE candidatos.partido_ci="+"'"+partido+"'"+"and candidatos.candidato_a="+"'"+elecciones+"'"+"and candidatos.nombre_estado="+"'"+state+"'"+"and candidatos.id_distrito="+str(int(distrito))+";"
                    if(elecciones=="Presidente"):
                        consulta3="SELECT DISTINCT candidatos.candidatura_propietaria, candidatos.candidatura_suplente, candidatos.candidato_a FROM candidatos WHERE candidatos.partido_ci="+"'"+partido+"'"+"and candidatos.candidato_a="+"'"+elecciones+"'"+";"
                    
                    
                    cur.execute(consulta3)
                    rows3 = cur.fetchall()
                    
                    for row3 in rows3:
                        candidato_prop=row3[0]
                        candidato_supl=row3[1]
                        candidato_a=row3[2]
                        #partido_ci=row3[3]
                        if(elecciones=="Senador"):
                            summary_senadores.write("Partido ganador "+partido+" con "+str(maximo)+" votos en el distrito "+str(id_distrito)+" "+nombre_distrito+" de "+state+'\n'+candidato_prop+" candidato a "+candidato_a+" y el candidato suplente "+candidato_supl+'\n'+'\n')
                            #print(candidato_prop," candidato a", candidato_a," y el candidato suplente ",candidato_supl)
                        
                        if(elecciones=="Diputado"):
                            summary_diputados.write("Partido ganador "+partido+" con "+str(maximo)+" votos en el distrito "+str(id_distrito)+" "+nombre_distrito+" de "+state+'\n'+candidato_prop+" candidato a "+candidato_a+" y el candidato suplente "+candidato_supl+'\n'+'\n')
                            #print(candidato_prop," candidato a", candidato_a," y el candidato suplente ",candidato_supl)
                            
                        if(elecciones=="Presidente"):
                            summary_presidente.write("Partido ganador "+partido+" con "+str(maximo)+" votos en el distrito "+str(id_distrito) +" "+nombre_distrito+" de "+state+'\n'+"Candidato: "+candidato_prop +"Candidato a: "+candidato_a+'\n'+'\n')
                            #print(candidato_prop,"candidato a:", candidato_a+'\n')
                            
                    #print("-----------------------------------------------------")
        
        if(elecciones=="Senador"):
            summary_senadores.close()
                
        if(elecciones=="Diputado"):
            summary_diputados.close()
                
        if(elecciones=="Presidente"):
            summary_presidente.close()            

        print("Operation successfully...")

### CODIGO END
##############
        
            
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()  

#+++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++
"""
Func que realiza el conteo de votos por distrito en un estado en particular, calcula tanto
para senadores como diputados, recibe el estado definido por el usuario y candidato es agregado
de manera directa, segun la opcion en la que se encuentre del menu.
"candidato=Senador" o "candidato=Diputado".

El resultado se muestra en pantalla

"""

def senadurias_gan_distr(estado, candidato):
    
    conn = None
    try:
        # read the connection parameters
        params = config()
        
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
################
### CODIGO BEGIN 

        if(candidato=="Senador"):
            msg=" Elecciones a Senador:"
            consulta1="select distinct senadurias_votos.id_distrito,senadurias_votos.nombre_distrito FROM senadurias_votos WHERE senadurias_votos.nombre_estado="+"'"+estado+"'"+"order by senadurias_votos.id_distrito"+";"
        else:
            msg=" Elecciones a Diputado:"
            consulta1="select distinct diputaciones_votos.id_distrito, diputaciones_votos.nombre_distrito FROM diputaciones_votos WHERE diputaciones_votos.nombre_estado="+"'"+estado+"'"+"order by diputaciones_votos.id_distrito;"
        
        
        cur.execute(consulta1)
        rows = cur.fetchall()

        
        print('\n')
        print("################################################")
        print('\n')
        print("Estado de", estado + msg+'\n')
        print("################################################")
        for row in rows:
            distrito=row[0]
            nombre_distrito=row[1]
            
            if(candidato=="Senador"):
                consulta2="select senadurias_votos.id_distrito, senadurias_votos.nombre_estado,SUM(senadurias_votos.PAN),SUM(senadurias_votos.PRI),SUM(senadurias_votos.PRD),SUM(senadurias_votos.PVEM), SUM(senadurias_votos.PT),SUM(senadurias_votos.MOVIMIENTO_CIUDADANO), SUM(senadurias_votos.NUEVA_ALIANZA), SUM(senadurias_votos.MORENA), SUM(senadurias_votos.ENCUENTRO_SOCIAL), SUM(senadurias_votos.PAN_PRD_MC), SUM(senadurias_votos.PAN_PRD), SUM(senadurias_votos.PAN_MC), SUM(senadurias_votos.PRD_MC), SUM(senadurias_votos.PRI_PVEM_NA), SUM(senadurias_votos.PRI_PVEM), SUM(senadurias_votos.PRI_NA), SUM(senadurias_votos.PVEM_NA), SUM(senadurias_votos.PT_MORENA_PES), SUM(senadurias_votos.PT_MORENA), SUM(senadurias_votos.PT_PES), SUM(senadurias_votos.MORENA_PES), SUM(senadurias_votos.CAND_IND_01), SUM(senadurias_votos.CAND_IND_02) from senadurias_votos WHERE senadurias_votos.nombre_estado="+"'"+estado+"'"+"and senadurias_votos.id_distrito="+str(int(distrito))+"group by senadurias_votos.id_distrito, senadurias_votos.nombre_estado;"
            else:
                consulta2="select diputaciones_votos.id_distrito, diputaciones_votos.nombre_estado,SUM(diputaciones_votos.PAN),SUM(diputaciones_votos.PRI),SUM(diputaciones_votos.PRD),SUM(diputaciones_votos.PVEM), SUM(diputaciones_votos.PT),SUM(diputaciones_votos.MOVIMIENTO_CIUDADANO), SUM(diputaciones_votos.NUEVA_ALIANZA), SUM(diputaciones_votos.MORENA), SUM(diputaciones_votos.ENCUENTRO_SOCIAL), SUM(diputaciones_votos.PAN_PRD_MC), SUM(diputaciones_votos.PAN_PRD), SUM(diputaciones_votos.PAN_MC), SUM(diputaciones_votos.PRD_MC), SUM(diputaciones_votos.PRI_PVEM_NA), SUM(diputaciones_votos.PRI_PVEM), SUM(diputaciones_votos.PRI_NA), SUM(diputaciones_votos.PVEM_NA), SUM(diputaciones_votos.PT_MORENA_PES), SUM(diputaciones_votos.PT_MORENA), SUM(diputaciones_votos.PT_PES), SUM(diputaciones_votos.MORENA_PES), SUM(diputaciones_votos.CAND_IND_01), SUM(diputaciones_votos.CAND_IND_02) from diputaciones_votos WHERE diputaciones_votos.nombre_estado="+"'"+estado+"'"+"and diputaciones_votos.id_distrito="+ str(int(distrito))+"group by diputaciones_votos.id_distrito, diputaciones_votos.nombre_estado;"
                
            cur.execute(consulta2)
            rows2 = cur.fetchall()
            
            for row2 in rows2:
                id_distrito=row2[0]
                #nombre_estado=row2[1]
                PAN=row2[2]
                PRI=row2[3]
                PRD=row2[4]
                PVEM=row2[5]
                PT=row2[6]
                MOVIMIENTO_CIUDADANO=row2[7]
                NUEVA_ALIANZA=row2[8]
                MORENA=row2[9]
                ENCUENTRO_SOCIAL=row2[10]
                PAN_PRD_MC=row2[11]
                PAN_PRD=row2[12]
                PAN_MC=row2[13]
                PRD_MC=row2[14]
                PRI_PVEM_NA=row2[15]
                PRI_PVEM=row2[16]
                PRI_NA=row2[17]
                PVEM_NA=row2[18]
                PT_MORENA_PES=row2[19]
                PT_MORENA=row2[20]
                PT_PES=row2[21]
                MORENA_PES=row2[22]
                CAND_IND_01=row2[23]
                CAND_IND_02=row2[24]
                maximo=max(PAN,PRI,PRD,PVEM,PT,MOVIMIENTO_CIUDADANO,NUEVA_ALIANZA,MORENA,ENCUENTRO_SOCIAL,PAN_PRD_MC,PAN_PRD,PAN_MC,PRD_MC,PRI_PVEM_NA,PRI_PVEM,PRI_NA,PVEM_NA,PT_MORENA_PES,PT_MORENA,PT_PES,MORENA_PES ,CAND_IND_01 ,CAND_IND_02)
                if (maximo==PAN):
                    partido="PAN"
                if (maximo==PRI):
                    partido="PRI"
                if (maximo==PRD):
                    partido="PRD"
                if (maximo==PVEM):
                    partido="PVEM"
                if (maximo==PT):
                    partido="PT"
                if (maximo==MOVIMIENTO_CIUDADANO):
                    partido="MOVIMIENTO_CIUDADANO"
                if (maximo==NUEVA_ALIANZA):
                    partido="NUEVA_ALIANZA"
                if (maximo==MORENA):
                    partido="MORENA"
                if (maximo==ENCUENTRO_SOCIAL):
                    partido="ENCUENTRO_SOCIAL"
                if (maximo==PAN_PRD_MC):
                    partido="PAN_PRD_MC"
                if (maximo==PAN_PRD):
                    partido="PAN_PRD"
                if (maximo==PAN_MC):
                    partido="PAN_MC"
                if (maximo==PRD_MC):
                    partido="PRD_MC"
                if (maximo==PRI_PVEM_NA):
                    partido="PRI_PVEM_NA"
                if (maximo==PRI_PVEM):
                    partido="PRI_PVEM"
                if (maximo==PRI_NA):
                    partido="PRI_NA"
                if (maximo==PVEM_NA):
                    partido="PVEM_NA"
                if (maximo==PT_MORENA_PES):
                    partido="PT_MORENA_PES"
                if (maximo==PT_MORENA):
                    partido="PT_MORENA"
                if (maximo==PT_PES):
                    partido="PT_PES"
                if (maximo==MORENA_PES):
                    partido="MORENA_PES"
                if (maximo==CAND_IND_01): 
                    partido="CAND_IND_01"
                if (maximo==CAND_IND_02):
                    partido="CAND_IND_02"
                    
                print("Partido ganador",partido, "con",maximo,"votos en el distrito",id_distrito,nombre_distrito+'\n')
                
                if(candidato=="Senador"):
                    consulta3="SELECT DISTINCT candidatos.candidatura_propietaria, candidatos.candidatura_suplente, candidatos.candidato_a, candidatos.partido_ci FROM candidatos WHERE candidatos.partido_ci="+"'"+partido+"'"+"and candidatos.candidato_a="+"'"+candidato+"'"+"and candidatos.nombre_estado="+"'"+estado+"'"+"and candidatos.id_distrito="+str(int(distrito))+";"
                else:
                    consulta3="SELECT DISTINCT candidatos.candidatura_propietaria, candidatos.candidatura_suplente, candidatos.candidato_a, candidatos.partido_ci FROM candidatos WHERE candidatos.partido_ci="+"'"+partido+"'"+"and candidatos.candidato_a="+"'"+candidato +"'"+"and candidatos.nombre_estado="+"'"+estado+"'"+"and candidatos.id_distrito="+str(int(distrito))+";"
                
                
                cur.execute(consulta3)
                rows3 = cur.fetchall()
                
                for row3 in rows3:
                    candidato_prop=row3[0]
                    candidato_supl=row3[1]
                    candidato_a=row3[2]
                    #partido_c=row3[3]
                    print(candidato_prop," candidato a", candidato_a," y el candidato suplente ",candidato_supl)
                    
                print("-----------------------------------------------------")
    
        print("Operation successfully...")
### CODIGO END
##############

        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()  


#+++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++
"""
Realiza el conteo de votos validos y votos nulos por distrito de un estado en particular
la func recibe el estado ingreso por el usuario y eleccion es definida en las opciones, calcula
los votos tanto para senador y diputado segun "eleccion=Diputado" o "eleccion=Senador".

El resultado se muestra en pantalla

"""
def votos_tot_null(estado,eleccion):
    
    conn = None
    try:
        # read the connection parameters
        params = config()
        
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
################
### CODIGO BEGIN
 
        if(eleccion=="Senador"):
            consulta1="select distinct senadurias_votos.id_distrito,senadurias_votos.nombre_distrito FROM senadurias_votos WHERE senadurias_votos.nombre_estado="+"'"+estado+"'"+"order by senadurias_votos.id_distrito;"
        else:
            consulta1="select distinct diputaciones_votos.id_distrito,diputaciones_votos.nombre_distrito FROM diputaciones_votos WHERE diputaciones_votos.nombre_estado="+"'"+estado+"'"+"order by diputaciones_votos.id_distrito;"
            
        cur.execute(consulta1)
        rows = cur.fetchall()
        
        print('\n')
        print("#############################################")
        print("Estado de",estado+" conteo de votos totales en elecciones a",eleccion ,'\n')
        print("#############################################")
        for row in rows:
            distrito=row[0]
            nombre_distrito=row[1]
            
            if(eleccion=="Senador"):
                consulta2="select SUM(senadurias_votos.PAN),SUM(senadurias_votos.PRI),SUM(senadurias_votos.PRD),SUM(senadurias_votos.PVEM), SUM(senadurias_votos.PT),SUM(senadurias_votos.MOVIMIENTO_CIUDADANO), SUM(senadurias_votos.NUEVA_ALIANZA), SUM(senadurias_votos.MORENA), SUM(senadurias_votos.ENCUENTRO_SOCIAL), SUM(senadurias_votos.PAN_PRD_MC), SUM(senadurias_votos.PAN_PRD), SUM(senadurias_votos.PAN_MC), SUM(senadurias_votos.PRD_MC), SUM(senadurias_votos.PRI_PVEM_NA), SUM(senadurias_votos.PRI_PVEM), SUM(senadurias_votos.PRI_NA), SUM(senadurias_votos.PVEM_NA), SUM(senadurias_votos.PT_MORENA_PES), SUM(senadurias_votos.PT_MORENA), SUM(senadurias_votos.PT_PES), SUM(senadurias_votos.MORENA_PES), SUM(senadurias_votos.CAND_IND_01), SUM(senadurias_votos.CAND_IND_02),SUM(VN) from senadurias_votos WHERE senadurias_votos.nombre_estado="+"'"+estado+"'"+"and senadurias_votos.id_distrito="+ str(int(distrito))+"group by senadurias_votos.id_distrito, senadurias_votos.nombre_estado;"
            else:
                consulta2="select SUM(diputaciones_votos.PAN),SUM(diputaciones_votos.PRI),SUM(diputaciones_votos.PRD),SUM(diputaciones_votos.PVEM), SUM(diputaciones_votos.PT),SUM(diputaciones_votos.MOVIMIENTO_CIUDADANO), SUM(diputaciones_votos.NUEVA_ALIANZA), SUM(diputaciones_votos.MORENA), SUM(diputaciones_votos.ENCUENTRO_SOCIAL), SUM(diputaciones_votos.PAN_PRD_MC), SUM(diputaciones_votos.PAN_PRD), SUM(diputaciones_votos.PAN_MC), SUM(diputaciones_votos.PRD_MC), SUM(diputaciones_votos.PRI_PVEM_NA), SUM(diputaciones_votos.PRI_PVEM), SUM(diputaciones_votos.PRI_NA), SUM(diputaciones_votos.PVEM_NA), SUM(diputaciones_votos.PT_MORENA_PES), SUM(diputaciones_votos.PT_MORENA), SUM(diputaciones_votos.PT_PES), SUM(diputaciones_votos.MORENA_PES), SUM(diputaciones_votos.CAND_IND_01), SUM(diputaciones_votos.CAND_IND_02),SUM(VN) from diputaciones_votos WHERE diputaciones_votos.nombre_estado="+"'"+estado+"'"+"and diputaciones_votos.id_distrito="+ str(int(distrito))+"group by diputaciones_votos.id_distrito, diputaciones_votos.nombre_estado;"
            
            cur.execute(consulta2)
            rows2 = cur.fetchall()
            
            for row2 in rows2:
                PAN=row2[0]
                PRI=row2[1]
                PRD=row2[2]
                PVEM=row2[3]
                PT=row2[4]
                MOVIMIENTO_CIUDADANO=row2[5]
                NUEVA_ALIANZA=row2[6]
                MORENA=row2[7]
                ENCUENTRO_SOCIAL=row2[8]
                PAN_PRD_MC=row2[9]
                PAN_PRD=row2[10]
                PAN_MC=row2[11]
                PRD_MC=row2[12]
                PRI_PVEM_NA=row2[13]
                PRI_PVEM=row2[14]
                PRI_NA=row2[15]
                PVEM_NA=row2[16]
                PT_MORENA_PES=row2[17]
                PT_MORENA=row2[18]
                PT_PES=row2[19]
                MORENA_PES=row2[20]
                CAND_IND_01=row2[21] 
                CAND_IND_02=row2[22]     
                
                #VOTOS NULOS
                VN=row2[23]
                
                TOTAL_VOTOS=(PAN+PRI+PRD+PVEM+PT+MOVIMIENTO_CIUDADANO+NUEVA_ALIANZA+MORENA+ENCUENTRO_SOCIAL+PAN_PRD_MC+PAN_PRD+PAN_MC+PRD_MC+PRI_PVEM_NA+PRI_PVEM+PRI_NA+PVEM_NA+PT_MORENA_PES+PT_MORENA+PT_PES+MORENA_PES+CAND_IND_01+CAND_IND_02)
                
                print("Total de votos validos en", estado,"distrito ", distrito, nombre_distrito,"es de ",TOTAL_VOTOS)
                print("Total de votos NULOS en", estado,"distrito ", distrito, nombre_distrito,"es de ",VN)
                print('\n')
                    
        print("Operation successfully...")
        
### CODIGO END
##############

        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()  

#+++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++
            

""" Recibe un nombre de estado ingresado por el usuario, sino esta en la lista no es un estado o esta mal escrito"""

def estados(estado):
    estados=["AGUASCALIENTES","BAJA CALIFORNIA","BAJA CALIFORNIA SUR","CAMPECHE","COAHUILA","COLIMA","CHIAPAS","CHIHUAHUA","CIUDAD DE MÉXICO","DURANGO","GUANAJUATO","GUERRERO","HIDALGO","JALISCO","MÉXICO","MICHOACÁN","MORELOS","NAYARIT","NUEVO LEÓN","OAXACA","PUEBLA","QUERÉTARO","QUINTANA ROO","SAN LUIS POTOSÍ","SINALOA","SONORA","TABASCO","TAMAULIPAS","TLAXCALA","VERACRUZ","YUCATÁN","ZACATECAS"]
    
    if(estado in estados):
        return 1
    else:
        return 0


#+++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++
""" Manajeo de opciones para elecciones a presidente"""

def presidencia():
    print("\t1 - Mostrar candidato ganador por estado")
    print("\t2 - Mostrar candidato ganador en casillas rurales y urbanas")
    print("\t3 - Resumen de elecciones (genera un archivo txt)")
    
    opcion = input("? >> ")
    
    if (opcion=="1"):
        cand_by_state()
        
    elif(opcion=="2"):
        print("Ingresa un estado de la Republica:")
        estado=input("> ").upper()
        if(estados(estado)==1):
            cand_box_rural_urb(estado)
        else:
            print("No es un estado o no esta bien escrito...")
    elif(opcion=="3"):
        print("Se generara un archivo de salida presidencia.txt")
        continuar=input("Continuar... s\\n: ")
        if(continuar=="s"):
            elecciones="Presidente"
            summary(elecciones)
        elif(continuar=="n"):
            presidencia()
        else:
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
    else:
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
          
        
#+++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++      
                
""" Manajeo de opciones para elecciones a diputados"""
def diputados():
    
    print("\t1 - Mostrar diputado ganador por distrito en un estado")
    print("\t2 - Mostrar total de votos y votos nulos por distrito en un estado")
    print("\t3 - Resumen de elecciones (genera un archivo txt)")
    
    opcion = input("? >> ")
    candidato="Diputado"
    eleccion="Diputado"
    
    if(opcion=="1"):    
        print("Ingresa un estado de la Republica:")
        estado=input("> ").upper()
        if(estados(estado)==1):
            senadurias_gan_distr(estado,candidato)
        else:
            print("No es un estado o no esta bien escrito...")
        
    elif(opcion=="2"):
        print("Ingresa un estado de la Republica:")
        estado=input("> ").upper()
        if(estados(estado)==1):
            votos_tot_null(estado,eleccion)
        else:
            print("No es un estado...")
        
    elif(opcion=="3"):
        print("Se generara un archivo de salida diputados.txt")
        continuar=input("Continuar... s\\n: ")
        if(continuar=="s"):
            elecciones="Diputado"
            summary(elecciones)
        elif(continuar=="n"):
            diputados()
        else:
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
        
    else:
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
        
        

#+++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++
""" Manajeo de opciones para elecciones a senador"""
def senadores():
    
    print("\t1 - Mostrar senador ganador por distrito en un estado")
    print("\t2 - Mostrar total de votos y votos nulos por distrito en un estado")
    print("\t3 - Mostrar resumen de elecciones (genera un archivo txt)")
    
    opcion = input("? >> ")
    candidato="Senador"
    eleccion="Senador"
    
    if(opcion=="1"):
        print("Ingresa un estado de la Republica:")
        estado=input("> ").upper()
        if(estados(estado)==1):
            senadurias_gan_distr(estado,candidato)
        else:
            print("No es un estado o no esta bien escrito...")
    elif(opcion=="2"):
        print("Ingresa un estado de la Republica:")
        estado=input("> ").upper()
        if(estados(estado)==1):
            votos_tot_null(estado,eleccion)
        else:
            print("No es un estado...")
    elif(opcion=="3"):
        print("Se generara un archivo de salida senadores.txt")
        continuar=input("Continuar... s\\n: ")
        if(continuar=="s"):
            elecciones="Senador"
            summary(elecciones)
        elif(continuar=="n"):
            diputados()
        else:
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
        
    else:
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
        

#+++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++

def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('clear') #
	print ("\nSelecciona una opción")
	print ("\t1 - Presidencia")
	print ("\t2 - Diputados")
	print ("\t3 - Senadores")
	print ("\t0 - Salir")
 

#+++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++
def main():
    while True:
    	# Mostramos el menu
    	menu()
     
    	# solicituamos una opción al usuario
    	opcionMenu = input("? >> ")
     
    	if (opcionMenu=="1"):
    		presidencia()
    	elif (opcionMenu=="2"):
    		diputados()
    	elif (opcionMenu=="3"):
    		senadores()
    	elif (opcionMenu=="0"):
    		break
    	else:
    		print ("")
    		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")


#+++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++

if __name__ == '__main__':

    main()
    
    
    
