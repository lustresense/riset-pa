Pak TB


13/03/26 - 1
Diskusi PA dengan Pak Tri Budi (Pak TB)
Peserta: Can (Frontend/UI/UX), Dias (Backend/AI), Pak Tri Budi (Dosen Pembimbing)
Topik: Interactive Human-in-the-Loop AI Playground for Elementary School Students (HITL)
Tanggal: Maret 2025
Status: Detail discussion sebelum finalisasi judul & proposal
________________


BAGIAN 1: PEMBAGIAN KERJA & ARSITEKTUR UMUM
1.1 Struktural Kerja Tim
Pak TB: "Karena gini, ada semacam pembagian pekerjaan gimana? Anda lebih kepada interface user interface-nya dan preprocessing-nya akan pengolahan gambar awal itu. Nanti setelah data diproses dimasukkan di tempat lain, akhirnya di servernya itu entah itu server sendiri atau apa gimana."
Can: "Jadi ada pengulangan dapurnya, jadi ada semacam counter awal, display depan counter awal. Ibaratnya ngomong restoran, itu kan ada bagian penyajian menu dan sebagainya sampai customer service-nya, dan sebagainya itu. Kemudian ada bagian dapurnya."
Pak TB: "Iya benar, Pak. Itu tidak apa-apa, yang bagus itu. Jadi model-model semacam ini memang harusnya dikembangkan di TRM. Karena kalau mengerjakan sendiri nanti tidak nututi memang gitu ya, akan kedodoran gitu. Yang penting adalah bagaimana Anda memaksimalkan UI-UI-nya tadi. Jadi tampilan-tampilannya harus dimaksimalkan, kemudian preprocessingnya juga Anda perkuat, seperti level progression dari UI dan UI interface dan sebagainya tadi, dan juga preprocessingnya."
________________


1.2 Fokus Utama
Pak TB: "Bahkan ada hal seperti penentuan tema, penentuan coloring, penentuan ini ada pertimbangan-pertimbangan yang nanti menguatkan apa yang sama yang desain gitu Mas ya. Ini memang harus tajam banget gitu dari penguasaan UI yang baru semata sekali. Nah, kemudian nanti satunya yang biasanya adalah diproses pengolahannya itu memang bener-bener AI yang seperti yang diharapkan gitu."
Can: "Oke, memang kerjanya berat sebetulnya karena beratnya begini, eh sinkronisasi kedua anggota tim ini harus bener-bener bagus ini ya."
Pak TB: "Oke, apa lagi yang dijelaskan, Mogul? Saya setuju ini mode lagi, senang saya."
________________


BAGIAN 2: GAME MECHANICS & LEVEL PROGRESSION
2.1 Level System & Timer
Dias (atau Can): "Untuk selanjutnya disini ada level sih Pak. Karena level kita sempat ide untuk nambah lagi kalau ada puzzle ini. Jadi kita tambahin level-levelnya biar secara gameplay itu matang juga, gak hanya sekali pakai. Terus ada timer siswa-nya biar ambil keputusan gitu biar gak terlalu lama. Jadi makin lama dia makin ragu, terus masuk ke datalog tadi kurang lebih seperti itu pak untuk level progression-nya."
2.2 Core Game Loop
Dias/Can: "Lalu untuk sistem interaktif dan gameplay-nya kurang lebih sama seperti kemarin. Bisa replay lagi kalau salah atau kalau mati gitu. Terus ini core loop yang awal: fase gambar → main → koreksi → terus redo object. Ini mungkin bisa di-undo nanti atau user-nya itu gambar mau gak jadi gitu, di undo."
2.3 Interaksi Object & Gesture
Dias/Can: "Nah objeknya ini bisa di drag and drop tadi menggunakan gesture, nanti diatur sendiri sama user-nya. Lalu ada audio feedback ini sih Pak. Ada kalau misal override atau memilih gitu, nanti ada audionya untuk user-nya biar dapat sensory dari multimedia lain seperti dari audio."
2.4 Deadzone & Camera Input
Dias/Can: "Lalu deadzone ini sama seperti yang ada di presentasi saya ini Pak, jadi kemungkinan bakal ada deadzone. Tetep kayak gini cuma pake kamera aja."
Pak TB: "Oke oke oke. Kurang lebih seperti itu."
________________


BAGIAN 3: TEKNIS AI & BACKEND (DIAS)
3.1 Model & Dataset
Dias: "Ini yang pertama sih Pak, ada 5 opsi. Terus ini ada contohnya dari GWT. Ini apa ya? Okay untuk sign up-nya gimana Dias? Cerita lo. Supaya lebih meyakinkan nanti waktu ngajukan judul.
Jadi untuk yang pertama, yang AI dan model. Untuk AI model-nya, kami pakai visual object classification itu CNN MobileNet yang kami pakai buat mengklasifikasi sketch-nya dari gambar. Sisanya jadi itu nanti kayak diklasifikasi lagi dari gambarnya itu. Lalu kami nampilin beberapa yang cocok sama gambar-gambarnya itu tadi."
Pak TB: "Oke."
Dias: "Nah terus ada dataset QuickDraw dari Google. Yang tadi juga dibilang, percaya itu ada beberapa kategori, 15-20. Terus untuk formatnya itu grayscale. Untuk ini, konversi ke TensorFlow.js plus quantization buat berjalan di client-side jadi enggak terlalu berat lah di device user-nya."
3.2 Dataset Viewer & Data Logging
Dias: "Lalu ada dataset viewer yang nanti siswa itu bisa lihat kayak contoh gambarnya dari dataset yang kami pakai gitu, biar siswa-nya itu lebih memahami kenapa itu bisa mengenali bentuk-bentuk tersebut."
Pak TB: "Oke."
Dias: "Terus ini ada log dan data. Ada tujuh data log point seperti: timestamp, prediksi confidence, override, confidence gap, jumlah objek, proses, dan durasi waktu per keputusan. Jadi nanti kayak log datanya itu lengkap gitu Pak. Nanti yang buat ditampilkan juga."
3.3 Session Management
Dias: "Terus ada session management yang mana tiap siswa ini punya ID terpisah, kayak history, terus penggunaannya. Lalu ini yang tadi juga masuk di loggin. Beberapa kali replay juga masuk di log karena kami juga export log ke CSV atau JSON-nya buat nanti ditampilkan juga di UI-nya."
3.4 Architecture & Platform
Dias: "Nah lalu buat arsitektur sama platform-nya, kami pakai REST API, Node.js, sama Express. Terus log-nya kesimpan di server. Nah lalu progressive web app yang nanti aplikasinya itu bisa di install di tablet sekolah. Di device bisa offline juga kalau pakai server sekolah, tapi buat log-nya ini tetap butuh koneksi internet sih."
Pak TB: "Oke."
Dias: "Lalu client-side inference path yang mana model ini jalannya di browser jadi gak terlalu mau bubani device user lah Pak."
3.5 K-means Clustering untuk Analisis
Dias: "Terus untuk analisis dan research ini ada K-means clustering yang digunakan buat mengelompokkan dari semua data-nya itu Pak. Jadi ada beberapa segmen yang kami bagi jadi tiga yaitu high over-rate, terus acceptor, dan moderate evaluator."
Pak TB: "Tadi kamu kok pakai K-means clustering kenapa? Dan CNN-nya kan tadi sudah dipakai juga, iya kan?"
Dias: "Iya."
Pak TB: "Apa ini pada objek yang berbeda atau pada tahapan yang berbeda clustering ini?"
Dias: "Oke, clustering ini buat ini apa persis yang berbeda. Dia memang dia lebih ringan sih daripada yang itu ya."
Pak TB: "Oke, enggak apa-apa. Sementara biar gitu dulu aja nanti ketika sudah mau kepada judul, pada proposal nanti kami akan lebih bicara lebih detail lagi ya Mas ya."
________________


BAGIAN 4: FINALISASI JUDUL PA
4.1 Pentingnya System Design
Pak TB: "Itu ya. Sementara oke ya, udah bagus ini. Arahnya sudah bagus dan mengarah. Nanti ketika mau proposal, kami harus sering ketemu supaya pembagian kerja-nya dan kemudian ini harus disajikan dalam bentuk blok by blok diagram prosesnya dari mana kemana kemana. Nanti dari urutan proses itu nanti akan ketahuan pembagian-nya secara lebih enak mas gitu Pak. Insya Allah sistem gitu Pak."
Pak TB: "Nah, desain sistemnya itu. Sementara oke, jalan judul. Kalau sudah ada desain sistem juga enggak apa-apa. Kemudian nanti kalau walaupun belum detail enggak apa-apa Mas ya, Mas Farhan dan Mas Dias. Jadi Anda kalau mengusulkan judul diharapkan ada desain sistemnya gitu ya, walaupun sederhana gitu. Dan kemudian nanti pemecahannya di mana gitu ya. Karena judulnya akan juga terpisah ya. Judul besarnya sama, nanti ada subjudulnya akan gitu kan."
4.2 Opsi Judul Awal
Dias/Can: "Untuk yang pertama sih Pak, ada 5 opsi. Terus ini ada contohnya dari GWT.
Opsi 1: Pengembangan interaktif human in the loop AI playground karena kami kan formatnya AI playground gitu. Saya lebih menonjolkan finger tracking MediaPipe dan simulasi interaktif berlevel atau GIMP tadi untuk literasi kecerdasan artificial pada siswa kelas 5.
Opsi 2: Lalu si biasanya ini pengembangan sistem klasifikasi sketch-nya CNN MobileNet dengan confidence core explicit dan K-means clustering lagi untuk pola keputusan pada human in the loop."
Pak TB: "Oke, enggak apa-apa. Kalau ada yang... Oke, enggak masalah. Saya rasa ini judul-nya bagus-bagus ya Tuan. Yang penting ada ya penghubungnya kalau bisa. Dua judul ini ada kalimaty penghubungnya, sehingga benar-benar terkait dulu ya."
________________


4.3 Finalisasi Judul Utama
Can: "Nah ada kalimat yang menghubungkan jadi saya bener-bener judul-nya ini memang satu project gitu supaya tidak terpisah nanti pembagian-nya supaya enak."
Pak TB: "Oke. Jadi kami belum harusnya begitu. Nanti apa misalnya judul 'Literasi Kecerdasan Artificial Sekolah-Sekolah Dasar' itu bagus ya, itu saja. Kan tujuannya itu kan ya, sistem literasi ini ya, nanti subjudul-nya apa dan apa gitu ya."
Can: "Jadi untuk judul-judul besarnya ini ya Pak?"
Pak TB: "Sistem literasi kecerdasan artificial untuk anak sekolah dasar, kelas 5? Enggak usah nanti aja. Ini bagus ini. Sistem literasi, itu bagus. Bagus kok itu ya. Nanti ada subjudul-nya apa gitu ya."
4.4 Struktur Judul Final
Can: "Gitu ya, manggungnya emang-nya mau pakai yang mana enggak papa tapi aja 22 sub judul-nya."
Pak TB: "Oh awan lu subjudul? Bingung akan judul kalimat-nya jodoh ya? Karena sistem literasi sedasan buatan ya siswa-siswa kasar gitu dulu GG masuk aja dulu. Bagus kemudian nanti subjudul-nya apa-apa gitu. Ndak usah panjang-panjang ya. Semuanya mau ya?"
Can: "Iya masih dikasih skemansi MobileNet nah ini konfusen skor-nya usah ya?"
Pak TB: "Oh gitu ada-ada usah net belajar. Wes nanti akan ada pada interaksi human in the loop apa gitu ya. Nah gitu aja jadi kami tetep nang yang tuh ini ya Pak."
Can: "Oh ya. Oh yang ini saya undur ini Pak. Ini nanti mau pakai subjudul yang mana? Silakan. Tapi ada ada tetap ada ini bahwa sistem literasi kecerdasan artificial siswa sekolah dasar itu dulu ya."
Pak TB: "Oh gitu? Biar menarik ya ini mengenal sekali targetnya kepada siapa dan kemudian mengembangkan. Ini mau pakai subjudul yang mana? Silakan. Tapi yang penting objek Doowoyo ini untuk subjudul ini yang dipakai Dias gitu kan? Yang dipakai Dias, jadi sampe kan saya yang saya cukup bingung disitu juga. Subjudul ini maksudnya gini, subjudul-nya Dias apa subjudul sampe apa berarti?"
Can: "Oh ya, mahasiswa itu punya judul sendiri terus sama punya subjudul sendiri iya. Judul-nya sama, judul utama-nya sama."
Pak TB: "Oh, jadi sistem literasi kecerdasan buatan untuk sekolah dasar itu dulu ya? Kemudian nanti subjudul-nya Farhan yang mana? Dias yang mana?"
Can: "Oh jadi, oh bener tadi ya Pak? Kami tetap menyantumin ini. Pertama ya, subjudul-nya apa? Judul besarnya 'Sistem Literasi Kecerdasan Artificial untuk Sekolah Dasar, Anak Sekolah Dasar' itu ya."
Pak TB: "Subjudul-nya mungkin Farhan bisa 'Pengembangan Interaktif Human in the Loop AI Playground' ini tadi. Jadi ini penulisannya di awal atau di awal? Di awal judul utama-nya baru dikasih subjudul ada titik 2 nya gitu?"
Can: "Iya, subjudul titik 2 ya, seperti itu kak."
________________


4.5 Format Judul Final yang Disepakati
Pak TB: "Jadi judul besarnya itu sistem interaktif gitu ya iya tak? Sistem literasi kecerdasan asumsi, siswa sekolah dasar, titik. Bagus itu. Sistem literasi kan, sistem literasi kecerdasan buatan, atau kecerdasan artificial, siswa sekolah dasar, kelas lima enggak usah nanti aja."
Can: "Baru bawahnya sub untuk Dias apa, sub untuk Farhan apa, sehingga nanti..."
Pak TB: "Oke ya. Supnya tulisan Farhan sih supmu apa? Oke bagus itu. Supnya tulisnya sup sup gini. Sudah langsung sistem titik 2."
Can: "Oh langsung titik 2 gini ya Pak?"
Pak TB: "Iya, sudah ini bawahnya supnya ya. Bisa gampang kan ganti ya?"
Can: "Oh gini ya Pak yang 2 gini. Supaya tadi kan 'Pengembangan Interaktif Apa itu tadi kan'?"
Pak TB: "Oh gitu. Pengembangan berbasis berbasis pinjera apa itu disampaikan terus goni tracking tadi, media tadi, kemudian satunya lagi. Tapi depannya dikasih subjudul itu ya. Depannya pengembangan itu."
Can: "Oh gitu ya Pak? Subjudul-nya apa gitu?"
Pak TB: "Nah titik 2, kami coba lihat tembara lagi. Takak panjang dikit ada apa ya. Yang penting ada judul utama-nya itu ya ya ya. Jadi pikir Dewi ngeluh hahaha. Kemarin ya. Sudah, ya sudah. Nanti bisa diajukan gambaran sistem-nya. Kalau bisa dibagi-bagi tidak apa-apa gitu ya. Lebih bagus."
________________


BAGIAN 5: RESEARCH GAPS & NEXT STEPS
5.1 Research & Jurnal
Pak TB: "Oke baik Pak. Oke ya, oke ya. Habis lo nonton sini nonton ini. Dari kami juga untuk gap research-nya, mungkin kami nanti nyari jurnal pendukung-nya gitu ya Pak."
Can: "Oh ya ya oke. Biasanya ya gitu ya."
Pak TB: "Oke, sudah bagus mas ini mas ya. Siap Pak ya. Sudah, sudah benar ini nanti yang lebih sama ini saya suruh pilih juga kok."
5.2 Motivasi & Pesan Pak TB
Pak TB: "Oh ya sama Wildan. Ya saya senang kalau ada tim-tim grup ini malah jadi enggak sendirian walaupun lebih sulit. Soalnya sirai wanglero itu beda dari sirai uji ya? Kalau berhasil jauh lebih bagus dalam proses-nya jauh lebih sulit karena tantangan-nya banyak. Nanti berhasil ya siap ya tenang ya Insyaallah. Lewat ke oleh Anu tukaran gak mau tapi daulah Godo yo."
________________


RINGKASAN KEPUTUSAN
Struktur Judul Final:
JUDUL UTAMA:
Sistem Literasi Kecerdasan Buatan untuk Siswa Sekolah Dasar
SUBJUDUL CAN (FARHAN):
Pengembangan Interaktif Human-in-the-Loop AI Playground dengan [fokus UI/UX/Interaction]
SUBJUDUL DIAS:
Pengembangan Sistem Klasifikasi Sketch berbasis CNN MobileNet dengan Data Logging dan Analisis K-means Clustering untuk Evaluasi Pola Keputusan User
Fokus Utama Per Anggota:
Aspek
	Can
	Dias
	UI/UX/Interface
	✅ Lead
	-
	Preprocessing/Image
	✅ Lead
	-
	Level Design
	✅
	✅
	AI Model (CNN MobileNet)
	-
	✅ Lead
	Backend/Server
	-
	✅ Lead
	Data Logging
	-
	✅ Lead
	K-means Clustering
	-
	✅ Lead
	PWA Development
	✅
	✅
	Deliverables Sebelum Proposal:
* [ ] System design diagram (blok by blok, alur proses)
* [ ] User flow detail
* [ ] UI mockup/design
* [ ] AI model specification detail
* [ ] Data logging specification
* [ ] Research gap & jurnal pendukung
* [ ] Finalisasi subjudul masing-masing
Timeline:
* [ ] Sering meeting untuk sinkronisasi pembagian kerja
* [ ] Prepare system design diagram
* [ ] Research gap analysis
* [ ] Submit judul + system design ke dosen
________________


Catatan Penting dari Pak TB:
"Yang penting adalah bagaimana Anda memaksimalkan UI-UI-nya tadi. Tampilan-tampilannya harus dimaksimalkan, kemudian preprocessingnya juga Anda perkuat. Penentuan tema, penentuan coloring, ada pertimbangan-pertimbangan yang nanti menguatkan desain."
"Sinkronisasi kedua anggota tim ini harus bener-bener bagus."
"Ketika mau proposal, harus disajikan dalam bentuk blok by blok diagram prosesnya dari mana kemana. Dari urutan proses itu nanti akan ketahuan pembagian-nya."
"Kalau ada tim grup ini malah jadi enggak sendirian walaupun lebih sulit. Kalau berhasil jauh lebih bagus. Tantangan-nya banyak, tapi nanti berhasil Insyaallah."


24/04/26
NOTULENSI BIMBINGAN (PAK TB & FARCHAN)
Berikut adalah rekapitulasi percakapan yang telah dibersihkan dari noise dan difokuskan pada poin-poin inti perancangan sistem.
BAGIAN 1: PRIORITAS DESAIN & FILOSOFI EDUKASI
Pak TB: Konsep berpikirnya adalah bagaimana membuat user interface yang orang ingin berinteraksi. Baru setelah itu kita buat gameplay dan narasinya. Edukasinya justru disisipkan terakhir. Kuncinya: Kita mengajari orang, tapi jangan sampai dia merasa diajari. Karena belum tentu semua orang suka diajari. Pahami apa yang disukai anak SMP dari sisi antarmuka, gambar, dan warna. Farchan: Baik Pak. Saya sempat bingung prioritasnya. Untuk menengahi Interaksi, Gameplay, dan Edukasi, saya membawa konsep Maskot (Momo). Dia bertindak sebagai Game Master yang memandu tutorial agar tidak membosankan. Edukasinya baru ditekankan di akhir level (misal: log penyadaran bahwa AI bisa salah). Pak TB: Ya, boleh. Nanti pada saat mendesain, pilih kalimat yang paling pas untuk audiensnya.
BAGIAN 2: JUSTIFIKASI TEMA VISUAL
Farchan: Tema visualnya adalah Sketchbook (Buku Gambar), karakternya stickman. Aturan gamenya, jika menggambar benda tajam (danger), buku gambarnya akan sobek dan gagal. Pak TB: Kenapa Anda memilih konsep buku gambar? Harus ada alasannya. Kenapa orang di negara maju bisa menang persaingan? Karena setiap yang mereka sampaikan punya alasan yang kuat (acuannya apa). Nanti saat sidang atau kerja, Anda akan ditantang "Kenapa begini?". Anda harus punya konsep yang kuat untuk meyakinkannya.
BAGIAN 3: USER FLOW & LEVEL DESIGN
Pak TB: (Melihat diagram) Ini tulisannya kecil-kecil sekali, Mas. Ini mungkin bisa dipecah-pecah per grup atau tahapan. Dari bagian yang banyak, jadikan satu per tahapan. Sehingga saat ditanya, Anda bisa jelaskan tahap pertama apa, kedua apa, beserta detailnya. Farchan: Baik Pak, nanti saya pecah ada main flow dan flow rincinya. Untuk levelnya, rencananya ada 3 level dengan durasi game 1-10 menit. Level 1 gambar biasa (AI akurasi tinggi). Level 2 maksimal 3 objek (AI memunculkan tebakan alternatif). Level 3 rintangan kompleks (akurasi AI diturunkan agar Maskot bingung dan siswa harus mikir/override).
BAGIAN 4: ARSITEKTUR AI & KESALAHAN ISTILAH (CRITICAL)
Farchan: Level 3 akurasinya diturunkan. Sebelumnya kami sempat diskusi karena referensi dari 'Quick, Draw!' untuk real-time detection pakai RNN untuk akurasi tinggi... Pak TB: RNN itu konsepnya output dijadikan input lagi untuk waktu berikutnya. Makanya kalau tipe sequence pakai RNN. Nanti di dalam RNN ada banyak variannya. Kenapa pakai ini? Harus ada alasannya. Pakai ini dulu baru dicari alasannya tidak apa-apa, biar jalan.
BAGIAN 5: BACKEND, LOGIN, DATABASE, & CLUSTERING (DIAS)
Farchan/Dias: Untuk akses, kami sepakat siswa tidak perlu login menggunakan NISN/NTSN, cukup menggunakan Session ID karena tujuannya hanya untuk melihat data perilakunya. Login hanya disediakan untuk Admin/Guru. Kami pakai TensorFlow.js (client-side). Database pakai SQLite (karena JSON terlalu besar). Data yang disimpan: Session ID, Result, Confidence Score, User Decision (Override), dll. Untuk klasifikasinya pakai K-Means. Pak TB: Klasternya kenapa dibagi menjadi: Trust Acceptor, Critical Operator, dan Fast Decider? Yang mencirikan masing-masing itu apa? Fitur-fiturnya harus bisa membedakan. Tolong dicari data apa yang masuk untuk membagi 3 itu supaya K-Means-nya bagus. Semakin banyak dimensinya semakin bagus. Pak TB (Penutup): Saya melihat pekerjaan kalian (Farchan & Dias) masih terpisah. Waktu proposal nanti, kalian harus menguasai bagian masing-masing. Farchan di desain, antarmuka, dan tema. Dias di AI dan Clustering. Tapi kalian berdua harus paham sistem keseluruhannya secara utuh. Walaupun kerjanya bareng-bareng, saat sidang pembagiannya harus dikuasai betul.
SUMMARY & ANALISIS OBJEKTIF (ACTION ITEMS)
(Catatan Strategis untuk Farchan agar SPPA Aman & Defensible)
Berdasarkan transkrip di atas, bimbingan ini sangat sukses, tapi ada beberapa "PR" dan "Jebakan" yang harus lu beresin segera sebelum sidang proposal.
🟢 THE WINS (Kemenangan Lu)
1. Prioritas Di-Approve: Pak TB setuju lu fokus ke UX/UI dan Keseruan Game dulu, baru edukasi di belakang. Ini bikin beban lu mendesain jauh lebih ringan.
2. Konsep Leveling Di-Approve: Pak TB sepakat sama ide Level 1 (Gampang) sampai Level 3 (AI Dibuat Bego).
3. Database Ringan & Bebas Auth Di-Approve: Pindah dari JSON ke SQLite disetujui, dan yang paling melegakan: Siswa tidak perlu login. Ini menghapus beban lu untuk bikin halaman Register/Login, Lupa Password, dan integrasi Auth untuk ratusan siswa.
🔴 THE RED FLAGS & CARA FIX-NYA (Sangat Penting)
1. Jebakan Istilah AI (RNN vs CNN)
* Masalah: Di transkrip, lu nyebut RNN (Recurrent Neural Network) gara-gara terinspirasi Quick, Draw!. Padahal di obrolan kita sebelumnya, arsitektur lu sama Dias itu pakai CNN (MobileNet via TF.js) karena ini image classification (gambar statis), bukan deteksi sequence coretan real-time.
* Cara Fix (Defensible): Jangan sebut RNN lagi di proposal lu. Quick, Draw! pakai RNN karena dia ngerekam urutan vektor tarikan garis dari mouse. Lu pakai MediaPipe + TF.js yang kemungkinan besar meng- capture gambar sebagai matriks pixel statis. Sinkronisasi sama Dias SEKARANG, pastikan di proposal tertulis CNN (Convolutional Neural Network), bukan RNN.
2. Alasan Pemilihan Tema (Filosofi Sketchbook)
* Masalah: Pak TB minta alasan akademis/logis kenapa milih Sketchbook. Lu belum ngasih jawaban yang memuaskan beliau di meeting tadi.
* Cara Fix (Defensible): Di Bab Perancangan (Bab 3), tulis alasan ini: "Tema Sketchbook dipilih sebagai representasi 'Dunia Analog/Manual' siswa, yang dikontraskan dengan Momo sebagai 'Entitas Digital'. Metafora kertas sobek digunakan karena memberikan konsekuensi visual yang paling intuitif bagi remaja saat sebuah kesalahan fatal terjadi, sesuai dengan arahan Pak TB untuk 'mengedukasi tanpa terasa menggurui'."
3. Diagram Flow yang "Mata Minus"
* Masalah: Pak TB komplain flowchart lu terlalu kecil dan tumplek-blek jadi satu.
* Cara Fix (Defensible): Pecah diagram lu jadi 3 gambar di proposal:
   1. Diagram Konteks Global (Start -> Main -> End).
   2. Diagram Onboarding (First-Time vs Returning).
   3. Diagram Core Gameplay Loop (Fase Gambar -> Fase AI Nebak -> Fase Override).
4. K-Means Clustering (Beban Dias)
* Masalah: Pak TB nanya "Apa variabel/fiturnya sehingga bisa dibagi jadi Trust Acceptor, Critical, Fast Decider?".
* Cara Fix (Defensible): Kasih tau Dias, variabel X dan Y untuk K-Means nya harus jelas.
   * X = Decision Latency (Berapa detik siswa mikir sebelum klik).
   * Y = Override Ratio (Berapa persen siswa menolak tebakan AI).
   * Z = Danger Acceptance (Berapa kali siswa tertipu benda tajam).
   * Dari 3 sumbu (dimensi) ini, algoritma K-Means baru bisa mengelompokkan siswa secara akurat.
Kesimpulan: Lu udah di jalur yang sangat benar, Can. Sisanya cuma masalah merapikan dokumen (pecah diagram) dan meluruskan istilah teknis (CNN bukan RNN) biar nggak dibantai sama penguji lain.


09/06/26
Oke, gue bersihin transkrip lo yang super berantakan itu. Ini hasil ekstraksi inti bimbingan lo semalam:


---


## Notulensi Bimbingan — Farchan (Can)


**Dosen:** Pak TB (Tri Budi)
**Tanggal:** Bimbingan malam, via Google Meet
**Peserta:** Farchan, Pak TB, beberapa mahasiswa lain
**Konteks:** Lo presentasi deck progres (PPT) ke Pak TB


---


### Poin 1 — Apresiasi Konsep


Pak TB bilang konsep lo udah matang. "Kekuatannya adalah di dalam ilustrasi yang Sampein buat. Ceritanya itu, konsep game-nya." Beliau juga reaffirm urutan prioritas yang lo pake: interaksi dan gameplay dulu, edukasi belakangan. "Kemudian baru nanti muncul di bagian belakang Sampein ingin memberikan edukasi." Ini konsisten dengan arahan beliau sebelumnya.


---


### Poin 2 — Mulai Nulis, Jangan Cuma PPT


Ini poin paling penting. Pak TB beberapa kali balik ke ini:


"Mulai sekarang, jangan hanya bikin PPT begini. Mulailah menulis."


"Biarkan saja apa yang pertama sampai menuliskan dulu. Bentuknya model apa saja tidak apa-apa. Nanti setelah selesai, kamu baca lagi, kan? Kemudian akan muncul ide baru lagi."


Beliau bilang jangan nunggu sempurna. Mulai tulis draf proposal—nanti revisi sambil jalan.


---


### Poin 3 — Style Penulisan: Buku TA vs Paper/Jurnal


"Ini ada flowchart yang detail banget ya. Nanti kalau di dalam penulisan mungkin bisa diseranakan. Kalau untuk buku tidak apa-apa, tapi ketika sampai gaya karya ilmiah tidak boleh."


"Kalau buku dibuat sedetail mungkin tidak apa-apa. Kalau paper atau paper konferen atau jurnal dibuat seminim mungkin, makanya dibuat paragraf itu."


Maksudnya: flowchart detail lo itu bagus buat buku TA, tapi nanti untuk jurnal atau paper harus diringkas jadi narasi paragraf.


---


### Poin 4 — Batasan Masalah Udah Oke


Pak TB sempat cek slide batasan masalah lo dan bilang: "Oh iya, oke, oke, cukup."


---


### Poin 5 — Pipeline Udah Oke, Arahnya Udah Bener


"Pipeline nya sudah oke, sudah ikuti sudah enak ini, kalau ingin mengikuti pola ini satu persatu ketemu nanti."


"Oke, ini arahnya untuk proposal kali ya, semuanya ya."


Beliau konfirmasi bahwa pipeline dan arah proposal lo udah benar.


---


### Poin 6 — Kirim Draf ke Pak TB


"Yang sudah ditulis tadi dikirimkan ke saya aja enggak apa-apa, belum jadi enggak apa-apa yang dokumen tadi."


Pak TB minta lo kirim draf proposal lo—meskipun belum jadi. Beliau mau lihat progres tulisan lo.


---


### Poin 7 — Deadline & Target


"Nanti kalau misalnya urusan KP sudah tuntas, proposalnya digeratak ya, cepetan ya."


"Jadi deadline-nya terpenuhi, gitu aja dulu ya semuanya. Oke, itu sampai di tengah jalan kita perbaiki, tidak apa-apa."


Intinya: kejar deadline, kumpulin dulu, revisi belakangan.


---


### Poin 8 — Dibikin Poin-Poin Biar Enak Dibaca


"Nanti tolong dibuat poin-poin tadi ya. Biar enak."


"Kalau di dalam penulisan buku lebih enak gitu, tapi kalau dalam penulisan paper karena dibatasi jumlah halamanya, biasanya dalam bentuk paragraf."


Beliau prefer format poin-poin untuk draf yang lo kirim ke beliau.


---


## Action Items (PR dari Bimbingan Ini)


| [x] | Task | Deadline |
|-----|------|----------|
| [ ] | **Mulai nulis proposal**—jangan cuma PPT. Tulis apa aja dulu, jangan nunggu sempurna | Sekarang |
| [ ] | **Kirim draf ke Pak TB**—yang udah ditulis, meskipun belum jadi. Format poin-poin dulu, bukan paragraf padat | Secepatnya |
| [ ] | Kejar deadline proposal | Sesuai timeline prodi |
| [ ] | Pertahanin pipeline dan arah yang udah disetujui | - |


---


## Yang Nggak Perlu Lo Pikirin


- Soal style penulisan jurnal/paper—itu urusan nanti. Sekarang fokus ke buku TA dulu yang bisa detail.
- Soal Dias—di bimbingan ini lo sendirian, Pak TB nggak nanya soal Dias. Tapi lo tetap perlu sinkronisasi.


Bu Hesti


13/03/26 - 2


All Transcript
ada fase koreksi juga, di sini kami punya klasifikasinya jadi gambar yang user menggambar sesuatu itu dikategorikan berdasarkan tiga ini ada benda yang solid, ada yang berbahaya dan ada dekorasi tembus pandang. Jadi ketika user menggambar suatu hal yang tajam dan dianggap berbahaya, itu user bisa gagal dan mengulangi lagi. Mengulangi ini bisa sampai beberapapun, nanti ada muncul tindakan untuk user bisa merevisi objek-objeknya mau ditambah lagi atau diganti atau dihapus gitu kan. Ada gak intro di awal yang mengatakan bahwa kalian tidak boleh menggambar-gambar yang berbahaya itu? Jadi mereka sudah tahu dari awal bahwa itu nanti tidak diperbolehkan di playgroundnya mereka ini? Itu awalnya seperti itu, memang masih abstract. Tapi setelah kita diskusi, kita menerapkan tiga level. Jadi di sini misi ada 3 level disini, level 1 bebas jadi usernya bebas menggambar apapun entah ukut tajam jadi bisa dibuat dikasih instruksi gitu. Mungkin lebih ke di level 3 ini atau di level 4 itu sudah disuruh menggambar objek yang diklasifikasikan sebagai yang berbahaya gitu. Jadi misalnya disini level 2 ada max 3 objek. Nanti kita rencana kasih instruksi atau quest gitu. Gambar 1 objek solid dan 3 objek berbahaya gitu. Apakah aman? Misalnya ini subjeknya siswa. Iya, iya. Siswanya umur berapa ini? Kelas berapa? Kalau target berdasarkan bukunya pasti masih. Masih terlalu kecil loh itu. Iya. Iya. Gimana caranya tidak sesuai dengan mereka deh. Kayaknya jangan deh ya. Oh gitu. Yang berbahaya itu apa gimana gitu ya. Makanya saya bilang di awal itu skenario-nya harus jelas. Yang boleh dan yang tidak boleh gitu. Oh gitu ya. Jadi dari awal sudah ada batasan yang mereka pahami. Ya. Gitu. Berarti kita mau. membuat seolah mereka nggak bisa gambar yang tajam. Iya, betul. Sebentar, ini goalnya apa? Endingnya nanti apa? Endingnya nanti apa yang kamu harapkan? Ending yang saya harapkan itu siswanya jadi lebih memahami probabilitas AI sama trial and error dari hasil gambar tadi. Untuk anak kelas 5 mah itu gak sampai di otak mereka itu. Terlalu sulit untuk anak kelas 5 itu. Memahami probabilitas error itu belum ada di otak mereka. Itu paling SMP ke atas ya. Kelas... kelas 7 ke atas itu sudah bisa tuh kalau itu jadi kalau mau tetap dengan goal kamu seperti itu kita goalnya tetap jangan di level SD mainkan di level SMP ke atas itu lebih enak gitu Gitu. Jadi kalau mau tetap skenarinya begini, tetap seperti ide kalian, enggak apa-apa, lanjut aja. Tapi ya itu, target usernya disesuaikan. Kalau untuk kelas 5 belum masuk di logika mereka. belum mereka itu kamu belum punya anak soalnya sih kamu tahu gitu belum sampai mereka cara berpikirnya ke situ SMP yang paling udah bisa ya makanya saya suka heran kalau orang tua ngelesin anaknya robot, anak-anak SD, anak TK gitu dilesin robot, menurut saya percuma karena secara perkembangan otaknya mereka belum bisa ke situ belum sampai, itu terlalu dipaksakan menurut saya anak-anak yang dari kecil SD, SMP, SDK sudah diajarin robot katanya untuk melatih logika logika itu nanti akan terbentuk sendiri kok kalau misalkan memang udah cukup umur gitu Jadi yang kita pahami di sini, ini saya rasa kalau kamu mau bicara tentang anak-anak bisa memahami probabilitas AI yang error dan enggak, dalam pemahaman saya dan pengamatan saya selama ini, ini untuk level SD masih sulit. Bukan enggak bisa, tapi akan sulit. Nanti kalau kamu pengujiannya banyak yang gagal, nanti sayang. Jadi mendingan langsung kita targetkan saja levelnya di level SD. Apa namanya? SMP ke atas. Iya, betul. Untuk SMP itu ada spesifikasi ke kelas berapakah? Atau di pertengahannya seperti kelas? Kelas 7 sudah bisa rasanya. 7, 8, 9. Malah 9 sudah sangat menurut saya sudah. 9 itu sudah di umur 14-15 tahun ya. Iya, betul. OSD kelas 5 itu masih umur berapa? 10, 10 tahun, 11 tahun, masih kecil banget itu. Belum bisa. Tapi kalau SMP itu sudah lebih terstruktur juga dan cara berpikirnya juga, kognitifnya juga sudah lebih matang dibandingkan anak kelas 5. Oke lanjut dulu. Silakan. Baik, terima kasih atas maksudnya. Untuk selanjutnya disini. kita pakai arsitektur ini yaitu hand sketch input tadi user itu menggambar lalu di process di mobile net cnn lalu di optimize untuk ditampilkan ke confidence dan atau untuk override dari user datasetnya kami dari quick draw tadi yang sudah saya highlight lalu kita pakai model optimization tadi yang pakai mobile net dan ini interaction matrix kita taruh ke log gitu sih jadi kayak ada dashboard untuk admin atau mungkin berguna untuk yang guru atau kita ikutkan saya minta kayaknya kamu lanjut dulu ya nanti saya takut saya lupa kamu harus bikin ini Farsan bikin use case use case itu gimana? saya baru dengar ini gimana caranya kalau mau menggambar disini bisa gak? menggambar di Di sini ada whiteboard-nya enggak ini? Google Meet. Iya. Ada enggak? Google Meet ini enggak ada. Enggak ada ya? Kalau di Zoom kan ada whiteboard ya? Iya di Zoom ada whiteboard. Oh. Atau... Gue mau bikin config untuk fiction. Enggak, jadi gini aja. Kamu bisa googling. Nanti saya coba kirimin contoh use case gambar. Jadi use case itu adalah ada berapa role yang masuk di sini. Kan ada role sebagai user, ada role sebagai admin kan ya? Oh, iya, iya, iya. Begitu kan? Nah, kamu harus bisa split di situ. Nanti kalau sebagai user, dia bisa mengakses fitur mana saja dan apa saja yang dia bisa lakukan di aplikasi kamu ini. Sementara di admin, dia bisa melakukan apa saja, modifikasi apa saja dan apa namanya... Rolnya itu apa saja gitu Coba di split dulu deh itu nanti ya Itu di buku kamu nanti Kamu sampaikan sebelum saya lupa Karena yang kelihatan di screen kamu ini Ini kan sebenarnya di mata user kan tidak tampak di mereka kan Iya Mereka tidak melakukan apa-apa Taunya tinggal gerak-gerakan aja kan Mereka tinggal pakai kan Nah yang tahu ini kan si admin ya Iya Mungkin ya dalam bayangan saya seperti itu. Coba kalian pikirkan lagi deh. Oke lanjut. Oke, baik-baik. Terima kasih atas sarannya. Sudah kami catat di sini. Untuk selanjutnya ada implementasi scalabilitas. Kita menggunakan TensorFlow.js untuk menangkap gambarnya tadi dan dikirim ke mobile net untuk diproses memunculkan ini, confidence form atau mencari data seperti tadi, dicocokkan dengan gambar user kita. Dulu kami pernah di Matkul AI itu belum berhasil jadi kita pakai Lendron. Oh yaudah oke. Harusnya enggak sulit sih. Oke terus lanjut. terus selanjutnya kurang lebih ada server yang buat lock tadi sama device ini kami masih mengkaji ulang sebut apakah kita pakai client side atau di device siswa itu dikasih modelnya atau enggak jadi antara di device siswa atau full di server pusat itu masih Nah itu ada plus minusnya masing-masing ya, kalau full di server itu kebergantungannya luar biasa, tapi kalau di device siswa kamu gak perlu nunggu connect-connect dulu ya. Jadi kalau di device siswa kami mikirnya yang connect ke server cuma untuk log data itu tadi. Lalu selanjutnya disini ada log yang kami maksud tadi. Ini dikelompokkan ada stempel waktu, ada prediksinya ini. Prediksi yang paling tinggi, yang menengah, atau yang paling bawah. Kalau disini tadi user menginterupsi atau meng-offline berdasarkan menurut dia itu gambar apa. Oh ada ya, boleh ya mereka ambigu ya. Nah konsep awalnya ada sih Bu, tapi itu takutnya mempengaruhi model AI sama data safety. Dipikirkan ulang lagi deh itu ya. Kalau masih awal-awal nggak apa-apa dimasukkan, cuman saya kok agak ragu ya. Coba selanjut aja dulu ya. Terima kasih. Jadi disini ada confidence score. yang data-data semua hasil user itu masuk ke sini ada point and score, ada pilihan user, ada status interaksinya itu apakah yang paling atas diterima atau direvisi yang kedua atau yang di-override ini yang gak ada pilihannya sama sekali jadi ada durasi keputusannya juga kurang lebih seperti itu Ini manfaatnya kurang lebih seperti ini ada human interaction prototype human idul tadi sama portfolio riset. Untuk batasan masalah di card kurang lebih seperti ini. ada subjek penelitian tadi mungkin juga kami akan ubah ke siswa SMP sesuai saran Bu Hesti kalau arsitektur modelnya kita pakai client-side tadi biar sama data set dari quickdraw biar latihan modelnya tidak dari nol banget terus ada cakupan dampaknya disini lebih ke ini sih gue yang saya masih bingungkan apakah kita itu wang evaluasi dampak psikologis yang kepanjang ya siswa kalau kamu pakai sampai ke situ kamu nggak selesai setahun kamu paling tahun butuhnya jadi bener ini enggak kita masukin atau kita tetap masukin di batasan masalah Oh sorry ini batasan masalah ini tetap di sini ya boleh Iya betul cakupan dampak. Jadi itu enggak masuk dalam sampai ke situ kalian risetnya ya. Terlalu jauh itu. Baik, saya lanjutkan ya. Di sini ada fokus analisis juga. Jadi masuk ke log tadi yang bisa dianalisis. Lalu evaluasinya dilakukan dengan data log yang saya highlight tadi. Lalu platform pengujiannya ini berbasis 2D tanpa proses berkemodal. Jadi seperti itu. Lalu disini ada referensinya, disini kesimpulan saja, mungkin saya skip. Dan referensinya itu kebijakan konteks pendidikan tadi yang mendampak teknologi perkembangan untuk anak dari beberapa dan ini dari yang kami pakai ada quick draw juga. Sekarang habis seperti itu. Cukup sibuk dari saya. Oh ini saya mau munculkan screen yang apa tadi? Quick draw. Quick draw ini. Quick draw mungkin bisa dijelasin sama dia. Silahkan. Oh gak di... Gambarmu kan bagus-bagus nih. Benar, saya buka dulu. Isin share screen buat quick draw-nya, Bu. jadi ini kan kita ambil datasetnya itu dari quickdraw nah nanti kita ambil beberapa sampel dari quickdraw juga terus kita juga ada adaptasi dari beberapa fitur quickdraw ini yuk terus ini kan bisa anggap ber link sourcer nah nanti itu kan kesimpen di database gambarnya itu, terus nanti ditampilkan lagi. Nah itu kita juga adaptasi di project kita kali ini. Gimana gambar Octopus? Ya, kurang lebih seperti itu. Yang kami implementasikan itu juga fitur yang tadi auto deteksi berdasarkan user menggambar. Jadi tiap pikselnya itu kita pakai. Kalau yang kita baca itu RNN. Deteksi real time dari setiap user menggambar. Di situ terlihat juga IC radio, IC kamera berdasarkan pengen digambar user. Ya. Itu teknikal banget ya yang seperti itu. Jadi saya pikir kalian perlu banyak, jangan langsung memutuskan akan pakai ini, pakai itu ya. Karena perlu riset dulu ya. Kalau kamu perlu riset dan nanti kalau riset akan ketemu, oh ini ternyata nggak cocok nih di sini ya, ini ada kendala di sini, ganti lagi yang lain gitu ya. Jadi saran saya kalau untuk di proposal, Apalagi di judul, jangan menyebutkan secara spesifik satu tool atau apa gitu ya, yang kalian gunakan karena takutnya nanti berubah kalau kalian masih belum yakin. Kecuali kalau kalian sudah yakin, itu boleh dicantumkan. Seperti itu. Baik, Bu. Terima kasih. Oke, ada lagi? Clear? Itu kamu apa sekarang gambarnya? Masih bulu. Masih bulu. Nah ini kan nanti ditampilkan semua di akhirnya pas kita udah selesai semua gitu. Nah ini nanti di project kita juga ada fiturnya kayak gini terus gambarnya juga nanti kita masukin ke database buat AI itu juga bisa menghitung probabilitas dari gambar-gambar yang dibuat siswa itu. Jadi nanti itu kayak patokannya itu gak cuma data yang kita ambil dari quick draw yang bagus gitu, jadi kita juga ambil data dari gambar siswa yang masih kurang bagus juga sih. Paham, paham. Ini untuk lebih memudahkan supaya bisa dipahami, coba kalian bikin flowchart ya. Flowchart dari awal sampai akhir itu seperti apa flow yang harus dilakukan oleh si user atau siswa. Jadi pertama kali masuk dia ketemu dengan apa Terus ada perintah apa Apa yang harus dilakukan Coba bikin dalam bentuk flowchart ya Flownya itu biar kelihatan Itu akan lebih mudah Kalau misalkan dia tidak berhasil Ada gak kemungkinan dia tidak berhasil? Ada kemungkinan tidak berhasil jika suatu benda yang digambar itu tidak bisa bikin karakternya itu sampai ke finish, Bu. Tidak sampai ke finish. Bukan tidak sesuai ya, tapi tidak se-finish ya. Iya benar, Bu. Ya, oke berarti dia tidak berhasil. Nah itu ada kondisinya, kalau dia tidak berhasil terus dia harus kemana, apa yang harus dia lakukan, itu makanya perlu dibikin flow-nya ya. Untuk memudahkan kalian mendesainnya nanti. Jadi if fail then what gitu loh. Iya ya. Kebayang ya. Saya paham maksud kalian, cuma saya ngebayanginnya ini flow-nya ini bagaimana dari awal sampai selesai ya. Ini sekalian-kalian sambil nyisil bikin design system ya, kayak kurang lebih nanti bisa jadi lebih paham kalau sudah kebayang atau ada gambaran flow-nya, user flow-nya itu bagaimana nanti setelah itu lebih mudah untuk bikin design systemnya. Berarti dari user flow dulu baru kita bikin design system. Iya, betul. Kalau design system itu intinya ada tiga, ada input, ada proses, ada output. Nah, kalau di user flow kamu sudah jelas, kamu akan tahu nanti inputnya ini apa. Misal inputnya gambar atau inputnya sound atau inputnya... Apa gitu ya. Gambar ini di prosesnya itu apa yang dilakukan gitu ya. Terus nanti outputnya bagaimana. Itu aja sih prinsipnya kalau design system. Ada input, ada business, ada output. Tapi selesaikan dulu flow usernya. Itu user flow-nya juga di-fix-kan dengan use case tadi ya? Itu dua hal yang berbeda sebenarnya, tapi terkait. Kalau use case itu dia cuma seperti ini. Sebentar saya carikan, banyak kok contohnya. Nah ini. Saya mau share screen gimana caranya? Bah, gap text saya. Ini, bisa enggak kalian lihat? Belum kelihatan. Oh ini udah? Udah, udah kelihatan. Jadi kalau di workflow itu menggambarkan dua hal yang kita gambarkan. Ada role. Sorry, ada aktor dan ada role. Nah, di sini kan kalau di sini use case ini ada 4 aktor atau 4 domain, 4 peran. Nah, perannya waiter ini dia bisa melakukan apa? Nanti di dalam aplikasinya itu ada aplikasi untuk order, ada untuk serve, ada untuk order wine, ada untuk cook. Ada untuk ini, ada untuk ini, ada untuk ini ya. Ini fitur-fiturnya ini. Nah siapa yang bisa mengakses fiturnya ini? Witer. Apa yang dia lakukan? Dia receive. Kemudian apa lagi yang dia bisa lakukan? Dia bisa serve. Kemudian apa lagi yang dia bisa lakukan? Dia bisa pay for food. Jadi kelihatan di sini nanti kemana saja jalurnya. Ini kalau kalian punya lebih dari satu role dalam aplikasi kalian. Tapi kalau kalian cuma punya satu role tidak perlu membuat server. satu ini sebenarnya satu asat torol itu peran atau aktor ya Hai ya Bu kebanyakan ya Cukup kebayang. Ini use case namanya. Kalau user flow itu gampang sih, itu biologik aja kalian gambangkan, masukkan apakah perlu login atau langsung start ya. Kalau langsung start apa yang dia lakukan di screen pertama, dia ketemu apa, terus apakah langsung drawing gambar atau bagaimana, atau harus select sesuatu dulu, terus next stepnya ngapain, ya seperti itu yang disebut sebagai user flow. Oke, baik. Nanti yang kami udah kebayang itu di awal kayak usernya dikasih grade dulu gitu. Menurut saya ya. Supaya mereka gak mendebak-nebak juga. Oke, baik. Tapi sudah, kalian coba kembangkan aja terus sendiri dulu. Ini menurut saya risetnya harus dalam ya. Iya, baik. Ini izin bertanya, dikarenakan dari Kak Prodi kan minta untuk sub-tut hari ini, jadi kira-kira yang perlu kita selesaikan untuk berkas pendukung itu apakah itu semua tadi juga nih? ah gak usah, prodetil itu gak usah gak usah itu selanjutnya untuk dimasukkan di dalam proposal kalau yang diminta Kak Prodi ini kan apa namanya sebenarnya kalian ngecap aja pun juga gak masalah ya soalnya yang saya dapet dari anak bimbingannya Pak Hafiz itu yang harus disubmit isinya Rencana penelitian, gap penelitian, metode penelitian, sama rencana. Jadi itu kayak kita nyusun secara general dulu aja gitu ya, Bu. Iya, gak usah spesifik. Jangan spesifik. Jadi ya biasa aja, general aja. Kalaupun tidak sesuai dengan yang kamu tulis, yang kamu masukkan, dan yang kamu kerjakan aja, gak apa-apa kan namanya juga masih ide. Namanya juga masih proposal. Jadi jangan terlalu khawatir yang kayak gitu-gitu. Iya. Berarti untuk yang hasil diskusi hari ini, kursamu BSD ini kami kembangkan untuk jangkaan dan ke depannya Iya betul Tidak harus hari ini, enggak Gila apa hari ini Enggak mungkin, kamu butuh mikir buat ngerjain itu Enggak mungkin, yang diminta Pak Hafiz itu saya lihat kok, karena Nabi Mi saya sudah screenshot ya, ngasih tau gitu ya, itu deskripsi biasa saja, enggak usah terlalu detail juga Oke Sebenarnya tujuannya Pak Hafidz dan Pak Zaka minta itu dia hanya ingin tahu mahasiswa A, B, C ini sudah dapat topik apa, dengan pemimpin siapa, itu aja sih. Jadi mendeteksi kalau ada yang belum, nah itu nanti akan kelihatan di list-nya mereka. Begitu tujuannya. Oke, baik-baik. Oke, clear ya? Sudah ya? Ini Bu, izin bertanya. Kan ini saya satu proyek dengan Bias dan Bias juga saya ajak untuk dosen pemimpin buahnya Bias. Barusan saya kan di-invite. Apakah Bias juga perlu di-invite juga? Iya, benar. Ini split pekerjaan kalian ya? Saya belum clear. Gimana Bu? split pekerjaan kalian Bagaimana jadinya saya saya tadi belum clear yang kita belum jelasin itu jadi split pengerjaan kamu saya izin share lagi ya iya iya silakan kami sempet apa ya bedah fiturnya sibuk ya rencana fitur awal terus kami udah itu kurang lebih saya di bagian kontennya disini kalau dia selalu bagian tekniknya atau ianya di AR-nya tadi yang Computer Vision di sini, Virtual Campus dan lain-lain itu yang hijau ini saya terus split-nya yang dia itu bagian dari AI-nya dan di sini dia juga sempat ada ideasi untuk ngasih head map gitu sih Bu untuk tiap gambaran dari usernya itu bagian mana yang paling mempengaruhi confidence score-nya gitu. - Kalau lebih seperti itu sih. - Oke. ya oke oke baik kalau begini ya oke terima kasih ya makasih sudah cukup ada lagi Hai dari saya cukup sibuk saya cukup ini karena sempat takut yang ini aja yang Pak Hafiz ingin kita juga masih bingung buat isinya juga soalnya Biasa aja itu jangan terlalu serius, gak usah dikhawatirkan ya, biasa aja. Kadang sebenarnya kalau saya mau ini, karena pengalaman di angkatan 2021 ya anak-anak saya terlalu detil menuliskan itu, punya-nya terlalu detil, terus tau-tau begitu dirapatkan di rapat judul, ada yang mirip gitu loh dengan yang dibuat dia. Jadi hati-hati jangan terlalu detil. Jadi ada bisa jadi ya. Nggak mau susun-susun tapi itu kemungkinannya selalu ada ya. Ada yang belum punya ide, dosen ngasih tahu ke mahasiswanya ini loh ada yang kayak gini gitu bikin yang mirip mungkin dibedakan objeknya, mungkin dibedakan usernya, mungkin dibedakan apanya gitu loh. Banyak yang seperti itu. Jadi saran saya jangan terlalu detail juga ya. Oke baik bu. Oke baik kalau begitu sudah ya terima kasih semuanya selamat siang terima kasih selamat berhibur ya hati-hati kalau dia berikut sama-sama Bu selamat liburan berhenti Alhamdulillah gua belum lebar Jir Yes Hai kenal primu kapan magang itu no free terus Bro cek kapan pre-opo menesok Senin sakit kenal ku terus selesai Waduh Pak saya masih sakit oleh teriak aduh How? Siap, siap. Siap. Siap. Siap. Siap, siap. Aku tanjukin aja. Iya, iya. Ayo, siap. Ayo, siap. ya udah dikotongnya terjadi pohon Cikgu itu ya 
Summary
# 001_Bu Hesti Summary — Bimbingan User Flow & Use Case


**Tanggal:** Kamis, 2 April 2026  
**Dosen Pembimbing:** Bu Hesti  
**Peserta:** Farchan Deano Muhammad (Can), Dias  
**Topik:** User Flow, Use Case, Revisi Target User


---


## 🎯 KEPUTUSAN PENTING


### 1. Perubahan Target User ⚠️
| Sebelum | Sesudah | Alasan |
|---------|---------|--------|
| SD Kelas 5 (10-11 tahun) | **SMP Kelas 7-9** (13-15 tahun) | Anak SD belum bisa paham logika probabilitas AI & trial-and-error. Perkembangan kognitif belum sampai situ. Terlalu dipaksakan. |


**Quote Bu Hesti:**
> "Kalau untuk kelas 5 mah itu gak sampai di otak mereka itu. Terlalu sulit untuk anak kelas 5 itu. Memahami probabilitas error itu belum ada di otak mereka. Itu paling SMP ke atas ya. Kelas 7 sudah bisa tuh."


---


### 2. Game Mechanics Revisi


#### Intro di Awal
- **WAJIB** ada intro yang jelasin batasan objek yang boleh/tidak boleh digambar
- User harus paham dari awal apa yang diperbolehkan
- Setelah intro, user bisa skip jika sudah paham


#### 3 Kategori Klasifikasi Gambar
1. **Benda Solid** — chair, car, table, house (bisa dipijak, membentuk platform)
2. **Benda Berbahaya/Tajam** — knife, scorpion, crocodile, axe (reset karakter ke awal)
3. **Dekorasi Tembus Pandang** — cloud, sun, rainbow, star (tidak ada efek fisik)


#### Fail Condition
- Jika user menggambar objek berbahaya di level yang tidak membolehkan → **FAIL**
- Jika karakter sentuh objek berbahaya → **RESET ke titik awal**
- Opsi setelah fail:
  - **Revisi:** hapus/ganti objek
  - **Ulangi Level:** start dari awal


#### Level System (3 Level)
| Level | Instruksi | Batasan |
|-------|-----------|---------|
| **Level 1** | Bebas | Semua objek diperbolehkan |
| **Level 2** | Max 3 objek | Batasan jumlah objek |
| **Level 3** | Quest spesifik | "Gambar 1 objek solid + 2 objek berbahaya" |


---


### 3. Use Case Diagram — Split Role


#### Role 1: SISWA (User)
**Apa yang user bisa akses:**
- Lihat intro & aturan
- Pilih level
- Gambar objek di canvas
- Lihat klasifikasi AI (Top-3 + confidence score)
- Putuskan: Accept / Override (masih diragukan)
- Atur posisi objek di arena
- Main game (gerakkan karakter)
- Hadapi fail condition → revisi/ulang
- Evaluasi & refleksi hasil sesi


**Apa yang user TIDAK tahu:**
- Model AI yang berjalan di background
- Log interaksi yang tercatat
- Dashboard analisis
- Database penyimpanan


#### Role 2: GURU (Admin)
**Apa yang admin bisa akses:**
- Kelola sesi pembelajaran (buat sesi, assign siswa)
- View log interaksi semua siswa
- Analisis pola keputusan (Accept vs Override, confidence gap)
- Modifikasi data (edit siswa, hapus sesi, reset progress)
- Export data log (JSON / CSV)


**Apa yang admin TIDAK bisa:**
- Intervensi saat siswa bermain
- Mengubah model AI
- Akses data sensitif di luar konteks pembelajaran


---


### 4. User Flow Chart — Wajib Ada Fail Path


```
┌─────────────────┐
│     START       │
└────────┬────────┘
         ↓
┌─────────────────────────┐
│  Tampil Intro & Aturan  │ ──→ User baca batasan objek
└────────┬────────────────┘    └─→ Skip jika sudah paham
         ↓
┌─────────────────────────┐
│     Pilih Level         │ ──→ Level 1/2/3 dengan instruksi berbeda
└────────┬────────────────┘
         ↓
┌─────────────────────────┐
│   Klik "Tambah Objek"   │
└────────┬────────────────┘
         ↓
┌─────────────────────────┐
│    Gambar di Canvas     │ ──→ User menggambar bebas
└────────┬────────────────┘
         ↓
┌─────────────────────────┐
│   Klasifikasi AI (CNN)  │ ──→ Top-3 prediksi + confidence score
└────────┬────────────────┘
         ↓
┌─────────────────────────┐
│   Putuskan (Accept/     │ ──→ Accept prediksi #1
│        Override)        │ ──→ Pilih prediksi #2/#3
└────────┬────────────────┘ ──→ Override: pilih manual
         ↓
┌─────────────────────────┐
│   Atur Posisi Objek     │ ──→ Drag & drop ke arena
└────────┬────────────────┘
         ↓
┌─────────────────────────┐
│   Ulangi Tambah Objek?  │ ──→ YA → kembali ke "Tambah Objek"
└────────┬────────────────┘    └─→ TIDAK → lanjut
         ↓
┌─────────────────────────┐
│      Klik "Play"        │
└────────┬────────────────┘
         ↓
┌─────────────────────────┐
│    Main Game (WASD)     │ ──→ Kendalikan karakter
└────────┬────────────────┘
         ↓
┌─────────────────────────┐
│  Deteksi Collision?     │
└────────┬────────────────┘
         │
         ├─→ Sentuh Objek Berbahaya ──→ FAIL ──┐
         │                                      ↓
         │                             ┌────────────────┐
         │                             │ Revisi/Ulang?  │
         │                             └────────┬───────┘
         │                                      │
         │                                      ├─→ Revisi → Atur ulang objek
         │                                      └─→ Ulang Level → Start
         │
         └─→ Sentuh Goal ──→ SUCCESS ──→ Evaluasi & Refleksi
                                              ↓
                                     ┌────────────────┐
                                     │ Ulangi Sesi?   │
                                     └────────┬───────┘
                                              │
                                              ├─→ YA → Pilih Level
                                              └─→ TIDAK → END
```


---


### 5. Fitur User Override — Masih Diragukan ⚠️


**Concern Bu Hesti:**
- Khawatir affect model AI jika user bisa override
- Data safety concern (data siswa bisa corrupt model)
- Belum jelas implementasi teknisnya


**Saran:**
> "Dipikir ulang lagi deh itu ya. Kalau masih awal-awal nggak apa-apa dimasukkan, cuman saya kok agak ragu ya."


**Status:** Masih perlu dikaji ulang. Bisa dihapus jika terlalu riskan.


---


### 6. Arsitektur — Masih Dikaji


#### Opsi 1: Full Client-Side (Device Siswa)
**Plus:**
- Tidak tergantung koneksi internet
- Inferensi langsung di browser
- Privasi lebih terjaga (data tidak keluar device)


**Minus:**
- Performance tergantung device siswa
- Model harus di-download dulu


#### Opsi 2: Full Server
**Plus:**
- Performance konsisten
- Model terpusat


**Minus:**
- Dependency tinggi pada koneksi
- Latency karena request-response
- Privasi concern (data dikirim ke server)


**Opsi Hybrid (Yang Mungkin Dipilih):**
- Inferensi di client-side (TensorFlow.js)
- Hanya sync log ke server pusat
- Best of both worlds


**Status:** Masih belum final, perlu dipikir ulang.


---


### 7. Batasan Masalah — Final


| **MASUK** ✅ | **KELUAR** ❌ |
|--------------|---------------|
| Log analysis (confidence score, user choice, interaction status, decision duration) | **Evaluasi dampak psikologis jangka panjang** (terlalu dalam, butuh 1 tahun) |
| Dataset QuickDraw + data user (opsional) | Pre-test / Post-test |
| Client-side architecture (rencana) | AR / Multimodal processing |
| User override (masih diragukan) | Dashboard monitoring real-time |
| Fail condition & revisi path | Deteksi anomali sistem |


**Quote Bu Hesti:**
> "Terlalu jauh itu. Kalau kamu pakai sampai ke situ kamu nggak selesai setahun."


---


### 8. Proposal Submit Pak Hafiz — Jangan Detail


**Yang Diminta:**
1. Rencana penelitian (general)
2. Gap penelitian
3. Metode penelitian
4. Timeline


**Saran Bu Hesti:**
> "Jangan terlalu detail. Jangan sebut tool spesifik (TensorFlow.js, MobileNet, dll) — bisa berubah saat riset. Cukup general aja. Namanya juga masih proposal."


**Contoh yang BENAR:**
- ✅ "Model klasifikasi visual ringan berbasis client-side"
- ✅ "Dataset publik gambar sketsa tangan"
- ✅ "Sistem berbasis web 2D"


**Contoh yang SALAH:**
- ❌ "TensorFlow.js dengan MobileNet V2"
- ❌ "Dataset Quick, Draw! dari Google"
- ❌ "React.js + Canvas API"


---


### 9. Design System — Urutan Pengerjaan


**Bu Hesti Tekankan:**
> "Selesaikan dulu flow usernya. Kalau user flow sudah jelas, kamu akan tahu nanti inputnya ini apa. Ini di prosesnya itu apa yang dilakukan. Terus nanti outputnya bagaimana. Itu aja sih prinsipnya kalau design system. Ada input, ada business, ada output."


**Urutan:**
```
User Flow → Fix → Design System (Input → Process → Output) → Implementasi
```


---


### 10. Split Pekerjaan — Can & Dias


| **Farchan (Can)** | **Dias** |
|-------------------|----------|
| Konten | AI / Computer Vision |
| AR (Augmented Reality) | Heatmap Analysis |
| Virtual Campus | Model Training & Optimization |
| User Flow & Use Case | Log Interaction System |
| UI/UX & Game 2D | Confidence Score Algorithm |


**Catatan:**
- Can tetap riset untuk **kedua bagian**, tapi prioritas utama bagian Can dulu
- Jika ada keputusan teknis yang menyentuh bagian Dias, catat sebagai "perlu dikonfirmasi ke Dias"
- Proposal ditulis untuk **keduanya secara terintegrasi**


---


## ✅ ACTION ITEMS


| Task | Priority | Status | Owner |
|------|----------|--------|-------|
| Buat Use Case Diagram (User vs Admin) | HIGH | ⏳ Pending | Can |
| Buat User Flow Chart (include fail path) | HIGH | ⏳ Pending | Can |
| Adjust target user ke SMP Kelas 7-9 | HIGH | ⏳ Pending | Can |
| Reconsider fitur user override | MEDIUM | ⏳ Pending | Can + Dias |
| Buat proposal general untuk Pak Hafiz | HIGH | ⏳ Pending | Can |
| Lanjut ke Design System setelah user flow fix | MEDIUM | ⏳ Pending | Can |
| Riset arsitektur (client-side vs server) | MEDIUM | ⏳ Pending | Dias |


---


## 📝 CATATAN PENTING


1. **Bu Hesti capable di konsep & development** — bisa konsultasi teknis
2. **Pak Hafiz & Pak Zaka** — hanya ingin tracking topik mahasiswa (jadi jangan terlalu detail)
3. **Penamaan file bimbingan:** `001_bu-hesti-<topik>.md` untuk tracking history
4. **Hati-hati jangan terlalu detail di proposal** — takut ada yang mirip dengan mahasiswa lain
5. **Ini bimbingan pertama dengan Bu Hesti** — next bimbingan update progress dari action items ini


---


## 🔗 LINK KE FILE TERKAIT


- **Use Case Diagram:** `docs/diagrams/use-case_20260402.md`
- **User Flow Chart:** (akan dibuat)
- **Design System:** (pending setelah user flow fix)
- **Proposal General:** `docs/proposal/proposal_v1_20260402.md` (akan dibuat)


---


**END OF SUMMARY**


*File ini dibuat untuk tracking history bimbingan. Update jika ada bimbingan berikutnya.*




Report
# Bimbingan 1 - Bu Hesti: User Flow & Use Case


**Tanggal:** Kamis, 2 April 2026  
**Dosen:** Bu Hesti  
**Peserta:** Farsan, Dias, Bu Hesti


---


## 📋 Perintah Utama dari Bu Hesti


1. **Bikin Use Case Diagram** - Split role User vs Admin
2. **Bikin User Flow Chart** - Dari awal sampai akhir, termasuk kondisi fail
3. **Target user diubah** - Dari SD Kelas 5 → SMP Kelas 7-9
4. **Keep proposal general** - Jangan terlalu detail untuk submit Pak Hafiz


---


## 🔑 Perubahan/Koreksi dari Bu Hesti


### 1. Target User
| Sebelum | Sesudah | Alasan |
|---------|---------|--------|
| SD Kelas 5 (10-11 th) | **SMP Kelas 7-9** (13-15 th) | Anak SD belum bisa paham logika probabilitas AI & trial-and-error. Perkembangan kognitif belum sampai situ. |


### 2. Game Mechanics
- Perlu **intro di awal** yang jelasin batasan apa yang boleh/tidak boleh digambar
- 3 kategori klasifikasi gambar:
  - **Benda solid**
  - **Benda berbahaya/tajam**
  - **Dekorasi tembus pandang**
- Jika user gambar objek berbahaya → **fail**, harus ulang/revisi
- Opsi revisi: tambah, ganti, atau hapus objek


### 3. Use Case Diagram
- Split 2 role: **User** dan **Admin**
- **User:** Fitur apa yang bisa diakses, action apa yang bisa dilakukan
- **Admin:** Dashboard, view log, modifikasi data
- User tidak perlu tahu proses backend (model AI, log, dll)


### 4. User Flow Chart
- Gambarkan flow dari **start → finish**
- Apa yang user lihat pertama kali
- Ada instruksi apa
- Langsung gambar atau pilih level dulu
- **Kondisi fail:** If fail → then what? (retry, revisi, dll)
- Ini akan mempermudah bikin Design System nanti


### 5. Arsitektur (Masih Dikaji)
- **Client-side (device):** Tidak tergantung koneksi, hanya sync log ke server
- **Full server:** Dependency tinggi pada koneksi
- Masih belum final, perlu dipikir ulang


### 6. User Override Feature ⚠️
- Bu Hesti **ragu** dengan fitur user override/correct prediction AI
- Khawatir affect model AI dan data safety
- **Saran:** Dipikir ulang, kalau masih awal-awal nggak apa-apa masukin, tapi hati-hati


### 7. Batasan Masalah
| Masuk | Keluar |
|-------|--------|
| Log analysis (confidence score, user choice, interaction status, decision duration) | **Evaluasi dampak psikologis** (terlalu dalam, butuh 1 tahun) |
| Dataset QuickDraw + data user | |
| Client-side architecture (rencana) | |


### 8. Proposal (Submit Pak Hafiz)
- **Jangan terlalu detail**
- **Jangan sebut tool spesifik** (TensorFlow.js, MobileNet, dll) - bisa berubah saat riset
- Cukup: Rencana penelitian, gap penelitian, metode penelitian, timeline
- Ini masih proposal, bisa berubah nanti


### 9. Design System
- **Urutan:** User Flow dulu → baru Design System
- Design System prinsipnya: **Input → Process → Output**
- Kalau user flow sudah jelas, input/proses/output akan ikut jelas


### 10. Split Pekerjaan
| Farsan | Dias |
|--------|------|
| Konten | AI / Computer Vision |
| AR | Heatmap analysis (bagian gambar yang affect confidence score) |
| Virtual Campus | |


---


## ✅ Action Items


- [ ] Buat **Use Case Diagram** (role: User, Admin)
- [ ] Buat **User Flow Chart** (termasuk fail condition)
- [ ] Adjust target user ke **SMP Kelas 7-9**
- [ ] Reconsider fitur **user override**
- [ ] Buat proposal **general** untuk Pak Hafiz (tidak terlalu detail)
- [ ] Lanjutkan ke **Design System** setelah user flow fix


---


## 📝 Catatan Tambahan


- Bu Hesti lebih capable di **konsep & development**
- Pak Tri Budi lebih ke **proposal** (meskipun agak kebalik)
- Penamaan file: `001_bu-hesti-<topik>.md` untuk tracking history bimbingan
- Ini adalah **bimbingan pertama** dengan Bu Hesti




All Transcript - 16/6/26
Siapa nih yang pake minyak? Saya, soalnya dari tadi pagi. Masuk angin kamu? Enggak. Apa? Minyak angin? Iya. Oh enggak, enggak. Itu minyak apa menurut kamu? Tapi parfum. Oh. [tertawa] Eh minyak angin. Bentar, bentar lagi ganti aja saya Bu. [tertawa] Minyak angin. Nanti kita kasih parfum. Sorry, sorry. [tertawa] Stock ku tak dol aja. Eh Mikis kamu dicariin tadi nggak masuk. Tunggu ya habis ini. Mba Kina, di Pak Aldi soalnya. Yaudah tunggu dulu aja ya. [tertawa] Saya pikir, nih saya cium kayak bau minyak angin ini siapa nih yang lagi sakit? Masuk angin. Aduh ampun. Jadi kesugesti juga saya Bu. Ampun. Oke. Gimana? Ini silau banget sih dari sana. Oke gimana? Jadi permisi untuk kemarin PR dari kami kan, eh ada beberapa yang pertama ini user flow yang dibagi tiga fase. Ya kamu udah split ya? Iya saya udah split. Udah dari Pak, Pak Tibo? Belum. Bapaknya cuma beneran bilang suruh ngumpulin proposal aja jadi nggak sempat ketemu. Yaudah nggak papa. Font-nya digedein. Maksud saya bukan di si-- bukan di saya. Nanti kalau kamu submit ini font-nya kurang, kurang besar nanti dibesarkan font-nya. Siap, Bu. Oke, kamu sudah split. Ya di sini split yang... Ya betul ini dia masuk ke fase ini ya. Dua. Oke. Fase tiga, fase dua. Oke good. Ini apa? Saya nggak bisa baca. Ini level belum selesai. Jadi yang belum selesai dari fase tiga masuk ke fase satu. Oke, oke sip. Jadi saya samain warnanya. Warnanya betul. Harus sama warnanya. Ini dari fase satu tadi yang oren. Buat ngajuin yang nampilin- Gak usah pakai kata from. Oh gitu. Jadi langsung fase satu gitu? Input itu kalau di ini kamu kan paham ya. Input itu harusnya begini dia se, em, begini bukan. Oh iya. Oh berarti dibuat gitu juga ya, Bu? Oh ini kan menunjukkan apa input ya. Terus kalau proses itu kan begini ya. Bener nggak sih? Bener. Kalau ada proses terus kalau, apa sih saya, kok saya lupa sih ini basic banget sih di... Ini input-nya fase satu aja nggak usah pakai from. Terus dia percabangnya coba lihat ke bawah. Ini percabangnya ada yang- Itu paralel ya? Iya. Ya ini decision ya. Iya. Oke. Terus. Jadi kan ada top three itu dipilih nanti jadi label. Nah ini juga nggak bisa gini, ini harus yang kayak gini. End kan. Start dan end-nya kan seperti ini. Oke. Oke. Ya nggak papa sih kalau kamu mau tulis from fase satu to fase three ya terserah. Soalnya biar saya sendiri nggak bingung gitu. Nggak papa. Tapi kamu nggak boleh keliru menggunakan logic, eh shape-nya. Ini logic shape-nya di programming kan harus seperti ini. Oke next yang fase tiganya. Ini untuk fase tiganya. Ini dari fase dua tadi. Objek yang udah digambar masuk ke world-nya terus dari sistem itu nerapin behavior objek apakah objeknya solid, decorative, atau danger. Nah itu ada di sini kalau decorative kurang membantu gitu. Jadi bisa berpeluang balik lagi gambar lagi. Ya balik. He'e. Ya kalau solid ini kan bisa ngebantu misalnya kalau bikin stairs yang kayak tangga gitu. He'e. Kamu lah yang mengerti alamnya ya. Saya cuma mau coba melihat dari sisi ini. Terus turun lagi. Turun lagi, eh jadi bis-- langsung user tuh gerakin stickman-nya buat jalan ngelewatin obstacle-nya. Nah ini gameplay progress-nya nanti apakah ada feedback dari si... User. Iya si user sama si maskotnya gitu. Jadi tiap- Gameplay progress feedback. Apakah ada? Berarti belum tentu ada. Iya tergantung yang dilakuin sama user-nya tapi- Berarti opsi dong. Iya. Opsi di sini decision dong. He'e. Ya kan? Kalau ada dia lanjut ke level berikutnya kan. Kalau enggak dia balik kan. Iya. Ke mana? Ini decision dong ini. Bener? Iya sih kalau dari penjelasan tadi, Bu. Yang kamu jelaskan. Iya yang saya jelasin. Iya berarti ini decision. Kalau yes dia lanjut, kalau enggak dia ke mana? Kalau enggak dia gambar lagi di sini. Lanjut ke- Naik ke? Plus, plus dua nggak sih? Iya balik ke fase dua tadi. Siapa yang fase dua? Nggak ada berarti balik ke fase dua harusnya. Redraw lagi. Nah betul. Kalau decision itu harus ada opsinya. Nggak cuman satu, eh lanjut. Loh ini opsi, ini decision-nya ini opsi kalau yes ya. Dia bisa tiga ini. Ini apa nih saya nggak bisa baca. Override. Ini override. Override. Iya milih dari top three-nya. Oke. Itu decision berarti yang tadi ya. Iya. Oke terus. Terus masuk decision lagi kalau selesai jadi masuk ke apa summary kayak penjelasan di edukasi, dari sisi edukasinya gitu, Bu. Terus- Dalam bentuk apa itu penjelasannya? Penjelasannya dalam bentuk interaktif dengan apa maskotnya tadi. Oh maskotnya ngomong? Maskotnya lah iya. Atau teks? Teks aja sih, Bu. Jadi kita nggak pakai suara gitu. Oh oke. Hearing. Iya kayak bubble gitulah. Oh bubble iya. Bubble muncul teks gitu penjelasannya. Iya. Terus kalau misal levelnya belum selesai, belum level tiga atau gimana dia balik lagi ke fase. Oke. Oke sip. Kurang lebih seperti itu. Untuk interaction matrix kemarin juga sudah kami hilangkan panahnya yang di sini. Hilangkan. Sama di sini. Oke. Terus use case-nya apa bener begini ya, Bu? Soalnya kan dalam satu sistem gini. Jadi di sini- Enggak. Kamu kok nggak paham-paham sih. Use case itu harus ada orang dan harus ada aktivitas. Intinya itu. Ini aktivitas. Nggak begitu tapi.Saya kira kayak di dalam satu kotak ada aktivitasnya apa gitu, terus dari usernya bisa melakukan aktivitas apa gitu bu. Iya tapi enggak flow. Oh. Berarti cuma si usernya ini bisa ngapain gitu. Satu-satu. Jadi jangan menunjukkan flow begini satu persatu gitu loh. Jadi dalam ini, ini ya, ini ya. Nah ini urut, ini aktivitas semua. Aktivitas ya. Masalah dia berurutan atau enggak kita enggak tahu. Ya ini use case. Kemudian sini aktor, aktor itu dalam bentuk begini, stickman. Ini wajib gitu ya. Ini biasanya untuk admin di sisi sini, kalau untuk yang user biasanya kita taruh di sini. Nah ini apakah admin satu, misalkan ini admin satu ya, terus ini mungkin kamu ada dua admin. Admin satu dia melakukan ini, ini ya udah gini gitu loh. Terus usernya dia bisa mengakses aktivitas ini atau gini. Gitu aja nggak ada dalam bentuk flow. Jadi semua aktivitas itu kamu breakdown di sini. Masalah ini lanjutan dari ini, ini lanjut ke sini, itu nggak kelihatan. Kita cuma menunjukkan bahwa admin ini punya akses melakukan ini, melakukan ini, melakukan ini, melakukan ini. Admin ini melakukan ini, melakukan ini, melakukan ini. User melakukan ini, melakukan ini, melakukan ini. Gitu. Berarti kalau stickmannya dibuat kayak gini itu enggak bisa bu? Enggak bisa. Stickman harus seperti ini. Formatnya harus. Format. Fix ini. Bukan saya ngarang. Kamu pasti belajar ini deh waktu di mana ya, ALPRO. Algoritma dan pemrograman. Ini basic ini. Yang kita ingat dari ALPRO cuma ERD, DFD. Iya enggak ada yang kayak gini. Yang ngajarnya siapa? Pak Dwi. Pak Dwi bagus loh. Iya kalau mungkin ada mungkin kita lupa sih. Tapi kita ingat yang paling ingat ya itu tadi ERD. ERD sama DFD. Saya itu yang paling inti Bapaknya selalu menekankan itu. Oke ya ini deh bikin di rumak lagi, bikin yang begini. Jangan bikin macam-macam gini. [tertawa] Tidak dalam bentuk flow ya. Iya kalau dari segi aktivitas ini berarti kayak yang Bu Hesti jelaskan tadi enggak perlu flow tinggal langsung- Betul menunjukkan ini. Iya ini aktivitas kan, aktivitas apa saja yang dilakukan, dan siapa yang bisa mengakses aktivitas ini gitu. Karena tidak semua aktivitas bisa diakses oleh semua role kan. Mungkin kalau super admin semua dia bisa akses. Tapi admin yang biasa saja mungkin admin lokal atau admin apa cuma mungkin terbatas. User juga mungkin apalagi hanya terbatas begitu. Ini contoh role-nya. Saya nggak tahu role kamu ada apa aja kan kamu yang tahu ya. Mungkin cuma satu admin dan satu user nggak masalah. Gitu. Diperbaiki ya. Perbaiki lagi sih. Ya udah. Apa lagi? Terus ini kayaknya dari sisi kita cuma nekanin proses human involved-nya aja dari segi ada di sedikit sistem. Jadi kita kayak ngebedah ini perlu enggak sih Bu untuk ditunjukin. Sebenarnya kami juga agak bingung sih. Enggak perlu. Enggak perlu ya. Jadi kayak ngasih tahu dari sisi manusia- Prosesnya. Kalau kamu mau masukin proposal bisa tapi enggak usah dipresentasikan. Oh untuk sample-nya. Karena terlalu banyak nantinya di proposal. Kalau di proposal masukkan aja enggak apa-apa tapi untuk PPT tidak perlu. PPT itu yang perlu kayak ini metodologi, desain sistem. Izin aja Bu untuk desain sistemnya itu kan karena kita satu proyek apakah perlu desain sistem- Dibedakan gitu. Iya betul. Berarti ada yang global. Jadi desain sistem itu kan ini ya secara keseluruhan ya. Nah di dalamnya kan ada berapa, ada berapa ya. Nah kamu kasih tahu tanda mungkin bisa dibedakan menurut warna mana yang kamu kerjakan mana yang kamu kerjakan. Dibedakan aja terus di bawahnya kasih keterangan warna ini, ini pekerjaan saya warna ini pekerjaan ini. Berarti bukan dibuat kayak- Jadi dua. Jadi dua gitu. Enggak usah, ribet. Malah nanti enggak kelihatan kalau yang kalian kerjakan itu satu sistem yang besar kalau di-split. Jadi satu sistemnya aja di sini tapi kamu di dalamnya udah ngasih tahu yang pekerjaan saya ini. Nah kecuali kalau misalkan ya ini satu sistem kan desain sistem itu kan ini input, ini proses, ini output. Di dalam input ini misalkan ini kerjanya Pak Ardan, ini kerjanya Diaz. Ternyata di sini ada hal lain yang perlu kamu jelaskan lebih detail kamu bisa tarik bikin desain sistem yang versi kamu sendiri. Tapi menurut saya ini tetap akan kalau di awal enggak perlu seperti inilah. Mungkin sambil jalan. Kalau untuk masih proposal ini secara keseluruhan saja dulu nanti kamu bedakan menurut warna atau dikasih kotak ini punya saya tapi menurut saya ribet menurut saya main di warna. Dibedakan warnanya saja. Main warna yang paling enak. Oke. Gitu. Nanti yang mahal. Enggak masalah. Enggak usah. Nanti kalau misalkan progress nah itu baru. Silakan progress. Baru kamu breakdown lagi. Dirincikan lagi. Breakdown punya kamu sama punya kamu ini bisa. Tapi kalau untuk proposal secara garis besar ini sudah cukup. Hei! Tumben kapan lari? Nanti lari. Aku sudah mau lari kalau anak-anak sudah beres semua. [tertawa] Tiap hari Bu lari saya. Lari ke mana? Dari kenyataan. [tertawa] Janganlah. Enggak perlu itu. Kita hadapi kenyataan. Udah lari. Iya iya iya. Aku sudah mau lari setelah anak-anak ini libur kan habis ini libur ya. Kok nunggu libur? Enggak ada waktu Bu. Ada. Ibu pulangnya jam berapa? Saya pulangnya sih cepat tapi sampai rumah masuk zoom lagi masuk ini lagi buka laptop lagi. Pak Agus juga gitu. Kadang malam lagi. Saya Sabtu Minggu, saya Sabtu pagi. Kalau Sabtu pagi mungkin bisa ya. Sabtu pagi gimana?Jumat malam sore malam gak mesti kadang di Koni kadang di jalan raya itu yang dekat rumah Ibu itu Iya Itu kan kalau muter kalau muter sampai Taman Flora balik lagi ke rumah kan sepuluh kilometer loh Sabtu jam berapa Bu? Sabtu pagi Bu saya jam lima habis sholat subuh langsung lari Enaknya tidur tuh. Nikmatnya Saya kira Masya Allah saya juga gak apa-apa sih Ibu saya jemput ah saya jemput ke rumah nanti anu sampai di gate nya residen saya permisi saya mau jemput Maya Bu paling jaman security-nya telepon dulu. Lima puluh aja Bu Jam lima pagi Oh my God Tapi gak panas Bu jam segitu Bener bener bener kalau sudah di atas di atas jam enam itu sudah mulai ini matahari saya juga nggak mau panas Bu Kalau saya kalau latihan kan di rumah dulu ya tapi kalau Sabtu Minggu itu kan kita karena longgar ya sepuluh, sepuluh lima, gak mesti kadang saya tujuh, delapan Yang penting gak kena panas matahari Bu Pasti nanti ending-endingnya jam enam kan sudah mulai ini ya tapi kan enggak terik Bu maksudnya itu Iya iya iya Kalau terik itu Bu saya paling satu kilo saya minum satu kilo minum Iya iya Saya mesti bawa air yang Iya iya. Bawa ransel ndak Bu? Ndak kadang bawa rompi kadang bawa Oh rompi Tali pinggang tapi ada airnya Nah itu repot juga lari sambil bawa beban Bu Airnya cuma airnya gak berat Bu gak sampai gak sampai air botol itu Bu botol itu lubunya kecil Bu Kayak gini dua liter Iya kalau saya niat maksudnya harus banget niat saya berhenti di Indomaret Alfamart Oh beli ya Oh berarti yang penting bawa duit mending bawa duit kamar kecil bawa duit lebih ringan daripada bawa botol minum Gak bawa duit Bu saya bawa HP Oh bawa HP ya Bawa smartwatch nanti kan bisa nyekel Oh oke oke oke. Saya niatnya ada sih Bu Itu sudah dicatat Bu kalau di agama Islam niat itu sudah dicatat Niat sudah ada, kemam apa ke kemampuannya yang belum ya, kemampuannya yang belum ya Ayo Bu mumpung lagi ini Iya iya nanti kalau semangatnya muncul Musim hujan malah nggak enak lari Iya iya benar benar benar. Ini tumben Wan Ri, Pak Agus Iya saya mahasiswa MMJ sama TRN Untuk? Ngisi survei Bu survei yang itu loh PPID saya kan dipindah ke PPID. Saya kan sudah tidak di UMAS Pak, saya pindah ke PPID. Nah di PPID itu saya mau start memperbaiki konten dan lain sebagainya informasinya kemasannya semua itu mau saya perbaiki Mana surveinya Bu? Mana surveinya? Surveinya sudah saya share di grup Grup mana? Kalau yang di apa Prodi ya Kalau yang di ini saya nge-share-nya ke tertentu karena sesuai list yang ada di grup. Saya dosen itu yang menjabat menjabat itu loh Bu Oh prodi ya. Oh berarti sudah dapat dari mahasiswa sudah ya? Ya sudah. Tapi saya berharapnya memang yang karyawan dan dosennya kurang Bu isinya. Padahal Bu saya sampai ke Ibu mau ngisi tak share ya? Boleh ndak ada sini kita Iya iya Kita nggak dapat. Boleh. Oh berarti bukan cuma mahasiswa Iya harapannya itu yang masukannya banyak itu kan mahasiswa kenapa? Karena penerima layanan Iya yang meracak kan Terbesar itu kan ya mahasiswa yang jumlah mahasiswanya paling besar. Nah cuma kemarin saya bagikan linknya itu saya bagikan melalui adik-adik BEM sama HIMA. Nah ini tadi mana loh katanya nggak tahu. Berarti kan ada sesuatu kok nggak nyampe Nggak nyampe berarti. Iya. Kalian ada yang ngisi survei? Survei gimana Bu? Kayaknya nggak nyampe deh. TRN TRN tadi temannya juga baru aku, aku loh di atas nunggu mereka keluar demo mereka selesai demo tak kasih survei tak apa tak jelaskan Oh bukan dalam bentuk link Karena bukan link yang saya bagi Bu karena kadang saya kasih link mereka tidak langsung mengisi Oh. Iya ndak apa-apa Bu Iya nggak apa-apa kalau mau link tapi diisi beneran loh ya jangan boak loh. Saya bagi Bu anak-anak itu iya Bu nanti saya bagi ke kelas Nggak dikerjain Saya bilang Mbak kalau bisa dua hari ya jangan lama-lama iya Bu dua hari kemudian saya cek tetap aja yang ngisi delapan puluh orang Nggak nggak nambah Iya nggak nambah. Kan kayak kayak Nggak nyampe Bu. Iya oh kalau link begitu sih ya. Iya ya. Eh saya kalau share link ke kalian itu kalian isi nggak? Iya Bu iya Bu iya Bu Kalau saya ini sih Bu jarang sih memang kalau misalnya Kadang isi kadang enggak Kadangan ketimpa gitu ketiduran Itu butuh banget loh kayak gitu gitu Ke depannya sendiri Pak Di-share ya Bu ya. Wan Ri ngapain buka sepatu? Di sini enggak, enggak bukan di lab. Enggak kok Bu nggak apa-apa. Ya udah apa lagi yang behavior Ini kayaknya redundant sama yang tadi nih Hampir mirip sama yang di atas Jadi mirip kayak inilah kayak Ah nggak usah kalian hobi banget sih bikin ginian ginian Nggak tahu ya Nggak usah gitu. Nah ini mode gamenya kamu ini kayak apa bentuknya? Mode gamenya nanti kita sebentar Bu mungkin saya kasih apa wireframenya ya sekalian. Mana ya? Itu templateMana banyak banget. Mock up nya aja bu. Iya. Iya. Gak ada lagi nih. Ini sih dia. Jadi kurang lebih kayak gini. Oh kamu udah pernah nunjukin ini ya? Iya. Jadi nanti gamenya ini gak, gak tentu kayak gini mungkin di bawahnya ada kayak duri. Nah, itu duri gimana ya bu, apakah boleh? Duri? Iya biar gagal gitu. Jadi secara- Menggagalkan usernya itu. Bentuk apa durinya? Mungkin cuma garis-garis tajam gini dong. Gak apa-apa sih. Kayaknya gak apa-apa. Soalnya user dengan- Daripada pisau atau apa. Duri. Duri ya ya udah lebih soft ya. Iya. Oh oke ya udah nggak apa-apa. Tapi dia tahu itu duri? Harusnya terlihat duri. Iya. Dari visualnya kan udah gitu. Tajam gitu. Atau mungkin nanti bisa diperjelas lagi sama maskotnya gitu. Mungkin he eh. Oh jadi kayak berarti tiap level kita harus kasih tutorialnya gitu bu. Sama pantangan-pantangan yang nggak boleh dilanggar. Menurut saya ya supaya lebih jelas ya. Sama biar maskotnya berguna gitu. Iya kalau nggak dia ngapain ada di situ kan. NPC. Ya nggak apa-apa dikasih aja gitu. Oke ada lagi? Kurang lebih kayak gitu sih bu. Nanti kan gambar terus ditebak di sini. Nah, sekalian nanya juga sih bu untuk maskotnya. Eh saya balik lagi ke tadi yang kamu mau berikan, eh apa namanya informasi untuk gamenya itu jangan sampai itu mengguide mereka untuk mengerjakan game karena jadinya nanti nggak ada gunanya kamu bikin game kalau mereka sudah tahu step by step. General ya. Betul kak bisa. General. Iya. Berarti kalau misal dibuat yang di level pertama itu kita ada guidenya buat ngerjain game terus semakin bertambahnya level itu guidenya kita kurangi. Iya bisa, bisa seperti itu. Soalnya ini sih bu masih bingung apakah di level itu harus ada prompt kayak gambar apa gitu apa nggak perlu ya? Itu kalian yang tahu. Saya kan nggak tahu kalian membagi tingkat kesulitan per levelnya itu seperti apa. Oh gitu ya bu. Iya nggak apa-apa. Yang pasti di bagian level satu itu harus semudah mungkin. Nah, makin naik baru makin sulit. Kalian kurangi clue-nya lah atau tambah tingkat kesulitannya atau apa gitu. Pokoknya makin naik nanti pasti makin sulit. Kalian yang paham itu. Dari segi game sih ada lagi. Dari sisi game. Oh iya level sih bu kan kita rencananya cuma tiga level aja karena dari klaim judul saya juga bukan game tapi saya narasin simulasi interaktif berlevel gitu karena fokusnya ke memory education. Nah, itu apakah kita tetap perlu nambah level sampai berapa atau cukup tiga ini. Tiga udah banyak loh. Iya. Oh iya sih sepuluh menit gitu ya. Itu banyak. Saya biasanya dua aja udah oke. Tapi kalau digeser sampai tiga mungkin singkat-singkat ya. Iya. Singkat-singkat. Satu level berapa lama? Satu level kalau level satu harusnya gampang mungkin dua menit. Semakin bertambah level semakin dikurangi durasinya. Oh berarti semakin tinggi semakin cepat. Iya. Harusnya cepat. Semakin tinggi semakin cepat. Kan level satu gampang. Iya. Level satu gampang. Iya semakin cepat. Semakin cepat. Semakin tinggi semakin lama. Iya dong. Semakin- Tak menantang. Nah, itu kalian pikirkan. Itu kalian pikirkan ya. Jadi pikirkan dari sisi usernya bagaimana. Nah, untuk itu kelanjutannya apakah kita diskusi lagi ke bosnya atau langsung kita jadiin. Nggak usah. Ini masih bisa berubah. Oh gitu ya. Nanti pelaksanaannya paling masih bisa berubah. Yang dilanjutkan di sidang proposal itu. Iya. Karena kamu dapat masukan nanti. Ya siapa tahu dibilang ini nggak perlu ini nggak perlu. Tapi nggak begitu sih. Sidang progres itu sebenarnya, eh sidang proposal itu cuman mengecek, eh kamu sudah sampai sejauh mana menyiapkan eh TAKM ini. Mock up ada, terus user flow ada, use case ada ya. Terus kalau bisa ada demo. Sudah ada demo untuk gamenya belum? Belum. Masih belum. Demo apa yang sudah ada? Sejauh ini masih kami bikin konsep desain dari keseluruhan aplikasinya dan baru wireframe ini sih bu. Ini baru UI yang beberapa aja. Sama pak Tri Budi nggak ditarget? Nggak. Nggak. Ya udah gini aja dulu maju. Metodologi kamu mana? Metodologi itu masih belum. Iya belum bu. Harusnya dari situ. Metodologi itu harus muncul. Coba tanya orang sebelah metodologinya gimana. Ya jadi metodologi itu kan biasanya misalkan dibagi fase satu, fase dua, fase tiga ya. Anak-anak suka bagi gitu karena kan tiga kali ujian ya. Fase satu itu sudah selesai semua di metodologi. Ada studi literatur, terus ada analisis apa kebutuhan pengguna gitu ya dan segala macam. Itu sudah harus kelihatan di metodologi, eh di sini. Nah, kamu bikin dulu tuh metodologi kamu gimana. Masa sudah sejauh ini nggak ada metodologi sih. Soalnya kami masih mikir mau bikin apa yang dulu gitu. Harusnya metodologi dulu. Oh gitu. Iya biar metodologi itu akan lebih terstruktur. Untuk sampai ke akhir itu metodologinya gimana. Coba lihat yang tadi barusan saya benerin itu, Supa. Coba lihat punya Supa. Itu udah proposalnya. Udah beres cuma masih saya benerin tadi.Nanti kalau sempat juga ini Pak Tribudi katanya bisa sih. Kita langsung diskusikan juga sama Pak Tribudi. Gitu sih Bu. Yaudah oke. Sama kamu lanjut ya. Ini yang buat yang objeknya itu kan kayak ada tiga yang solid, danger sama dekoratif. Nah itu yang dekoratif kan kayak fungsinya itu kurang gitu. Nah kita itu masih bingung itu ditaruh apa nggak. Apa harus di-research lagi ya Bu untuk dekoratif itu keperluannya atau gimana? Solid. Danger sama dekoratif. Danger yang bahaya tadi kayak misal duri atau pisau gitu yang- Yang berbahaya lah. Kalau dekoratif itu lebih kepada apa? Misalnya kayak gambar awan gitu dia tembus. Jadi kayak nggak seberapa ngaruh gitu. Semuanya tembus sih kalau misalnya gambar bunga atau gambar apa. Kalau solid? Kalau solid dia bisa dipijak atau didorong. Pertanyaan kamu tadi apa? Nah itu kan yang dekoratif itu kayak fungsinya kurang gitu Bu. Nah itu- Estetika. Maksudnya di gamenya itu jadi kita tambahin yang dekoratif itu apa cuma dua yang solid sama danger itu? Yang ada yang sudah fix ada ininya kan fungsinya yang solid sama yang danger. Kalau dekoratif menyusul kali ya. Kalau kamu belum tahu konsepnya mau bagaimana nggak usah dimasukkan. Berarti sementara yang dimasukkan cuma danger sama yang solid aja. Iya yang kamu sudah paham konsepnya. Kalau masih ragu mendingan jangan. Karena ini sambil jalan bisa bertambah. Kalau kamu rasa oh bisa nih akhirnya menemukan konsep untuk dekoratif fungsinya buat apa. Tuh nah itu ditambah kan. Oke sudah? Ini sebelum ke bagian data teknisnya. Saya mau nanya berarti untuk kan ini saya bawa atau mockup tadi ya. Itu ke seminar nanti SPPA. Itu kalau maskotnya juga apakah saya bawa desainnya keseluruhan yang udah jadi atau saya frame bentuknya dulu? Iya makanya kamu perlu desain metodologi. Karena di metodologi itu nanti kelihatan yang sudah kamu kelihatan yang kamu kerjakan apa yang belum apa gitu. Nah kayak desain maskot itu di tahap awal di fase pertama. Maskot, mockup, terus kenapa sampai bikin ini. Terus juga latar belakangnya bagaimana ya. Itu sebenarnya perlu. Bikin fishbone-nya. Fishbone iya. Kamu bikin fishbone-nya. Supaya bisa kelihatan urut-urutan tahapannya itu bagaimana. Coba yang punyanya Supa deh. Dari saya cukup. Silakan dilanjut. Ini untuk sistem arsitektur sementara dari kami yang general yang belum diklasifikasikan berdasarkan warna. Betul ini kamu harus split ya. Jadi nggak bisa seperti ini. Ini siapa yang ngerjain ya apa? Siapa yang mengerjakan apa? Itu masih belum ada di sini. Soalnya ini memang masih keseluruhannya. Coba dibuat seperti ini tapi kalian kasih perbedaannya. Mana yang bagian kamu mana yang bagian ini gitu ya. Mungkin dalam bentuk warna. Ya. Yaudah gitu aja. Itu untuk dari- Dari sisi back end-nya. Kamu yang ngerjain ya? Iya. Nah ini buat entry front end-nya terus masuk ke back end-nya itu pakai payload dari JSON-nya gitu. Terus nanti divalidasi payload-nya itu udah bener semua apa ada yang masih berantakan gitu. Kalau masih berantakan bisa diulang lagi dari awal. Store apa itu? Ini buat databasenya. Storage SQLite. Untuk databasenya. Itu habis dari sini tuh datanya semua masuk ke admin dashboard terus bisa didownload jadi Excel gitu. Terus diklasifikasikan lagi di cluster. Jadi yang di bawah ini yang clusteringnya itu. Jadi kemarin yang masih bingung clusteringnya itu jadinya ini clusteringnya. Jadi kita kelompokin mana kelas yang kritis dan mana yang enggak. Kenapa harus berdasarkan itu? Apanya? Kritis dan enggak kritis. Bukan kritis lebih ke percaya. Percaya AI-nya apa enggak gitu. Iya, iya. Oh lebih percaya AI-nya atau enggak gitu. Oke. Dalam satu kelas itu berapa yang ternyata lebih sering percaya AI langsung. Dan mana yang- Ya sering koreksi atau- Outputnya nanti berupa apa itu? Percaya atau enggak gitu. Ini artinya kamu pikir berupa kesimpulan gitu gimana sih? Apa lebih jadi kayak misal- Pak Tribudi ada request nggak? Kalau kesimpulan kan kualitatif tuh. Oh iya ya. Ya nggak sih? Atau data angka. Kesimpulan jadinya. Kesimpulan dimulai kan dari data ya. Mungkin lebih banyak. Kamu menganalisa nggak? Kan keluar angka tuh hasilnya kan ya. Berapa yang percaya berapa yang nggak gitu ya. Nah itu kamu analisa kan? Iya. Keluar analisanya? Keluar nanti di hasilnya gitu. Kualitatif berarti. Narasi. Harusnya iya. Narasi. Ya yang kami pikir iya sih untuk hasilnya narasi karena dari data log yang matrix itu karena hasil coba user semua. Apa ya, matrix yang ada di admin itu kan itu semua hasil dari user nyobain. Nah, itu kami mikirnya hasilnya berupa kalimat ya sih. Ya kan? Matrix pun itu sebenarnya hasil kan output ya. Matriks hasil ya tapi jangan berhenti di situ harus ada analisa terhadap matriknya itu. Nah itu berarti-- Kalimat. Kalau kalimat tadi jadinya kualitatif. Matriksnya itu yang kuantitatif. Oh gitu. Matrik angka kan. Matriksnya itu yang kuantitatif yang kualitatif penjelasan terhadap matriknya itu. Nah pertanyaan saya penjelasan terhadap matriknya itu auto generate. AI. AI. AI. Panggil API. API-nya. API-nya dia auto generate. Dia langsung baca gitu loh ini apa. Gimana dia. Gitu caranya. Harus auto. Nambah lagi. Iya. Ada Gemini API free di Google. Betul. Tapi limit. Banyak. Banyak banget. Fuad. Oh iya sih, Mas Fuad ya. Fuad itu. Dia men-generate hasil dari segala macam itu dari entah berapa AI-nya dia pakai ya. Coba deh. Mas Fuad itu oh berarti nanti saya tanyakan detailnya ya Bu apakah beli atau enggak. Cuma seingat saya dia dari awal itu nggak masalah sih dia dari awal itu kualitatif terus, terus, terus sampai selesai. Jadi dia nggak ada data dalam bentuk matriks. Tapi menurut saya secara konsep harusnya bisa sama dengan yang kalian punya gitu kan. Jadi AI-nya menganalisa data matrix-nya ini apa. Kalau si Fuad itu menganalisa hasil dari input-input yang dimasukkan oleh usernya dia. Ada miripnya sih. Bisalah. Oke? API-nya di mana coba jelaskan. Iya. Nge-prompt AI-nya mau. Gampang sih itu. Bikin prompt dari prompt. Gampang itu. Gimana nge-prompt-nya kamu? Bikin prompt dari AI. Bikin prompt dari AI gitu. Ada ini untuk yang di- Dashboard-nya. Ini untuk flow-nya aja sih Bu. Jadi adminnya cuma bisa buka dashboard-nya langsung lihat session list tadi siapa aja yang udah berapa yang udah karena kita rencana nggak pakai login sih Bu. Jadi kayak session- Cuma session ID doang. Dia nggak bisa nge-save. Enggak. Enggak. Dia harus menyelesaikan ketika dia main satu ses-- eh satu ini. Satu apa sequence satu sesi. Dia nggak boleh berhenti tengah-tengah ya. Kalau prosesnya itu kalau misal prosesnya itu berhenti di tengah-tengah maka dia itu dihapus langsung. Terhapus. Iya datanya itu terhapus. Berarti ketika dia mau coba lagi dia mulai dari nol lagi. Iya. Ya ada plus minusnya sih. Plusnya kerjaan kamu nggak berat kalau kayak gitu. Iya karena nggak perlu numpang ke server mana buat naruh data gitu kan ya. Dari sisi kalian mudah. Dari sisi usernya yang nggak enak. Mulai dari awal. Cuma pertanyaan saya gini kalian sudah pernah membayangkan satu user itu untuk menyelesaikan semuanya berapa lama? Kalau tiga puluh menit itu cukup lama dia harus ada kesempatan untuk bisa berhenti di tengah-tengah. Artinya kamu harus kesempatan-- kasih kesempatan dia bisa save yang sudah dia kerjakan kalau tiga puluh menit. Kalau cuma sepuluh menit ya udah nggak apa-apa nggak pakai login. Berarti kalau misal bisa save gitu harus pakai login. Iya kalau dia butuh nge-save. Kan ada di awal ada yang kita di awal ada yang bangunin maskotnya gitu Bu yang waving hand kan itu maskotnya bangun ditanyain. Sempat kepikiran sih dari saya dibangun nanyain pernah udah pernah ke sini atau belum gitu. Kalau waving lagi. Nah itu. Pakai ID dong. Nah iya itu itu apakah- Berarti dia harus bisa ada history kalau dia sudah pernah atau belum. Login. Mending pakai login. Login dah. Iya. Harus ada history kalau memang skenarionya seperti itu. Iya. Harus ada history. Dia bisa membaca history-nya si user yang sama. Gampang itu coba tanya Fuad. Fuad itu ruwet banget punya dia tapi bisa gitu loh mendeteksi ini sudah ini. Bisa dia. History-nya. Bisa. Bisa bisa bisa. Kalau loginnya gitu kalau pakai kayak- ID SN. ID SN. Oh mau nge-host ke mana servernya apa segala macam banyak yang gratis. Kita kebetulan udah izin ini sih Bu buat pakai servernya. PRM? Iya. Oh ya udah bagus malah. Siapa yang ngasih izin? Pak Hafiz. Soalnya dari Mbak Tri Budi suruh minta Bapak Rodi langsung. Bagus bagus bagus. Tapi Pak Afrodit buat suruh nanya Pak Doto itu gimana. Karena memang yang handle Pak Doto. Tapi pas saya tanya lagi kalau kata Mbak Tri Budi izinnya ke Pak Afrodit sih. Terus Pak Hafiz bilang ya udah pakai aja. Berarti bisa dipakai. Bisa semuanya pakai cuman memang akan ada kendala kalau mau akses. Coba tanya Faza. Faza itu kan pakai itu. Nah kemarin itu dia tetap nggak boleh ya memang wajar nggak boleh pegang server langsung. Jadi dia kendalanya adalah kalau mau pakai harus ngontak anak buahnya Pak Doto. Oh gitu. Kok setahu saya saya juga sering ngobrol sama Mbak Faza sih Bu buat setup server karena sempat kepikiran buat servernya. Itu Mbak Faza katanya cuma bilang ke iniAnaknya punya Pak Doto, Ridho. Oh iya habis bilang Mas Ridho. Bilangnya ke aslab-aslabnya Pak Hafiz gitu? Gak tahu lagi. Aslab-aslab yang mahasiswa itu. Oh nggak tahu lagi kalau itu. Setahu saya fasya itu selalu harus kontak Ridho supaya bisa ini. Cuman nggak tahu setelah itu bagaimana lagi deh. Coba ngobrol aja tanya deh gimana. Udah Bu, nggak masalah. Tapi kalau Pak Hafiz sudah bilang oke harusnya sih nggak masalah. Oke? TFJS. TFJS. Apa? Perlu didiskusikan yang modelnya jadinya. Jadi modelnya itu kan awalnya dari- Python. Iya dari Python terus hasil trainingnya itu formatnya keras gitu. Apa format keras? Nah itu kayak format filenya. Nah itu kan masih berat gitu. Terus kita ubah jadi JSON. Iya JSON baru JavaScript itu kan TensorFlow kan cuma pakai ini loh. Meng-convert gitu kan. Eh itu hal teknis yang harus kalian selesaikan bukan saya yang mikir. Iya dong. Diskusi Pak Tri. Enggak dengan Pak Tri juga kamu nggak mau. Itu kamu, kamu kalau dikasih jawabannya kamu ngapain? Gitu. Bisa dijawab ini nggak sih? Iya kalau udah, kalau udah dikasih tahu dosen terus kamu ngapain dong? Kamu harus cari tahu sendiri tuh. Sedih, sedih. [tertawa] Yang kayak gitu gitu. Anak tikus kopi. Ada banyak hal-hal teknis ya yang harusnya kalian solve sendiri ketika kalian ini running gitu kan ya. Karena kita kan nggak running, dosen kan nggak running gitu. Jadi kalau kayak gitu-gitu tuh keluarnya begini berat atau enggak gitu kan, kan kita nggak lihat gitu, kita nggak experience dan nggak, nggak mengerjakan. Kamu tanya Pak Tribudi juga paling diketawain kamu. [tertawa] Diketawain. Diketawain kamu. Berarti ini sih kalau teknis. Iya sudah. Ya udah gitu ya. Oke? Kebetulan juga cukup sih Bu dari kami sudah selesai. Terima kasih. Kamu jisismu sidang tanggal delapan belas ya? Iya delapan belas. Kamis. Iya sama ini juga. Kita mau nanya tentang yang lembar pengesahan. Mana yang harus ditandatangani? Sudah ditandatangan Pak Tribudi? Itu rencananya habis ini- Kalau Pak Tribudi tanda tangan bawa ke saya. Saya maksimal sampai jam tiga di sini ya. Oke Bu. Ya sampai jam tiga. Oke? Ya udah. Saya cari Pak Tribudi dulu. Selamat siang.
Summarize - 16/6/26
Ini rangkuman linear hasil bimbingan Bu Hesti barusan — saya buang obrolan minyak angin dan lari pagi, ambil yang penting buat proposal:
1. User Flow (3 Fase)
* Sudah benar di-split 3 fase, font digedein pas submit
* Warna harus konsisten antar fase (fase 1 = oren, dst)
* Shape flowchart jangan salah: input = jajaran genjang, proses = persegi panjang, decision = belah ketupat, start/end = oval. Jangan tulis "from fase 1"
* Fase 3: objek yang digambar masuk world → sistem kasih behavior (solid/decorative/danger). Kalau decorative → balik gambar lagi
* Gameplay progress feedback itu decision, bukan proses lurus. Kalau yes → level next, kalau no → balik ke fase 2 redraw
* Override = decision dari Top-3
2. Edukasi / Maskot
* Penjelasan akhir level pakai bubble teks maskot, tanpa suara
* Tutorial level 1 harus ada, level 2-3 kurangi clue. Jangan guide step-by-step, nanti gamenya jadi tidak berguna
3. Use Case
* SALAH total yang kemarin. Use case bukan flow.
* Harus ada aktor (stick figure) di kiri, aktivitas di kanan. Satu kotak = satu aktivitas, tidak urut
* Stickman formatnya fix seperti di ALPRO, bukan gambar bebas
* Tunjukkan siapa bisa akses apa (admin vs user)
4. Desain Sistem
* Jangan di-split jadi dua. Satu sistem besar, bedakan pekerjaan kamu dan Diaz pakai warna
* Dekoratif: kalau masih ragu fungsinya, buang dulu. Pakai solid dan danger saja. Bisa ditambah sambil jalan
* Buat fishbone dan metodologi (fase 1 studi literatur, fase 2 analisis, fase 3 implementasi). Ini wajib untuk proposal
5. Teknis
* Backend: payload JSON → validasi → SQLite → admin dashboard → export Excel
* Clustering: kelompokkan "percaya AI" vs "koreksi AI"
* Output: matriks = kuantitatif, narasi = kualitatif. Narasi harus auto-generate pakai Gemini API (tanya Mas Fuad)
* Session: wajib login, jangan session ID saja. User butuh history kalau pernah main (30 menit terlalu lama untuk sekali jalan)
* Server: pakai PRM sudah izin Pak Hafiz, tapi akses harus lewat Ridho (anak buah Pak Doto)
* TFJS: convert model Python → JSON, kerjakan sendiri, jangan tanya Pak Tri
6. Sidang 18 Juni
* Yang dicek: mockup, user flow, use case, metodologi, kalau bisa demo
* 3 level cukup, jangan tambah. Level 1 = 2 menit, level makin tinggi makin menantang (bukan makin cepat)
* Lembar pengesahan: minta tanda tangan Pak Tribudi dulu, baru ke Bu Hesti maksimal jam 3 sore hari ini
Intinya Bu Hesti: perbaiki shape flowchart, betulkan use case, buat metodologi + fishbone, bedakan kerjaan pakai warna, dan jangan pamer proses human-involved di PPT.




20/04/26


Claude ver.
Catatan Diskusi PA (Proyek Akhir) dengan Bu Hesti
Topik: Interactive Human-in-the-Loop AI Playground for Elementary School Students
Peserta: Can (Mahasiswa), Bu Hesti (Dosen Pembimbing)
Status: SPPA (Seminar Proposal Proyek Akhir)
________________


1. Klarifikasi Problem Statement vs Background
Bu Hesti:
"Bukan yang melatar belakang. Itu dua hal yang berbeda dan mahasiswa masih suka kebalik. Jadi permasalahan itu adalah yang mau kamu kerjakan itu apa."
Key Point: Problem statement harus fokus pada solusi yang ingin dicapai, bukan sekadar background.
________________


2. Target User & Scope
Can:
Awalnya sistem ini dirancang untuk siswa SD, tapi sedang dikomunikasikan dengan Pak Trikudi untuk menjadi SMP karena ada perubahan scope.
Tujuan Utama:
Mengedukasi siswa SMP bahwa automation bias itu nyata — mereka sering menganggap semua bisa di-generate otomatis. PA ini akan menunjukkan cara kerja AI dengan cara yang interaktif dan gamified, sehingga mereka paham bahwa AI memiliki pilihan seperti manusia.
________________


3. Tiga Pilar Utama Sistem
3.1 Interaksi
* Harus smooth dan tidak kaku (berbeda dari produk biasa yang hanya punya button & tombol)
* Menggunakan computer vision untuk membuat interaksi natural
* Target user adalah SMP, jadi design harus sesuai dengan preferensi mereka
3.2 Edukasi
* Bukan hanya sekadar interaksi, harus ada perubahan pemahaman
* Siswa harus memahami cara kerja AI melalui gameplay
* Ada batasan tertentu agar edukasi tercapai tanpa overload
3.3 Game Mechanics
* Sistem gamified untuk membuat pembelajaran lebih engaging
* Interaksi yang banyak dan variatif perlu dipikirkan dengan matang
Bu Hesti:
"Kamu sudah bisa mulai mendesain interaksi apa saja yang mau kamu masukkan. Karena banyak interaksi itu ya. Dan yang penting, interaksi itu harus cocok dengan target user (anak SMP), bukan hanya dengan preferensi developer."
________________


4. Konsep Mascot & Visual Theme
Can:
Mascot yang direncanakan adalah:
* Narasi visual dengan stickman sebagai karakter utama
* Theme: Space/Angkasa
* Mascot akan membantu stickman mencapai tujuan (naratif pemandu)
* Konsep visual: immersive space dengan planet-planet
Flow Visual:
* User melihat background angkasa
* Berpindah dari planet satu ke planet lain sebagai progression
* Mascot floating di sekitar, memberikan guidance
Placement Mascot:
Mascot akan bergerak/berpindah sesuai dengan kondisi gameplay. Ketika user mengambil/menyelesaikan sesuatu, mascot otomatis berpindah posisi.
________________


5. User Flow & Onboarding
5.1 First-Time User Flow
Can: Ketika user masuk pertama kali:
1. Intro/rules diberikan oleh mascot (sebagai game master)
2. User diarahkan ke tutorial dengan 3 level
3. Ada tombol untuk lanjut (thumbs up / confirm)
4. Jika tidak paham, ada opsi untuk melihat penjelasan ulang
Bu Hesti:
"User flow yang harus dibuat sampai selesai. Nanti kita lihat di tahap mana kamu bisa mulai implementasi."
Pertanyaan yang perlu dijawab dalam flow:
* Apa yang pertama kali user lihat setelah login?
* Harus lihat materi dulu atau langsung main?
* Apakah harus mengumpulkan sesuatu sebelum bermain?
* Flow seperti apa dari awal sampai selesai?
5.2 Returning User
Jika user bukan first-time:
* Mereka bisa skip intro/tutorial (jika sudah paham)
* Atau jika belum paham level 1, tetap harus mulai dari level 1
* Sistem mendeteksi "first time" via user choice confirmation
Mekanisme Deteksi: Bu Hesti bertanya: "Tapi kamu tahu dari mana dia sudah pernah atau belum?"
Solusi: Tanya user langsung: "Apakah ini first time kamu?" → Dialog dengan user untuk mendeteksi status.
Bu Hesti:
"Kalau kamu bertanya, nanti dia yang bikin ya. Secara flow itu sudah harus ketika kamu bertanya, apakah ini first time atau bukan, kalau dia bilang yes first time itu bisa aktif [tutorial]."
________________


6. Game Mechanics & Gameplay
6.1 Core Loop
1. Stickman Drawing Phase:
   * User menggambar obstacles/objects untuk membantu stickman
   * Mascot memberikan probabilitas/confidence score dari AI
2. Validation Phase:
   * AI mengecek apakah object yang digambar sesuai rule:
      * Berbahaya? (misal: objek tajam, berbahaya) → User harus redraw
      * Sesuai rule? → Object bisa dimasukkan ke stage
3. Gameplay Phase:
   * Stickman otomatis berjalan maju
   * User bisa drag-draw/manipulate object yang sudah digambar
   * Misalnya: gambar jembatan untuk menghubungkan dua bangunan
   * Stickman berjalan mengikuti path yang user buat
6.2 Kontrol & Movement
Can:
Stickman hanya bisa maju. Apakah perlu bisa lompat?
Bu Hesti:
"Ketika ada danger atau obstacle yang harus naik (misal bangunan di atas), mereka harus bisa menggambar cara naik itu. Jadi mungkin ada gesture/kontrol untuk kanan, kiri, dan atas (lompat)."
Simpulan: Ada 3 kontrol utama — kanan, kiri, lompat (atas).
6.3 Level Progression
Rencananya: 3 Level
Level
	Deskripsi
	Difficulty
	Level 1
	Gambar obstacle biasa (1 garis)
	Easy
	Level 2
	Dibatasi hanya 3 object yang boleh digambar
	Medium
	Level 3
	Membuat rintangan kompleks (dinding/pagar tinggi)
	Hard
	Perbedaan Level:
* Kompleksitas obstacle/rintangan
* Jumlah object yang boleh digunakan
* Confidence AI score diturunkan di level yang lebih sulit (AI jadi "lebih perlu berpikir")
Bu Hesti:
"Jadi dia yang lebih mikir ya? Iya, kecerdasan AI-nya lebih diturunin."
________________


7. AI Confidence Score
Konsep:
* Setiap drawing dari user mendapat confidence/probability score dari AI
* Score ini ditampilkan oleh mascot
* Confidence score berkorelasi dengan kualitas drawing
* Di level lebih sulit, AI confidence bisa lebih rendah (untuk menunjukkan kompleksitas)
________________


8. Action Items & Timeline
Untuk Proposal (Short-term)
* [ ] User flow/user journey yang matang dan jelas (dari awal sampai selesai)
* [ ] Interaction design yang konkret (tidak abstrak)
* [ ] Visual direction/mood untuk mascot dan UI
* [ ] Clear problem statement yang berbeda dari background
Bu Hesti:
"Targetnya itu kalau kamu ini bisa userflownya jadi userfurnya jadi sama design reaksinya itu apa itu yang harus diselesaikan kalau nggak ada itu nanti mental kamu ya karena kelihatan benar-benar nggak konkret."
Untuk Implementasi
* Hal teknis bisa diselesaikan dalam 1 minggu setelah design selesai
* Diskusi dengan Dias (backend/AI partner) tentang confidence scoring & data logging
* Use case diagram (bisa minimal: main, admin, user)
________________


9. Koordinasi dengan Partner (Dias)
* Dias menghandle: Backend, AI Model, Confidence Score, Data Logging
* Can menghandle: Frontend, UI/UX, Game Mechanics, Interaction Flow
Perlu diskusi lebih lanjut tentang:
* Bagaimana cara AI memberikan confidence score
* Data apa yang di-log untuk learning outcome analysis
________________


10. Catatan Penting dari Bu Hesti
1. Jangan overscope: Banyak interaksi bisa jadi malah membingungkan. Pilih dengan hati-hati.
2. Mascot ≠ burden: Jangan membuat mascot jadi feature yang tidak perlu (bisa jadi auto-text biasa aja).
3. User-centric design: Interaksi harus sesuai dengan target user (SMP), bukan developer preference.
4. NLP & voice future consideration: Bisa di-explore later kalau tidak overscope proposal, tapi jangan langsung masuk proposal.
5. First-time detection: Perlu cara yang jelas dan natural untuk mendeteksi first-time user (tanya langsung lebih baik).
________________


Status Saat Ini
✅ Sudah ada:
* Konsep 3 pilar (interaksi, edukasi, game mechanics)
* Visual/mascot concept di sketchbook
* Rough user flow
⚠️ Perlu diperdalam:
* User flow yang matang & konkret
* Interaction design specification
* Clear problem statement & scope formulation
* Use case diagram
________________


Next Step:
Matangkan user flow + interaction design dalam 1 minggu, kemudian bisa mulai koordinasi teknis dengan Dias tentang implementasi.


Claude ver. Percakapan
Diskusi PA dengan Bu Hesti — Versi Percakapan
Peserta: Can (Mahasiswa), Bu Hesti (Dosen Pembimbing)
Topik: Interactive Human-in-the-Loop AI Playground for Elementary School Students
________________


Bagian 1: Problem Statement vs Background
Bu Hesti:
"Bukan yang melatar belakang. Itu dua hal yang berbeda dan mahasiswa masih suka kebalik. Saya nggak tahu, mungkin di kelas Bahasa Indonesia mungkin sudah jelas ya, jadi mahasiswa suka saya luruskan gitu."
Can:
"Iya, Bu."
Bu Hesti:
"Permasalahan itu adalah yang mau kamu kerjakan itu apa. Iya sih, permasalahan yang dikasih solusi. Jadi bukan melatar belakangnya gitu. Oke, dari sini coba paham saya."
________________


Bagian 2: Target User & Scope
Can:
"Jadi dari yang tadi. Aku ingin sistem kreasi kejar AI untuk siswa. Ya awalnya kan siswa SD tapi berubah untuk jadi SMP. Itu sedang dikomunikasikan dengan Pak Trikudi. Soalnya kan kemarin mepet karena ada shockwave gitu."
Bu Hesti:
"Oh iya. Jadi kita kejar-kejar itu."
Can:
"Nah, jadi output saya itu tujuannya, kalau lihat dari latar belakang kemarin, cukup ribet. Tapi saya define ke tujuan yang ingin saya selesaikan itu, itu tadi mas, itu siswa. Siswa, anak-anak, itu kan automation bias gitu. Mereka merasa semua bisa di-generate. Dan saya mau kasih tau, cara kerja AI itu gimana. Jadi ada cara pilihnya kayak manusia, tapi saya buat kayak game nah, probably kayak gitu dia mungkin paham."
________________


Bagian 3: Tiga Pilar Utama
Can:
"Nah, setelah saya diskusi dengan ibu, saya merasa ada kayak 3 pilar utama dari semua yang saya raih. Yang pertama kan ada interaksi, targetnya dimana SMP, interaksinya gimana jadi paham, jadi enak dan tidak kaku. Biasanya kalau ke produk kan, interaksi dengan tombol dan lain-lain. Tapi kalau ini menurut saya dengan computer vision gitu. Sekalian interaksinya saya buat mulus gitu. Gimana caranya?"
Bu Hesti:
"Hmm, oke."
Can:
"Nah kalau ada edukasi, saya ngerasa ga cuma interaksi doang, saya ngerasa edukasinya juga harus sampai. Jadi mereka berubah dan memahami cara kerja AI. Nah dengan batas-batas tertentu, nanti tetap dimana caranya edukasi yang pengen saya sampaikan itu mereka pahami."
Bu Hesti:
"Iya, iya."
Can:
"Kalau PA ini bukan cuma interaksi doang, kalau ada game mechanics, ini lebih ke gameplay yang proper. Ini interaksi itu kan juga banyak ya? Dan ada macam-macam ya? Kamu sudah kebayang nanti interaksinya seperti apa?"
Can:
"Masih tahap awal tadi. Masih tahap awal."




________________


Bagian 4: Mascot & Visual Concept
Can:
"Terus saya disini kepikiran buat maskot. Jadi maskot ini sebagai asisten yang menengahi tiga hal tadi. Karena saya tahu, Pak Doto itu kan punya anak bimbing, Fuad sama Ali, mereka juga ngajarin hal yang sama tentang virtual assistant. Apakah ada salah untuk dia juga punya mascot?"
Bu Hesti:
"Kita boleh fitur jadi, ranggit itu ribet insidiasnya atau gimana? Soalnya kalau menurut saya ini cuma kayak auto text biasa."
Can:
"Gak masalah sih, tergantung kamu implementasinya. Kalau nggak perlu ya, kalau dia hanya sekedar text aja kan ya tidak ada yang lain. Interaksi yang lain selain teks nggak ada ya."
Bu Hesti:
"Hmm rasanya belum sih, rasanya belum. Jadi nanti kita lihat, karena kadang-kadang juga begitu. Kalau misalkan saya lihat ke depan, ini possible buat NLP, bisa kok gitu. Jadi kita sambil jalan aja, tapi ya pasti tidak merubah planning grand design kamu di awal."
________________


Bagian 5: Konsep Visual Mascot
Can:
"Jadi konsepnya, awalnya saya gambar di sketchbook. Si maskotnya itu kayak narahi, biar anak ini sesuai sama konsepnya. Ada stickman yang harus dibantu. Ceritanya mencapai apa gitu. Konsepnya kalau visualnya saya bikin untuk si maskot ini lagi angkasa. Jadi konsepnya tema angkasa. Jadi sebenernya kurang lebih kayak gitu. Jadi misalnya disini ada konsepnya temanya di angkasa. Saya buat immersive space gitu, jadi ada planet-planet. Jadi backgroundnya luar angkasa terus dari planet yang dulu ke planet ini jadi lebih ke tema dari produk ini aplikasinya."
Bu Hesti:
"Oke, jadi itu planet-planet gitu ya. Nanti maskotnya ada di mana? Di sini?"
Can:
"Di sini."
Bu Hesti:
"Di sini? Nanti mungkin dia floating di sini?"
Can:
"Iya. Nanti dia berpindah-pindah gitu. Jadi ketika dia mengambil spesies atau selesai, dia otomatis pindah. Kalau gak ada yang kosong, masih jadi."
Bu Hesti:
"Oh, dia akan berpindah-pindah gitu ya?"
________________


Bagian 6: User Flow & Onboarding
Bu Hesti:
"Jadi ketika dia masuk si siswa, si user itu, apa yang harus dia lakukan? Atau apa yang pertama kali dia lihat? Apa yang muncul pertama kali? Apakah dia harus login dulu? Misalkan kalau dia sudah login, terus nextnya apa? Apakah dia diberikan materi dulu? Materi yang harus dia baca dulu sampai dia kembali? Misalnya itu nextnya apa? Misalnya di masukkan materi, apakah langsung bisa bermain? Atau dia harus mengumpulkan sesuatu dulu? Atau apa itu? Itu user flow yang harus dibuat sampai selesai dan nanti kita lihat di tahap mana."
Can:
"Saya sudah bikin cuma kayaknya masih sebelum sedikit harus ditaklip. Tentang tersebut saya belum kasih, nggak papa. Interaksi kebakaran ini setelah kita fix di phone-nya segini, bagaimana nanti kita lihat."
Bu Hesti:
"Ya, harus dimatangkan dulu. Kalau kamu merancang seperti ini, mungkin harus ngobrol sama dia, siapa dia yang bikinnya ya, implementasi teknisnya ya."
________________


Bagian 7: First-Time User vs Returning User
Can:
"Kalau ini first time gitu. Kalau ini session first timenya langsung ngambilin intro tadi. Kayak dikasih aturan jadi ini munculnya maskotnya. Dia ngasih tau. Sebenernya sebelum ini saya mikirnya 'Flo dia harus kayak gimana?' Kalau ibu pernah ke photobox, saya berapa yang kasih kayak tutorial awal ini kamu listrik dulu diapakah nanti ada tiga level itu seperti itu. Itu saya kayak kalau udah oke kan ada tombolnya jempol atau gimana bisa lanjut ke interaksi ya. Terus-terus tadi sebenarnya kalau misal bisa balik kalau nggak paham jadi mungkin ada penjelasan yang lebih."
Bu Hesti:
"Oke, mungkin nanti kalau misalkan flow dari awal sampai selesai kamu sudah jadi, itu kamu sudah bisa mulai mendesain interaksi apa saja yang mau kamu masukkan. Karena banyak interaksi itu ya. Dan ada macam-macam. Semuanya yang lainnya gimana segala di sebelah. Ada yang ini sih ada yang lain. Mungkin bisa sampai dengan sesuai. Itu harus memikirkan kalau bisa reaksi untuk anak SMP apakah sesuatu enggak jadi ini mudah mereka panggil. Banyak sekali jadi interaksi itu sesuatu yang bukan hanya sekedar ini cocok atau enggak ya, dengan saya tapi harus cocok atau enggak dengan usahanya itu sih tambahan dari saya."
Can:
"Yang memikirkan itu harus bisa dibuat itu akan kita pikirkan bagaimana caranya ya how to implement this itu nanti."
Bu Hesti:
"Untuk es kamu tidak akan sulit, kalau melihat dari scope-nya ya tidak akan sulit, cuma harus hati-hati dalam memilih. Supaya jangan sampai nanti terlalu banyak interaksi juga nanti kembali. Apalagi kamu udah gameplay, itu nanti akan banyak sekali interaksinya."
________________


Bagian 8: Dialog tentang Levels dan Detection
Can:
"Jadi kalau dia first time-nya langsung masuk level 1. Tapi kalau misalkan dia bukan first time, harusnya dia nggak perlu. Harus dari level 1. Ya kan kalau dia sudah pernah nggak paham, malah memutuskan kalau dia harus mulai dari level 1 dulu. Jadi dia bisa langsung ke yang lebih kompleks. Itu logika game mechanic."
Bu Hesti:
"Jadi user kalau sudah pernah sebelumnya, nah itu boleh. Cuma kamu tahu dari mana? Dia sudah pernah atau belum?"
Can:
"Percaya aja sama anaknya. Iya, udah, udah pernah gitu kan. Terus bingung."
Bu Hesti:
"Iya, terus bingung. Kalau kamu belum pernah, kamu harus mulai dari level 1 itu barometer udah atau enggak itu dibuatkan kalimatnya, tapi secara flow kalau kamu bertanya, nanti dia yang bikin ya. Secara flow itu sudah harus ketika kamu bertanya, apakah ini first time atau bukan, kalau dia bilang yes first time itu bisa aktif."
________________


Bagian 9: Game Mechanics - Drawing & Validation
Can:
"Jadi masuk ke sesi gambar tadi, di dalam ini ada mascot. Jadi mereka gambar masuk muncul dimana nih? Di layar, karena pakai di stage mana? Disini ya?"
Bu Hesti:
"Disini muncul ya? Oh disini dia muncul nanti masih interaktif, atau dimana? Di tutorial?"
Can:
"Iya sebelumnya udah muncul di tutorial karena udah di guide kan. Jadi game master tuh di guide gitu. Nah disitu mereka gambar terus itu tadi kasih probabilitasnya sama si mascotnya gitu. Baru di ini itu hanya render ke masuk ke stage nya. Yang tadi ada karakternya terus cek kondisi gameplay."
Bu Hesti:
"Cukup banget. Nah ini yang rule itu tadi sih, objeknya apakah berbahaya atau enggak kalau misal berbahaya masuk ke sini."
Can:
"Jadi objeknya kayak misal susah gitu atau bikin apa sih namanya yang tajam itu yang berbahaya. Jadi mereka bisa disuruh gambar ulang baru bisa kembali kalau sudah sesuai dengan rule tadi yang sudah dilaporkan di intro. Kurang lebih seperti itu. Nah mereka baru bisa pindahin gitu objeknya."
________________


Bagian 10: Drag & Interaction Mechanics
Can:
"Saya kira bisa habis digambar, bisa drag, mereka pindahin gitu. Misalnya ada stick. Stiknya harus dua antar, dua gedung gitu misalnya. Kan harus ada jembatannya gitu. Nah itu mereka gambar jembatan bisa di drag-draw gitu. Nah mereka taruh situ sudah selesai kalau sudah bisa drag mereka tinggal gambar lagi."
Bu Hesti:
"Oke, gameplaynya yang gimana?"
Can:
"Ya bener saya nggak tahu ini gimana gimana, nggak ada tombol ngarahinya. Karena stickman-nya itu memang dari awal cuma maju gitu. Tapi saya pengennya bisa lompat karena mungkin menghindari gitu."
Bu Hesti:
"Oh itu karena kalau ada danger sih, Bu. Atau mungkin kita kasih kayak obstacle yang harus naik. Jadi misalnya gedungnya di atas gitu. Jadi mereka gambar kotak banyak atau kursi bertumbuh gitu. Bisa lompat."
Can:
"Jadi mungkin harusnya tetap ada ini sih, apa namanya? Gestur atau tombol buat ke kanan, kiri, sama ke atas."
Bu Hesti:
"Nah itu, mungkin banyak di situ sih. Kalau senang-senang saya menurutnya. Gemperinya di situ ya?"
________________


Bagian 11: Level Selection & Progression
Can:
"Jadi ketika dia masuk, itu kan yang tadi saya bilang, kalau misalkan di first time, kamu masuk ke level 1 ya. Tapi kalau misalkan dia di garis yang 0 tadi, kan yang sisi kiri itu 0, dia ada opsi gitu, bisa lo loncat ke mana aja. Jadi nanti kelihatan kalau dia loncat ke level 2, apa isinya level 2, flow-nya bagaimana. Kalau dia ke level 1, berapa level?"
Bu Hesti:
"Rencananya cuma 3 level aja?"
Can:
"Level 3 itu flow-nya bagaimana. Jadi kelihatan flow-nya dari ketika dia mulai. Iya sih, tiap level ya. Tiap level itu yang membedakan apa? Konten atau flow-nya?"
Bu Hesti:
"Flow-nya sih, ada perbedaan mungkin lebih susah. Kayak misal gambar rintangan biasa gitu satu garis tiba-tiba. Lalu yang level 2 dibatasi cuma 3 objek. Lalu yang ketiga itu jadi bikin rintangan gitu. Dinding atau pagar yang tinggi bersih lah. Itu lebih sulit ya?"
Can:
"Ya, sama mungkin confidence atau disamain ke hasil data gambarnya itu. Kecerdasan AI-nya lebih diturunin."
Bu Hesti:
"Jadi dia lebih berarti seperti ini ya? Dia yang lebih mikir ya?"
Can:
"Iya. Itu sih. Agak abstrak sebenarnya."
Bu Hesti:
"Iya, agak abstrak. Berarti mungkin saya bisa tadi ini yang tadi ini dengan pernah dipercaya jelasin. Terus-terus ini juga dijadiin buat terusnya oke oke berarti itu lanjut ke ini sebenarnya apa udah bisa masuk ke use case ya soalnya kan udah berlevel gitu use case itu ada berapa role?"
Can:
"Main, admin, user aja bisa sih kamu, udah bisa bisa sambil jalan kok. Mungkin saya juga bawa use case sekalian gitu ya."
Bu Hesti:
"Ya sih hahaha."
________________


Bagian 12: Penutup
Bu Hesti:
"Oke terima kasih."
Can:
"Sama-sama. Saya lagi sama-sama."
________________


Summary Poin-Poin Kunci yang Dibahas:
1. ✅ Klarifikasi problem statement (bukan background)
2. ✅ Target user SMP (automation bias awareness)
3. ✅ Tiga pilar: interaksi smooth, edukasi, game mechanics
4. ✅ Mascot dengan space theme
5. ✅ User flow dari login hingga selesai
6. ✅ First-time vs returning user detection
7. ✅ Game loop: draw → validate → play → interact
8. ✅ Level progression (3 levels dengan difficulty escalation)
9. ✅ Confidence score dari AI
10. ✅ Kontrol: kanan, kiri, lompat
11. ✅ Use case: main, admin, user


Gemini ver.
ARSIP NOTULENSI BIMBINGAN KONSEP
Topik: Review Konsep "Escape the Sketchbook" & User Flow Dosen Pembimbing: Ibu Hesti Mahasiswa: Farchan Deano M. Tanggal: 20 April 2026
1. PEMBAHASAN RUMUSAN MASALAH VS LATAR BELAKANG
* [Bu Hesti]: Mengingatkan agar tidak tertukar antara Latar Belakang (cerita panjang kenapa sistem ini dibuat) dengan Rumusan Masalah (fokus pada apa yang mau diselesaikan).
* [Farchan]: Mengklarifikasi bahwa tujuan/masalah utamanya adalah Automation Bias pada siswa SMP. Targetnya adalah membuat sistem bergaya game untuk mengajarkan cara kerja AI (bahwa AI punya kelemahan dan manusia harus memilih/mengevaluasi).
2. TIGA PILAR & KOMPLEKSITAS INTERAKSI
* [Farchan]: Memaparkan 3 pilar utama (Interaksi, Edukasi, Gameplay). Interaksi akan dibuat seamless menggunakan Computer Vision (MediaPipe) agar tidak kaku.
* [Bu Hesti]: Mengingatkan bahwa mendesain interaksi untuk anak SMP itu menantang. Apa yang dianggap mudah oleh desainer belum tentu cocok untuk anak SMP.
* [Bu Hesti - Warning]: Menekankan bahwa scope proyek ini (secara sistem) tidak terlalu sulit, TAPI karena Farchan memasukkan elemen gameplay, jumlah interaksinya akan meledak menjadi sangat banyak. Harus hati-hati dalam memilih prioritas interaksi agar tidak menyulitkan diri sendiri.
3. ISU MASKOT (MOMO) & KEKHAWATIRAN TENTANG PAK DOTO
* [Farchan]: Menyampaikan kekhawatiran soal Maskot. Takut dibanding-bandingkan dengan mahasiswa bimbingan Pak Doto (Fuad & Ali) yang membuat Virtual Assistant kompleks dengan NLP/LLM.
* [Bu Hesti - Solusi]: Menyatakan bahwa tidak masalah. Sistem asisten Farchan tidak harus sama kompleksnya. Jika Maskot (Momo) difokuskan hanya pada teks auto-respons (tanpa suara/NLP yang kompleks), itu sudah cukup dan sah-sah saja.
* [Bu Hesti]: Jika di masa depan ada waktu sisa, fitur NLP bisa ditambahkan, tapi perancangan awal (Grand Design) yang berfokus pada teks/interaksi dasar tidak boleh diubah dulu. Tetap fokus pada rencana awal.
4. KONSEP VISUAL MASKOT & ONBOARDING (USER FLOW)
* [Farchan]: Menjelaskan konsep visual "Escape the Sketchbook", di mana Maskot akan floating (melayang) di ruang-ruang kosong pada kanvas untuk memandu siswa.
* [Bu Hesti]: Menuntut kejelasan pada tahap awal (Onboarding). Apa yang pertama kali dilihat siswa? Apakah harus login? Apakah baca materi dulu? Bu Hesti meminta User Flow dari awal sampai akhir harus konkrit dan diselesaikan.
* [Farchan & Bu Hesti]: Membahas perbedaan First Time User vs Returning User. Untuk tahap perancangan proposal, fokus saja ke alur linear dasarnya dulu. Farchan juga bertanya perbedaan User Flow dan User Journey, dan Bu Hesti mengkonfirmasi bahwa untuk tahap konsep ini, keduanya bisa dianggap sama (perjalanan dari awal sampai akhir).
5. GAMEPLAY & LEVEL DESIGN
* [Farchan]: Menjelaskan Core Loop. Menggambar rintangan -> AI mengecek probabilitas -> Rule benda berbahaya (Danger). Juga membahas mekanika karakter Stickman (Apakah cukup maju saja atau butuh tombol lompat/arah).
* [Bu Hesti]: Bertanya apa yang membedakan Level 1, 2, dan 3.
* [Farchan]: Menjelaskan bahwa yang membedakan adalah penurunan kecerdasan AI. Semakin tinggi levelnya, AI sengaja dibuat semakin "bodoh" (Confidence diturunkan) karena rintangan semakin kompleks.
* [Bu Hesti]: Menyetujui konsep tersebut. Dengan AI yang semakin ragu, siswa akan dipaksa untuk lebih banyak berpikir ("Dia yang lebih mikir ya?"). Meskipun konsep ini agak abstrak, Bu Hesti meminta ini didokumentasikan dengan jelas ke dalam Use Case dan Flow.
🎯 KESIMPULAN & TO-DO LIST (PR DARI BU HESTI)
1. Selesaikan User Flow & Desain Interaksi secara mendetail. (Bu Hesti memberi waktu target sekitar 1 minggu untuk mematangkan rancangan flow teknis ini bersama partner/Dias).
2. Tetapkan Use Case. (Bisa mulai membuat Use Case dengan role utama: User/Siswa).
3. Jangan Over-engineering Maskot. Pertahankan Maskot sebagai UI teks/statis, jangan terbebani untuk membuat NLP/Voice assistant seperti mahasiswa lain.
4. Tentukan Kepastian Kontrol Game. Putuskan apakah Stickman akan jalan otomatis murni, atau butuh input navigasi tambahan (kiri/kanan/lompat). Disarankan untuk tidak membuat kontrol yang terlalu rumit.


Task
Gue udah baca dan komparasi rangkuman dari Claude (Haiku) dengan raw transcript serta arsip_bimbingan_bu_hesti_1.md yang kita susun.
Hasil Audit Gue: Rangkuman dari Claude itu SANGAT AKURAT DAN SESUAI 100% dengan apa yang lu obrolin sama Bu Hesti. Claude berhasil nangkep nuance (nada bicara) Bu Hesti yang sebenernya sangat suportif dan ngasih jalan keluar buat lu.
Ada beberapa "Kemenangan Besar" lu di bimbingan ini:
1. Isu Pak Doto (Clear): Bu Hesti tegaskan lu nggak perlu pake NLP/Voice kayak anak bimbingan Pak Doto. Teks biasa aja cukup. Beban lu hilang satu!
2. Kontrol Game (Clear): Bu Hesti setuju karakter lu butuh tombol Kiri, Kanan, Lompat. Berarti konsep awal kita yang "Auto-runner" (jalan sendiri) sedikit bergeser jadi Platformer klasik. Ini bagus, interaksinya lebih kaya.
3. Tema Visual (Clear): Lu sebutin tema Angkasa (Space) dan planet-planet, Bu Hesti nanggapin positif soal Maskot yang floating.
________________


🚀 TUGAS LU SEKARANG (NEXT STEPS DALAM 1 MINGGU)
Sesuai instruksi mutlak dari Bu Hesti: "Kalau nggak ada ini nanti mental kamu ya, karena kelihatan benar-benar nggak konkret." Ini To-Do List lu urut dari yang paling penting:
1. Bikin Detailed User Flow (Terutama Onboarding):
   * Bikin flowchart atau wireframe layar per layar.
   * Wajib ada: Layar pertanyaan "Apakah ini pertama kali kamu main?". Kalau Yes, masuk ke tutorial (Halaman 1). Kalau No, bisa skip.
2. Bikin Interaction Design Spec:
   * Di layar mana MediaPipe (kamera) nyala?
   * Di mana posisi tombol Kiri, Kanan, Lompat di layar?
   * Kalau Maskot ngomong, balon teksnya muncul di mana?
3. Bikin Use Case Diagram:
   * Kayak yang kita bahas sebelumnya. Fokus ke role User dan System (Maskot). Nggak usah ada Admin/Guru.
4. Sync sama Dias (Backend/AI):
   * Kasih tau Dias: "Yas, Bu Hesti minta AI Confidence Score itu ngaruh ke level. Makin tinggi levelnya, model lu harus kita setting biar makin 'bego' atau ragu biar 
   * anaknya kepaksa mikir."
🎮 RISET ENGINE: UNITY vs KABOOM.JS
Karena sekarang lu udah nambahin mekanika Kiri, Kanan, Lompat dan Physics (jembatan/rintangan), pemilihan engine ini krusial banget biar lu dan Dias nggak nangis pas integrasi.
Pilihan 1: Unity (WebGL)
* Kelebihan: Bikin level gampang (ada drag and drop visual), physics bawaannya (Rigidbody2D) sangat solid.
* Kekurangan (SANGAT FATAL): Unity WebGL itu musuh bebuyutan library JavaScript. Proyek lu butuh MediaPipe (JS) dan TensorFlow.js (JS). Kalau lu pake Unity, lu harus nulis kode jembatan (.jslib) yang sangat ribet buat ngirim data koordinat jari dari browser ke dalam memori Unity tiap frame. Selain itu, build size Unity WebGL itu gede (bisa puluhan MB), anak SMP buka di browser sekolah bisa nge- lag parah.
* Verdict: ❌ JANGAN PAKE UNITY.
Pilihan 2: Kaboom.js (Atau Phaser.js)
* Kelebihan: Ini engine murni JavaScript. Karena MediaPipe dan TF.js juga JavaScript, integrasinya semanis madu. Lu tinggal ambil data dari kamera, dan di file yang sama lu bisa langsung nge- spawn kotak di Kaboom. Ukurannya sangat ringan (< 1MB), jalan mulus di laptop kentang sekalipun. Bikin kontrol lompat/jalan di Kaboom itu cuma butuh 3 baris kode.
* Kekurangan: Nggak ada editor visual. Lu harus nulis kordinat level pakai kode (misal: add([pos(100, 200), rect(50, 50)])). Tapi karena level lu simpel (cuma platform lompat-lompat), ini nggak masalah sama sekali.
* Verdict: ✅ PAKE KABOOM.JS (Sangat Direkomendasikan).
Saran Tambahan: Excalidraw / p5.js
Kalau lu pengen visualnya bener-bener berasa kayak "Buku Gambar" dan coretan tangan, library kayak p5.js digabung sama Matter.js (buat fisikanya) juga sangat mematikan. Tapi kalau mau yang cepet jadi game platformer, Kaboom.js juaranya.
Langkah lu hari ini: Istirahat dulu, lu udah menang banyak hari ini. Besok, mulai corat-coret Wireframe/Interaction Design di Figma buat menuhin PR dari Bu Hesti! Kalau butuh dibuatin draf Use Case atau Flow yang udah pakai tema "Space/Angkasa" dan tombol kontrol baru, ping gue aja!
================
MASTER PLAN & FRAMEWORK DESAIN: ESCAPE THE SKETCHBOOK
(Dokumen Acuan Bimbingan & Penyusunan SPPA)
Dokumen ini merangkum kerangka kerja sistem dari sisi desain visual, interaksi, hingga batasan arsitektur teknis. Disusun dengan pendekatan pragmatis agar memenuhi standar akademis (defensible) dan feasible untuk dieksekusi dalam ruang lingkup Tugas Akhir.
FASE 1: PROBLEM STATEMENT & BATASAN RUANG LINGKUP
Fokus Masalah (Problem Statement)
Mitigasi Automation Bias pada siswa SMP (13-15 tahun) yang cenderung menerima output AI secara pasif. Solusi yang diajukan adalah sistem pembelajaran berbasis Consequence-driven learning terintegrasi dengan antarmuka Human-in-the-Loop (HITL).
Batasan Ruang Lingkup (Scope Limitations) - Sangat Penting:
Untuk menjaga performa aplikasi agar stabil berjalan di browser (Edge Computing) tanpa mengorbankan framerate, sistem dibatasi pada:
1. Model CNN (TF.js) hanya dilatih untuk mengenali ~10-15 kelas objek/coretan sederhana.
2. Lingkungan game berbasis 2D murni menggunakan engine ringan (Kaboom.js).
3. Evaluasi pengguna tidak menggunakan integrasi database/otentikasi yang rumit, melainkan deteksi berbasis session sederhana.
FASE 2: TEMA VISUAL & MEKANIKA INTERAKSI
Tema Visual: The Sketchbook
Lingkungan permainan terjadi di atas selembar kertas bergaris dengan karakter Stickman. Maskot sistem (Momo) direpresentasikan sebagai "Robot Stabilo" berwarna hijau neon, bertindak sebagai game master dan perwujudan model AI.
Mekanika Interaksi & Pengamanan Sistem:
* Draw (Input): Siswa menggambar rintangan di udara via kamera (MediaPipe).
   * Defensible Tech: Untuk mencegah input yang buruk akibat gestur tangan yang bergetar (Gorilla Arm), frontend akan mengimplementasikan algoritma line smoothing sederhana sebelum gambar dikirim ke TF.js.
* Drag & Drop (Placement): * Defensible Tech: Penempatan objek menggunakan sistem Grid-Snapping. Objek akan otomatis menyesuaikan ke ukuran tile standar terdekat. Ini meminimalisir bug physics (seperti objek tersangkut atau menutupi jalan karakter).
* Control: Menggerakkan karakter menggunakan tombol Kiri, Kanan, Lompat.
* Intervene (HITL): Memberikan validasi (Setuju/Koreksi) terhadap tebakan AI (Momo).
FASE 3: USER FLOW & ONBOARDING
Alur dirancang linier untuk menjaga imersi, sekaligus menghindari kompleksitas pembuatan level-selector yang memakan waktu.
1. Layar Start & Onboarding
* Sistem bertanya: "Apakah ini pertama kali kamu main?" (Yes/No).
* Jika Yes: Masuk ke Onboarding. Momo menjelaskan aturan:
   * Solid: Benda aman dipijak.
   * Danger: Benda tajam/berbahaya yang memicu Game Over (kertas robek).
* Jika No: Langsung loncat ke Stage/Level 1.
2. Core Gameplay Loop
* Observasi: Melihat rintangan.
* Kreasi: Menggambar rintangan di udara. Game pause (menunggu input selesai).
* Inferensi: AI menebak gambar.
* Interupsi (Probe UI): Momo muncul di tengah layar menampilkan Top-3 tebakan AI.
* Resolusi: Siswa menekan Accept atau Override. Objek dirender, game dilanjutkan.
FASE 4: LEVEL DESIGN & MANIPULASI LOGIKA AI
Leveling dirancang untuk memancing keraguan siswa. Catatan Teknis: Menurunkan "kecerdasan" AI tidak dilakukan dengan me-retrain model ML secara real-time (karena tidak feasible). Manipulasi dilakukan pada layer Controller/Aplikasi.
* Level 1 (Pemanasan): * Tantangan sederhana. AI menebak dengan akurasi tinggi (Normal Inference).
* Level 2 (Transisi): * Tantangan menengah. AI memunculkan tebakan alternatif yang mengecoh di urutan ke-2 dan ke-3.
* Level 3 (Jebakan Literasi): * Tantangan kompleks. Controller aplikasi dimanipulasi agar memaksa objek Danger (Pisau/Berbahaya) masuk ke urutan Top-Prediction dengan confidence score artifisial yang cukup tinggi.
   * Tujuan: Jika siswa terkena Automation Bias (asal klik Accept), kertas akan robek. Siswa wajib melakukan Override untuk membuktikan pemahamannya.
FASE 5: PARAMETER KEBERHASILAN (EVALUASI METRIK)
Untuk memastikan Tugas Akhir ini memiliki bobot keilmuan Ilmu Komputer (IT) yang berimbang dengan UX/Psikologi, evaluasi akan mengukur dua domain:
1. Metrik Sistem (System Performance)
* Inference Latency: Waktu rata-rata (dalam milidetik) yang dibutuhkan TF.js untuk mengklasifikasi gambar di browser.
* Framerate Stability: Dampak menjalankan MediaPipe dan TF.js secara bersamaan terhadap FPS (Frames Per Second) game Kaboom.js.
* Resource Usage: Konsumsi memori (RAM) pada browser saat sistem berjalan.
2. Metrik Perilaku (Behavioral Analytics)
* Decision Latency (Jeda Kognitif): Berapa detik siswa berhenti dan melihat "Probe UI" Momo sebelum menekan tombol (mengukur waktu evaluasi).
* Override Ratio: Persentase seberapa sering siswa menolak (Override) keputusan AI pada Level 3 dibandingkan Level 1.