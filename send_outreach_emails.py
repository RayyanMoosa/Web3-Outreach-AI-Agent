import pandas as pd
import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# Load your outreach CSV
df = pd.read_csv('outreach_with_messages.csv')

# Load credentials (make sure token.json and credentials.json exist)
creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/gmail.send'])
service = build('gmail', 'v1', credentials=creds)

def create_message(to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw}

def send_message(service, user_id, message):
    try:
        sent = service.users().messages().send(userId=user_id, body=message).execute()
        print(f"Message sent to {message['raw'][:30]}...")  # print first 30 chars of raw
        return sent
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

for i, row in df.iterrows():
    # Try both 'email' and 'Contact Info' columns
    email = None
    if 'email' in row and pd.notna(row['email']) and str(row['email']).strip():
        email = row['email']
    elif 'Contact Info' in row and pd.notna(row['Contact Info']) and str(row['Contact Info']).strip():
        email = row['Contact Info']

    if not email:
        print(f"No email for row {i}, skipping.")
        continue

    # Get outreach message, fallback if missing
    message_text = row['outreach_message'] if 'outreach_message' in row and pd.notna(row['outreach_message']) else "Hi, I wanted to reach out regarding an exciting opportunity!"

    message = create_message(email, "Exciting Web3 Opportunity", message_text)
    send_message(service, 'me', message)
