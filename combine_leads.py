import pandas as pd

# Load old outreach CSV (from X)
df_old = pd.read_csv("outreach_with_messages.csv")

# Load new leads + messages from SerpApi scraping (actual file you have)
df_new = pd.read_csv("web3_leads.csv")

# Combine both, ignoring index so it resets
df_combined = pd.concat([df_old, df_new], ignore_index=True)

# Save combined results back to CSV
df_combined.to_csv("outreach_with_messages.csv", index=False)

print("✅ Combined outreach CSV saved with all leads and messages")