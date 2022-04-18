import re
import json
import requests


url = 'https://docs.google.com/forms/d/e/1FAIpQLSfAwhTYoCs5zDUq2D8QO0MWUX6YB64nyIOoiNvqsIlFPBhX8g/viewform'
html_data = requests.get(url).text

data = json.loads( re.search(r'FB_PUBLIC_LOAD_DATA_ = (.*?);', html_data, flags=re.S).group(1) )

def get_ids(d):
    if isinstance(d, dict):
        for k, v in d.items():
            yield from get_ids(v)
    elif isinstance(d, list):
        if len(d) >1 and d[1] is None:
            yield d[0]
        else:
            for v in d:
                yield from get_ids(v)

# uncomment this to print all data:
# print(json.dumps(data, indent=4))

for i in get_ids(data):
    print(i)