import subprocess
import fileinput

# ~ def build_onepage(*args, **kwargs):
def build_onepage(*args, **kwargs):
    subprocess.call( [ "mkdocs2pandoc","-f","mkdocs.yml","-o","docs/one.md" ] )
    

    # Remove lines 6 to 22 and replace '#' with '##' for a nice toc generation
    with fileinput.FileInput("docs/one.md", inplace=True) as infile:
        for line in infile:
            if infile.lineno() > 6 and infile.lineno() < 22 :
                continue
            print( (line.replace('##', '#') ).replace( '#', '##' ) , end='')
