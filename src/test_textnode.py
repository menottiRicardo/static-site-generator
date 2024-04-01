import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node2", text_type_text)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", text_type_italic, "https://www.boot.dev")
        node2 = TextNode(
            "This is a text node", text_type_italic, "https://www.boot.dev"
        )
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

    def test_eq_code(self):
        node = TextNode("This is a text node", text_type_code, "https://www.boot.dev")
        node2 = TextNode(
            "This is a text node", text_type_code, "https://www.boot.dev"
        )
        self.assertEqual(node, node2)
    
    def test_eq_link(self):
        node = TextNode("This is a text node", text_type_link, "https://www.boot.dev")
        node2 = TextNode(
            "This is a text node", text_type_link, "https://www.boot.dev"
        )
        self.assertEqual(node, node2)

    def test_eq_image(self):
        node = TextNode("This is a text node", text_type_image, "https://www.boot.dev")
        node2 = TextNode(
            "This is a text node", text_type_image, "https://www.boot.dev"
        )
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
