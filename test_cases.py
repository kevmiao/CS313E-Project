import unittest
from project import build_binary_search_tree, query_tree


class TestMaterialSelection(unittest.TestCase):

    def setUp(self):
        # Sample dataset
        self.materials_data = [
            {"material": "A", "tensile_strength": 390, "density": 7.85, "cost": 10, "corrosion_resistance": "high"},
            {"material": "B", "tensile_strength": 385, "density": 2.65, "cost": 20, "corrosion_resistance": "medium"},
            {"material": "C", "tensile_strength": 386, "density": 2.7, "cost": 19, "corrosion_resistance": "medium"},
            {"material": "D", "tensile_strength": 380, "density": 2.6, "cost": 20, "corrosion_resistance": "medium"},
            {"material": "E", "tensile_strength": 387, "density": 2.9, "cost": 15, "corrosion_resistance": "medium"}
            ]

    def test_query_search_tensile_strength(self):
        # Test case 1: Query materials with tensile strength between 380 and 386
        root_node = build_binary_search_tree(self.materials_data, "tensile_strength")
        query_results = query_tree(root_node, 380, 387)

        expected_results = [
            {"material": "D", "tensile_strength": 380, "density": 2.6, "cost": 20, "corrosion_resistance": "medium"},
            {"material": "B", "tensile_strength": 385, "density": 2.65, "cost": 20, "corrosion_resistance": "medium"},
            {"material": "C", "tensile_strength": 386, "density": 2.7, "cost": 19, "corrosion_resistance": "medium"},
            {"material": "E", "tensile_strength": 387, "density": 2.9, "cost": 15, "corrosion_resistance": "medium"}
        ]
        self.assertEqual(query_results, expected_results)


    def test_query_search_cost(self):
        # Test case 3: Query materials with cost between 150 and 200
        root_node = build_binary_search_tree(self.materials_data, "cost")
        query_results = query_tree(root_node, 150, 200)

        expected_results = []
        self.assertEqual(query_results, expected_results)

if __name__ == '__main__':
    unittest.main()