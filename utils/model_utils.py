import os
import pickle

# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def save_model(model, filename="best_model.pkl"):
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    artifacts_dir = os.path.join(project_root, "artifacts")
    os.makedirs(artifacts_dir, exist_ok=True)

    model_path = os.path.join(artifacts_dir, filename)
    with open(model_path, mode="wb") as f:
        pickle.dump(model, f)

    print(f"Model has been saved in {model_path}")
    return model_path

