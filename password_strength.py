import re
import streamlit as st # Streamlit library for building web apps in Python 

# Page configuration
st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔒",
    layout="centered"
)

# Custom CSS for dark theme and better UI
st.markdown("""
    <style>
        /* Dark theme colors */
        :root {
            --background-color: #1a1b1e;
            --text-color: #ffffff;
            --input-bg: #2d2e33;
            --weak-color: #ffa500;
            --error-color: #ff4444;
            --success-color: #00cc88;
            --progress-bg: #2d2e33;
        }
        
        /* Global styles */
        .stApp {
            background-color: var(--background-color);
            color: var(--text-color);
        }
        
        .main-title {
            color: var(--text-color);
            font-size: 2rem;
            text-align: center;
            margin-bottom: 0.5rem;
        }
        
        .subtitle {
            color: #a0a0a0;
            font-size: 1.2rem;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Input field styling */
        .stTextInput > div > div {
            background-color: var(--input-bg) !important;
            color: var(--text-color) !important;
            border-radius: 8px !important;
            border: none !important;
            padding: 8px 12px;
        }
        
        /* Strength indicators */
        .strength-text {
            font-size: 1.3rem;
            margin: 1rem 0;
        }
        
        .very-weak { color: #ff4444; }
        .weak { color: #ffa500; }
        .medium { color: #ffdd00; }
        .strong { color: #00cc88; }
        .very-strong { color: #00ff88; }
        
        /* Requirements list */
        .requirement {
            display: flex;
            align-items: center;
            margin: 0.5rem 0;
            font-size: 1.1rem;
        }
        
        .requirement-error {
            color: var(--error-color);
        }
        
        .requirement-success {
            color: var(--success-color);
        }
        
        /* Progress bar */
        .stProgress > div > div {
            background-color: var(--progress-bg);
        }
        
        .stProgress > div > div > div {
            background-color: #3498db;
        }
    </style>
""", unsafe_allow_html=True)

# App header
st.markdown('<h1 class="main-title">Password Strength Checker</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Create a strong password to protect your accounts</p>', unsafe_allow_html=True)

def check_password_strength(password):
    requirements = {
        'length': len(password) >= 8,
        'number': bool(re.search(r"\d", password)),
        'lowercase': bool(re.search(r"[a-z]", password)),
        'uppercase': bool(re.search(r"[A-Z]", password)),
        'special': bool(re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password))
    }
    
    score = sum(requirements.values())
    strength_labels = {
        0: ("Very Weak", "very-weak"),
        1: ("Weak", "weak"),
        2: ("Medium", "medium"),
        3: ("Strong", "strong"),
        4: ("Very Strong", "very-strong"),
        5: ("Very Strong", "very-strong")
    }
    
    return requirements, score, strength_labels[score]

# Password input
password = st.text_input("Enter your password", type="password")

if password:
    requirements, score, (strength_text, strength_class) = check_password_strength(password)
    
    # Display strength
    st.markdown(
        f'<div class="strength-text">Password Strength: '
        f'<span class="{strength_class}">{strength_text}</span></div>',
        unsafe_allow_html=True
    )
    
    # Progress bar
    st.progress(score / 5)
    
    # Requirements list
    st.markdown("### Password Requirements:")
    
    requirements_text = {
        'length': "At least 8 characters",
        'number': "Contains a number",
        'lowercase': "Contains a lowercase letter",
        'uppercase': "Contains an uppercase letter",
        'special': "Contains a special character"
    }
    
    for req_key, is_met in requirements.items():
        status_class = "requirement-success" if is_met else "requirement-error"
        icon = "✓" if is_met else "✗"
        st.markdown(
            f'<div class="requirement {status_class}">'
            f'{icon} {requirements_text[req_key]}</div>',
            unsafe_allow_html=True
        )
else:
    st.info("Enter a password to check its strength")