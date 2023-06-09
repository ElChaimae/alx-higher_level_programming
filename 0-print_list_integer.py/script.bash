#!/usr/bin/python3
#!/bin/bash

for file in *
do
	    if [ -f "$file" ]; then
		            echo "#!/usr/bin/python3" | cat - "$file" > temp && mv temp "$file"
			        fi
			done
