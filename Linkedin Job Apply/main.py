from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.linkedin.com/jobs/search/?keywords=python')

login_button = driver.find_element(by=By.CLASS_NAME, value='nav__button-secondary')
login_button.click()

username = driver.find_element(by=By.ID, value='username')
username.send_keys('LINKEDIN_USERNAME')
password = driver.find_element(by=By.ID, value='password')
password.send_keys('LINKEDIN_PASSWORD', Keys.ENTER)

jobs = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

for job in jobs:
    job.click()

    try:
        apply = driver.find_element(by=By.CSS_SELECTOR, value='.jobs-s-apply button')
        apply.click()

        submit = driver.find_element(by=By.CSS_SELECTOR, value='footer button')
        if submit.get_attribute('data-control-name') == 'continue_unify':
            close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
            close_button.click()
            discard_button = driver.find_element(by=By.CLASS_NAME, value=".artdeco-modal__actionbar .artdeco-button--primary")
            discard_button.click()
        else:
            try:
                step_1 = driver.find_element(by=By.XPATH,
                                             value='/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button/span')
                step_1.click()
                step_2 = driver.find_element(by=By.XPATH,
                                             value='/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button[2]/span')
                step_2.click()

                step_3 = driver.find_element(by=By.XPATH,
                                             value='/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button[2]/span')
                step_3.click()
            except ElementClickInterceptedException:
                exit = driver.find_element(by=By.XPATH, value='//*[@id="ember347"]/li-icon/svg/path')
                exit.click()

    except NoSuchElementException:
        continue
