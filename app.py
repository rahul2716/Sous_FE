import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify, redirect, url_for
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

try:
    # Get the API key from the environment variables
    api_key = os.environ["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    
    # Initialize the Gemini Pro model
    model = genai.GenerativeModel('gemini-2.5-pro')
    
    # Start a chat session
    chat = model.start_chat(history=[])
    
    print("Gemini API configured successfully!")

except KeyError:
    print("\n[ERROR] The GOOGLE_API_KEY environment variable is not set.")
    print("Please create a .env file, add your key (e.g., GOOGLE_API_KEY='YOUR_API_KEY'), and restart.")
    exit()
except Exception as e:
    print(f"An error occurred during Gemini configuration: {e}")
    exit()

def call_gemini(prompt):
    """Sends a structured prompt to the ongoing Gemini chat session."""
    print(f"Sending prompt to Gemini: '{prompt[:80]}...'")
    try:
        response = chat.send_message(prompt)
        if response and response.parts:
            if response.prompt_feedback.block_reason:
                 return f"Response blocked due to: {response.prompt_feedback.block_reason.name}"
            return response.text
        else:
            return "I'm sorry, I couldn't get a valid response. Please try again."
    except Exception as e:
        print(f"An error occurred while calling the Gemini API: {e}")
        return "An error occurred while trying to connect to the assistant. Please check your connection."

# --- Routes for Login Flow ---

@app.route('/')
def login_page():
    """Renders the login page, which is now the main entry point."""
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def handle_login():
    """
    Handles the login form submission.
    In a real app, you would verify credentials here.
    For now, we just redirect to the chat page.
    """
    return redirect(url_for('chat_page'))

@app.route('/chat_page')
def chat_page():
    """Renders the main chat interface page."""
    return render_template('index.html')


# --- Chat API ---

@app.route('/chat', methods=['POST'])
def chat_handler():
    """Handles chat messages, constructs prompts, and returns the model's response."""
    data = request.json
    user_message = data.get('message')
    request_type = data.get('type', 'chat')

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # This prompt engineering section remains unchanged.
    if request_type == 'ingredients':
        prompt_for_gemini = f"""
        **Persona**: You are 'Sous-Chef', a creative and resourceful AI chef who loves a good challenge. You see a list of ingredients not as a limitation, but as a puzzle.
        **Core Task**: The user has provided a list of ingredients they have on hand. Your job is to brainstorm and present 1 to 2 delicious and practical recipes they can make.
        **Ingredient List**: "{user_message}"
        **Instructions**:
        1.  **Analyze the Ingredients**: First, assess the core ingredients.
        2.  **Acknowledge Limitations**: If the list is sparse, suggest a simple classic dish.
        3.  **Identify Missing Staples**: Create a "You might also need" section for common pantry staples.
        4.  **Structure the Output**: Use a bold title, ingredient list, and numbered steps.
        5.  **Be Creative**: Suggest interesting recipes beyond the obvious.
        6.  **Format**: Use Markdown for perfect readability.
        """
    elif request_type == 'meal_plan':
        prompt_for_gemini = f"""
        **Persona**: You are 'Sous-Chef', an expert and highly organized AI meal planner.
        **Core Task**: A user has requested a custom meal plan.
        **User's Request**: "{user_message}"
        **Instructions**:
        1.  **Deconstruct the Request**: Analyze duration, dietary needs, and goals.
        2.  **Generate a Structured Plan**: Organize by Day, with Breakfast, Lunch, and Dinner.
        3.  **Provide Balanced and Varied Ideas**: Ensure a good mix of flavors and food groups.
        4.  **Add a "Pro Tip"**: Include one helpful tip related to their request at the end.
        5.  **Tone**: Be encouraging, realistic, and non-judgmental.
        6.  **Format**: Present the entire plan in clean, readable Markdown.
        """
    else: # Default handler for general chat questions ('chat').
        prompt_for_gemini = f"""
        **Persona**: You are 'Sous-Chef', an AI cooking companion with the personality of a friendly, passionate chef.
        **Core Task**: Respond to the user's cooking-related query.
        **Instructions**:
        1.  **Recipe Requests**: Provide in clear Markdown with a description, ingredients, and steps.
        2.  **Technique Questions**: Provide a step-by-step guide.
        3.  **Ingredient Substitutions**: Give safe and effective suggestions and explain why they work.
        4.  **Safety First**: Prioritize safety and advise against risky actions clearly.
        5.  **Maintain Persona**: Use cooking-related metaphors and a warm tone. Start your very first response with a chef emoji 👨‍🍳.
        **User's query**: "{user_message}"
        """

    bot_response = call_gemini(prompt_for_gemini)
    return jsonify({"reply": bot_response})

if __name__ == '__main__':
    print("Starting the Sous-Chef Flask server...")
    app.run(debug=True, port=5000)

