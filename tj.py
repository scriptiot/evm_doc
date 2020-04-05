import sys
import os
import re

EXCLUDE_DIRS = [
    "C:\\Users\\codemao\\Desktop\\workspcae\\evm\\build",
    "C:\\Users\\codemao\\Desktop\\workspcae\\evm\\release",
    "C:\\Users\\codemao\\Desktop\\workspcae\\evm\\libevm"
]

def getCHppFiles(rootpath):
    hfiles = []
    cppfiles = []
    cfiles = []
    for root, dirs, files in os.walk(rootpath) :
        if '.git' not in root:
            for f in files:
                fpath = os.path.abspath(os.sep.join([root, f]))

                isExclude = False
                for d in EXCLUDE_DIRS:
                    if fpath.startswith(d):
                        isExclude = True
                if isExclude:
                    # print(fpath)
                    continue
                if fpath.endswith(".h"):
                    hfiles.append(fpath)
                elif fpath.endswith(".cpp") or f.endswith(".c"):
                    cppfiles.append(fpath)
    return hfiles, cppfiles

def count(path, apis):
    ret = {}
    with open(path, "rb") as f:
        content = str(f.read())
        for api in apis:
            ret[api] = content.count(api)
    return ret

def main():
    apis = []
    with open("C:\\Users\\codemao\\Desktop\\workspcae\\evm\\libevm\\evm.h", "rb") as f:
        for line in f.readlines():
            s = str(line)
            if "evm_" in s:
                x = re.search("\sevm_.*", s)
                if x and "(" in x.string:
                    es = x.string[x.start():].split("(")[0]
                    # if " " not in es:
                    api = es.split(" ")[1]
                    if api not in apis:
                        apis.append(api)

    _, cFiles = getCHppFiles("C:\\Users\\codemao\\Desktop\\workspcae\\evm\\native")
    apis = apis[1:]

    rets = {}
    for f in cFiles:
        ret = count(f, apis)
        if len(rets) == 0:
            rets = ret
        else:
            for key in ret:
                rets[key] += ret[key]
    # print(rets)
    rets = sorted(rets.items(), key=lambda item:item[1], reverse=True)
    with open("apis_call_count_third.md", "wb") as f:
        for item in rets:
            f.write(("%30s:%d\r\n" % (str(item[0]), item[1])).encode())

    # for api in apis:
        # count()

if __name__ == '__main__':
    main()
