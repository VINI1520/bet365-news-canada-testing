Feature: Testing the news from bet365 website
    Scenario: Verify the display of standard news categories
        Given I am on the bet365 website
        Then I should see the following standard categories:
            | Category            |
            | NBA                 |
            | MLB                 |
            | NFL                 |
            | GOLF                |
            | SOCCER              |
            | COLLEGE SPORTS      |
            | TENNIS              |
            | MORE SPORTS         |

    Scenario: Verify the display of first news articles by category
        Given I am on the bet365 website
        Then I should see the headline of the first news article for each category:
            | Category            |
            | NBA                 |
            | MLB                 |
            | NFL                 |
            | GOLF                |
            | SOCCER              |
            | COLLEGE SPORTS      |
            | TENNIS              |
            | MORE SPORTS         |