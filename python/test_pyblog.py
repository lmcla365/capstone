#!/usr/bin/env python3

import pyblog


def test_wphealthcheck():
    val = pyblog_utils.wphealthcheck()
    assert val == 200

def test_readnonpost():
    val = pyblog_utils.readpost(0)
    assert val == "Post ID not valid."

def test_readpost():
    val = pyblog_utils.readpost(1)
    assert val == """Hello world!
<p>Welcome to WordPress. This is your first post. Edit or delete it, then start writing!</p>
"""

def test_getposts():
    val = pyblog_utils.getposts()
    assert val == """Hello world!
<p>Welcome to WordPress. This is your first post. Edit or delete it, then start writing!</p>
"""

def test_searchpost():
    val = pyblog_utils.searchpost("hello")
    assert val == """Hello world!
<p>Welcome to WordPress. This is your first post. Edit or delete it, then start writing!</p>
"""

def test_writepost():
    f = open("infile.txt", "a")
    f.write("Writepost test \n\nNow the file has content!")
    f.close()
    val = pyblog_utils.writepost("infile.txt")
    assert val == "Post written to Wordpress."

def test_updatepost():
    f = open("update.txt", "a")
    f.write("Updatepost test \n\nNow the file has been updated!")
    f.close()
    postid = pyblog_utils.getlastpostid()
    val = pyblog_utils.updatepost("update.txt", postid)
    assert val == "Post updated in Wordpress."

def test_postcomment():
    postid = pyblog_utils.getlastpostid()
    val = pyblog_utils.postcomment(postid,"This is a comment","student","student@example.com")
    assert val == "Comment written to Wordpress post."
