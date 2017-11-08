Feature: Add To Do Item
  As a to-do app user
  I want to add an item to my to-do list
  In order to remember the things that I have to do

#  Scenario: Add "Buy peacock feathers" to Edith to-do list
#    Given I start the to-do app as "Edith"
#    And I see "To-Do" as the page title
#    And I see "To-Do" as the page header
#    And I see "Enter a to-do item" as an invitation to add a to-do item
#    And layout and styling are correct
#    When I fill "Buy peacock feathers" in the new to-do textbox
#    And I press the Enter key
#    Then I can see "Buy peacock feathers" in the list of to-do items
#    And I finish the to-do app
#
#  Scenario: Add "Use peacock feathers to make a fly" to Edith to-do list
#    Given I start the to-do app as "Edith"
#    And I see "To-Do" as the page title
#    And I see "To-Do" as the page header
#    And I see "Enter a to-do item" as an invitation to add a to-do item
#    And layout and styling are correct
#    When I fill "Use peacock feathers to make a fly" in the new to-do textbox
#    And I press the Enter key
#    Then I can see "Use peacock feathers to make a fly" in the list of to-do items
#    And I finish the to-do app
#
#  Scenario: Add "" to Edith to-do list
#    Given I start the to-do app as "Edith"
#    And I see "To-Do" as the page title
#    And I see "To-Do" as the page header
#    And I see "Enter a to-do item" as an invitation to add a to-do item
#    And layout and styling are correct
#    When I fill "" in the new to-do textbox
#    And I press the Enter key
#    Then I can see the error The item cannot be empty
#    And I finish the to-do app
#
#  Scenario: Add "Buy Milk" to Francis to-do list
#    Given I start the to-do app as "Francis"
#    And I see "To-Do" as the page title
#    And I see "To-Do" as the page header
#    And I see "Enter a to-do item" as an invitation to add a to-do item
#    And layout and styling are correct
#    When I fill "Buy Milk" in the new to-do textbox
#    And I press the Enter key
#    Then I can see "Buy Milk" in the list of to-do items
#    And I finish the to-do app
#
#  Scenario: Add "Elemento cualquiera" two times to Francis to-do list
#    Given I start the to-do app as "Francis"
#    And I see "To-Do" as the page title
#    And I see "To-Do" as the page header
#    And I see "Enter a to-do item" as an invitation to add a to-do item
#    And layout and styling are correct
#    When I fill "Buy Milk" in the new to-do textbox
#    And I press the Enter key
#    And I fill the same item one more time in the new to-do textbox
#    And I press the Enter key
#    Then I can see the error You have already got this in your list
#    And I finish the to-do app

  Scenario: Add "Elemento cualquiera" two times to Edith to-do list and after add a correct input
    Given I start the to-do app as "Francis"
    And I see "To-Do" as the page title
    And I see "To-Do" as the page header
    And I see "Enter a to-do item" as an invitation to add a to-do item
    And layout and styling are correct
    When I fill "Buy Milk" in the new to-do textbox
    And I press the Enter key
    And I fill the same item one more time in the new to-do textbox
    And I press the Enter key
    Then I can see the error You have already got this in your list
    And I fill "Hola correcto" in the new to-do textbox
    Then the error message is closed
    And I finish the to-do app