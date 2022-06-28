# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# noinspection PyBroadException
def get_in(data: dict, key_path: str):
    keys = key_path.split('/')
    value = data
    for key in keys:
        try:
            value = value[key]
        except:
            return "No value found for the given key"
    return value


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    object1 = {"a": {"b": {"c": "d"}}}
    print(get_in(object1, "a/b/c"))
