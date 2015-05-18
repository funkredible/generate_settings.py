# argv[0]: Output file name.
# argv[1]: Template file name. Template file must be in templates dir.
# argv[2]: Tag(branch) name.
import sys, os
from jinja2 import Environment, FileSystemLoader

template_dir = 'templates'

env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), template_dir)))
template = env.get_template(sys.argv[2])
output_from_template = template.render(tag_name=sys.argv[3])

# to save the results
with open(os.path.join(os.path.dirname(__file__), sys.argv[1]), "wb") as fh:
    fh.write(bytes(output_from_template, 'UTF-8'))
