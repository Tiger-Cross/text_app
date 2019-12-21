import nexmo
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

# Load in configuration from environment
NEXMO_API_KEY = os.environ.get('NEXMO_API_KEY')
NEXMO_API_SECRET = os.environ.get('NEXMO_API_SECRET')
NEXMO_NUMBER = os.environ.get('NEXMO_NUMBER')

# Create new nexmo client object
nexmo_client = nexmo.Client(
    api_key=NEXMO_API_KEY, api_secret=NEXMO_API_SECRET
)

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
    result = nexmo_client.send_message({
        'from': NEXMO_NUMBER,
        'to': recipient_number,
        'text': message
    })

    # Redirect the user back to the form
    return redirect(url_for('sms_form'))


if __name__ == '__main__':
    app.run()
