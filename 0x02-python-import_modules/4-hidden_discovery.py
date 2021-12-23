#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for file_name in dir(hidden_4):
        if file_name[1] != "_":
            print(file_name)
