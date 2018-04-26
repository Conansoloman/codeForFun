import os
import tarfile
import pandas as pd
from six.moves import urllib
import matplotlib.pyplot as plt

DOWNLOAD_ROOT = "http://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"


def fetch_housing_data(housing_url=HOUSING_URL):
    print(1 + 2)
    tgz_path = os.path.join(os.getcwd(), 'housing.tgz')
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=os.getcwd())
    housing_tgz.close()


def loading_housing_data(housing_path=os.getcwd()):
    csv_path = os.path.join(housing_path, 'housing.csv')
    return pd.read_csv(csv_path)


if __name__ == '__main__':
    # housing = loading_housing_data()
    # print(housing.info())
    plt.plot([1, 2], [3, 4])
    plt.show()



