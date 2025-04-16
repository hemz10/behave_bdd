Feature: showing off behave

	Scenario: run a simple test
		Given we have behave installed
		When we implement a test
		Then behave will test it for us!
    @wip
	Scenario Outline: Example for Scenario Outline with multiple columns that demonstarates addition of numbers and verification of the result
		Given we have behave installed
		When we perform certain mathematical operations between <number1> and <number2>
		Then the result should be <result>

		Examples:
			| number1 | number2 | result |
			| 2       | 3       | 5      |
			| 4       | 5       | 9      |
			| 10      | 20      | 30     |
			| 100     | 200     | 300    |

	Scenario: Passing a table as a data through step enclosed in triple quotes
		Given we have behave installed
		When we pass a table as a data through step enclosed in double
			| number1 | number2 | result |
			| 2       | 3       | 5      |
			| 4       | 5       | 9      |
		Then behave should be able to read the table

	
    Scenario: Passing a sentence as a data through step enclosed in triple double quotes and in double quotes
		Given we have behave installed
		When we pass a sentence as a data through step enclosed in triple quotes
		"""
		This is a sentence that is passed as a data through step
		"""
		Then behave should be able to read the sentence "This is a sentence that is passed as a data through step"