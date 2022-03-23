<template>
  <BasicLayout @menuSelect="(item) => { content=item}">
    <MainContent :content="content"/>
  </BasicLayout>
</template>


<script>

import BasicLayout from "@/components/layouts/BasicLayout";
import MainContent from "@/components/layouts/MainContent";

export default {
  name: 'App',
  components: {MainContent, BasicLayout},
  data() {
    return {
      content: {
        label: "대시보드",
        index: "Dashboard",
        path: "main",

      },
    };
  },
};
</script>

<style>
</style>
