import re
import os


def rename_functions_in_file(file_path):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Print the size of the original file
    original_size = os.path.getsize(file_path)
    print(f"Original file size: {original_size} bytes")
    
    # Find all function definitions
    function_pattern = re.compile(r'def (\w+)\(')
    functions = function_pattern.findall(content)
    
    # Rename functions to single letters
    new_content = content
    letter = ord('a')
    function_mapping = {}
    
    for func_name in functions:
        new_func_name = chr(letter)
        if letter > ord('z'):
            raise ValueError("Not enough letters to rename all functions.")
        function_mapping[func_name] = new_func_name
        letter += 1
    
    # Replace old function names with new ones
    for old_name, new_name in function_mapping.items():
        new_content = re.sub(rf'\b{old_name}\b', new_name, new_content)
        
    # Create the new file path with "_better" appended
    base, ext = os.path.splitext(file_path)
    new_file_path = f"{base}_better{ext}"
    
    # Write the updated content to the new file
    with open(new_file_path, 'w') as file:
        file.write(new_content)
    
    # Print the size of the new file
    new_file_size = os.path.getsize(new_file_path)
    print(f"New file size: {new_file_size} bytes")
    compression_ratio = round(((original_size - new_file_size) / original_size) * 100, 2)
    print(f"Wow!!! We compressed the file by {compression_ratio}%")
    
    print(f"Functions renamed successfully! New file created: {new_file_path}")
    
rename_functions_in_file("math_util.py")
