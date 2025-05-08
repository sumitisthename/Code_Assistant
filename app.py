import requests
import json
import gradio as gr

url="http://localhost:11434/api/generate"

headers = {
    "Content-Type": "application/json",
}

history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)
    # final_prompt = f"Please write a python code for the following prompt: {prompt}"
    data ={
        "model": "coder",
        "prompt":final_prompt,
        "stream": False,

    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response = response.text
        data = json.loads(response)
        actual_response = data['response']
        return actual_response
    else:
        return "Error: " + str(response.status_code) + " - " + response.text
    

interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(label="Enter your prompt", placeholder="Enter your prompt here..."),
    outputs=gr.Textbox(label="Response", placeholder="Response will be shown here...")
)


interface.launch(share=True, debug=True)