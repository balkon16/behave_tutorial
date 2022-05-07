Feature: get information on transactions

  Scenario: Open the webpage with information on transactions
    Given a set of transactions
      | transaction ID | name      | status      |
      | 1              | groceries | completed   |
      | 23             | shoes     | in progress |
      | 44             | rent      | completed   |
    When I count the number of transactions by type
    Then I get 2 transactions with a status "completed"
    Then I get 1 transaction with a status "in progress"

#  Given: I open the webpage with information on the transaction no.