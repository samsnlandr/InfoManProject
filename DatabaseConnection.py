import mysql.connector
from config import dbconnect


# TODO
#  implement the Card_No_of_Dependents derive
#  implement insert supplementary
#  implement the fetching of Work_ID primary key
#           I imagine it to work like:
                #-After filling out the primary card infos, we store the things in a temp tuple,
                #-We proceed into filling out the Work information, after filling out the Work Info,
                #-Proceed to submit button that inserts work info to the database table
                #-Fetch the work_ID primary key
                #-Insert the Work_ID into the temp tuple
                #-Place the temp tuple as argument for the insert primary owner
                #-commit

database = dbconnect()

def insertprimaryowner(values):

    mycursor = database.cursor()

    sqlcommand = ("INSERT INTO primary_card (Card_Name, Card_Birthdate, Card_Place_of_Birth, Card_Sex, Card_Display_Name,"
                  "Card_Mother_Maiden_Name, Card_Educational_Attainment, Card_Civil_status, Card_No_of_Dependents,"
                  "Card_TIN, Card_SSS_GSIS, Card_Car_Ownership, Card_Citizenship, Card_Mobile_Number,"
                  "Card_Home_Phone_Number, Card_Address, Card_Zip_code, Card_Email, Card_Preferred_Card_Delivery,"
                  "Card_Basic_Monthly_Income, Work_ID)"
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")


    try:
        print(f"inserted income: {values[19]}{type(values[19])}")
        print(f"inserted email: {values[17]}{type(values[17])}")
        mycursor.execute(sqlcommand, values)

        database.commit()
        rcount = mycursor.rowcount
        lrid = mycursor.lastrowid
        successline = f"Insert to primary_card successful!\n Rows affected: {rcount}\nInserted ID:{lrid} "
        return successline, lrid


    except mysql.connector.Error as err:
        database.rollback()
        return f"Error Occurred:{err}\n"


def insertwork(values):

    mycursor = database.cursor()

    sqlcommand = ("INSERT INTO work"
                  "(Work_Employment_Type, Work_Employer_Name, Work_Business_Address, Work_Nature_of_Business,"
                  "Work_Business_Phone_Number, Work_Years_With_Present_Employer, Work_Position, Work_Zip_Code,"
                  "Work_Email_Address, Work_Previous_Employer)"
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

    try:
        mycursor.execute(sqlcommand, values)

        database.commit()

        rcount = mycursor.rowcount
        lrid = mycursor.lastrowid
        successline = f"Insert to work successful! \nRows affected: {rcount}\nInserted ID:{lrid}"

        return successline , lrid

    except mysql.connector.Error as err:
        database.rollback()
        return f"Error Occurred: {err}"

def insertsupplementary(values, execount):
    mycursor = database.cursor()

    sqlcommand = ("INSERT INTO supplementary"
                  "(SC_Name, SC_Birthday, SC_Place_of_Birth, SC_Sex, SC_Civil_Status,"
                  "SC_Citizenship, SC_Address, SC_Zip_Code, SC_Home_Phone_Number,"
                  "SC_Mobile_Number, SC_Email_Address, SC_Employer_Business_Name,"
                  "SC_Employer_Business_Address, SC_Source_of_Funds, SC_Nature_of_Business_Industry,"
                  "SC_Business_Number, SC_Relationship_to_Principal_Cardholder, Primary_Card_ID)"
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

    try:
        mycursor.execute(sqlcommand, values)

        database.commit()

        rcount = mycursor.rowcount
        lrid = mycursor.lastrowid
        successline = f"Insert to supplementary_{execount} successful! \nRows affected: {rcount}\nInserted ID:{lrid}"

        return successline, lrid

    except mysql.connector.Error as err:
        database.rollback()
        return f"Error Occurred: {err}"

def fetch_primarytable():
    mycursor = database.cursor()
    selectall = "SELECT * FROM primary_card"

    mycursor.execute(selectall)

    rows = mycursor.fetchall()
    columns = [i[0] for i in mycursor.description]

    return columns, rows

def fetch_work():
    mycursor = database.cursor()
    selectall = "SELECT * FROM work"

    mycursor.execute(selectall)

    rows = mycursor.fetchall()
    columns = [i[0] for i in mycursor.description]

    return columns, rows

def fetch_supplementary():
    mycursor = database.cursor()
    selectall = "SELECT * FROM supplementary"

    mycursor.execute(selectall)

    rows = mycursor.fetchall()
    columns = [i[0] for i in mycursor.description]

    return columns, rows

def fetch_line_primary(row_id):
    mycursor = database.cursor()
    selectall = "SELECT * FROM primary_card WHERE Card_ID = %s"

    mycursor.execute(selectall,(row_id,))

    rows = mycursor.fetchall()
    columns = [i[0] for i in mycursor.description]

    return columns, rows


def fetch_line_work(row_id):
    mycursor = database.cursor()
    selectall = "SELECT * FROM work WHERE Work_ID = %s"

    mycursor.execute(selectall, (row_id,))

    rows = mycursor.fetchall()
    columns = [i[0] for i in mycursor.description]

    return columns, rows


def fetch_line_supplementary(row_id):
    mycursor = database.cursor()
    selectall = "SELECT * FROM supplementary WHERE Supplementary_Cardholder_No = %s"

    mycursor.execute(selectall, (row_id,))

    rows = mycursor.fetchall()
    columns = [i[0] for i in mycursor.description]

    return columns, rows