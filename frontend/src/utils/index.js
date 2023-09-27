export default function handlePopState() {
    function deleteAllCircles() {
        const circles = document.querySelectorAll('.blur-circle')
        circles.forEach(circle => {
            circle.remove()
        })
    }
    deleteAllCircles();

    function createCircles() {
        const app = document.getElementById("app");
        const body = document.body;
    
        const spacing = 900;
        const position = '7%';
    
        const appHeight = app.clientHeight;
        const numCircles = Math.max(1, Math.floor(appHeight / spacing));
    
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
    
            if (i == 0) {
                div1.style.top = `250px`;
                div2.style.top = `250px`;
            } else {
                const marginTop = i * spacing;
                div1.style.top = `${marginTop}px`;
                div2.style.top = `${marginTop}px`;
            }
    
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
    createCircles();
}