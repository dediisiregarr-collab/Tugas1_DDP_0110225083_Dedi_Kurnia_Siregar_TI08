from django.shortcuts import render

def home(request):
    context = {
        'name': 'Dedi Kurnia Siregar',
        'profession': 'Web Developer',
        'profile_photo': 'images/profile.jpeg',
        'description': '''
            Saya Dedi Kurnia Siregar, mahasiswa Teknik Informatika di Sekolah Tinggi Teknologi Terpadu Nurul Fikri (STT-NF)
            yang memiliki ketertarikan kuat pada bidang pengembangan perangkat lunak, pemrograman, dan teknologi web. 
            Saya memiliki komitmen tinggi terhadap proses pembelajaran berkelanjutan, mampu bekerja secara mandiri maupun kolaboratif,
            serta berorientasi pada ketelitian dan kualitas dalam setiap pekerjaan.
        ''',
        'email': 'dediisiregarr@gmail.com',
        'phone': '+62 896-5306-7631',
        'location': 'Depok, Indonesia'
    }
    return render(request, 'home.html', context)

def about(request):
    context = {
        'education': [
            {
                'degree': 'Teknik Informatika',
                'institution': 'STT-NF',
                'year': '2025 - Sekarang',
            },
            
            {
                'degree': 'SMK',
                'institution': 'SMK Negeri 1 Padangsidimpuan',
                'year': '2020 - 2023',
            },
            
            {
                'degree': 'SMP',
                'institution': 'SMP Negeri 6 Padangsidimpuan',
                'year': '2017 - 2020',
            },
            
            {
                'degree': 'SD',
                'institution': 'SD Negeri 5 Padangsidimpuan',
                'year': '2011 - 2017',
            },
        ],
        'organizations': [
            {
                'name': 'OSIS SMK Negeri 1 Padangsidimpuan',
                'position': 'Anggota',
                'period': '2021 - 2022',
                'description': 'Aktif dalam kegiatan organisasi'
            },
        ]
    }
    return render(request, 'about.html', context)

def gallery(request):
    context = {
        'images': [
            {
                'url': '/static/images/bola.jpeg',
                'title': 'Kegiatan 1',
                'description': 'Bermain Sepak Bola'
            },
            {
                'url': '/static/images/heal.jpeg',
                'title': 'Kegiatan 2',
                'description': 'Jalan Jalan Naik Vespa'
            },
            {
                'url': '/static/images/rame.jpeg',
                'title': 'Kegiatan 3',
                'description': 'Organisasi OSIS'
            },
        ]
    }
    return render(request, 'gallery.html', context)