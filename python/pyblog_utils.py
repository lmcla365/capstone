import requests
import json
import base64
import os
import fileinput


# base_url = 'http://localhost:8080/'
errorstr = "Check the supplied arguments and user credentials defined in Application Passwords. Error: "
base_url = os.environ.get("WORDPRESSURL")  # , "http://3.80.76.206:8080/")
apiuser = os.environ.get("APIUSER")  # , "student")
apipwd = os.environ.get("APIPWD")  # , "lp3P xt98 GFXx TzB0 cwmB 7bVO")
if isinstance(apiuser, str):
    credentials = apiuser + ":" + apipwd
else:
    print('Set system varibles on target system for WORDPRESSURL, APIUSER, APIPWD')
    exit()
token = base64.b64encode(credentials.encode())

# Read file contents from stdin files
def readinfile(infile):
    ctr = 0
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
    header = {"Authorization": "Basic " + token.decode("utf-8")}
    response = requests.get(url, headers=header)
    if str(response.status_code)[0] == "2":
        response_json = response.json()
        print(response_json[0].get("title").get("rendered"))
        print(response_json[0].get("content").get("rendered"))
    else:
        print(errorstr + str(response.status_code))


# Get all posts and pass latest to readpost
def getposts():
    url = base_url + "/wp-json/wp/v2/posts"
    header = {"Authorization": "Basic " + token.decode("utf-8")}
    response = requests.get(url, headers=header)
    if str(response.status_code)[0] == "2":
        response_json = response.json()
        print(response_json[0].get("id"))
        readpost(response_json[0].get("id"))
    else:
        print(errorstr + str(response.status_code))


# Lists all posts by id and title
def listposts():
    url = base_url + "/wp-json/wp/v2/posts"
    header = {"Authorization": "Basic " + token.decode("utf-8")}
    response = requests.get(url, headers=header)
    if str(response.status_code)[0] == "2":
        response_json = response.json()
        print("Post ID    Post Title")
        i = 0
        while i < len(response_json):
            print(
                response_json[i].get("id"),
                "     ",
                response_json[i].get("title").get("rendered"),
            )
            i += 1
    else:
        print(errorstr + str(response.status_code))

def searchpost(search):
    url = base_url + "/wp-json/wp/v2/posts?search=" + search
    print(url)
    header = {'Authorization': 'Basic ' + token.decode('utf-8')}
    response = requests.get(url , headers=header)
    if str(response.status_code)[0] == '2':
        response_json = response.json()
        print(response_json[0].get('title').get('rendered'))
        print(response_json[0].get('content').get('rendered'))
    else:
        print(errorstr + str(response.status_code))

def writepost(infile):
    title, content = readinfile(infile)
    url = base_url + "/wp-json/wp/v2/posts"
    header = {"Authorization": "Basic " + token.decode("utf-8")}
    post = {"title": title, "status": "publish", "content": content}
    response = requests.post(url, headers=header, json=post)
    if str(response.status_code)[0] == "2":
        print("Post written to Wordpress.")
    else:
        print(errorstr + str(response.status_code))


def updatepost(infile, id):
    title, content = readinfile(infile)
    print("title::: ", title)
    url = base_url + "/wp-json/wp/v2/posts/" + str(id)
    print(url)
    header = {"Authorization": "Basic " + token.decode("utf-8")}
    post = {
        "title": title,
        "status": "publish",
        "format": "standard",
        "content": content,
    }
    response = requests.post(url, headers=header, json=post)
    if str(response.status_code)[0] == "2":
        print("Post updated in Wordpress.")
    else:
        print(errorstr + str(response.status_code))


def postcomment(id, MyComment, author_name, author_email):
    url = base_url + "/wp-json/wp/v2/comments"
    header = {"Authorization": "Basic " + token.decode("utf-8")}
    post = {
        "post": id,
        "content": MyComment,
        "author_name": author_name,
        "author_email": author_email,
    }
    response = requests.post(url, headers=header, json=post)
    if str(response.status_code)[0] == "2":
        print("Comment written to Wordpress post.")
    else:
        print(errorstr + str(response.status_code))
