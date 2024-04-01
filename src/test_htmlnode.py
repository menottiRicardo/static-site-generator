import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p", "this is a paragraph")
        self.assertEqual("HTMLNode tag:p value:this is a paragraph", repr(node))

    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "link to paradise",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        print(node.props_to_html())

        self.assertEqual(' class="greeting" href="https://boot.dev"', node.props_to_html())


if __name__ == "__main__":
    unittest.main()
