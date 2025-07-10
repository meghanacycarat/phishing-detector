import streamlit as st
import pandas as pd
import joblib
from urllib.parse import urlparse
import re

# --- Sci-Fi Theme Config ---
st.set_page_config(
    page_title="🚀 PhishGuard AI",
    page_icon="👾",
    layout="centered"
)

# Custom CSS for sci-fi look
st.markdown("""
<style>
    .stTextInput>div>div>input {
        background-color: #DFE2E2;
        color: #00FF41;
        border: 1px solid #00FF41;
    }
    .stButton>button {
        background: linear-gradient(to right, #0d47a1, #00bcd4);
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        padding: 10px 24px;
    }
    .stButton>button:hover {
        background: linear-gradient(to right, #00bcd4, #0d47a1);
    }
    .feature-table {
        font-family: monospace;
        background: #0E1117;
        border-radius: 10px;
        padding: 15px;
        border-left: 3px solid #00FF41;
    }
</style>
""", unsafe_allow_html=True)

# --- Load Model ---
@st.cache_resource
def load_model():
    return joblib.load('phishing_model.pkl')

model = load_model()

# --- Feature Extraction ---
def extract_features(url):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    parsed = urlparse(url)
    domain = parsed.netloc if parsed.netloc else parsed.path.split('/')[0]
    
    features = {
        'url_length': len(url),
        'domain_length': len(domain),
        'num_dots': url.count('.'),
        'num_hyphens': url.count('-'),
        'num_at': url.count('@'),
        'num_question': url.count('?'),
        'num_equal': url.count('='),
        'num_ampersand': url.count('&'),
        'num_slash': url.count('/'),
        'num_double_slash': url.count('//'),
        'has_ip': int(bool(re.match(r'\d+\.\d+\.\d+\.\d+', domain))),
        'is_https': int(url.startswith('https')),
        'has_port': int(':' in domain),
        'num_subdomains': domain.count('.') - 1 if '.' in domain else 0,
        'path_length': len(parsed.path),
        'has_php_ext': int(parsed.path.endswith('.php')),
        'has_exe_ext': int(parsed.path.endswith('.exe')),
    }
    return features

# --- Sci-Fi UI ---
st.title("👾 PhishGuard AI")
st.markdown("> *Defense system against interstellar phishing threats*")

with st.form("url_form"):
    url = st.text_input("Enter cosmic URL to scan:", placeholder="https://")
    submitted = st.form_submit_button("🚀 Launch Scan")
    
if submitted and url:
    with st.spinner("Analyzing quantum signature..."):
        try:
            # Extract features
            features = extract_features(url)
            features_df = pd.DataFrame([features])
            
            # Predict
            proba = model.predict_proba(features_df)[0][1]
            
            # Display result
            st.balloons() if proba < 0.2 else None
            if proba > 0.8:
                st.error(f"""
                ## ⚠️ ALERT: Phishing Detected
                **Confidence**: {proba:.0%}  
                **Threat Level**: Critical
                """)
            else:
                st.success(f"""
                ## ✅ Safe Passage Granted
                **Confidence**: {1-proba:.0%}  
                **Threat Level**: Minimal
                """)
            
            # Feature display (collapsible)
            with st.expander("📊 View Quantum Scan Report", expanded=True):
                st.markdown("### Feature Matrix")
                st.dataframe(features_df.T.style.background_gradient(cmap="RdYlGn_r"))
                
                st.markdown("### Threat Analysis")
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("URL Length", features['url_length'], 
                             delta="Suspicious" if features['url_length'] > 75 else "Normal")
                with col2:
                    st.metric("Subdomains", features['num_subdomains'],
                             delta="Danger" if features['num_subdomains'] > 3 else "Safe")
                
        except Exception as e:
            st.warning(f"🛑 System Error: {str(e)}")

# Footer
st.markdown("---")
st.caption("🔭 Powered by PhishGuard AI | Defense Protocol v2.6")