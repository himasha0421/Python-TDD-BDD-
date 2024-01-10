TDD / BDD driven software development

general software testing levels

1. unit tests -> test to verify each single module works as espected
2. integration testing -> combine individual components and test as a group
3. system test -> test complete test for vulnerabilities , compliance issues ect.
4. acceptance test -> user acceptence tests

Traditional software release cycle

1. Development --> unit tests
2. Build --> unit tests
3. package repo 
4. Test --> component test / integration test / performance test
5. Stage --> performance test / user acceptance test
6. Prod

difference between TDD & BDD

BDD 
* Focus on the behaviour of the system from the outside
* works great for integration testing
* use syntax both developers stackholders can easiliy understand

TDD
* focusses on how system works from inside
* test driven the design


TDD workflow

RED -> write test case that fails 
GREEN -> write code to make it pass
REFACTOR -> improve the code quality

* iterate over the above development cycle

Tools for python development testing

PyUnit
Pytest
Doctest
Rspec
Nose