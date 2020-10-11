from requests_html import HTML, HTMLSession
from bs4 import BeautifulSoup
import concurrent.futures
import requests
import docx
import time
import random
import zipfile
from io import BytesIO


# TASK
class Copycase:
    def __init__(self, uque):
        self.uque = uque
        self.prev_st = 0

    def sort_que(self):  # seperate each
        self.uquelist = self.uque.split(',')
        print(f'Sorted query: {self.uquelist}')

    def rev_list(self):  # remove spaces from 0
        uql = self.uquelist
        for xn in range(len(uql)):
            x = uql[xn]
            if x[0] == ' ':
                uql[xn] = x[1:]
        print(f'Proper query: {uql}')
        return uql

