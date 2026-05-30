document.addEventListener('DOMContentLoaded', () => {
    const topicContainer = document.querySelector('.topic-container');
    if (!topicContainer) return;

    const topicId = topicContainer.getAttribute('data-topic-id');

    if (topicId === 'pifagor') {
        const katetA = document.getElementById('katetA');
        const katetB = document.getElementById('katetB');
        const result = document.getElementById('pifagor-result');

        const calcPifagor = () => {
            const a = parseFloat(katetA.value);
            const b = parseFloat(katetB.value);
            if (a > 0 && b > 0) {
                result.textContent = `c = ${Math.sqrt(a*a + b*b).toFixed(2)}`;
            } else {
                result.textContent = 'Введіть коректні дані...';
            }
        };
        ['input', 'change'].forEach(evt => {
            katetA.addEventListener(evt, calcPifagor);
            katetB.addEventListener(evt, calcPifagor);
        });
        return;
    }

    const inputs = document.querySelectorAll('.calc-input');
    const resultDisplay = document.getElementById('calc-result');

    const calculate = () => {
        let values = {};
        inputs.forEach(input => { values[input.id] = parseFloat(input.value); });

        let out = '';
        switch(topicId) {
            case 'square':
                if(values.side > 0) out = `S = ${values.side ** 2} | P = ${values.side * 4}`;
                break;
            case 'rectangle':
                if(values.sideA > 0 && values.sideB > 0) out = `S = ${values.sideA * values.sideB} | P = ${2 * (values.sideA + values.sideB)}`;
                break;
            case 'triangle':
                if(values.base > 0 && values.height > 0) out = `S = ${0.5 * values.base * values.height}`;
                break;
            case 'circle':
                if(values.radius > 0) out = `S = ${(Math.PI * values.radius ** 2).toFixed(2)} | C = ${(2 * Math.PI * values.radius).toFixed(2)}`;
                break;
            case 'rhombus':
                if(values.d1 > 0 && values.d2 > 0) out = `S = ${0.5 * values.d1 * values.d2}`;
                break;
            case 'trapezoid':
                if(values.baseA > 0 && values.baseB > 0 && values.heightT > 0) out = `S = ${((values.baseA + values.baseB) / 2) * values.heightT}`;
                break;
            case 'parallelogram':
                if(values.sideP > 0 && values.heightP > 0) out = `S = ${values.sideP * values.heightP}`;
                break;
            case 'cube':
                if(values.edge > 0) out = `V = ${values.edge ** 3} | S_пов = ${6 * (values.edge ** 2)}`;
                break;
            case 'sphere':
                if(values.sphRadius > 0) out = `V = ${((4/3) * Math.PI * values.sphRadius ** 3).toFixed(2)}`;
                break;
            case 'cone':
                if(values.coneRad > 0 && values.coneH > 0) out = `V = ${((1/3) * Math.PI * (values.coneRad ** 2) * values.coneH).toFixed(2)}`;
                break;
            case 'cylinder':
                if(values.cylRad > 0 && values.cylH > 0) out = `V = ${(Math.PI * (values.cylRad ** 2) * values.cylH).toFixed(2)}`;
                break;
            case 'logarithms':
                if(values.logBase > 0 && values.logBase !== 1 && values.logNum > 0) out = `Результат = ${(Math.log(values.logNum) / Math.log(values.logBase)).toFixed(4)}`;
                else out = 'Недопустимі дані!';
                break;
            case 'trigonometry':
                if(!isNaN(values.angleDeg)) {
                    let rad = values.angleDeg * Math.PI / 180;
                    out = `sin = ${Math.sin(rad).toFixed(4)} | cos = ${Math.cos(rad).toFixed(4)} | tg = ${Math.sin(rad) ? Math.tan(rad).toFixed(4) : 'не існує'}`;
                }
                break;
            case 'quadratic':
                if(!isNaN(values.coeffA) && !isNaN(values.coeffB) && !isNaN(values.coeffC)) {
                    if (values.coeffA === 0) out = 'Це лінійне рівняння!';
                    else {
                        let D = values.coeffB**2 - 4*values.coeffA*values.coeffC;
                        if(D > 0) {
                            let x1 = (-values.coeffB + Math.sqrt(D)) / (2*values.coeffA);
                            let x2 = (-values.coeffB - Math.sqrt(D)) / (2*values.coeffA);
                            out = `D = ${D} | x1 = ${x1.toFixed(2)}, x2 = ${x2.toFixed(2)}`;
                        } else if(D === 0) {
                            out = `D = 0 | x = ${(-values.coeffB / (2*values.coeffA)).toFixed(2)}`;
                        } else out = `D = ${D} | Коренів немає`;
                    }
                }
                break;
        }
        resultDisplay.textContent = out || 'Введіть дані у поля вище...';
    };

    inputs.forEach(input => {
        ['input', 'change'].forEach(evt => input.addEventListener(evt, calculate));
    });
});