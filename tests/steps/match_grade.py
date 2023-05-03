from behave import *
from hamcrest import is_, assert_that

import pyard.mg


@given("The first typing for a recipient is {r_type1}")
def step_impl(context, r_type1):
    context.r_type1 = r_type1


@step("The second typing for a recipient is {r_type2}")
def step_impl(context, r_type2):
    context.r_type2 = r_type2


@step("The first typing for a donor is {d_type1}")
def step_impl(context, d_type1):
    context.d_type1 = d_type1


@step("The second typing for a donor is {d_type2}")
def step_impl(context, d_type2):
    context.d_type2 = d_type2


@when("We calculate the research match grade")
def step_impl(context):
    rmg_1 = pyard.mg.research_mg(context.r_type1, context.d_type1)
    rmg_2 = pyard.mg.research_mg(context.r_type2, context.d_type2)
    context.rmg = f"{rmg_1}:{rmg_2}"


@then("The research match grade is {dna_mg}")
def step_impl(context, dna_mg):
    assert_that(context.rmg, is_(dna_mg))
