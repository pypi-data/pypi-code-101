import unittest
from rbdt import parse, CollatedRules


class TestStringMethods(unittest.TestCase):

    def test_one_allow(self):
        l = """
        user-agent: A
        allow: /
        """
        left = parse(l)
        right = [CollatedRules(user_agents={"a"},
                               allows={"/"},
                               disallows=set())]
        self.assertEqual(left, right)

    def test_one_disallow(self):
        l = """
        user-agent: A
        disallow: /
        """
        left = parse(l)
        right = [CollatedRules(
            user_agents={"a"}, allows=set(), disallows={"/"})]
        self.assertEqual(left, right)

    def test_one_of_each(self):
        l = """
        user-agent: A
        allow: /
        disallow: /
        """

        r = """
        user-agent: A
        disallow: /
        allow: /
        """

        left = parse(l)
        right = parse(r)
        middle = [CollatedRules(user_agents={"a"}, allows={
                                "/"}, disallows={"/"})]
        self.assertEqual(left, right)
        self.assertEqual(left, middle)

    def test_lots(self):
        l = """
        user-agent: A 
        allow: /a
        allow: /b 
        allow: /c
        disallow: /d
        disallow: /d/e
        disallow: /f
        """

        left = parse(l)
        right = [CollatedRules(user_agents={"a"}, allows= {"/a", "/b", "/c"}, disallows={"/d", "/d/e", "/f"})]
        self.assertEqual(left, right)

    def test_overlapping(self):
        l = """
        user-agent: A
        allow: /
        disallow: /

        user-agent: B 
        disallow: /
        allow: /
        """

        left = parse(l)
        right = [CollatedRules(user_agents={"a", "b"}, allows={
                                "/"}, disallows={"/"})]
        self.assertEqual(left, right)

if __name__ == '__main__':
    unittest.main()
