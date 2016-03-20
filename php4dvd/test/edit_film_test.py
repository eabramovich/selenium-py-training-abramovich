import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EditFilmTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://localhost/"

    def test_edit_film(self):
        movieTitle = "Devchata"
        imdbNumber = "0134614"
        duration = "92"
        rating = "8.362"
        linkTrailer = "https://www.youtube.com/watch?v=LaCUkjlQuVw"
        year = "1961"


        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")
        username = driver.find_element_by_id("username")
        username.send_keys("admin")
        password = driver.find_element_by_name("password")
        password.send_keys("admin")
        driver.find_element_by_name("submit").click()

        movie = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#results div[title='" + movieTitle + "']"))
        )
        movie.click()

        edit = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#content nav ul li:nth-child(3) a"))
        )
        edit.click()

        imdbidField = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.NAME, "imdbid"))
        )
        imdbidField.send_keys(imdbNumber)
        durationField = driver.find_element_by_name("duration")
        durationField.send_keys(duration)
        ratingField = driver.find_element_by_name("rating")
        ratingField.send_keys(rating)
        trailerField = driver.find_element_by_name("trailer")
        trailerField.send_keys(linkTrailer)

        save = driver.find_element_by_id("submit")
        save.click();

        h2Title = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".maininfo_full h2"))
        )
        self.assertEqual(h2Title.text, movieTitle + " (" + year + ")")

        driver.find_element_by_css_selector("#content nav ul li:nth-child(5) a").click()

        imdbidField2 = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.NAME, "imdbid"))
        )
        durationField2 = driver.find_element_by_name("duration")
        ratingField2 = driver.find_element_by_name("rating")
        trailerField2 = driver.find_element_by_name("trailer")

        self.assertEqual(imdbidField2.get_attribute("value"), imdbNumber)
        self.assertEqual(durationField2.get_attribute("value"), duration)
        self.assertEqual(ratingField2.get_attribute("value"), rating)
        self.assertEqual(trailerField2.get_attribute("value"), linkTrailer)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
