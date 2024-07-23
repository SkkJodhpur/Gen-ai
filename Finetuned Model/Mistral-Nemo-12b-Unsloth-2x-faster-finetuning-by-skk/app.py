import gradio as gr
from unsloth import FastLanguageModel
import torch

# Load the model and tokenizer
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="skkjodhpur/Mistral-Nemo-12b-Unsloth-2x-faster-finetuning-by-skk",
    max_seq_length=2048,
    load_in_4bit=True
)
FastLanguageModel.for_inference(model)

# Define the function to generate output
def generate_response(instruction, input_text):
    alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

    ### Instruction:
    {}

    ### Input:
    {}

    ### Response:
    {}"""
    
    inputs = tokenizer(
        [alpaca_prompt.format(instruction, input_text, "")],
        return_tensors="pt"
    ).to("cuda")

    output = model.generate(input_ids=inputs.input_ids, attention_mask=inputs.attention_mask, max_new_tokens=64, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

# Create the Gradio interface
with gr.Blocks(css=".gradio-container {background-color: #f0f4f8; padding: 20px; border-radius: 10px;} .input-text {background-color: #e0f7fa; border: 1px solid #00796b; border-radius: 5px;} .output-text {background-color: #fff3e0; border: 1px solid #e65100; border-radius: 5px;}") as demo:
    gr.Markdown("<h1 style='text-align: center; color: #00796b;'>AI Response Generator</h1>")
    
    with gr.Row():
        instruction_input = gr.Textbox(label="Instruction", placeholder="Enter instruction here...", lines=2, css="input-text")
    
    with gr.Row():
        context_input = gr.Textbox(label="Input Context", placeholder="Enter input context here...", lines=4, css="input-text")
    
    with gr.Row():
        submit_button = gr.Button("Generate Response", variant="primary")

    output_text = gr.Textbox(label="Generated Response", interactive=False, lines=4, css="output-text")

    submit_button.click(generate_response, inputs=[instruction_input, context_input], outputs=output_text)

# Launch the interface
demo.launch()
