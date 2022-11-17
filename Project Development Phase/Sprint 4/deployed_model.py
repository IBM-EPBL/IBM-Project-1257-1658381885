import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "_6Vrqs5_bsVKms1b6wlT389sAA5vH5ROR54gnOVznPMz"
token_response = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/b12fd7e9-7f2c-4b09-9810-cd5503af9bf2/predictions?version=2022-11-17', data={"apikey":
API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [[[[0.61645854, 0.54194874, 0.557635  ], [0.6257725 , 0.5512627 , 0.56694895],         [0.62695605, 0.55244625, 0.5681325 ]]]], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/b12fd7e9-7f2c-4b09-9810-cd5503af9bf2/predictions?version=2022-11-17', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())