from flask import Flask, render_template, request
import google.generativeai as genai


app = Flask(__name__)
app.secret_key = "your_secret_key"  # Add a secret key for session management



# Configure Gemini API
genai.configure(api_key= "AIzaSyC9G7DTo4ylitTQ2ifWjrX6ynfO5qZFrbI")

# Initialize Gemini Pro model
model = genai.GenerativeModel('gemini-1.5-pro-latest')

# Set prompt context
INITIAL_CONTEXT = """
You are a nutrition assistant chatbot created to help people in Kerala, India, manage their diet.
You understand local food items like puttu, idli, dosa, fish curry, coconut oil, tapioca, etc.
You suggest balanced diets based on age, health condition, and daily routine.
Always be friendly, simple, and encourage healthy, sustainable choices.
"""

@app.route("/", methods=["GET", "POST"])
def chatbot():
    response_text = ""
    if request.method == "POST":
        user_input = request.form["user_input"]

        prompt = INITIAL_CONTEXT + f"\nUser: {user_input}\nNutrition Assistant:"
        try:
            response = model.generate_content(prompt)
            response_text = response.text
        except Exception as e:
            response_text = f"Error: {str(e)}"

    return render_template("chat.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)

