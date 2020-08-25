class Repository:
    def __init__(self):
          self.packages = {}
    def add_package(self, package):
          self.packages[package.name] = package
    def total_size(self):
        result = 0
        for package in self.packages.values():
            result += package.size
        return result


class Package:
    def __init__(self, name, size):
        self.name = name
        self.size = size


pkg1 = Package("numpy", 30)
pkg2 = Package("pandas", 40)
pkg3 = Package("django", 100)

repo1 = Repository()
repo1.add_package(pkg1)
repo1.add_package(pkg2)
repo1.add_package(pkg3)

print(repo1.total_size())

repo1.packages["numpy"].size = 60

print(repo1.total_size())
