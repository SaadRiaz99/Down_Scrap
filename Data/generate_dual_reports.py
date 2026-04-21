import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import os

def generate_dual_visuals_v2():
    csv_files = glob.glob("*.csv")
    output_dir = "individual_graphs"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    print(f"Updating {len(csv_files)} reports with 2-word headings and clear axis labels...")

    for file_path in csv_files:
        file_name = os.path.basename(file_path)
        base_name = os.path.splitext(file_name)[0]
        
        # Determine a 2-word heading based on the filename
        if "student" in base_name.lower():
            heading = "Student Data"
        elif "behavior" in base_name.lower():
            heading = "Behavior Data"
        elif "performance" in base_name.lower() or "mobile" in base_name.lower():
            heading = "Performance Data"
        else:
            heading = "Report Data"

        try:
            df = pd.read_csv(file_path)
            line_df = df.head(150) if len(df) > 150 else df
            numeric_cols = df.select_dtypes(include=['number']).columns
            categorical_cols = df.select_dtypes(include=['object', 'bool']).columns
            
            if len(numeric_cols) < 1:
                continue
            target_val = numeric_cols[-1]

            plt.figure(figsize=(20, 8))
            
            # --- 1. THE LINE GRAPH ---
            plt.subplot(1, 2, 1)
            plt.plot(line_df.index, line_df[target_val], color='teal', linewidth=1, marker='o', markersize=2)
            plt.title(f"{heading} Line", fontsize=16)
            plt.xlabel("Index Count")
            plt.ylabel(f"{target_val} Value")
            plt.grid(True, alpha=0.3)

            # --- 2. THE BAR GRAPH ---
            plt.subplot(1, 2, 2)
            if len(categorical_cols) > 0:
                cat_col = categorical_cols[0]
                avg_data = df.groupby(cat_col)[target_val].mean().reset_index()
                sns.barplot(x=cat_col, y=target_val, data=avg_data, palette='viridis')
                plt.title(f"{heading} Bar", fontsize=16)
                plt.xlabel(f"{cat_col} Category")
                plt.ylabel(f"Average {target_val}")
            else:
                sample_df = df.head(15)
                plt.bar(sample_df.index.astype(str), sample_df[target_val], color='orange')
                plt.title(f"{heading} Bar", fontsize=16)
                plt.xlabel("Record ID")
                plt.ylabel(f"{target_val} Score")
            
            plt.xticks(rotation=45)
            plt.tight_layout()
            output_path = os.path.join(output_dir, f"{base_name}_dual_report.png")
            plt.savefig(output_path)
            plt.close()
            print(f"✅ Updated: {output_path}")

        except Exception as e:
            print(f"❌ Error on {file_name}: {e}")

if __name__ == "__main__":
    generate_dual_visuals_v2()
