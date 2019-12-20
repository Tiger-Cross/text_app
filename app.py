import nexmo
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from .util import env_var

# Load environment variables from .env file
load_dotenv('.env')

# Load in configuration from environment
NEXMO_API_KEY = env_var('NEXMO_API_KEY')
NEXMO_API_SECRET = env_var('NEXMO_API_SECRET')
NEXMO_NUMBER = env_var('NEXMO_NUMBER')

# Create new nexmo client object
nexmo_client = nexmo.Client(
    api_key=NEXMO_API_KEY, api_secret=NEXMO_API_SECRET
)

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = env_var('FLASK_SECRET_KEY')


@app.route('/')
def send_sms():
    """A view that renders the send sms form."""
    return render_template('sms_form.html')


if __name__ == '__main__':
    app.run()
