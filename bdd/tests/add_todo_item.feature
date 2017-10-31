Feature: Add To Do Item
  As a to-do app user
  I want to add an item to my to-do list
  In order to remember the things that I have to do

  Scenario: Add "Buy peacock feathers"
    Given I start the to-do app
    And I see "To-Do" as the page title
    And I see "To-Do" as the page header
    And I see "Enter a to-do item" as an invitation to add a to-do item
    When I fill "Buy peacock feathers" in the new to-do textbox
    And I press the Enter key
    Then I can see "Buy peacock feathers" in the list of to-do items
    And I finish the to-do app

  Scenario: Add "Use peacock feathers to make a fly"
    Given I start the to-do app
    And I see "To-Do" as the page title
    And I see "To-Do" as the page header
    And I see "Enter a to-do item" as an invitation to add a to-do item
    When I fill "Use peacock feathers to make a fly" in the new to-do textbox
    And I press the Enter key
    Then I can see "Use peacock feathers to make a fly" in the list of to-do items
    And I finish the to-do app
