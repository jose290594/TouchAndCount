import os
import sqlite3
import time
import datetime
global conndb1
global db_file
global sqlite3
global os
global time
global datetime
global passtodo
global pasmas
global conndb1
db_file=r"cuentas.sqlite3"
conndb1 = sqlite3.connect(db_file)
#print(sqlite3.version)
##os("clear")
optiontodo=str("0")
sql_create_ingresos_table = """ CREATE TABLE IF NOT EXISTS ingresos (
                                        monto real NOT NULL,
                                        concepto text NOT NULL,
                                        registrador text,
                                        fecha text
                                    ); """
sql_create_egresos_table = """ CREATE TABLE IF NOT EXISTS egresos (
                                        monto real NOT NULL,
                                        concepto text NOT NULL,
                                        registrador text,
                                        fecha text
                                    ); """
sql_create_users1_table = """ CREATE TABLE IF NOT EXISTS users1(
                                        usuario text NOT NULL,
                                        pin text NOT NULL
                                        
                                    ); """
sql_create_users2_table = """ CREATE TABLE IF NOT EXISTS users2(
                                        usuario text NOT NULL,
                                        pin text NOT NULL
                                        
                                    ); """

cc1 = conndb1.cursor()
cc1.execute(sql_create_ingresos_table)
conndb1.commit()
cc2 = conndb1.cursor()
cc2.execute(sql_create_egresos_table)
conndb1.commit()
cc3 = conndb1.cursor()
cc3.execute("SELECT usuario FROM users1")
UserList1 = cc3.fetchall()
ccpas=conndb1.cursor()
ccpas.execute("SELECT pin FROM users1")
PassList1=ccpas.fetchall()
#print(PassList1)
cc4 = conndb1.cursor()
cc4.execute(sql_create_users1_table)
conndb1.commit()
cc5 = conndb1.cursor()
cc5.execute(sql_create_users2_table)
conndb1.commit()
ccmas = conndb1.cursor()
ccmas.execute(""" SELECT pin FROM users1 
WHERE usuario = 'master' """)
pasmas1=ccmas.fetchall()
pasmas2=pasmas1[0]
pasmas=pasmas2[0]

#print(pasmas)
#pasmas2=TotIngdes1[0]
#TotIng = float(TotIngBrut[0])

#conndb1
def AddUsrDB(UserToPut, PassToPut):
    cc4 = conndb1.cursor()
    cc4.execute(''' INSERT INTO users1 (usuario,pin)
                VALUES('''+"'"+str(UserToPut)+"'"+''','''+"'"+str(PassToPut)+"'"+''')'''
                )


def maaiin(optiontodo):
    while optiontodo == str("0"):
        os.system('clear')
        optiontodo=input("""

                    ******** Bienvenido a Touch And Count ********
                        
                        :tipee una opcion y presione Enter:
                        
                1.-)Declarar Ingreso
                
                2.-)Declarar Egreso
                
                3.-)Cierre del dia

                4.-)Añadir usuario
                
                

                                                hecho por: Touch And Shop
                                        
                        :  """)
        os.system('clear')
        #UserList1=["jaqui", "jessi", "juan", "hernan", "andres"]
        #PassList1=["1990","1991","1992","1993","1994"]

        def PutIng(optiontodo):
                #os.system('clear')
                
                print("""         ++++++Declaracion de Ingreso++++++
                
                """)
                usertodo1=input("""escriba el usuario quien registra la operacion:
                
                :  """)
                cclog1=conndb1.cursor()
                cclog1.execute(""" SELECT pin FROM users1 
                WHERE usuario = """+"'"+str(usertodo1)+"'")
                passtodo1=cclog1.fetchall()
                passtodo2=passtodo1[0]
                passtodo3=passtodo2[0]
                passtodo=input("""escriba su contraseña """+str(usertodo1)+""" :
                
                :  """)
                os.system('clear')
                while str(passtodo) == str(passtodo3):
                    ingmont1=input("""monto ingresado:
                    
                    : """)
                    ingconc1=input("""concepto del ingreso:
                    
                    : """)

                    if (usertodo1 or ingmont1) == str("salir"):
                        optiontodo=str("0")

                    fech1=datetime.datetime.now()
                    
                    sqlsend1 = ''' INSERT INTO ingresos (monto,concepto,registrador,fecha)
                    VALUES('''+"'"+str(ingmont1)+"'"+''','''+"'"+str(ingconc1)+"'"+''','''+"'"+str(usertodo1)+"'"+''','''+"'"+str(fech1)+"'"+''')'''
                    os.system('clear')
                    print(sqlsend1)
                    time.sleep(2)
                    conndb2=sqlite3.connect('cuentas.sqlite3')
                    cc3=conndb2.cursor()
                    cc3.execute(str(sqlsend1))
                    conndb2.commit()
                    print("             //Ingreso guardado, por favor espere...//")
                    time.sleep(1)
                    print("1...")
                    time.sleep(1)
                    print("2...")
                    time.sleep(1)
                    
                    optiontodo=str("0")
                    return maaiin(optiontodo)

                else:
                    print("contraseña incorrecta")
                    return PutIng(optiontodo)
                if usertodo1 or ingmont1== str("salir"):
                    optiontodo=str("0")
                    return maaiin(optiontodo)
                

        while optiontodo == str("1") or str("2") or str("3"):

            #os.system('clear')
            if optiontodo == str("1"):
                #os.system('clear')
                
                print("""         ++++++Declaracion de Ingreso++++++
                
                """)
                usertodo1=input("""escriba el usuario quien registra la operacion:
                
                :  """)
                cclog1=conndb1.cursor()
                cclog1.execute(""" SELECT pin FROM users2 
                WHERE usuario = """+"'"+str(usertodo1)+"'")
                passtodo1=cclog1.fetchall()
                passtodo2=passtodo1[0]
                passtodo3=passtodo2[0]
                passtodo=input("""escriba su contraseña """+str(usertodo1)+""" :
                
                :  """)
                os.system('clear')
                if str(passtodo) == str(passtodo3):
                    ingmont1=input("""monto ingresado:
                    
                    : """)
                    ingconc1=input("""concepto del ingreso:
                    
                    : """)

                    if (usertodo1 or ingmont1) == str("salir"):
                        optiontodo=str("0")

                    fech1=datetime.datetime.now()
                    
                    sqlsend1 = ''' INSERT INTO ingresos (monto,concepto,registrador,fecha)
                    VALUES('''+"'"+str(ingmont1)+"'"+''','''+"'"+str(ingconc1)+"'"+''','''+"'"+str(usertodo1)+"'"+''','''+"'"+str(fech1)+"'"+''')'''
                    os.system('clear')
                    print(sqlsend1)
                    time.sleep(2)
                    conndb2=sqlite3.connect('cuentas.sqlite3')
                    cc3=conndb2.cursor()
                    cc3.execute(str(sqlsend1))
                    conndb2.commit()
                    print("             //Ingreso guardado, por favor espere...//")
                    time.sleep(1)
                    print("1...")
                    time.sleep(1)
                    print("2...")
                    time.sleep(1)
                    passtodo=str("null")
                    os.system('clear')
                    optiontodo=str("0")
                    return maaiin(optiontodo)

                else:
                    print("contraseña incorrecta")
                if usertodo1 or ingmont1== str("salir"):
                    optiontodo=str("0")
                    return maaiin(optiontodo)
                
            


            if optiontodo == str("2"):
                os.system('clear')
                print("""         ------Declaracion de Egreso------
                
                """)
                usertodo4=input("""escriba el usuario quien registra la operacion:
                
                :  """)

                cclog4=conndb1.cursor()
                cclog4.execute(""" SELECT pin FROM users2 
                WHERE usuario = """+"'"+str(usertodo4)+"'")
                passtodo4=cclog4.fetchall()
                passtodo5=passtodo4[0]
                passtodo6=passtodo5[0]
                passtodo7=input("""escriba su contraseña """+str(usertodo4)+""" :
                
                :  """)
                os.system('clear')
                if str(passtodo7) == str(passtodo6):
                    egrmont1=input("""monto egresado:
                    
                    : """)
                    egrconc1=input("""concepto del egreso:
                    
                    : """)
                    if (usertodo4 or egrmont1 or passtodo) == str("salir"):
                        optiontodo=str("0")
                        return maaiin(optiontodo)
                    fech1=datetime.datetime.now()
                    
                    sqlsend2 = ''' INSERT INTO egresos (monto,concepto,registrador,fecha)
                    VALUES('''+"'"+str(egrmont1)+"'"+''','''+"'"+str(egrconc1)+"'"+''','''+"'"+str(usertodo4)+"'"+''','''+"'"+str(fech1)+"'"+''')'''
                    os.system('clear')
                    print(sqlsend2)
                    time.sleep(2)
                    #conndb2=sqlite3.connect('cuentas.sqlite3')
                    cc3=conndb1.cursor()
                    cc3.execute(sqlsend2)
                    conndb1.commit()
                    print("             //Egreso guardado, por favor espere...//")
                    time.sleep(1)
                    print("1...")
                    time.sleep(1)
                    print("2...")
                    time.sleep(1)
                    passtodo=str("null")
                    os.system('clear')
                    optiontodo=str("0")
                    return maaiin(optiontodo)
                else:
                    print("contraseña incorrecta...")
                    passtodo=str("null")
                    optiontodo=str("0")
                    return maaiin(optiontodo)
                if usertodo1 or ingmont1== str("salir"):
                    passtodo=str("null")
                    optiontodo=str("0")
                    return maaiin(optiontodo)   

            if optiontodo == str(3):
                os.system("clear")
                print("Generando archivo de cierre, por favor espere...")
                ccclo = conndb1.cursor()
                ccclo.execute("SELECT SUM(monto) FROM ingresos")
                TotIngdes1=ccclo.fetchall()
                TotIngBrut=TotIngdes1[0]
                TotIng = float(TotIngBrut[0])
                print(TotIng)
                ccclo2 = conndb1.cursor()
                ccclo2.execute("SELECT SUM(monto) FROM egresos")
                TotEgrdes1=ccclo2.fetchall()
                TotEgrBrut=TotEgrdes1[0]
                TotEgr = float(TotEgrBrut[0])
                print(TotEgr)
                BalFin1 = float(TotIng - TotEgr)
                print(BalFin1)
                os.system("clear")
                print("Total ingresado: "+str(TotIng))
                print("Total egresado: "+str(TotEgr))
                print("El Balance final es de $"+str(BalFin1))
                puttodata ="""

                """+"al "+str(datetime.datetime.now())+"""
                """+str("Total ingresado: "+str(TotIng))+"""
                """+str("Total egresado: "+str(TotEgr))+"""
                """+str("El Balance final es de $"+str(BalFin1))
                histodata = open(r"historico.txt","a")
                histodata.write(puttodata)
                histodata.close()
                time.sleep(8)
                print("Redirigiendo al inicio...")
                time.sleep(1)
                print("1...")
                time.sleep(1)
                print("2...")
                time.sleep(1)
                os.system('clear')
                optiontodo=str("0")
                    
                return maaiin(optiontodo)

            if optiontodo == str("4"):
                
            
                passtodo7=input("""escriba su contraseña, Master:
                
                :  """)
                os.system("clear")

                if str(passtodo7) == str(pasmas):

                    NewUSRdb=input("""escriba el usuario a registrar:
                    
                    :  """)
                    NewPSSdb=input("""escriba su contraseña nueva para """+str(NewUSRdb)+""" :
                    
                    :  """)
                    print(NewPSSdb)
                    print(NewUSRdb)

                    sqlsend7 = ''' INSERT INTO users2 (usuario,pin)
                        VALUES('''+"'"+str(NewUSRdb)+"'"+''','''+"'"+str(NewPSSdb)+"'"+")"
                    print(sqlsend7)
                    cc41=conndb1.cursor()
                    cc41.execute(str(sqlsend7))
                    conndb1.commit()
                    
                    print("             //Usuario nuevo guardado, por favor espere...//") 
                    time.sleep(3)   
                os.system('clear')
                optiontodo=str("0")
                    
                return maaiin(optiontodo)




    return maaiin(optiontodo)
maaiin(optiontodo)


            #TotIng=sum(TotIngdes)
            #print(TotIng)

      #  if optiontodo == int(4):


        #if optiontodo != int(1) and int(2) and int(3):
        #   print("""Opcion desconocida.
        #  Elija una opcion valida...""")
        # print(optiontodo)