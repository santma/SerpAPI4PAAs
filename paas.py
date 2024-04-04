from serpapi import GoogleSearch
import requests
import json
import csv

input_filename = 'keywords.csv'

output_filename = 'paas.csv'

API_KEY = '[Your SERP API Key]'

def get_paas(keyword, API_KEY):
        params = {
            'engine': 'google',
            'q': keyword,
            'api_key': API_KEY,
            'location': 'United States',
            'google_domain': 'google.com',
            'gl': 'us',
            'hl': 'en'
        }
        response = requests.get('https://serpapi.com/search', params)
        if response.status_code == 200:
            data = response.json()
            # Extract the 'people also ask' questions
            paa_questions = data.get('people_also_ask', [])
            print(f"Questions for '{keyword}':")
            print(paa_questions)
            return(paa_questions)
        else:
            print(f"Failed to retrieve data for keyword: {keyword}")


# Reading keywords from CSV
input_csv = 'keywords.csv'  # Replace with your input CSV file path
keywords = []
with open(input_csv, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader, None)  # Skip the header if there is one
    for row in reader:
        keywords.append(row[0])  # Assuming keywords are in the first column

# Processing each keyword and writing results to a new CSV
output_csv = 'paas.csv'  # Replace with your desired output CSV file path
with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Writing a header (optional)
    writer.writerow(['Keyword', 'PAA Question 1', 'PAA Question 2', 'PAA Question 3', 'PAA Question 4'])

    for keyword in keywords:
        paa_questions = get_paas(keyword, API_KEY)
        row = [keyword] + paa_questions
        writer.writerow(row)

print("Processing complete. Results are in", output_csv)
