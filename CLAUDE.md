# CLAUDE.md — Agri-Tech Valuation Engine

Bu dosya, projede yapılacak tüm kodlama ve tasarım işlemlerinde uygulanacak kuralları tanımlar.
Aşağıdaki prensipler üç kaynaktan derlenmiştir:
- [pbakaus/impeccable](https://github.com/pbakaus/impeccable)
- [kylezantos/design-motion-principles](https://github.com/kylezantos/design-motion-principles)
- [anthropics/claude-code](https://github.com/anthropics/claude-code) (frontend-design plugin)

---

## 1. Genel Tasarım Felsefesi (impeccable)

Jenerik AI estetiğinden kaçın. Her arayüz kararı bilinçli ve ayırt edici olmalı.

### Tipografi
- Varsayılan Inter veya Arial kullanma; projeye özel font seç ve pair'le.
- Modüler tip skalası uygula (ör. Major Third, Perfect Fourth).
- Başlık hiyerarşisi için OpenType özelliklerinden (liga, kern, frac) yararlan.
- Font weight'leri anlam taşımalı; dekoratif amaçla değil.

### Renk ve Kontrast
- OKLCH renk uzayını tercih et; HSL veya hex tabanlı rastgele tonlardan kaçın.
- Nötr grilerde istemeden oluşan renksel tonlanmaya dikkat et — saf siyah/beyaz nadiren doğal görünür.
- Dark mode için ayrı token seti tanımla.
- WCAG AA minimum; kritik metin için AAA hedefle.
- Renkli arka plan üzerinde gri metin kullanma.

### Boşluk ve Izgara
- 4px veya 8px tabanlı tutarlı bir spacing sistemi uygula.
- Grid yapısını görsel hiyerarşiye göre belirle; card içinde card iç içeliğinden kaçın.
- Beyaz alan bir öğe kadar önemli — sıkıştırma.

### Etkileşim Tasarımı
- Form alanları net focus state'e sahip olmalı (outline kalkmaz, stilize edilir).
- Loading durumları skeleton veya progress göstergesiyle belirtilmeli.
- Boş durumlar (empty state) bilgilendirici kopya içermeli.

### UX Yazımı
- Buton metni eylem fiiliyle başlamalı: "Kaydet", "Hesapla", "Görüntüle".
- Hata mesajları suçlayıcı değil, çözüm odaklı olmalı.
- Boş durum metinleri kullanıcıyı bir sonraki adıma yönlendirmeli.

### Duyarlı Tasarım
- Mobile-first yaz; büyük ekrana doğru genişlet.
- Container queries'i kullanarak bileşen bazlı duyarlılık sağla.
- Fluid typography ve spacing için `clamp()` kullan.

---

## 2. Anti-Patterns — Kesinlikle Yapılmayacaklar

Bu kurallar otomatik olarak uygulanır, istisna yoktur:

| Anti-Pattern | Neden Yasak |
|---|---|
| Arial / Inter varsayılan seçimi | Jenerik AI görünümü |
| Renkli bg üstünde düşük kontrastlı gri metin | Erişilebilirlik ihlali |
| Aşırı card iç içe geçmesi | Görsel gürültü |
| Bounce / elastic easing animasyonları | Tarihli ve dikkat dağıtıcı |
| İstemeden oluşan siyah/gri renk tonları | Tutarsız görsel dil |
| Dekoratif animasyon fazlası | Performans ve odak kaybı |

---

## 3. Motion Tasarım Prensipleri (design-motion-principles)

### Üç Perspektif — Proje Bağlamına Göre Seç

**Emil Kowalski — "Kısıtlama & Hız"**
Üretkenlik araçları ve yüksek frekanslı etkileşimler için:
- Animasyonlar kısa ve işlevsel (100–200ms).
- Yalnızca anlamsal değişimleri animate et.
- Tekrar eden eylemler için animasyon yorgunluğundan kaçın.

**Jakub Krehel — "Production Polish"**
Tüketici uygulamaları için:
- Geçişler pürüzsüz ve tutarlı (200–350ms).
- Giriş/çıkış animasyonları bileşenin ağırlığına göre ayarlanır.
- Her etkileşim state'i (hover, active, focus) için tanımlı geçiş.

**Jhey Tompkins — "Yaratıcı Deney"**
Keşif veya oyunsal bağlamlar için:
- Beklenmedik, zevkli micro-interaction'lar.
- Fizik tabanlı veya SVG animasyonu kullanılabilir.
- Performans izlenerek uygulanır.

> **Bu proje için:** Agri-tech veri arayüzü olduğu için Kowalski + Krehel karışımı uygula — hız ve netlik önce, parlama ikinci.

### Motion Audit Kriterleri
- Koşullu UI (modal, tooltip, dropdown) animasyonsuz olmamalı.
- Dinamik stil değişimleri (renk, boyut) transition içermeli.
- `prefers-reduced-motion` media query her animasyonda kontrol edilmeli.
- GPU'ya taşı: `transform` ve `opacity` animasyonlarını tercih et, `width`/`height` değil.

### Easing Referansı
```css
/* Standart geçiş */
transition: all 200ms cubic-bezier(0.4, 0, 0.2, 1);

/* Giriş */
animation-timing-function: cubic-bezier(0, 0, 0.2, 1);

/* Çıkış */
animation-timing-function: cubic-bezier(0.4, 0, 1, 1);

/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
  * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}
```

---

## 4. Frontend-Design Plugin Kuralları (anthropics/claude-code)

### Üretim Kalitesi Standartları
- Her bileşen izole ve yeniden kullanılabilir olmalı.
- Props arayüzleri açık ve minimal olmalı (prop drilling en aza indir).
- Stil için design token sistemi kullan (CSS custom properties veya Tailwind config).

### Görsel Ayrıntı
- Hover, focus, active state'leri her etkileşimli öğede tanımlı olmalı.
- Icon ve illustration seçimi tipografiyle uyumlu olmalı.
- Border-radius, shadow, ve opacity değerleri token'lar üzerinden yönetilmeli.

### Tipografi Hiyerarşisi
- En fazla 3 font weight projede bulunmalı.
- Line-height değerleri: başlık için 1.1–1.3, gövde için 1.5–1.7.
- Letter-spacing başlıklarda hafif negatif (-0.02em), body'de nötr.

### Animasyon & Hareket
- Anlamsız animasyon ekleme; her hareket bir bilgi iletmeli.
- Geçiş süresi hiyerarşisi: mikro (50–100ms), normal (150–300ms), vurgu (300–500ms).
- `will-change` mülkünü yalnızca gerektiğinde kullan.

---

## 5. Bu Projede Uygulanacak Geliştirme Kuralları

- Kod yorumu yalnızca neden (why) için; ne (what) iyi adlandırılmış kod tarafından anlatılır.
- Yeni soyutlama yalnızca üçten fazla tekrar varsa.
- Güvenlik: kullanıcı girdisi her zaman validate edilir; iç fonksiyon güvenilirdir.
- Hata işleme yalnızca sistem sınırlarında (API, kullanıcı girdisi).
- Test golden path ve edge case'leri kapsamalı.
