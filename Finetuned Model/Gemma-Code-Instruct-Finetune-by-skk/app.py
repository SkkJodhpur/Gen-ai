import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load model and tokenizer
model_name = "skkjodhpur/Gemma-Code-Instruct-Finetune-by-skk"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Move model to CPU
device = "cpu"
model = model.to(device)

def generate_text(prompt):
    if not prompt.strip():
        return "Please enter a valid question."

    try:
        # Tokenize input
        input_ids = tokenizer.encode(f"<s>[INST] {prompt} [/INST]", return_tensors="pt").to(device)
        
        # Generate text with greedy search for faster response
        with torch.no_grad():
            output = model.generate(
                input_ids,
                max_length=100,  # Reduced max length for faster generation
                num_return_sequences=1,
                do_sample=False,  # Use greedy search
            )
        
        # Decode and return the generated text
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
        return generated_text
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Gradio interface
def chatbot_response(user_input):
    return generate_text(user_input)

iface = gr.Interface(
    fn=chatbot_response, 
    inputs="text", 
    outputs="text",     
    title="Doctors-Patient Chatbot",
    description="Ask me any question related to patient concerns. This model is designed for educational and informational purposes only. Please do not use it for medical diagnosis or treatment. Always consult a qualified healthcare provider for medical advice.",
    allow_flagging="never",  # Disable flagging if not needed
)

iface.launch(share=True)
