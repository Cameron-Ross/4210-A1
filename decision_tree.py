#-------------------------------------------------------------------------
# AUTHOR: Cameron Ross
# FILENAME: decision_tree.py
# SPECIFICATION: Create a decision tree for a dataset
# FOR: CS 4210- Assignment #1
# TIME SPENT: ~10 min
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

# importing some Python libraries 
from sklearn import tree
import matplotlib.pyplot as plt, csv
db = []
X = []
Y = []

# reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append(row)
         print(row)

for i in range(len(db)):
  record = db[i]
  list = []
  # Age  
  if record[0] == 'Young': list.append(1)
  elif record[0] == 'Presbyopic': list.append(2)
  else: list.append(3)
  # Prescription  
  list.append(1 if record[1] == 'Hypermetrope' else 2)
  # Astigmatism  
  list.append(1 if record[2] == 'No' else 2)
  # Tears  
  list.append(1 if record[3] == 'Normal' else 2)
  # Append
  X.append(list)
  Y.append(1 if record[4] == 'No' else 2)


# fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

# plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()