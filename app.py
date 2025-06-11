from flask import Flask, redirect, url_for, render_template, request
from DatabaseConnection import insertprimaryowner, insertwork, insertsupplementary

app = Flask(__name__)
primary_owner_values = [] #List that contains the infos for primary owner table in SQL
about_work_values = [] #List that contains the infos for work table in SQL
supplementary_1_values = [] #List that contains the infos for supplementary1 table in SQL
supplementary_2_values = [] #List that contains the infos for supplementary2 in SQL
preferred_card_delivery = None #Variable to fetch from different page
basic_monthly_income_global = None

#TODO Unique Values, error code


@app.route("/")
def redirect_homepage():
    return redirect(url_for("homepage"))

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

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
        noofdependents = 0

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


        global primary_owner_values
        primary_owner_values = [name, birthdate, placeofbirth, sex, displayname, mothermaidenname, educationalattainment, civilstatus,
                                noofdependents, tinnumber, sssgsis, carownership, citizenship, mobilenumber, homephonenumber, homeaddress,
                                zipcode, emailaddress]

       # print(insertprimaryowner(primary_owner_values)) # REMOVED TO ADD FOR FINAL SUBMIT BUTTON

        return redirect(url_for("work_forms"))

    else:
        return redirect(url_for("fill_out_forms"))

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

        print(f"about work values: {about_work_values}")

        action_val = request.form.get("actionbtn")

        if action_val == "add supplementary":
             return redirect(url_for("supplementary_forms"))
        elif action_val == "submit":
            return redirect(url_for("primaryinjector"))

    else:
        return redirect(url_for("work_forms"))


@app.route("/supplementary_forms")
def supplementary_forms():
    return render_template("supplementary.html")

@app.route("/submitsupplementary", methods =['POST', 'GET'])
def submit_supplementary1():

    if request.method == "POST":
        # Get name
        surname = request.form.get("supSurname")
        firstname = request.form.get("supFirstName")
        middlename = request.form.get("supMiddleName")

        if middlename == "N/A":
            name = firstname + " " + surname
        else:
            name = firstname + " " + middlename + " " + surname

        # Get relationship
        relationship = request.form.get("supRelationship")
        if relationship == "other":
            relationship = request.form.get("supOtherRelationship")

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

        # Get citizenship
        citizenship = request.form.get("supCitizenship")
        if citizenship == "non-filipino":
            citizenship = request.form.get("supOtherCitizenship")

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
        supplementary_1_values = [name, birthday, placeofbirth, sex, civilstatus, citizenship, address, zipcode,
                                  homephone,
                                  mobilephone, email, employername, employeraddress, sourceoffunds, naturebusiness,
                                  officephone, relationship]
        # action button
        action_val = request.form.get("actionbtn")
        if action_val == "addanother":
            print(f"button value:{action_val}")
            return redirect(url_for("supplementary_forms_2"))
        elif action_val == "submit":
            print(f"button value:{action_val}")
            return redirect(url_for("inject_supplementary_1"))
    else:
        return redirect(url_for("supplementary_forms"))


@app.route("/supplementary_forms_2")
def supplementary_forms_2():
    return render_template("supplementary2.html")

@app.route("/submitsupplementary2", methods = ['POST', 'GET'])
def submit_supplementary2():
    if request.method == "POST":
        # Get name
        surname = request.form.get("supSurname")
        firstname = request.form.get("supFirstName")
        middlename = request.form.get("supMiddleName")

        if middlename == "N/A":
            name = firstname + " " + surname
        else:
            name = firstname + " " + middlename + " " + surname

        # Get relationship
        relationship = request.form.get("supRelationship")
        if relationship == "other":
            relationship = request.form.get("supOtherRelationship")

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

        # Get citizenship
        citizenship = request.form.get("supCitizenship")
        if citizenship == "non-filipino":
            citizenship = request.form.get("supOtherCitizenship")

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

        global supplementary_2_values
        supplementary_2_values = [name, birthday, placeofbirth, sex, civilstatus, citizenship, address, zipcode,
                                  homephone,
                                  mobilephone, email, employername, employeraddress, sourceoffunds, naturebusiness,
                                  officephone, relationship]
        # action button
        action_val = request.form.get("actionbtn")
        if action_val == "submit":
            print(f"button value:{action_val}")
            return redirect(url_for("inject_supplementary_2"))
    else:
        return redirect(url_for("supplementary_forms"))

@app.route("/inject_primary_only")
def primaryinjector():              #Function to insert record, 0 dependents
    global primary_owner_values
    global about_work_values
    global preferred_card_delivery
    global basic_monthly_income_global

    primary_owner_values[8] = 0

    # Get basicmonthlyincome
    primary_owner_values.append(preferred_card_delivery)
    primary_owner_values.append(basic_monthly_income_global)

    worksuccess, work_id_val = insertwork(about_work_values)  # insert and receive workid
    print(worksuccess)

    primary_owner_values.append(work_id_val)

    pownersuccess, primary_id_val = insertprimaryowner(primary_owner_values)
    print(pownersuccess)

    return redirect(url_for("confirmation_page"))

@app.route("/inject_supplementary_1")
def inject_supplementary_1():
    global primary_owner_values
    global about_work_values
    global supplementary_1_values
    global preferred_card_delivery
    global basic_monthly_income_global

    primary_owner_values[8] = 1

    # Get basicmonthlyincome
    primary_owner_values.append(preferred_card_delivery)
    primary_owner_values.append(basic_monthly_income_global)

    worksuccess, work_id_val = insertwork(about_work_values)  # insert and receive workid
    print(worksuccess)

    primary_owner_values.append(work_id_val)

    pownersuccess, primary_id_val = insertprimaryowner(primary_owner_values)
    print(pownersuccess)

    supplementary_1_values.append(primary_id_val)
    supplementary1success, supp_id_val = insertsupplementary(supplementary_1_values, 1)
    print(supplementary1success)

    return redirect(url_for("confirmation_page"))


@app.route("/inject_supplementary_2")
def inject_supplementary_2():
    global primary_owner_values
    global about_work_values
    global supplementary_1_values
    global supplementary_2_values
    global preferred_card_delivery
    global basic_monthly_income_global

    primary_owner_values[8] = 2 # supplementary_count
    print(f"Count of Dependents:{primary_owner_values[8]}")

    # Get basicmonthlyincome
    primary_owner_values.append(preferred_card_delivery)
    primary_owner_values.append(basic_monthly_income_global)

    worksuccess, work_id_val = insertwork(about_work_values)  # insert and receive workid
    print(worksuccess)

    primary_owner_values.append(work_id_val)

    pownersuccess, primary_id_val = insertprimaryowner(primary_owner_values)
    print(pownersuccess)

    supplementary_1_values.append(primary_id_val)
    supplementary1success, supp_id_val = insertsupplementary(supplementary_1_values, 1)
    print(supplementary1success)

    supplementary_2_values.append(primary_id_val)
    print(f"Supplement 2 Values: {supplementary_2_values}")
    supplementary2success, supp_id2_val = insertsupplementary(supplementary_2_values, 2)
    print(supplementary2success)

    return redirect(url_for("confirmation_page"))

@app.route("/confirmation_page")
def confirmation_page():
    return render_template("confirmation.html")

if __name__ == "__main__":
    app.run(debug = True)