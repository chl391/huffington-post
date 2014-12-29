from selenium import webdriver

#Credentials
huffpo_username = "chl391"
huffpo_password = "interview"
gmail = "charleslin.huffpo@gmail.com"
gmail_pass = "interview"

driver = webdriver.Firefox()
driver.get('http://huffingtonpost.com')

driver.find_element_by_css_selector('#hp_login_bt').click()
driver.find_element_by_xpath("//form[1]").click()

pagesource = driver.page_source

#Login to Huffington Post
username = driver.find_element_by_css_selector('#quicklogin_name')
password = driver.find_element_by_css_selector('#quicklogin_pass')
username.send_keys(huffpo_username)
password.send_keys(huffpo_password)
driver.find_element_by_id("quicklogin_button").click()

pagesource = driver.page_source

#Click h1 article
driver.find_element_by_css_selector('h1>a').click()

pagesource = driver.page_source

#Click share google+
driver.find_element_by_css_selector('.googleplus>a').click()

driver.switch_to_window(driver.window_handles[1])

pagesource = driver.page_source

#Login to Google+
gmail_username = driver.find_element_by_css_selector('#Email')
gmail_password = driver.find_element_by_css_selector('#Passwd')
gmail_username.send_keys(gmail)
gmail_password.send_keys(gmail_pass)
driver.find_element_by_id("signIn").click()

pagesource = driver.page_source

#Share
driver.find_element_by_css_selector(".bI>div:first-child").click()
