document.addEventListener("DOMContentLoaded", function () {
    // Мобільна навігація
    const mobileMenu = document.getElementById("mobile-menu");
    const navbar = document.getElementById("navbar");

    if (mobileMenu) {
        mobileMenu.addEventListener("click", () => {
            navbar.classList.toggle("active");
            mobileMenu.classList.toggle("open");
        });
    }
            const noResults = document.getElementById("no-results");
            if (anyVisible) {
                noResults.classList.add("hidden");
            } else {
                noResults.classList.remove("hidden");
            }
        });
    }

    // Пошук у таблиці формул
    const formulaSearch = document.getElementById("formula-search");
    if (formulaSearch) {
        formulaSearch.addEventListener("input", function (e) {
            const query = e.target.value.toLowerCase().trim();
            const rows = document.querySelectorAll("#formula-table tbody tr");

            rows.forEach(row => {
                const searchData = row.getAttribute("data-search");
                if (searchData.includes(query)) {
                    row.classList.remove("hidden");
                } else {
                    row.classList.add("hidden");
                }
            });
        });
    }


    const topicPage = document.getElementById("topic-page");
    const btnCompute = document.getElementById("btn-compute");
    const calcResult = document.getElementById("calc-result");

    if (topicPage && btnCompute) {
        const topicId = topicPage.getAttribute("data-topic-id");

        btnCompute.addEventListener("click", function () {
            let htmlResult = "";

            if (topicId === "square") {
                const side = parseFloat(document.getElementById("side").value);
                if (side > 0) {
                    htmlResult = `<p><strong>Периметр (P):</strong> ${(4 * side).toFixed(2)}</p>
                                  <p><strong>Площа (S):</strong> ${(side * side).toFixed(2)}</p>
                                  <p><strong>Діагональ (d):</strong> ${(side * Math.sqrt(2)).toFixed(2)}</p>`;
                }
            } 
            else if (topicId === "rectangle") {
                const a = parseFloat(document.getElementById("sideA").value);
                const b = parseFloat(document.getElementById("sideB").value);
                if (a > 0 && b > 0) {
                    htmlResult = `<p><strong>Площа (S):</strong> ${(a * b).toFixed(2)}</p>
                                  <p><strong>Периметр (P):</strong> ${(2 * (a + b)).toFixed(2)}</p>
                                  <p><strong>Діагональ (d):</strong> ${Math.sqrt(a*a + b*b).toFixed(2)}</p>`;
                }
            } 
            else if (topicId === "triangle") {
                const base = parseFloat(document.getElementById("base").value);
                const height = parseFloat(document.getElementById("height").value);
                if (base > 0 && height > 0) {
                    htmlResult = `<p><strong>Площа (S):</strong> ${(0.5 * base * height).toFixed(2)}</p>`;
                }
            } 
            else if (topicId === "circle") {
                const r = parseFloat(document.getElementById("radius").value);
                if (r > 0) {
                    htmlResult = `<p><strong>Довжина кола (C):</strong> ${(2 * Math.PI * r).toFixed(2)}</p>
                                  <p><strong>Площа круга (S):</strong> ${(Math.PI * r * r).toFixed(2)}</p>`;
                }
            } 
            else if (topicId === "rhombus") {
                const d1 = parseFloat(document.getElementById("d1").value);
                const d2 = parseFloat(document.getElementById("d2").value);
                if (d1 > 0 && d2 > 0) {
                    htmlResult = `<p><strong>Площа (S):</strong> ${(0.5 * d1 * d2).toFixed(2)}</p>`;
                }
            } 
            else if (topicId === "trapezoid") {
                const a = parseFloat(document.getElementById("baseA").value);
                const b = parseFloat(document.getElementById("baseB").value);
                const h = parseFloat(document.getElementById("heightT").value);
                if (a > 0 && b > 0 && h > 0) {
                    htmlResult = `<p><strong>Площа (S):</strong> ${(((a + b) / 2) * h).toFixed(2)}</p>`;
                }
            } 
            else if (topicId === "parallelogram") {
                const a = parseFloat(document.getElementById("sideP").value);
                const h = parseFloat(document.getElementById("heightP").value);
                if (a > 0 && h > 0) {
                    htmlResult = `<p><strong>Площа (S):</strong> ${(a * h).toFixed(2)}</p>`;
                }
            } 
            else if (topicId === "cube") {
                const a = parseFloat(document.getElementById("edge").value);
                if (a > 0) {
                    htmlResult = `<p><strong>Об'єм (V):</strong> ${Math.pow(a, 3).toFixed(2)}</p>
                                  <p><strong>Площа поверхні (S):</strong> ${(6 * a * a).toFixed(2)}</p>`;
                }
            } 
            else if (topicId === "sphere") {
                const r = parseFloat(document.getElementById("sphRadius").value);
                if (r > 0) {
                    htmlResult = `<p><strong>Об'єм (V):</strong> ${((4/3) * Math.PI * Math.pow(r, 3)).toFixed(2)}</p>
                                  <p><strong>Площа сфери (S):</strong> ${(4 * Math.PI * r * r).toFixed(2)}</p>`;
                }
            } 
            else if (topicId === "cone") {
                const r = parseFloat(document.getElementById("coneRad").value);
                const h = parseFloat(document.getElementById("coneH").value);
                if (r > 0 && h > 0) {
                    htmlResult = `<p><strong>Об'єм (V):</strong> ${((1/3) * Math.PI * r * r * h).toFixed(2)}</p>`;
                }
            } 
            else if (topicId === "cylinder") {
                const r = parseFloat(document.getElementById("cylRad").value);
                const h = parseFloat(document.getElementById("cylH").value);
                if (r > 0 && h > 0) {
                    htmlResult = `<p><strong>Об'єм (V):</strong> ${(Math.PI * r * r * h).toFixed(2)}</p>
                                  <p><strong>Площа бічної поверхні:</strong> ${(2 * Math.PI * r * h).toFixed(2)}</p>`;
                }
            } 
            else if (topicId === "logarithms") {
                const a = parseFloat(document.getElementById("logBase").value);
                const b = parseFloat(document.getElementById("logNum").value);
                if (a > 0 && a !== 1 && b > 0) {
                    htmlResult = `<p><strong>Результат log_a(b):</strong> ${(Math.log(b) / Math.log(a)).toFixed(4)}</p>`;
                } else {
                    htmlResult = `<span style="color:var(--danger)">Помилка ОДЗ логарифма!</span>`;
                }
            } 
            else if (topicId === "trigonometry") {
                const deg = parseFloat(document.getElementById("angleDeg").value);
                if (!isNaN(deg)) {
                    const rad = deg * (Math.PI / 180);
                    htmlResult = `<p><strong>sin(α):</strong> ${Math.sin(rad).toFixed(4)}</p>
                                  <p><strong>cos(α):</strong> ${Math.cos(rad).toFixed(4)}</p>
                                  <p><strong>tg(α):</strong> ${Math.abs(deg % 180) === 90 ? 'Не існує' : Math.tan(rad).toFixed(4)}</p>`;
                }
            } 
            else if (topicId === "quadratic") {
                const a = parseFloat(document.getElementById("coeffA").value);
                const b = parseFloat(document.getElementById("coeffB").value);
                const c = parseFloat(document.getElementById("coeffC").value);
                if (a === 0) {
                    htmlResult = `<span style="color:var(--danger)">Коефіцієнт 'a' не може дорівнювати 0!</span>`;
                } else {
                    const D = b*b - 4*a*c;
                    htmlResult = `<p><strong>Дискримінант (D):</strong> ${D.toFixed(2)}</p>`;
                    if (D > 0) {
                        const x1 = (-b + Math.sqrt(D)) / (2*a);
                        const x2 = (-b - Math.sqrt(D)) / (2*a);
                        htmlResult += `<p><strong>x₁:</strong> ${x1.toFixed(2)}</p><p><strong>x₂:</strong> ${x2.toFixed(2)}</p>`;
                    } else if (D === 0) {
                        const x = -b / (2*a);
                        htmlResult += `<p><strong>Єдиний корінь x:</strong> ${x.toFixed(2)}</p>`;
                    } else {
                        htmlResult += `<p style="color:var(--warning)">Дійсних коренів немає (D < 0)</p>`;
                    }
                }
            }
            else if (topicId === "pifagor") {
                const a = parseFloat(document.getElementById("sideA").value);
                const b = parseFloat(document.getElementById("sideB").value);
                const c = parseFloat(document.getElementById("hypC").value);
                
                let inputsCount = [a, b, c].filter(x => !isNaN(x) && x > 0).length;
                if (inputsCount !== 2) {
                    htmlResult = `<span style="color:var(--danger)">Заповніть рівно 2 будь-які поля!</span>`;
                } else {
                    if (isNaN(c)) {
                        htmlResult = `<p><strong>Гіпотенуза c:</strong> ${Math.sqrt(a*a + b*b).toFixed(2)}</p>`;
                    } else if (isNaN(a)) {
                        if (c > b) {
                            htmlResult = `<p><strong>Катет a:</strong> ${Math.sqrt(c*c - b*b).toFixed(2)}</p>`;
                        } else { htmlResult = `<span style="color:var(--danger)">c повинно бути більше b!</span>`; }
                    } else if (isNaN(b)) {
                        if (c > a) {
                            htmlResult = `<p><strong>Катет b:</strong> ${Math.sqrt(c*c - a*a).toFixed(2)}</p>`;
                        } else { htmlResult = `<span style="color:var(--danger)">c повинно бути більше a!</span>`; }
                    }
                }
            }

            if (htmlResult) {
                calcResult.innerHTML = htmlResult;
                calcResult.classList.remove("hidden");
            } else if (!calcResult.classList.contains("hidden") && htmlResult === "") {
                calcResult.innerHTML = `<span style="color:var(--danger)">Перевірте коректність введених даних. Числа мають бути більші за 0!</span>`;
                calcResult.classList.remove("hidden");
            }
        });
    }
});
