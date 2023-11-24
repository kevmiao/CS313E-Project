# import libraries
import pandas as pd

# read file
dataframe = pd.read_csv("Data.csv")
print(dataframe.head())

# Convert each row to a dictionary
material_dicts = []
for index, row in dataframe.iterrows():
    material_dict = row.to_dict()
    material_dicts.append(material_dict)

# Display the list of dictionaries
print(material_dicts)

# Step 1: Data Preprocessing

# Sample dataset (replace this with your actual dataset)
materials_data = [
    {"material": "Steel", "tensile_strength": 500, "density": 7.85, "cost": 10, "corrosion_resistance": "high"},
    {"material": "Aluminum", "tensile_strength": 300, "density": 2.7, "cost": 20, "corrosion_resistance": "medium"},
    # ... add more materials and their properties
]

# Step 2: Decision Tree Construction

def build_decision_tree(dataset, criteria):
    # Recursive function to build decision tree
    # Implement your decision tree construction algorithm here
    # ...
    class Node:
        def __init__(self, data, lchild, rchild):
            self.data = data
            self.lchild = lchild
            self.rchild = rchild
            self.materials = materials
# Step 3: User Interaction

def recommend_material(user_input, decision_tree):
    # Traverse the decision tree based on user input
    # Implement the traversal logic here
    # ...
    return
# Step 4: Visualization

def visualize_decision_tree(decision_tree):
    # Use a library like Graphviz to visualize the decision tree
    # ...
    return
# Example usage:

# Step 1: Data Preprocessing
materials = [material["material"] for material in materials_data]
material_properties = {material: {key: value for key, value in material.items() if key != "material"} for material in materials_data}

# Step 2: Decision Tree Construction
criteria = ["tensile_strength", "density", "cost", "corrosion_resistance"]
decision_tree = build_decision_tree(material_properties, criteria)

# Step 3: User Interaction
user_input = {"tensile_strength": 400, "cost": 15}
recommended_material = recommend_material(user_input, decision_tree)
print(f"Recommended Material: {recommended_material}")

# Step 4: Visualization
visualize_decision_tree(decision_tree)
