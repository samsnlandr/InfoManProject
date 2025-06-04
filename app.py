from flask import Flask, redirect, url_for, render_template, request
from DatabaseConnection import insertprimaryowner, insertwork
from decimal import Decimal

#TODO /Submit Route form.gets
app = Flask(__name__)
primary_owner_values = [] #List that contains the infos for primary owner table in SQL
about_work_values = [] #List that contains the infos for work table in SQL
preferred_card_delivery = None #Variable to fetch from different page
basic_monthly_income_global = None




@app.route("/")
def home():
    return redirect(url_for("fill_out_forms"))

@app.route("/Card_Holder_Application_Form")
def fill_out_forms():
    return render_template("index.html")

@app.route("/submitprimaryowner", methods = ["POST", "GET"])
def submitprimaryowner():
    if request.method == "POST":

        # Get Name & Display name
        if request.form.get("middleName") == "N/A":
            name = request.form.get("firstName") + request.form.get("surname")
            displayname = name
        else:
            name = request.form.get("firstName") +" "+ request.form.get("middleName") +" "+ request.form.get("surname")
            displayname = request.form.get("firstName") +" "+ request.form.get("middleName")[0] +" "+ request.form.get("surname")

        # Get birthdate
        birthdate = request.form.get("birthdate")

        # Get placeofbirth
        placeofbirth = request.form.get("placeofbirth")

        # Get sex
        sex = request.form.get("sex")
        if sex == "male":
            sex = "M"
        elif sex == "female":
            sex = "F"

        # Get mothermaidenname
        mothermaidenname = request.form.get("mothermaidenname")

        # Get educationalattainment
        educationalattainment = request.form.get("educationalattainment")

        # Get noofdependents
        noofdependents = 0 # TODO Here is temporary values. fetch from supplementary count

        # Get civilstatus
        civilstatus = request.form.get("civilstatus")
        if civilstatus == "single":
            civilstatus = "S"
        elif civilstatus == "married":
            civilstatus = "M"
        elif civilstatus == "divorced":
            civilstatus = "D"
        elif civilstatus == "Widowed":
            civilstatus = "W"

        # Get tinnumber
        tinnumber = request.form.get("tinnumber")
        if tinnumber == "N/A":
            tinnumber = None

        # Get sssgsis
        sssgsis = request.form.get("sssgsis")
        if sssgsis == "N/A":
            sssgsis = None

        # Get carownership
        carownership = request.form.get("carownership")
        if carownership == "Owned":
            carownership = "O"
        elif carownership == "Mortgaged":
            carownership = "M"
        elif carownership == "None":
            carownership = "N"

        # Get citizenship
        if request.form.get("citizenship") == "non-filipino":
            citizenship = request.form.get("othercitizenship")
        else:
            citizenship = "filipino"

        # Get mobilenumber
        mobilenumber = request.form.get("mobilenumber")

        # Get homephonenumber
        homephonenumber = request.form.get("homephonenumber")

        # Get homeaddress
        homeaddress = request.form.get("homeaddress")

        # Get zipcode
        zipcode = request.form.get("zipcode")

        # Get emailaddress
        emailaddress = request.form.get("emailaddress")
        print("Email Received:", emailaddress)


        global primary_owner_values
        primary_owner_values = [name, birthdate, placeofbirth, sex, displayname, mothermaidenname, educationalattainment, civilstatus,
                                noofdependents, tinnumber, sssgsis, carownership, citizenship, mobilenumber, homephonenumber, homeaddress,
                                zipcode, emailaddress]

       # print(insertprimaryowner(primary_owner_values)) # REMOVED TO ADD FOR FINAL SUBMIT BUTTON

        return redirect(url_for("work_forms"))

    else:
        return render_template("index.html")

@app.route("/About_Work_Form")
def work_forms():
    return render_template("aboutwork.html")

@app.route("/submitaboutwork", methods = ["POST", "GET"])
def submitaboutwork():
    if request.method == "POST":

        # Get employmenttype
        employmenttype = request.form.get("employmentType")
        if employmenttype == "others":
            employmenttype = request.form.get("otherEmploymentType")

        # Get employerbusinessname
        employerbusinessname = request.form.get("employerbusinessname")

        # Get yearswithpresentemployer
        yearswithpresentemployer = int(request.form.get("yearswithpresentemployer"))

        # Get position
        position = request.form.get("position")

        # Get natureofbusiness
        natureofbusiness = request.form.get("natureofbusiness")

        # Get officeaddress
        officeaddress = request.form.get("officeaddress")

        # Get zipcode
        officezipcode = request.form.get("officezipcode")

        # Get officephonenumber
        officephonenumber = request.form.get("officephonenumber")

        # Get preferreddelivery
        global primary_owner_values
        global preferred_card_delivery
        if request.form.get("preferredDelivery") == "homeAddress":
            preferred_card_delivery = 'Home Address'
        elif request.form.get("preferredDelivery") == "officeAddress":
            preferred_card_delivery = 'Office Address'

        # Get basicmonthlyincome
        global basic_monthly_income_global
        basic_monthly_income_global = int(request.form.get("basicmonthlyincome"))
        print("Test basic income:", basic_monthly_income_global, type(basic_monthly_income_global))

        # Get officeemailaddress
        officeemailaddress = request.form.get("officeemailaddress")

        # Get previousemployer
        previousemployer = request.form.get("previousemployer")

        global about_work_values
        about_work_values = [employmenttype, employerbusinessname, officeaddress, natureofbusiness,
                             officephonenumber, yearswithpresentemployer, position, officezipcode,
                             officeemailaddress, previousemployer]

        return redirect(url_for("databasetest"))


    else:
        return render_template("aboutwork.html")

@app.route("/databasetest")
def databasetest():
    global primary_owner_values
    global about_work_values
    global preferred_card_delivery


    # Get basicmonthlyincome
    primary_owner_values.append(preferred_card_delivery)
    primary_owner_values.append(basic_monthly_income_global)

    worksuccess, work_id_val = insertwork(about_work_values) #insert and receive workid
    print(worksuccess)

    primary_owner_values.append(work_id_val)

    pownersuccess, primary_id_val = insertprimaryowner(primary_owner_values)
    print(pownersuccess)


    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug = True)