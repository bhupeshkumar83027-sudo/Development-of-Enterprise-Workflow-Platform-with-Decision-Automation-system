import streamlit as st

from workflows.basic_workflow import workflow


st.set_page_config(
    page_title="AI Agent Coordination & Decision Engine",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 AI Agent Coordination & Decision Engine")

st.subheader("Module 1 - Agent Foundation Development")

st.write(
    "Multi-agent business analysis and recommendation system"
)


business_request = st.text_area(
    "Enter your business request:",
    placeholder=(
        "Example: My company is experiencing declining sales. "
        "Analyze the problem and suggest what should be investigated."
    ),
    height=150
)


if st.button("🚀 Analyze Business Request"):

    if not business_request.strip():

        st.warning(
            "Please enter a business request."
        )

    else:

        try:

            with st.spinner(
                "AI agents are processing your request..."
            ):

                result = workflow.invoke(
                    {
                        "request": business_request,
                        "analysis": "",
                        "recommendation": ""
                    }
                )

            st.success(
                "Business request successfully processed!"
            )

            st.divider()

            st.header("🔍 Business Analysis")

            st.write(
                result["analysis"]
            )

            st.divider()

            st.header("💡 Recommendation")

            st.write(
                result["recommendation"]
            )

        except Exception as e:

            st.error(
                f"An error occurred: {str(e)}"
            )