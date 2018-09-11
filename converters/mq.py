import os
import sys
import logging
import pymysql
import datetime
import time
import re
import json




if __name__ == '__main__':
    with open("../raw/movie_quotes.txt", "r") as ins:
        is_new_line = False

        with open("../raw/movie_quotes.yml", "a") as myfile:

            in_map = {}
            latest_question = ''

            for line in ins:
                str_line = str(line)
                line = line.replace(":", "").replace("\"", "").replace("}", "").replace("*", "")
                if line[0] == "'":
                    line = line[1:]

                if str_line[0].isdigit() and str_line[1].isdigit() and str_line[2].isdigit():
                    print("NUMBER LINE : " + line)

                elif line in ['\n', '\r\n']:
                    print("NEW LINE : " + line)
                    is_new_line = True
                else:
                    if is_new_line:
                        print("QUESTION LINE : " + line)

                        line = line.rstrip()

                        if line not in in_map:
                            in_map[line] = []
                        else:
                            latest_question = line


                        #myfile.write("- - " + line)
                        is_new_line = False
                    else:
                        print("RESPONSE LINE : " +  line)

                        if latest_question != '':
                            line = line.rstrip()
                            in_map[latest_question].append(line)


                        #myfile.write("  - " + line)


            #print(in_map)
            for key, value in in_map.iteritems():
                myfile.write("- - " + key + "\n")
                for v in value:
                    myfile.write("  - " + v + "\n")


