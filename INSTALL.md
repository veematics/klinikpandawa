# Panduan Instalasi Website Klinik Utama Pandawa

## Langkah-langkah Instalasi

### 1. Upload Files ke Server
```bash
# Extract file ZIP
unzip klinik-pandawa-website-complete.zip

# Upload ke server menggunakan FTP/SFTP
# Atau copy langsung jika akses server
```

### 2. Struktur Folder di Server
```
public_html/
├── index.html (redirect ke beranda.html)
├── beranda.html
├── tentang-klinik.html
├── hubungi-kami.html
├── spesialis-kulit-dan-kelamin.html
├── seksual-dan-reproduksi.html
├── estetika-dan-anti-aging.html
├── kesehatan-gigi.html
├── layanan/
│   ├── eksim.html
│   ├── vitiligo.html
│   ├── dermatitis.html
│   ├── [22 halaman layanan lainnya]
│   └── template-layanan.html
└── assets/
    ├── dokter_spesialis_team.webp
    ├── infeksi_menular_seksual_card.webp
    └── konsultasi_dokter_privat.webp
```

### 3. Update Konfigurasi

#### A. Nomor WhatsApp
Ganti semua instance `6281234567890` dengan nomor WhatsApp asli:
```bash
# Gunakan find & replace di editor
# Atau command line:
sed -i 's/6281234567890/62811234567/g' *.html layanan/*.html
```

#### B. Email Address
Ganti `info@klinikpandawa.id` dengan email asli:
```bash
sed -i 's/info@klinikpandawa.id/info@klinikutamapandawa.id/g' *.html layanan/*.html
```

#### C. Google Maps
Edit file `hubungi-kami.html`, cari section Google Maps dan ganti dengan embed code lokasi asli.

### 4. SSL Certificate
Pastikan SSL certificate sudah terinstall:
```bash
# Cek SSL
curl -I https://yourdomain.com
```

### 5. Setup Analytics

#### Google Analytics
1. Buat account Google Analytics
2. Tambahkan tracking code sebelum `</head>` di semua halaman:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

#### Google Search Console
1. Verify domain ownership
2. Submit sitemap.xml
3. Monitor search performance

### 6. Performance Optimization

#### Enable Gzip Compression
Tambahkan ke `.htaccess`:
```apache
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/plain
    AddOutputFilterByType DEFLATE text/html
    AddOutputFilterByType DEFLATE text/xml
    AddOutputFilterByType DEFLATE text/css
    AddOutputFilterByType DEFLATE application/xml
    AddOutputFilterByType DEFLATE application/xhtml+xml
    AddOutputFilterByType DEFLATE application/rss+xml
    AddOutputFilterByType DEFLATE application/javascript
    AddOutputFilterByType DEFLATE application/x-javascript
</IfModule>
```

#### Browser Caching
```apache
<IfModule mod_expires.c>
    ExpiresActive on
    ExpiresByType text/css "access plus 1 year"
    ExpiresByType application/javascript "access plus 1 year"
    ExpiresByType image/png "access plus 1 year"
    ExpiresByType image/jpg "access plus 1 year"
    ExpiresByType image/jpeg "access plus 1 year"
    ExpiresByType image/webp "access plus 1 year"
</IfModule>
```

### 7. Security Headers
Tambahkan security headers:
```apache
Header always set X-Content-Type-Options nosniff
Header always set X-Frame-Options DENY
Header always set X-XSS-Protection "1; mode=block"
Header always set Strict-Transport-Security "max-age=63072000; includeSubDomains; preload"
Header always set Content-Security-Policy "default-src 'self'"
```

### 8. Testing

#### Checklist Testing
- [ ] Semua halaman load dengan benar
- [ ] Navigation menu berfungsi
- [ ] WhatsApp links berfungsi
- [ ] Form contact berfungsi
- [ ] Responsive design di mobile
- [ ] Page speed < 3 detik
- [ ] SSL certificate aktif

#### Tools Testing
- Google PageSpeed Insights
- GTmetrix
- Mobile-Friendly Test
- SSL Labs Test

### 9. Backup Strategy
```bash
# Setup automated backup
# Backup files
tar -czf backup-$(date +%Y%m%d).tar.gz public_html/

# Backup database (jika ada)
mysqldump -u username -p database_name > backup-$(date +%Y%m%d).sql
```

### 10. Monitoring
- Setup uptime monitoring
- Monitor Google Analytics
- Check Search Console regularly
- Monitor page speed

## Troubleshooting

### Common Issues

#### 1. Images Not Loading
- Check file paths in HTML
- Verify image files uploaded
- Check file permissions

#### 2. WhatsApp Links Not Working
- Verify phone number format
- Test on mobile device
- Check URL encoding

#### 3. Slow Loading
- Enable compression
- Optimize images
- Use CDN if needed

#### 4. Mobile Issues
- Test on real devices
- Check viewport meta tag
- Verify responsive CSS

## Support

Untuk bantuan teknis:
- Email: support@doxadigital.com
- Documentation: Lihat folder dokumentasi
- Emergency: Contact development team

---

**© 2024 Klinik Utama Pandawa - Developed by Doxadigital Strategist Team**

