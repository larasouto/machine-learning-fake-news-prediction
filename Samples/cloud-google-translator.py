import os
import csv
from google.cloud import translate_v2

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'google-credentials.json'

translate_client = translate_v2.Client()

with open('Fake.br-Corpus.csv', 'r') as file_csv, open('Fake.br-Corpus_English.csv', 'a', newline='') as output_csv:
    read_csv = csv.reader(file_csv)
    write_csv = csv.writer(output_csv)
    
    header = next(read_csv)
    
    for row in read_csv:
        index, label, news = row[:3]
        preprocessed_news = translate_client.translate(news, target_language='en')['translatedText'].lower().replace(",", "")
        write_csv.writerow([index, label, preprocessed_news])
        
