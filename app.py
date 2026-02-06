import os
import gradio as gr
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def chat_with_groq(message, history):
    if not message.strip():
        return "Please kuch type karo 🙂"

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a beginner-friendly chatbot. Explain clearly and simply."},
                {"role": "user", "content": message},
            ],
            temperature=0.7,
            max_tokens=1200,
        )
        reply = response.choices[0].message.content
    except Exception:
        reply = "⚠️ Model response nahi de raha. Thori dair baad dobara try karo."

    return reply

custom_css = """
.gradio-container {
    max-width: 100% !important;
    height: 100vh !important;
    background: linear-gradient(135deg, #ff8c00 0%, #ff4500 50%, #ff6b35 100%);
    font-family: 'Segoe UI', sans-serif !important;
}

/* Full screen - no phone frame */
.frame-container, .gradio-container > div {
    border: none !important;
    box-shadow: none !important;
    border-radius: 0 !important;
    width: 100vw !important;
    height: 100vh !important;
}

/* Title styling */
h1 {
    background: linear-gradient(45deg, #FFD700, #FFA500, #FF8C00);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-weight: 800 !important;
    text-align: center;
    font-size: 2.5rem !important;
    text-shadow: 0 0 30px rgba(255, 215, 0, 0.6);
    margin: 20px 0 !important;
}

/* ChatInterface full height */
.chat-interface {
    height: 90vh !important;
    background: rgba(255, 255, 255, 0.08) !important;
    backdrop-filter: blur(20px);
    border-radius: 25px !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    box-shadow: 0 25px 50px rgba(0,0,0,0.4);
    margin: 20px !important;
}

/* Chatbot area */
#chatbot {
    height: 75vh !important;
    background: rgba(0, 0, 0, 0.4) !important;
    border-radius: 20px !important;
    margin-bottom: 10px !important;
}

/* Messages */
.message {
    background: rgba(255, 255, 255, 0.18) !important;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 215, 0, 0.4) !important;
    border-radius: 15px !important;
    color: #ffffff !important;
    font-weight: 500;
    font-size: 15px !important;
}

/* Textbox */
textarea {
    background: rgba(0, 0, 0, 0.5) !important;
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255, 215, 0, 0.5) !important;
    border-radius: 30px !important;
    color: #FFD700 !important;
    font-size: 16px !important;
    padding: 18px 25px !important;
}

/* Send Button */
button[data-testid="send-button"], .send-button {
    background: rgba(255, 215, 0, 0.25) !important;
    backdrop-filter: blur(25px);
    border: 2px solid rgba(255, 215, 0, 0.6) !important;
    border-radius: 50px !important;
    color: #FFD700 !important;
    font-weight: 800 !important;
    font-size: 15px !important;
    padding: 15px 30px !important;
    margin-left: 10px !important;
    text-transform: uppercase;
    letter-spacing: 1px;
}

button[data-testid="send-button"]:hover, .send-button:hover {
    background: rgba(255, 215, 0, 0.45) !important;
    box-shadow: 0 0 25px rgba(255, 215, 0, 0.7) !important;
    transform: translateY(-3px) !important;
}

/* Settings Button */
button:has(svg) {
    background: rgba(255, 165, 0, 0.25) !important;
    backdrop-filter: blur(25px);
    border: 2px solid rgba(255, 165, 0, 0.6) !important;
    border-radius: 50px !important;
    color: #FFA500 !important;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 10px;
}
::-webkit-scrollbar-track {
    background: rgba(0,0,0,0.3);
}
::-webkit-scrollbar-thumb {
    background: linear-gradient(45deg, #FFD700, #FFA500);
    border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(45deg, #FFA500, #FF8C00);
}
"""

with gr.Blocks(fill_height=True, fill_width=True) as demo:
    gr.Markdown("# ⚡ GROQ AI CHAT")
    
    gr.ChatInterface(
        fn=chat_with_groq,
        title="",
        description="",
        examples=None,
        cache_examples=False,
    )

demo.launch(
    server_name="0.0.0.0", 
    server_port=7860,
    share=False,
    show_error=True,
    css=custom_css  # CSS sirf YAHAN pass hoga!
)
