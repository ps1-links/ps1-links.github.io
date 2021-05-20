import subprocess

# ~ def build_onepage(*args, **kwargs):
def build_onepage(*args, **kwargs):
    subprocess.call( [ "mkdocs2pandoc","-f","mkdocs.yml","-o","docs/one.md" ] )
