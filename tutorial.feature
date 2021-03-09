Feature: Checking if the Cosmos UI works

    Scenario: The Cosmos UI returns a 200 response
        Given I've configured my http client with my dev cert
        When I request the Cosmos homepage
        Then the I should get a 200 response
