people_d = {'Alex': (23, 178), 'Noah': (34, 189), 'Peter': (29, 175), 'John': (41, 185), 'Michelle': (35, 165)}

# Write your code here
def people_information(dictionary, key):
      print("Name: ", key)
      age, height = dictionary[key]
      print("Age:", age, "y.o.")
      print("Height:", height, "cm")

# Testing
people_information(people_d, "Alex")
people_information(people_d, "Michelle")