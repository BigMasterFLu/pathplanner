import json
import os

# Ensure the 'autos' folder exists
os.makedirs("autos", exist_ok=True)

data_names = [
    "S1", "S2", "S3", "TR", "TL", "MR", "ML", "BR", "BL", "Processor"
]

commands = [
    "AutoAimLeft", "AutoAimRight", "AutoAlign", "L1", "L2", "L3", "L4", "Outtake", "Intake", "Low Algae", "High Algae"
]

def generate_auto_file(start, middle, end, command_sequence, suffix):
    # Replace names for file naming purposes
    suffix = suffix.replace("AutoAimLeft", "Left").replace("AutoAimRight", "Right").replace("High Algae", "High").replace("Low Algae", "Low")
    file_name = f"autos/{start}-{middle}-{end}-{suffix}.auto"
    file_content = {
        "version": "2025.0",
        "command": {
            "type": "sequential",
            "data": {
                "commands": command_sequence
            }
        },
        "resetOdom": True,
        "folder": None,
        "choreoAuto": False
    }
    
    with open(file_name, "w") as f:
        json.dump(file_content, f, indent=2)
    print(f"Generated: {file_name}")

def generate_combinations():
    starts_input = input("Enter start elements separated by commas: ").strip().split(",")
    starts = [s.strip() for s in starts_input if s.strip() in data_names]
    
    middles_input = input("Enter middle elements separated by commas: ").strip().split(",")
    middles = [m.strip() for m in middles_input if m.strip() in data_names]
    
    end_input = input("Enter end elements separated by commas: ").strip().split(",")
    ends = [e.strip() for e in end_input if e.strip() in data_names]
    
    if not starts or not middles or not ends:
        return
    
    for start in starts:
        for middle in middles:
            for end in ends:
                if middle == end:
                    continue
                for autoaim in ["AutoAimLeft", "AutoAimRight"]:
                    for algae in ["High Algae", "Low Algae"]:
                        for l_command in ["L1", "L2", "L3", "L4"]:
                            command_sequence = [
                                {"type": "path", "data": {"pathName": f"{start} - {middle}"}},
                                {
                                    "type": "parallel",
                                    "data": {
                                        "commands": [
                                            {"type": "named", "data": {"name": autoaim}},
                                            {"type": "named", "data": {"name": "AutoAlign"}},
                                            {"type": "named", "data": {"name": l_command}}
                                        ]
                                    }
                                },
                                {"type": "named", "data": {"name": "Outtake"}},
                                {"type": "named", "data": {"name": algae}},
                                {"type": "named", "data": {"name": "Intake"}},
                                {"type": "path", "data": {"pathName": f"{middle} - {end}"}}
                             ]
                            if end == "Processor":
                                command_sequence.append({"type": "named", "data": {"name": "Outtake"}})
                            suffix = f"{autoaim}-{algae}-{l_command}"
                            generate_auto_file(start, middle, end, command_sequence, suffix)

generate_combinations()