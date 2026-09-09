from prompts.business_prompt import business_prompt
from prompts.recommendation_prompt import recommendation_prompt


def test_business_prompt():

    result = business_prompt.format(
        business_request="Sales are decreasing."
    )

    assert "Sales are decreasing." in result


def test_recommendation_prompt():

    result = recommendation_prompt.format(
        analysis="Sales have decreased because of customer retention issues."
    )

    assert "customer retention issues" in result