# Chatbot Web Project

This project integrates a chatbot functionality using a backend implemented in Python and a frontend built with HTML, CSS, and JavaScript.

## Project Structure

```
chatbot-web
├── backend
│   ├── chatbot.py          # Contains the chatbot logic, including intent prediction and response generation.
│   ├── requirements.txt    # Lists the Python dependencies required for the backend.
│   └── README.md           # Documentation for the backend setup and usage.
├── frontend
│   ├── index.html          # Main HTML file for the web interface.
│   ├── style.css           # Styles for the web interface.
│   └── app.js              # JavaScript code for handling user interactions and displaying responses.
└── README.md               # Documentation for the entire project setup and usage.
```

## Backend Setup

1. Navigate to the `backend` directory.
2. Install the required Python packages listed in `requirements.txt` using pip:
   ```
   pip install -r requirements.txt
   ```
3. Run the chatbot server:
   ```
   python chatbot.py
   ```

## Frontend Setup

1. Open the `frontend/index.html` file in a web browser to access the chatbot interface.
2. Ensure the backend server is running to handle requests from the frontend.

## Usage

- Type your message in the input field and press Enter to send it to the chatbot.
- The chatbot will respond based on the predefined intents and responses.
- To exit the chatbot, type "quit", "exit", or "thoát".

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.