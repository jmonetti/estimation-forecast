from forecast.utils.singleton import Singleton


class DataAccess():
    __metaclass__ = Singleton

    def __init__(self):
        self.projects = []

    def add_project(self, new_project):
        self.projects.append(new_project)

    def add_projects(self, new_projects):
        self.projects += new_projects

    def get_projects(self):
        return self.projects

    def reset_projects(self):
        self.projects = []

    # def update_project(self, id, updated_project):
    #     for project in self.projects:
    #         if project.get('id') == id:

