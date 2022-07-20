import requests
import base64
import os
import fileinput

errorstr = "Check the supplied arguments and user credentials defined in Application Passwords. Error: "
base_url = os.environ.get("WORDPRESSURL")  # , "http://3.80.76.206:8080/")
apiuser = os.environ.get("APIUSER")  # , "student")
apipwd = os.environ.get("APIPWD")  # , "lp3P xt98 GFXx TzB0 cwmB 7bVO")
if isinstance(apiuser, str):
    credentials = apiuser + ":" + apipwd
else:
    print("Set system varibles on target system for WORDPRESSURL, APIUSER, APIPWD")
    exit()
token = base64.b64encode(credentials.encode())
header = {"Authorization": "Basic " + token.decode("utf-8")}
resp = ""

def wphealthcheck():
    page = requests.get(base_url)
    # print(type(page))
    return int(page.status_code)


# Read file contents from stdin files
def readinfile(infile):
    ctr = 0
    title = ""
    content = ""
    for line in fileinput.input(files=(infile)):
        if ctr < 1:
            title = line
            ctr += 1
        else:
            content += line
    return (title, content)


# Read latest post
def readpost(id):
    url = base_url + "/wp-json/wp/v2/posts?include=" + str(id)
    response = requests.get(url, headers=header)
    if response.json() == []:
        resp = "Post ID not valid."
    elif str(response.status_code)[0] == "2" and response.json() != []:
        response_json = response.json()
        resp = (
            response_json[0].get("title").get("rendered")
            + "\n"
            + response_json[0].get("content").get("rendered")
        )
    else:
        resp = errorstr + str(response.status_code)
    return resp


# Get all posts and pass latest to readpost
def getposts():
    url = base_url + "/wp-json/wp/v2/posts"
    response = requests.get(url, headers=header)
    if str(response.status_code)[0] == "2":
        response_json = response.json()
        resp = readpost(response_json[0].get("id"))
    else:
        resp = errorstr + str(response.status_code)
    return resp


def getlastpostid():
    url = base_url + "/wp-json/wp/v2/posts"
    response = requests.get(url, headers=header)
    if str(response.status_code)[0] == "2":
        response_json = response.json()
        resp = response_json[0].get("id")
    else:
        resp = errorstr + str(response.status_code)
    return resp


# Lists all posts by id and title
def listposts():
    url = base_url + "/wp-json/wp/v2/posts"
    response = requests.get(url, headers=header)
    if str(response.status_code)[0] == "2":
        response_json = response.json()
        resp = "Post ID    Post Title\n"
        i = 0
        while i < len(response_json):
            resp += (
                str(response_json[i].get("id"))
                + "     "
                + response_json[i].get("title").get("rendered")
                + "\n"
            )
            i += 1
    else:
        resp = errorstr + str(response.status_code)
    return resp


# search post by keyword
def searchpost(search):
    url = base_url + "/wp-json/wp/v2/posts?search=" + search
    response = requests.get(url, headers=header)
    if str(response.status_code)[0] == "2":
        response_json = response.json()
        resp = (
            response_json[0].get("title").get("rendered")
            + "\n"
            + response_json[0].get("content").get("rendered")
        )
    else:
        resp = errorstr + str(response.status_code)
    return resp


def writepost(infile):
    title, content = readinfile(infile)
    url = base_url + "/wp-json/wp/v2/posts"
    post = {"title": title, "status": "publish", "content": content}
    response = requests.post(url, headers=header, json=post)
    if str(response.status_code)[0] == "2":
        resp = "Post written to Wordpress."
    else:
        resp = errorstr + str(response.status_code)
    return resp


def updatepost(infile, id):
    title, content = readinfile(infile)
    url = base_url + "/wp-json/wp/v2/posts/" + str(id)
    post = {
        "title": title,
        "status": "publish",
        "format": "standard",
        "content": content,
    }
    response = requests.post(url, headers=header, json=post)
    if str(response.status_code)[0] == "2":
        resp = "Post updated in Wordpress."
    else:
        resp = errorstr + str(response.status_code)
    return resp


def postcomment(id, MyComment, author_name, author_email):
    url = base_url + "/wp-json/wp/v2/comments"
    post = {
        "post": id,
        "content": MyComment,
        "author_name": author_name,
        "author_email": author_email,
    }
    response = requests.post(url, headers=header, json=post)
    if str(response.status_code)[0] == "2":
        resp = "Comment written to Wordpress post."
    else:
        resp = errorstr + str(response.status_code)
    return resp
