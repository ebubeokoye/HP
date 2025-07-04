from flask import Flask, redirect, render_template, request, jsonify

app =Flask (__name__, template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registeras")
def registeras():
    return render_template("register-as.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/reg_direction")
def reg_direction():
    return render_template("registration-direction.html")

@app.route("/createaccount-user")
def createaccountuser():
    return render_template("signup-user.html")

@app.route("/createaccount-vendor")
def createaccountvendor():
    return render_template("signup-vendor.html")

@app.route("/createaccount-agents")
def createaccountagents():
    return render_template("signup-agents.html")

@app.route("/createaccount-explore")
def createaccountexplore():
    return render_template("signup-explore.html")

# OTP pages to verify email
@app.route("/verify_useremail_otp", methods=["GET", "POST"])
def verify_useremail_otp():
    if request.method == "POST":
        return render_template("verify-useremail-otp.html")
    else:
        return render_template("verify-useremail-otp.html")
    
@app.route("/verify_vendoremail_otp", methods=["GET", "POST"])
def verify_vendoremail_otp():
    if request.method == "POST":
        return render_template("verify-vendoremail-otp.html")
    else:
        return render_template("verify-vendoremail-otp.html")
    
@app.route("/verify_landagentemail_otp", methods=["GET", "POST"])
def verify_landagentemail_otp():
    if request.method == "POST":
        return render_template("verify-landagentemail-otp.html")
    else:
        return render_template("verify-landagentemail-otp.html")
    
@app.route("/verify_houseagentemail_otp", methods=["GET", "POST"])
def verify_houseagentemail_otp():
    if request.method == "POST":
        return render_template("verify-houseagentemail-otp.html")
    else:
        return render_template("verify-houseagentemail-otp.html")
    
@app.route("/verify_explorersemail_otp", methods=["GET", "POST"])
def verify_explorersemail_otp():
    if request.method == "POST":
        return render_template("verify-explorersemail-otp.html")
    else:
        return render_template("verify-explorersemail-otp.html")



# when the user clicks on Buy from the landing page
@app.route("/buylinkfrompage2", methods=["POST"])
def buylinkfrompage2():
    return render_template("buylinkfrompage2.html")

# this section is for the user after they've registered/logged in
@app.route("/homepage", methods=["GET", "POST"])
def homepage(): 
    if request.method == "POST":
        return render_template("homepage.html")
    else: 
        return render_template("homepage.html")
    
# user buy land listing
@app.route("/buyland")
def buyland(): 
    return render_template("user-buyland.html")

@app.route("/user_eachlandcategory_listing")
def user_eachlandcategory_listing():
    return render_template("user-eachlandcategory-listing.html")

@app.route("/user_viewdetails_general_form")
def user_viewdetails_general_form():
    return render_template("user-viewdetails-general-form.html")

# page to get user location
@app.route("/get_user_location")
def get_user_location():
    return render_template("get-user-location.html")

# when they click on see all vendors from get user location html
@app.route("/all_vendors_from_userlocation")
def all_vendors_from_userlocation():
    return render_template("all-vendors-from-userlocation.html")

# when they click on see all houseagents from get user location html
@app.route("/all_houseagents_from_userlocation")
def all_houseagents_from_userlocation():
    return render_template("all-houseagents-from-userlocation.html")

# when they click on see all landagents from get user location html
@app.route("/all_landagents_from_userlocation")
def all_landagents_from_userlocation():
    return render_template("all-landagents-from-userlocation.html")

# user navigations after registration
@app.route("/rent")
def rent(): 
    return render_template("user-rent.html")

@app.route("/user_vendors")
def user_vendors(): 
    return render_template("user-buyvendors.html")

@app.route("/user_land_house_nav3")
def user_land_house_nav3(): 
    return render_template("user-land-house-nav3.html")

@app.route("/user_vendorsearch_nav")
def user_allcategories_nav(): 
    return render_template("user-vendorsearch-nav.html")

@app.route("/user_cart_nav4")
def user_cart_nav4(): 
    return render_template("user-cart-nav4.html")

@app.route("/user-account")
def useraccount(): 
    return render_template("user-account.html")

@app.route("/user_filterby_for_landagents")
def user_filterby_for_landagents(): 
    return render_template("user-filterby-for-landagents.html")

@app.route("/user_filterby_for_houseagents")
def user_filterby_for_houseagents(): 
    return render_template("user-filterby-for-houseagents.html")

# this section is for the land agent

@app.route("/land_agent_homepage", methods=["GET", "POST"])
def land_agent_homepage():
    if request.method == "POST":
        return render_template("landagent-homepage.html")
    else:
        return render_template("landagent-homepage.html")
    
@app.route("/agent_land_listing", methods=["GET", "POST"])
def agent_land_listing():
    if request.method == "POST":
        return redirect("/agent_land_listing")
    else:
        return render_template("agent-land-listing.html")
    
@app.route("/form_to_add_item_landagent")
def form_to_add_item_landagent():
    if request.method == "POST":
        return render_template("form-to-add-item-landagent.html")
    else:
        return render_template("form-to-add-item-landagent.html")
        
@app.route("/landing_agent_oneacre_listingpg2", methods=["GET", "POST"])
def landing_agent_oneacre_listingpg2():
    if request.method == "POST":
        return render_template("landing-agent-oneacre-listingpg2.html")
    else:
        return render_template("landing-agent-oneacre-listingpg2.html")
    
@app.route("/landagent_profilepage", methods=["GET", "POST"])
def landagent_profilepage():
    if request.method == "POST":
        return render_template("landagent-profilepage.html")
    else:
        return render_template("landagent-profilepage.html")
    
@app.route("/landagent_kyc_form", methods=["GET", "POST"])
def landagent_kyc_form():
    if request.method == "POST":
        return render_template("KYC-landagent-form.html")
    else:
        return render_template("KYC-landagent-form.html")

# this section is for the housing agent

@app.route("/housing_agent_homepage", methods=["GET", "POST"])
def housing_agent_homepage():
    if request.method =="POST":
        return render_template("housing-agent-homepage.html")
    else:
        return render_template("housing-agent-homepage.html")
# items listing
@app.route("/agent_housing_listing", methods=["GET", "POST"])
def agent_housing_listing():
    if request.method == "POST":
        return render_template("agent-housing-listing.html")
    else:
        return render_template("agent-housing-listing.html")

@app.route("/housing_agent_bungalow_listingpg2",  methods=["GET", "POST"])
def housing_agent_bungalow_listingpg2():
    if request.method == "POST":
        return render_template("housing-agent-bungalow-listingpg2.html")
    else:
        return render_template("housing-agent-bungalow-listingpg2.html")

@app.route("/form_to_add_item_housingagent")
def form_to_add_item_housingagent():
    return render_template("form-to-add-item-housingagent.html")

@app.route("/form_to_edit_item_housingagent")
def form_to_edit_item_housingagent():
    return render_template("edit-item-houseagent.html")

# Insights section
@app.route("/insights_page_housingagent")
def insights_page_housingagent():
    return render_template("insightspage-housingagent.html")

@app.route("/houseagent_profilepage", methods=["GET", "POST"])
def houseagent_profilepage():
    if request.method == "POST":
        return render_template("houseagent-profilepage.html")
    else:
        return render_template("houseagent-profilepage.html")
    
@app.route("/houseagent_kyc_form", methods=["GET", "POST"])
def houseagent_kyc_form():
    if request.method == "POST":
        return render_template("KYC-houseagent-form.html")
    else:
        return render_template("KYC-houseagent-form.html")


# this section is for the vendor after they've registered/logged in
@app.route("/vendor_homepage", methods=["GET", "POST"])
def vendor_homepage():
    if request.method == "POST":
        return render_template("vendor-homepage.html")
    else:
        return render_template("vendor-homepage.html")
    
@app.route("/vendor_listing", methods=["GET", "POST"])
def vendor_listing():
    if request.method == "POST":
        return render_template("vendor-listing.html")
    else:
        return render_template("vendor-listing.html")
    
@app.route("/form_to_add_item_vendor")
def form_to_add_item_vendor():
    if request.method == "POST":
        return render_template("form-to-add-item-vendor.html")
    else:
        return render_template("form-to-add-item-vendor.html")
    
@app.route("/vendor_kitchenitems_listingpg2", methods=["GET", "POST"])
def vendor_kitchenitems_listingpg2():
    if request.method == "POST":
        return render_template("vendor-kitchenitems-listingpg2.html")
    else:
        return render_template("vendor-kitchenitems-listingpg2.html")
    
@app.route("/vendor_profilepage", methods=["GET", "POST"])
def vendor_profilepage():
    if request.method == "POST":
        return render_template("vendor-profilepage.html")
    else:
        return render_template("vendor-profilepage.html")
    
@app.route("/vendor_kyc_form", methods=["GET", "POST"])
def vendor_kyc_form():
    if request.method == "POST":
        return render_template("KYC-vendorform.html")
    else:
        return render_template("KYC-vendorform.html")
    
@app.route("/store_info_and_operations_page")
def store_info_and_operations_page():
    return render_template("store-info-and-operations-page.html")
    
# this section  is for the vendors when they click vendor button on the landing page
@app.route("/vendor_button_landingpage")
def vendor_button_landingpage():
    return render_template("vendor-landingpage.html")

@app.route("/vendor_storeoperations", methods=["GET", "POST"])
def vendor_storeoperations():
    if request.method == "POST":
        return render_template("vendor-storeoperations.html")
    else:
        return render_template("vendor-storeoperations.html")
    
# this section is for the explorers after they've registered/logged in
@app.route("/explorers_profilepage", methods=["GET", "POST"])
def explorers_profilepage():
    if request.method == "POST":
        return render_template("explorers-profilepage.html")
    else:
        return render_template("explorers-profilepage.html")

# This if for the after logout, the page that serves them a login option back   
@app.route("/after_logout_page")
def after_logout_page():
    return render_template("after-logout-page.html")