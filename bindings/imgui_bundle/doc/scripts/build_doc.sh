#!/usr/bin/env bash

# You will need to install asciidoctor, asciidoctor-reducer and pandoc:
#     brew install asciidoctor
#     gem install asciidoctor-reducer
#     brew install pandoc

this_dir=$(dirname -- "$0")
doc_dir=$this_dir/..
cd $doc_dir

# asciidoctor-reducer will preprocess the includes, so that github display the readme nicely
echo "generate Readme.adoc (for github)"
asciidoctor-reducer Readme_source.adoc -o Readme.adoc

# Generate a markdown doc for pypi
echo "Generating Readme_pypi.md (for pypi)"
asciidoctor -b docbook --attribute env_pypi=1 Readme_source.adoc
pandoc -f docbook -t markdown_strict Readme_source.xml -o ../Readme_pypi.md

# Generate html doc
echo "Generating html/Readme.html (for github pages)"
asciidoctor Readme_source.adoc -o html/Readme.html
