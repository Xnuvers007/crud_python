#/usr/bin/env python3
#!/usr/bin/python3
#/usr/bin/python3
#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
# See
# https://github.com/Xnuvers007
# Author: Xnuvers007
# License: GNU, see LICENSE
# Country: Indonesia
# =================================================================



# Making Crud for beginner
import sys
from sys import platform # import library sys and os

# check python version
import os

if not sys.version_info.major==3 and sys.version_info.minor >= 6:
    print("you need to upgrade your python version to up > 3.6") # Attention
    os.system("xdg-open https://python.org/download") # If you use python < 3.6 you need to download it
    sys.exit(1) # exit if you not use python > 3.6 

# try to import module
try:
    import mysql.connector
except (ImportError,ModuleNotFoundError): # if you get error why that module cannot import/module not found
    sys.setrecursionlimit(5000) # set recursion limit to 5000
    sys.getrecursionlimit() # get value recursion
    if platform=="linux" or platform=="linux2": # check your operating system, you are using linux
        os.system("sudo pip3 install mysql-connector-python") # system will execute command 
    elif platform=="darwin": # you are using Mac OS X (10.4, 10.5, etc.)
        os.system("pip3 install mysql-connector-python") # system will execute command
    elif platform=="win32": # You Are using Windows
        os.system("pip3 install mysql-connector-python") # system operation will execute this command
    elif platform=="cygwin": # you are using windows/Cygwin
        os.system("pip3 install mysql-connector-python") # system operation will execute this command
    elif platform=="aix": # You Are using operation system AIX
        os.system("pip3 install mysql-connector-python") # System will execute this command

    else: # if device cannot detect
        print("Cannot Detect This device")
        os.system("sudo pip3 install mysql-connector-python||pip3 install mysql-connector-python||pip install mysql-connector-python||python3 -m pip install mysql-connector-python")

# Create connection to databases mysql
# create connection if database already exist
try:
    koneksi = mysql.connector.connect(
        host="localhost",
        user="root",
        password="", # fill with your password databases
        database="db_crud_python"
    )
    # print(koneksi)
    mycursor = koneksi.cursor()
except: # Create connection if database not exist
    koneksi = mysql.connector.connect(
        host="localhost",
        user="root",
        password="" # fill with your password databases
    )
    # print(koneksi)
    mycursor = koneksi.cursor()


# if databases not found, create databases and tables
try:
    mycursor.execute("create database db_crud_python") # create database with name db_crud_python
    databases = mycursor.execute("show databases") # Show databases
    for x in databases:
        print(x) # Show all list databases
    sql = """
        CREATE TABLE user (
        id int(15) NOT NULL AUTO_INCREMENT,
        nama varchar(255) NOT NULL,
        alamat varchar(255) NOT NULL,
        email varchar(255) NOT NULL,
        telepon varchar(25) NOT NULL,
        PRIMARY KEY (id)
        )
        """ # id int(11) NOT NULL, AUTO_INCREMENT
    mycursor.execute(sql) # execute command from sql
    print("Table user created successfully") # Attention

except:
    #if database already exist, create tables
    print("Database Already Exists")
    try:
        sql = """
        CREATE TABLE user (
        id int(15) NOT NULL AUTO_INCREMENT,
        nama varchar(255) NOT NULL,
        alamat varchar(255) NOT NULL,
        email varchar(255) NOT NULL,
        telepon varchar(25) NOT NULL,
        PRIMARY KEY (id)
        )
        """ # id int(11) NOT NULL, AUTO_INCREMENT
        mycursor.execute(sql) # execute command from sql
        print("Table user created successfully") # Attention
    except:
        print("Table user already exists")
        pass

usernm = os.getlogin() # get login user

lanjut =  True # boolean true for while
while lanjut: # do looping
    # Create list
    print("====="*5)
    print("Welcome to Databases {}".format(usernm))
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")
    print("====="*5)
    # select option
    pilih = int(input("Pilih Menu : "))
    # if you choose 1, then create
    if pilih == 1:
        nama = input("Name : ") # input name
        alamat = input("Address : ") # input address
        telepon = int(input("Telephone : ")) # input telephone number
        email = input("Email : ") # input email address
        sql = "insert into user (nama,alamat,telepon,email) values (%s,%s,%s,%s)" # command for mysql
        val = (nama,alamat,telepon,email) # fill %s
        mycursor.execute(sql,val) # execute command from sql
        koneksi.commit() # commit to databases
        print(mycursor.rowcount, "Data successfully added") # Attention
    # if you choose 2, then read
    elif pilih == 2:
        mycursor.execute("select * from user") #  execute command from sql
        myresult = mycursor.fetchall() # fetch all data from databases
        print("======="*2)
        print("(ID, Name, Address, Email Address, Telephone Number)") # Attention
        for x in myresult:
            print(x) # print all data from databases
    # if you choose 3, then update
    elif pilih == 3:
        id = int(input("ID : ")) # input id
        query = "select * from user where id = %s limit 1" # command for mysql
        mycursor.execute(query,(id,)) # execute command from sql
        result = mycursor.fetchall() # fetch all data from databases
        user = None # set user to None
        for x in result:
            user = x # set user to x
        if (user != None): # if user is not None
            nama = input("Nama ("+str(user[1])+") : ") # input name
            alamat = input("Address ("+str(user[2])+") : ") # input address
            telepon = int(input("Telephone ("+str(user[4])+") : ")) # input telephone number
            email = input("Email ("+str(user[3])+") : ") # input email address
            sql = "update user set nama = %s, alamat = %s, telepon = %s, email = %s where id = %s" # command for mysql
            val = (nama,alamat,telepon,email,id) # fill %s
            mycursor.execute(sql,val) # execute command from sql
            koneksi.commit() # commit to databases
            print(mycursor.rowcount, "Data Successfully Updated") # Attention
        else: # if user is None
            print("Data tidak ditemukan") # Attention
    # if you choose 4, then delete
    elif pilih == 4:
        id = int(input("ID : ")) # input id
        query = "select * from user where id = %s limit 1" # command for mysql
        mycursor.execute(query,(id,)) # execute command from sql
        result = mycursor.fetchall() # fetch all data from databases
        user = None # set user to None
        for x in result:
            user = x # set user to x
        if (user != None): # if user is not None
            print("Erasing Data : ", user) # Attention for erasing data
            sql = "delete from user where id = %s" # command for mysql
            val = (id,) # fill %s
            mycursor.execute(sql,val) # execute command from sql
            koneksi.commit() # commit to databases
            print(mycursor.rowcount, "Data Successfully Deleted") # Attention
        else: # if user is None
            print("Data tidak ditemukan") # Attention
    # if you choose 5, then exit
    elif pilih == 5:
        lanjut = False # boolean false for while
        print("Terima Kasih")
        for i in range(1,4):
            i += 0 # for looping
            print(i) # print for looping
        exit(code=None) # exit program
        pass # pass for while
    # if you choose other, then print error
    else:
        print("Pilih Menu 1-5")
    print("====="*5)
    print("")
    print("")
    
    lanjut = str(input("Lanjutkan (y/n) : ")) # input lanjutkan/continue
    if (lanjut == "y" or lanjut == "Y"): # if lanjutkan/continue is y or Y
        lanjut = True # boolean true for while
    elif (lanjut == "n" or lanjut == "N"): # if lanjutkan/continue is n or N
        lanjut = False # exit program
    else:
        print("invalid")
        exit(code=None) # exit program
