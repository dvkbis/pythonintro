import re

def checkDOM(strParam):
    """
    Checks the validity of HTML tags in a given string.

    Args:
        strParam (str): The input string containing HTML tags.

    Returns:
        bool or str: Returns False if the HTML tags are invalid or mismatched. 
                    Returns the mismatched tag if there is only one mismatch. 
                    Returns True if all tags are valid and matched.

    Examples:
        >>> checkDOM("<b>Hello</b>")
        True

        >>> checkDOM("<b>Hello</i>")
        'b'

        >>> checkDOM("<b>Hello")
        False
    """
    matches = re.finditer(r"<(/?)([^<>\s]+)\s*>", strParam)
    queue = []
    result = True

    for match in matches:
        backslash = match.group(1)
        tag = match.group(2)

        if backslash:
            if len(queue) == 0:
                return False
                
            previous_tag = queue.pop()
            if tag.lower() != previous_tag:
                if result == True:
                    result = previous_tag
                else:
                    return False
        else:
            tag = tag.lower()
            if tag not in ("em", "b", "p", "i", "div"):
                return False
            
            queue.append(tag)

    return result if len(queue) == 0 else False


import unittest

class TestCheckDOM(unittest.TestCase):
    """
    A test case class for the CheckDOM.py module.
    This class contains multiple test methods to validate the behavior of the checkDOM function.
    """
    def test_example_1(self):
        self.assertTrue(checkDOM("<div><b><p>hello world</p></b></div>"))

    def test_example_2(self):
        self.assertEqual(checkDOM("<div><i>hello</i>world</b>"), "div")

    def test_example_3(self):
        self.assertFalse(checkDOM("</div><p></p><div>"))

    def test_example_4(self):
        self.assertEqual(checkDOM("<em></em><em></em><p></b>"), "p")

    def test_example_5(self):
        self.assertFalse(checkDOM("<div><p></p><b><p></div>"))

    def test_valid_html_nested_correctly(self):
        self.assertTrue(checkDOM("<div><b><p>hello world</p></b></div>"))
        self.assertTrue(checkDOM("<b><i><em>nested text</em></i></b>"))
        self.assertTrue(checkDOM("<p><i>text inside</i></p>"))
        self.assertFalse(checkDOM("<b><p>text</b></p>"))
    
    def test_single_tag_change_for_validity(self):
        self.assertEqual(checkDOM("<div><i>hello</i>world</b>"), "div")
        self.assertEqual(checkDOM("<b><i><em>text</em></i></div>"), "b")
        self.assertEqual(checkDOM("<div><p><i>example</i></b></div>"), "p")

    def test_invalid_html_multiple_changes_needed(self):
        self.assertFalse(checkDOM("</div><p></p><div>"))
        self.assertFalse(checkDOM("<b><em>text</em></i></b>"))
        self.assertFalse(checkDOM("<b><i>text</i><b>"))
        self.assertFalse(checkDOM("<div><p>text</div>"))

    def test_valid_html(self):
        self.assertTrue(checkDOM("<div><b><p>hello world</p></b></div>"))

    def test_mismatched_closing_tag(self):
        self.assertEqual(checkDOM("<div><i>hello</i>world</b>"), "div")

    def test_invalid_closing_tag(self):
        self.assertFalse(checkDOM("</div><p></p><div>"))

    def test_single_mismatched_opening_tag(self):
        self.assertEqual(checkDOM("<em></em><em></em><p></b>"), "p")

    def test_multiple_mismatched_opening_tags(self):
        self.assertFalse(checkDOM("<div><p></p><b><p></div>"))

    def test_no_tags(self):
        self.assertTrue(checkDOM("hello world"))

    def test_empty_string(self):
        self.assertTrue(checkDOM(""))

    def test_nested_valid_tags(self):
        self.assertTrue(checkDOM("<div><p><b>text</b></p></div>"))

    def test_nested_invalid_tags(self):
        self.assertFalse(checkDOM("<div><p></p><b><p></div>"))

    def test_single_tag(self):
        self.assertEqual(checkDOM("<div>"), False)

    def test_single_tag_closed(self):
        self.assertEqual(checkDOM("</div>"), False)

    def test_mixed_content(self):
        self.assertTrue(checkDOM("hello <b>world</b>"))

    def two_open(self):
        self.assertEqual(checkDOM("<div><div>"), False)

    def two_close(self):
        self.assertEqual(checkDOM("</div></div>"), False)

    def test_valid_combination(self):
        self.assertTrue(checkDOM("<div><b><i>text</i></b></div>"))

    def test_excessive_closing_tags(self):
        self.assertFalse(checkDOM("<div></div></div>"))

    def test_nested_invalid_similar_tags(self):
        self.assertFalse(checkDOM("<b><i>text</b></i>"))

    def test_valid_mixed_content(self):
        self.assertTrue(checkDOM("text <b>bold</b> text <i>italic</i>"))

    def test_adjacent_mismatched_tags(self):
        self.assertFalse(checkDOM("<div><b></div></b>"))

    def test_multiple_mismatched_tags(self):
        self.assertFalse(checkDOM("<b><i>text</b><p></i></p>"))

    def test_case_sensitive_tags(self):
        self.assertFalse(checkDOM("<Div><b></DIV>"))

    def test_nested_empty_tags(self):
        self.assertTrue(checkDOM("<div><b></b></div>"))

    def test_valid_no_content(self):
        self.assertTrue(checkDOM("<div><b></b></div>"))

    def test_invalid_unmatched_multiple(self):
        self.assertFalse(checkDOM("<div><b><i></b></div><p>"))

    def test_whitespace_between_tags(self):
        self.assertTrue(checkDOM("<div>   <b>text</b>   </div>"))

    def test_multiple_valid_nested_tags(self):
        self.assertTrue(checkDOM("<div><div><b><i>text</i></b></div></div>"))

    # Additional edge cases
    def test_tags_with_extra_whitespace(self):
        self.assertTrue(checkDOM("<div> <b> text </b> </div>"))

    def test_tags_with_text_and_nested_tags(self):
        self.assertTrue(checkDOM("<div>hello <b>world</b></div>"))

    def test_multiple_nested_tags_with_text(self):
        self.assertTrue(checkDOM("<div><p>hello <b>world</b></p></div>"))

    def test_empty_tags(self):
        self.assertTrue(checkDOM("<div><b></b></div>"))

    def test_single_tag_with_text(self):
        self.assertTrue(checkDOM("<b>hello</b>"))

    def test_multiple_adjacent_tags(self):
        self.assertTrue(checkDOM("<b></b><i></i>"))

    def test_tags_with_mixed_content(self):
        self.assertTrue(checkDOM("<div>hello <b>world</b>!</div>"))

    def test_tags_with_only_text(self):
        self.assertTrue(checkDOM("hello world"))

    def test_tags_with_only_whitespace(self):
        self.assertTrue(checkDOM("   "))

    def test_tags_with_special_characters(self):
        self.assertTrue(checkDOM("<div>@#$%^&*()</div>"))

    def test_nested_valid_empty_tags(self):
        self.assertTrue(checkDOM("<div><b></b><i></i></div>"))

    def test_tags_with_special_html_characters(self):
        self.assertTrue(checkDOM("<div>&lt; &gt; &amp; </div>"))

    def test_nested_tags_with_text_and_empty_tags(self):
        self.assertTrue(checkDOM("<div><b>text</b><i></i></div>"))

    def test_adjacent_empty_tags(self):
        self.assertTrue(checkDOM("<b></b><i></i>"))

    def test_long_string_of_text_with_tags(self):
        self.assertTrue(checkDOM("<div>" + "hello " * 1000 + "</div>"))

    def test_invalid_tags_with_unmatched_nested_tags(self):
        self.assertFalse(checkDOM("<div><b><i></div></b></i>"))

    def test_tags_with_numeric_characters(self):
        self.assertTrue(checkDOM("<div>123 <b>456</b></div>"))

    def test_empty_nested_structure(self):
        self.assertTrue(checkDOM("<div><div></div></div>"))

    def test_mismatched_tags_with_special_characters(self):
        self.assertFalse(checkDOM("<div><b>text</b></i></div>"))

    def test_large_input_with_correct_nesting(self):
        self.assertTrue(checkDOM("<div>" + "<b><i>nested</i></b>" * 1000 + "</div>"))

    def test_large_input_with_incorrect_nesting(self):
        self.assertFalse(checkDOM("<div>" + "<b><i>nested</b></i>" * 1000 + "</div>"))

    def test_multiple_closing_tags(self):
        self.assertFalse(checkDOM("<div></div></div>"))

    def test_correctly_nested_with_mixed_content(self):
        self.assertTrue(checkDOM("<div><b>Content</b> and <i>more</i></div>"))

    def test_tags_with_extra_whitespace(self):
        self.assertTrue(checkDOM("<div > <b> text </b> </div>"))
        self.assertTrue(checkDOM("<div> <i> text </i> </div>"))

    def test_case_insensitive_tags(self):
        self.assertTrue(checkDOM("<DIV><b>text</B></DIV>"))
        self.assertTrue(checkDOM("<div><B>text</b></DIV>"))

    def test_invalid_characters_in_tags(self):
        self.assertFalse(checkDOM("<div><b@>text</b@></div>"))
        self.assertFalse(checkDOM("<div><i#>text</i#></div>"))

    def test_empty_tags(self):
        self.assertTrue(checkDOM("<div><b></b></div>"))
        self.assertTrue(checkDOM("<div><i></i></div>"))

    def test_large_input_with_incorrect_nesting(self):
        self.assertFalse(checkDOM("<div>" + "<b><i>nested</b></i>" * 1000 + "</div>"))

    def test_multiple_closing_tags(self):
        self.assertFalse(checkDOM("<div></div></div>"))

    def test_correctly_nested_with_mixed_content(self):
        self.assertTrue(checkDOM("<div><b>Content</b> and <i>more</i></div>"))


if __name__ == '__main__':
    unittest.main()
    # pass