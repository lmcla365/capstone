#!/usr/bin/env python3

import pyblog


def test_wphealthcheck():
    val = wphealthcheck()
    assert val == 200
    
def test_readpost():
    val = readpost(1)
    assert val == """Hello world!
    Welcome to WordPress. This is your first post. Edit or delete it, then start writing!
    """

def test_getposts():
    val = getposts()
    assert val == """Hello world!
    Welcome to WordPress. This is your first post. Edit or delete it, then start writing!
    """

def test_listposts():
    val = listposts()
    assert val == """Post ID    Post Title
    6       test post
    1       Hello world!
    """

def test_writepost():
    val = writepost('Test_Title','Test_Content')
    assert val == 'Post written to Wordpress.'
