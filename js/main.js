(function ($) {
    "use strict";

    async function loadPartials() {

        async function loadFile(paths) {
            for (const path of paths) {
                try {
                    const res = await fetch(path);
                    if (res.ok) {
                        return await res.text();
                    }
                } catch (e) { }
            }
            return "";
        }

        try {

            // Load spinner trước để hiển thị ngay
            const spinner = await loadFile([
                "../spinner.html",
                "spinner.html"
            ]);

            if (spinner) {
                document.body.insertAdjacentHTML("afterbegin", spinner);
            }

            // Load header + footer song song
            const [header, footer] = await Promise.all([
                loadFile(["../header.html", "header.html"]),
                loadFile(["../footer.html", "footer.html"])
            ]);

            if (header) {
                document.body.insertAdjacentHTML("afterbegin", header);
            }

            if (footer) {
                document.body.insertAdjacentHTML("beforeend", footer);
            }

        } catch (err) {
            console.error("Partial load error:", err);
        }

        // Ẩn spinner
        setTimeout(() => {
            const spinnerEl = document.getElementById("spinner");
            if (spinnerEl) spinnerEl.classList.remove("show");

            const overlay = document.querySelector(".spinner-overlay");
            if (overlay) overlay.classList.add("d-none");
        }, 400);
    }


    function setActiveMenu() {

        const current = window.location.pathname;

        document.querySelectorAll(".navbar-nav .nav-link").forEach(link => {

            const href = link.getAttribute("href");
            if (!href) return;

            if (href.includes("brands") && current.includes("brands")) {
                link.classList.add("active");
            }

            if (current.endsWith(href)) {
                link.classList.add("active");
            }

        });
    }


    function initUI() {

        new WOW().init();

        const $dropdown = $(".dropdown");
        const $dropdownToggle = $(".dropdown-toggle");
        const $dropdownMenu = $(".dropdown-menu");
        const showClass = "show";

        $(window).on("load resize", function () {

            if (window.matchMedia("(min-width: 992px)").matches) {

                $dropdown.hover(
                    function () {
                        const $this = $(this);
                        $this.addClass(showClass);
                        $this.find($dropdownToggle).attr("aria-expanded", "true");
                        $this.find($dropdownMenu).addClass(showClass);
                    },
                    function () {
                        const $this = $(this);
                        $this.removeClass(showClass);
                        $this.find($dropdownToggle).attr("aria-expanded", "false");
                        $this.find($dropdownMenu).removeClass(showClass);
                    }
                );

            } else {
                $dropdown.off("mouseenter mouseleave");
            }

        });

        // Back to top
        $(window).scroll(function () {

            if ($(this).scrollTop() > 300) {
                $('.back-to-top').fadeIn('slow');
                $('.sticky-top').css('top', '0px');
            } else {
                $('.back-to-top').fadeOut('slow');
                $('.sticky-top').css('top', '-100px');
            }

        });

        $('.back-to-top').click(function () {
            $('html, body').animate({ scrollTop: 0 }, 1500, 'easeInOutExpo');
            return false;
        });

        // Header carousel
        $(".header-carousel").owlCarousel({
            autoplay: true,
            smartSpeed: 1500,
            items: 1,
            dots: false,
            loop: true,
            nav: true,
            navText: [
                '<i class="bi bi-chevron-left"></i>',
                '<i class="bi bi-chevron-right"></i>'
            ]
        });

        // Testimonials carousel
        $(".testimonial-carousel").owlCarousel({
            autoplay: true,
            smartSpeed: 1000,
            center: true,
            margin: 24,
            dots: true,
            loop: true,
            nav: false,
            responsive: {
                0: { items: 1 },
                576: { items: 2 },
                768: { items: 3 },
                992: { items: 4 }
            }
        });

    }


    $(async function () {

        await loadPartials();   // load header/footer trước

        initUI();               // sau đó init UI
        setActiveMenu();        // active menu

    });

})(jQuery);