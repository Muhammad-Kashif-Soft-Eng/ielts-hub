import streamlit as st
import time

# --- CONFIGURATION ---
st.set_page_config(page_title="IELTS AI Prep", page_icon="🎓", layout="wide")

# --- MOCK API FUNCTION ---
def call_grok_api(prompt):
    return "This is a placeholder for the AI-generated evaluation and feedback."

# --- NAVIGATION ---
st.sidebar.title("🎓 IELTS AI Prep")
menu = ["Dashboard", "Listening", "Reading", "Writing", "Speaking", "Settings"]
choice = st.sidebar.radio("Navigation", menu)

# --- DASHBOARD ---
if choice == "Dashboard":
    st.title("Welcome back, Muhammad.")
    st.subheader("Your Target Band: 8.5")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Listening", "7.5", "+0.5")
    col2.metric("Reading", "8.0", "0")
    col3.metric("Writing", "6.5", "+1.0")
    col4.metric("Speaking", "7.0", "-0.5")
    col5.metric("Overall Est.", "7.5", "+0.5")
    
    st.divider()
    
    colA, colB = st.columns(2)
    with colA:
        st.write("### 📉 Weak Areas Identified")
        st.info("**Listening:** Multiple Choice\n\n**Reading:** True/False/Not Given\n\n**Writing:** Task Response\n\n**Speaking:** Fluency")
    
    with colB:
        st.write("### 💡 Recommended Practice")
        st.success("Your Reading performance is strong, but your True/False/Not Given accuracy is low. Click below to practice this question type next.")
        st.button("Start Recommended Practice")

# --- LISTENING MODULE ---
elif choice == "Listening":
    st.title("🎧 Listening Practice - Section 2")
    st.write("**Topic:** University Orientation | **Difficulty:** Advanced")
    
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3") 
    st.divider()
    
    st.write("### Questions 11 - 13")
    st.radio("11. The main purpose of the meeting is:", ["A. To discuss housing", "B. To introduce campus facilities", "C. To pay tuition fees", "D. To register for classes"], index=None)
    st.text_input("12. The student should first visit: (No more than THREE words)")
    
    if st.button("Submit Answers"):
        with st.spinner("AI Evaluating..."):
            time.sleep(1)
            st.success("Score: 1/2")
            st.write("### Feedback")
            st.write("**Q12. Your Answer:** Library")
            st.write("**Correct Answer:** Student Services Office")
            st.write("**Why:** The speaker initially mentions the library but clarifies that students must visit Student Services first.")

# --- READING MODULE ---
elif choice == "Reading":
    st.title("📖 Reading Practice")
    st.write("**Time Remaining:** 42:18")
    
    col_text, col_q = st.columns([1.5, 1])
    
    with col_text:
        st.write("### Passage: The Evolution of Renewable Energy")
        st.container(height=500, border=True).write("""
        (Mock Passage Text)
        The transition to renewable energy sources has been a major focus of the 21st century. 
        Solar power, in particular, has seen exponential growth due to falling costs in photovoltaic cell manufacturing. 
        However, grid storage remains a significant challenge for policymakers and engineers alike...
        """)
        
    with col_q:
        st.write("### Questions 1 - 3")
        st.radio("1. The main driver of solar power growth is:", ["A. Government policy", "B. Falling manufacturing costs", "C. Grid storage improvements"], index=None)
        st.radio("2. The primary challenge mentioned is grid storage.", ["True", "False", "Not Given"], index=None)
        
        if st.button("Submit Reading Test"):
            st.info("Evaluation logic will be implemented here.")

# --- WRITING MODULE ---
elif choice == "Writing":
    st.title("✍️ Writing Practice")
    task = st.selectbox("Select Task", ["Task 1 (Academic)", "Task 2 (Essay)"])
    
    if task == "Task 2 (Essay)":
        st.write("**Prompt:** Some people believe that technology has made our lives too complex, while others believe it has made our lives simpler. Discuss both views and give your opinion.")
        
        user_text = st.text_area("Write your essay here:", height=300)
        word_count = len(user_text.split()) if user_text else 0
        
        st.write(f"**Word Count:** {word_count} / 250 minimum")
        
        if st.button("Submit for AI Evaluation"):
            with st.spinner("Grok AI is evaluating your writing..."):
                time.sleep(2)
                st.write("### 📊 AI Evaluation")
                st.write("**Estimated Band: 7.0**")
                st.write("- Task Response: 7.0")
                st.write("- Coherence & Cohesion: 7.5")
                st.write("- Lexical Resource: 6.5")
                st.write("- Grammar: 7.0")
                st.info("**AI Feedback:** " + call_grok_api(user_text))

# --- SPEAKING MODULE ---
elif choice == "Speaking":
    st.title("🎙️ Speaking Practice - Part 2")
    
    st.write("### Prompt")
    st.info("**Describe a useful skill you learned.**\nYou should say:\n- What it was\n- How you learned it\n- Why it is useful\n\n*You have 1 minute to prepare and 2 minutes to speak.*")
    
    audio_value = st.audio_input("Record your answer")
    
    if audio_value:
        st.audio(audio_value)
        if st.button("Submit Recording"):
            with st.spinner("Transcribing and Evaluating..."):
                time.sleep(2)
                st.write("### 📊 AI Evaluation")
                st.write("**Estimated Band: 7.5**")
                st.warning("**Feedback:** You used the filler word 'you know' 4 times. Try replacing fillers with short pauses.")

# --- SETTINGS / API KEYS ---
elif choice == "Settings":
    st.title("⚙️ Settings")
    st.write("Configure your external providers here.")
    
    st.text_input("Grok API Key", type="password")
    st.text_input("TTS Provider API Key", type="password")
    
    if st.button("Save Settings"):
        st.success("Settings saved for this session.")
