import json
import os

# Mapping between JSON categories and Directory names
CATEGORY_MAP = {
    "Sorting Algorithms": "Sorting",
    "Searching & Selection": "Searching",
    "Divide & Conquer": "Divide_and_Conquer",
    "Graph Algorithms": "Graph_Algorithms",
    "Basic Data Structures": "Data_Structures",
    "Greedy & Practical Tech": "Greedy_Algorithms"
}

def slugify(text):
    """Converts 'Selection Sort' to 'selection_sort'"""
    return text.lower().replace(" ", "_").replace("-", "_").replace("(", "").replace(")", "").replace("/", "_")

def load_file_content(filepath):
    """Loads content of a file if it exists, otherwise returns empty string."""
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

def main():
    # Load original metadata
    metadata_path = "dsa_cheatsheet_data.json"
    if not os.path.exists(metadata_path):
        print(f"Error: {metadata_path} not found.")
        return

    with open(metadata_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    book_data = []

    for category_item in data:
        category_name = category_item["category"]
        dir_name = CATEGORY_MAP.get(category_name)
        
        if not dir_name:
            print(f"Warning: No mapping for category '{category_name}'")
            continue

        processed_category = {
            "category": category_name,
            "topics": []
        }

        for topic in category_item["topics"]:
            topic_name = topic["name"]
            slug = slugify(topic_name)
            
            # Explicit Mappings
            explicit_map = {
                "Balanced Binary Search Tree (AVL)": "balanced_binary_search",
                "Dijkstra's Algorithm": "dijkstras_algorithm",
                "Bellman-Ford": "bellman_ford_algorithm",
                "Floyd-Warshall": "floyd_warshall_algorithm",
                "BFS / DFS": ["breadth_first_search", "depth_first_search"],
                "Kruskal / Prim (MST)": ["kruskals_algorithm", "prims_algorithm"],
                "Topological Sort / Longest Path": ["topological_sort", "longest_path_dag"]
            }

            slugs = explicit_map.get(topic_name, slug)
            if isinstance(slugs, str):
                slugs = [slugs]

            theory_content = []
            code_content = []

            for s in slugs:
                # Try direct slug, then with _algorithm suffix
                options = [s, f"{s}_algorithm", f"{s}_implementation"]
                for opt in options:
                    md_path = os.path.join("..", dir_name, f"{opt}.md")
                    py_path = os.path.join("..", dir_name, f"{opt}.py")
                    
                    t = load_file_content(md_path)
                    c = load_file_content(py_path)
                    
                    if t: theory_content.append(t)
                    if c: code_content.append(c)
                    
                    if t or c: break # Found something, stop looking for suffixes

            processed_topic = topic.copy()
            processed_topic["theory"] = "\n\n---\n\n".join(theory_content)
            processed_topic["code"] = "\n\n# ---\n\n".join(code_content)
            processed_category["topics"].append(processed_topic)

        book_data.append(processed_category)

    # Save aggregated data
    output_path = "dsa_book_data.js"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("const SOURCE_DATA = ")
        json.dump(book_data, f, indent=2)
        f.write(";")
    
    print(f"Successfully generated {output_path}")

if __name__ == "__main__":
    main()
