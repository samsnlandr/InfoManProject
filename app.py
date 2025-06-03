from flask import Flask, redirect, url_for, render_template, request

from DatabaseConnection import insertprimaryowner

#TODO /Submit Route form.gets
app = Flask(__name__)
primary_owner_values = [] #List that contains the infos to insert to primary owner table in SQL

@app.route("/")
def home():
    return redirect(url_for("fill_out_forms"))

@app.route("/Card_Holder_Application_Form")
def fill_out_forms():
    return render_template("index.html")

@app.route("/submit", methods = ["POST", "GET"])
def submit():
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

        # Get sssgsis
        sssgsis = request.form.get("sssgsis")

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

        # Get preferredcarddelivery
        preferredcarddelivery = "Home Address" #TODO temporary value fetch from workpage

        # Get basicmonthlyincome
        basicmonthlyincome = 20000 #TODO temporary value, fetch from workpage

        # Get workid
        workid = 1 #TODO temporary value, fetch from workpage

        global primary_owner_values
        primary_owner_values = [name, birthdate, placeofbirth, sex, displayname, mothermaidenname, educationalattainment, civilstatus,
                                noofdependents, tinnumber, sssgsis, carownership, citizenship, mobilenumber, homephonenumber, homeaddress,
                                zipcode, emailaddress, preferredcarddelivery, basicmonthlyincome, workid]

       # print(insertprimaryowner(primary_owner_values)) # REMOVED TO ADD FOR FINAL SUBMIT BUTTON

        return redirect(url_for("work_forms"))

    else:
        return render_template("index.html")

@app.route("/About_Work_Form")
def work_forms():
    return render_template("aboutwork.html")

if __name__ == "__main__":
    app.run(debug = True)