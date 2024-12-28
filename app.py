import streamlit as st
from agents import agents  # Import agents from the agents.py file

# Streamlit App Configuration
st.set_page_config(page_title="StockBotX", layout="centered", initial_sidebar_state="expanded")

# App Header
st.title("🤑 StockBotX")
st.markdown("### Chat with the intelligent agent for stock insights!")

# Sidebar Information
with st.sidebar:
    st.header("ℹ️ About StockBotX")
    st.markdown(
        """
        StockBotX is your personal stock advisor, leveraging AI to provide insightful answers to your stock-related queries. 
        Ask about market trends, stock performance, and more!
        """
    )
    st.markdown("**👨‍💻 Built by [Shubham Prajapati](https://www.linkedin.com/in/shubhamprajapati7748/)**")
    st.markdown("Connect on [LinkedIn](https://www.linkedin.com/in/shubhamprajapati7748/) for collaborations!")

    # st.markdown("#### 🚀 Powered by AI | Built with ❤️ using Streamlit")

# Initialize conversation state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display conversation history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if user_input := st.chat_input("Type your query..."):
    # Add user message to the conversation
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message in the app
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate agent response
    try:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = agents.run(user_input, stream=False)
                st.markdown(response.content)

        # Save response to the conversation
        st.session_state.messages.append({"role": "assistant", "content": response.content})
    except Exception as e:
        with st.chat_message("assistant"):
            st.markdown("🚨 An error occurred while processing your request. Please try again.")
        st.error(f"Error: {str(e)}")

# Footer
st.markdown("---")
st.markdown("**Disclaimer**: StockBotX provides insights for educational purposes only and is not a substitute for professional financial advice.")
