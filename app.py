import os
# Import Bolt for Python (github.com/slackapi/bolt-python)
from slack_bolt import App

# Initializes your Bolt app with a bot token and signing secret
app = App(
    token="xoxb-3231366837447-3334991930082-c1EzFOF62rrd8MXqhwZC9kyw",
    signing_secret="3c7fc45075aa90342eef08d00bc90232"
)

@app.event("app_mention")
def event_test(body, say, logger):
    logger.info(body)
    say("What's up?")

@app.event("app_home_opened")
def handle_app_home_opened_events(body, logger):
    print('WE GOT IT')
    logger.info(body)

@app.event("message")
def handle_message_events(body, say, logger):
    print('test')
    if 'andres' in body['event']['text'].lower():
        if 'likes' in body['event']['text'].lower():
            say('ME TOO!')
        else: 
            say('WATUP BOI')
        #  say(f"Hey there <@{message['user']}>!")
    else:
        print('get outta here')
    logger.info(body)


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))