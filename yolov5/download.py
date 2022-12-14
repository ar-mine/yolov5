import gdown
import sys
import os
import yaml

ROOT = os.path.dirname(__file__)


def download(prefix, file_id, file_name):
    url = 'https://drive.google.com/uc?id=' + file_id
    output = os.path.join(ROOT, prefix, file_name)
    gdown.download(url, output, quiet=False)


def main():
    if len(sys.argv) < 2:
        print("Usage: python download.py model_name")
    with open(os.path.join(ROOT, "model_ids.yaml"), 'r', encoding="utf-8") as f:
        file_data = f.read()

    # print(file_data)
    # print("Type: ", type(file_data))

    data = yaml.load(file_data, Loader=yaml.FullLoader)
    if sys.argv[1] in data.keys():
        contains = data[sys.argv[1]]
        download('data', contains['data']['link'], contains['data']['file'])
        download('models', contains['models']['link'], contains['models']['file'])


if __name__ == "__main__":
    main()



