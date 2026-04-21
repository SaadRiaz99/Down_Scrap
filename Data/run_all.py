import subprocess
import os

def run_script(script_name, args=None):
    print(f"\n>>> Running {script_name}...")
    try:
        command = ["uv", "run", script_name]
        if args:
            command.extend(args)
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"SUCCESS: {script_name} finished.")
            print(result.stdout)
        else:
            print(f"FAILED: {script_name} exited with code {result.returncode}")
            print(result.stderr)
    except Exception as e:
        print(f"ERROR running {script_name}: {str(e)}")

if __name__ == "__main__":
    # 1. Run the generic plot script
    run_script("main.py")

    # 2. Run the Human Behavior Analysis (E-commerce)
    run_script("analyze_behavior.py")

    # 3. Run the Mobile Usage vs Academic Performance Analysis
    run_script("analyze_performance.py")

    print("\n--- Project Run Summary ---")
    files_to_check = [
        "human_behavior_data.csv", 
        "behavior_analysis.png", 
        "mobile_usage_academic_performance.csv", 
        "academic_performance_analysis.png",
        "plot.png"
    ]
    
    for f in files_to_check:
        status = "Exists" if os.path.exists(f) else "Missing"
        print(f"File {f:40} : {status}")
