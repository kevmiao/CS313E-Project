# Materials Database Selector

Material Selection for Structural Components Software - Kevin Miao, Tyler Yan

## What is your project idea about?

The objective of this project is to develop a system that assists in the selection of materials for structural components based on specific criteria, such as strength and density.

## If you use any datasets, describe the dataset and provide how one can access and download it.

Utilized a comprehensive material properties database that includes information such as tensile strength, density, Brinell Hardness Number, etc., for various materials like metals, polymers, and composites.

The dataset can be downloaded from kaggle here: https://www.kaggle.com/datasets/purushottamnawale/materials

## Describe your design for main packages, classes, methods, functions, and iterations between them.

1. Main Packages:

The code imports the Pandas library and NumPy library using the aliases pd and np, respectively.

2. Classes:

Node Class:
- Represents a node in a binary search tree.
- Contains attributes: data (node value), left (left child), right (right child), and materials (a list of materials associated with the node's value).

3. Methods/Functions:

Data Preprocessing Section:
Read File:
- Uses Pandas to read a CSV file ("Data.csv") and stores it in a DataFrame (dataframe).

Replace NaN with None:
- Uses NumPy to replace NaN values in the DataFrame with None.

Convert to Dictionary:
- Iterates over rows in the DataFrame, converts each row to a dictionary, and appends it to the list material_dicts.

BST Construction Section:
build_bst Function:
- Takes a dataset and a property name as input.
- Constructs a binary search tree based on the specified property.
- Uses the Node class to create nodes.

print_tree_in_order Function:
- Performs an in-order traversal of the binary search tree and prints each node's data and associated materials.

User Interaction Section:
query_tree Function:
- A DFS algorithm that searches a binary search tree based on a range of values
- Takes a node and a range (minimum, maximum) as input.
- Recursively searches the binary search tree and collects materials within the specified range.
- Returns a list of materials.

4. Iterations Between Them:

The code follows a sequential flow:
- Reads and preprocesses data.
- Constructs a binary search tree based on a property.
- Performs a query on the tree to find materials with that property within a specified range.
- Prints the results.
5. Main Function:

main Function:
- Identifies a property depending on the input.
- Constructs the binary search tree using the provided dataset.
- Performs a query on the tree.
- Prints the results.
6. Execution:

The main function is executed if the script is run as the main program.

For the test_cases.py file:

1. Packages/Modules:

The unittest module is used for testing.

2. Classes and Functions:

TestMaterialSelection Class (unittest.TestCase):
setUp Method:
- Initializes the sample dataset (self.materials_data) for testing.

test_query_search_tensile_strength Method:
- Tests the query_tree function for querying materials based on tensile strength.
- Builds a binary search tree using tensile strength as the property.
- Queries for materials within the range of 1 and 4 tensile strength.
- Asserts that the query results match the expected results.

test_query_search_tensile_strength_2 Method:
- Tests the query_tree function for querying materials based on tensile strength.
- Builds a binary search tree using tensile strength as the property.
- Queries for materials within the range of 4 and 5 tensile strength.
- Asserts that the query results match the expected results.

test_query_search_cost Method:
- Tests the query_tree function for querying materials based on cost.
- Builds a binary search tree using cost as the property.
- Queries for materials within the range of 150 and 200 cost.
- Asserts that the query results match the expected results.

test_query_search_cost_2 Method: 
- Tests the query_tree function for querying materials based on cost.
- Builds a binary search tree using cost as the property.
- Queries for materials within the range of 1 and 15 cost.
- Asserts that the query results match the expected results.

test_query_search_density Method
- Tests the query_tree function for querying materials based on density.
- Builds a binary search tree using density as the property.
- Queries for materials within the range of 5 and 9 cost.
- Asserts that the query results match the expected results.

3. Execution:

The unittest.main() method is used to run the test cases when the script is executed.

## Describe any libraries that you use.

Pandas is a data manipulation and analysis library for Python. It provides easy-to-use data structures like DataFrames and Series, which are designed to work seamlessly with structured data. It has comprehensive tools for cleaning, merging, reshaping, and aggregating data, and it is able to read and write data in various formats (CSV, Excel, SQL databases, etc.).

NumPy is a fundamental library for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays. Some NumPy features include N-dimensional arrays, various mathematical functions, and random number generation.

In the test_cases.py file: The unittest library is the built-in testing framework and provides a test discovery mechanism, test fixtures, and assertions for verifying the correctness of code.

## Design some Test cases that can test the correctness of your software.

Check the test_cases.py file.

## What is your current expectations of your software? For example, do you expect that it works well? What are the expected weaknesses?

### Expected Strengths:

The code is able to handle data preprocessing pretty well using Pandas, including reading from a CSV file and handling NaN values. As a result, the software should be able to take in and iterate through any well-formatted data. The binary search construction is appropriately implemented, and it is able to organize the numeric values of a specified property, as long as the data in the column is an integer or float and the specified column exists. The query functionality works, and it is able to take in the root node and range accordingly.

### Expected Weaknesses or Areas of Improvement:

One area of improvement is the memory usage. The code creates a list of dictionaries (material_dicts) in memory. For large datasets, this could consume a significant amount of memory. If memory efficiency is a concern, there are definitely ways to improve it.

Another thing is that the software might have some problems and errors if the user specifies a column that does not exist. Additionally, for columns that are not integers or floats, creating the binary tree might cause some errors.

## Additional: Interpretation of Results

The results of running the software is a dictionary, multiple dictionaries, or no dictionaries at all. These dictionaries are within a range of a parameter, previously set by the user. Additionally, this software is applicable to other databases as well (as shown by the test cases), though the instructions in the main function only apply to this database. The benefit of this selection helper is that it is able to search through a large quantity of data and return information useful to the user. Each time the user searches for a set of data, the helper resets the list that is returned, allowing for reusability.
