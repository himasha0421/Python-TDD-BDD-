Feature: Search for pets by category

As a customer who is looking to buy a pet 
I need to search pets by it's category
So that I can only see the pets that I'm intrested in buying

Background:
    Given following pets should be in the database
      | name  | category | available |
      | Fido  | dog      | True      |
      | Kitty | cat      | True      |
      | Leo   | lion     | Fasle     |
        

Scenario: Search for dogs
    Given I am on the "Home Page"
    When I set the "Category" to "dog"
    And I click the "Search" button
    Then I should see the "Success" message
    And I should see "Fido" as my result
    But I should not see "Kitty" as my result
    And I should not see "Leo" as my result