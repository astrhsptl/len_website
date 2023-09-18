class About:
    def __init__(self, 
            first_name: str,
            last_name: str,
            resume: str,
            image: str,
            about: str) -> None:

        self.first_name: str = first_name
        self.last_name: str = last_name
        self.resume: str = resume
        self.image: str = image
        self.about: str = about


DEVELOPERS = [
    About(
        first_name="Олег",
        last_name = "Гранов",
        resume = "resume/granov.pdf",
        image = "resume_images/granov.jpg",
        about = "Веб-разработчик. Пишу клиентские приложения с использованием фреймворка Next.js (React) и языка TypeScript",
    ),
    About(
        first_name="Никита",
        last_name = "Кульпинов",
        resume = "resume/kulpinov.pdf",
        image = "resume_images/kulpinov.jpg",
        about = "Back-End/Front-End разработчик с уклоном в DevOps инженерию",
    ),
    About(
        first_name="Николай",
        last_name = "Назарько",
        resume = "resume/nazarko.pdf",
        image = "resume_images/nazarko.jpg",
        about = "Я - frontend веб-разработчик. Владею языком JavaScript и фреймворком React",
    ),
    About(
        first_name="Михаил",
        last_name = "Скуратов",
        resume = "resume/skuratov.pdf",
        image = "resume_images/skuratov.jpg",
        about = "Я – веб-разработчик (backend). Пишу серверные приложения на языке Python (Django/Fast API).",
    ),
    About(
        first_name="Веденёв",
        last_name = "Алексей",
        resume = "resume/vedenev.pdf",
        image = "resume_images/vedenev.jpg",
        about = "Веб-разработчик, хорошо знающий Python. Занимаюсь backend частью приложений с помощью фреймворка Django.",
    ),
]