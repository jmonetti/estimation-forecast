from forecast.utils.singleton import Singleton


class DataAccess():
    __metaclass__ = Singleton

    def __init__(self):
        self.projects = []

    def add_projects(self, new_projects):
        self.projects += new_projects

    def get_projects(self):
        return self.projects


