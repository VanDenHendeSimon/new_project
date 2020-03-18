from github import Github
from GUI import GUI
import os


class NewProject:
    def __init__(self):
        self.user = None
        self.login()

        self.ui = GUI(self)
        self.ui.open()

        print([repo.name for repo in self.user.get_repos()])

    @staticmethod
    def get_credentials():
        with open("creadentials.txt", "r") as f:
            data = [line.rstrip("\n") for line in f.readlines()]

        return data

    def login(self):
        credentials = self.get_credentials()

        if len(credentials) == 2:
            g = Github(credentials[0], credentials[1])
            self.user = g.get_user()

    def create_repo(self, name, description, private):
        repo = self.user.create_repo(
            name=name,
            description=description,
            private=private,
            auto_init=True
        )

        print("Get path from execution location (. after call)")
        print(repo.html_url)
        # os.system("cd %s" % sys.argv[1])
        # os.system("git clone %s" % repo.html_url)


if __name__ == '__main__':
    project = NewProject()
