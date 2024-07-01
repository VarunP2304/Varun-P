# Define two fuzzy sets
A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
B = {"a": 0.9, "b": 0.9, "c": 0.4, "d": 0.5}

# Check if A is a subset of B
def is_subset(A, B):
    return all(A[key] <= B.get(key, 0) for key in A)

# Check if B is a superset of A
def is_superset(A, B):
    return all(B[key] >= A.get(key, 0) for key in A)

# Function to perform union of fuzzy sets
def fuzzy_union(A, B):
    Y = {}
    for key in A.keys() | B.keys():
        Y[key] = max(A.get(key, 0), B.get(key, 0))
    return Y

# Function to perform intersection of fuzzy sets
def fuzzy_intersection(A, B):
    Y = {}
    for key in A.keys() & B.keys():
        Y[key] = min(A[key], B[key])
    return Y

# Function to perform difference of fuzzy sets (A - B)
def fuzzy_difference(A, B):
    Y = {}
    for key in A.keys() | B.keys():
        Y[key] = A.get(key, 0) - B.get(key, 0)
    return Y

# Printing the original fuzzy sets
print('The First Fuzzy Set is :', A)
print('The Second Fuzzy Set is :', B)

# Checking subset and superset relationships
if is_subset(A, B):
    print("A is a subset of B")
else:
    print("A is not a subset of B")

if is_superset(A, B):
    print("B is a superset of A")
else:
    print("B is not a superset of A")

# Performing fuzzy set operations
union_result = fuzzy_union(A, B)
intersection_result = fuzzy_intersection(A, B)
difference_result = fuzzy_difference(A, B)

# Printing the results of fuzzy set operations
print('Fuzzy Set Union is :', union_result)
print('Fuzzy Set Intersection is :', intersection_result)
print('Fuzzy Set Difference (A - B) is :', difference_result)