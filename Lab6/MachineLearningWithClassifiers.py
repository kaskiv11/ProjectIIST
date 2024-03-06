#   1. Download the "2022 Ukraine Russia War" dataset from the site https://www.kaggle.com/datasets/piterfm/2022-ukraine-russian-war (I
#downloaded this dataset and placed it on my Google Drive)
#   2. Visualize the losses of Muscovites, tanks,...
#   3. Apply training on the subject "on what day was the war" lost the same number of tanks and planes? For what period
#the number of downed drones exceeded the number of tanks? (May be some condition of yours, because I am not very sure whether it is possible well perform)
#   4. Apply classifiers
#   1. The method of k-nearest neighbors (K-Nearest Neighbors);
#   2. Method of support vectors (Support Vector Machines);
#   3. Decision Tree Classifier / Random forest (Random Forests);
#   4. Naive Bayes method (Naive Bayes);
#   5. Linear discriminant analysis (Linear discriminant analysis);
#   6. Logistic regression (Logistic Regression)

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.exceptions import ConvergenceWarning
import warnings

# Load data
equipment_losses_file = 'archive/russia_losses_equipment.csv'
personnel_losses_file = 'archive/russia_losses_personnel.csv'
equipment_corr_losses_file = 'archive/russia_losses_equipment_correction.csv'

equipment_losses = pd.read_csv(equipment_losses_file)
personnel_losses = pd.read_csv(personnel_losses_file)
equipment_corr_losses = pd.read_csv(equipment_corr_losses_file)

# Task 1: Visualization of Russian equipment losses
plt.figure(figsize=(10, 6))
equipment_cols = ['aircraft', 'helicopter', 'tank', 'APC', 'field artillery', 'MRL',
                   'military auto', 'fuel tank', 'drone', 'naval ship', 'anti-aircraft warfare',
                   'special equipment', 'mobile SRBM system', 'vehicles and fuel tanks', 'cruise missiles', 'submarines']
for col in equipment_cols:
    plt.plot(equipment_losses['day'], equipment_losses[col], label=col)

# Task 1: Visualization of Russian equipment losses
plt.figure(figsize=(12, 8))  # Збільшуємо розмір фігури
for col in equipment_cols:
    plt.plot(equipment_losses['day'], equipment_losses[col], label=col, linewidth=2)  # Збільшуємо товщину лінії

plt.xlabel('Day')
plt.ylabel('Equipment Losses')
plt.title('Russian Equipment Losses Over Time')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize='small')  # Зменшуємо розмір шрифту легенди
plt.grid(True, linestyle='--', alpha=0.5)  # Додаємо сітку з пунктиром та знижуємо її прозорість
plt.tight_layout()  # Оптимізуємо розміщення графіку
plt.show()

# Task 1.1: Visualization of Russian personnel losses
plt.figure(figsize=(12, 6))  # Змінюємо розмір фігури
plt.plot(personnel_losses['day'], personnel_losses['personnel'], label='Personnel Losses', color='black', linestyle='-', marker='o')  # Встановлюємо чорний колір, з'єднання ліній, та маркери точок
plt.xlabel('Day')
plt.ylabel('Personnel Losses')
plt.title('Russian Personnel Losses Over Time')
plt.legend(fontsize='small')  # Зменшуємо розмір шрифту легенди
plt.grid(True, linestyle='--', alpha=0.5)  # Додаємо сітку з пунктиром та знижуємо її прозорість
plt.tight_layout()  # Оптимізуємо розміщення графіку
plt.show()

# Task 2: Analysis of equipment losses
# Calculate the difference between downed drones and destroyed tanks
equipment_losses['drone_tank_diff'] = equipment_losses['drone'] - equipment_losses['tank']
days_exceed_tanks = (equipment_losses['drone_tank_diff'] > 0).sum()

# Find the day with the largest total increase in equipment losses
total_equipment_diff = equipment_losses[equipment_cols].diff().sum(axis=1)
max_equipment_day = equipment_losses['date'][total_equipment_diff.idxmax()]

# Calculate the total number of air units shot down (including drones)
total_air_units_shot_down = equipment_losses['aircraft'] + equipment_losses['helicopter'] + equipment_losses['drone']

# Find the direction with the most mentions for the biggest losses of equipment
most_mentioned_direction = equipment_losses['greatest losses direction'].value_counts().idxmax()

# Display results for Task 2
print(f"Days when downed drones exceeded destroyed tanks: {days_exceed_tanks} days")
print(f"On which day was the largest total increase in equipment losses: {max_equipment_day}")
print(f"Total number of air units shot down: {total_air_units_shot_down.sum()}")
print(f"Most mentioned direction for the biggest losses of equipment: {most_mentioned_direction}")

# Task 3: Apply classifiers
merged_data = pd.merge(equipment_losses, personnel_losses, on=['date', 'day'])

# Create bins for the counts and assign labels
bins = [0, 50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000, float('inf')]
labels = ['0-50k', '50k-100k', '100k-150k', '150k-200k', '200k-250k', '250k-300k', '300k-350k', '350k-400k', '400k+']

merged_data['personnel_category'] = pd.cut(merged_data['personnel'], bins=bins, labels=labels, right=False)

X = merged_data[equipment_cols]
y = merged_data['personnel_category']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Impute missing values and scale the features
imputer = SimpleImputer(strategy='mean')
X_train_imputed = imputer.fit_transform(X_train)
X_test_imputed = imputer.transform(X_test)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_imputed)
X_test_scaled = scaler.transform(X_test_imputed)

warnings.filterwarnings("ignore", category=ConvergenceWarning)

# Initialize classifiers
classifiers = {
    'K-Nearest Neighbors': KNeighborsClassifier(),
    'Support Vector Machines': SVC(),
    'Decision Tree Classifier': DecisionTreeClassifier(),
    'Random Forests': RandomForestClassifier(),
    'Naive Bayes': GaussianNB(),
    'Linear Discriminant Analysis': LinearDiscriminantAnalysis(),
    'Logistic Regression': LogisticRegression(max_iter=1000)
}

# Train and evaluate classifiers
for name, clf in classifiers.items():
    clf.fit(X_train_scaled, y_train)
    accuracy = clf.score(X_test_scaled, y_test)
    print(f"{name} - Accuracy: {accuracy}")

# Task 4: Display results (already displayed during Task 2)

import matplotlib.pyplot as plt

# Initialize an empty dictionary to store accuracies
accuracies = {}

# Train and evaluate classifiers
for name, clf in classifiers.items():
    clf.fit(X_train_scaled, y_train)
    accuracy = clf.score(X_test_scaled, y_test)
    accuracies[name] = accuracy

# Plot the accuracies
plt.figure(figsize=(12, 6))
plt.bar(accuracies.keys(), accuracies.values(), color='skyblue')
plt.xlabel('Classifier')
plt.ylabel('Accuracy')
plt.title('Accuracy of Different Classifiers')
plt.ylim(0, 1)  # Set y-axis limits from 0 to 1
plt.xticks(rotation=45, ha='right')
plt.show()




# Find the days when the number of lost tanks and aircraft was equal
equipment_losses['tank_aircraft_diff'] = equipment_losses['tank'] - equipment_losses['aircraft']
equal_tank_aircraft_days = equipment_losses[equipment_losses['tank_aircraft_diff'] == 0]['day']

# Find the periods when the number of shot down drones exceeded the number of lost tanks
equipment_losses['drones_exceeded_tanks'] = (equipment_losses['drone'] - equipment_losses['tank']) > 0
drones_exceeded_tanks_periods = []
start_day = None
for index, row in equipment_losses.iterrows():
    if row['drones_exceeded_tanks'] and start_day is None:
        start_day = row['day']
    elif not row['drones_exceeded_tanks'] and start_day is not None:
        drones_exceeded_tanks_periods.append((start_day, row['day']))
        start_day = None
if start_day is not None:
    drones_exceeded_tanks_periods.append((start_day, equipment_losses.iloc[-1]['day']))

# Plot the equipment losses over time
plt.figure(figsize=(12, 8))
plt.step(equipment_losses['day'], equipment_losses['tank'], label='Tanks', where='mid')
plt.step(equipment_losses['day'], equipment_losses['aircraft'], label='Aircraft', where='mid')
plt.step(equipment_losses['day'], equipment_losses['drone'], label='Drones', where='mid')

# Highlight the days when the number of tanks and aircraft was equal
plt.scatter(equal_tank_aircraft_days, [0] * len(equal_tank_aircraft_days), color='blue', label='Equal Tanks and Aircraft')

# Highlight the periods when the number of shot down drones exceeded the number of tanks
for period in drones_exceeded_tanks_periods:
    plt.axvspan(period[0], period[1], color='red', alpha=0.3, label='Drones Exceeded Tanks Periods')

plt.xlabel('Day')
plt.ylabel('Number of Units')
plt.title('Equipment Losses Over Time')
plt.legend()
plt.show()

plt.figure(figsize=(8, 7))

