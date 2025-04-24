Feature: Filtering products by sale status

  Scenario: User can filter by sale status Out of Stocks
    Given the user is on the main page
    When the user logs in
    And the user clicks on "Off-plan" in the menu
    Then the correct page should open
    When the user filters by "Out of Stocks"
    Then all listed products should be marked as "Out of Stocks"


