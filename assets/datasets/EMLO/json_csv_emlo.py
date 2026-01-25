import json
import csv

# Read the JSON file
with open('womentomen.json', 'r') as f:
    data = json.load(f)

# Extract the document records from the response
docs = data.get('response', {}).get('docs', [])

# Convert documents to rows with relevant fields
rows = []
for doc in docs:
    # Extract date - prefer the year field
    year = doc.get('ox_started-ox_year', '')
    date = doc.get('started_date_sort', '')
    if not date: date = year
    
    # Extract origin and destination from the doc if available
    # Since these don't seem to be in individual docs, check facets
    origin = doc.get('origin_sort', '')
    destination = doc.get('destination_sort', '')
    
    # Get author and recipient
    author = doc.get('author_sort', '')
    recipient = doc.get('recipient_sort', '')
    
    # Get description
    description = doc.get('dcterms_description', '')
    
    # Get manifestation institution/place if available
    places = doc.get('manifestation-institution-place', [])
    location = ', '.join(places) if isinstance(places, list) else places
    
    rows.append({
        'Description': description,
        'Author': author,
        'Recipient': recipient,
        'Date': date,
        'Year': year,
        'Location': location,
        'Origin': origin,
        'Destination': destination
    })

# Write to CSV
fieldnames = ['Description', 'Author', 'Recipient', 'Date', 'Year', 'Location', 'Origin', 'Destination']
with open('womentomen.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Successfully converted womentomen.json to womentomen.csv")
print(f"Total entries: {len(rows)}")
print(f"Fields: {', '.join(fieldnames)}")
