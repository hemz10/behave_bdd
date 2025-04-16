from behave import given, when, then


@given(u'we have behave installed')
def step_impl(context):
    context.a = 10     


@when(u'we implement a test')
def step_impl(context):
    context.a 


@then(u'behave will test it for us!')
def step_impl(context):
    pass


@when(u'we perform certain mathematical operations between {number1: d} and {number2: d}')
def step_impl(context, number1, number2):
    number1 = (number1)
    number2 = (number2)
    context.result = number1 + number2


@then(u'the result should be {result: d}')
def step_impl(context, result):
    assert context.result == (result), f"Expected {result}, but got {context.result}"

@when(u'we pass a table as a data through step enclosed in double')
def step_impl(context):
    for row in context.table:
        context.number1 =int(row['number1'])
        context.number2 =int(row['number2'])
        context.expectedresult = int(row['result'])


@then(u'behave should be able to read the table')
def step_impl(context):
   context.actual_result = context.number1 + context.number2
   assert context.actual_result == context.expectedresult, f"Expected {context.expectedresult}, but got {context.actual_result}"

@when(u'we pass a sentence as a data through step enclosed in triple quotes')
def step_impl(context):
    context.sentence = context.text


@then(u'behave should be able to read the sentence "{sentence}"')
def step_impl(context, sentence):
    if context.text:
        assert context.text == sentence