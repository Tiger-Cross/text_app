import messagebird
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

# Load in configuration from environment
SMS_API_KEY = os.environ.get('SMS_API_KEY')
SENDER_NUMBER = os.environ.get('SENDER_NUMBER')

# Create new sms client object
sms_client = messagebird.Client(SMS_API_KEY)

# Create and bootstrap app
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')


@app.route('/')
def sms_form():
    """A view that renders the send sms form."""
    return render_template('sms_form.html')


@app.route('/send_sms', methods=['POST'])
def send_sms():
    """POST endpoint that sends an sms. """

    # Extract form values.
    recipient_number = request.form['recipient']
    message = request.form['message']

    # Send sms message.
    result = sms_client.message_create(
        '+' + SENDER_NUMBER,
        '+' + recipient_number,
        message,
        {'reference': 'From my text app'}
    )

    # Redirect the user back to the form
    return redirect(url_for('confirm_sms'))


@app.route('/sms_conf')
def confirm_sms():
    """A view that renders the confirmation page for sending an sms."""
    return render_template('sms_confirmation.html')


if __name__ == '__main__':
    app.run()
