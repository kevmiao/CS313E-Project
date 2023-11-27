'''Test Cases for Material Database'''
# By: Kevin Miao, Tyler Yan
# CS 313E 52590
# 11/28/2023

import unittest
from project import *

class TestMaterialSelection(unittest.TestCase):
    '''Tests Material Selecter'''

    def setUp(self):
        # Sample dataset
        self.materials_data = [
            {"material": "A", "tensile_strength": 1, "density": 8, "cost": 10, "corrosion_resistance": "high"},
            {"material": "B", "tensile_strength": 2, "density": 10, "cost": 20, "corrosion_resistance": "medium"},
            {"material": "C", "tensile_strength": 3, "density": 6, "cost": 5, "corrosion_resistance": "medium"},
            {"material": "D", "tensile_strength": 4, "density": 1, "cost": 20, "corrosion_resistance": "medium"},
            {"material": "E", "tensile_strength": 5, "density": 20, "cost": 15, "corrosion_resistance": "medium"}
            ]

    def test_query_search_tensile_strength(self):
        """Test case 1: Query materials with tensile strength between 1 and 4"""

        results.clear()
        root_node = build_bst(self.materials_data, "tensile_strength")
        query_results = query_tree(root_node, 1, 4)

        expected_results = [
            {"material": "A", "tensile_strength": 1, "density": 8, "cost": 10, "corrosion_resistance": "high"},
            {"material": "B", "tensile_strength": 2, "density": 10, "cost": 20, "corrosion_resistance": "medium"},
            {"material": "C", "tensile_strength": 3, "density": 6, "cost": 5, "corrosion_resistance": "medium"},
            {"material": "D", "tensile_strength": 4, "density": 1, "cost": 20, "corrosion_resistance": "medium"},
        ]
        self.assertEqual(query_results, expected_results)

    def test_query_search_tensile_strength_2(self):
        """Test case 2: Query materials with tensile strength between 4 and 5"""

        results.clear()
        root_node = build_bst(self.materials_data, "tensile_strength")
        query_results = query_tree(root_node, 4, 5)

        expected_results = [
            {"corrosion_resistance": "medium", "cost": 20, "density": 1, "tensile_strength": 4, "material": "D"},
            {"corrosion_resistance": "medium", "cost": 15, "density": 20, "tensile_strength": 5, "material": "E"}
        ]
        self.assertEqual(query_results, expected_results)

    def test_query_search_cost(self):
        """Test case 3: Query materials with cost between 150 and 200"""

        results.clear()
        root_node = build_bst(self.materials_data, "cost")
        query_results = query_tree(root_node, 150, 200)

        expected_results = []
        self.assertEqual(query_results, expected_results)

    def test_query_search_cost_2(self):
        """Test case 4: Query materials with cost between 1 and 15"""

        results.clear()
        root_node = build_bst(self.materials_data, "cost")
        query_results = query_tree(root_node, 1, 15)

        expected_results = [
            {"material": "C", "tensile_strength": 3, "density": 6, "cost": 5, "corrosion_resistance": "medium"},
            {"material": "A", "tensile_strength": 1, "density": 8, "cost": 10, "corrosion_resistance": "high"},
            {"material": "E", "tensile_strength": 5, "density": 20, "cost": 15, "corrosion_resistance": "medium"}
        ]
        self.assertEqual(query_results, expected_results)

    def test_query_search_density(self):
        """Test case 4: Query materials with density between 5 and 9"""

        results.clear()
        root_node = build_bst(self.materials_data, "density")
        query_results = query_tree(root_node, 5, 9)

        expected_results = [
            {"material": "C", "tensile_strength": 3, "density": 6, "cost": 5, "corrosion_resistance": "medium"},
            {"material": "A", "tensile_strength": 1, "density": 8, "cost": 10, "corrosion_resistance": "high"}
        ]
        self.assertEqual(query_results, expected_results)

if __name__ == '__main__':
    unittest.main()