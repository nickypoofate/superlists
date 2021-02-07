from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    #edith has heard about a cool new online to-do app. she goes to 
    #check out its homepage
    self.browser.get('http://localhost:8000')
    #she notices the page title / header mention to-do lists
    self.assertIn('To-Do', self.browser.title)
    self.fail('Finish the test!')
    #She is invited to enter an item straight away
    #She types "buy peacock feathers"  into a text box  (her hobby is fly-fishing lures)
    #when she hits enter, the page updates, and now the page lists --
    #"1: buy peacock feathers" as an item in a todo list
    #There is still a text box inviting her to add another item. She 
    #enters "use peacock feathers to make a fly" (edith is methodical)
    #the page updates again, and now shows both items on her list
    #Edith wonders whether the site will remember her list.  Then she sees that
    #the site has generated a unique url for her -- there is some 
    #explanatory text to that effect
    #she visits the url -- her to-do list is still there
    #satisfied, she goes back to sleep

if __name__ == '__main__':
  unittest.main()
browser.quit()
