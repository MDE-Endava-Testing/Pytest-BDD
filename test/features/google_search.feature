Feature: Google Search
  As user,
  I want to search in Google.

  Scenario: Search for a word in Google
    Given the user goes to Google
    When he searches for "translator"
    Then one of the results should contain "Traductor"