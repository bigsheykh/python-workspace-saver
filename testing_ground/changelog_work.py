import changelogs
from changelogs.changelogs import _bootstrap_functions
import os
import json
import sys
from requests import Session
import functools

os.makedirs("package_infos", exist_ok=True)
packages = [
    "numpy",
    "pandas",
    "scipy",
    "celery",
    "scrapy",
    "pyyaml",
    "python-dateutil", ]

package_infos = []
INSECURE = []
with open("safety-db/data/insecure.json") as __f:
    INSECURE = json.loads(__f.read())


for package in packages:
    if not package in INSECURE:
        INSECURE[package] = []
    package_info = {"name": package, "insecurity": INSECURE[package]}
    file_name = os.path.join("package_infos", package)
    if not os.path.exists(file_name):
        # subprocess.getoutput([sys.executable, "-m", "changelogs", "-v", package])
        # vendor="pypi"
        # name = package
        # functions = {}
        # fns = _bootstrap_functions(name=name, vendor=vendor, functions=functions)
        # session = Session()
        # session.request = functools.partial(session.request, timeout=10)
        # session.max_redirects = 3

        # # get meta data for the given package and use this metadata to
        # # find urls pointing to a possible changelog
        # data = fns["get_metadata"](session=session, name=name)
        # releases = fns["get_releases"](name=name, data=data)
        # urls, repos = fns["get_urls"](
        #     session=session,
        #     name=name,
        #     data=data,
        #     releases=releases,
        #     find_changelogs_fn=fns["find_changelogs"]
        # )
        # print(name)
        # print(urls)
        # print(repos)
        # print(releases)
        # print(data)
        # print()
        # print()
        # print()
        # print()
        # # https://github.com/numpy/numpy/releases/download/v2.0.1/2.0.1-changelog.rst
        # # https://github.com/numpy/numpy/tree/main/doc/changelog

        # # https://pandas.pydata.org/docs/_sources/whatsnew/v2.2.2.rst.txt
        # # https://github.com/pandas-dev/pandas/tree/main/doc/source/whatsnew

        # ## https://github.com/scipy/scipy/tree/main/doc/source/release
        # ## https://github.com/celery/celery/blob/main/docs/history
        # # https://github.com/scrapy/scrapy/blob/2.11/docs/news.rst

        
        package_info["changelog"] = changelogs.get(package)
        if len(package_info["changelog"]) > 0:
            x = open(os.path.join("package_infos", package), "w")
            x.write(json.dumps(package_info["changelog"]))
            x.close()
        else:
            package_info["changelog"] = changelogs.get(package)
    else:
        with open(file_name) as __f:
            package_info["changelog"] = json.loads(__f.read())
    package_infos.append(package_info)
    
x = open(os.path.join("package_infos", "all"), "w")
x.write(json.dumps(package_infos))
x.close()
