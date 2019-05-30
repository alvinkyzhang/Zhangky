import sys
for line in sys.stdin:
    
    line = line.strip() # Remove white spaces
    
    words = line.split() # Split the line into words
    
    for word in words:
        print(word, 1)
