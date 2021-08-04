import unittest
from wikitojson.src import wikitojson


class WikiTest(unittest.TestCase):

    def test_simple(self):
        content = """
        content intro
        """
        result = wikitojson.getdict(content)
        self.assertEqual(1, len(result))
        self.assertDictEqual(result[0], {'name': 'intro', 'content': 'content intro'})

    def test_empty(self):
        content = ""
        result = wikitojson.getdict(content)
        self.assertEqual(1, len(result))
        self.assertDictEqual(result[0], {'name': 'intro', 'content': ''})

    def test_paragraphsintro(self):
        content = """
        paragraph 1
        
        paragraph 2
        """
        result = wikitojson.getdict(content)
        self.assertEqual(1, len(result))
        self.assertDictEqual(result[0], {
            'name': 'intro',
            'content': """paragraph 1
        
        paragraph 2"""
        })

    def test_simplesub(self):
        content = """
        paragraph intro

        == subsection 1 ==
        
        paragraph subsection 1
        """
        result = wikitojson.getdict(content)
        self.assertEqual(1, len(result))
        self.assertDictEqual(result[0], {
            'name': 'intro',
            'content': "paragraph intro",
            'subsections': [
                {
                    'name': 'subsection 1',
                    'content': "paragraph subsection 1",
                }
            ]
        })

    def test_emptysimple(self):
        content = """
        paragraph intro

        == subsection 1 ==
        """
        result = wikitojson.getdict(content)
        self.assertEqual(1, len(result))
        self.assertDictEqual(result[0], {
            'name': 'intro',
            'content': "paragraph intro",
            'subsections': [
                {
                    'name': 'subsection 1',
                    'content': "",
                }
            ]
        })

    def test_paragraphssub(self):
        content = """
        paragraph intro

        == subsection 1 ==

        paragraph 1 subsection  
        paragraph 2 subsection  
        """
        result = wikitojson.getdict(content)
        self.assertEqual(1, len(result))
        self.assertDictEqual(result[0], {
            'name': 'intro',
            'content': "paragraph intro",
            'subsections': [
                {
                    'name': 'subsection 1',
                    'content': """paragraph 1 subsection  
        paragraph 2 subsection""",
                }
            ]
        })

    def test_siblings(self):
        content = """
        paragraph intro

        == subsection 1 ==

        paragraph subsection 1  
        
        == subsection 2 ==
        paragraph subsection 2  
        """
        result = wikitojson.getdict(content)
        self.assertEqual(1, len(result))
        self.assertDictEqual(result[0], {
            'name': 'intro',
            'content': "paragraph intro",
            'subsections': [
                {
                    'name': 'subsection 1',
                    'content': "paragraph subsection 1",
                },
                {
                    'name': 'subsection 2',
                    'content': "paragraph subsection 2",
                }
            ]
        })

    def test_siblingsemptyfirst(self):
        content = """
        paragraph intro

        == subsection 1 ==

        == subsection 2 ==
        paragraph subsection 2  
        """
        result = wikitojson.getdict(content)
        self.assertEqual(1, len(result))
        self.assertDictEqual(result[0], {
            'name': 'intro',
            'content': "paragraph intro",
            'subsections': [
                {
                    'name': 'subsection 1',
                    'content': "",
                },
                {
                    'name': 'subsection 2',
                    'content': "paragraph subsection 2",
                }
            ]
        })

    def test_siblingsemptylast(self):
        content = """
        paragraph intro

        == subsection 1 ==
        paragraph subsection 1 

        == subsection 2 ==         
        """
        result = wikitojson.getdict(content)
        self.assertEqual(1, len(result))
        self.assertDictEqual(result[0], {
            'name': 'intro',
            'content': "paragraph intro",
            'subsections': [
                {
                    'name': 'subsection 1',
                    'content': "paragraph subsection 1",
                },
                {
                    'name': 'subsection 2',
                    'content': "",
                }
            ]
        })

    def test_subsub(self):
        content = """
        paragraph intro

        == subsection 1 ==
        
        paragraph subsection 1
        
        === subsubsection 1 ===
        
        paragraph subsubsection 1
        
        """
        result = wikitojson.getdict(content)
        self.assertEqual(1, len(result))
        self.assertDictEqual(result[0], {
            'name': 'intro',
            'content': "paragraph intro",
            'subsections': [
                {
                    'name': 'subsection 1',
                    'content': "paragraph subsection 1",
                    'subsections': [
                        {
                            'name': 'subsubsection 1',
                            'content': "paragraph subsubsection 1",

                        }
                    ]
                }
            ]
        })

    def test_subsub_empty1(self):
        content = """
        paragraph intro

        == subsection 1 ==

        === subsubsection 1 ===

        paragraph subsubsection 1

        """
        result = wikitojson.getdict(content)
        self.assertEqual(1, len(result))
        self.assertDictEqual(result[0], {
            'name': 'intro',
            'content': "paragraph intro",
            'subsections': [
                {
                    'name': 'subsection 1',
                    'content': "",
                    'subsections': [
                        {
                            'name': 'subsubsection 1',
                            'content': "paragraph subsubsection 1",

                        }
                    ]
                }
            ]
        })

    def test_subsub_empty2(self):
        content = """
        paragraph intro

        == subsection 1 ==
        
        paragraph subsection 1

        === subsubsection 1 ===

        """
        result = wikitojson.getdict(content)
        self.assertEqual(1, len(result))
        self.assertDictEqual(result[0], {
            'name': 'intro',
            'content': "paragraph intro",
            'subsections': [
                {
                    'name': 'subsection 1',
                    'content': "paragraph subsection 1",
                    'subsections': [
                        {
                            'name': 'subsubsection 1',
                            'content': "",
                        }
                    ]
                }
            ]
        })

    def test_subsub_empty3(self):
        content = """
        paragraph intro

        == subsection 1 ==

        === subsubsection 1 ===

        """
        result = wikitojson.getdict(content)
        self.assertEqual(1, len(result))
        self.assertDictEqual(result[0], {
            'name': 'intro',
            'content': "paragraph intro",
            'subsections': [
                {
                    'name': 'subsection 1',
                    'content': "",
                    'subsections': [
                        {
                            'name': 'subsubsection 1',
                            'content': "",
                        }
                    ]
                }
            ]
        })

    def test_subsubsibling(self):
        content = """
        paragraph intro

        == subsection 1 ==

        paragraph subsection 1

        === subsubsection 1 ===

        content subsubsection 1

        === subsubsection 2 ===

        content subsubsection 2
        """
        result = wikitojson.getdict(content)
        self.assertEqual(1, len(result))
        self.assertDictEqual(result[0], {
            'name': 'intro',
            'content': "paragraph intro",
            'subsections': [
                {
                    'name': 'subsection 1',
                    'content': "paragraph subsection 1",
                    'subsections': [
                        {
                            'name': 'subsubsection 1',
                            'content': "content subsubsection 1",
                        },
                        {
                            'name': 'subsubsection 2',
                            'content': "content subsubsection 2",
                        }
                    ]
                }
            ]
        })

    def test_subsiblingsub_1(self):
        content = """
        paragraph intro

        == subsection 1 ==

        paragraph subsection 1

        === subsubsection 1 ===

        content subsubsection 1

        == subsection 2 ==

        content subsection 2
        """
        result = wikitojson.getdict(content)
        self.assertEqual(1, len(result))
        self.assertDictEqual(result[0], {
            'name': 'intro',
            'content': "paragraph intro",
            'subsections': [
                {
                    'name': 'subsection 1',
                    'content': "paragraph subsection 1",
                    'subsections': [
                        {
                            'name': 'subsubsection 1',
                            'content': "content subsubsection 1",
                        }
                    ]
                },
                {
                    'name': 'subsection 2',
                    'content': "content subsection 2",
                }
            ]
        })

    def test_subsiblingsub_2(self):
        content = """
        paragraph intro

        == subsection 1 ==

        paragraph subsection 1

        == subsection 2 ==

        content subsection 2

        === subsubsection 1 ===

        content subsubsection 1

        """
        result = wikitojson.getdict(content)
        self.assertEqual(1, len(result))
        self.assertDictEqual(result[0], {
            'name': 'intro',
            'content': "paragraph intro",
            'subsections': [
                {
                    'name': 'subsection 1',
                    'content': "paragraph subsection 1"
                },
                {
                    'name': 'subsection 2',
                    'content': "content subsection 2",
                    'subsections': [
                        {
                            'name': 'subsubsection 1',
                            'content': "content subsubsection 1",
                        }
                    ]
                }
            ]
        })

    def test_precedence1(self):
        content = """
        paragraph intro

        === subsection 1 ===

        paragraph subsection 1
        """
        result = wikitojson.getdict(content)
        self.assertEqual(1, len(result))
        self.assertDictEqual(result[0], {
            'name': 'intro',
            'content': "paragraph intro",
            'subsections': [
                {
                    'name': 'subsection 1',
                    'content': "paragraph subsection 1",
                }
            ]
        })

    def test_precedence2(self):
        content = """
        paragraph intro

        === subsection 1 ===

        paragraph subsection 1
        
        == subsection 2 ==

        paragraph subsection 2
        """
        result = wikitojson.getdict(content)
        self.assertEqual(1, len(result))
        self.assertDictEqual(result[0], {
            'name': 'intro',
            'content': "paragraph intro",
            'subsections': [
                {
                    'name': 'subsection 1',
                    'content': "paragraph subsection 1",
                },
                {
                    'name': 'subsection 2',
                    'content': "paragraph subsection 2",
                }
            ]
        })

    def test_precedence3(self):
        content = """
        paragraph intro

        === subsection 1 ===

        paragraph subsection 1

        ==== subsubsection 1 ====

        paragraph subsubsection 1
        
        == subsection 2 ==

        paragraph subsection 2
        """
        result = wikitojson.getdict(content)
        self.assertEqual(1, len(result))
        self.assertDictEqual(result[0], {
            'name': 'intro',
            'content': "paragraph intro",
            'subsections': [
                {
                    'name': 'subsection 1',
                    'content': "paragraph subsection 1",
                    'subsections': [
                        {
                            'name': 'subsubsection 1',
                            'content': "paragraph subsubsection 1",
                        }
                    ]
                },
                {
                    'name': 'subsection 2',
                    'content': "paragraph subsection 2",
                }
            ]
        })

    def test_precedence4(self):
        content = """
        paragraph intro

        == subsection 1 ==

        paragraph subsection 1

        ==== subsubsection 1 ====

        paragraph subsubsection 1

        == subsection 2 ==

        paragraph subsection 2
        """
        result = wikitojson.getdict(content)
        self.assertEqual(1, len(result))
        self.assertDictEqual(result[0], {
            'name': 'intro',
            'content': "paragraph intro",
            'subsections': [
                {
                    'name': 'subsection 1',
                    'content': "paragraph subsection 1",
                    'subsections': [
                        {
                            'name': 'subsubsection 1',
                            'content': "paragraph subsubsection 1",
                        }
                    ]
                },
                {
                    'name': 'subsection 2',
                    'content': "paragraph subsection 2",
                }
            ]
        })

    def test_precedence5(self):
        content = """
        paragraph intro

        == subsection 1 ==

        paragraph subsection 1

        ==== subsubsection 1 ====

        paragraph subsubsection 1
        
        === subsubsection 2 ===

        paragraph subsubsection 2

        == subsection 2 ==

        paragraph subsection 2
        """
        result = wikitojson.getdict(content)
        self.assertEqual(1, len(result))
        self.assertDictEqual(result[0], {
            'name': 'intro',
            'content': "paragraph intro",
            'subsections': [
                {
                    'name': 'subsection 1',
                    'content': "paragraph subsection 1",
                    'subsections': [
                        {
                            'name': 'subsubsection 1',
                            'content': "paragraph subsubsection 1",
                        },
                        {
                            'name': 'subsubsection 2',
                            'content': "paragraph subsubsection 2",
                        }
                    ]
                },
                {
                    'name': 'subsection 2',
                    'content': "paragraph subsection 2",
                }
            ]
        })

    def test_pagelevel(self):
        content = """
        paragraph intro

        = section 1 =

        paragraph section 1
        """
        result = wikitojson.getdict(content)

        self.assertEqual(2, len(result))
        self.assertDictEqual(result[0], {
            'name': 'intro',
            'content': "paragraph intro",
        })

        self.assertDictEqual(result[1], {
            'name': 'section 1',
            'content': "paragraph section 1",
        })

if __name__ == '__main__':
    unittest.main()
