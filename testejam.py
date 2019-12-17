import os
from github import Github


def commitFile(fname):
    #gh_key = os.environ['GH_KEY']
    # using an access token
    # Create token - https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line
    g = Github("4c03f031f471a24a49ba2b39488764c6298da10c")
    repo=g.get_repo("juris124/heroku-tests")

    with open(fname, "r", encoding='utf-8') as f:
        dircont = repo.get_dir_contents("/static/dati")
        for fn in dircont:
            print(fn.path)
            if fn.path == fname:
                contents = repo.get_contents(fname)
                repo.update_file(contents.path, "Faila augšupielāde", f.read(), contents.sha)
                break
        else:
            c = repo.create_file(fname, "test commit from script", f.read())
            print(c)
        
    print(repo.name)
    
        # Docs https://pygithub.readthedocs.io/en/latest/examples/Repository.html#create-a-new-file-in-the-repository
        # Reference https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository.create_file
        
    
commitFile("static/dati/20191210_html1.csv")
 