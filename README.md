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
![image](https://user-images.githubusercontent.com/79067835/148237752-9174f058-bbf9-4238-be19-dde63374134b.png)

