import streamlit as st
import google.generativeai as genai
import os
import time

# --- 1. SETUP & PAGE CONFIG ---
st.set_page_config(page_title="Agroww | Enterprise Audit", layout="wide", page_icon="🌾")

# --- 2. ADVANCED CSS ANIMATIONS & BACKGROUND ---
st.markdown("""
<style>
    /* === MAIN BACKGROUND CHANGE === */
    .stApp {
        /* We use a linear-gradient overlay to fade the image so text is readable */
        background-image: 
            linear-gradient(to bottom, rgba(240, 249, 240, 0.85), rgba(255, 255, 255, 0.95)),
            url('data:image/jpeg;base64,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'); /* High-res Farm Photo */
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: fixed; /* Keeps bg still while scrolling */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* === ANIMATION DEFINITIONS === */
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes pulse-red {
        0% { box-shadow: 0 0 0 0 rgba(198, 40, 40, 0.4); }
        70% { box-shadow: 0 0 0 10px rgba(198, 40, 40, 0); }
        100% { box-shadow: 0 0 0 0 rgba(198, 40, 40, 0); }
    }

    /* === CARD STYLING (Made slightly translucent) === */
    .audit-card {
        background-color: rgba(255, 255, 255, 0.95); /* Slight transparency */
        padding: 25px;
        border-radius: 12px;
        border-top: 4px solid #2e7d32; /* Sahyadri Green */
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        animation: slideUp 0.6s ease-out;
        transition: transform 0.2s, box-shadow 0.2s;
        backdrop-filter: blur(5px); /* Modern frosted glass effect */
    }
    
    /* Hover Effect: Lift Card */
    .audit-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }

    /* === RISK BADGES === */
    .badge-critical {
        background-color: #ffebee;
        color: #c62828;
        padding: 8px 16px;
        border-radius: 50px;
        font-weight: 700;
        border: 1px solid #c62828;
        display: inline-block;
        animation: pulse-red 2s infinite;
    }
    
    .badge-safe {
        background-color: #e8f5e9;
        color: #2e7d32;
        padding: 8px 16px;
        border-radius: 50px;
        font-weight: 700;
        border: 1px solid #2e7d32;
        display: inline-block;
    }

    /* === CUSTOM BUTTON === */
    div.stButton > button {
        background-color: #1b5e20; 
        color: white; 
        border-radius: 8px;
        height: 50px;
        font-size: 18px;
        font-weight: 600;
        border: none;
        transition: background-color 0.3s, transform 0.2s;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    div.stButton > button:hover {
        background-color: #144a17;
        box-shadow: 0 6px 12px rgba(0,100,0,0.3);
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)

# --- 3. API SETUP ---
os.environ["GEMINI_API_KEY"] = "Google API key here"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-2.5-flash')

# --- 4. SIDEBAR ---
with st.sidebar:
    st.image("https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTfDLniWVwSxay7aD_Tpcyl5YCXcmfZSiNxUg148twEAU2dxTuB", width=100)
    st.markdown("## ****TechSprint AI Hack '25****")
    st.caption("v3.1 Pro | Visual Update")
    st.divider()
    st.markdown("### Tech Titan ")
    st.info("**Participants:** Kaivalya Thombare and Riya Patrao\n **Status:** Online 🟢")

# --- 5. MAIN HEADER ---
col_head1, col_head2 = st.columns([3, 1])
with col_head1:
    st.title("🚜 Intelligent Contract Audit")
    st.markdown("AI-Powered Legal breakdown system.")
with col_head2:
    st.markdown("""
        <div style="text-align: right; padding: 10px;">
            <span style="color: grey; font-size: 12px;">SYSTEM LATENCY</span><br>
            <span style="color: green; font-weight: bold;">⚡ 12ms (Excellent)</span>
        </div>
    """, unsafe_allow_html=True)

# --- 6. INPUT SECTION ---
st.markdown('<div class="audit-card">', unsafe_allow_html=True)
c1, c2 = st.columns([2, 1])
with c1:
    st.subheader("📄 Contract Input")
    upload_type = st.radio("Input Source:", ["📂 Load Sample PDF", "📝 Manual Entry"], horizontal=True)
    
    if upload_type == "📝 Manual Entry":
        user_text = st.text_area("Paste Clause:", height=150)
    else:
        st.info("ℹ️ Demo Mode: Pre-loading 'Trap' Contract...")
        user_text = """
        SECTION 5: FORCE MAJEURE. In the event of unseasonal rain, hail, or drought, the Buyer reserves the right 
        to cancel this entire agreement without penalty. The Farmer bears 100% of the cost for any crop spoilage.
        SECTION 6: PAYMENT. Payment will be processed 60 days after quality check.
        """
with c2:
    st.write("")
    st.write("")
    st.write("")
    analyze_btn = st.button("🚀 INITIATE SCAN", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 7. ANALYSIS LOGIC ---
if analyze_btn:
    if not user_text:
        st.error("⚠️ System Error: No Input Data Found.")
    else:
        # --- LOADING SEQUENCE ---
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        time.sleep(0.5)
        my_bar.progress(30, text="📡 Connecting to Legal Database...")
        time.sleep(0.5)
        my_bar.progress(60, text="🔍 Scanning for Hidden Clauses...")
        
        try:
            prompt = f"""
            You are a senior agricultural lawyer. Analyze this contract text: "{user_text}"
            
            Structure your answer exactly like this:
            RISK_LEVEL | SCORE
            SUMMARY
            POINT 1
            POINT 2
            POINT 3
            
            RISK_LEVEL must be 'CRITICAL RISK', 'MODERATE RISK', or 'SAFE'.
            SCORE is 0-100.
            SUMMARY is 2 sentences max.
            POINTS are the specific dangerous phrases and why.
            """
            response = model.generate_content(prompt)
            
            my_bar.progress(100, text="✅ Analysis Complete.")
            time.sleep(0.3)
            my_bar.empty()

            # Parsing
            lines = response.text.strip().split('\n')
            header = lines[0].split('|')
            risk_level = header[0].strip()
            score = int(header[1].strip())
            summary = lines[1].strip() if len(lines) > 1 else "Done."
            details = [l for l in lines[2:] if l.strip()]

            # --- DISPLAY RESULTS ---
            if score < 50:
                badge_class = "badge-critical"
                icon = "🚨"
            else:
                badge_class = "badge-safe"
                icon = "✅"

            st.markdown(f"""
            <div class="audit-card" style="border-left: 10px solid {'#c62828' if score < 50 else '#2e7d32'};">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <span class="{badge_class}">{icon} {risk_level}</span>
                        <h1 style="margin: 10px 0 0 0; font-size: 3em;">{score}<span style="font-size: 0.4em; color: grey;">/100 Safety Score</span></h1>
                    </div>
                    <div style="text-align: right;">
                        <h3 style="margin:0; color: grey;">ESTIMATED RISK</h3>
                        <h2 style="margin:0; color: {'#c62828' if score < 50 else '#2e7d32'};">{'High' if score < 50 else 'Low'} Financial Exposure</h2>
                    </div>
                </div>
                <hr style="margin: 20px 0; border-top: 1px solid #eee;">
                <p style="font-size: 1.2em; color: #444;"><b>📢 Executive Summary:</b> {summary}</p>
            </div>
            """, unsafe_allow_html=True)

            col_d1, col_d2 = st.columns([2, 1])
            
            with col_d1:
                st.markdown('<div class="audit-card">', unsafe_allow_html=True)
                st.subheader("🔍 Clause-by-Clause Breakdown")
                for detail in details:
                    clean = detail.replace("POINT 1", "").replace("POINT 2", "").replace("POINT 3", "").strip()
                    if clean:
                        st.markdown(f"""
                        <div style="padding: 10px; border-bottom: 1px solid #eee;">
                            <span style="color: #c62828; font-weight: bold;">⚠️ FLAGGED:</span> {clean}
                        </div>
                        """, unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            with col_d2:
                st.markdown('<div class="audit-card">', unsafe_allow_html=True)
                st.subheader("💡 Recommendation")
                st.success("Negotiate 'Force Majeure'.")
                st.warning("Request 'Advance Payment'.")
                st.info("Ask for 'Liability Sharing'.")
                st.markdown('</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Analysis Failed: {e}")

