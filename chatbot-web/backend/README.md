# Backend Chatbot Documentation

## Overview
This project implements a chatbot using Python, which can predict user intents and generate appropriate responses. The chatbot logic is encapsulated in the `chatbot.py` file, while the backend dependencies are listed in `requirements.txt`.

## Files

### chatbot.py
This file contains the core logic of the chatbot, including:
- **Intent Prediction**: Uses a machine learning model to predict user intents based on input text.
- **Response Generation**: Returns a random response from a predefined set of responses based on the predicted intent.
- **Text Preprocessing**: Cleans and tokenizes user input for better prediction accuracy.
- **Chatbot Execution**: Contains the main loop to interact with users.

### requirements.txt
This file lists the necessary Python libraries required to run the chatbot. Ensure to install these dependencies before running the application.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd chatbot-web/backend
   ```

2. **Install Dependencies**
   It is recommended to use a virtual environment. You can create one using:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Chatbot**
   Execute the chatbot by running:
   ```bash
   python chatbot.py
   ```

4. **Interacting with the Chatbot**
   Once the chatbot is running, you can interact with it through the command line. Type your messages and receive responses until you type 'quit', 'exit', or 'thoát' to end the session.

## Additional Notes
- Ensure that the `data/intents.json` file is correctly populated with intents for the chatbot to function properly.
- For further customization, you can modify the intents and responses in the `chatbot.py` file.