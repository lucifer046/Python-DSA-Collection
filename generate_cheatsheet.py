import json
from fpdf import FPDF

class DSACheatsheetPDF(FPDF):
    def header(self):
        pass

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 9)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def chapter_title(self, label):
        self.ln(4)
        self.set_font('helvetica', 'B', 18)
        self.set_fill_color(245, 245, 245) # Very light gray background
        self.set_text_color(26, 35, 126) # Deep Blue
        self.cell(0, 12, f'  {label.upper()}', ln=True, fill=True)
        self.ln(6)

    def draw_row(self, label, content):
        self.set_x(12)
        # Bold label in Deep Blue for clear hierarchy
        self.set_font('helvetica', 'B', 10)
        self.set_text_color(26, 35, 126)
        self.cell(45, 8, label, ln=0)
        
        # Soft Body Text with better line spacing (h=8)
        self.set_font('helvetica', '', 11)
        self.set_text_color(44, 44, 44) # Near black
        self.multi_cell(0, 8, content)
        self.ln(2) # Space between rows

    def algorithm_section(self, algo):
        # Algorithm Name with bottom border
        self.set_font('helvetica', 'B', 15)
        self.set_text_color(0, 0, 0)
        self.cell(0, 10, f" {algo['name']}", ln=True)
        self.set_draw_color(200, 200, 200)
        self.line(12, self.get_y(), 198, self.get_y())
        self.ln(4)
        
        # Section Content
        self.draw_row('Key Concept:', algo['designed_for'])
        if 'purpose' in algo:
            self.draw_row('Practical Use:', algo['purpose'])
        self.draw_row('Mechanism:', algo['how_it_works'])
        
        # Pros & Cons Section
        self.ln(4)
        start_y = self.get_y()
        self.set_font('helvetica', 'B', 10)
        self.set_text_color(27, 94, 32) # Dark Forest Green
        self.cell(90, 8, '  (+) STRENGTHS / PROS', ln=0)
        self.set_x(105)
        self.set_text_color(183, 28, 28) # Dark Red
        self.cell(90, 8, '  (-) WEAKNESSES / CONS', ln=1)
        
        self.set_font('helvetica', '', 10)
        self.set_text_color(60, 60, 60)
        pros_text = "* " + "\n* ".join(algo['pros'])
        cons_text = "* " + "\n* ".join(algo['cons'])
        
        text_y = self.get_y()
        self.multi_cell(90, 7, pros_text) # Soft line spacing for list
        end_y_pros = self.get_y()
        
        self.set_xy(105, text_y)
        self.multi_cell(90, 7, cons_text)
        end_y_cons = self.get_y()
        
        self.set_y(max(end_y_pros, end_y_cons) + 6)
        
        # Complexity Grid (Clean Style)
        self.set_fill_color(252, 252, 252)
        self.set_font('helvetica', 'B', 10)
        self.set_text_color(0, 0, 0)
        self.cell(30, 10, 'Scenario', border='B', fill=True, align='C')
        self.cell(30, 10, 'Complexity', border='B', fill=True, align='C')
        self.cell(0, 10, 'Why / Logic?', border='B', fill=True, align='C')
        self.ln()
        
        self.set_font('helvetica', '', 10)
        cases = [
            ('Best Case', algo['complexities']['best']),
            ('Avg Case', algo['complexities']['avg']),
            ('Worst Case', algo['complexities']['worst']),
            ('Space Use', {'time': algo['complexities']['space'], 'note': 'Auxiliary memory'})
        ]
        
        for name, data in cases:
            self.set_font('helvetica', 'B', 10)
            self.cell(30, 9, name, border='B', align='C')
            self.set_text_color(26, 35, 126)
            self.cell(30, 9, data['time'], border='B', align='C')
            self.set_text_color(60, 60, 60)
            self.set_font('helvetica', '', 9)
            self.cell(0, 9, f" {data['note']}", border='B')
            self.ln()
            
        self.ln(12) # Major gap between algorithms

def generate():
    with open('dsa_cheatsheet_data.json', 'r') as f:
        data = json.load(f)
        
    pdf = DSACheatsheetPDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()
    
    # Header (First page only)
    pdf.set_fill_color(105, 105, 105) # Grey
    pdf.rect(0, 0, 210, 35, 'F')
    
    pdf.set_y(12)
    pdf.set_font('helvetica', 'B', 26)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 10, 'PYTHON DSA CHEATSHEET', ln=True, align='C')
    pdf.ln(10)
    
    # Notation Key - Wrapped in a subtle box
    pdf.set_fill_color(240, 244, 255) # Soft blueprint blue
    pdf.rect(10, pdf.get_y(), 190, 48, 'F')
    pdf.set_y(pdf.get_y() + 4)
    pdf.set_font('helvetica', 'B', 12)
    pdf.set_text_color(26, 35, 126)
    pdf.cell(0, 8, '   NOTATION KEY (QUICK REFERENCE):', ln=True)
    pdf.ln(2)
    
    legend = [
        ("n", "Total elements in the collection."),
        ("V / E", "Vertices and Edges in a graph/tree network."),
        ("h", "Height of the tree (governs search depth)."),
        ("log n", "Complexity halves on every step (very fast).")
    ]
    for char, desc in legend:
        pdf.set_font('helvetica', 'B', 10)
        pdf.set_x(15)
        pdf.cell(20, 6, f"{char}:", ln=0)
        pdf.set_font('helvetica', '', 10)
        pdf.set_text_color(44, 44, 44)
        pdf.cell(0, 6, desc, ln=True)
    pdf.ln(10)
    
    first_category = True
    for category in data:
        if not first_category:
            pdf.add_page()
        first_category = False
        
        pdf.chapter_title(category['category'])
        for topic in category['topics']:
            if pdf.get_y() > 190: # Careful page break calculation
                pdf.add_page()
            pdf.algorithm_section(topic)
            
    pdf.output('DSA_Cheatsheet.pdf')
    print("Premium PDF generated successfully.")

if __name__ == "__main__":
    generate()
