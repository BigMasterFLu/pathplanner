# List of commands
commands = [
    "AutoAimLeft",
    "AutoAimRight",
    "AutoAlign",
    "L1",
    "L2",
    "L3",
    "L4",
    "Outtake",
    "Intake",
    "Low Algae",
    "High Algae"
]

# Data list from the previous script (only names)
data_names = [
    "S1", "S2", "S3", "TR", "TL", "MR", "ML", "BR", "BL", 
    "Algae T", "Algae M", "Algae B", "Processor"
]

def generate_combinations():
    starts_input = input("Enter start elements separated by commas: ").strip().split(", ")
    starts = [s for s in starts_input if s in data_names]
    
    middles_input = input("Enter middle elements separated by commas: ").strip().split(", ")
    middles = [m for m in middles_input if m in data_names]
    
    end_input = input("Enter an end element: ").strip()
    end = end_input if end_input in data_names else None
    
    if not starts:
        return
    if not middles:
        return
    if not end:
        return
    
    for start in starts:
        for middle in middles:
            if middle in ["TL", "TR", "ML", "MR", "BL", "BR"]:
                for l_command in ["L1", "L2", "L3", "L4"]:
                    # Parallel command group for AutoAimLeft, AutoAimRight, AutoAlign, and L commands
                    parallel_group_left = f"(AutoAimLeft, AutoAlign, {l_command})"
                    parallel_group_right = f"(AutoAimRight, AutoAlign, {l_command})"
                    
                    # Add Outtake and High/Low Algae based on constraints
                    if l_command == "L2":
                        # L2 cannot have Low Algae
                        print(f"{start} - {middle} - {end}: {start} - {middle}, {parallel_group_left}, Outtake, High Algae, Intake, {middle} - {end}" + (", Outtake" if end == "Processor" else ""))
                        print(f"{start} - {middle} - {end}: {start} - {middle}, {parallel_group_right}, Outtake, High Algae, Intake, {middle} - {end}" + (", Outtake" if end == "Processor" else ""))
                    elif l_command == "L3":
                        # L3 cannot have Low Algae or High Algae
                        print(f"{start} - {middle} - {end}: {start} - {middle}, {parallel_group_left}, Outtake, Intake, {middle} - {end}" + (", Outtake" if end == "Processor" else ""))
                        print(f"{start} - {middle} - {end}: {start} - {middle}, {parallel_group_right}, Outtake, Intake, {middle} - {end}" + (", Outtake" if end == "Processor" else ""))
                    else:
                        # L1 and L4 can have either High Algae or Low Algae
                        print(f"{start} - {middle} - {end}: {start} - {middle}, {parallel_group_left}, Outtake, High Algae, Intake, {middle} - {end}" + (", Outtake" if end == "Processor" else ""))
                        print(f"{start} - {middle} - {end}: {start} - {middle}, {parallel_group_left}, Outtake, Low Algae, Intake, {middle} - {end}" + (", Outtake" if end == "Processor" else ""))
                        print(f"{start} - {middle} - {end}: {start} - {middle}, {parallel_group_right}, Outtake, High Algae, Intake, {middle} - {end}" + (", Outtake" if end == "Processor" else ""))
                        print(f"{start} - {middle} - {end}: {start} - {middle}, {parallel_group_right}, Outtake, Low Algae, Intake, {middle} - {end}" + (", Outtake" if end == "Processor" else ""))
            else:
                # Normal path without AutoAim, AutoAlign, or L commands
                print(f"{start} - {middle} - {end}: {start} - {middle}, {middle} - {end}" + (", Outtake" if end == "Processor" else ""))

generate_combinations()