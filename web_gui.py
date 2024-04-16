import streamlit as st
import functions

actions=functions.get_act()

def add_actions():
    action=st.session_state["adding"] + "\n"
    if action not in actions:
        actions.append(action)
        functions.set_act(actions)
        st.session_state["adding"]=""

st.title("first app")
st.subheader("subheading")
st.text("this list contains list of actions to complete")

for index,action in enumerate(actions):
    checkbox=st.checkbox(action, key=action)
    if checkbox:
        actions.pop(index)
        functions.set_act(actions)
        del st.session_state[action]
        st.rerun()

st.text_input(label="", placeholder="add a new action",
              on_change=add_actions ,key="adding")

st.session_state
