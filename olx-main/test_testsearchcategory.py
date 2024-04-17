# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestsearchcategory():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testsearchcategory(self):
    self.driver.get("http://localhost:3000/")
    self.driver.set_window_size(1051, 846)
    self.driver.find_element(By.CSS_SELECTOR, ".searchInputs > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".searchInputs > input").send_keys("camera")
    self.driver.find_element(By.CSS_SELECTOR, ".dataItem:nth-child(1) > p").click()
    self.driver.find_element(By.CSS_SELECTOR, ".searchInputs > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".searchInputs > input").send_keys("motor")
    self.driver.find_element(By.CSS_SELECTOR, ".dataItem > p").click()
    self.driver.close()
  