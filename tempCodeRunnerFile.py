import os
import pickle
from typing import Optional, List,Dict,Any,Tuple

import numpy as np 
import pandas as pd 
import httpx 
from fastapi import FASTAPI,HTTPException,Query
from fastapi.middleware.core import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv