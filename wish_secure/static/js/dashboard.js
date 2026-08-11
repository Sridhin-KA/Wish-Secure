document.addEventListener("DOMContentLoaded", function () {

    const cards = document.querySelectorAll(
        ".dashboard-stat, .latest-card, .activity-item"
    );

    cards.forEach(function (card, index) {

        card.style.opacity = "0";

        card.style.transform = "translateY(20px)";

        setTimeout(function () {

            card.style.transition =
                "opacity 0.5s ease, transform 0.5s ease";

            card.style.opacity = "1";

            card.style.transform =
                "translateY(0)";

        }, index * 80);

    });

});