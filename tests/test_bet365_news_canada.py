#test_bet365_news.py

from pytest_bdd import scenarios
from step_definitions.test_bet365_news_canada_steps import *

#define the feature file(s) to be used
scenarios("../features/bet365_news_canada.feature")