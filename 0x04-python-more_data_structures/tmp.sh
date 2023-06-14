#!/usr/bin/python3
#!/bin/bash
for file in *; do
	  if [[ -f "$file" ]]; then
		      echo "#!/usr/bin/python3" > "$file.tmp"
		          cat "$file" >> "$file.tmp"
			      mv "$file.tmp" "$file"
			        fi
			done

