<<<<<<< HEAD
// Espera o HTML carregar
window.addEventListener("DOMContentLoaded", () => {

    // Cria a tag <script> do VLibras
    const script = document.createElement("script");
    script.src = "https://vlibras.gov.br/app/vlibras-plugin.js";

    // Quando terminar de carregar, ativa o widget
    script.onload = () => {
        new window.VLibras.Widget('https://vlibras.gov.br/app');
    };

    // Adiciona o script no <head>
    document.head.appendChild(script);


=======
// Espera o HTML carregar
window.addEventListener("DOMContentLoaded", () => {

    // Cria a tag <script> do VLibras
    const script = document.createElement("script");
    script.src = "https://vlibras.gov.br/app/vlibras-plugin.js";

    // Quando terminar de carregar, ativa o widget
    script.onload = () => {
        new window.VLibras.Widget('https://vlibras.gov.br/app');
    };

    // Adiciona o script no <head>
    document.head.appendChild(script);


>>>>>>> bf110d567f6f181621370c7983c6161933701340
});