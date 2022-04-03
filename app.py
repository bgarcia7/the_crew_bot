import os
# Import Bolt for Python (github.com/slackapi/bolt-python)
from slack_bolt import App
from utils import clean_message

# Initializes your Bolt app with a bot token and signing secret
app = App(
    # token="xapp-1-A03AJM7ALHE-3337314575652-7c26f0dc2732c4666d3f2fbb47ff87121d1c88fd6c4d774bed200a0505095aed",
    token ="xoxb-3231366837447-3334991930082-iuN4K2kMr5MPd926KSTaBVkP",
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
    print(body)
    text = clean_message(body)
    if 'andres' in text:
        if 'likes' in text:
            say('ME TOO!')
        else: 
            say('WATUP BOI')
        #  say(f"Hey there <@{message['user']}>!")
    if 'read spots' in text: 
        say(read_meetup_spots())
    elif 'log spot' in text:
        say(log_meetup_spot(text))
    else:
        print('get outta here')
    logger.info(body)

def log_meetup_spot(text):
    spot = 'http' + text.split('http')[1]
    file1 = open("spots.txt", "a")  # append mode
    file1.write(spot + "\n")
    file1.close()
    return('all done')

def read_meetup_spots():
    with open('spots.txt') as f:
        spots = ''.join(f.readlines())
        return(spots)

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))