# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import functools
# import re
# import ssl
# import urlparse
#
# old_match_hostname = ssl.match_hostname
#
# @functools.wraps(old_match_hostname)
# def match_hostname_bugfix_ssl_py_2_7_9(cert, hostname):
#     m = re.search(r':\d+$',hostname)  # hostname:port
#     if m is not None:
#         o = urlparse.urlparse('https://' + hostname)
#         hostname = o.hostname
#     old_match_hostname(cert, hostname)
#
# ssl.match_hostname = match_hostname_bugfix_ssl_py_2_7_9

# from Source.CLI import CLI

from CLI import CLI


def main(): 
    print("MAIN", flush=True)

if __name__ == '__main__':
    main()

cli = CLI()
cli.Start()

# See PyCharm help at https:I//www.jetbrains.com/help/pycharm/
