class Resources:
    def __init__(self):
        links = {}
        links["github"] = "https://github.com/Islanderrobotics/irdatacleaning"
        for i in links.keys():
            print(f"the link to {i} is {links[i]}")


if __name__ == '__main__':
    data = Resources()
