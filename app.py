import os
# Import Bolt for Python (github.com/slackapi/bolt-python)
from slack_bolt import App

# Initializes your Bolt app with a bot token and signing secret
app = App(
    token="xoxb-3231366837447-3334991930082-d7ju9AMx96Ek8elP6o8eBZGb",
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
    if 'andres' in body['event']['text'].lower():
        say('WATUP BOI')
        # say(f"Hey there <@{message['user']}>!")
    else:
        print('get outta here')
    logger.info(body)

# The open_modal shortcut opens a plain old modal
# Shortcuts require the command scope
@app.shortcut("open_modal")
def open_modal(ack, shortcut, client, logger):
    # Acknowledge shortcut request
    ack()

    try:
        # Call the views.open method using the WebClient passed to listeners
        result = client.views_open(
            trigger_id=shortcut["trigger_id"],
            view={
                "type": "modal",
                "title": {"type": "plain_text", "text": "My App"},
                "close": {"type": "plain_text", "text": "Close"},
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "About the simplest modal you could conceive of :smile:\n\nMaybe <https://api.slack.com/reference/block-kit/interactive-components|*make the modal interactive*> or <https://api.slack.com/surfaces/modals/using#modifying|*learn more advanced modal use cases*>.",
                        },
                    },
                    {
                        "type": "context",
                        "elements": [
                            {
                                "type": "mrkdwn",
                                "text": "Psssst this modal was designed using <https://api.slack.com/tools/block-kit-builder|*Block Kit Builder*>",
                            }
                        ],
                    },
                ],
            },
        )
        logger.info(result)

    except SlackApiError as e:
        logger.error("Error creating conversation: {}".format(e))

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))