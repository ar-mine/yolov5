import gdown
import sys
import os
import yaml
import argparse

ROOT = os.path.dirname(__file__)


def download(prefix, file_id, file_name):
    url = 'https://drive.google.com/uc?id=' + file_id
    output = os.path.join(ROOT, prefix, file_name)
    gdown.download(url, output, quiet=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", help="The predefined model to be downloaded.")
    parser.add_argument("-l", "--list", help="List all the models that can be downloaded.", action="store_true")
    args = parser.parse_args()

    with open(os.path.join(ROOT, "model_ids.yaml"), 'r', encoding="utf-8") as f:
        file_data = f.read()
        data = yaml.load(file_data, Loader=yaml.FullLoader)
    key_list = list(data.keys())

    if args.list:
        print("The supported models is" + "".join(key_list))

    if args.name in key_list:
        contains = data[args.name]
        download('data', contains['data']['link'], contains['data']['file'])
        download('models', contains['models']['link'], contains['models']['file'])
    else:
        print("Wrong model's name, the supported models is" + "".join(key_list))


if __name__ == "__main__":
    main()



