# Code LLaMA - Gradio Chatbot with Local Coder Model

This is a simple Gradio-based frontend application that interacts with a locally hosted Code LLaMA model (`coder`) using HTTP API. It supports prompt-based code generation and conversational history tracking.

## Project Structure
```
CODE_LLAMA/
│
├── .gradio/ # Gradio certificates and flagged examples
│ └── certificate.pem
├── .venv/ # Python virtual environment
├── app.py # Main Python app for Gradio interface
├── Modelfile # Model configuration (for Ollama or local runner)
├── requirements.txt # Python dependencies
└── README.md # Project documentation (this file)
```


## Features

- Connects to a locally hosted `coder` model endpoint (Ollama or similar).
- Tracks prompt history to allow contextual responses.
- Uses Gradio UI for interactive prompt submission and response display.
- Secure Gradio sharing enabled with HTTPS certificate.

## Requirements

Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

Ensure your local model server is running and accessible at:
```
http://localhost:11434/api/generate
```

## Usage
Run the Gradio app:
}
```
python app.py
```

## API Expected Input

The app sends a POST request with this structure:
```
{
  "model": "coder",
  "prompt": "your combined prompt here",
  "stream": false
}
```





