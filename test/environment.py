def before_feature(context, feature):
    # Set up resources specific to a feature
    print(f"Setting up environment for feature: {feature.name}")

def after_feature(context, feature):
    # Clean up resources specific to a feature
    print(f"Cleaning up after feature: {feature.name}")

def before_scenario(context, scenario):
    # Set up resources specific to a scenario
    print(f"Setting up for scenario: {scenario.name}")
    context.scenario_var = "Scenario-specific Data"

def after_scenario(context, scenario):
    # Clean up resources specific to a scenario
    print(f"Cleaning up after scenario: {scenario.name}")

def before_step(context, step):
    # Set up before a step is executed
    print(f"Before step: {step.name}")

def after_step(context, step):
    # Tear down after a step is executed
    print(f"After step: {step.name}")

def before_tag(context, tag):
    # Set up resources specific to a tag
    print(f"Setting up for tag: {tag}")

def after_tag(context, tag):
    # Clean up resources specific to a tag
    print(f"Cleaning up after tag: {tag}")