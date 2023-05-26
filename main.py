# Installing required libraries

from flask import Flask, request
from flask_cors import CORS
import requests
import pandas as pd
import numpy as np
import pickle
import nltk
import re
from datetime import datetime,timedelta,date,timezone
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

app = Flask(__name__)
CORS(app)

if (__name__=='__main__'):
    app.run()

