import sys
import os
import argparse
import pyblog_utils


if len(sys.argv) < 2:
    print('''    *** How to use pyblog ***
    Upload a blogpost from file:  python3 pyblog.py upload -f <filename>
    Update a blogpost from file by blog id:  python3 pyblog.py update -f <filename>  <id>  
    Show the latest blog post:  python3 pyblog.py latestpost
    List all blog post:  python3 pyblog.py listposts')
    Show specific blog post:  python3 pyblog.py readpost <post_id>
    Post comment to a blog post:  python3 pyblog.py postcomment <post_id> "<comment>" <author name> <author email>''')
    quit()

if (sys.argv[1].lower() == 'latestpost'):
    pyblog_utils.getposts()
    exit()
if (sys.argv[1].lower() == 'listposts'):
    pyblog_utils.listposts()
    exit()    
if (sys.argv[1].lower() == 'readpost'):
    pyblog_utils.readpost(sys.argv[2])
    exit()
if (sys.argv[1].lower() == 'postcomment'):
    pyblog_utils.postcomment(str(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5] )
    exit()
if (len(sys.argv) == 4 and sys.argv[1].lower() == 'upload' and  os.path.exists(sys.argv[3])):
    pyblog_utils.writepost(sys.argv[3])
if (len(sys.argv) == 5 and sys.argv[1].lower() == 'update' and  os.path.exists(sys.argv[4])):
    pyblog_utils.updatepost(sys.argv[4], sys.argv[2])
