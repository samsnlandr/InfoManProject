import mysql.connector
from config import dbconnect

# TODO
#  implement the Card_No_of_Dependents derive
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

def insertprimaryowner(Card_Name, Card_Birthdate, Card_Place_of_Birth, Card_Sex, Card_Display_Name,
                       Card_Mother_Maiden_Name, Card_Educational_Attainment, Card_Civil_status, Card_No_of_Dependents,
                       Card_TIN, Card_SSS_GSIS,Card_Car_Ownership, Card_Citizenship, Card_Mobile_Number,
                       Card_Home_Phone_Number, Card_Address, Card_Zip_code, Card_Email, Card_Preffered_Card_Delivery,
                       Card_Basic_Monthly_Income, Work_ID):

    mycursor = database.cursor()

    sqlcommand = ("INSERT INTO primary_card (Card_Name, Card_Birthdate, Card_Place_of_Birth, Card_Sex, Card_Display_Name,"
                  "Card_Mother_Maiden_Name, Card_Educational_Attainment, Card_Civil_status, Card_No_of_Dependents,)"
                  "Card_TIN, Card_SSS_GSIS,Card_Car_Ownership, Card_Citizenship, Card_Mobile_Number,"
                  "Card_Home_Phone_Number, Card_Address, Card_Zip_code, Card_Email, Card_Preffered_Card_Delivery,"
                  "Card_Basic_Monthly_Income, Work_ID)"
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s")
    values = (Card_Name, Card_Birthdate, Card_Place_of_Birth, Card_Sex, Card_Display_Name,
              Card_Mother_Maiden_Name, Card_Educational_Attainment, Card_Civil_status, Card_No_of_Dependents,
              Card_TIN, Card_SSS_GSIS,Card_Car_Ownership, Card_Citizenship, Card_Mobile_Number,
              Card_Home_Phone_Number, Card_Address, Card_Zip_code, Card_Email, Card_Preffered_Card_Delivery,
              Card_Basic_Monthly_Income, Work_ID)

    try:
        mycursor.execute(sqlcommand, values)

        database.commit()
        print("✅ Insert to primary_card successful!")
        print("Rows affected:", mycursor.rowcount)
        print("Inserted ID:", mycursor.lastrowid)

    except mysql.connector.Error as err:
        print("Error Occured: ", err)
        database.rollback()

    finally:
        mycursor.close()
        database.close()

def insertwork(Work_Employment_Type, Work_Employer_Name, Work_Business_Address, Work_Nature_of_Business,
               Work_Business_Phone_Number, Work_Years_With_Present_Employer, Work_Position, Work_Zip_Code,
               Work_Email_Address, Work_Previous_Employer):
    mycursor = database.cursor()

    sqlcommand = ("INSERT INTO work"
                  "(Work_Employment_Type, Work_Employer_Name, Work_Business_Address, Work_Nature_of_Business,"
                  "Work_Business_Phone_Number, Work_Years_With_Present_Employer, Work_Position, Work_Zip_Code,"
                  "Work_Email_Address, Work_Previous_Employer)"
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s")
    values =  (Work_Employment_Type, Work_Employer_Name, Work_Business_Address, Work_Nature_of_Business,
               Work_Business_Phone_Number, Work_Years_With_Present_Employer, Work_Position, Work_Zip_Code,
               Work_Email_Address, Work_Previous_Employer)

    try:
        mycursor.execute(sqlcommand, values)

        database.commit()
        print("✅ Insert to work successful!")
        print("Rows affected:", mycursor.rowcount)
        print("Inserted ID:", mycursor.lastrowid)

    except mysql.connector.Error as err:
        print("Error Occured: ", err)
        database.rollback()

    finally:
        mycursor.close()
        database.close()

