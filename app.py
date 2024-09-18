import streamlit as st
from src.module import generate_blog

st.set_page_config("Blog Generator")
PURPOSE_OPTIONS = ['Common people', 'Data Scientists', 'Software Engineers', 'Teachers', 'Body Builders']

# front end
st.header("Blog Generator")
topic = st.text_input("Enter the blog topic.")
col1, col2 = st.columns(2)
with col1:
    no_words = st.text_input("Number of words.")
with col2:
    purpose = st.selectbox("Create blog for whom?", options=PURPOSE_OPTIONS, index=0)
submit_btn = st.button("Generate", type='primary')
st.divider()


# process handling
if submit_btn:
    if (topic != "") and (no_words != ""):
        with st.spinner("Generating.."):
            blog, time_taken = generate_blog(topic, no_words, purpose)
            st.write(blog)
            st.write(f"Time taken: {time_taken}")

    else:
        st.error("Please enter the details.")