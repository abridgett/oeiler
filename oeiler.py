#!/usr/bin/env python3

import urllib.parse
import urllib.request

# From http://www.europarl.europa.eu/oeil/search/search.do
SEARCH_BASE = "http://www.europarl.europa.eu/oeil/popups/printresultlist.xml"
# TODO: No idea what these are
SEARCH_EXTRA = "all&s1&"

PROCEDURETYPE_SID = {"Interinstitutional ordinary legislative procedures": 573004}

STAGEREACHED_SID = {"Completed": "PROC_T"}


def buildurl(proceduretype=None, stagereached=None):
    params = {}
    params = {"searchTab": "y", "snippet": "true", "lang": "en", "dismax": "y"}
    if proceduretype:
        params[":procedureType_sid"] = PROCEDURETYPE_SID[proceduretype]
    if stagereached:
        params[":stageReached_sid"] = STAGEREACHED_SID[stagereached]
    url = SEARCH_BASE + "?" + SEARCH_EXTRA + urllib.parse.urlencode(params)
    # TODO = add "limit=100000"
    return url

def fetchurl(url, filename):
    print("Fetching file %s from %s" % (filename, url))
    urllib.request.urlretrieve(url, filename)
    print("Fetch complete")

def getxml_legal(filename):
    url=buildurl(proceduretype="Interinstitutional ordinary legislative procedures",
    stagereached="Completed")
    fetchurl(url, filename)

def getxml_all(filename):
    url=buildurl()
    print("Fetching file %s from %s" % (filename, url))
    urllib.request.urlretrieve(url, filename)
    print("Fetch complete")

if __name__ == "__main__":
    #getxml_legal("legal.xml")
    getxml_all("all.xml")
