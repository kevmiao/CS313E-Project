'''Engineering Materials Database and Material Selection Helper'''
# By: Kevin Miao, Tyler Yan
# CS 313E 52590
# 11/28/2023

# import libraries
import pandas as pd
import numpy as np


# 1. Data Preprocessing

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


# 2. BST Construction

class Node:
    '''BST Node Class'''
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.materials = []

def build_bst(dataset, property_name):
    '''Sort the dataset based on the specified property, recursive'''
    sorted_dataset = sorted(dataset, key=lambda x: x[property_name])

    if not sorted_dataset:
        return None

    middle_index = len(sorted_dataset) // 2
    node = Node(sorted_dataset[middle_index][property_name])
    node.materials = [sorted_dataset[middle_index]]  # Store only the middle element in materials
    node.left = build_bst(sorted_dataset[:middle_index], property_name)
    node.right = build_bst(sorted_dataset[middle_index + 1:], property_name)

    return node

def print_tree_in_order(node):
    '''Function to perform in-order traversal and print nodes'''
    if node:
        print_tree_in_order(node.left)
        print(f"Node: {node.data}, Materials: {node.materials}")
        print_tree_in_order(node.right)


# 3. User Interaction

results = []
def query_tree(node, min_strength, max_strength):
    '''Helps determine the correct material'''

    if node:
        # Convert node data to numeric type for proper comparison
        num_node_data = float(node.data) if node.data is not None else None

        # Recursively search the left subtree if there could be relevant materials
        if num_node_data is not None and num_node_data >= min_strength:
            query_tree(node.left, min_strength, max_strength)

        # If the node's data is within the specified range, add materials
        if min_strength <= num_node_data and num_node_data <= max_strength:
            results.extend(node.materials)
            # print(type(node.materials))
            # print(type(node.materials[0]))

        # Recursively search the right subtree if there could be relevant materials
        if num_node_data is not None and num_node_data <= max_strength:
            query_tree(node.right, min_strength, max_strength)

    return results


def main():
    'Main Function Call'

    print("\nThis is the Material Selection for Structural Components software.\n")
    print("You can specify the property that you desire, "
            "as well as the range for the values of the property.\n")

    while True:
        results.clear()

        print("These are the current compatible properties that you can search through:")
        print("    Su (Tensile Strength) [Mpa]")
        print("    Sy (Yield Strength) [MPa]")
        print("    A5 (Elongation at Break or Strain) [%]")
        print("    Bhn (Brinell Hardness Number)")
        print("    E (Elastic Modulus) [MPa]")
        print("    G (Shear Modulus) [MPa]")
        print("    mu (Poisson's Ratio)")
        print("    Ro (Density) [kg/m^3]")
        print("    select X to exit")
        print()

        # Property to use for sorting
        property_name = input("Make your selection: ")
        print()
        if property_name == "X":
            break
        if property_name not in ["Su", "Sy", "A5", "Bhn", "E", "G", "mu", "Ro"]:
            print("Please select a property listed above.")
            continue

        # Construct the binary search tree
        root_node = build_bst(material_dicts, property_name)

        # Example search: Find materials with tensile strength between 200 and 400
        minimum = int(input("Minimum value: "))
        maximum = int(input("Maximum value: "))
        print()

        query_results = query_tree(root_node, minimum, maximum)

        # Print the results
        if query_results:
            print(f"These are the results of {property_name} that fall "
                "in between {minimum} and {maximum}: \n")
            for material in query_results:
                print(material)
        else:
            print(f"Sorry, there are no materials with {property_name} that fall "
                "in between {minimum} and {maximum}: \n")

        print()

    print("Thanks for using the Material Selection for "
          "Structural Components software. See you again!\n\n")

if __name__ == "__main__":
    main()