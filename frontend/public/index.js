function createCircles() {
    const body = document.body;

    const spacing = 900;
    const position = '7%';

    const viewportHeight = window.innerHeight;
    const numCircles = Math.max(1, Math.floor(viewportHeight / spacing));

    for (let i = 0; i < numCircles; i++) {
        const div1 = document.createElement("div");
        const div2 = document.createElement("div");

        if (i % 2 === 0) {
            div1.className = "blur-circle blue-circle";
            div2.className = "blur-circle green-circle";
        } else {
            div1.className = "blur-circle green-circle";
            div2.className = "blur-circle blue-circle";
        }

        const marginTop = i * spacing;
        div1.style.marginTop = `${marginTop}px`;
        div2.style.marginTop = `${marginTop}px`;

        if (i % 2 !== 0) {
            div1.style.left = position;
            div2.style.right = position;
        } else {
            div1.style.left = position;
            div2.style.right = position;
        }

        body.appendChild(div1);
        body.appendChild(div2);
    }
}

document.addEventListener("DOMContentLoaded", createCircles);