import streamlit as st

from workflows.basic_workflow import workflow


st.set_page_config(
    page_title="AI Agent Coordination Engine",
    page_icon="🤖"
)


def extract_text(response):
    """
    Extract plain text from Gemini/LangChain response content.
    """

    if isinstance(response, str):
        return response

    if isinstance(response, list):
        texts = []

        for item in response:
            if isinstance(item, dict) and item.get("type") == "text":
                texts.append(item.get("text", ""))

        return "\n".join(texts)

    return str(response)


st.title("🤖 AI Agent Coordination & Decision Engine")

st.write(
    "Module 1 - Agent Foundation Development"
)

request = st.text_area(
    "Enter your business request:"
)

if st.button("Analyze Business Request"):

    if not request.strip():

        st.warning("Please enter a business request.")

    else:

        with st.spinner("Agents are processing your request..."):

            result = workflow.invoke({
                "request": request,
                "analysis": "",
                "recommendation": ""
            })

        st.subheader("Business Analysis")

        st.markdown(
            extract_text(result["analysis"])
        )

        st.subheader("Recommendation")

        st.markdown(
            extract_text(result["recommendation"])
        )