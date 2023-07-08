import os
import random
import shutil

# Define the path to your dataset folder
dataset_path = os.getcwd()

# Define the path to your data folder
data_path = os.path.join(dataset_path, "data")

# Define the paths to the two subfolders
submarine_path = os.path.join(data_path, "submarine")
sailboat_path = os.path.join(data_path, "sailboat")

# Define the paths to the train and test subfolders inside the dataset folder
train_path = os.path.join(dataset_path, "dataset/train")
test_path = os.path.join(dataset_path, "dataset/test")
sub_train_path = os.path.join(train_path, "submarine")
sub_test_path = os.path.join(test_path, "submarine")
sail_train_path = os.path.join(train_path, "sailboat")
sail_test_path = os.path.join(test_path, "sailboat")

# Delete the train and test folders if they already exist
if os.path.exists(train_path):
    shutil.rmtree(train_path)
if os.path.exists(test_path):
    shutil.rmtree(test_path)

# Create the train and test directories
os.makedirs(sub_train_path)
os.makedirs(sub_test_path)
os.makedirs(sail_train_path)
os.makedirs(sail_test_path)

# Define the size of the train set as a percentage of the total data
train_size = 0.8

# Loop through each subfolder
for subfolder_name in ["submarine", "sailboat"]:
    # Get the list of image file names in the subfolder
    file_names = os.listdir(os.path.join(data_path, subfolder_name))
    # Shuffle the file names randomly
    random.shuffle(file_names)
    # Split the file names into train and test sets
    train_file_names = file_names[:int(len(file_names)*train_size)]
    test_file_names = file_names[int(len(file_names)*train_size):]
    # Loop through the train file names and copy them to the appropriate train subfolder
    for file_name in train_file_names:
        src_path = os.path.join(data_path, subfolder_name, file_name)
        if subfolder_name == "submarine":
            dst_path = os.path.join(sub_train_path, file_name)
        else:
            dst_path = os.path.join(sail_train_path, file_name)
        shutil.copy(src_path, dst_path)
    # Loop through the test file names and copy them to the appropriate test subfolder
    for file_name in test_file_names:
        src_path = os.path.join(data_path, subfolder_name, file_name)
        if subfolder_name == "submarine":
            dst_path = os.path.join(sub_test_path, file_name)
        else:
            dst_path = os.path.join(sail_test_path, file_name)
        shutil.copy(src_path, dst_path)