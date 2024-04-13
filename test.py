from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pickle
#options = Options()
#options.add_argument("user-data-dir=C:\Users\Dell\AppData\Local\Google\Chrome\User Data")
dr = Driver(user_data_dir="C:/Users/Dell/AppData/Local/Temp/tmpxatvvb4d")
dr.get("https://www.google.com")
dr.assert_element("#APjFqbsegzetreu")
pause = input("Done ?")
#coockie = dr.get_cookies()
#with open('cookies.pkl', 'wb') as file:
#    pickle.dump(coockie, file)

dr.sleep(1000)
dr.fullscreen_window()

dr.click("#onetrust-accept-btn-handler")
dr.sleep(2)

dr.click("#content > div > div > div.l-front-hero.l-inner-fullwidth > div > div.frontHero__signin > button.g-opacity-transition.frontHero__loginButton.g-button-transparent-inverted.sc-button.sc-button-medium.loginButton.sc-button-tertiary")


#dr.get("https://soundcloud.com/")
#dr.click("#onetrust-accept-btn-handler")
#dr.switch_to.window(dr.window_handles[1])
frame = dr.find_elements(By.CSS_SELECTOR, "body > div.webAuthContainerWrapper > iframe")
dr.switch_to_frame(frame[0])
dr.sleep(2)

#dr.click("#app > div > div > div > div > div > div > div.provider-buttons > div:nth-child(2) > button")
dr.type("#sign_in_up_email","tarek10032024@outlook.com")
dr.sleep(2)
dr.click("#sign_in_up_submit")
dr.sleep(5)

dr.type("#enter_password_field","antimage1992")
dr.sleep(8)

dr.click("#enter_password_submit")
dr.switch_to.default_content()
dr.sleep(5)
#dr.get("https://soundcloud.com/")