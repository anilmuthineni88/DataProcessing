import pandas as pd
import json


def process_json(json_file, output_file):
    # Read json file
    with open(json_file) as data:
        event_data = json.load(data)
    print('Json read completed for file: {}'.format(json_file))
    # Flatten the data in json file and add '_' as separator in column names
    df = pd.json_normalize(event_data, sep='_')
    print('Json normalization completed')
    # Transform the data keeping payload_id as primary key and each field denoting event time
    df = df.groupby('Payload_ID', as_index=False).first()
    print('Data transformation completed')
    # Load the data to a CSV which can be ingested into most modern databases
    df.to_csv(output_file, index=False)
    return 'Data processing completed and output file: {} has been generated'.format(output_file)


process_json('tt', 'hh')
