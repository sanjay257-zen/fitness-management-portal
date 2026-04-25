import random
import json
from datetime import datetime, timedelta

# Constants
NUM_STUDENTS = 300
NUM_CLASSES = 1500
NUM_TRAINERS = 5
CLASS_DURATION = 60  # in minutes

# Generate mock students data
students = [{'id': i, 'name': f'Student {i}', 'email': f'student{i}@example.com'} for i in range(1, NUM_STUDENTS + 1)]

# Generate mock trainers data
trainers = [{'id': i, 'name': f'Trainer {i}', 'email': f'trainer{i}@example.com'} for i in range(1, NUM_TRAINERS + 1)]

# Generate mock classes data
classes = []
start_date = datetime.utcnow()  # Current UTC time
for i in range(NUM_CLASSES):
    class_date = start_date + timedelta(days=random.randint(0, 180))  # 6 months span
    class_time = class_date.replace(hour=random.randint(6, 21), minute=random.randint(0, 59))
    trainer = random.choice(trainers)
    classes.append({
        'id': i + 1,
        'title': f'Class {i + 1}',
        'datetime': class_time.isoformat(),
        'trainer_id': trainer['id'],
    })

# Create a mock data dictionary
mock_data = {
    'students': students,
    'trainers': trainers,
    'classes': classes,
}

# Write mock data to a JSON file
with open('mock_data.json', 'w') as f:
    json.dump(mock_data, f, indent=4)

print('Mock data generated successfully.')