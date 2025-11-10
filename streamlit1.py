import streamlit as st
import google.generativeai as genai

# --- App Title ---
st.title("💬 Gemini Text Generator")
st.write("Experiment with **temperature** and **max tokens** to see how Gemini's creativity changes!")

# --- API Key Input ---
api_key = st.text_input("🔑 Enter your Gemini API Key:", type="password")

if api_key:
    # Configure Gemini
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-pro")

    # --- User Inputs ---
    prompt = st.text_area("🧠 Enter your prompt:", "Write a haiku about the sunrise.")
    temperature = st.slider("🎨 Creativity (temperature)", 0.0, 1.0, 0.7, 0.1)
    max_tokens = st.slider("🧾 Max Output Tokens", 50, 5000, 200, 50)

    # --- Generate Button ---
    if st.button("✨ Generate"):
        with st.spinner("Generating response..."):
            try:
                response = model.generate_content(
                    prompt,
                    generation_config={
                        "temperature": temperature,
                        "max_output_tokens": max_tokens
                    }
                )

                # Safe response handling
                if response.candidates and response.candidates[0].content.parts:
                    st.subheader("📝 Gemini's Response:")
                    st.write(response.text)
                else:
                    st.warning("No text generated — try increasing token limit or adjusting temperature.")

            except Exception as e:
                st.error(f"⚠️ Error: {e}")
else:
    st.info("Please enter your API key to start.")
