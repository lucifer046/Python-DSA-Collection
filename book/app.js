// =========================================
//  DSA HANDBOOK — App Logic v2.0
//  Features: Command Palette, Keyboard Nav,
//  Progress Tracking, Smooth Transitions,
//  Mobile Swipe Gestures
// =========================================

let bookData = [];
let currentCodeElement = null;

// Track current page position [catIndex, topIndex]
let currentCat = null;
let currentTop = null;

// Flat list of all topics for prev/next navigation
let flatTopics = []; // [{catIndex, topIndex, name, category}]

// ---- Progress Storage ----
const PROGRESS_KEY = 'dsa_handbook_progress';

function getProgress() {
    try {
        return JSON.parse(localStorage.getItem(PROGRESS_KEY)) || {};
    } catch { return {}; }
}

function setProgress(data) {
    localStorage.setItem(PROGRESS_KEY, JSON.stringify(data));
}

function isCompleted(catIndex, topIndex) {
    return !!getProgress()[`${catIndex}_${topIndex}`];
}

function toggleCompleted(catIndex, topIndex) {
    const progress = getProgress();
    const key = `${catIndex}_${topIndex}`;
    if (progress[key]) {
        delete progress[key];
    } else {
        progress[key] = true;
    }
    setProgress(progress);
    return !!progress[key];
}

// ---- Toast ----
let toastTimer = null;
function showToast(msg, icon = '✓') {
    const el = document.getElementById('app-toast');
    if (!el) return;
    el.innerHTML = `<span>${icon}</span> ${msg}`;
    el.classList.add('visible');
    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(() => el.classList.remove('visible'), 2500);
}

// =========================================
//  X-RAY DICTIONARY
// =========================================
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

// =========================================
//  VIEW SWITCHER (Theory / Code tabs)
// =========================================
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

// =========================================
//  INIT
// =========================================
async function init() {
    console.log("Initializing App...");
    try {
        if (typeof lucide !== 'undefined') {
            lucide.createIcons();
        }

        if (typeof SOURCE_DATA !== 'undefined') {
            bookData = SOURCE_DATA;
        } else {
            const response = await fetch('book/dsa_book_data.json');
            bookData = await response.json();
        }

        // Build flat topic list for navigation
        buildFlatTopics();

        renderMenu();

        // Close sidebar on overlay backdrop click
        document.getElementById('sidebar-overlay').addEventListener('click', function (e) {
            if (e.target === this) this.classList.remove('active');
        });

        // Default: Home
        loadHome();

        const layout = document.getElementById('book-layout');
        if (!layout.classList.contains('show-theory') && !layout.classList.contains('show-code')) {
            layout.classList.add('show-theory');
        }

        // Setup all interaction systems
        setupKeyboardShortcuts();
        setupCmdPalette();
        setupSwipeGestures();

    } catch (error) {
        console.error('Initialization Error:', error);
    }
}

// =========================================
//  FLAT TOPIC INDEX (for Prev/Next nav)
// =========================================
function buildFlatTopics() {
    flatTopics = [];
    bookData.forEach((category, catIndex) => {
        category.topics.forEach((topic, topIndex) => {
            flatTopics.push({ catIndex, topIndex, name: topic.name, category: category.category });
        });
    });
}

function getCurrentFlatIndex() {
    if (currentCat === null || currentTop === null) return -1;
    return flatTopics.findIndex(t => t.catIndex === currentCat && t.topIndex === currentTop);
}

// =========================================
//  MENU / SIDEBAR
// =========================================
function toggleMenu() {
    const overlay = document.getElementById('sidebar-overlay');
    overlay.classList.toggle('active');
}

function renderMenu(activeCat = null, activeTop = null) {
    const list = document.getElementById('menu-content');
    const progress = getProgress();

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
        const total = category.topics.length;
        const done = category.topics.filter((_, i) => progress[`${catIndex}_${i}`]).length;
        const pct = total > 0 ? done / total : 0;
        const radius = 8;
        const circumference = 2 * Math.PI * radius;
        const dashOffset = circumference * (1 - pct);
        const ringColor = pct === 1 ? '#27ae60' : '#1e5a8f';

        html += `
            <div class="menu-category">
                <div class="menu-category-title">
                    <span>${category.category}</span>
                    <svg class="category-progress-ring" viewBox="0 0 22 22" xmlns="http://www.w3.org/2000/svg" title="${done}/${total} completed">
                        <circle cx="11" cy="11" r="${radius}" fill="none" stroke="rgba(30,90,143,0.15)" stroke-width="2.2"/>
                        <circle cx="11" cy="11" r="${radius}" fill="none" stroke="${ringColor}" stroke-width="2.2"
                            stroke-dasharray="${circumference.toFixed(2)}"
                            stroke-dashoffset="${dashOffset.toFixed(2)}"
                            stroke-linecap="round"
                            transform="rotate(-90 11 11)"
                            style="transition: stroke-dashoffset 0.6s cubic-bezier(0.25,1,0.5,1);"/>
                    </svg>
                </div>
                <div class="menu-grid">
        `;

        category.topics.forEach((topic, topIndex) => {
            const isActive = catIndex === activeCat && topIndex === activeTop;
            const done = progress[`${catIndex}_${topIndex}`];
            html += `
                <div class="menu-item ${isActive ? 'active' : ''} ${done ? 'completed' : ''}" onclick="loadPage(${catIndex}, ${topIndex})">
                    <span style="flex:1;">${topic.name}</span>
                    <div class="progress-check" title="${done ? 'Completed ✓' : 'Not yet completed'}"></div>
                </div>
            `;
        });

        html += `</div></div>`;
    });

    html += `
        <div class="menu-footer">
            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
            Handbook by <span>Divya Prakash</span>
        </div>
    `;

    list.innerHTML = html;
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }
}

// =========================================
//  HOME
// =========================================
function loadHome() {
    const layout = document.getElementById('book-layout');
    const overlay = document.getElementById('sidebar-overlay');

    currentCat = null;
    currentTop = null;

    overlay.classList.remove('active');
    renderMenu(null, null);

    layout.style.pointerEvents = 'none';
    layout.classList.remove('loaded');
    layout.classList.remove('full-focus');

    setTimeout(() => {
        renderHomeContent();
        layout.classList.add('loaded');
        document.querySelector('.theory-pane').scrollTop = 0;
        document.querySelector('.code-box').scrollTop = 0;
        layout.style.pointerEvents = 'all';
    }, 200);
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
                    [ ALGORITHMS &amp; DATA STRUCTURES <span style="color: var(--accent-primary); font-weight: 600;">USING PYTHON</span> ]
                </p>
                <div style="display:flex; gap:0.75rem; justify-content:center; flex-wrap:wrap;">
                    <button onclick="toggleMenu()" style="background: #111; color: white; border: none; padding: 1rem 2.5rem; font-size: 1rem; font-weight: 600; border-radius: 2rem; cursor: pointer; transition: all 0.3s; box-shadow: 0 5px 15px rgba(0,0,0,0.2);">Explore Topics</button>
                    <button onclick="openCmdPalette()" style="background: rgba(30,90,143,0.08); color: var(--accent-primary); border: 2px solid var(--border-highlight); padding: 1rem 1.75rem; font-size: 1rem; font-weight: 600; border-radius: 2rem; cursor: pointer; transition: all 0.3s; display:flex; align-items:center; gap:0.5rem;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                        Quick Search
                        <kbd style="font-family:'Fira Code',monospace;font-size:0.7rem;background:rgba(30,90,143,0.12);color:var(--accent-primary);border:1px solid var(--border-highlight);border-radius:4px;padding:0.15rem 0.4rem;">Ctrl K</kbd>
                    </button>
                </div>
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

// =========================================
//  CANVAS ANIMATION
// =========================================
function initDSACanvas() {
    const canvas = document.getElementById('dsa-home-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let width = canvas.width = canvas.parentElement.clientWidth;
    let height = canvas.height = canvas.parentElement.clientHeight;

    const nodes = [];
    const numNodes = 60;
    const colors = ['#1e5a8f', '#4a6a8a', '#a6b8c7'];

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
        if (!document.getElementById('dsa-home-canvas')) return;
        ctx.clearRect(0, 0, width, height);

        for (let i = 0; i < nodes.length; i++) {
            nodes[i].update();
            nodes[i].draw();
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

// =========================================
//  LOAD PAGE — with smooth transition
// =========================================
function loadPage(catIndex, topIndex) {
    const topic = bookData[catIndex].topics[topIndex];
    const layout = document.getElementById('book-layout');

    // Update current position
    currentCat = catIndex;
    currentTop = topIndex;

    // Close menu
    document.getElementById('sidebar-overlay').classList.remove('active');

    // Update active state in menu
    renderMenu(catIndex, topIndex);

    // Smooth fade-out, then render, then fade-in
    layout.style.pointerEvents = 'none';
    layout.classList.remove('loaded');

    setTimeout(() => {
        renderContent(topic, catIndex, topIndex);

        if (!topic.code || topic.code.trim() === '' || topic.code.includes('Code implementation soon')) {
            layout.classList.add('full-focus');
        } else {
            layout.classList.remove('full-focus');
        }

        layout.classList.add('loaded');
        applyXRay();

        if (typeof lucide !== 'undefined') {
            lucide.createIcons();
        }
        if (window.MathJax) {
            window.MathJax.typesetPromise();
        }

        document.querySelector('.theory-pane').scrollTop = 0;
        document.querySelector('.code-box').scrollTop = 0;
        layout.style.pointerEvents = 'all';

        // Reset to Theory view on mobile
        switchView('theory');
    }, 200);
}

// =========================================
//  RENDER CONTENT
// =========================================
function renderContent(topic, catIndex, topIndex) {
    const theoryContainer = document.getElementById('theory-content-area');
    const isDone = isCompleted(catIndex, topIndex);

    // Build complexity pills
    let complexityHtml = '';
    if (topic.complexities) {
        const comps = topic.complexities;
        
        const getVal = (obj) => {
            if (!obj) return '--';
            return typeof obj === 'object' ? (obj.time || '--') : obj;
        };

        complexityHtml = `
            <div class="complexity-dashboard">
                <div class="comp-pill"><span class="comp-label">Best</span><span class="comp-value best-val">${getVal(comps.best)}</span></div>
                <div class="comp-pill"><span class="comp-label">Average</span><span class="comp-value avg-val">${getVal(comps.avg)}</span></div>
                <div class="comp-pill"><span class="comp-label">Worst</span><span class="comp-value worst-val">${getVal(comps.worst)}</span></div>
                <div class="comp-pill"><span class="comp-label">Space</span><span class="comp-value space-val">${getVal(comps.space)}</span></div>
            </div>
        `;
    }

    let theory = topic.theory || '*Theory content placeholder*';
    theory = theory.replace(/docs\/images\//g, './docs/images/');

    // Process GitHub-style alert callouts
    const alertRegex = /^>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*([\s\S]*?)(?=\n\n|\n[^>]|$)/gm;
    theory = theory.replace(alertRegex, (match, type, content) => {
        const iconMap = { 'NOTE': 'info', 'TIP': 'lightbulb', 'IMPORTANT': 'alert-circle', 'WARNING': 'alert-triangle', 'CAUTION': 'zap' };
        const cleanedContent = content.replace(/^>\s?/gm, '').trim();
        return `<div class="callout callout-${type.toLowerCase()}">
            <div class="callout-title"><i data-lucide="${iconMap[type]}"></i>${type}</div>
            <div class="theory-content-inner">${marked.parse(cleanedContent)}</div>
        </div>`;
    });

    // Build prev/next nav
    const flatIdx = flatTopics.findIndex(t => t.catIndex === catIndex && t.topIndex === topIndex);
    const prev = flatIdx > 0 ? flatTopics[flatIdx - 1] : null;
    const next = flatIdx < flatTopics.length - 1 ? flatTopics[flatIdx + 1] : null;

    const navHtml = `
        <div style="display:flex; justify-content:space-between; gap:1rem; margin-top:0.5rem; margin-bottom:2rem;">
            ${prev ? `<button onclick="loadPage(${prev.catIndex},${prev.topIndex})" style="display:flex;align-items:center;gap:0.5rem;background:transparent;border:1px solid var(--border-light);padding:0.5rem 1rem;border-radius:0.65rem;cursor:pointer;color:var(--text-muted);font-size:0.85rem;font-family:'Inter',sans-serif;transition:all 0.2s;" onmouseover="this.style.borderColor='var(--accent-primary)';this.style.color='var(--accent-primary)';" onmouseout="this.style.borderColor='var(--border-light)';this.style.color='var(--text-muted)';">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>
                <span>${prev.name}</span>
            </button>` : '<div></div>'}
            ${next ? `<button onclick="loadPage(${next.catIndex},${next.topIndex})" style="display:flex;align-items:center;gap:0.5rem;background:transparent;border:1px solid var(--border-light);padding:0.5rem 1rem;border-radius:0.65rem;cursor:pointer;color:var(--text-muted);font-size:0.85rem;font-family:'Inter',sans-serif;transition:all 0.2s;margin-left:auto;" onmouseover="this.style.borderColor='var(--accent-primary)';this.style.color='var(--accent-primary)';" onmouseout="this.style.borderColor='var(--border-light)';this.style.color='var(--text-muted)';">
                <span>${next.name}</span>
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg>
            </button>` : '<div></div>'}
        </div>
    `;

    // Mark as completed widget
    const markHtml = `
        <div class="mark-complete-wrap">
            <button class="mark-complete-btn ${isDone ? 'is-done' : ''}" id="mark-complete-btn" onclick="handleMarkComplete(${catIndex}, ${topIndex})">
                <div class="btn-icon-circle"></div>
                <span>${isDone ? 'Completed ✓' : 'Mark as Understood'}</span>
            </button>
            <span class="mark-complete-hint">Saves your progress locally</span>
        </div>
    `;

    theoryContainer.innerHTML = `
        ${navHtml}
        <div class="theory-header">
            <h1 class="theory-title">${topic.name}</h1>
            ${complexityHtml}
        </div>
        <div class="theory-content">
            ${marked.parse(theory)}
        </div>
        ${markHtml}
    `;

    // Render Code
    const codeContainer = document.getElementById('code-container');
    const escapedCode = escapeHtml(topic.code || '# Code implementation soon');
    codeContainer.innerHTML = `<code class="language-python">${escapedCode}</code>`;
    Prism.highlightElement(codeContainer.querySelector('code'));
}

// =========================================
//  MARK AS COMPLETED
// =========================================
function handleMarkComplete(catIndex, topIndex) {
    const isDone = toggleCompleted(catIndex, topIndex);
    const btn = document.getElementById('mark-complete-btn');
    if (btn) {
        btn.classList.toggle('is-done', isDone);
        btn.querySelector('span').textContent = isDone ? 'Completed ✓' : 'Mark as Understood';
    }
    // Update sidebar rings + checkmarks
    renderMenu(catIndex, topIndex);
    showToast(isDone ? 'Marked as understood! 🎉' : 'Progress removed.', isDone ? '🎓' : '↩');
}

// =========================================
//  X-RAY
// =========================================
function applyXRay() {
    const codeEl = document.querySelector('code.language-python');
    if (!codeEl) return;

    const keys = Object.keys(XRAY_DICTIONARY).sort((a, b) => b.length - a.length);
    if (keys.length === 0) return;

    // Build a single regex to match all keys in one pass (efficient and safe)
    const pattern = keys.map(k => k.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|');
    const regex = new RegExp(`\\b(${pattern})\\b`, 'g');

    // Create a TreeWalker to find all text nodes
    const walker = document.createTreeWalker(codeEl, NodeFilter.SHOW_TEXT, null, false);
    const nodesToProcess = [];
    
    let node;
    while (node = walker.nextNode()) {
        // Skip text nodes inside comments or strings (docstrings)
        let parent = node.parentElement;
        let shouldSkip = false;
        while (parent && parent !== codeEl) {
            const list = parent.classList;
            // Robust check for PrismJS tokens and typical comment/string classes
            if (list.contains('comment') || 
                list.contains('string') || 
                list.contains('docstring') ||
                (list.contains('token') && (list.contains('comment') || list.contains('string')))) {
                shouldSkip = true;
                break;
            }
            parent = parent.parentElement;
        }
        if (!shouldSkip) {
            nodesToProcess.push(node);
        }
    }

    // Process the collected nodes
    nodesToProcess.forEach(textNode => {
        const originalText = textNode.textContent;
        const escapedText = escapeHtml(originalText);
        
        const newHtml = escapedText.replace(regex, (match) => {
            const tooltip = XRAY_DICTIONARY[match] || XRAY_DICTIONARY[match.toLowerCase()];
            return `<span class="xray-var" data-tooltip="${tooltip}">${match}</span>`;
        });

        if (newHtml !== escapedText) {
            const fragment = document.createRange().createContextualFragment(newHtml);
            textNode.parentNode.replaceChild(fragment, textNode);
        }
    });
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// =========================================
//  CODE ACTIONS (zoom + copy)
// =========================================
let currentZoom = 0.9;

function setupCodeActions() {
    const zoomInBtn = document.getElementById('zoom-in-btn');
    const zoomOutBtn = document.getElementById('zoom-out-btn');
    const copyBtn = document.getElementById('copy-code-btn');
    const codeContainer = document.getElementById('code-container');

    if (zoomInBtn) {
        zoomInBtn.addEventListener('click', () => {
            currentZoom = Math.min(currentZoom + 0.1, 1.8);
            codeContainer.style.setProperty('font-size', `${currentZoom}rem`, 'important');
            updateZoomLevelDisplay();
        });
    }

    if (zoomOutBtn) {
        zoomOutBtn.addEventListener('click', () => {
            currentZoom = Math.max(currentZoom - 0.1, 0.5);
            codeContainer.style.setProperty('font-size', `${currentZoom}rem`, 'important');
            updateZoomLevelDisplay();
        });
    }

    function updateZoomLevelDisplay() {
        const zoomLevelDisplay = document.getElementById('zoom-level');
        if (zoomLevelDisplay) {
            const percentage = Math.round((currentZoom / 0.9) * 100);
            zoomLevelDisplay.textContent = `${percentage}%`;
        }
    }

    if (copyBtn) {
        copyBtn.addEventListener('click', () => triggerCopy());
    }
}

function triggerCopy() {
    const codeContainer = document.getElementById('code-container');
    const copyBtn = document.getElementById('copy-code-btn');
    const codeEl = codeContainer ? (codeContainer.querySelector('code') || codeContainer) : null;
    if (!codeEl) return;

    navigator.clipboard.writeText(codeEl.innerText).then(() => {
        showToast('Code copied to clipboard!', '📋');
        if (copyBtn) {
            const iconCopy = copyBtn.querySelector('.icon-copy');
            const iconCheck = copyBtn.querySelector('.icon-check');
            if (iconCopy && iconCheck) {
                iconCopy.style.display = 'none';
                iconCheck.style.display = 'block';
                setTimeout(() => {
                    iconCopy.style.display = 'block';
                    iconCheck.style.display = 'none';
                }, 2000);
            }
        }
    }).catch(err => console.error('Copy failed:', err));
}

// =========================================
//  KEYBOARD SHORTCUTS
// =========================================
function setupKeyboardShortcuts() {
    document.addEventListener('keydown', (e) => {
        // Skip if focused in an input (except the palette itself)
        const tag = document.activeElement.tagName.toLowerCase();
        const isPaletteInput = document.activeElement.id === 'cmd-palette-input';
        const isTyping = (tag === 'input' || tag === 'textarea' || tag === 'select') && !isPaletteInput;

        // Cmd/Ctrl + K — Open Command Palette (always)
        if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
            e.preventDefault();
            openCmdPalette();
            return;
        }

        // If palette is open, let it handle its own keys
        const paletteActive = document.getElementById('cmd-palette-overlay').classList.contains('active');
        if (paletteActive) {
            handlePaletteKeydown(e);
            return;
        }

        if (isTyping) return;

        switch (e.key) {
            // Left/Right arrow — Previous/Next algorithm
            case 'ArrowLeft': {
                e.preventDefault();
                const idx = getCurrentFlatIndex();
                if (idx > 0) {
                    const t = flatTopics[idx - 1];
                    loadPage(t.catIndex, t.topIndex);
                    showToast(`← ${flatTopics[idx - 1].name}`, '🔼');
                }
                break;
            }
            case 'ArrowRight': {
                e.preventDefault();
                const idx = getCurrentFlatIndex();
                if (idx >= 0 && idx < flatTopics.length - 1) {
                    const t = flatTopics[idx + 1];
                    loadPage(t.catIndex, t.topIndex);
                    showToast(`${flatTopics[idx + 1].name} →`, '🔽');
                }
                break;
            }

            // T — Theory tab
            case 't':
            case 'T':
                switchView('theory');
                showToast('Switched to Theory', '📖');
                break;

            // C — Code tab (without Shift)
            case 'c':
                if (!e.shiftKey) {
                    switchView('code');
                    showToast('Switched to Code', '💻');
                }
                break;

            // Shift+C — Copy code
            case 'C':
                if (e.shiftKey) {
                    triggerCopy();
                }
                break;

            // Escape — close sidebar
            case 'Escape':
                document.getElementById('sidebar-overlay').classList.remove('active');
                break;
        }
    });
}

// =========================================
//  COMMAND PALETTE
// =========================================
let paletteResults = []; // flat filtered list [{catIndex, topIndex, name, category}]
let paletteFocusIndex = -1;

function openCmdPalette() {
    const overlay = document.getElementById('cmd-palette-overlay');
    const input = document.getElementById('cmd-palette-input');
    overlay.classList.add('active');
    paletteFocusIndex = -1;
    renderPaletteResults('');
    setTimeout(() => input && input.focus(), 50);
}

function closeCmdPalette() {
    document.getElementById('cmd-palette-overlay').classList.remove('active');
    document.getElementById('cmd-palette-input').value = '';
}

function handlePaletteOverlayClick(e) {
    if (e.target === document.getElementById('cmd-palette-overlay')) {
        closeCmdPalette();
    }
}

function setupCmdPalette() {
    const input = document.getElementById('cmd-palette-input');
    if (!input) return;

    input.addEventListener('input', (e) => {
        paletteFocusIndex = -1;
        renderPaletteResults(e.target.value.trim());
    });
}

function renderPaletteResults(query) {
    const resultsEl = document.getElementById('cmd-palette-results');
    const progress = getProgress();
    const lq = query.toLowerCase();

    // Filter
    paletteResults = flatTopics.filter(t =>
        !query || t.name.toLowerCase().includes(lq) || t.category.toLowerCase().includes(lq)
    );

    if (paletteResults.length === 0) {
        resultsEl.innerHTML = `<div class="cmd-palette-empty">No algorithms found for "<strong>${escapeHtml(query)}</strong>"</div>`;
        return;
    }

    // Group by category
    const groups = {};
    paletteResults.forEach(t => {
        if (!groups[t.category]) groups[t.category] = [];
        groups[t.category].push(t);
    });

    let html = '';
    let globalIdx = 0;
    Object.entries(groups).forEach(([cat, topics]) => {
        html += `<div class="cmd-result-category">${cat}</div>`;
        topics.forEach(t => {
            const done = progress[`${t.catIndex}_${t.topIndex}`];
            html += `
                <div class="cmd-result-item ${done ? 'is-done' : ''}" data-idx="${globalIdx}"
                    onclick="paletteSelectIndex(${globalIdx})"
                    onmouseenter="paletteFocusIndex = ${globalIdx}; updatePaletteFocus();">
                    <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
                    <span>${highlightMatch(t.name, query)}</span>
                    <span class="cmd-result-check">✓</span>
                </div>`;
            globalIdx++;
        });
    });

    resultsEl.innerHTML = html;
    if (paletteFocusIndex >= 0) updatePaletteFocus();
}

function highlightMatch(text, query) {
    if (!query) return escapeHtml(text);
    const escaped = escapeHtml(text);
    const escapedQuery = escapeHtml(query).replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    return escaped.replace(new RegExp(`(${escapedQuery})`, 'gi'), '<mark style="background:rgba(30,90,143,0.15);color:var(--accent-primary);border-radius:2px;padding:0 1px;">$1</mark>');
}

function paletteSelectIndex(idx) {
    if (idx < 0 || idx >= paletteResults.length) return;
    const t = paletteResults[idx];
    closeCmdPalette();
    loadPage(t.catIndex, t.topIndex);
}

function updatePaletteFocus() {
    const items = document.querySelectorAll('.cmd-result-item');
    items.forEach((el, i) => el.classList.toggle('focused', i === paletteFocusIndex));
    // Scroll into view
    const focused = items[paletteFocusIndex];
    if (focused) focused.scrollIntoView({ block: 'nearest' });
}

function handlePaletteKeydown(e) {
    switch (e.key) {
        case 'Escape':
            e.preventDefault();
            closeCmdPalette();
            break;
        case 'ArrowDown':
            e.preventDefault();
            paletteFocusIndex = Math.min(paletteFocusIndex + 1, paletteResults.length - 1);
            updatePaletteFocus();
            break;
        case 'ArrowUp':
            e.preventDefault();
            paletteFocusIndex = Math.max(paletteFocusIndex - 1, 0);
            updatePaletteFocus();
            break;
        case 'Enter':
            e.preventDefault();
            if (paletteFocusIndex >= 0) {
                paletteSelectIndex(paletteFocusIndex);
            } else if (paletteResults.length > 0) {
                paletteSelectIndex(0);
            }
            break;
    }
}

// =========================================
//  SWIPE GESTURES (Mobile Theory ↔ Code)
// =========================================
function setupSwipeGestures() {
    const layout = document.getElementById('book-layout');
    let touchStartX = 0;
    let touchStartY = 0;
    let isSwiping = false;

    layout.addEventListener('touchstart', (e) => {
        touchStartX = e.touches[0].clientX;
        touchStartY = e.touches[0].clientY;
        isSwiping = true;
    }, { passive: true });

    layout.addEventListener('touchend', (e) => {
        if (!isSwiping) return;
        isSwiping = false;

        const dx = e.changedTouches[0].clientX - touchStartX;
        const dy = e.changedTouches[0].clientY - touchStartY;

        // Only count as horizontal swipe if horizontal movement dominates
        if (Math.abs(dx) < 50 || Math.abs(dy) > Math.abs(dx) * 0.8) return;

        // Only apply on mobile (when view-switcher is visible)
        if (window.innerWidth > 1024) return;

        if (dx < 0) {
            // Swipe Left → Show Code
            switchView('code');
            showToast('Swiped to Code', '💻');
        } else {
            // Swipe Right → Show Theory
            switchView('theory');
            showToast('Swiped to Theory', '📖');
        }
    }, { passive: true });

    layout.addEventListener('touchmove', (e) => {
        const dx = e.touches[0].clientX - touchStartX;
        const dy = e.touches[0].clientY - touchStartY;
        // If scrolling vertically more than horizontally, cancel swipe detection
        if (Math.abs(dy) > Math.abs(dx)) isSwiping = false;
    }, { passive: true });
}

// =========================================
//  DOMContentLoaded
// =========================================
document.addEventListener('DOMContentLoaded', () => {
    init();
    setupCodeActions();
});
