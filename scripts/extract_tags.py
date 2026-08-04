"""Extract all mph feature types from tags.json into organized references."""
import json, os

TAGS_PATH = r"C:\Users\xueqianz\AppData\Local\Programs\Python\Python313\Lib\site-packages\mph\tags.json"
OUT_DIR = r"D:\ENV\claude\comsol-skill\references"
SEP = " \u2192 "  # RIGHTWARDS ARROW with surrounding spaces

with open(TAGS_PATH, "r", encoding="utf-8-sig") as f:
    tags = json.load(f)

# Build hierarchy — keys like "physics", "physics SEP SolidMechanics", etc.
hier = {}
for k, v in tags.items():
    parts = k.split(SEP)
    node = hier
    for p in parts[:-1]:
        if isinstance(node, str):
            # Current node is a leaf — need to promote to container
            # This shouldn't happen with proper parsing but handle gracefully
            break
        if p not in node:
            node[p] = {}
        elif isinstance(node[p], str):
            # Existing node is leaf → promote to container
            node[p] = {"__tag__": node[p]}
        node = node[p]
    # Set last part
    last = parts[-1]
    if isinstance(node, str):
        continue  # can't add child to leaf
    if last in node and isinstance(node[last], dict):
        node[last]["__tag__"] = v
    else:
        node[last] = v


def write_tree(node, f, depth=0):
    """Write tree structure to file handle."""
    if isinstance(node, str):
        return  # leaf at root shouldn't happen

    items = sorted(node.items())
    # Separate dict children from leaf values
    containers = [(n, v) for n, v in items if isinstance(v, dict) and n != "__tag__"]
    leaves = [(n, v) for n, v in items if not isinstance(v, dict) and n != "__tag__"]

    # Print own _value if exists
    own_val = node.get("__tag__", "")
    if own_val:
        indent = "  " * depth
        f.write(f"{indent}Tag: `{own_val}`\n")

    for name, val in containers + leaves:
        indent = "  " * depth
        if isinstance(val, dict):
            f.write(f"\n{indent}### {name}\n")
            # Print _value for container nodes
            cv = val.get("__tag__", "")
            if cv:
                f.write(f"{indent}Tag: `{cv}`\n")
            write_tree(val, f, depth + 1)
        else:
            f.write(f"{indent}- `{name}` -> `{val}`\n")


# Extract per category
categories = {
    "physics": "Physics Interfaces",
    "multiphysics": "Multiphysics Couplings",
    "geometries": "Geometry Features",
    "meshes": "Mesh Features",
    "studies": "Study Features",
    "results": "Results Features",
    "selections": "Selection Types",
    "functions": "Function Types",
    "materials": "Material Types",
    "batches": "Batch/Sweep Types",
}

os.makedirs(OUT_DIR, exist_ok=True)

for cat_key, cat_label in categories.items():
    if cat_key not in hier:
        continue

    path = os.path.join(OUT_DIR, f"tags_{cat_key}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# {cat_label} — mph Feature Tags\n\n")
        f.write(f"Extracted from mph tags.json (COMSOL 6.4).\n")
        f.write(f"Feature type strings for use with `create(tag, type_string, dim)`.\n\n")
        write_tree(hier[cat_key], f)

    # Count leaves
    def count_leaves(node):
        if isinstance(node, str):
            return 1
        n = 1 if node.get("__tag__") else 0
        for k, v in node.items():
            if k == "__tag__":
                continue
            if isinstance(v, dict):
                n += count_leaves(v)
            else:
                n += 1
        return n

    root_node = hier[cat_key]
    if isinstance(root_node, str):
        print(f"  {cat_label}: 1 feature (root leaf) -> {path}")
        continue
    leaf_count = count_leaves(root_node)
    print(f"Saved {cat_label}: {leaf_count} features -> {path}")

print("Done!")
