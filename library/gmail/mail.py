from __future__ import print_function
import httplib2
from apiclient import discovery
# from oauth2client import tools
from library.gmail import send_email
# import argparse
import os

# try:
#
#     flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
# except ImportError:
#     flags = None

from library.gmail import auth


def get_labels():
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])


SCOPES = 'https://mail.google.com/'
cwd_dir = os.getcwd()
CLIENT_SECRET_FILE = os.path.join(cwd_dir, 'library/gmail/client_secret.json')
APPLICATION_NAME = 'Gmail API Python Quickstart'
authInst = auth.Auth(SCOPES, CLIENT_SECRET_FILE, APPLICATION_NAME)
credentials = authInst.get_credentials()

http = credentials.authorize(httplib2.Http())
service = discovery.build('gmail', 'v1', http=http)


def mail_otp(receiver, pin_code, username):
    send_inst = send_email.SendEmail(service)
    message = send_inst.create_otp('raxoweb@gmail.com', receiver, 'Raxoweb OTP Assistant',
                                   pin_code, username)
    print("message sent")
    send_inst.send_message('me', message)


def mail_info(receiver, user):
    send_inst = send_email.SendEmail(service)
    message = send_inst.create_message('raxoweb@gmail.com', receiver,
                                       'We will contact you soon', user)
    send_inst.send_message('me', message)


def mail_me(name, sender, mobile, message):
    send_inst = send_email.SendEmail(service)
    message = send_inst.create_message_for_me('raxoweb@gmail.com', 'raxoweb@gmail.com',
                                              'someone want to contact', name, sender,
                                              mobile, message)
    send_inst.send_message('me', message)

# mail_me(name, sender, mobile, message):
# info = f"""name: {name}\nEmail: {sender}\nMobile: {mobile}\nMessage: {message}"""
# send_inst = send_email.SendEmail(service)
# message = send_inst.create_message_with_attachment('raxoweb@gmail.com', 'raxoweb@gmail.com',
#                                                    'contact us response', info, 'image.jpg')
# send_inst.send_message('me', message)

if __name__ =='__main__':
    mail_otp('kumarbipulsingh@gmail.com', '3456', 'Bipul')