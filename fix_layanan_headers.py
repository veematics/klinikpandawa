#!/usr/bin/env python3
"""
Script to fix header and navigation issues in all layanan pages
Applies the same fixes that were done to seksual-dan-reproduksi.html and eksim.html
"""

import os
import re

# List of files to fix (excluding already fixed ones)
files_to_fix = [
    'botox.html',
    'dermatitis.html', 
    'disfungsi-ereksi.html',
    'ejakulasi-dini.html',
    'infus-whitening.html',
    'keputihan.html',
    'klar-aligner.html',
    'labiaplasty.html',
    'pap-smear.html',
    'perawatan-akar-gigi.html',
    'rhinoplasty.html',
    'sifilis-diagnosis-pengobatan.html',
    'tambal-gigi.html',
    'threadlift.html',
    'vaginoplasty.html',
    'veneer.html',
    'vitiligo.html'
]

def fix_css_styles(content):
    """Fix CSS styles - remove fixed positioning and add dynamic header height"""
    
    # Remove padding-top from body
    content = re.sub(
        r'body\s*{[^}]*padding-top:\s*\d+px;[^}]*}',
        lambda m: m.group(0).replace(re.search(r'padding-top:\s*\d+px;', m.group(0)).group(0), ''),
        content
    )
    
    # Add header affix and main content CSS after body styles
    body_pattern = r'(body\s*{[^}]*})'
    replacement = r'''\1

        /* Header Affix */
        .header-affix {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1030;
        }

        /* Main Content */
        .main-content {
            margin-top: var(--header-height, 140px);
        }

        @media (max-width: 768px) {
            .main-content {
                margin-top: var(--header-height-mobile, 120px);
            }
        }

        @media (max-width: 576px) {
            .main-content {
                margin-top: var(--header-height-small, 100px);
            }
        }'''
    
    content = re.sub(body_pattern, replacement, content)
    
    # Remove fixed positioning from top-bar
    content = re.sub(
        r'(\.top-bar\s*{[^}]*?)position:\s*fixed;[^}]*?top:\s*\d+;[^}]*?left:\s*\d+;[^}]*?right:\s*\d+;[^}]*?z-index:\s*\d+;([^}]*})',
        r'\1\2',
        content
    )
    
    # Remove fixed positioning from navbar
    content = re.sub(
        r'(\.navbar\s*{[^}]*?)position:\s*fixed;[^}]*?top:\s*\d+px;[^}]*?left:\s*\d+;[^}]*?right:\s*\d+;[^}]*?z-index:\s*\d+;([^}]*})',
        r'\1\2',
        content
    )
    
    return content

def add_header_script(content):
    """Add dynamic header height JavaScript before closing head tag"""
    
    script = '''    
    <script>
        function setHeaderHeight() {
            const header = document.querySelector('.header-affix');
            if (header) {
                const height = header.offsetHeight;
                document.documentElement.style.setProperty('--header-height', height + 'px');
                
                // Set responsive heights
                if (window.innerWidth <= 576) {
                    document.documentElement.style.setProperty('--header-height-small', height + 'px');
                } else if (window.innerWidth <= 768) {
                    document.documentElement.style.setProperty('--header-height-mobile', height + 'px');
                }
            }
        }
        
        document.addEventListener('DOMContentLoaded', setHeaderHeight);
        window.addEventListener('resize', setHeaderHeight);
    </script>'''
    
    content = re.sub(r'(\s*</style>\s*</head>)', f'\\1{script}\n</head>', content)
    return content

def fix_header_structure(content):
    """Fix header HTML structure"""
    
    # Wrap top-bar and navbar in header-affix
    content = re.sub(
        r'<body>\s*<!-- Top Bar -->',
        '<body>\n    <!-- Header -->\n    <div class="header-affix">\n        <!-- Top Bar -->',
        content
    )
    
    # Update top-bar content
    content = re.sub(
        r'<i class="fas fa-clock"></i> Buka Setiap Hari: 08:00 - 21:00 WIB',
        '<i class="fas fa-clock"></i> Buka Setiap Hari: 08:00 - 20:00 WIB',
        content
    )
    
    content = re.sub(
        r'<i class="fas fa-phone"></i> <a href="tel:081234567890"',
        '<i class="fab fa-whatsapp"></i> <a href="https://wa.me/6281234567890"',
        content
    )
    
    # Close header-affix and add main-content wrapper
    content = re.sub(
        r'(</nav>)\s*(<!-- Breadcrumb -->)',
        r'\1\n    </div>\n\n    <!-- Main Content -->\n    <div class="main-content">\n    \2',
        content
    )
    
    # Close main-content before footer
    content = re.sub(
        r'(</section>)\s*(<!-- Footer -->)',
        r'\1\n    </div>\n\n    \2',
        content
    )
    
    return content

def fix_file(filepath):
    """Apply all fixes to a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"Fixing {os.path.basename(filepath)}...")
        
        # Apply all fixes
        content = fix_css_styles(content)
        content = add_header_script(content)
        content = fix_header_structure(content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Fixed {os.path.basename(filepath)}")
        return True
        
    except Exception as e:
        print(f"✗ Error fixing {os.path.basename(filepath)}: {e}")
        return False

def main():
    """Main function to fix all layanan files"""
    layanan_dir = 'layanan'
    fixed_count = 0
    
    print("Starting header fixes for layanan pages...")
    print(f"Files to fix: {len(files_to_fix)}")
    print("-" * 50)
    
    for filename in files_to_fix:
        filepath = os.path.join(layanan_dir, filename)
        if os.path.exists(filepath):
            if fix_file(filepath):
                fixed_count += 1
        else:
            print(f"✗ File not found: {filename}")
    
    print("-" * 50)
    print(f"Fixed {fixed_count}/{len(files_to_fix)} files successfully")
    print("Header fixes completed!")

if __name__ == '__main__':
    main()