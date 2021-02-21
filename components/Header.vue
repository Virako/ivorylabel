<template>
  <header class="header">
    <div class="white-bg" />
    <div class="header-bg" />
    <div class="header-text">
      <nuxt-link class="logo" :to="localeRoute('/')">
        <img class="logo-img" src="@/assets/images/logo.svg" alt="logo" />
      </nuxt-link>
      <Menu />
    </div>
  </header>
</template>

<style>
.header {
  position: sticky;
  z-index: 2;
  top: 0;
  display: flex;
  align-items: center;
  height: var(--height-header);
  justify-content: space-between;
}

.white-bg {
  position: absolute;
  background-color: white;
  height: var(--height-header);
  width: 100%;
}

.header-bg {
  position: absolute;
  filter: opacity(70%) grayscale(100%);
  background-image: url("~@/assets/images/bg_header.jpg");
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  height: var(--height-header);
  width: 100%;
}

.header-text {
  position: absolute;
  text-align: center;
  margin: auto;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}

.logo-img {
  filter: contrast(100%);
  width: 300px;
}
</style>

