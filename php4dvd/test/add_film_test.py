import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddFilmTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://localhost/"

    def test_add_film(self):
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")
        username = driver.find_element_by_id("username")
        username.send_keys("admin")
        password = driver.find_element_by_name("password")
        password.send_keys("admin")
        driver.find_element_by_name("submit").click()

        addMovie = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='./?go=add']"))
        )
        addMovie.click()

        movieTitle = "Devchata"
        inputTitle = driver.find_element_by_name("name")
        error = "This field is required"
        errorTitle = driver.find_element_by_css_selector("label[for='name']")
        errorTitleText = errorTitle.text
        errorYear = driver.find_element_by_css_selector("label[for='year']")
        errorYearText = errorYear.text
        self.assertEqual(error, errorTitleText)
        self.assertEqual(error, errorYearText)

        inputTitle.send_keys(movieTitle)
        self.assertEqual(False, errorTitle.is_displayed())
        self.assertEqual(error, errorYearText)

        save = driver.find_element_by_id("submit")
        save.click()
        self.assertEqual(True, errorYear.is_displayed())

        year = "1961"
        yearInput = driver.find_element_by_name("year")
        yearInput.send_keys(year)
        save.click()

        h2Title = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".maininfo_full h2"))
        )
        self.assertEqual(h2Title.text, movieTitle + " (" + year + ")")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
