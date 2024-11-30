from app import create_app, socketio

# Create the Flask app
flask_app = create_app(debug=True)  # Enable debug mode here if needed

# Ensure a secret key is set for session management
flask_app.config['SECRET_KEY'] = "your_secret_key"  # Replace with a strong secret key!

# Import events after app creation to avoid circular imports
import app.events

# Define the main entry point
def main():
    socketio.run(flask_app, host="127.0.0.1", port=5000)

# Run the application
if __name__ == "__main__":
    main()


