import streamlit as st

def lock():
    st.session_state.lock = True

def validated_submission():
    st.write("Provide three non-negative integers that sum to 10")
    a = st.number_input("A", value=0, min_value=0, max_value=10, disabled=st.session_state.lock, key=f"A_{st.session_state.attempt}")
    b = st.number_input("B", value=0, min_value=0, max_value=10, disabled=st.session_state.lock, key=f"B_{st.session_state.attempt}")
    c = st.number_input("C", value=0, min_value=0, max_value=10, disabled=st.session_state.lock, key=f"C_{st.session_state.attempt}")
    submit = st.button("Submit", on_click=lock)
    if "status" in st.session_state:
        st.error(st.session_state.status)
    if submit:
        # Check that all fields are filled
        if a is None or b is None or c is None:
            st.session_state.status = "A value is missing. Please fill in all fields."
            st.session_state.lock = False

        # Validate sum
        elif a + b + c != 10:
            st.session_state.status = "The sum of values is not 10. Please update the values."
            st.session_state.lock = False

        # Accept the submission
        else:
            st.session_state.A = a
            st.session_state.B = b
            st.session_state.C = c
            st.session_state.lock = False
            if "status" in st.session_state:
                del st.session_state.status
            st.session_state.attempt += 1


def delete_submission():
    del st.session_state.A
    del st.session_state.B
    del st.session_state.C

if "attempt" not in st.session_state:
    st.session_state.attempt = 1
if "lock" not in st.session_state:
    st.session_state.lock = False

st.write("Lorem ipsum")

validated_submission()

if "A" in st.session_state:
    st.write("Submitted answers")
    st.write(f"A = {st.session_state.A}")
    st.write(f"B = {st.session_state.B}")
    st.write(f"C = {st.session_state.C}")

st.button("Clear data", on_click=delete_submission)

st.write("Lorem ipsum")