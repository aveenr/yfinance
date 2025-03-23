import yfinance as yf
import os

# Define stock ticker and download settings
TICKER = "SOL.JO"  # Sasol Ltd on JSE
DOWNLOAD_FOLDER = "stocks_data"  # Folder where CSV will be saved

# Ensure the download folder exists
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# Download all available historical data
print(f"Downloading all available data for {TICKER}...")
data = yf.download(TICKER, period="max", auto_adjust=True)

# Save to CSV
csv_filename = os.path.join(DOWNLOAD_FOLDER, f"{TICKER}_full_history.csv")
data.to_csv(csv_filename)

# Confirm download
print(f"Data saved to {csv_filename}")
print(data.tail())  # Print the last few rows to verify
