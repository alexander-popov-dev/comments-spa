  import { defineStore } from 'pinia'
  import { ref } from 'vue'

  export const useCommentsStore = defineStore('comments', () => {
    const comments = ref([])
    const loading = ref(false)

    async function fetchComments() {
      loading.value = true
      // тут будет запрос через axios
      loading.value = false
    }

    return { comments, loading, fetchComments }
  })
