<template>
  <el-container class="main">
    <el-header>
      <BasicHeader />
    </el-header>
    <el-container>
      <el-aside :width="menuWidth">
        <SideMenu :isCollapse="isCollapse" @menuSelect="(item) => { $emit('menuSelect', item)}"/>

      </el-aside>
      <el-main><slot></slot></el-main>
    </el-container>
  </el-container>
</template>

<script>
import BasicHeader from "@/components/BasicHeader";
import SideMenu from "@/components/layouts/SideMenu";
import useBreakpoint from "@/composables/useBreakpoint";
import {computed} from "vue";

export default {
  name: "BasicLayout",
  components: {SideMenu, BasicHeader},
  setup() {
    const {type} = useBreakpoint();
    const isCollapse = computed(() => type.value == "sm");
    const menuWidth = computed(() => isCollapse.value ? "65px" : "200px")

    return {
      isCollapse,
      menuWidth,
    };
  },

};
</script>

<style scoped>
.el-header {
  background: #409eff;
  color: #fff;
  display: flex;
  align-items: center;
}

.main {
  height: 100%;
}
</style>