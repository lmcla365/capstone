# Created By  : NULL Capstone Cohort7 Team
# Created Date: 7/22
# version ='1.0'
# Methods for accessing Wordpress API V:2
import sys
import os

# import argparse
import pyblog_utils

# 1st check if wordpress is running.
if pyblog_utils.wphealthcheck() != 200:
    print("Wordpress is currently down, check if site is running")
    exit()

arglen = len(sys.argv)
if arglen < 2 or sys.argv[1].lower() == "help":
    print(
        """    *** How to use pyblog ***
    Upload a blogpost from file:  python3 pyblog.py upload -f <filename>
    Update a blogpost from file by blog id:  python3 pyblog.py update -f <filename>  <id>
    Show the latest blog post:  python3 pyblog.py latestpost
    List all blog post:  python3 pyblog.py listposts')
    Show specific blog post:  python3 pyblog.py readpost <post_id>
    Post comment to a blog post:  python3 pyblog.py postcomment <post_id> "<comment>" <author name> <author email>"""
    )
    exit()

argv1 = sys.argv[1].lower()
if arglen == 2:
    if (argv1 == "latestpost"):
        resp = pyblog_utils.getposts()
    elif (argv1 == "listposts"):
        resp = pyblog_utils.listposts()
    else:
        exit()
if arglen == 3:
    argv2 = sys.argv[2].lower()
    if (argv1 == "readpost"):
        resp = pyblog_utils.readpost(sys.argv[2])
    elif (argv1 == "searchpost"):
        resp = pyblog_utils.searchpost(sys.argv[2])
    else:
        exit()
if arglen > 3:
    if (argv1 == "postcomment"):
        resp = pyblog_utils.postcomment(str(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5] )
    elif (arglen == 4 and argv1 == "upload" and  os.path.exists(sys.argv[3])):
        resp = pyblog_utils.writepost(sys.argv[3])
    elif (arglen == 5 and argv1 == "update" and  os.path.exists(sys.argv[4])):
        resp = pyblog_utils.updatepost(sys.argv[4], sys.argv[2])
    else:
        exit()
print(resp)
