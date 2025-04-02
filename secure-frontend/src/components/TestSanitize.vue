<template>
  <div>
    <div v-html="safeContent"></div>
  </div>
</template>

<script>
import { sanitize } from '@/helpers/sanitize';

export default {
  data() {
    return {
      userContent: '<img src="x" onerror="alert(\'XSS\')">'
    };
  },
  computed: {
    safeContent() {
      return sanitize(this.userContent);
    }
  }
};
</script>
