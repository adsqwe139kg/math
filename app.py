from flask import Flask, render_template

app = Flask(__name__)

TOPICS = {
    "square": {
        "title": "Квадрат",
        "desc": "Чотирикутник, у якого всі сторони рівні і всі кути прямі.",
        "theory": "Квадрат є окремим випадком прямокутника, ромба та паралелограма. Має 4 осі симетрії.",
        "formulas": [{"name": "Периметр", "formula": "P = 4a"}, {"name": "Площа", "formula": "S = a²"}, {"name": "Діагональ", "formula": "d = a√2"}],
        "example": "Якщо сторона квадрата a = 5 см, то його площа S = 25 см², а периметр P = 20 см.",
        "inputs": [{"id": "side", "label": "Сторона (a)"}],
        "svg": '<rect x="25" y="25" width="150" height="150" fill="none" stroke="#61afef" stroke-width="4"/>'
    },
    "rectangle": {
        "title": "Прямокутник",
        "desc": "Чотирикутник, у якого всі кути прямі.",
        "theory": "Протилежні сторони прямокутника рівні та паралельні.",
        "formulas": [{"name": "Площа", "formula": "S = a · b"}, {"name": "Периметр", "formula": "P = 2(a + b)"}],
        "example": "При сторонах a = 4 см і b = 3 см, площа S = 12 см².",
        "inputs": [{"id": "sideA", "label": "Сторона A"}, {"id": "sideB", "label": "Сторона B"}],
        "svg": '<rect x="15" y="40" width="170" height="120" fill="none" stroke="#98c379" stroke-width="4"/>'
    },
    "triangle": {
        "title": "Трикутник",
        "desc": "Фігура з трьох точок і трьох відрізків.",
        "theory": "Сума кутів будь-якого трикутника дорівнює 180°.",
        "formulas": [{"name": "Площа", "formula": "S = 0.5 · a · h"}],
        "example": "Основа a = 6 см, висота h = 4 см, площа S = 12 см².",
        "inputs": [{"id": "base", "label": "Основа (a)"}, {"id": "height", "label": "Висота (h)"}],
        "svg": '<polygon points="100,25 25,175 175,175" fill="none" stroke="#e5c07b" stroke-width="4"/>'
    },
    "circle": {
        "title": "Коло",
        "desc": "Геометричне місце точок, рівновіддалених від центра.",
        "theory": "Відношення довжини кола до діаметра дорівнює числу π.",
        "formulas": [{"name": "Довжина кола", "formula": "C = 2πr"}, {"name": "Площа круга", "formula": "S = πr²"}],
        "example": "При радіусі r = 3 см, площа S ≈ 28.27 см².",
        "inputs": [{"id": "radius", "label": "Радіус (r)"}],
        "svg": '<circle cx="100" cy="100" r="75" fill="none" stroke="#e06c75" stroke-width="4"/>'
    },
    "rhombus": {
        "title": "Ромб",
        "desc": "Паралелограм, у якого всі сторони рівні.",
        "theory": "Діагоналі ромба взаємно перпендикулярні.",
        "formulas": [{"name": "Площа", "formula": "S = 0.5 · d1 · d2"}],
        "example": "Діагоналі 8 см і 6 см, площа S = 24 см².",
        "inputs": [{"id": "d1", "label": "Діагональ 1"}, {"id": "d2", "label": "Діагональ 2"}],
        "svg": '<polygon points="100,20 175,100 100,180 25,100" fill="none" stroke="#c678dd" stroke-width="4"/>'
    },
    "trapezoid": {
        "title": "Трапеція",
        "desc": "Чотирикутник, у якого дві сторони паралельні.",
        "theory": "Паралельні сторони — основи, інші дві — бічні.",
        "formulas": [{"name": "Площа", "formula": "S = ((a + b) / 2) · h"}],
        "example": "Основи 5 і 7, висота 4. Площа: S = 24.",
        "inputs": [{"id": "baseA", "label": "Основа a"}, {"id": "baseB", "label": "Основа b"}, {"id": "heightT", "label": "Висота h"}],
        "svg": '<polygon points="50,40 150,40 180,160 20,160" fill="none" stroke="#56b6c2" stroke-width="4"/>'
    },
    "parallelogram": {
        "title": "Паралелограм",
        "desc": "Чотирикутник, у якого протилежні сторони паралельні.",
        "theory": "У паралелограмі протилежні сторони і кути рівні.",
        "formulas": [{"name": "Площа", "formula": "S = a · h"}],
        "example": "Сторона a = 8, висота h = 5. Площа S = 40.",
        "inputs": [{"id": "sideP", "label": "Сторона (a)"}, {"id": "heightP", "label": "Висота (h)"}],
        "svg": '<polygon points="60,40 180,40 140,160 20,160" fill="none" stroke="#abb2bf" stroke-width="4"/>'
    },
    "cube": {
        "title": "Куб",
        "desc": "Правильний багатогранник, кожна грань якого є квадратом.",
        "theory": "У куба 6 граней, 12 ребер та 8 вершин.",
        "formulas": [{"name": "Об'єм", "formula": "V = a³"}, {"name": "Поверхня", "formula": "S = 6a²"}],
        "example": "Ребро a = 3. Об'єм V = 27.",
        "inputs": [{"id": "edge", "label": "Ребро куба (a)"}],
        "svg": '<g fill="none" stroke="#61afef" stroke-width="3"><rect x="30" y="60" width="100" height="100"/><rect x="70" y="30" width="100" height="100"/><line x1="30" y1="60" x2="70" y2="30"/><line x1="130" y1="60" x2="170" y2="30"/><line x1="30" y1="160" x2="70" y2="130"/><line x1="130" y1="160" x2="170" y2="130"/></g>'
    },
    "sphere": {
        "title": "Куля (Сфера)",
        "desc": "Геометричне тіло, обмежене сферою.",
        "theory": "Утворюється обертанням півкола навколо діаметра.",
        "formulas": [{"name": "Об'єм кулі", "formula": "V = (4/3)·π·r³"}],
        "example": "Радіус r = 3. Об'єм V ≈ 113.1.",
        "inputs": [{"id": "sphRadius", "label": "Радіус (r)"}],
        "svg": '<circle cx="100" cy="100" r="70" fill="none" stroke="#98c379" stroke-width="4"/><ellipse cx="100" cy="100" rx="70" ry="25" fill="none" stroke="#98c379" stroke-width="2" stroke-dasharray="5,5"/>'
    },
    "cone": {
        "title": "Конус",
        "desc": "Тіло, отримане обертанням прямокутного трикутника.",
        "theory": "Складається з круглої основи та бічної поверхні.",
        "formulas": [{"name": "Об'єм", "formula": "V = (1/3)·π·r²·h"}],
        "example": "Радіус r = 3, висота h = 4. Об'єм V ≈ 37.7.",
        "inputs": [{"id": "coneRad", "label": "Радіус основи"}, {"id": "coneH", "label": "Висота (h)"}],
        "svg": '<ellipse cx="100" cy="160" rx="60" ry="20" fill="none" stroke="#e5c07b" stroke-width="3"/><line x1="100" y1="30" x2="40" y2="160" stroke="#e5c07b" stroke-width="3"/><line x1="100" y1="30" x2="160" y2="160" stroke="#e5c07b" stroke-width="3"/>'
    },
    "cylinder": {
        "title": "Циліндр",
        "desc": "Тіло обертання, утворене поворотом прямокутника.",
        "theory": "Має дві паралельні круглі основи.",
        "formulas": [{"name": "Об'єм", "formula": "V = π·r²·h"}],
        "example": "Радіус r = 2, висота h = 5. Об'єм V ≈ 62.83.",
        "inputs": [{"id": "cylRad", "label": "Радіус (r)"}, {"id": "cylH", "label": "Висота (h)"}],
        "svg": '<ellipse cx="100" cy="40" rx="60" ry="20" fill="none" stroke="#e06c75" stroke-width="3"/><ellipse cx="100" cy="160" rx="60" ry="20" fill="none" stroke="#e06c75" stroke-width="3"/><line x1="40" y1="40" x2="40" y2="160" stroke="#e06c75" stroke-width="3"/><line x1="160" y1="40" x2="160" y2="160" stroke="#e06c75" stroke-width="3"/>'
    },
    "logarithms": {
        "title": "Логарифми",
        "desc": "Показник степеня, до якого потрібно піднести основу.",
        "theory": "Рівняння log_a(b) = c означає a^c = b.",
        "formulas": [{"name": "Добуток", "formula": "log_a(x·y) = log_a(x) + log_a(y)"}],
        "example": "log_2(8) = 3, бо 2³ = 8.",
        "inputs": [{"id": "logBase", "label": "Основа (a)"}, {"id": "logNum", "label": "Число (b)"}],
        "svg": '<text x="30" y="110" fill="#c678dd" font-size="45" font-family="monospace">log_a(b)</text>'
    },
    "trigonometry": {
        "title": "Тригонометрія",
        "desc": "Вивчає залежність між сторонами і кутами.",
        "theory": "Синус, Косинус, Тангенс визначаються через прямокутний трикутник.",
        "formulas": [{"name": "Тотожність", "formula": "sin²α + cos²α = 1"}],
        "example": "sin(30°) = 0.5.",
        "inputs": [{"id": "angleDeg", "label": "Кут у градусах (α)"}],
        "svg": '<path d="M 30,150 A 50,50 0 0,1 70,120" fill="none" stroke="#56b6c2" stroke-width="3"/><polygon points="30,150 170,150 170,50" fill="none" stroke="#abb2bf" stroke-width="3"/>'
    },
    "quadratic": {
        "title": "Квадратні рівняння",
        "desc": "Рівняння виду ax² + bx + c = 0.",
        "theory": "Кількість коренів залежить від дискримінанта D = b² - 4ac.",
        "formulas": [{"name": "Дискримінант", "formula": "D = b² - 4ac"}],
        "example": "x² - 5x + 6 = 0: D = 1. Корені: 3 і 2.",
        "inputs": [{"id": "coeffA", "label": "Коефіцієнт a"}, {"id": "coeffB", "label": "Коефіцієнт b"}, {"id": "coeffC", "label": "Коефіцієнт c"}],
        "svg": '<path d="M 20,50 Q 100,180 180,50" fill="none" stroke="#61afef" stroke-width="4"/>'
    }
}

@app.route('/')
def index(): return render_template('index.html', topics=TOPICS)

@app.route('/formulas')
def formulas(): return render_template('formulas.html', topics=TOPICS)

@app.route('/topic/<topic_id>')
def topic(topic_id):
    if topic_id == "pifagor": return render_template('pifagor.html')
    return render_template('topic.html', id=topic_id, data=TOPICS.get(topic_id))

if __name__ == '__main__':
    app.run(debug=True)