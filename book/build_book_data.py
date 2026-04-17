import json
import os

# Mapping between JSON categories and Directory names
CATEGORY_MAP = {
    "Sorting Algorithms": "Sorting",
    "Searching & Selection": "Searching",
    "Divide & Conquer": "Divide_and_Conquer",
    "Graph Algorithms": "Graph_Algorithms",
    "Basic Data Structures": "Data_Structures",
    "Greedy & Practical Tech": "Greedy_Algorithms",
    "Dynamic Programming": "Dynamic_Programming",
    "Practice Sessions": "Practice_Problems"
}

def slugify(text):
    """Converts 'Selection Sort' to 'selection_sort'"""
    return text.lower().replace(" ", "_").replace("-", "_").replace("'", "").replace("(", "").replace(")", "").replace("/", "_")

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
                "Quick Select / Fast Select": "Divide_and_Conquer/quick_select_algorithm",
                "Closest Pair of Points": "closest_pair",
                "Karatsuba's Multiplication": "karatsubas_multiplication",
                "Counting Inversions": "counting_inversions",
                "Dijkstra's Algorithm": "dijkstras_algorithm",
                "Bellman-Ford": "bellman_ford_algorithm",
                "Floyd-Warshall": "floyd_warshall_algorithm",
                "BFS / DFS": ["breadth_first_search", "depth_first_search"],
                "Kruskal's Algorithm": "kruskals_algorithm",
                "Prim's Algorithm": "prims_algorithm",
                "Topological Sort / Longest Path": ["topological_sort", "longest_path_dag"],
                "Stack / Queue": ["stack_implementation", "queue_implementation"],
                "Union-Find (Disjoint Set)": "union_find",
                "Quiz 1 - Practice Problems": "Practice_Problems/Quiz_1/quiz_1_practice",
                "Fibonacci (DP Case Study)": ["fibonacci", "fibonacci_dp"],
                "House Robber (Max Loot)": "house_robber",
                "Unique Grid Paths": "grid_paths",
                "Longest Common Subsequence (LCS)": "longest_common_subsequence",
                "Longest Common Subword (LCW)": "longest_common_substring"
            }

            slugs = explicit_map.get(topic_name, slug)
            if isinstance(slugs, str):
                slugs = [slugs]

            theory_content = []
            code_content = []

            for s in slugs:
                # Handle cross-directory mappings (e.g., "Divide_and_Conquer/slug")
                if "/" in s:
                    parts = s.split("/", 1)
                    current_dir = parts[0]
                    actual_slug = parts[1]
                else:
                    current_dir = dir_name
                    actual_slug = s

                # Try direct slug, then with common suffixes
                options = [actual_slug, f"{actual_slug}_algorithm", f"{actual_slug}_implementation"]
                for opt in options:
                    md_path = os.path.join("..", current_dir, f"{opt}.md")
                    py_path = os.path.join("..", current_dir, f"{opt}.py")
                    
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

    # Save aggregated data as JS for browser usage
    output_js = "dsa_book_data.js"
    with open(output_js, 'w', encoding='utf-8') as f:
        f.write("const SOURCE_DATA = ")
        json.dump(book_data, f, indent=2)
        f.write(";")
    
    # Save aggregated data as JSON for reference
    output_json = "dsa_book_data.json"
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(book_data, f, indent=2)
        
    print(f"Successfully generated {output_js} and {output_json}")

if __name__ == "__main__":
    main()
