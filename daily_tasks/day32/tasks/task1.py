import kagglehub
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("spscientist/students-performance-in-exams")

print("Path to dataset files:", path)

df = pd.read_csv(os.path.join(path, "Students_performance.csv"))

