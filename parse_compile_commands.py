import json
import sys

def find_include_paths(compile_commands_path, source_file):
    with open(compile_commands_path, 'r') as f:
        compile_commands = json.load(f)

    for command in compile_commands:
        if command['file'] == source_file:
            return ' '.join(command['command'].split()[4::2])

    return ''

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: parse_compile_commands.py <path_to_compile_commands.json> <path_to_source_file>")

    compile_commands_path = sys.argv[1]
    source_file = sys.argv[2]

    include_paths = find_include_paths(compile_commands_path, source_file)
    print(include_paths)
