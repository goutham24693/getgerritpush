from pygerrit2 import GerritRestAPI, HTTPBasicAuth


username = "username"
password = "password"
gerrit_url = "https://gerrit.abcdefgh.com/"
repo = "aaa/bbbb/ccccc/generic"


auth = HTTPBasicAuth(username, password)
rest = GerritRestAPI(url=gerrit_url, auth=auth)

commits = rest.get("/changes/?q=project:" + repo)
for commit in commits:
	if commit["status"] == "MERGED":
		print( commit["submitted"].split()[0]  + " " + commit["subject"] )