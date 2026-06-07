import streamlit as st
import requests as rq
s_url=""
weather_tab,budget_tab,places_tab=st.tabs(["Weather","Budget","Famous Places"])

with weather_tab:
    st.title("Weather Details")
    city=st.text_input("Enter City")
    question=st.text_input("Ask About Weather",placeholder="should i have carry umbrella today?")
    if st.button("Get Weather Advice"):
        res=rq.post(
            f"{s_url}/weather_tool_call",
            params={
                "city":city,
                "question":question
            }
        )
        obj = res.json()
        st.success(obj["messages"][-1]["content"])

with budget_tab:

    st.title("Travel Budget Planner")

    source_city = st.text_input(
        "Source City"
    )

    destination_city = st.text_input(
        "Destination City"
    )

    question = st.text_input(
        "Ask Budget Question",
        placeholder="What is the total travel cost?"
    )

    if st.button("Get Budget"):

        res = rq.post(
            f"{s_url}/budget_tool_calling",
            params={
                "source_city": source_city,
                "destination_city": destination_city,
                "question": question
            }
        )

        obj = res.json()

        st.success(
            obj["messages"][-1]["content"]
        )

with places_tab:
    st.title("Must Vist Places")
    f_city=st.text_input("Enter City you want to tarvel")
    f_question=st.text_input("Ask Your Question about that city")
    if st.button("Find Places"):
        res=rq.post(
    f"{s_url}/places_tool_calling",
    params={
        "city": f_city,
        "question": f_question
    }
)
        obj=res.json()
        st.success(
    obj["messages"][-1]["content"]
)

