"""
Enables us to download data from url on the a csv saved on local machine

Usage: src/download_data.py --url=<url> --input_path=<input_path>

Options:
--url=<url>                   Url to download data from
--input_path=<input_path>     path to the raw data file location

Example: python3 src/download_data.py --url=https://assets.datacamp.com/production/repositories/1764/datasets/79c5446a4a753e728e32b4a67138344847b8f131/Churn.csv --input_path="data/raw/customer_churn.csv"
"""

import pandas as pd
import numpy as np
import os
from docopt import docopt


def main(url, input_path):
    
    data = pd.read_csv(url)
    
    if not os.path.exists(os.path.dirname(input_path)):
        os.makedirs(os.path.dirname(input_path))
        
        data.to_csv(input_path, index= False, encoding="utf-8")
    

if __name__ == "__main__":
    opt = docopt(__doc__)
    main(opt["--url"], opt["--input_path"])
    
    