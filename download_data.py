#!/usr/bin/env python
import requests
import sys
import os

class DataDownloader:
    def __init__(self, basedir, host, token):
        self.basedir = basedir
        self.host = host
        self.s = requests.session()
        self.s.headers["Authorization"] = "Token %s" % token
        self.s.verify = False

    def same(self, filename, txt):
        real_fn = os.path.join(self.basedir, filename)
        if not os.path.exists(real_fn):
            return False

        with open(real_fn) as f:
            return f.read() == txt

    def write_file(self, filename, txt):
        real_fn = os.path.join(self.basedir, filename)
        if self.same(real_fn, txt):
            return

        temp_fn = real_fn + ".tmp"
        with open(temp_fn, 'w') as f:
            f.write(txt)
        os.rename(temp_fn, real_fn)

    def download_tables(self):
        tables = self.s.get(self.host + "/bro/api/table/").json()
        for t in tables:
            filename = "tables/%(name)s.csv" % t
            print filename
            c = self.s.get(t['flat'])
            self.write_file(filename, c.text)

    def download_regexes(self):
        regexes = self.s.get(self.host + "/bro/api/regex/").json()
        for regex in regexes:
            filename = "regexes/%(name)s.csv" % regex
            print filename
            c = self.s.get(regex['csv'])
            self.write_file(filename, c.text)

    def download(self):
        for f in self.download_tables, self.download_regexes:
            try :
                f()
            except Exception, e:
                print e

if __name__ == "__main__":
    token = os.getenv("portal_token")
    basedir = sys.argv[1]
    host = sys.argv[2]
    DataDownloader(basedir, host, token).download()
