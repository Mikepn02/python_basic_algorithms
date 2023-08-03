import requests

url='https://www.py4e.com/code3/mbox.txt'
original_file_name = "mbox.txt"
filtered_file_name = "filtered_mbox.txt"
try:
    response =  requests.get(url)
    if response.status_code == 200:
        lines = response.text.splitlines()
        filtered_lines = [line for line in lines if "Received" in line]
        with open(filtered_file_name, "w", encoding="utf-8") as file:
            file.write("\n".join(filtered_lines))
        print(f"Filtered file '{filtered_file_name}' created successfully.")
    else:
        print(f"Failed to download the file. Status Code: {response.status_code}")
except requests.RequestException as e:
    print(f"An error occurred while downloading the file: {e}")        