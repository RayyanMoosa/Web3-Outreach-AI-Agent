import pandas as pd

# Load your CSV file
df = pd.read_csv("web3_leads.csv")

# Optional: Normalize column names just in case
df.columns = df.columns.str.strip()  # Remove leading/trailing spaces

# Loop through the leads and generate personalized messages
for index, row in df.iterrows():
    name = row['Name']
    title = row['Title']
    url = row['URL']
    contact_info = row['Contact Info'] if pd.notna(row['Contact Info']) else "N/A"
    notes = row['Notes'] if pd.notna(row['Notes']) else "No extra notes"

    message = f"""\
Hi {name},

I came across your post titled "{title}" ({url}) and found it insightful. I'm currently building AI tools tailored for Web3 founders, and your work really aligns with what we're working on.

I'd love to connect and learn more about your journey — maybe there's a way we can collaborate or bring value to your community.

Best,  
Rayyan
"""

    print("======")
    print(message)

