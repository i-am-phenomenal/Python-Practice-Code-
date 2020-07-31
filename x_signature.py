# Python sample: how to check the x-sendbird-signature header value

from __future__ import unicode_literals
import hashlib, hmac

api_token = b'APITOKEN'   # Convert a string of your API token to a bytes object.
webhook_payload = '{"category": "group_channel:message_send","sender": {"user_id": "Jeff","nickname": "Oldies but goodies",...},...}'  # The webhook payload parsed from a received HTTP POST request.

signature_to_compare = hmac.new(
    key=api_token,
    msg=bytes(webhook_payload.encode('utf8')),
    digestmod=hashlib.sha256).hexdigest()

print(signature_to_compare)

assert signature_to_compare == 'x_sendbird_signature'   # Check if the value of the 'x-sendbird-signature' request header is the same as the comparison value you've created. 
