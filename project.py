# import libraries
import pandas as pd
import numpy as np

# Step 1: Data Preprocessing

# Read file
dataframe = pd.read_csv("Data.csv")

# Replace NaN with None
dataframe.replace(np.NaN, None, inplace = True )

# Print first 5 values
# print(dataframe.head())

# Convert each row to a dictionary
material_dicts = []
for index, row in dataframe.iterrows():
    material_dict = row.to_dict()
    material_dicts.append(material_dict)

# Display the list of dictionaries
# print(material_dicts)


# Step 2: Decision Tree Construction
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.materials = []

def build_binary_search_tree(dataset, property_name):
    # Sort the dataset based on the specified property, recursive
    sorted_dataset = sorted(dataset, key=lambda x: x[property_name])

    if not sorted_dataset:
        return None

    middle_index = len(sorted_dataset) // 2
    node = Node(sorted_dataset[middle_index][property_name])
    node.materials = [sorted_dataset[middle_index]]  # Store only the middle element in materials
    node.left = build_binary_search_tree(sorted_dataset[:middle_index], property_name)
    node.right = build_binary_search_tree(sorted_dataset[middle_index + 1:], property_name)

    return node

# Function to perform in-order traversal and print nodes
def print_tree_in_order(node):
    if node:
        print_tree_in_order(node.left)
        print(f"Node: {node.data}, Materials: {node.materials}")
        print_tree_in_order(node.right)

# Step 2: Decision Tree Construction

# Sample dataset (replace this with your actual dataset)
materials_data = [
    {"material": "Steel", "tensile_strength": 387, "density": 7.85, "cost": 10, "corrosion_resistance": "high"},
    {"material": "Aluminum", "tensile_strength": 385, "density": 2.7, "cost": 20, "corrosion_resistance": "medium"},
    {"material": "doge", "tensile_strength": 386, "density": 2.7, "cost": 20, "corrosion_resistance": "medium"},
    {"material": "fish", "tensile_strength": 380, "density": 2.7, "cost": 20, "corrosion_resistance": "medium"},
    {"material": "cat", "tensile_strength": 390, "density": 2.7, "cost": 20, "corrosion_resistance": "medium"}
    # ... add more materials and their properties
]

# Property to use for sorting
property_name = "tensile_strength"

# Construct the binary search tree
root_node = build_binary_search_tree(materials_data, property_name)

# print_tree_in_order(root_node)
# Step 3: User Interaction
results = []

def query_tree(node, min_strength, max_strength):


    if node:
        # Convert node data to numeric type for proper comparison
        num_node_data = float(node.data) if node.data is not None else None

        # Recursively search the left subtree if there could be relevant materials
        if num_node_data is not None and num_node_data >= min_strength:
            query_tree(node.left, min_strength, max_strength)

        # If the node's data is within the specified range, add materials
        if min_strength <= num_node_data and num_node_data <= max_strength:
            results.extend(node.materials)
        
        # Recursively search the right subtree if there could be relevant materials
        if num_node_data is not None and num_node_data <= max_strength:
            query_tree(node.right, min_strength, max_strength)

    return results


# Example search: Find materials with tensile strength between 200 and 400
min_tensile_strength = 385
max_tensile_strength = 387
query_results = query_tree(root_node, min_tensile_strength, max_tensile_strength)

# Print the results
for material in query_results:
    print(material)
