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
        return f"✅ Insert to primary_card successful!\n Rows affected: {rcount}\nInserted ID:{lrid}", lrid


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

        return f"✅ Insert to work successful! \nRows affected: {rcount}\nInserted ID:{lrid} ", lrid


    except mysql.connector.Error as err:
        database.rollback()
        return f"Error Occurred: {err}"


