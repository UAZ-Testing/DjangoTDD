# -*- coding: utf-8 -*-
import math
import random

from lettuce import step
from lettuce import world
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time
import os

import sys

reload(sys)
sys.setdefaultencoding("utf-8")


################################## Steps #######################################


@step(u'Given I start the to-do app as "([^"]*)"')
def given_i_start_the_to_do_app_as_group1(step, usuario):
    world.browser = webdriver.Firefox()
    # world.browser.get('http://localhost:8000/lists/%s' % (usuario))
    if usuario == 'Edith':
        list_id = '1'
    else:
        list_id = '2'
    staging_server = os.environ.get('STAGING_SERVER')
    if staging_server:
        world.server_url = 'http://' + staging_server
    else:
        world.server_url = 'http://localhost:8000'

    world.browser.get('%s/lists/%s/' % (world.server_url, list_id))
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
    # world.inputbox = world.browser.find_element_by_id('id_new_item')
    world.inputbox = get_item_input_box()

    obtained = world.inputbox.get_attribute('placeholder')

    assert expected == obtained, 'El placeholder esperado es "%s" y el ' \
                                 'obtenido "%s"' % (expected, obtained)


@step(u'When I fill "([^"]*)" in the new to-do textbox')
def when_i_fill_group1_in_the_new_to_do_textbox(step, to_do_item):
    i_fill_item_in_the_new_to_do_textbox(to_do_item)


@step(u'And I press the Enter key')
def and_i_press_the_enter_key(step):
    world.inputbox.send_keys(Keys.ENTER)
    time.sleep(1)


@step(u'Then I can see "([^"]*)" in the list of to-do items')
def then_i_can_see_group1_in_the_list_of_to_do_items(step, to_do_item):
    i_can_see_item_in_the_list_of_to_do_items(to_do_item)


@step(u'And I finish the to-do app')
def and_i_finish_the_to_do_app(step):
    world.browser.quit()


@step(u'And layout and styling are correct')
def and_layout_and_styling_are_correct(step):
    world.browser.set_window_size(1024, 768)

    inputbox = get_item_input_box()

    real_center = inputbox.location['x'] + inputbox.size['width'] / 2
    expected_center = 512

    assert areAlmostEqual(real_center, expected_center, 10), \
        'El centro esperado es %f y el real es %f' % (
            expected_center, real_center)


@step(u'And I fill the same item one more time in the new to-do textbox')
def and_i_fill_the_same_item_one_more_time_in_the_new_to_do_textbox(step):
    time.sleep(1)
    world.inputbox = get_item_input_box()
    world.inputbox.send_keys(world.last_item_inserted)


@step(u'Then I can see the error You have already got this in your list')
def then_i_can_see_the_error_you_ve_already_got_this_in_your_list(step):
    wait_for(lambda: find_repeated_item_error())


@step(u'And I fill "([^"]*)" in the new to-do textbox')
def and_i_fill_group1_in_the_new_to_do_textbox(step, to_do_item):
    world.inputbox = get_item_input_box()
    i_fill_item_in_the_new_to_do_textbox(to_do_item)


@step(u'Then the error message is closed')
def then_the_error_message_is_closed(step):
    assert not error_box_is_shown(), 'Los errores tenían que ocultarse'


@step(u'And I can see "([^"]*)" in the list of to-do items')
def and_i_can_see_group1_in_the_list_of_to_do_items(step, to_do_item):
    i_can_see_item_in_the_list_of_to_do_items(to_do_item)


@step(u'Then I can see the error The item cannot be empty')
def then_i_can_see_the_error_the_item_cannot_be_empty(step):
    wait_for(lambda: findEmptyItemError())


############################## Steps helpers ###################################
def i_fill_item_in_the_new_to_do_textbox(to_do_item):
    if len(to_do_item) > 0:
        to_do_item = to_do_item + ' ' + str(random.randint(1000, 9999))
    world.inputbox.send_keys(to_do_item)
    world.last_item_inserted = to_do_item


def i_can_see_item_in_the_list_of_to_do_items(to_do_item):
    table = world.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')

    assert any(to_do_item in row.text for row in rows), \
        'No se encuentra "%s" en la lista de To-Do' % (to_do_item)


################################# Helpers ######################################


def get_item_input_box():
    return world.browser.find_element_by_id('id_text')


def error_box_is_shown():
    try:
        error = world.browser.find_element_by_css_selector('.has-error')
        return error.is_displayed()
    except:
        return False


def find_repeated_item_error():
    error_buscado = "You've already got this in your list"
    try:
        errors = world.browser.find_element_by_css_selector('.has-error').text
        assert error_buscado in errors, \
            'No se encuentra "%s" en "%s"' % (error_buscado, errors)
    except:
        assert False, 'No se desplegó ningún error'


def findEmptyItemError():
    try:
        error_msg = world.browser.find_element_by_css_selector(
            '#id_text:invalid')
        assert True
    except:
        assert False, 'No se desplegó el error en el form'


def areAlmostEqual(a, b, difference):
    return abs(a - b) <= difference


def wait_for(fn):
    start_time = time.time()
    while True:
        try:
            return fn()
        except (AssertionError, WebDriverException) as e:
            if time.time() - start_time > 10:
                raise e
            time.sleep(0.5)
