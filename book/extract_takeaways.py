import json
import os
import re

# Mapping between JSON categories and Directory names (Copied from build_book_data.py)
CATEGORY_MAP = {
    "Sorting Algorithms": "Sorting",
    "Searching & Selection": "Searching",
    "Divide & Conquer": "Divide_and_Conquer",
    "Graph Algorithms": "Graph_Algorithms",
    "Basic Data Structures": "Data_Structures",
    "Greedy & Practical Tech": "Greedy_Algorithms",
    "Practice Sessions": "Practice_Problems"
}

def slugify(text):
    return text.lower().replace(" ", "_").replace("-", "_").replace("'", "").replace("(", "").replace(")", "").replace("/", "_")

def sanitize_text(text):
    """Replaces non-ASCII characters that cause FPDF errors."""
    replacements = {
        '—': '--',
        '–': '-',
        '’': "'",
        '‘': "'",
        '“': '"',
        '”': '"',
        '…': '...',
        '✅': '[YES]',
        '❌': '[NO]',
        '⚠️': '[ALERT]'
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    # Remove any remaining non-ASCII characters
    return text.encode('ascii', 'ignore').decode('ascii')

def extract_takeaways(content):
    """Finds the 'Key Takeaways' section and extracts bullet points."""
    # Find section starting with ## Key Takeaways
    match = re.search(r'## Key Takeaways\s+(.*)', content, re.DOTALL)
    if not match:
        return []
    
    takeaways_text = match.group(1).strip()
    # Extract lines starting with numbers or bullets
    lines = takeaways_text.split('\n')
    takeaways = []
    for line in lines:
        line = line.strip()
        if not line: continue
        # Matches "1. Text" or "* Text" or "- Text"
        point = re.sub(r'^(\d+\.|\*|\-)\s+', '', line).strip()
        if point:
            takeaways.append(sanitize_text(point))
    return takeaways

def main():
    metadata_path = "dsa_cheatsheet_data.json"
    if not os.path.exists(metadata_path):
        print(f"Error: {metadata_path} not found.")
        return

    with open(metadata_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for category_item in data:
        category_name = category_item["category"]
        dir_name = CATEGORY_MAP.get(category_name)
        if not dir_name: continue

        for topic in category_item["topics"]:
            topic_name = topic["name"]
            slug = slugify(topic_name)
            
            # Explicit Mappings (Sync with build_book_data.py)
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
                "Kruskal / Prim (MST)": ["kruskals_algorithm", "prims_algorithm"],
                "Topological Sort / Longest Path": ["topological_sort", "longest_path_dag"],
                "Stack / Queue": ["stack_implementation", "queue_implementation"],
                "Union-Find (Disjoint Set)": "union_find",
                "Binary Heap": "binary_heap_implementation",
                "Binary Tree": "binary_tree",
                "Strict Binary Tree": "strict_binary_tree",
                "Quiz 1 - Practice Problems": "Practice_Problems/Quiz_1/quiz_1_practice"
            }

            slugs = explicit_map.get(topic_name, slug)
            if isinstance(slugs, str):
                slugs = [slugs]

            all_takeaways = []
            for s in slugs:
                if "/" in s:
                    parts = s.split("/", 1)
                    current_dir = parts[0]
                    actual_slug = parts[1]
                else:
                    current_dir = dir_name
                    actual_slug = s

                options = [actual_slug, f"{actual_slug}_algorithm", f"{actual_slug}_implementation"]
                for opt in options:
                    md_path = os.path.join("..", current_dir, f"{opt}.md")
                    if os.path.exists(md_path):
                        with open(md_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        takeaways = extract_takeaways(content)
                        all_takeaways.extend(takeaways)
                        break
            
            if all_takeaways:
                topic["takeaways"] = all_takeaways
                print(f"Extracted {len(all_takeaways)} takeaways for {topic_name}")

    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print("Updated dsa_cheatsheet_data.json with takeaways.")

if __name__ == "__main__":
    main()
