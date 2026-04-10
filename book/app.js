let bookData = [];
let currentCodeElement = null;

const XRAY_DICTIONARY = {
    'pivot': 'The element chosen to partition the array',
    'p': 'Pivot element chosen for partitioning',
    'mid': 'The middle index used to divide the list',
    'm': 'Middle index/element',
    'low': 'Starting index of the current partition',
    'high': 'Ending index of the current partition',
    'n': 'Total number of elements / vertices',
    'pq': 'Priority Queue (Min-Heap) for greedy selection',
    'd': 'Distance array/map storing shortest paths',
    'G': 'Graph representation (Adjacency List/Matrix)',
    'L': 'Input List / Left sublist',
    'R': 'Right sublist',
    'res': 'Resulting merged/sorted list'
};

function switchView(view) {
    const layout = document.getElementById('book-layout');
    const theoryBtn = document.getElementById('show-theory');
    const codeBtn = document.getElementById('show-code');
    
    if (view === 'theory') {
        layout.classList.add('show-theory');
        layout.classList.remove('show-code');
        theoryBtn.classList.add('active');
        codeBtn.classList.remove('active');
    } else {
        layout.classList.add('show-code');
        layout.classList.remove('show-theory');
        codeBtn.classList.add('active');
        theoryBtn.classList.remove('active');
    }
}

async function init() {
    console.log("Initializing App...");
    try {
        if (typeof lucide !== 'undefined') {
            lucide.createIcons();
            console.log("Icons created.");
        } else {
            console.warn("Lucide library not loaded.");
        }
        
        if (typeof SOURCE_DATA !== 'undefined') {
            bookData = SOURCE_DATA;
            console.log("Data loaded from SOURCE_DATA.");
        } else {
            console.warn("SOURCE_DATA not found. Trying fetch...");
            const response = await fetch('book/dsa_book_data.json');
            bookData = await response.json();
        }
        
        renderMenu();
        
        // Close sidebar when clicking on the overlay backdrop
        document.getElementById('sidebar-overlay').addEventListener('click', function(e) {
            if (e.target === this) {
                this.classList.remove('active');
            }
        });
        
        console.log("All data pre-loaded for offline access.");
        
        // Default to Home View
        loadHome();
        
        // Initialize mobile view classes
        const layout = document.getElementById('book-layout');
        if (!layout.classList.contains('show-theory') && !layout.classList.contains('show-code')) {
            layout.classList.add('show-theory');
        }
    } catch (error) {
        console.error('Initialization Error:', error);
    }
}

function toggleMenu() {
    const overlay = document.getElementById('sidebar-overlay');
    overlay.classList.toggle('active');
}

function renderMenu(activeCat = null, activeTop = null) {
    const list = document.getElementById('menu-content');
    let html = `
        <div class="menu-item home-btn ${activeCat === null ? 'active' : ''}" onclick="loadHome()">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
            <span>Home</span>
        </div>
        <div class="menu-item home-btn" onclick="window.open('DSA_Cheatsheet.pdf', '_blank')">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
            <span>Cheat Sheet PDF</span>
        </div>
    `;

    bookData.forEach((category, catIndex) => {
        html += `
            <div class="menu-category">
                <div class="menu-category-title">${category.category}</div>
                <div class="menu-grid">
        `;
        category.topics.forEach((topic, topIndex) => {
            const isActive = catIndex === activeCat && topIndex === activeTop;
            html += `
                <div class="menu-item ${isActive ? 'active' : ''}" onclick="loadPage(${catIndex}, ${topIndex})">
                    ${topic.name}
                </div>
            `;
        });
        html += `</div></div>`;
    });

    html += `
        <div class="menu-footer">
            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
            Created by <span>Divya Prakash</span>
        </div>
    `;

    list.innerHTML = html;
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }
}

function getComplexityStyle(time) {
    if (!time) return 'average';
    const t = time.toLowerCase();
    if (t.includes('1') || t.includes('log n')) return 'excellent';
    if (t.includes('n^2') || t.includes('n^3') || t.includes('v^3') || t.includes('v * e')) return 'poor';
    return 'average';
}

function loadHome() {
    const layout = document.getElementById('book-layout');
    const overlay = document.getElementById('sidebar-overlay');
    
    overlay.classList.remove('active');
    renderMenu(null, null);
    
    layout.style.pointerEvents = 'none';
    layout.classList.remove('loaded');
    
    setTimeout(() => {
        renderHomeContent();
        layout.classList.add('loaded');
        document.querySelector('.theory-pane').scrollTop = 0;
        document.querySelector('.code-box').scrollTop = 0;
        layout.style.pointerEvents = 'all';
    }, 400);
}

function renderHomeContent() {
    const theoryContainer = document.getElementById('theory-content-area');
    const codeContainer = document.getElementById('code-container');
    
    theoryContainer.innerHTML = `
        <div class="home-canvas-container" style="position:relative; width: 100%; height: 75vh; display: flex; align-items: center; justify-content: center; overflow: hidden; border-radius: 1.5rem; background: var(--bg-surface); border: 1px solid var(--border-light); box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
            <canvas id="dsa-home-canvas" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0.6;"></canvas>
            <div style="position: relative; z-index: 10; text-align: center; background: rgba(255,255,255,0.7); padding: 3rem 4rem; border-radius: 1.5rem; border: 1px solid rgba(255,255,255,0.5); backdrop-filter: blur(12px); box-shadow: 0 20px 50px rgba(30,90,143,0.1);">
                <i data-lucide="network" width="48" height="48" style="color: var(--accent-primary); margin-bottom: 1rem;"></i>
                <h1 style="font-size: 2.8rem; font-weight: 800; color: #111; margin-bottom: 0.5rem; letter-spacing: -0.02em;">DSA HANDBOOK</h1>
                <p style="font-size: 0.95rem; color: var(--text-muted); font-family: 'Fira Code', monospace; letter-spacing: 0.05em; margin-bottom: 2rem;">
                    [ ALGORITHMS & DATA STRUCTURES <span style="color: var(--accent-primary); font-weight: 600;">USING PYTHON</span> ]
                </p>
                <button onclick="toggleMenu()" style="background: #111; color: white; border: none; padding: 1rem 2.5rem; font-size: 1rem; font-weight: 600; border-radius: 2rem; cursor: pointer; transition: all 0.3s; box-shadow: 0 5px 15px rgba(0,0,0,0.2);">Explore Topics</button>
            </div>
        </div>
    `;
    
    codeContainer.innerHTML = `
        <div class="code-placeholder-view" style="height: 100%; display: flex; align-items: center; justify-content: center; flex-direction: column;">
            <i data-lucide="binary" width="48" height="48" style="margin-bottom: 1.5rem; opacity: 0.3; color: white;"></i>
            <h3 style="font-size: 1.25rem; font-family: 'Fira Code', monospace; color: rgba(255,255,255,0.4); font-weight: 400;">// Waiting for input...</h3>
        </div>
    `;
    
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }
    
    setTimeout(() => { initDSACanvas(); }, 100);
}

// Canvas Data Structures Animation Engine
function initDSACanvas() {
    const canvas = document.getElementById('dsa-home-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let width = canvas.width = canvas.parentElement.clientWidth;
    let height = canvas.height = canvas.parentElement.clientHeight;

    const nodes = [];
    const numNodes = 60;
    const colors = ['#1e5a8f', '#4a6a8a', '#a6b8c7']; // Slate palette

    class Node {
        constructor() {
            this.x = Math.random() * width;
            this.y = Math.random() * height;
            this.vx = (Math.random() - 0.5) * 1.5;
            this.vy = (Math.random() - 0.5) * 1.5;
            this.radius = Math.random() * 4 + 2;
            this.type = Math.random() > 0.7 ? 'square' : 'circle';
            this.color = colors[Math.floor(Math.random() * colors.length)];
        }
        update() {
            this.x += this.vx;
            this.y += this.vy;
            if (this.x < 0 || this.x > width) this.vx *= -1;
            if (this.y < 0 || this.y > height) this.vy *= -1;
        }
        draw() {
            ctx.fillStyle = this.color;
            ctx.beginPath();
            if (this.type === 'square') {
                ctx.rect(this.x - this.radius, this.y - this.radius, this.radius * 2, this.radius * 2);
            } else {
                ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
            }
            ctx.fill();
        }
    }

    for (let i = 0; i < numNodes; i++) nodes.push(new Node());

    function animate() {
        if (!document.getElementById('dsa-home-canvas')) return; // Stop if unmounted
        ctx.clearRect(0, 0, width, height);

        for (let i = 0; i < nodes.length; i++) {
            nodes[i].update();
            nodes[i].draw();
            
            // Connect close nodes to form graph structures
            for (let j = i + 1; j < nodes.length; j++) {
                const dx = nodes[i].x - nodes[j].x;
                const dy = nodes[i].y - nodes[j].y;
                const dist = Math.sqrt(dx * dx + dy * dy);
                
                if (dist < 120) {
                    ctx.beginPath();
                    ctx.strokeStyle = `rgba(30, 90, 143, ${1 - dist / 120})`;
                    ctx.lineWidth = 1;
                    ctx.moveTo(nodes[i].x, nodes[i].y);
                    ctx.lineTo(nodes[j].x, nodes[j].y);
                    ctx.stroke();
                }
            }
        }
        requestAnimationFrame(animate);
    }
    
    animate();
    
    window.addEventListener('resize', () => {
        if (!document.getElementById('dsa-home-canvas')) return;
        width = canvas.width = canvas.parentElement.clientWidth;
        height = canvas.height = canvas.parentElement.clientHeight;
    }, { once: true });
}

function loadPage(catIndex, topIndex) {
    const topic = bookData[catIndex].topics[topIndex];
    const layout = document.getElementById('book-layout');
    
    // Close menu
    document.getElementById('sidebar-overlay').classList.remove('active');
    
    // Update active state in menu
    renderMenu(catIndex, topIndex);
    
    // Show Loading state
    layout.style.pointerEvents = 'none';
    layout.classList.remove('loaded');
    
    setTimeout(() => {
        renderContent(topic);
        layout.classList.add('loaded');
        applyXRay();
        if (window.MathJax) {
            window.MathJax.typesetPromise();
        }
        document.querySelector('.theory-pane').scrollTop = 0;
        document.querySelector('.code-box').scrollTop = 0;
        layout.style.pointerEvents = 'all';
    }, 400); // 400ms flash to give it that fresh-load feeling
}

function renderContent(topic) {
    // Render Theory
    const theoryContainer = document.getElementById('theory-content-area');
    const comps = topic.complexities || { best:{time:'N/A'}, avg:{time:'N/A'}, worst:{time:'N/A'}, space:'N/A' };
    
    const complexityHtml = `
        <div class="complexity-dashboard">
            <div class="comp-pill"><span class="comp-label">Best</span><span class="comp-value ${getComplexityStyle(comps.best.time)}">${comps.best.time}</span></div>
            <div class="comp-pill"><span class="comp-label">Average</span><span class="comp-value ${getComplexityStyle(comps.avg.time)}">${comps.avg.time}</span></div>
            <div class="comp-pill"><span class="comp-label">Worst</span><span class="comp-value ${getComplexityStyle(comps.worst.time)}">${comps.worst.time}</span></div>
            <div class="comp-pill"><span class="comp-label">Space</span><span class="comp-value ${getComplexityStyle(comps.space)}">${comps.space}</span></div>
        </div>
    `;

    let theory = topic.theory || '*Theory content placeholder*';
    
    // Fix image paths for GitHub Pages sub-directories
    // Ensure they always resolve relative to the root index.html
    theory = theory.replace(/docs\/images\//g, './docs/images/');

    theoryContainer.innerHTML = `
        <div class="theory-header">
            <h1 class="theory-title">${topic.name}</h1>
            ${complexityHtml}
        </div>
        <div class="theory-content">
            ${marked.parse(theory)}
        </div>
    `;

    // Render Code
    const codeContainer = document.getElementById('code-container');
    const escapedCode = escapeHtml(topic.code || '# Code implementation soon');
    codeContainer.innerHTML = `<code class="language-python">${escapedCode}</code>`;
    
    // Trigger Prism Highlight
    Prism.highlightElement(codeContainer.querySelector('code'));
}

function applyXRay() {
    const codeEl = document.querySelector('code.language-python');
    if (!codeEl) return;
    
    let html = codeEl.innerHTML;
    
    // Reverse sort dictionary keys by length to avoid partial matches
    const keys = Object.keys(XRAY_DICTIONARY).sort((a,b) => b.length - a.length);
    
    keys.forEach(key => {
        // Match whole words only, avoiding inside HTML tags by using a lookahead
        const regex = new RegExp(`\\\\b(${key})\\\\b(?![^<]*>)`, 'g');
        const tooltip = XRAY_DICTIONARY[key];
        html = html.replace(regex, `<span class="xray-var" data-tooltip="${tooltip}">$1</span>`);
    });
    
    codeEl.innerHTML = html;
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

document.addEventListener('DOMContentLoaded', init);
