#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 02:54:09 2018

@author: fredy
"""

import psycopg2
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
 
def create_tables():
    """ create tables in the PostgreSQL database"""
    tables = (
        """
        CREATE TABLE candidatos(
    ID SERIAL PRIMARY KEY,
    ID_ESTADO integer,
    ID_DISTRITO integer,
    NOMBRE_ESTADO varchar,
    PARTIDO_CI varchar,
    CANDIDATO_A varchar,
    CANDIDATURA_PROPIETARIA varchar,
    CANDIDATURA_SUPLENTE varchar
);
        """,
        """ 
        CREATE TABLE diputaciones_votos(
	CLAVE_CASILLA varchar, 
	CLAVE_ACTA varchar PRIMARY KEY,
	ID_ESTADO integer,
    FOREIGN KEY (ID_ESTADO)
        REFERENCES candidatos (ID)
        ON UPDATE CASCADE ON DELETE CASCADE,
	NOMBRE_ESTADO varchar, 
	ID_DISTRITO integer, 
	NOMBRE_DISTRITO varchar, 
	SECCION integer, 
	ID_CASILLA varchar, 
	TIPO_CASILLA varchar, 
	EXT_CONTIGUA varchar, 
	CASILLA varchar, 
	NUM_ACTA_IMPRESO varchar, 
	PAN integer, 
	PRI integer, 
	PRD integer, 
	PVEM integer, 
	PT integer, 
	MOVIMIENTO_CIUDADANO integer, 
	NUEVA_ALIANZA integer, 
	MORENA integer, 
	ENCUENTRO_SOCIAL integer, 
	PAN_PRD_MC integer, 
	PAN_PRD integer, 
	PAN_MC integer, 
	PRD_MC integer, 
	PRI_PVEM_NA integer, 
	PRI_PVEM integer, 
	PRI_NA integer, 
	PVEM_NA integer, 
	PT_MORENA_PES integer, 
	PT_MORENA integer, 
	PT_PES integer, 
	MORENA_PES integer, 
	CAND_IND_01 integer, 
	CAND_IND_02 integer, 
	CNR varchar, 
	VN integer, 
	TOTAL_VOTOS_CALCULADOS integer, 
	LISTA_NOMINAL_CASILLA varchar, 
	OBSERVACIONES varchar, 
	MECANISMOS_TRASLADO varchar, 
	FECHA_HORA varchar
    
);

        """,
        """
        CREATE TABLE presidencia_votos(
	CLAVE_CASILLA varchar, 
	CLAVE_ACTA varchar PRIMARY KEY,
	ID_ESTADO integer, 
	FOREIGN KEY (ID_ESTADO)
        REFERENCES candidatos (ID)
        ON UPDATE CASCADE ON DELETE CASCADE,
     
    NOMBRE_ESTADO varchar, 
	ID_DISTRITO integer,
	NOMBRE_DISTRITO varchar, 
	SECCION integer, 
	ID_CASILLA varchar, 
	TIPO_CASILLA varchar, 
	EXT_CONTIGUA varchar, 
	CASILLA varchar, 
	NUM_ACTA_IMPRESO varchar, 
	PAN integer, 
	PRI integer, 
	PRD integer, 
	PVEM integer, 
	PT integer, 
	MOVIMIENTO_CIUDADANO integer, 
	NUEVA_ALIANZA integer, 
	MORENA integer, 
	ENCUENTRO_SOCIAL integer, 
	PAN_PRD_MC integer, 
	PAN_PRD integer, 
	PAN_MC integer, 
	PRD_MC integer, 
	PRI_PVEM_NA integer, 
	PRI_PVEM integer, 
	PRI_NA integer, 
	PVEM_NA integer, 
	PT_MORENA_PES integer, 
	PT_MORENA integer, 
	PT_PES integer, 
	MORENA_PES integer, 
	CAND_IND_01 integer, 
	CAND_IND_02 integer, 
	CNR varchar, 
	VN integer, 
	TOTAL_VOTOS_CALCULADOS integer, 
	LISTA_NOMINAL_CASILLA varchar, 
	OBSERVACIONES varchar, 
	MECANISMOS_TRASLADO varchar, 
	FECHA_HORA varchar
);
        """,
        """
        CREATE TABLE senadurias_votos(
	CLAVE_CASILLA varchar, 
	CLAVE_ACTA varchar PRIMARY KEY,
	ID_ESTADO integer, 
    	FOREIGN KEY (ID_ESTADO)
        REFERENCES candidatos (ID)
        ON UPDATE CASCADE ON DELETE CASCADE,
	NOMBRE_ESTADO varchar, 
	ID_DISTRITO integer, 
	NOMBRE_DISTRITO varchar, 
	SECCION integer, 
	ID_CASILLA varchar, 
	TIPO_CASILLA varchar, 
	EXT_CONTIGUA varchar, 
	CASILLA varchar, 
	NUM_ACTA_IMPRESO varchar, 
	PAN integer, 
	PRI integer, 
	PRD integer, 
	PVEM integer, 
	PT integer, 
	MOVIMIENTO_CIUDADANO integer, 
	NUEVA_ALIANZA integer, 
	MORENA integer, 
	ENCUENTRO_SOCIAL integer, 
	PAN_PRD_MC integer, 
	PAN_PRD integer, 
	PAN_MC integer, 
	PRD_MC integer, 
	PRI_PVEM_NA integer, 
	PRI_PVEM integer, 
	PRI_NA integer, 
	PVEM_NA integer, 
	PT_MORENA_PES integer, 
	PT_MORENA integer, 
	PT_PES integer, 
	MORENA_PES integer, 
	CAND_IND_01 integer, 
	CAND_IND_02 integer, 
	CNR varchar, 
	VN integer, 
	TOTAL_VOTOS_CALCULADOS integer, 
	LISTA_NOMINAL_CASILLA varchar, 
	OBSERVACIONES varchar, 
	MECANISMOS_TRASLADO varchar, 
	FECHA_HORA varchar
);
        """)
    delete_tables= (
            """
            DROP TABLE diputaciones_votos;
            """,
            """
            DROP TABLE presidencia_votos;
            """,
            """
            DROP TABLE senadurias_votos;
            """,
            """
            DROP TABLE candidatos;
            """
            
            
            )
    conn = None
    try:
        # read the connection parameters
        params = config()
        
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
	
		# create or delete table one by one
        #for command in delete_tables:

        for command in tables: 
            cur.execute(command)
                    
        # close communication with the PostgreSQL database server
        cur.close()
        
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
 
if __name__ == '__main__':
    create_tables()
    