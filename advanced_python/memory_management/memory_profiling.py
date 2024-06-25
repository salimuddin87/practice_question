"""
We will be using memory-profiler from PyPi. We will also be needing requests to test the functionality.
To do so, simply type the following in your terminal
    pip3 install memory-profiler requests

Note:- An important thing to remember is that memory-profiler itself consumes a significant amount of
        memory. Use this only in development but avoid it in production.
"""


from memory_profiler import profile
import requests


class BaseExtractor:
    # decorator which specifies which
    # function to monitor
    @profile
    def parse_list(self, array):
        # create a file object
        f = open('words.txt', 'w')
        for word in array:
            # writing words to file
            f.writelines(word)

        # decorator which specifies which

    # function to monitor
    @profile
    def parse_url(self, url):
        # fetches the response
        response = requests.get(url).text
        with open('url.txt', 'w') as f:
            # writing response to file
            f.writelines(response)


"""
Notice the @profile this is a decorator. Any function which is decorated by this decorator, that function 
will be tracked. Now, our main code is ready. Let’s write the driver code which will call this class functions.
"""
if __name__ == "__main__":
    # url for word list (huge)
    url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'

    # word list in array
    array = ['one', 'two', 'three', 'four', 'five']

    # initializing BaseExtractor object
    extractor = BaseExtractor()

    # calling parse_url function
    extractor.parse_url(url)

    # calling pasrse_list function
    extractor.parse_list(array)

"""
So, basically now we are done. You will notice that parse_url() will consume more memory than parse_list() 
which is obvious because parse_url calls a URL and writes the response content to a text file. If you open 
the link, then you will find that the word list is huge.
"""

# output:-
"""
Filename: C:\Users\md_salimuddin_ansari\PycharmProjects\practice_question\advanced_python\memory_management\memory_profiling.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    28     27.9 MiB     27.9 MiB           1       @profile
    29                                             def parse_url(self, url):
    30                                                 # fetches the response
    31     34.2 MiB      6.4 MiB           1           response = requests.get(url).text
    32     34.2 MiB      0.0 MiB           1           with open('url.txt', 'w') as f:
    33                                                     # writing response to file
    34     34.3 MiB      0.0 MiB           1               f.writelines(response)


Filename: C:\Users\md_salimuddin_ansari\PycharmProjects\practice_question\advanced_python\memory_management\memory_profiling.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    17     29.6 MiB     29.6 MiB           1       @profile
    18                                             def parse_list(self, array):
    19                                                 # create a file object
    20     29.6 MiB      0.0 MiB           1           f = open('words.txt', 'w')
    21     29.6 MiB      0.0 MiB           6           for word in array:
    22                                                     # writing words to file
    23     29.6 MiB      0.0 MiB           5               f.writelines(word)
    24                                         
    25                                                 # decorator which specifies which


Process finished with exit code 0
"""
