import requests, os, zipfile, io

download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
]


def main():
    # your code here
    cwd = os.getcwd()
    directory =  cwd + "/downloads"
    if not os.path.exists(directory):
        os.makedirs(directory)


    for i in download_uris:
        filename = requests.get(i)
        if filename.status_code == 200:
            z = zipfile.ZipFile(io.BytesIO(filename.content))
            z.extractall(directory)
            print("200")
    return("Finished")

    pass


if __name__ == '__main__':
    main()
