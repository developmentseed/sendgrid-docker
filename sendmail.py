import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

FROM_EMAIL = os.environ.get('FROM_EMAIL')
TO_EMAILS = os.environ.get('TO_EMAILS')
EMAIL_SUBJECT = os.environ.get('EMAIL_SUBJECT')
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
EMAIL_MESSAGE = os.environ.get('EMAIL_MESSAGE')

print(SENDGRID_API_KEY)

message = Mail(
    from_email=FROM_EMAIL,
    to_emails=TO_EMAILS,
    subject=EMAIL_SUBJECT,
    html_content=EMAIL_MESSAGE)

try:
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)