import yfinance as yf
import os

# Define stock ticker and download settings
TICKER = "SOL.JO"  # Sasol Ltd on JSE
START_DATE = "2023-01-01"
END_DATE = "2024-01-01"
DOWNLOAD_FOLDER = "stocks_data"  # Folder where CSV will be saved

# Ensure the download folder exists
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# Download stock data
print(f"Downloading data for {TICKER} from {START_DATE} to {END_DATE}...")
data = yf.download(TICKER, start=START_DATE, end=END_DATE, auto_adjust=True)

# Save to CSV
csv_filename = os.path.join(DOWNLOAD_FOLDER, f"{TICKER}.csv")
data.to_csv(csv_filename)

# Confirm download
print(f"Data saved to {csv_filename}")
print(data.tail())  # Print the last few rows to verify
