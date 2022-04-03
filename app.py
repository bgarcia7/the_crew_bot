import logging
logging.basicConfig(level=logging.DEBUG)

from slack_bolt import App

app = App()

# Add functionality here

if __name__ == "__main__":
    app.start(3000)  # POST http://localhost:3000/slack/events