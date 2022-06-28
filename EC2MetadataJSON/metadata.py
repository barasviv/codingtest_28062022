import requests
import json

url = "http://169.254.169.254/latest/"


def get_metadata_json(url, key_list):
    metadata_dict = {}
    for key in key_list:
        response = requests.get(url + key)
        text = response.text
        # Below is the exception/special case for public-keys as the value returned is "0=KeyName"
        if key == "public-keys/":
            metadata_dict[key[:-1]] = get_metadata_json(url + key, ['0/'])
        # Call the function recursively for the complex keys/elements
        elif key[-1] == '/':
            metadata_dict[key[:-1]] = get_metadata_json(url + key, text.split('\n'))
        # if th value is json convert the string to dictionary and add it to response dict
        elif is_json(text):
            metadata_dict[key] = json.loads(text)
        # Simple with the string value.
        else:
            metadata_dict[key] = text
    return metadata_dict


# Return True if the string is a valid dictionary/json object
def is_json(obj):
    try:
        json.loads(obj)
    except:
        return False
    return True


# Get the value for the given key. The inpot is the dictionary and the key_path is the path in a/b/c format.
def get_value_for_key(data: dict, key_path: str):
    keys = key_path.split('/')
    print(keys)
    value = data
    for key in keys:
        try:
            value = value[key]
        except:
            return "No value found for the given key"
    return value


if __name__ == '__main__':
    # Get Metadata in json
    metadata_json = json.dumps(get_metadata_json(url, ["meta-data/"]), indent=4, sort_keys=True)
    print(f'##############The JSON output is###############\n{metadata_json}')

    # Search for the key based on the path
    key_path = "meta-data/iam/security-credentials/ecsInstanceRole/AccessKeyId"
    print(f'The value at {key_path} is {get_value_for_key(json.loads(metadata_json), key_path)}')
