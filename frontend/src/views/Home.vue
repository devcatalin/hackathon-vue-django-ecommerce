<template>
    <div>
        <h1>Locul unde găsești cele mai bune produse românești</h1>
        <router-link to="/products">
            <svg viewBox="45 60 400 320" xmlns="http://www.w3.org/2000/svg">
                <path
                    fill="#fff"
                    d="M 90 210 C 90 180 90 150 90 150 C 150 150 180 150 180 150 C 180 150 300 150 300 150 C 300 150 330 150 390 150 C 390 150 390 180 390 210 C 390 240 390 270 390 270 C 330 270 300 270 300 270 C 300 270 180 270 180 270 C 180 270 150 270 90 270 C 90 270 90 240 90 210"
                    mask="url(#knockout-text)"
                ></path>
                <mask id="knockout-text">
                    <rect width="100%" height="100%" fill="#fff" x="0" y="0" />
                    <text x="147" y="227" fill="#000">Explorează</text>
                </mask>
            </svg>
        </router-link>
    </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
div {
    position: relative;
    height: 90vh;
    background-image: url("/romania_farm.jpg");
    background-size: cover;
    background-position: center;

    display: grid;
    justify-content: center;
    align-content: center;
}

h1 {
    font-size: 5rem;
    color: white;
    text-align: center;
    font-family: "Gloria Hallelujah", cursive;
    text-shadow: 5px 3px 0px rgba(0, 0, 0, 1);
    transform: translateY(-25%);
    padding: 4.5rem;
}
svg {
    width: 80vw;
    position: fixed;
    bottom: 1vh;
    left: 50vw;
    max-width: 430px;
    transform: translateX(-50%);
    z-index: 2;

    filter: drop-shadow(0 0 40px rgba(0, 0, 0, 0.3));

    path {
        cursor: pointer;
        animation: blob 2s infinite forwards;
        transform-origin: 50% 50%;

        &:hover {
            fill: #fafafa;
        }
    }

    text {
        font-size: 45px;
        transform: translateX(-6.5%);
        font-family: "Raleway", sans-serif;
    }
}

@keyframes blob {
    25% {
        d: path(
            "M 90 210 C 90 180 110 160 130 160 C 160 160 180 140 200 130 C 230 120 270 100 290 140 C 310 170 340 100 360 140 C 370 160 390 180 390 210 C 390 240 380 290 350 280 C 330 270 300 280 280 290 C 260 300 230 300 220 290 C 200 270 160 310 140 280 C 130 260 90 240 90 210 "
        );
        transform: rotate(-5deg);
    }
    50% {
        d: path(
            "M 90 210 C 90 180 100 150 120 130 C 150 100 180 140 200 130 C 230 120 270 100 290 140 C 300 160 330 130 360 140 C 390 150 390 180 390 210 C 390 240 380 300 350 280 C 330 270 320 230 280 260 C 260 280 220 310 200 290 C 180 270 160 280 140 280 C 110 280 90 240 90 210"
        );
    }
    75% {
        d: path(
            "M 90 210 C 90 180 110 180 130 170 C 150 160 170 130 200 130 C 240 130 260 150 290 140 C 310 130 340 120 360 140 C 380 160 390 180 390 210 C 390 240 380 260 350 270 C 320 280 290 270 270 260 C 240 250 230 280 210 290 C 180 310 130 300 110 280 C 90 260 90 240 90 210"
        );
        transform: rotate(5deg);
    }
}
</style>
