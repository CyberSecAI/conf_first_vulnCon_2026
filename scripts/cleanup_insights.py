
import os
import re

def final_cleanup():
    files = os.listdir('insights')
    for filename in files:
        if not filename.endswith('.md'): continue
        filepath = os.path.join('insights', filename)
        with open(filepath, 'r') as f: lines = f.readlines()
        
        new_lines = []
        skip_next = False
        for i in range(len(lines)):
            if skip_next:
                skip_next = False
                continue
            
            # Match "The speaker, [Name], discusses the topic."
            match = re.search(r'The speaker(?:s)?, (.*?), discusses the topic\.', lines[i])
            if match:
                speaker = match.group(1)
                # Check if the next non-empty line contains the speaker name
                j = i + 1
                while j < len(lines) and not lines[j].strip():
                    j += 1
                
                if j < len(lines) and speaker in lines[j]:
                    # Duplicate found, skip this line
                    continue
            
            new_lines.append(lines[i])
            
        with open(filepath, 'w') as f: f.writelines(new_lines)

if __name__ == "__main__":
    final_cleanup()
