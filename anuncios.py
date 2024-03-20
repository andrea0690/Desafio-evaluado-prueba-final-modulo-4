campanas = (
    {
        "tipo": "Video",
        "nombre": "Campaña de video 1",
        "presupuesto": 10000,
        "fecha_inicio": "2023-11-14",
        "fecha_termino": "2023-12-14",
        "anuncios": [
            {
                "subtipo": "instream",
                "duracion": 30,
                "url_archivo": "video1.mp4",
                "url_clic": "https://www.ejemplo.com/video1",
            },
            {
                "subtipo": "outstream",
                "duracion": 60,
                "url_archivo": "video2.mov",
                "url_clic": "https://www.ejemplo.com/video2",
            },
        ],
    },
    {
        "tipo": "Display",
        "nombre": "Campaña de display 2",
        "presupuesto": 5000,
        "fecha_inicio": "2023-11-21",
        "fecha_termino": "2023-12-21",
        "anuncios": [
            # {
            #     "subtipo": "tradicional",
            #     "ancho": 300,
            #     "alto": 250,
            #     "url_archivo": "tradicional1.png",
            #     "url_clic": "https://www.ejemplo.com/tradicional1",
            # },
            {
                "subtipo": "native",
                "ancho": 728,
                "alto": 90,
                "url_archivo": "native1.jpg",
                "url_clic": "https://www.ejemplo.com/native1",
            },
        ],
    },
    {
        "tipo": "Social",
        "nombre": "Campaña de social 3",
        "presupuesto": 2000,
        "fecha_inicio": "2023-11-28",
        "fecha_termino": "2023-12-28",
        "anuncios": [
            # {
            #     "subtipo": "facebook",
            #     "texto": "Este es un anuncio de Facebook",
            #     "url_imagen": "imagen1.jpg",
            #     "url_clic": "https://www.ejemplo.com/facebook1",
            # },
            {
                "subtipo": "linkedin",
                "texto": "Este es un anuncio de linkedin",
                "url_imagen": "imagen2.jpg",
                "url_clic": "https://www.ejemplo.com/linkedin1",
            },
        ],
    },
)
