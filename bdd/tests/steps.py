# -*- coding: utf-8 -*-
from lettuce import step
from lettuce import world
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


@step(u'Given I start the to-do app')
def given_i_start_the_to_do_app(step):
    world.browser = webdriver.Firefox()
    world.browser.get('http://localhost:8000')


@step(u'And I see "([^"]*)" as the page title')
def and_i_see_group1_as_the_page_title(step, page_title):
    assert page_title in world.browser.title, 'No se encuentra "%s" en el ' \
                                              'título de la página "%s"' % (
                                                  page_title,
                                                  world.browser.title)


@step(u'And I see "([^"]*)" as the page header')
def and_i_see_group1_as_the_page_header(step, page_header):
    header_text = world.browser.find_element_by_tag_name('h1').text
    assert page_header in header_text, 'No se encuentra "%s" en el título ' \
                                       'de la página "%s"' % (
                                           page_header, header_text)


@step(u'And I see "([^"]*)" as an invitation to add a to-do item')
def and_i_see_group1_as_an_invitation_to_add_a_to_do_item(step, expected):
    world.inputbox = world.browser.find_element_by_id('id_new_item')

    obtained = world.inputbox.get_attribute('placeholder')

    assert expected == obtained, 'El placeholder esperado es "%s" y el ' \
                                 'obtenido "%s"' % (expected, obtained)


@step(u'When I fill "([^"]*)" in the new to-do textbox')
def when_i_fill_group1_in_the_new_to_do_textbox(step, to_do_item):
    world.inputbox.send_keys(to_do_item)


@step(u'And I press the Enter key')
def and_i_press_the_enter_key(step):
    world.inputbox.send_keys(Keys.ENTER)
    time.sleep(1)


@step(u'Then I can see "([^"]*)" in the list of to-do items')
def then_i_can_see_group1_in_the_list_of_to_do_items(step, to_do_item):
    table = world.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')

    assert any(row.text == to_do_item for row in rows), \
        'No se encuentra "%s" en la lista de To-Do' % (to_do_item)


@step(u'And I finish the to-do app')
def and_i_finish_the_to_do_app(step):
    world.browser.quit()


    # from selenium import webdriver
    # from selenium.webdriver.common.keys import Keys
    # import time
    # import unittest
    #
    # class NewVisitorTest(unittest.TestCase):
    #
    #     def setUp(self):
    #         self.browser = webdriver.Firefox()
    #
    #     def tearDown(self):
    #         self.browser.quit()
    #
    #     def test_can_start_a_list_and_retrieve_it_later(self):
    #         # Edith has heard about a cool new online to-do app. She goes
    #         # to check out its homepage
    #         self.browser.get('http://localhost:8000')
    #
    #         # She notices the page title and header mention to-do lists
    #         self.assertIn('To-Do', self.browser.title)
    #         header_text = self.browser.find_element_by_tag_name('h1').text
    #         self.assertIn('To-Do', header_text)
    #
    #         # She is invited to enter a to-do item straight away
    #         inputbox = self.browser.find_element_by_id('id_new_item')
    #         self.assertEqual(
    #             inputbox.get_attribute('placeholder'),
    #             'Enter a to-do item'
    #         )
    #
    #         # She types "Buy peacock feathers" into a text box (Edith's hobby
    #         # is tying fly-fishing lures)
    #         inputbox.send_keys('Buy peacock feathers')
    #
    #         # When she hits enter, the page updates, and now the page lists
    #         # "1: Buy peacock feathers" as an item in a to-do list table
    #         inputbox.send_keys(Keys.ENTER)
    #         time.sleep(1)
    #
    # table = self.browser.find_element_by_id('id_list_table')
    # rows = table.find_elements_by_tag_name('tr')
    # self.assertTrue(
    #     any(row.text == '1: Buy peacock feathers' for row in rows)
    # )
    #
    #         # There is still a text box inviting her to add another item. She
    #         # enters "Use peacock feathers to make a fly" (Edith is very
    #         # methodical)
    #         self.fail('Finish the test!')
    #
    #         # The page updates again, and now shows both items on her list
    #         [...]
