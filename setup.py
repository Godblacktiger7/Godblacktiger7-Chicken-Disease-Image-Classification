import setuptools

with open ("README.md",'r',encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME="Godblacktiger7-Chicken-Disease-Image-Classification"
AUTHOR_USER_NAME="Godblacktiger7"
SRC_REPO="cnnClassifier"
AUTHOR_EMAIL="c7blacktiger@outlook.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Small Package For CNN App",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug_tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",

    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")




)