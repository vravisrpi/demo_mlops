import os

dirs=[
    os.path.join("data","raw"),
    os.path.join("data","processed"),
    "notebooks",
    "saved_models",
    "src"
]

for dir_ in dirs:
    os.makedirs(dir_,exist_ok=True)
    with open (os.path.join(dir_,".gitkeep"),"w") as f: #Since these are empty directors, we won't be able to push to git, so we are dumping .gitkeep file in each dir
        pass 


files=[
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py")
]

for file_ in files:
    with open (file_,"w") as f:
        pass
