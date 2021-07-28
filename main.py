import time

from selenium import webdriver

from local_settings import DRIVER_PATH, PASSWORD, EMAIL, MANABY_ID, MANABY_PASSWORD, REDMINE_ID

try:
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    options.add_experimental_option("detach", True)

    print('connecting to remote browser...')
    driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
    driver.set_window_position(0, -1000)
    driver.maximize_window()
    driver.implicitly_wait(10)

    print('open TeamHack and login...')
    driver.get('https://teamhack.io/login')
    driver.find_element_by_id('action-form').find_element_by_name('email').send_keys(EMAIL)
    driver.find_element_by_id('action-form').find_element_by_name('password').send_keys(PASSWORD)
    driver.find_element_by_id('submit-button').click()

    print('open Redmine and login...')
    driver.execute_script('window.open()')
    window = driver.window_handles
    driver.switch_to.window(window[1])
    driver.get('http://ec2-54-199-63-60.ap-northeast-1.compute.amazonaws.com/login')
    driver.find_element_by_id('username').send_keys(REDMINE_ID)
    driver.find_element_by_id('password').send_keys(PASSWORD)
    driver.find_element_by_id('login-submit').click()
    driver.get('http://ec2-54-199-63-60.ap-northeast-1.compute.amazonaws.com/projects/homete/issues/gantt')

    print('open sushida...')
    driver.execute_script('window.open()')
    window = driver.window_handles
    driver.switch_to.window(window[2])
    driver.get('http://typingx0.net/sushida/play.html')

    print('open shakyo.io and login...')
    driver.execute_script('window.open()')
    window = driver.window_handles
    driver.switch_to.window(window[3])
    driver.get('https://shakyo.io/users/sign_in')
    driver.find_element_by_id('user_email').send_keys(EMAIL)
    driver.find_element_by_id('user_password').send_keys(PASSWORD)
    driver.find_element_by_name('commit').click()
    driver.find_element_by_css_selector('a.navbar-item-link.nav-link').click()

    print('open manaby e-learning site and login...')
    driver.execute_script('window.open()')
    window = driver.window_handles
    driver.switch_to.window(window[4])
    driver.get('https://elearning-site.herokuapp.com/top/manaby')
    driver.find_element_by_id('user_usernumber').send_keys(MANABY_ID)
    driver.find_element_by_id('user_password').send_keys(MANABY_PASSWORD)
    driver.find_element_by_name("commit").click()

    # Team Hack画面に移動
    driver.switch_to.window(window[0])
    print('completed successfully all page open!!')
except Exception as e:
    print(e)
    time.sleep(30)
finally:
    print('finish')
