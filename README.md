# DataProcessing
Develop Python script to process Json data and generate a csv file which can be consumed by database

  **Process:**
  The script is written in a simple way using Pandas library to perform Json normalization and to generate output file.
  
  **Assumptions:**
  While Developing the script, the following points were taken into consideration
  1. Data format used should be supported by most of the modern databases.
  2. Generated output should be in a normalized way where further transformations in datbase won't be required.
  3. 'Type' column has been removed, since requirement is to get data related to Sent, Delivered, Opened, Clicked, and Paid.

  **Usage:**
  since AWS was mentioned in job description, the following will be my approach in AWS.
  1. Scenario 1 - If the input Json files are small, I would recommend using AWS lambda to process the input file and deliver the output to S3. If you are using Aurora or redshift or snowflake, we can integrate the copy command in same script to laod data to database. We can also integrate S3 events to Lambda and viceversa to make the full process automated. This process is very Cost effective.
  2. Scenario 2 - If the volume of data is moderate, I would recommend using AWS Glue to run the Python Script. The only limitation is Glue takes some time to warm up, if the event processing has to happen in real time, this could be a problem.
  3. Scenario 3 - If we are handling large amount of volume, we can use EMR to process the data.
  
  **Sample Output:**
  Payload_ID	RecordedAt	Payload_SentAt	Payload_UndeliveredAt	Payload_DeliveredAt	Payload_OpenedAt	Payload_ClickedAt	Payload_SubmittedAt	Payload_EmailID
0001a8b8-03d3-4349-ba00-2a86c77888f4	2021-11-04T13:26:10Z	2021-11-04T13:26:10Z	2021-11-04T13:26:10Z					
0002ec94-081a-4e7d-b2f1-c6c849797c54	2021-01-20T17:41:55Z	2021-01-20T17:41:55Z	2021-01-20T17:41:55Z					
00098283-0c8e-435f-a185-8657d64558f5	2021-03-01T10:31:18Z	2021-03-01T10:31:18Z		2021-03-01T10:32:18Z	2021-03-01T11:23:18Z	2021-03-01T11:23:18Z		
000b2a91-680f-4c61-a73d-0c1b26d7e232	2021-02-13T23:45:11Z	2021-02-13T23:45:11Z		2021-02-13T23:46:11Z				
0015c996-4f74-4a4c-8e31-a5fda336b3b7	2021-07-18T13:07:27Z	2021-07-18T13:07:27Z		2021-07-18T13:07:27Z				
00207e7e-e9cd-4c2a-9200-3d7499bbcddc	2021-07-29T19:38:30Z	2021-07-29T19:38:30Z		2021-07-29T19:38:30Z				
00232f27-a699-4167-834b-b3356b996d9f	2021-11-26T13:49:51Z	2021-11-26T13:49:51Z		2021-11-26T13:49:51Z				
002355bb-9d12-476b-b14e-1571e8b2413e	2021-03-16T11:59:23Z	2021-03-16T11:59:23Z		2021-03-16T11:59:23Z				
0023d20e-e491-48d6-87fd-91111fdd2a7d	2021-06-12T16:39:39Z	2021-06-12T16:39:39Z		2021-06-12T16:40:39Z				
0023d534-f82b-4282-b2ad-512f37339a69	2021-01-18T08:42:52Z	2021-01-18T08:42:52Z		2021-01-18T08:42:52Z				
