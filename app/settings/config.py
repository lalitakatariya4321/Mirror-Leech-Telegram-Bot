from dotenv import load_dotenv
import os

class Config:
    def __init__(self):
        load_dotenv()
        self.tele_api_key = os.getenv("8584810761:AAGD9fmEjGQ0HLJHFEwER7g2cXZKzMTXhAc")
        self.save_path = os.getenv("DOWNLOAD_PATH")
        self.saved_path_link = os.getenv("DOWNLOAD_PATH_LINK")
