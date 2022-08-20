import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "10721037"))
API_HASH = getenv("API_HASH", "e26226b077080fcf940adb0778693917")
BOT_TOKEN = getenv("BOT_TOKEN", "5712910799:AAEBhNVHuiikxfyR56edyMx-uFMznVZPkjc")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "BQCPifaQ77gLHPIP_8UdQXgzuCUPe5ojVw4gCgN2JcKf8zGg7AeCUkozJyjKsy4m0rQY1eceTIiy1xlEcEYpl8BUu9ob-uBKD7W73KpsgILpHEglf59FhEPzsrwKITv2109_cxNw2B8_ilgmvpAHBJ-Ptq3BnEy5ULSu9ESMU6_PDmkJpy4KxFAtbd-9Pfx_G3hilEEAWy0CXuvBff9zAos7ga9j3CNu8J3S14naYAIcgsjZAFiBqHTC3bAGPf1wt8YbRt2XT3nHhKvCzUa3651sYxu6r7Tv7rHVSo52zvSV-JxEoAnYxJw0OggnvLJsV_LM8Y_vMEayZaSk73q8Wfx0AAAAAUmntbsA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5381983783").split()))
