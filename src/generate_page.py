import os
from block_markdown import extract_title, markdown_to_html_node
from htmlnode import HTMLNode


def generate_page(from_path, template_path, dest_path):
    from_abs = os.path.abspath(from_path)
    template_abs = os.path.abspath(template_path)
    dest_abs = os.path.abspath(dest_path)
    print(f"generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_abs) as f:
        print(f"opening and reading {from_path}")
        markdown = f.read()

    with open(template_abs) as f:
        print(f"opening and reading {template_path}")
        template = f.read()

    html_node = markdown_to_html_node(markdown)
    html_string = html_node.to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)

    dir_name_dest_path = os.path.dirname(dest_abs)

    if not os.path.exists(dir_name_dest_path):
        os.makedirs(dir_name_dest_path)

    with open(dest_abs, "w") as f:
        _ = f.write(template)

def generate_files_recursively(from_path, template_path):
    for path in os.listdir(from_path):
        path = os.path.join(from_path, path)
        from_new = path
        dest_new = path.replace("/content", "/public")
        dest_new = dest_new.replace(".md", ".html")
        if os.path.isdir(path):
            generate_files_recursively(from_new, template_path)
        elif path.endswith(".md"):
            generate_page(from_new, template_path, dest_new)
