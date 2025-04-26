import json

# Saving  the structured summary to a JSON file
def save_output(summary, output_file="output.json"):
    with open(output_file, 'w', encoding='utf-8') as f:  # Open the file in write mode
        json.dump(summary, f, indent=2)  # Write the summary as formatted JSON
    print(f"✅ Output saved to {output_file}")  # Confirm the output was saved
