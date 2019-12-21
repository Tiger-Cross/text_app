## SMS text app

Instructions for use:

Clone this git repository,

Define two environment variables:

`SENDER_NUMBER` - The number for the sms client to send from.

`SMS_API_KEY` - The API key for the sms client (messagebird used)

Run the app locally using the command `FLASK_APP=app.py flask run`

NOTE: Ensure both the `SENDER NUMBER` recipient number input into the app contain the country codes but not a + at the beginnning and no spaces.

Next steps:

- Use nexmo to actually send the texts
- Use docker to containerise
- Create default text message
- Create form field for receivers name and input into message to make more personal.
