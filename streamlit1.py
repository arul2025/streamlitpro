import streamlit as st
import google.generativeai as genai

# 🔐 Configure Gemini with your API key from Streamlit Secrets
genai.configure(api_key=st.secrets["AIzaSyDj1wNAWvAB5GcbKa657dUGeXlnIMLGR88"])

# ---- Streamlit App UI ----
st.set_page_config(page_title="Gemini Chat", page_icon="💬", layout="centered")

st.title("💬 Gemini AI Chatbot")
st.write("Ask anything and get a response from Google's Gemini model!")

# ---- User Input ----
user_input = st.text_area("Enter your question or prompt:", height=150)

# ---- Generate Response ----
if st.button("Generate Response"):
    if user_input.strip():
        try:
            # Use Gemini model (choose one)
            model = genai.GenerativeModel("gemini-2.0-pro")
            response = model.generate_content(user_input)

            st.subheader("💡 Response:")
            st.write(response.text)

        except Exception as e:
            st.error(f"⚠️ An error occurred: {e}")
    else:
        st.warning("Please enter a prompt before clicking Generate.")

# ---- Footer ----
st.markdown("---")
st.caption("Built with ❤️ using Streamlit and Google Gemini API")
