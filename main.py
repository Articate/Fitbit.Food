#!/usr/bin/env python
from kolonial.search import Search

class Program:
    def __init__(self):
        pass

    @staticmethod
    def run():
        s = Search()
        s.query("philadelphia")
        s.find_info(4786)

if __name__ == "__main__":
    Program.run()
