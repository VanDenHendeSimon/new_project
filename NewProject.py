from github import Github
from GUI import GUI
import os
import sys


class NewProject:
    def __init__(self):
        self.script_folder = self.get_script_folder()

        self.user = None
        self.login()

        self.ui = GUI(self)
        self.ui.open()

    @staticmethod
    def get_script_folder():
        try:
            dist_folder = next(
                f for f in os.environ["Path"].split(";")
                if "new_project" in f
            )
            # Go up one directory
            return dist_folder[:dist_folder.rfind("\\")]
        except Exception:
            # Quit
            exit("Failed to locate script folder.")

    def get_credentials(self):
        try:
            credentials = os.path.join(self.script_folder, "credentials.txt")
            with open(credentials, "r") as f:
                data = [line.rstrip("\n") for line in f.readlines()]

            return data

        except Exception:
            return None

    def login(self):
        credentials = self.get_credentials()

        if credentials:
            if len(credentials) >= 2:
                g = Github(credentials[0], credentials[1])
                self.user = g.get_user()
        else:
            print("Failed to fetch credentials")

    def create_repo(self, name, description, private):
        try:
            repo = self.user.create_repo(
                name=name,
                description=description,
                private=private,
                auto_init=True
            )

            # Cloning repo
            os.system("git clone %s" % repo.html_url)
            os.system("code %s" % os.path.join(os.path.dirname(os.path.abspath(__file__)), name))

        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    project = NewProject()
