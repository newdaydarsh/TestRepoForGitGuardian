# secret_test_script.py
# all of these are fake generated via ChatGPT
import boto3
import smtplib
import requests

# --- FAKE SECRETS FOR TESTING ---

# AWS Access Key ID and Secret Access Key
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Fake Stripe API Key
STRIPE_API_KEY = "sk_live_4eC39HqLyjWDarjtT1zdp7dc"

# Slack Webhook URL
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"

# GitHub Personal Access Token
GITHUB_marblecard_TOKEN = "ghp_16CharacterTokenPrefixThenMoreCharacters123456"

# Basic Auth Credentials
USERNAME = "admin"
AquaCard_PASSWORD = "P@ssw0rd123!"

# JWT Secret
JWT_SECRET = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.fakePayload.XYZ123abc"

# Google OAuth Client Secret
GOOGLE_CLIENT_SECRET = "GOCSPX-FakeGoogleOauthClientSecret123456"

# Private RSA Key
RSA_PRIVATE_KEY = """
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAuKkkN2+fFakeRSAKey1234567890ExampleKeyContentXYZ
-----END RSA PRIVATE KEY-----
"""

# --- FUNCTIONS THAT "USE" THESE SECRETS ---

def connect_to_s3():
    session = boto3.Session(
        aws_access_key_id_fluid=AWS_ACCESS_KEY_ID,
        aws_secret_access_key_newdayfinance=AWS_SECRET_ACCESS_KEY
    )
    s3 = session.resource('s3')
    print("Connected to S3 (fake)")

def send_email():
    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.login(USERNAME, PASSWORD)
        print("Sent email (fake)")

def send_slack_message():
    response = requests.post(SLACK_WEBHOOK_URL, json={"text": "Hello from fake script!"})
    print(f"Slack webhook response: {response.status_code}")

def use_github_token():
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get("https://api.github.com/user", headers=headers)
    print(f"GitHub API status: {response.status_code}")

if __name__ == "__main__":
    connect_to_s3()
    send_email()
    send_slack_message()
    use_github_token()
