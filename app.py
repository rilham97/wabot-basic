from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from utils import fetch_reply

app = Flask(__name__)
#
#@app.route("/")
#def hello():
#    return "Asse loleee!"
#
#@app.route('/bot', methods=['POST'])
#def bot():
#    incoming_msg = request.values.get('Body', '').lower()
#    resp = MessagingResponse()
#    msg = resp.message()
#    responded = False
#    if 'quote' in incoming_msg:
#        # return a quote
#        r = requests.get('https://api.quotable.io/random')
#        if r.status_code == 200:
#            data = r.json()
#            quote = f'{data["content"]} ({data["author"]})'
#        else:
#            quote = 'I could not retrieve a quote at this time, sorry.'
#        msg.body(quote)
#        responded = True
#    if 'cat' in incoming_msg:
#        # return a cat pic
#        msg.media('https://cataas.com/cat')
#        responded = True
#    if not responded:
#        msg.body('I only know about famous quotes and cats, sorry!')
#    return str(resp)
#
#if __name__ == "__main__":
#    app.run(debug=True)


@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    phone_no = request.form.get('From')
    
    reply = fetch_reply(msg,phone_no)

    # Create reply
    resp = MessagingResponse()
    resp.message(reply)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)