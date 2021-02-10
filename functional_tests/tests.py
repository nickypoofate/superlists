from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def check_for_row_in_list_table(self, row_text):
    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertIn(row_text, [row.text for row in rows])

  def test_can_start_a_list_and_retrieve_it_later(self):
    #edith has heard about a cool new online to-do app. she goes to
    #check out its homepage
    self.browser.get(self.live_server_url)
    #she notices the page title / header mention to-do lists
    self.assertIn('To-Do', self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('To-Do', header_text)
    #She is invited to enter an item straight away
    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
    #She types "buy peacock feathers"  into a text box  (her hobby is fly-fishing lures)
    inputbox.send_keys('Buy peacock feathers')
    #when she hits enter, the page updates, and now the page lists --
    #"1: buy peacock feathers" as an item in a todo list
    inputbox.send_keys(Keys.ENTER)
    time.sleep(1)
    self.check_for_row_in_list_table('1: Buy peacock feathers')
    #There is still a text box inviting her to add another item. She
    #enters "use peacock feathers to make a fly" (edith is methodical)
    inputbox = self.browser.find_element_by_id('id_new_item')
    inputbox.send_keys('Use peacock feathers to make a fly')
    inputbox.send_keys(Keys.ENTER)
    time.sleep(1)

    #the page updates again, and now shows both items on her list
    self.check_for_row_in_list_table('1: Buy peacock feathers')
    self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
    self.fail('Finish the test!')
    #Edith wonders whether the site will remember her list.  Then she sees that
    #the site has generated a unique url for her -- there is some
    #explanatory text to that effect
    #she visits the url -- her to-do list is still there
    #satisfied, she goes back to sleep
