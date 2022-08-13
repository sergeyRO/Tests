import requests

def create_folder_YADisk(token):
    url = 'https://cloud-api.yandex.net:443'
    params = {'path': 'TEST_FOLDER'}
    headers = {"Authorization": token}
    response = requests.put(url + '/v1/disk/resources', headers=headers, params=params)
    return response

if __name__ == '__main__':
    TOKEN_YA_DISK = 'AQAAAAAvigESAADLW_SDgmkCJUIuq3-AUBI_m-Y'
    create_folder_YADisk(TOKEN_YA_DISK)