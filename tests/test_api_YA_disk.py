import api
import pytest

def test_create_folder():
    token = 'AQAAAAAvigESAADLW_SDgmkCJUIuq3-AUBI_m-Y'
    result = api.create_folder_YADisk(token)
    try:
        assert result.status_code == 201
        print('Создал только что')
    except:
        print('Уже была создана')
        assert result.status_code == 409

def test_created_folder():
    token = 'AQAAAAAvigESAADLW_SDgmkCJUIuq3-AUBI_m-Y'
    result = api.create_folder_YADisk(token)
    print('Уже была создана')
    assert result.status_code == 409