import pytest
from concurrent.futures import ThreadPoolExecutor, as_completed
import yaml

from common_functions import get_output_command


def test_find_route_in_devs():
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(get_output_command, device) for device in devices]
        for future in as_completed(futures):
            result = future.result()
            assert '10.111.11.0' in result, f'Маршрут 10.111.11.0 отсутсвует на устройстве {result[0]}'
