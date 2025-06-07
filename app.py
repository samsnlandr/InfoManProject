from flask import Flask, redirect, url_for, render_template, request
from DatabaseConnection import insertprimaryowner, insertwork

app = Flask(__name__)
primary_owner_values = [] #List that contains the infos for primary owner table in SQL
about_work_values = [] #List that contains the infos for work table in SQL
supplementary_1_values = [] #List that contains the infos for work table in SQL
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
            name = request.form.get("firstName") + " " + request.form.get("surname")
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

        action_val = request.form.get("actionbtn")
        if action_val == "add supplementary":
             return redirect(url_for("supplementary_forms"))
        elif action_val == "final submit":
            return redirect(url_for("databasetest")) #TODO Change and replace with InjectDatabasePrimaryOnly


    else:
        return render_template("aboutwork.html")


@app.route("/supplementary_forms")
def supplementary_forms():
    return render_template("supplementary.html")

@app.route("/submitsupplementary", methods =['POST', 'GET'])
def submit_supplementary1():

    # Get name
    surname = request.form.get("supSurname")
    firstname = request.form.get("supFirstName")
    middlename = request.form.get("supMiddleName")

    if middlename == "N/A":
        name = firstname + " " + surname
    else:
        name = firstname + " " + middlename + " " + surname

    # Get relationship #TODO add functionalities for other
    relationship = request.form.get("supRelationship")

    # Get birthday
    birthday = request.form.get("supBirthdate")

    # Get placeofbirth
    placeofbirth = request.form.get("supPlaceOfBirth")

    # Get sex
    sex = request.form.get("supSex")
    if sex == "male":
        sex = "M"
    elif sex == "female":
        sex = "F"

    # Get civilstatus
    civilstatus = request.form.get("supCivilStatus")
    if civilstatus == "single":
        civilstatus = "S"
    elif civilstatus == "married":
        civilstatus = "M"
    elif civilstatus == "divorced":
        civilstatus = "D"
    elif civilstatus == "Widowed":
        civilstatus = "W"

    # Get citizenship #TODO Add functionalities for non-filipino
    citizenship = request.form.get("supCitizenship")

    # Get address
    address = request.form.get("supHomeAddress")

    # Get zipcode
    zipcode = request.form.get("supZipCode")

    # Get homephone
    homephone = request.form.get("supHomePhoneNumber")

    # Get mobilephone
    mobilephone = request.form.get("supMobileNumber")

    # Get email
    email = request.form.get("supEmailAddress")

    # Get employername
    employername = request.form.get("supEmployerBusinessName")

    # Get employeraddress
    employeraddress = request.form.get("supEmployerBusinessAddress")

    # Get sourceoffunds
    sourceoffunds = request.form.get("supSourceOfFunds")

    # Get naturebusiness
    naturebusiness = request.form.get("supNatureOfBusiness")

    # Get officephone
    officephone = request.form.get("supOfficePhoneNumber")

    global supplementary_1_values
    supplementary_1_values = [name, birthday, placeofbirth, sex, civilstatus, citizenship, address, zipcode, homephone,
                              mobilephone, email, employername, employeraddress, sourceoffunds, naturebusiness, officephone,
                              relationship] #TODO append the primary card id after putting them in the database

    # action button
    actionbtn = request.form.get("actionbtn")
    if actionbtn == "add another":
       return redirect(url_for("supplementary_forms_2"))
    elif actionbtn == "submit":
        return redirect(url_for("")) #TODO injectsupp1

@app.route("/supplementary_forms_2")
def supplementary_forms_2():
    render_template("supplementary2.html")

def submit_supplementary2():

    # Get name
    surname = request.form.get("supSurname")
    firstname = request.form.get("supFirstName")
    middlename = request.form.get("supMiddleName")

    if middlename == "N/A":
        name = firstname + " " + surname
    else:
        name = firstname + " " + middlename + " " + surname

    # Get relationship #TODO add functionalities for other
    relationship = request.form.get("supRelationship")

    # Get birthday
    birthday = request.form.get("supBirthdate")

    # Get placeofbirth
    placeofbirth = request.form.get("supPlaceOfBirth")

    # Get sex
    sex = request.form.get("supSex")
    if sex == "male":
        sex = "M"
    elif sex == "female":
        sex = "F"

    # Get civilstatus
    civilstatus = request.form.get("supCivilStatus")
    if civilstatus == "single":
        civilstatus = "S"
    elif civilstatus == "married":
        civilstatus = "M"
    elif civilstatus == "divorced":
        civilstatus = "D"
    elif civilstatus == "Widowed":
        civilstatus = "W"

    # Get citizenship #TODO Add functionalities for non-filipino
    citizenship = request.form.get("supCitizenship")

    # Get address
    address = request.form.get("supHomeAddress")

    # Get zipcode
    zipcode = request.form.get("supZipCode")

    # Get homephone
    homephone = request.form.get("supHomePhoneNumber")

    # Get mobilephone
    mobilephone = request.form.get("supMobileNumber")

    # Get email
    email = request.form.get("supEmailAddress")

    # Get employername
    employername = request.form.get("supEmployerBusinessName")

    # Get employeraddress
    employeraddress = request.form.get("supEmployerBusinessAddress")

    # Get sourceoffunds
    sourceoffunds = request.form.get("supSourceOfFunds")

    # Get naturebusiness
    naturebusiness = request.form.get("supNatureOfBusiness")

    # Get officephone
    officephone = request.form.get("supOfficePhoneNumber")

    global supplementary_1_values
    supplementary_1_values = [name, birthday, placeofbirth, sex, civilstatus, citizenship, address, zipcode, homephone,
                              mobilephone, email, employername, employeraddress, sourceoffunds, naturebusiness, officephone,
                              relationship] #TODO append the primary card id after putting them in the database

    return redirect(url_for("")) #TODO injectsupp2




@app.route("/databasetest")
def databasetest(): #TODO to be changed with different injector functions
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