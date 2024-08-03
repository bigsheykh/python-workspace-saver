import changelogs
from changelogs.changelogs import _bootstrap_functions
import os
import json
from requests import Session
import functools
from typing import Tuple
from pip._vendor.packaging.specifiers import SpecifierSet

os.makedirs("package_infos", exist_ok=True)
packages = [
    "numpy",
    "pandas",
    "scipy",
    "celery",
    "scrapy",
    "pyyaml",
    "python-dateutil",
]

package_infos = []
INSECURE = []
with open("safety-db/data/insecure.json") as __f:
    INSECURE = json.loads(__f.read())


def is_text_useful(txt: str) -> Tuple[bool, int]:
    if "has been fixed" in txt:
        return (True, 1)
    if "has been removed" in txt:
        return (True, 2)
    if "be remove" in txt or "will remove" in txt:
        return (False, 0)
    if (
        "removed" in txt
        and "selectively removed" not in txt
        and "removed by default" not in txt
        and "make sure" not in txt
        and "removed unused" not in txt
    ):
        return (True, 2)
    if "will be fix" in txt or "when the fix" in txt or "promised a fix" in txt:
        return (True, 4)
    if "fix" in txt and "`fix" not in txt and "non-bugfix" not in txt:
        return (True, 1)

    if "add" in txt and "will be add" not in txt and "will add" not in txt:
        return (True, 3)

    return (False, 0)


for package in packages:
    if not package in INSECURE:
        INSECURE[package] = []
    package_info = {
        "name": package,
        "insecurity": [
            SpecifierSet(version, prereleases=True) for version in INSECURE[package]
        ],
    }
    file_name = os.path.join("package_infos", package)
    if not os.path.exists(file_name):
        # subprocess.getoutput([sys.executable, "-m", "changelogs", "-v", package])
        vendor = "pypi"
        name = package
        functions = {}
        fns = _bootstrap_functions(name=name, vendor=vendor, functions=functions)
        session = Session()
        session.request = functools.partial(session.request, timeout=10)
        session.max_redirects = 3

        # get meta data for the given package and use this metadata to
        # find urls pointing to a possible changelog
        data = fns["get_metadata"](session=session, name=name)
        releases = fns["get_releases"](name=name, data=data)
        urls, repos = fns["get_urls"](
            session=session,
            name=name,
            data=data,
            releases=releases,
            find_changelogs_fn=fns["find_changelogs"],
        )

        changelogs_ = {}
        for url in urls:
            try:
                resp = session.get(url)
                release_name = ""
                for release in releases:
                    if release in url:
                        release_name = release
                assert release_name != ""
                if resp.status_code == 200:
                    changelogs_[release_name] = resp.text
            except:
                pass

        package_info["changelog"] = changelogs_
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


for x in package_infos:
    print(x["name"])
    print(x["changelog"].keys())
    print(x["insecurity"])
    print()
    print()
    output_directory = "changelog-info/" + x["name"]
    os.makedirs(output_directory, exist_ok=True)
    for change_version in x["changelog"]:
        file_version = open(f"{output_directory}/{change_version}", "w")
        text = x["changelog"][change_version].split("\n")
        a = [
            (is_text_useful(txt=txt)[1], txt)
            for txt in text
            if is_text_useful(txt=txt)[0]
        ]
        for ww in a:
            file_version.write(str(ww) + "\n\n")
        file_version.close()

