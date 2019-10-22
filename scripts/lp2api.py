#!/usr/bin/env python3

import requests
import yaml
from pprint import pprint
from os import walk

# path_to_lp = (
#     "/home/ubuntu/projects/atc-api/tests/files/"
#     "LP_0003_windows_sysmon_process_creation.yml"
# )

lp_dir = '/home/ubuntu/projects/atomic-threat-coverage/logging_policies'

dirpath, _, filenames = next(walk(lp_dir))

for file in filenames:

    with open(dirpath + "/" + file, 'r') as stream:
        lp = yaml.safe_load(stream)

    r = requests.post(
        'http://127.0.0.1:8000/api/v1/atc/loggingpolicy/',
        json=lp
    )

    if r.status_code != 200:
        pprint(file)
        pprint(r.text)

# pprint(r.text)
