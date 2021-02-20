<template>
  <header class="header">
    <header-bg class="header-bg" />
    <content class="content">
      <nuxt-link class="logo" :to="localeRoute('/')">
        <img class="logo-img" src="@/assets/images/logo.svg" alt="logo" />
      </nuxt-link>
      <Menu />
    </content>
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

.header-bg {
  position: fixed;
  filter: opacity(70%) grayscale(100%);
  background-image: url("~@/assets/images/bg_header.jpg");
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  height: var(--height-header);
  width: 100%;
}

.content {
  position: fixed;
  text-align: center;
  margin: auto;
  width: 100%;
}

.logo-img {
  filter: contrast(100%);
  width: 300px;
}
</style>

