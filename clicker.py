import random
from dotenv import load_dotenv
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import time
from instagrapi import Client
import pickle

load_dotenv()

email = os.environ["EMAIL"]
password = os.environ["PASSWORD"]
# email_insta = os.getenv("EMAIL_INSTA")
# password_insta = os.getenv("PASSWORD_INSTA")

with open("insta_cookie.pkl", "rb") as f:
    client = pickle.load(f)


driver = Driver(
    uc=True,
    headed=True,
    user_data_dir="./CookiesFolderUcHeaded/",
    chromium_arg="--disable-blink-features=AutomationControlled",
)


# pause = input("Pause")
driver.implicitly_wait(10)


def getRandSleepTime(driver=driver):
    driver.sleep(random.randint(4, 8))


def getSmallRandSleepTime(driver=driver):
    driver.sleep(random.uniform(0.7, 1.9))


def getTypingTime():
    return random.uniform(0.2, 0.6)


def driverType(driver=driver, selector=None, text=None):
    label = driver.find_elements(By.CSS_SELECTOR, selector)

    for letter in text:
        driver.sleep(getTypingTime())
        label[0].send_keys(letter)


def actionType(driver=driver, selector=None, text=None):
    action = ActionChains(driver=driver)
    for letter in text:
        driver.sleep(getTypingTime())

        action.send_keys(letter).perform()

    pass


def getRandomPauseTime():
    return random.randint(180, 230)


def youtubeFollow():
    pass


def youtubeLike():
    pass


def TwitterFollow(driver=driver):
    link = "https://www.like4like.org/user/earn-twitter.php"
    driver.get(link)
    getRandSleepTime()

    driver.click(".pulse-checkBox")
    driver.switch_to.window(driver.window_handles[1])

    getRandSleepTime()

    # twitterReconnect(driver=driver)
    getRandSleepTime()

    try:
        action = ActionChains(driver)
        action.send_keys(Keys.ENTER).perform()
        print("[+] Twitter Follow")
    except Exception as e:
        print("Failed to perform twitterFollow :", e)

    getRandSleepTime()
    getRandSleepTime()

    driver.close()


def TwitterLike(driver=driver):
    link = "https://www.like4like.org/user/earn-twitter-favorites.php"
    driver.get(link)
    getRandSleepTime()

    driver.click(".pulse-checkBox")
    driver.switch_to.window(driver.window_handles[1])
    getRandSleepTime()
    # twitterReconnect(driver=driver)

    try:
        button = driver.find_element(
            By.CSS_SELECTOR, ".r-13awgt0:nth-child(3) .r-1ny4l3l"
        )
        ActionChains(driver).move_to_element(button).click(button).perform()
        print("[+] Twitter Like")
    except Exception as e:
        print("Failed to twitterLike : ", e)

    getRandSleepTime()
    getRandSleepTime()

    driver.close()


def tiktokFollow(driver=driver):
    link = "https://www.like4like.org/user/earn-tiktok-follow.php"
    driver.get(link)
    getRandSleepTime()

    driver.click(".pulse-checkBox")
    driver.switch_to.window(driver.window_handles[1])
    getRandSleepTime()

    try:
        button = driver.find_element(
            By.CSS_SELECTOR,
            "#main-content-others_homepage > div > div.css-1g04lal-DivShareLayoutHeader-StyledDivShareLayoutHeaderV2.enm41492 > div.css-1gk89rh-DivShareInfo.ekmpd5l2 > div.css-1nbnul7-DivShareTitleContainer.ekmpd5l3 > div > div.css-1h3j14u-DivFollowButtonWrapper.e18e4obn4 > button",
        )
        ActionChains(driver).move_to_element(button).click(button).perform()
        print("[+] Tiktok Follow")
    except Exception as e:
        print("Failed to tiktokFollow :", e)

    # driver.click("#main-content-others_homepage > div > div.css-1g04lal-DivShareLayoutHeader-StyledDivShareLayoutHeaderV2.enm41492 > div.css-1gk89rh-DivShareInfo.ekmpd5l2 > div.css-1nbnul7-DivShareTitleContainer.ekmpd5l3 > div > div.css-1h3j14u-DivFollowButtonWrapper.e18e4obn4 > button")
    getRandSleepTime()

    driver.close()


def tiktokLike(driver=driver):
    link = "https://www.like4like.org/user/earn-tiktok-like.php"
    driver.get(link)
    getRandSleepTime()

    driver.click(".pulse-checkBox")
    driver.switch_to.window(driver.window_handles[1])
    getRandSleepTime()

    try:
        # button = driver.find_element(By.CSS_SELECTOR,"#main-content-video_detail > div > div.css-12kupwv-DivContentContainer.ege8lhx2 > div.css-1senhbu-DivLeftContainer.ege8lhx3 > div.css-1sb4dwc-DivPlayerContainer.eqrezik4 > div.css-ty9aj4-DivVideoContainer.eqrezik7 > div.css-79f36w-DivActionBarWrapper.eqrezik8 > div > button:nth-child(1)")

        # ActionChains(driver).move_to_element(button).click(button)
        driver.click(
            "#main-content-video_detail > div > div.css-12kupwv-DivContentContainer.ege8lhx2 > div.css-1senhbu-DivLeftContainer.ege8lhx3 > div.css-1sb4dwc-DivPlayerContainer.eqrezik4 > div.css-ty9aj4-DivVideoContainer.eqrezik7 > div.css-79f36w-DivActionBarWrapper.eqrezik8 > div > button:nth-child(1)"
        )
        print("[+] Tiktok Like")
    except Exception as e:
        print("Failed to tiktokLike :", e)
    getRandSleepTime()
    driver.close()


def soundcloudFollow(driver=driver):
    link = "https://www.like4like.org/user/earn-soundcloud-follow.php"
    driver.get(link)
    getRandSleepTime()

    driver.click(".pulse-checkBox")
    driver.switch_to.window(driver.window_handles[1])

    try:
        button = driver.find_elements(
            By.CSS_SELECTOR,
            "#content > div > div.l-vertical-bar > div > div.userInfoBar__buttons > div > button.sc-button-follow.sc-button.sc-button-medium.sc-button-responsive.sc-button-cta.sc-button-primary",
        )
        # print(button)

        # ActionChains(driver).move_to_element(button[0]).click(button[0]).perform()
        driver.click(
            "#content > div > div.l-vertical-bar > div > div.userInfoBar__buttons > div > button.sc-button-follow.sc-button.sc-button-medium.sc-button-responsive.sc-button-cta.sc-button-primary"
        )
        print("[+] SoundCloud Follow")
    except Exception as e:
        print("Failed to soundcloudFollow :", e)
    getRandSleepTime()
    getRandSleepTime()

    driver.close()


def soundcloudLike(driver=driver):
    link = "https://www.like4like.org/user/earn-soundcloud-like.php"
    driver.get(link)
    getRandSleepTime()

    driver.click(".pulse-checkBox")
    driver.switch_to.window(driver.window_handles[1])
    getRandSleepTime()

    try:
        buttons = driver.find_elements(By.CSS_SELECTOR, ".sc-button-like")
        for i in buttons:
            print(i.text)
            if "Like" in i.text:
                button = i
                break
        ActionChains(driver).move_to_element(button).click(button).perform()
        print("[+] SoundCloud Like")

    except Exception as e:
        print("Failed to soundcloudLike :", e)
    getRandSleepTime()
    driver.close()


def facebookFollow(driver=driver, link=None):

    driver.get(link)
    getSmallRandSleepTime()

    print("Done")
    driver.click(".pulse-checkBox")
    driver.switch_to.window(driver.window_handles[1])

    driver.sleep(10)

    try:
        researchButton = driver.find_elements(
            By.CSS_SELECTOR, ".xusnbm3+ .xusnbm3 .x1dem4cn .xuxw1ft"
        )

        suivre = driver.find_elements(By.XPATH, '//*[contains(text(),"Suivre")]')
        postLike = driver.find_elements(By.CSS_SELECTOR, ".x5ve5x3 .xuxw1ft")
        print("suivre :", suivre)

        # likeButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(),"J\'aime")]')))

        for i in researchButton:
            if i.text == "J’aime":
                ActionChains(driver).move_to_element(i).click(i).perform()
                getRandSleepTime()
                print("[+] J'aime")
                driver.close()
                return

        for j in suivre:
            if j.text == "Suivre":
                ActionChains(driver).move_to_element(j).click(j).perform()
                getRandSleepTime()
                print("[+] Suivre")
                driver.close()
                return
    except Exception as e:
        print("Failed to facebookFollow :", e)

    getRandSleepTime()

    driver.close()
    return


def facebookComment(driver=driver):
    link = "https://www.like4like.org/user/earn-facebook-comments.php"
    driver.get(link)
    getSmallRandSleepTime()

    driver.click(".pulse-checkBox")
    driver.switch_to.window(driver.window_handles[1])
    # driver.maximize_window()
    getRandSleepTime()

    text = "Nice !!!"
    label = ".notranslate .x1mh8g0r"

    try:
        driverType(selector=label, text=text)
        actions = ActionChains(driver)
        getSmallRandSleepTime()
        actions.send_keys(Keys.ENTER).perform()
        print("[+] Facebook Comment")
    except Exception as e:
        print("Failed to facebookComment :", e)
    getRandSleepTime()
    driver.close()


def instaFollowApi(link=None, client=client):
    username = link.split("/")[-2]
    try:
        user_id = client.user_id_from_username(username)
        follow = client.user_follow(user_id)
        print("[+] Successfully InstaFollowApi")
    except Exception as e:
        print("Failed to instaFollowApi : ", e)


def instagramFollow(driver=driver):
    link = "https://www.like4like.org/user/earn-instagram-follow.php"
    driver.get(link)
    getSmallRandSleepTime()

    driver.click(".pulse-checkBox")
    driver.switch_to.window(driver.window_handles[1])
    getRandSleepTime()
    # instagramReconnect()
    getRandSleepTime()
    instaurl = driver.current_url

    instaFollowApi(link=instaurl)

    # try:
    #     button = driver.find_element(By.CSS_SELECTOR, "._ap30")
    #     ActionChains(driver).move_to_element(button).click(button).perform()

    # except Exception as e:
    #     print("Failed to InstagramFollow :", e)
    # getRandSleepTime()

    driver.close()


def instaLikeApi(link=None, client=client):
    try:
        media_pk = client.media_pk_from_url(link)
        media_id = client.media_id(media_pk)
        media = client.media_like(media_id)
        print("[+] instaLike Successfully")
    except Exception as e:
        print("Failed to instaLikeApi :", e)


def instagramLike(driver=driver):
    link = "https://www.like4like.org/user/earn-instagram-like.php"
    driver.get(link)
    getSmallRandSleepTime()

    driver.click(".pulse-checkBox")
    driver.switch_to.window(driver.window_handles[1])
    getRandSleepTime()

    instaurl = driver.current_url

    instaLikeApi(link=instaurl)

    # try:
    #     button = driver.find_elements(By.CSS_SELECTOR, ".xp7jhwk .xl56j7k")[0]
    #     ActionChains(driver).move_to_element(button).click(button).perform()
    # except Exception as e:
    #     print("Failed to instagramLike :", e)
    # getRandSleepTime()

    driver.close()


def instaCommentApi(link=None, client=client):
    try:
        media_pk = client.media_pk_from_url(link)
        media_id = client.media_id(media_pk)
        comment = client.media_comment(media_id, "...")
        print("[+] Successfully instaCommentedApi ")
    except Exception as e:
        print("Failed to instaCommentApi :", e)


def instagramComment(driver=driver):
    link = "https://www.like4like.org/user/earn-instagram-comment.php"
    driver.get(link)
    getSmallRandSleepTime()

    driver.click(".pulse-checkBox")
    driver.switch_to.window(driver.window_handles[1])
    getRandSleepTime()

    instaurl = driver.current_url
    instaCommentApi(link=instaLikeApi)
    # instagramReconnect()
    # getRandSleepTime()

    # text = "Nice !!!"
    # label = ".x12bmzex.xurb0ha"

    # try:

    #     button = driver.find_elements(By.CSS_SELECTOR, label)[0]
    #     ActionChains(driver).move_to_element(button).click(button).perform()
    #     getSmallRandSleepTime()

    #     # driverType(selector=label,text=text)
    #     actionType(text=text)
    #     actions = ActionChains(driver)
    #     getSmallRandSleepTime()

    #     actions.send_keys(Keys.ENTER).perform()
    # except Exception as e:
    #     print("Failed to instagramComment :", e)

    driver.close()


def pinterestFollow(driver=driver):
    ptlink = "https://www.like4like.org/user/earn-pinterest-follow.php"
    driver.get(ptlink)
    getSmallRandSleepTime()

    driver.click(".pulse-checkBox")
    driver.switch_to.window(driver.window_handles[1])

    getRandSleepTime()
    try:
        driver.click(".Il7")
        print("[+] pinterest Follow")
    except Exception as e:
        print("Failed to pinterest follow")
        pass
    getRandSleepTime()

    getRandSleepTime()
    driver.close()


def Submit(driver=driver):
    driver.switch_to.window(driver.window_handles[0])
    getSmallRandSleepTime()

    driver.click(".pulse-checkBox")


def likeLoggin(driver=driver):

    driver.get("https://www.like4like.org/login/")
    # pause = input("test ...")
    try:
        driver.assert_element("#username")
        driver.assert_element("#password")
        # loginSelector = driver.find_element(By.CSS_SELECTOR,"#username")
        # passwordSelector = driver.find_element(By.CSS_SELECTOR,"#password")
        driverType(selector="#username", text=email)
        getRandSleepTime()
        driverType(selector="#password", text=password)
        driver.click("#login > fieldset > table > tbody > tr:nth-child(8) > td > span")

    except Exception as e:
        print(e)
        print("Already logged in !")
        pass


def quit(driver=driver):
    driver.quit()


jobs = [
    TwitterFollow,
    TwitterLike,
    tiktokFollow,
    tiktokLike,
    facebookFollow,
    facebookComment,
    instagramFollow,
    instagramLike,
    instagramComment,
    pinterestFollow,
    soundcloudFollow,
    soundcloudLike,
]


def test():
    likeLoggin()
    getSmallRandSleepTime()
    soundcloudFollow()
    Submit()


# test()


def main():
    iter = 0
    fbLinks = [
        "https://www.like4like.org/user/earn-facebook-subscribes.php",
        "https://www.like4like.org/user/earn-facebook-user-follow.php",
    ]
    likeLoggin()
    # pause = input("Pause")
    while iter < 3:
        iter += 1
        print("[+]  ITER ===> ", iter)

        for job in jobs:

            getSmallRandSleepTime()
            try:
                if job == facebookFollow:
                    for link in fbLinks:
                        job(link=link)
                        Submit()

                else:
                    job()
                    Submit()
            except Exception as e:
                print("Failed in Like4Like website :", e)
        time.sleep(getRandomPauseTime())
        print(f"[+] Finished iteration {iter}")
    quit()


if __name__ == "__main__":
    main()
