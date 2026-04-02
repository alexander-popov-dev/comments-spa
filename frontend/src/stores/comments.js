import {defineStore} from 'pinia'
import {ref} from 'vue'
import api from '@/api/index.js'

const useCommentsStore = defineStore('comments', () => {
    const comments = ref([])
    const loading = ref(false)
    const totalCount = ref(0)
    const currentPage = ref(1)
    const orderField = ref('created_at')
    const orderDir = ref('desc')

    async function fetchComments(page = 1) {
        loading.value = true
        const ordering = (orderDir.value === 'desc' ? '-' : '') + orderField.value
        const response = await api.get('/api/v1/comment/', {params: {page, ordering}})
        comments.value = response.data.results
        totalCount.value = response.data.count
        currentPage.value = page
        loading.value = false
    }

    function setOrdering(field, dir) {
        orderField.value = field
        orderDir.value = dir
        fetchComments(1)
    }

    async function fetchReplies(commentId) {
        const response = await api.get(`/api/v1/comment/${commentId}/`)
        return response.data.replies
    }

    async function createComment(data) {
        await api.post(`/api/v1/comment/`, data)
    }

    return {
        comments,
        loading,
        totalCount,
        currentPage,
        orderField,
        orderDir,
        fetchComments,
        fetchReplies,
        setOrdering,
        createComment
    }
})

export default useCommentsStore
