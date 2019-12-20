import nexmo
import os
from flask import Flask, render_template
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
def send_sms():
    """A view that renders the send sms form."""
    return render_template('sms_form.html')


if __name__ == '__main__':
    app.run()
