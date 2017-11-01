# -*- coding: utf-8 -*-

from lettuce import step
from lettuce import world
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time

import sys

reload(sys)
sys.setdefaultencoding("utf-8")


@step(u'Given I start the to-do app as "([^"]*)"')
def given_i_start_the_to_do_app_as_group1(step, usuario):
    world.browser = webdriver.Firefox()
    # world.browser.get('http://localhost:8000/lists/%s' % (usuario))
    world.browser.get('http://localhost:8000/lists/the-only-list-in-the-world/')
    world.browser.implicitly_wait(1)


@step(u'And I see "([^"]*)" as the page title')
def and_i_see_group1_as_the_page_title(step, page_title):
    assert page_title in world.browser.title, \
        'No se encuentra "%s" en el título de la página "%s"' \
        % (page_title, world.browser.title)


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

    assert any(to_do_item in row.text for row in rows), \
        'No se encuentra "%s" en la lista de To-Do' % (to_do_item)


@step(u'And I finish the to-do app')
def and_i_finish_the_to_do_app(step):
    world.browser.quit()


'''
def holamundo():
    print('holamundo')
    assert False, 'Falló la llamada a holamundo()'


def wait_for_work_to_be_done(function_to_execute):
    start_time = time.time()

    while True:
        try:
            function_to_execute()
            print('succesful, bye bye')
            return
        except (AssertionError, WebDriverException) as e:
            print('exception, try one more time')
            if time.time() - start_time > 10:
                raise e
            time.sleep(0.5)

wait_for_work_to_be_done(holamundo)
'''
