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

def updateprimary(values, row_id):
    mycursor = database.cursor()
    command = ("UPDATE primary_card SET "
               "Card_Name = %s,"
               "Card_Birthdate = %s,"
               "Card_Place_of_Birth = %s,"
               "Card_Sex = %s,"
               "Card_Display_Name = %s,"
               "Card_Mother_Maiden_Name = %s,"
               "Card_Educational_Attainment = %s,"
               "Card_Civil_Status = %s,"
               "Card_No_of_Dependents = %s,"
               "Card_TIN = %s,"
               "Card_SSS_GSIS = %s,"
               "Card_Car_Ownership = %s,"
               "Card_Citizenship = %s,"
               "Card_Mobile_Number = %s,"
               "Card_Home_Phone_Number = %s,"
               "Card_Address = %s,"
               "Card_Zip_Code = %s,"
               "Card_Email = %s,"
               "Card_Preferred_Card_Delivery = %s,"
               "Card_Basic_Monthly_Income = %s,"
               "Work_ID = %s "
               "WHERE Card_ID = %s")

    values.append(row_id)
    mycursor.execute(command, values)

    database.commit()

    successalert = f"Update to primary table successful!"

    return successalert

def updatework(values, row_id):
    mycursor = database.cursor()
    command = ("UPDATE work SET "
               "Work_Employment_Type = %s,"
               "Work_Employer_Name = %s,"
               "Work_Business_Address = %s,"
               "Work_Nature_of_Business =%s,"
               "Work_Business_Phone_Number = %s,"
               "Work_Years_With_Present_Employer = %s,"
               "Work_Position = %s,"
               "Work_Zip_Code = %s,"
               "Work_Email_Address = %s,"
               "Work_Previous_Employer = %s "
               "WHERE Work_ID = %s")

    values.append(row_id)
    mycursor.execute(command, values)

    database.commit()

    successalert = f"Update to work table successful!"

    return successalert

def updatesupplementary(values, row_id):
    mycursor = database.cursor()
    command = ("UPDATE supplementary SET "
               "SC_Name = %s,"
               "SC_Birthday = %s,"
               "SC_Place_of_Birth = %s,"
               "SC_Sex = %s,"
               "SC_Civil_Status =%s,"
               "SC_Citizenship = %s,"
               "SC_Address = %s,"
               "SC_Zip_Code = %s,"
               "SC_Home_Phone_Number = %s,"
               "SC_Mobile_Number = %s,"
               "SC_Email_Address = %s,"
               "SC_Employer_Business_Name = %s,"
               "SC_Employer_Business_Address = %s,"
               "SC_Source_of_Funds = %s,"
               "SC_Nature_of_Business_Industry = %s,"
               "SC_Business_Number = %s,"
               "SC_Relationship_to_Principal_Cardholder = %s,"
               "Primary_Card_ID = %s "
               "WHERE Supplementary_Cardholder_No = %s")

    values.append(row_id)
    mycursor.execute(command, values)

    database.commit()

    successalert = f"Update to supplementary table successful!"

    return successalert

def deletePrimaryandChildren(row_id):
    mycursor = database.cursor()
    selectworkcommand = "SELECT Work_ID FROM primary_card WHERE Card_ID = %s;"
    mycursor.execute(selectworkcommand, (row_id,))

    work_id = mycursor.fetchone()

    deletesupp = "DELETE FROM supplementary Where Primary_Card_ID = %s; "
    deleteprimary = "DELETE FROM primary_card WHERE Card_ID = %s; "
    deletework = "DELETE FROM work WHERE Work_ID = %s;"
    mycursor.execute(deletesupp,(row_id, ))
    mycursor.execute(deleteprimary, (row_id,))
    mycursor.execute(deletework, work_id)

    database.commit()

    successalert = f"Deletion from primary_card table, work table, and supplementary table successful"

    return successalert

def deletesupplementary(row_id):
    mycursor = database.cursor()

    selectcommand = "SELECT Primary_Card_ID FROM supplementary WHERE Supplementary_Cardholder_No = %s "
    mycursor.execute(selectcommand, (row_id, ))
    primary_card_id = mycursor.fetchone()[0]
    print(f"Selected Primary ID: {primary_card_id} ")

    deletecommand = "DELETE FROM supplementary WHERE Supplementary_Cardholder_No = %s; "
    mycursor.execute(deletecommand, (row_id, ))
    print(f"ID to be deleted: {row_id}")

    count_no_of_dependents_command = "SELECT COUNT(*) AS NumberOfDependents FROM supplementary WHERE Primary_Card_ID = %s; "
    mycursor.execute(count_no_of_dependents_command, (primary_card_id, ))
    count = int(mycursor.fetchone()[0])
    print(f"Updated Count of Dependents: {count}")

    updatecommand = "UPDATE primary_card SET Card_No_of_Dependents = %s WHERE Card_ID = %s; "
    mycursor.execute(updatecommand, (count, primary_card_id, ))

    successline = f"Sucessfully Updated Dependent Count and Deleted Supplementary!"

    database.commit()

    return successline


