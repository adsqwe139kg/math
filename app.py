from flask import Flask, render_template, request

app = Flask(__name__)

# База даних тем для динамічної генерації сторінок
TOPICS = {
    "square": {
        "title": "Квадрат",
        "desc": "Чотирикутник, у якого всі сторони рівні і всі кути прямі.",
        "theory": "Квадрат є окремим випадком прямокутника, ромба та паралелограма. Має 4 осі симетрії.",
        "formulas": [
            {"name": "Периметр", "formula": "P = 4a"},
            {"name": "Площа", "formula": "S = a²"},
            {"name": "Діагональ", "formula": "d = a√2"}
        ],
        "example": "Якщо сторона квадрата $a = 5\text{ см}$, то його площа $S = 5^2 = 25\text{ см}^2$, а периметр $P = 4 \times 5 = 20\text{ см}$.",
        "inputs": [{"id": "side", "label": "Сторона (a)"}],
        "svg": '<rect x="25" y="25" width="150" height="150" fill="none" stroke="#61afef" stroke-width="4"/>'
    },
    "rectangle": {
        "title": "Прямокутник",
        "desc": "Чотирикутник, у якого всі кути прямі.",
        "theory": "Протилежні сторони прямокутника рівні та паралельні. Діагоналі рівні і діляться точкою перетину навпіл.",
        "formulas": [
            {"name": "Площа", "formula": "S = a · b"},
            {"name": "Периметр", "formula": "P = 2(a + b)"},
            {"name": "Діагональ", "formula": "d = √(a² + b²)"}
        ],
        "example": "При сторонах $a = 4\text{ см}$ і $b = 3\text{ см}$, площа $S = 4 \times 3 = 12\text{ см}^2$, діагональ $d = \sqrt{4^2 + 3^2} = 5\text{ см}$.",
        "inputs": [{"id": "sideA", "label": "Сторона A"}, {"id": "sideB", "label": "Сторона B"}],
        "svg": '<rect x="15" y="40" width="170" height="120" fill="none" stroke="#98c379" stroke-width="4"/>'
    },
    "triangle": {
        "title": "Трикутник",
        "desc": "Геометрична фігура, що складається з трьох точок і трьох відрізків.",
        "theory": "Сума кутів будь-якого трикутника дорівнює 180°. Площа обчислюється через сторону та висоту або за формулою Герона.",
        "formulas": [
            {"name": "Площа (через висоту)", "formula": "S = 0.5 · a · h"},
            {"name": "Периметр (рівносторонній)", "formula": "P = 3a"}
        ],
        "example": "Якщо основа $a = 6\text{ см}$, а висота $h = 4\text{ см}$, то площа $S = 0.5 \times 6 \times 4 = 12\text{ см}^2$.",
        "inputs": [{"id": "base", "label": "Основа (a)"}, {"id": "height", "label": "Висота (h)"}],
        "svg": '<polygon points="100,25 25,175 175,175" fill="none" stroke="#e5c07b" stroke-width="4"/>'
    },
    "circle": {
        "title": "Коло",
        "desc": "Геометричне місце точок, рівновіддалених від заданої точки.",
        "theory": "Відношення довжины кола до його діаметра є постійним і дорівнює числу $\pi \approx 3.14159$.",
        "formulas": [
            {"name": "Довжина кола", "formula": "C = 2πr"},
            {"name": "Площа круга", "formula": "S = πr²"}
        ],
        "example": "При радіусі $r = 3\text{ см}$, площа $S = \pi \times 3^2 \approx 28.27\text{ см}^2$.",
        "inputs": [{"id": "radius", "label": "Радіус (r)"}],
        "svg": '<circle cx="100" cy="100" r="75" fill="none" stroke="#e06c75" stroke-width="4"/>'
    },
    "rhombus": {
        "title": "Ромб",
        "desc": "Паралелограм, у якого всі сторони рівні.",
        "theory": "Діагоналі ромба взаємно перпендикулярні і є бісектрисами його кутів.",
        "formulas": [
            {"name": "Площа (через діагоналі)", "formula": "S = 0.5 · d1 · d2"},
            {"name": "Периметр", "formula": "P = 4a"}
        ],
        "example": "Якщо діагоналі $d_1 = 8\text{ см}$, $d_2 = 6\text{ см}$, то площа $S = 0.5 \times 8 \times 6 = 24\text{ см}^2$.",
        "inputs": [{"id": "d1", "label": "Діагональ 1"}, {"id": "d2", "label": "Діагональ 2"}],
        "svg": '<polygon points="100,20 175,100 100,180 25,100" fill="none" stroke="#c678dd" stroke-width="4"/>'
    },
    "trapezoid": {
        "title": "Трапеція",
        "desc": "Чотирикутник, у якого дві сторони паралельні, а дві інші не паралельні.",
        "theory": "Паралельні сторони називаються основами, інші дві — бічними сторонами. Відрізок, що з'єднує середини бічних сторін — середня лінія.",
        "formulas": [
            {"name": "Площа", "formula": "S = ((a + b) / 2) · h"}
        ],
        "example": "Основи $a = 5, b = 7$, висота $h = 4$. Площа: $S = ((5+7)/2) \times 4 = 24$.",
        "inputs": [{"id": "baseA", "label": "Основа a"}, {"id": "baseB", "label": "Основа b"}, {"id": "heightT", "label": "Висота h"}],
        "svg": '<polygon points="50,40 150,40 180,160 20,160" fill="none" stroke="#56b6c2" stroke-width="4"/>'
    },
    "parallelogram": {
        "title": "Паралелограм",
        "desc": "Чотирикутник, у якого протилежні сторони попарно паралельні.",
        "theory": "У паралелограмі протилежні сторони рівні, протилежні кути рівні, а сума сусідніх кутів дорівнює 180°.",
        "formulas": [
            {"name": "Площа", "formula": "S = a · h"},
            {"name": "Периметр", "formula": "P = 2(a + b)"}
        ],
        "example": "Сторона $a = 8$, висота $h = 5$. Площа $S = 8 \times 5 = 40$.",
        "inputs": [{"id": "sideP", "label": "Сторона (a)"}, {"id": "heightP", "label": "Висота (h)"}],
        "svg": '<polygon points="60,40 180,40 140,160 20,160" fill="none" stroke="#abb2bf" stroke-width="4"/>'
    },
    "cube": {
        "title": "Куб",
        "desc": "Правильний багатогранник, кожна грань якого є квадратом.",
        "theory": "У куба 6 граней, 12 ребер та 8 вершин. Усі ребра рівні.",
        "formulas": [
            {"name": "Об'єм", "formula": "V = a³"},
            {"name": "Площа поверхні", "formula": "S = 6a²"}
        ],
        "example": "Ребро $a = 3$. Об'єм $V = 3^3 = 27$. Площа поверхні $S = 6 \times 3^2 = 54$.",
        "inputs": [{"id": "edge", "label": "Ребро куба (a)"}],
        "svg": '<g fill="none" stroke="#61afef" stroke-width="3"><rect x="30" y="60" width="100" height="100"/><rect x="70" y="30" width="100" height="100"/><line x1="30" y1="60" x2="70" y2="30"/><line x1="130" y1="60" x2="170" y2="30"/><line x1="30" y1="160" x2="70" y2="130"/><line x1="130" y1="160" x2="170" y2="130"/></g>'
    },
    "sphere": {
        "title": "Куля (Сфера)",
        "desc": "Геометричне тіло, обмежене сферою.",
        "theory": "Сфера утворюється обертанням півкола навколо його діаметра.",
        "formulas": [
            {"name": "Об'єм кулі", "formula": "V = (4/3)·π·r³"},
            {"name": "Площа сфери", "formula": "S = 4·π·r²"}
        ],
        "example": "Радіус $r = 3$. Площа поверхні $S = 4 \times \pi \times 9 \approx 113.1$.",
        "inputs": [{"id": "sphRadius", "label": "Радіус (r)"}],
        "svg": '<circle cx="100" cy="100" r="70" fill="none" stroke="#98c379" stroke-width="4"/><ellipse cx="100" cy="100" rx="70" ry="25" fill="none" stroke="#98c379" stroke-width="2" stroke-dasharray="5,5"/>'
    },
    "cone": {
        "title": "Конус",
        "desc": "Тіло, отримане обертанням прямокутного трикутника навколо одного з катетів.",
        "theory": "Складається з круглої основи та бічної поверхні, що звужується до вершини.",
        "formulas": [
            {"name": "Об'єм конуса", "formula": "V = (1/3)·π·r²·h"},
            {"name": "Площа основи", "formula": "S_осн = π·r²"}
        ],
        "example": "Радіус основи $r = 3$, висота $h = 4$. Об'єм $V = (1/3) \times \pi \times 9 \times 4 \approx 37.7$.",
        "inputs": [{"id": "coneRad", "label": "Радіус основи"}, {"id": "coneH", "label": "Висота (h)"}],
        "svg": '<ellipse cx="100" cy="160" rx="60" ry="20" fill="none" stroke="#e5c07b" stroke-width="3"/><line x1="100" y1="30" x2="40" y2="160" stroke="#e5c07b" stroke-width="3"/><line x1="100" y1="30" x2="160" y2="160" stroke="#e5c07b" stroke-width="3"/>'
    },
    "cylinder": {
        "title": "Циліндр",
        "desc": "Тіло обертання, утворене поворотом прямокутника навколо однієї зі сторін.",
        "theory": "Має дві паралельні круглі основи однакового радіусу та циліндричну поверхню.",
        "formulas": [
            {"name": "Об'єм", "formula": "V = π·r²·h"},
            {"name": "Площа бічної поверхні", "formula": "S_біч = 2·π·r·h"}
        ],
        "example": "Радіус $r = 2$, висота $h = 5$. Об'єм $V = \pi \times 4 \times 5 \approx 62.83$.",
        "inputs": [{"id": "cylRad", "label": "Радіус (r)"}, {"id": "cylH", "label": "Висота (h)"}],
        "svg": '<ellipse cx="100" cy="40" rx="60" ry="20" fill="none" stroke="#e06c75" stroke-width="3"/><ellipse cx="100" cy="160" rx="60" ry="20" fill="none" stroke="#e06c75" stroke-width="3"/><line x1="40" y1="40" x2="40" y2="160" stroke="#e06c75" stroke-width="3"/><line x1="160" y1="40" x2="160" y2="160" stroke="#e06c75" stroke-width="3"/>'
    },
    "logarithms": {
        "title": "Логарифми",
        "desc": "Показник степеня, до якого потрібно піднести основу, щоб отримати число.",
        "theory": "Рівняння $\log_a(b) = c$ еквівалентне $a^c = b$, де $a > 0, a \neq 1, b > 0$.",
        "formulas": [
            {"name": "Основна властивість", "formula": "a^(log_a(b)) = b"},
            {"name": "Логарифм добутку", "formula": "log_a(x·y) = log_a(x) + log_a(y)"},
            {"name": "Логарифм частки", "formula": "log_a(x/y) = log_a(x) - log_a(y)"}
        ],
        "example": "$\log_2(8) = 3$, оскільки $2^3 = 8$.",
        "inputs": [{"id": "logBase", "label": "Основа (a)"}, {"id": "logNum", "label": "Число (b)"}],
        "svg": '<text x="30" y="110" fill="#c678dd" font-size="45" font-family="monospace">log_a(b)</text>'
    },
    "trigonometry": {
        "title": "Тригонометрія",
        "desc": "Розділ математики, що вивчає залежність між сторонами і кутами трикутників.",
        "theory": "Функції Синус, Косинус, Тангенс визначаються через відношення сторін у прямокутному трикутнику.",
        "formulas": [
            {"name": "Основна тотожність", "formula": "sin²α + cos²α = 1"},
            {"name": "Тангенс кута", "formula": "tgα = sinα / cosα"}
        ],
        "example": "Якщо кут $\alpha = 30^\circ$, то $\sin(30^\circ) = 0.5$, а $\cos(30^\circ) = \sqrt{3}/2 \approx 0.866$.",
        "inputs": [{"id": "angleDeg", "label": "Кут у градусах (α)"}],
        "svg": '<path d="M 30,150 A 50,50 0 0,1 70,120" fill="none" stroke="#56b6c2" stroke-width="3"/><polygon points="30,150 170,150 170,50" fill="none" stroke="#abb2bf" stroke-width="3"/>'
    },
    "quadratic": {
        "title": "Квадратні рівняння",
        "desc": "Рівняння виду ax² + bx + c = 0, де a ≠ 0.",
        "theory": "Кількість коренів залежить від дискримінанта $D = b^2 - 4ac$. Якщо $D > 0$ — два корені, $D = 0$ — один, $D < 0$ — дійсних коренів немає.",
        "formulas": [
            {"name": "Дискримінант", "formula": "D = b² - 4ac"},
            {"name": "Корені рівняння", "formula": "x = (-b ± √D) / 2a"}
        ],
        "example": "Для $x^2 - 5x + 6 = 0$: $D = 25 - 24 = 1$. Корені: $x_1 = (5+1)/2 = 3$, $x_2 = (5-1)/2 = 2$.",
        "inputs": [{"id": "coeffA", "label": "Коефіцієнт a"}, {"id": "coeffB", "label": "Коефіцієнт b"}, {"id": "coeffC", "label": "Коефіцієнт c"}],
        "svg": '<path d="M 20,50 Q 100,180 180,50" fill="none" stroke="#61afef" stroke-width="4"/>'
    }
}

@app.route('/')
def index():
    return render_template('index.html', topics=TOPICS)

@app.route('/formulas')
def formulas():
    return render_template('formulas.html', topics=TOPICS)

@app.route('/topic/<topic_id>')
def topic(topic_id):
    if topic_id == "pifagor":
        return render_template('pifagor.html')
    data = TOPICS.get(topic_id)
    if not data:
        return "Тему не знайдено", 404
    return render_template('topic.html', id=topic_id, data=data)

if __name__ == '__main__':
    app.run(debug=True)
