# kicad-custom-symbols
Custom symbols for kicad

# Directory Structure
All directories at top-level are considered to be "Part Categories"
Within each category there exist "Part Families". These families are 
what KiCAD considers to be separate symbol libraries. 

# Usage 
THe "build.sh" script in the root directory will go through each 
"Part Category" directory and run any "build.sh" script that it finds.
This is mainly used to invoke kipart to regenerate symbols.
