🍀 Sous: The AI-Powered Sous-Chef
Sous is a smart, conversational cooking assistant designed to make your time in the kitchen more creative, fun, and efficient. Powered by Google's Gemini Pro model, Sous acts as your personal sous-chef, ready to provide recipes, generate meal plans, and even brainstorm ideas based on the ingredients you have on hand.

The application features a beautiful, modern "Aurora" themed UI with a secure login system, ensuring a polished and personalized user experience.

<!-- Placeholder: You would replace this with a real screenshot -->

✨ Features
Conversational AI Chat: Ask for recipes, cooking techniques, or ingredient substitutions in plain English.

"What Can I Make?" Tool: Enter the ingredients you have, and the AI will generate custom recipe ideas for you.

Custom Meal Plan Generation: Request personalized meal plans based on your dietary needs, duration, and goals (e.g., "a 3-day high-protein vegetarian plan").

Secure User Sessions: A simple and effective login flow ensures that the chat area is a protected route.

Stunning, Modern UI: A responsive, single-page application with a beautiful "Aurora" background and a "glassmorphism" design aesthetic.

🛠️ Tech Stack
Backend: Python with the Flask web framework.

AI Model: Google Gemini Pro via the google-generativeai library.

Frontend: HTML5, CSS3, and modern JavaScript (no external frameworks).

Dependencies: python-dotenv for managing environment variables.

🚀 Getting Started
Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Python 3.8 or higher

A Google API Key with the Gemini API enabled. You can get one from Google AI Studio.

Installation & Setup
Clone the Repository (or download the project files):

git clone [https://github.com/your-username/Sous.git](https://github.com/your-username/Sous.git)
cd Sous

Create a Virtual Environment:
It's highly recommended to use a virtual environment to keep project dependencies isolated.

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate

Install Dependencies:
Install Flask and the other required Python packages.

pip install Flask google-generativeai python-dotenv

Configure Environment Variables:
Create a file named .env in the root directory of your project. This file will securely store your API key. Add the following line to it, replacing YOUR_API_KEY_HERE with your actual key:

GOOGLE_API_KEY='YOUR_API_KEY_HERE'

Run the Application:
Once the setup is complete, you can start the Flask development server.

python app.py

You should see output in your terminal indicating that the server is running, like this:

* Running on [http://127.0.0.1:5000](http://127.0.0.1:5000)

Usage
Open your web browser and navigate to http://127.0.0.1:5000. You will be greeted by the login page. From there, you can log in or continue as a guest to access the main chat interface.

📂 Project Structure
.
├── app.py              # The main Flask application backend
├── templates/
│   ├── index.html      # The main chat interface
│   └── login.html      # The login page
├── .env                # Stores the Google API Key (you must create this)
└── README.md           # This file
