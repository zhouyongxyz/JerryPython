#!/usr/bin/python3

import sqlite3

def main():
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")

if __name__ == "__main__":
    main()