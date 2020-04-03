class Locators:
    # HomePageLocators
    signOn_xpath = "/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a"
    register_xpath = "/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a"
    support_xpath = "/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[3]/a"
    contact_xpath = "/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[4]/a"

    # RegisterPageLocators
    firstName_xpath = '//input[@name="firstName"]'
    lastName_xpath = '//input[@name="lastName"]'
    phone_xpath = '//input[@name="phone"]'
    email_xpath = '//*[@id="userName"]'
    address_xpath = '//input[@name="address1"]'
    city_xpath = '//input[@name="city"]'
    state_xpath = '//input[@name="state"]'
    postalCode_xpath = '//input[@name="postalCode"]'
    userName_xpath = '//input[@id="email"]'
    password_xpath = '//input[@name="password"]'
    confirmPassword_xpath = '//input[@name="confirmPassword"]'
    submitButton_xpath = '//input[@name="register"]'
    registerText_xpath = "//*[contains(text(), 'using the user name and password')]"

    # SignOnLocators
    loginUserName_xpath = '//input[@name="userName"]'
    loginPassword_xpath = '//input[@name="password"]'
    loginSubmit_xpath = '//input[@name="login"]'

    # FlightsLocators
    flightsButton_xpath = '/html/body/div/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/a'
    flightsUserName_xpath = '//input[@name="userName"]'
    flightsPassword = '//input[@name="password"]'

    # HomeTabLocators
    homelink = "/html/body/div/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/font/a"

    # FlightBookingLocators
    passenger_count_xpath = "//select[@name='passCount']"
    trip_type_xpath = "//input[@value='oneway']"
    
