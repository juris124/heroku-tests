import os
from github import Github

​def commitFile(fname):
    #gh_key = os.environ['GH_KEY']
    # using an access token
    # Create token - https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line
    g = Github("430482994867d92906262f3fc1055dac3288db0d")
​
    repo = g.get_repo("juris124/heroku-tests")
    print(repo.name)
    with open(fname, "r") as f:
        # Docs https://pygithub.readthedocs.io/en/latest/examples/Repository.html#create-a-new-file-in-the-repository
        # Reference https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository.create_file
        c = repo.create_file(fname, "test commit from script", f.read())
    print(c)
​
​
commitFile("testa_fails.txt")